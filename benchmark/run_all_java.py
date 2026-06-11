import datetime
import json
import logging
import statistics
import subprocess
import time
from pathlib import Path

import tqdm

# set up logging for benchmark progress and results; this will include info-level logs for overall progress and timing, as well as warnings for any issues encountered during runs (e.g. timeouts, inconsistent solutions, etc.); we will log to console for real-time feedback during the benchmark run, and we will log failures to a separate file for later analysis
today = datetime.datetime.now()
DIR_PATH = Path(__file__).resolve().parent / "logs" / "java"
DIR_PATH.mkdir(parents=True, exist_ok=True)
logging_path: Path = DIR_PATH / f"benchmark_{today.strftime('%Y-%m-%d_%H-%M-%S')}.log"
logging_path.unlink(missing_ok=True)  # remove old log file if it exists to start fresh
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(), logging.FileHandler(logging_path)],
)
logger = logging.getLogger(__name__)


# set up paths for knowledge base files and failures log; ensure failures directory exists
DATA_DIR = Path(__file__).resolve().parent / "data"
RESULTS_DIR = Path(__file__).resolve().parent / "results"
RESULTS_DIR.mkdir(exist_ok=True)

# number of runs per provider per file
DEFAULT_RUNS = 10
# max consecutive failures before giving up on a provider for a file; this is to prevent spending too much time on providers that are consistently failing on a file, while still allowing for some failures due to variability or instability without completely discarding the provider's results for that file
MAX_RUNS_FAILURE = (
    1  # max runs per provider before giving up on that provider for this file
)
# max minutes per run before killing the process and counting as failure; this is to prevent hanging indefinitely on runs that are taking too long, while still allowing for longer runtimes on harder files without prematurely killing them
MAX_MINUTES_PER_RUN = (
    20  # max minutes per run before killing the process and counting as failure
)


def run_file_with_fdl(filepath: Path) -> dict[str, float] | None:
    """
    Run the given .txt file with fuzzDL and return a list of successful run times in seconds.

    If a run fails (e.g. due to timeout or error), it will be counted as a failure but not included in the times list. If the number of failures reaches MAX_RUNS_FAILURE, the function will stop running and return the times collected so far, which may be empty if all runs failed.

    Note: this function assumes that the run_fdl.sh script is set up to run fuzzDL on the given file and that it outputs timing information in the format produced by /usr/bin/time -p, which includes lines like "real 12.34". The function captures this output to extract the timing information.
    """

    # list to store successful run times
    times: list[float] = []
    # counter for consecutive failures
    fails: int = 0
    logger.info(f"Running {filepath.name} with fuzzDL...")
    # use tqdm to show progress and allow early exit on too many failures
    for _ in tqdm.tqdm(range(DEFAULT_RUNS), desc=f"Runs for {filepath.name}"):
        if MAX_RUNS_FAILURE > 0 and fails >= MAX_RUNS_FAILURE:
            # too many failures – likely indicates a problem with this provider on this file; skip remaining runs and discard times as unreliable
            logger.warning(
                f"Too many failures for {filepath} ({fails} failures), skipping remaining runs."
            )
            times = []  # remove times for this file since it's not reliable
            break
        try:
            # run the fuzzDL script with timing and capture output
            t0 = time.perf_counter()
            r = subprocess.run(
                ["./run_fdl.sh", f"./{filepath}"],
                check=True,
                timeout=MAX_MINUTES_PER_RUN * 60,  # convert minutes to seconds
                capture_output=True,
                text=True,
            )
            t1 = time.perf_counter()
            logger.info(r.stdout.strip())
            if (
                "Is KnowledgeBase satisfiable?" not in r.stdout
                and "KnowledgeBase inconsistent" not in r.stdout
            ):
                # if the expected success message is not in stdout, count as failure
                logger.warning(
                    f"Expected success message not found in stdout for {filepath.name}, counting as failure."
                )
                fails += 1
                continue
            wall: float = t1 - t0
            logger.info(f"Finished in {wall:.2f} seconds.")
            if wall == 0.0:
                logger.warning(
                    f"Could not extract timing information for {filepath.name}, counting as failure."
                )
                fails += 1
                continue
            # successful run
            times.append(wall)
        except subprocess.TimeoutExpired:
            # timeout for this run – skip timing but count as failure
            logger.warning(f"Timeout expired for {filepath.name}, skipping.")
            fails += 1
        except subprocess.CalledProcessError as e:
            # error during execution – skip timing but count as failure
            logger.warning(f"Error running {filepath.name}: {e}")
            logger.warning(e.stdout)
            # if e.stderr:
            #     logger.warning(e.stderr)
            fails += 1

    if not times:
        logger.warning(f"No successful runs for {filepath.name}, skipping stats.")
        return {}

    results = {
        "avg": statistics.mean(times),
        "std": statistics.stdev(times) if len(times) > 1 else 0.0,
        "min": min(times),
        "max": max(times),
        "total": sum(times),
        "runs": len(times),
    }
    logger.info(f"avg={results['avg']:.4f}s")
    return results


