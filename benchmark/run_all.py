"""
Benchmark script for FuzzyDL reasoner MILP solver providers.

Usage:
    python benchmark/benchmark.py

Runs every ``.txt`` file in ``benchmark/data/`` with every available MILP
provider, measuring the average wall-clock time of the ``(sat?)`` query.
Results are persisted as JSON and can be plotted or exported to LaTeX.
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

# DLParser.load_config() reads CONFIG.ini from os.getcwd(); pin cwd to the
# script directory so it does not depend on where the user invokes Python from.
os.chdir(Path(__file__).resolve().parent)

# add project root to sys.path so we can import modules for benchmarking; this allows us to run the benchmark script from its own directory without worrying about the current working directory or PYTHONPATH, and it ensures we are testing the actual code in the project rather than accidentally importing from a different location; we use Path for cross-platform path handling and to make it clear that this is a filesystem path rather than a module import; we resolve the path to ensure it's absolute and avoid any issues with relative paths or symlinks; we append to sys.path rather than inserting at the front to avoid accidentally shadowing any standard library modules or other dependencies, while still ensuring our project modules are available for import; this is a common pattern for scripts that need to import from the project but may be run from different locations or environments, and it helps keep the script self-contained and easy to run without additional setup
SYS_PATH = Path(__file__).resolve().parent.parent
# Insert at front so the local checkout shadows any pip-installed
# fuzzy_dl_owl2 in site-packages. Appending lets site-packages win.
if str(SYS_PATH) in sys.path:
    sys.path.remove(str(SYS_PATH))
sys.path.insert(0, str(SYS_PATH))


import datetime
import json
import logging
import statistics
import time
import typing

import tqdm

from fuzzy_dl_owl2.fuzzydl.util import constants

# set up logging for benchmark progress and results; this will include info-level logs for overall progress and timing, as well as warnings for any issues encountered during runs (e.g. timeouts, inconsistent solutions, etc.); we will log to console for real-time feedback during the benchmark run, and we will log failures to a separate file for later analysis
DIR_PATH = Path(__file__).resolve().parent / "logs" / "python"
DIR_PATH.mkdir(parents=True, exist_ok=True)
today = datetime.datetime.now()
logger_path: Path = DIR_PATH / f"benchmark_{today.strftime('%Y%m%d_%H%M%S')}.log"
logger_path.unlink(missing_ok=True)  # remove old log file if it exists to start fresh

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(), logging.FileHandler(logger_path)],
)
logger = logging.getLogger("benchmark")


# set up paths for knowledge base files and failures log; ensure failures directory exists
DATA_DIR = Path(__file__).resolve().parent / "data"
RESULTS_DIR = Path(__file__).resolve().parent / "results"
RESULTS_DIR.mkdir(exist_ok=True)

# === Constants for benchmark configuration ===

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

_ALL_PROVIDERS = list(constants.MILPProvider)
# # subset of providers to benchmark to reduce runtime
_ALL_PROVIDERS = [
    constants.MILPProvider.GUROBI,
    constants.MILPProvider.PULP,
    constants.MILPProvider.PULP_HIGHS,
]
PROVIDER_RENAME = {
    constants.MILPProvider.GUROBI: "Gurobi",
    constants.MILPProvider.MIP: "MIP",
    constants.MILPProvider.PULP: "CBC",
    constants.MILPProvider.PULP_CPLEX: "CPLEX",
    constants.MILPProvider.PULP_GLPK: "GLPK",
    constants.MILPProvider.PULP_HIGHS: "HiGHS",
}


def _find_cplex_executable() -> typing.Optional[str]:
    """Locate the CPLEX command-line binary across macOS, Linux, and Windows.

    Resolution order: PATH lookup, CPLEX-specific env vars, then platform-specific
    install-directory globs.
    """
    import glob
    import os
    import platform
    import shutil

    system = platform.system()
    exe_name = "cplex.exe" if system == "Windows" else "cplex"
    found = shutil.which(exe_name)
    if found:
        return found

    for env_var in ("CPLEX_STUDIO_BINARIES", "CPLEX_HOME", "CPLEX_STUDIO_DIR"):
        base = os.environ.get(env_var)
        if not base:
            continue
        candidates = glob.glob(os.path.join(base, "**", exe_name), recursive=True)
        if candidates:
            return sorted(candidates)[-1]

    if system == "Darwin":
        patterns = ["/Applications/CPLEX_Studio*/cplex/bin/*/cplex"]
    elif system == "Windows":
        patterns = [
            r"C:\Program Files\IBM\ILOG\CPLEX_Studio*\cplex\bin\*\cplex.exe",
            r"C:\Program Files (x86)\IBM\ILOG\CPLEX_Studio*\cplex\bin\*\cplex.exe",
        ]
    else:
        patterns = [
            "/opt/ibm/ILOG/CPLEX_Studio*/cplex/bin/*/cplex",
            "/opt/CPLEX_Studio*/cplex/bin/*/cplex",
            os.path.expanduser("~/CPLEX_Studio*/cplex/bin/*/cplex"),
        ]

    for pattern in patterns:
        matches = sorted(glob.glob(pattern))
        if matches:
            return matches[-1]

    return None


def _provider_available(provider: constants.MILPProvider) -> bool:
    """Check whether a MILP provider can be instantiated without error."""
    if provider in (constants.MILPProvider.PULP_CPLEX,):
        try:
            import pulp

            cplex_path = _find_cplex_executable()
            if cplex_path is None or not pulp.CPLEX_CMD(path=cplex_path).available():
                return False
        except Exception:
            return False
    if provider == constants.MILPProvider.GUROBI:
        try:
            import gurobipy
        except Exception:
            return False
    if provider == constants.MILPProvider.MIP:
        try:
            import mip
        except Exception:
            return False
    return True


def benchmark_file(
    fdl_path: Path,
    providers: typing.Optional[list[constants.MILPProvider]] = None,
    num_runs: int = DEFAULT_RUNS,
) -> dict[str, dict[str, float]]:
    """
    Benchmark a single FDL file across all (available) MILP providers.

    :param fdl_path: Path to the FuzzyDL text file.
    :param providers: Subset of MILPProvider to test; defaults to all available.
    :param num_runs: Number of timed executions per provider.
    :param warmup_runs: Number of untimed warmup executions before timing.
    :return: Mapping provider_name -> {avg, std, min, max, total, runs}.
    """
    if providers is None:
        providers = [p for p in _ALL_PROVIDERS if _provider_available(p)]

    results: dict[str, dict[str, float]] = {}

    for provider in providers:
        provider_name = PROVIDER_RENAME.get(provider, provider.name.lower())

        # _reload_modules()

        # counter for consecutive failures; if too many, skip remaining runs for this provider
        fails: int = 0
        # list of successful run times for this provider; if too many failures, these will be discarded as unreliable
        times: list[float] = []

        # runs are performed in a separate process with timeout to prevent hangs and ensure clean state between runs
        for _ in tqdm.tqdm(
            range(num_runs),
            desc=f"Runs for {fdl_path.name} - Provider: {provider_name}",
            unit="run",
        ):
            if MAX_RUNS_FAILURE > 0 and fails >= MAX_RUNS_FAILURE:
                # too many failures – likely indicates a problem with this provider on this file; skip remaining runs and discard times as unreliable
                logger.warning(
                    f"{fails} consecutive failures for {fdl_path.name} with {provider_name}. Skipping provider."
                )
                break

            t0 = time.perf_counter()
            try:
                output = subprocess.run(
                    [
                        sys.executable,
                        "run_queries.py",
                        provider_name,
                        str(fdl_path),
                    ],
                    check=True,
                    text=True,
                    capture_output=True,
                    timeout=MAX_MINUTES_PER_RUN * 60,
                )
            except subprocess.TimeoutExpired:
                logger.warning(
                    f"Timeout expired for {fdl_path.name} with {provider_name}"
                )
                fails += 1
                continue

            t1 = time.perf_counter()
            logger.info(
                f"Output for {fdl_path.name} with {provider_name}:\n{output.stdout}".strip()
            )
            logger.info(
                f"Run completed for {fdl_path.name} with {provider_name} in {t1 - t0:.4f} seconds"
            )
            if "None" in output.stdout:
                logger.warning(
                    f"Solution is None for {fdl_path.name} with {provider_name}"
                )
                fails += 1
                continue

            # successful run
            times.append(t1 - t0)

        if not times:
            # no successful runs for this provider on this file; skip stats and continue to next provider
            logger.warning(
                f"No successful runs for {fdl_path.name} with {provider_name}. Skipping stats."
            )
            results[provider_name] = {}
            continue

        # compute stats for this provider on this file
        results[provider_name] = {
            "avg": statistics.mean(times),
            "std": statistics.stdev(times) if len(times) > 1 else 0.0,
            "min": min(times),
            "max": max(times),
            "total": sum(times),
            "runs": len(times),
        }
        logger.info(f"avg={results[provider_name]['avg']:.4f}s")

    return results


def run_benchmark(
    data_dir: Path = DATA_DIR,
    results_dir: Path = RESULTS_DIR,
    num_runs: int = DEFAULT_RUNS,
    providers: typing.Optional[list[constants.MILPProvider]] = None,
) -> dict:
    """
    Run the full benchmark suite.

    :return: Nested dict {filename: {provider_name: stats}}.
    """

    # get list of .txt files to benchmark
    fdl_files = sorted(data_dir.glob("*.txt"))
    if not fdl_files:
        # no files to benchmark – raise error
        raise FileNotFoundError(f"No .txt files found in {data_dir}")

    if providers is None:
        # list of providers to benchmark, filtered by availability; if none are available, raise error
        providers = sorted([p for p in _ALL_PROVIDERS if _provider_available(p)])

    logger.info(
        f"Benchmarking {len(fdl_files)} file(s) × {len(providers)} provider(s) x {num_runs} runs"
    )

    # worst-case expected time is if every run for every provider on every file hits the timeout limit; log this so we have an idea of how long the benchmark may take in the worst case
    expected_time: float = (
        len(fdl_files) * len(providers) * num_runs * MAX_MINUTES_PER_RUN
    )
    # convert to human-readable format
    expected_time_str = str(datetime.timedelta(minutes=expected_time))
    logger.info(f"Expected worst-case runtime: {expected_time_str}")

    min_expected_time: float = (
        len(fdl_files) * len(providers) * MAX_RUNS_FAILURE * MAX_MINUTES_PER_RUN
    )
    min_expected_time_str = str(datetime.timedelta(minutes=min_expected_time))
    logger.info(
        f"Expected minimum runtime (if all files fail after max failures): {min_expected_time_str}"
    )

    # nested dict to hold all results; structure: {filename: {provider_name: stats_dict}}
    all_results: dict[str, dict[str, dict[str, float]]] = {}
    # output JSON file for results
    out_json = results_dir / "benchmark_results.json"

    # load previously saved results if they exist, to avoid re-running files that have already been benchmarked; this allows resuming an interrupted benchmark run without losing progress
    if out_json.exists():
        with open(out_json, "r") as f:
            all_results = json.load(f)
        logger.info(
            f"Loaded previously saved results for {len(all_results)} files from {out_json.name}."
        )

    files_to_skip: set[str] = set()
    files_to_skip_path = results_dir / "python_skip.json"
    if files_to_skip_path.exists():
        with open(files_to_skip_path, "r") as f:
            skip_data = json.load(f)
            files_to_skip = set(skip_data.get("files", []))
        logger.info(
            f"Loaded list of files to skip for Python benchmark: {files_to_skip}"
        )

    # benchmark each file and store results, saving intermediate results to JSON after each file to ensure progress is not lost if the script is interrupted
    for fdl_path in fdl_files:
        logger.info(f"File: {fdl_path.name}")
        if fdl_path.name not in files_to_skip:
            logger.info(
                f"Skipping {fdl_path.name} based on skip list loaded from {files_to_skip_path.name}."
            )
            continue
        if fdl_path.name in all_results:
            logger.info(
                f"Results for {fdl_path.name} already exist, skipping. To rerun, delete the entry from {out_json.name}."
            )
            continue

        # benchmark this file across providers and store results
        all_results[fdl_path.name] = benchmark_file(
            fdl_path, providers=providers, num_runs=num_runs
        )
        if all(len(s) for s in all_results[fdl_path.name].values()) == 0:
            logger.warning(
                f"All providers failed for {fdl_path.name}. Results may be unreliable."
            )
            continue

        # persist JSON
        with open(out_json, "w") as f:
            json.dump(all_results, f, indent=2, sort_keys=True)
        logger.info(f"Results written to {out_json.name}")

    logger.setLevel(logging.INFO)
    return all_results


if __name__ == "__main__":
    # quick smoke test with 3 runs; override DEFAULT_RUNS for full 1000-run benchmark
    NUM_RUNS = int(os.environ.get("BENCHMARK_RUNS", DEFAULT_RUNS))
    results = run_benchmark(num_runs=NUM_RUNS)
