# Architecture

How the reasoner turns an FDL knowledge base into an answer. The pipeline has
four stages: **parse** -> **knowledge base** -> **MILP encoding** ->
**solver dispatch**. This page is a conceptual map of the `fuzzydl` package; for
the public how-to see [Usage](usage.md).

## Pipeline overview

:::{only} html
```text
 .fdl source
     |  DLParser / DLParserFast
     v
 KnowledgeBase  --(axioms, assertions, TBox)
     |  kb.solve_kb()      preprocess once
     v
 tableau expansion  --(lazy unfolding of concepts/roles into constraints)
     |  via MILPHelper
     v
 MILP model  (Variable / Term / Expression / Inequation)
     |  query.solve(kb) -> MILPHelper.optimize(objective)
     v
 solver backend  (Gurobi | MIP | PuLP: CBC/GLPK/HiGHS/CPLEX)
     |
     v
 Solution
```
:::

:::{only} latex
```{raw} latex
\begin{center}
\begin{tikzpicture}[
    node distance=6mm and 0mm,
    every node/.style={font=\small},
    stage/.style={
        draw, rounded corners, fill=blue!5,
        align=center, inner sep=4pt,
        text width=0.62\linewidth,
    },
    note/.style={font=\footnotesize\itshape, text=black!55},
    arrow/.style={-{Stealth[length=2.4mm]}, thick},
]
    \node[stage] (src)    {\texttt{.fdl} source};
    \node[stage, below=of src] (kb)
        {\textbf{KnowledgeBase}\\ \footnotesize ABox + TBox (axioms, assertions)};
    \node[stage, below=of kb] (tab)
        {Tableau expansion\\ \footnotesize lazy unfolding of concepts / roles into constraints};
    \node[stage, below=of tab] (milp)
        {MILP model\\ \footnotesize Variable / Term / Expression / Inequation};
    \node[stage, below=of milp] (solver)
        {Solver backend\\ \footnotesize Gurobi $\mid$ MIP $\mid$ PuLP: CBC / GLPK / HiGHS / CPLEX};
    \node[stage, below=of solver] (sol) {\textbf{Solution}};

    \draw[arrow] (src)    -- node[right, note] {\;DLParser / DLParserFast} (kb);
    \draw[arrow] (kb)     -- node[right, note] {\;kb.solve\_kb() --- preprocess once} (tab);
    \draw[arrow] (tab)    -- node[right, note] {\;via MILPHelper} (milp);
    \draw[arrow] (milp)   -- node[right, note] {\;query.solve(kb) $\to$ optimize(objective)} (solver);
    \draw[arrow] (solver) -- (sol);
\end{tikzpicture}
\end{center}
```
:::

## 1. Parsing

`DLParser` (pyparsing) or `DLParserFast` (hand-rolled tokenizer +
recursive-descent; see *Optional: Compile the Fast Parser* in
[Installation and Configuration](install_and_config.md)) reads the source and
populates two class-level fields shared by both implementations:

* `DLParser.kb` — a `KnowledgeBase` being filled with concepts, axioms, and
  assertions.
* `DLParser.queries_list` — the parsed [queries](queries.md).

`get_kb(path)` returns `(kb, queries)`.

## 2. KnowledgeBase

`fuzzy_dl_owl2.fuzzydl.knowledge_base.KnowledgeBase` is the central object (the
single largest module). It stores the ABox (assertions about individuals) and
TBox (concept/role axioms) and owns a `MILPHelper` instance (`self.milp`).

`kb.solve_kb()` performs one-time preprocessing before any query runs:

* defaults the semantics to Łukasiewicz if none was set;
* computes the description-logic language of the KB;
* interns symbolic strings to integers for speed;
* resolves role axioms — inverse, role-inclusion, reflexive, functional;
* preprocesses the TBox and computes the blocking strategy;
* marks the KB loaded (`KB_LOADED = True`).

After this, each query reasons against the prepared KB.

## 3. Tableau to MILP encoding

Reasoning is **tableau-style** but the branching is replaced by **constraints**:
each logical construct is *lazily unfolded* into rows of a Mixed-Integer Linear
Program rather than expanded into an explicit completion tree. The unfolding
rules live on `KnowledgeBase` (e.g. `solve_gci`, `solve_lukasiewicz_gci`,
`rule_domain_lazy_unfolding`, ...) and emit constraints through the MILP layer.

### The MILP class hierarchy

The model is built from four classes in `fuzzy_dl_owl2.fuzzydl.milp`:

| Class | Role |
|---|---|
| `Variable` | A decision variable. Its `VariableType` is one of `BINARY`, `CONTINUOUS`, `INTEGER`, `SEMI_CONTINUOUS`. Degrees, role memberships and nominals each become a variable. |
| `Term` | A coefficient times a `Variable` (a `coefficient * Variable` product). |
| `Expression` | A constant plus a sum of `Term`s — a linear expression. |
| `Inequation` | An `Expression` compared against zero with an `InequalityType` (`GREATER_THAN`, `LESS_THAN`, `EQUAL`). |

### MILPHelper

`MILPHelper` is the only sanctioned way to build the model. Key entry points:

* `get_variable(*args)` — the **single** allocator for degree / role / nominal
  variables. It is heavily overloaded (by assertion, relation, individual+concept,
  created individual, ...) so callers ask for the variable that represents a given
  domain entity and get a stable handle back.
* `add_new_constraint(expr, op, degree)` — adds a constraint. Constraints are
  **normalised so the right-hand side is zero**: the helper shifts the
  expression by the `Degree` before storing the `Inequation`.
