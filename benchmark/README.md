# Benchmarks

Performance harness for the `fuzzy_dl_owl2` reasoner. It runs a corpus of
fuzzy-DL knowledge bases through the Python port across several MILP solver
providers, runs the **same** corpus through the original Java fuzzyDL reasoner
(the oracle), and produces a side-by-side LaTeX comparison table.

## Layout

| Path | What it is |
|---|---|
| `data/` | 61 fuzzy-DL knowledge bases (`*.txt`, fuzzyDL syntax). The benchmark corpus. |
| `owl/` | The same ontologies in OWL 2 form (`*.owl`). |
| `results/` | Generated JSON results and the solver model dumps. |
| `logs/python/`, `logs/java/` | Timestamped run logs (one file per invocation). |
| `lib/`, `fuzzydl.jar` | Java oracle classpath (owlapi, gurobi, jung, junit, …). |
| `CONFIG` | Java reasoner config (`fuzzydl.parser.Parser` reads it from cwd). |

## Scripts

| Script | Role |
|---|---|
| `run_queries.py <provider> <file>` | Single run: solve one KB with one provider. The building block the harness shells out to. |
| `run_all.py` | Python benchmark. Every `data/*.txt` × every available provider × N runs → `results/benchmark_results.json`. |
| `run_all_java.py` | Java benchmark. Shells out to `run_fdl.sh` per file → `results/java_benchmark_results.json`. |
| `run_fdl.sh <file>` | Runs the Java oracle (`fuzzydl.jar`) on one file. Hardcoded to Gurobi. |
| `create_latex_table.py` | Merges the two JSON result files → `benchmark_table.tex`. |
| `test_run.py` | Smoke test: invokes `run_queries.py` on a single KB and times it. |

Providers accepted by `run_queries.py` / `PROVIDER_MAP`:
`gurobi`, `mip`, `cbc` (PuLP+CBC), `cplex`, `glpk`, `highs`.

## Prerequisites

- **Python**: project installed (`poetry install` from the repo root). At least
  one MILP solver. CBC and HiGHS ship with PuLP; Gurobi and CPLEX need a local
  install + license. `run_all.py` auto-detects which providers are available
  and skips the rest.
- **Java oracle** (only for `run_all_java.py` / `run_fdl.sh`): a JDK, `fuzzydl.jar`
  and `lib/` present here, and Gurobi. Set `GUROBI_HOME` (the script also probes
  `/Library/gurobi*` and `/opt/gurobi*`) and `GRB_LICENSE_FILE`
  (defaults to `~/gurobi.lic`).

## Running

All scripts `chdir` to this directory, so run them from anywhere.

### One KB, one provider
```bash
python run_queries.py gurobi ./data/FuzzyWine.txt
```

### Full Python benchmark
```bash
python run_all.py                 # DEFAULT_RUNS (10) per provider per file
BENCHMARK_RUNS=1000 python run_all.py   # full statistical run
```
Behavior worth knowing:
- **Resumable.** Results are written to `results/benchmark_results.json` after
  each file; a KB already present there is skipped. To re-run a KB, delete its
  entry from that JSON.
- **Skip list.** `results/python_skip.json` (`{"files": [...]}`) controls which
  files are processed.
- **Timeout / failures.** Each run is killed after `MAX_MINUTES_PER_RUN` (20 min)
  and counts as a failure; `MAX_RUNS_FAILURE` (1) consecutive failures abandon a
  provider for that file.
- **Providers.** Edit `_ALL_PROVIDERS` in `run_all.py` to change the set
  (default: Gurobi, CBC, HiGHS).

### Full Java benchmark
```bash
python run_all_java.py            # writes results/java_benchmark_results.json
```
Uses `results/java_skip.json` as its skip list; otherwise mirrors the Python run.

### Comparison table
```bash
python create_latex_table.py      # reads both *_results.json → benchmark_table.tex
```
Both JSON files must exist. Reports per-KB Java vs. fastest-Python timings,
speedup count, and aggregate stats.

### KB statistics
```bash
python kb_statistics.py
```

## Result format

`benchmark_results.json` is `{filename: {provider_name: stats}}`; the Java file
is `{filename: stats}`. Provider display names: `Gurobi`, `MIP`, `CBC`,
`CPLEX`, `GLPK`, `HiGHS`.

## Typical workflow

1. `python run_all.py` — Python side.
2. `python run_all_java.py` — oracle side.
3. `python create_latex_table.py` — comparison table.

Java is the oracle: where the two disagree, the Java result is correct.