# Installation and Configuration

Check the [repository](https://github.com/giuseppefilippone/fuzzy_dl_owl2/). The library is available on PyPI, so you can install it using pip: `pip install fuzzy-dl-owl2`.

Examples of supported Fuzzy Description Logic Constructs

| Python Class         | Description                       |
|----------------------|-----------------------------------|
| AtomicConcept        | Define an atomic concept          |
| ChoquetIntegral      | Define a choquet integral concept |
| ApproximationConcept | Define a tight/upper/* lower/upper approximation concept |

## Configuration of the MILP solver

For the configuration, create a `CONFIG.ini` file in the same directory used for the execution of the library.
Example of your execution directory:
```text
your_directory
├── CONFIG.ini
├── your_file.py
```

The file `CONFIG.ini` is structured as follows:
```text
[DEFAULT]
debugPrint = False
epsilon = 0.001
maxIndividuals = -1
owlAnnotationLabel = fuzzyLabel
milpProvider = mip
```

| Configuration Variable | Description                       |
|----------------------|-----------------------------------|
| debugPrint        | Enable/disable debugging          |
| epsilon | Define the precision of the solution. For instance, epsilon = 0.001 means that the solution will be calculated with an accuracy to the third decimal place |
| maxIndividuals | Define the maximal number of individuals to handle. The value $-1$ indicates that there is no maximum |
| owlAnnotationLabel | Define the Annotation label used to build the Fuzzy OWL 2 RDF/XML ontology |
| milpProvider | Define the MILP provider used by the reasoner. The supported providers are listed below. |

Supported MILP Providers:
| Provider | milpProvider |
|--------------|----------------------|
| Gurobi | gurobi |
| CPLEX | pulp_cplex |
| CBC | pulp |
| GLPK | pulp_glpk |
| HiGHS | pulp_highs |
| MIP | mip |

## MILP Provider Usage and Configuration

### GUROBI

- Install [gurobipy](https://pypi.org/project/gurobipy/): `pip install gurobipy==12.0.0`
- Download the GUROBI license from their [website](https://www.gurobi.com/solutions/licensing/).
- Add Gurobi to the PATH

### MIP

- Install Python [MIP](https://www.python-mip.com/): `pip install mip==1.16rc0`

### GLPK

- Install [GLPK](https://www.gnu.org/software/glpk/) v5.0 and [GMP](https://gmplib.org/) v6.3.0
- Install Python [pulp](https://github.com/coin-or/PuLP?tab=readme-ov-file): `pip install pulp==3.2.1`
- Add GLPK to the PATH

### CBC

- Install [CBC](https://github.com/coin-or/Cbc)
- Install Python [pulp](https://github.com/coin-or/PuLP?tab=readme-ov-file): `pip install pulp==3.2.1`
- Add CBC to the PATH

### CPLEX

- Install [CPLEX](https://www.ibm.com/it-it/products/ilog-cplex-optimization-studio) v22.11
- Install Python [pulp](https://github.com/coin-or/PuLP?tab=readme-ov-file): `pip install pulp==3.2.1`
- Add CPLEX to the PATH

### HiGHS

- Install [HiGHS](https://ergo-code.github.io/HiGHS/dev/interfaces/cpp/) v1.10.0
- Install python [pulp](https://github.com/coin-or/PuLP?tab=readme-ov-file): `pip install pulp==3.2.1`
- Add HiGHS to the PATH

## Optional: Compile the Fast Parser

The legacy `DLParser` class (module `fuzzy_dl_owl2.fuzzydl.parser.dl_parser`)
uses [pyparsing](https://github.com/pyparsing/pyparsing) to interpret FuzzyDL
source files. For large knowledge bases this can dominate end-to-end runtime. A
drop-in alternative is provided as `DLParserFast` (module
`fuzzy_dl_owl2.fuzzydl.parser.dl_parser_fast`), which uses a hand-rolled
tokenizer plus a deterministic single-pass recursive-descent parser. The grammar
accepted is identical and every semantic action of the original parser is reused
unchanged, so the resulting `KnowledgeBase` and query list are byte-equivalent.

`DLParserFast` is already 5-10x faster than `DLParser` when imported as pure
Python (no backtracking, no packrat cache, no bounded-recursion bookkeeping).
When the native extensions are compiled, tokenization runs in a C scanner and
the hot-path modules are Cythonized, adding a further 2-3x speedup on the
tokenize and dispatch hot path.

### Build dependencies

Compilation is driven by `build.py` at the repository root, declared in
`pyproject.toml` as a Poetry build hook (`[tool.poetry.build] script = "build.py"`).
The build-system requirements are listed there and are installed automatically
when the package is built:

```text
cython>=3.0
setuptools>=70.0
cffi>=1.16
```

In addition you need:

* A working C compiler (Xcode Command Line Tools on macOS, `build-essential` on
  Debian/Ubuntu, MSVC Build Tools on Windows).
* A lexer generator on `PATH` to build the C tokenizer (see below). If none is
  found, `build.py` skips the C scanner and the parser falls back to its
  pure-Python tokenizer.

### Lexer backend: re2c or flex

The C tokenizer is generated from a single master table (`generate.py`) into one
of two equivalent scanner backends:

* [re2c](https://re2c.org/) &rarr; `lexer_re2c.re` (preferred).
* [flex](https://github.com/westes/flex) &rarr; `lexer_flex.l` (fallback).

At build time `build.py` first tries `re2c`; if it is not on `PATH`, it tries
`flex`. The corresponding scanner source (`lexer_re2c.re` or `lexer_flex.l`) is
(re)generated by `build.py` automatically from `generate.py`, so only the tool
itself needs to be installed. Both backends produce the same token stream, so
install whichever is available:

```bash
# macOS (Homebrew)
brew install re2c        # or: brew install flex

# Debian/Ubuntu
sudo apt install re2c    # or: sudo apt install flex
```

On Windows, install one of the generators and make sure it is on `PATH`:

```powershell
# re2c
choco install re2c       # Chocolatey
scoop install re2c       # or Scoop

# flex (win_flex.exe — expose it as `flex` on PATH)
choco install winflexbison3
```

> On Windows the flex distribution ships the executable as `win_flex.exe`. Add a
> `flex` alias (or copy/rename it to `flex.exe`) on `PATH` so `build.py` can
> invoke it. Preferring re2c avoids this extra step.

### Building the native extensions

The extensions are compiled in place whenever the package is built from source:

```bash
pip install .
# or
poetry build
```

`build.py` cythonizes the hot-path modules and, when re2c or flex is available,
builds the C tokenizer extensions (`_fdl_lexer` via CFFI and `_fdl_tuples` via
Cython) inside `fuzzy_dl_owl2/fuzzydl/parser/tokenizer/`. The resulting `.so`
(or `.pyd` on Windows) files sit next to the Python sources; Python automatically
prefers a compiled module when both files are present, so no further
configuration is required.

### Using DLParserFast

`DLParserFast` exposes the same public API as `DLParser` (`get_kb`, `main`,
`parse_string`, `parse_string_opt`, `load_config`). Swap the import to opt in:

```python
from fuzzy_dl_owl2.fuzzydl.parser import DLParserFast as DLParser

DLParser.main("example.fdl")
```

If the compilation step is skipped, importing `DLParserFast` still works and uses
the pure-Python implementation.