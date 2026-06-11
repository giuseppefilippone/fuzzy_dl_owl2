from __future__ import annotations

import argparse
import os
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


from fuzzy_dl_owl2.fuzzydl.milp.solution import Solution
from fuzzy_dl_owl2.fuzzydl.parser import DLParserFast as DLParser
from fuzzy_dl_owl2.fuzzydl.util import constants
from fuzzy_dl_owl2.fuzzydl.util.config_reader import ConfigReader

PROVIDER_MAP = {
    "gurobi": constants.MILPProvider.GUROBI,
    "mip": constants.MILPProvider.MIP,
    "cbc": constants.MILPProvider.PULP,
    "cplex": constants.MILPProvider.PULP_CPLEX,
    "glpk": constants.MILPProvider.PULP_GLPK,
    "highs": constants.MILPProvider.PULP_HIGHS,
}


def run(provider: str, file_path: str) -> list[str | None]:
    solutions: list[Solution] = []
    # t0 = time.perf_counter()
    # profiler = cProfile.Profile()
    # profiler.enable()
    results = DLParser.main(
        str(file_path),
        debugPrint=False,
        milpProvider=PROVIDER_MAP.get(provider.lower(), constants.MILPProvider.GUROBI),
    )
    # profiler.disable()
    # t1 = time.perf_counter()
    print(f"Debugging: {ConfigReader.DEBUG_PRINT}")
    print(f"Provider: {ConfigReader.MILP_PROVIDER}")
    # pstats.Stats(profiler).strip_dirs().sort_stats("tottime").print_stats(20)
    for query, solution in results.items():
        solutions.append(f"{query}{solution}")
    # print(f"Processing completed in {t1 - t0:.2f} seconds.")
    return solutions


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Run processing for a provider and file path."
    )

    parser.add_argument(
        "help",
        action="store_true",
        help="Usage: python run_queries.py <provider> <file_path>",
    )

    parser.add_argument(
        "provider",
        type=str,
        default="gurobi",
        help="Provider name, e.g. gurobi, mip, cbc, cplex, glpk, highs",
    )

    parser.add_argument(
        "file_path",
        type=str,
        help="Path to the input file",
    )

    args = parser.parse_args()

    results = run(
        provider=args.provider,
        file_path=args.file_path,
    )
    print("\n".join(results))