def run_all(
    kb_dir: Path = DATA_DIR,
    results_dir: Path = RESULTS_DIR,
) -> None:
    """Run all .txt files in the given directory with fuzzDL."""

    # get list of .txt files to benchmark
    fdl_files = sorted(kb_dir.glob("*.txt"))
    if not fdl_files:
        # no files to benchmark – raise error
        raise FileNotFoundError(f"No .txt files found in {kb_dir}")

    logger.info(f"Benchmarking {len(fdl_files)} file(s) x {DEFAULT_RUNS} runs")

    # worst-case expected time is if every run for every provider on every file hits the timeout limit; log this so we have an idea of how long the benchmark may take in the worst case
    expected_time: float = len(fdl_files) * DEFAULT_RUNS * MAX_MINUTES_PER_RUN
    # convert to human-readable format
    expected_time_str = str(datetime.timedelta(minutes=expected_time))
    logger.info(f"Expected worst-case runtime: {expected_time_str}")

    min_expected_time: float = len(fdl_files) * MAX_RUNS_FAILURE * MAX_MINUTES_PER_RUN
    min_expected_time_str = str(datetime.timedelta(minutes=min_expected_time))
    logger.info(
        f"Expected minimum runtime (if all files fail after max failures): {min_expected_time_str}"
    )

    # dictionary to store results for each file
    all_results: dict[str, dict[str, float]] = {}
    # output JSON file for results
    out_json = results_dir / "java_benchmark_results.json"

    if out_json.exists():
        with open(out_json, "r") as f:
            all_results = json.load(f)
        logger.info(
            f"Loaded previously saved results for {len(all_results)} files from {out_json.name}."
        )

    files_to_skip: set[str] = set()
    files_to_skip_path = results_dir / "java_skip.json"
    if files_to_skip_path.exists():
        with open(files_to_skip_path, "r") as f:
            skip_data = json.load(f)
            files_to_skip = set(skip_data.get("files", []))
        logger.info(f"Loaded list of files to skip for Java benchmark: {files_to_skip}")

    # run each .txt file in the directory with fuzzDL and collect times
    for kb_file in fdl_files:
        # get the relative path of the file for better logging and results keys
        filepath = kb_file.relative_to(kb_dir.parent)
        if filepath.name in files_to_skip:
            logger.info(
                f"Skipping {filepath.name} based on skip list loaded from {files_to_skip_path.name}."
            )
            continue
        if filepath.name in all_results:
            logger.info(
                f"Results for {filepath.name} already exist, skipping. To rerun, delete the entry from {out_json.name}."
            )
            continue

        # run the file with fuzzDL and get the list of successful run times in seconds; store the results in the dictionary under the relative file path as key
        all_results[filepath.name] = run_file_with_fdl(filepath)

        # save intermediate results to JSON after each file to ensure progress is not lost if the script is interrupted
        with open(out_json, "w") as f:
            json.dump(all_results, f, indent=2, sort_keys=True)


if __name__ == "__main__":
    run_all(DATA_DIR, RESULTS_DIR)