* `optimize(objective)` — solves the current model for an objective `Expression`
  and returns a `Solution`.

The fuzzy-operator encodings (the t-norm / t-conorm / implication rows for
Łukasiewicz and Zadeh) are produced only by the dedicated solver classes
(`LukasiewiczSolver`, `ZadehSolver`); other code does not inline these.

## 4. Solver dispatch

`MILPHelper.optimize` selects the backend from `ConfigReader.MILP_PROVIDER`:

| `MILP_PROVIDER` | Method | Backend |
|---|---|---|
| `GUROBI` | `solve_gurobi` | Gurobi |
| `MIP` | `solve_mip` | Python-MIP |
| `PULP`, `PULP_GLPK`, `PULP_HIGHS`, `PULP_CPLEX` | `solve_pulp` | PuLP (CBC / GLPK / HiGHS / CPLEX) |

An unrecognised provider raises `ValueError`. The chosen backend also fixes the
numerical limit $k_{\infty}$ (`MAXVAL`) — higher limits accumulate floating-point error,
so each solver gets a tuned value (see the *MILP Solver Constraints* table in
[Grammatics](grammar.md)). Install/config per backend is in
[Installation and Configuration](install_and_config.md).

## 5. Answering a query

A query holds the objective it wants optimised. `query.solve(kb)`:

1. clones the prepared MILP model (so each query is independent);
2. applies any query-specific assertions (e.g. `solve_assertions`);
3. calls `cloned.optimize(self.obj_expr)` to get the optimum;
4. wraps the outcome in a [`Solution`](queries.md).

If the KB is inconsistent, the `Solution` reports `is_consistent_kb() == False`
and every query trivially answers `1.0`.

## Native acceleration

The whole pipeline runs as pure Python, but the hot paths are also shipped as
compiled extensions. When the package is built from source (`pip install .` /
`poetry build`), the `build.py` Poetry hook produces native `.so` (`.pyd` on
Windows) modules in place; Python automatically prefers a compiled module over
its `.py` twin when both are present, so importing is unchanged. If the build
step is skipped, every module falls back to pure Python — same results, lower
speed. See *Optional: Compile the Fast Parser* in
[Installation and Configuration](install_and_config.md) for the toolchain.

### Cython-compiled modules

`build.py` cythonizes the modules that dominate runtime — `knowledge_base`,
`general_concept_inclusion`, `primitive_concept_definition`, `graph/digraph`,
`util/constants`, and everything under `concept/`, `individual/`, `query/`,
`milp/`, and `parser/` (except the pure-data `tokens.py`, `generate.py`,
`tokenizer_handler.py`, and the legacy `dl_parser.py`). They are compiled with
aggressive directives (`boundscheck=False`, `wraparound=False`,
`initializedcheck=False`, `cdivision=True`, `nonecheck=False`, `infer_types=True`)
and `-O3`. PEP 484 annotation enforcement is **off** (`annotation_typing=False`)
so `Optional`/`Union` arguments still accept `None` at the C level. The
extensions are built in place next to their `.py` sources, so the package stays
importable either way.

### C tokenizer (re2c / flex)

The fast parser's tokenizer has a C scanner core, generated from a single master
table (`generate.py`) into one of two equivalent backends:

* `lexer_re2c.re` compiled by [re2c](https://re2c.org/) (preferred), or
* `lexer_flex.l` compiled by [flex](https://github.com/westes/flex) (fallback).

The scanner exposes `fdl_count_tokens` / `fdl_tokenize`, which fill three
`int32` spans per token (kind, start, length) and build **no Python objects** —
the expensive per-token tuple construction is kept out of the C pass. Two
extensions wrap it inside `parser/tokenizer/`:

* **`_fdl_lexer`** — a CFFI wrapper exposing the raw int32-array API used by
  `tokens.py`.
* **`_fdl_tuples`** — a Cython module whose `tokenize_tuples(bytes)` runs both
  scanner passes and emits the `(kind, value, lower, offset)` 4-tuples the
  recursive-descent parser consumes directly, replacing the Python tuple-building
  loop. (`COMMA` is dropped; a trailing EOF sentinel is appended.)

At runtime the tokenizer picks the fastest backend available, in order:

1. **Cython `_fdl_tuples`** — tuples built entirely in C (fastest).
2. **CFFI `_fdl_lexer`** — C scan into int32 arrays, tuples assembled in Python.
3. **Pure-Python regex** (`PythonRegexTokenizer`) — the master regex; always
   available, used when neither extension was built.

`_fdl_ok` reports whether the C backend is importable; large files are streamed
form-by-form (`FdlFileTokenizer`) so peak token memory stays bounded regardless
of backend.

## Performance notes

* `get_kb` / `main` disable Python's cyclic garbage collector during the run:
  KB construction builds a large acyclic object graph with nothing to reclaim
  mid-parse, so the collector would only scan the growing graph repeatedly. It is
  restored afterwards.
* Building the `concept_individual_list` blocking index appends in ascending
  individual-id order, so membership uses an in-place sorted insert rather than
  rebuilding the set per addition.

## See also

* [Fuzzy Concepts](concepts.md) — the concept objects that get unfolded.
* [Queries and Solutions](queries.md) — the query/result objects.
* [Modifiers and Degrees](modifiers_degrees.md) — how degrees enter the MILP.
* [Grammatics](grammar.md) — FDL syntax and the per-solver $k_{\infty}$ table.