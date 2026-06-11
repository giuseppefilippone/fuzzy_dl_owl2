# Queries and Solutions

This page documents the query *object model* — the Python classes that the
parser builds from the `?`-suffixed forms of the FDL language, what each query
computes, and how to read the `Solution` returned by solving it. For the FDL
*syntax* of each query see [Grammatics](grammar.md); this page describes the
runtime objects.

## The query lifecycle

Every query is a subclass of `Query`
(`fuzzy_dl_owl2.fuzzydl.query.query.Query`). When `DLParser`/`DLParserFast`
parses an FDL file, each query form is turned into a query instance and appended
to `DLParser.queries_list`. The typical flow is:

```python
from fuzzy_dl_owl2.fuzzydl.parser import DLParserFast as DLParser
from fuzzy_dl_owl2.fuzzydl.milp.solution import Solution

kb, queries = DLParser.get_kb("./example.fdl")
kb.solve_kb()                       # solve the TBox once, up front

for query in queries:
    result: Solution = query.solve(kb)
    if result.is_consistent_kb():
        print(f"{query}{result}")
    print(f"Time (s): {query.get_total_time()}")
```

`Query` exposes three members used by the loop above:

* `solve(kb) -> Solution` — runs the query against a solved `KnowledgeBase` and
  returns a `Solution`.
* `get_total_time() -> float` — wall-clock time of the last `solve`, in seconds
  (the internal counter is nanoseconds; this accessor divides by `1e9`).
* `__str__()` — a human-readable description of the query (used in the log
  output, e.g. `Is audi instance of SportCar ? `).

## Query classes

The table maps each FDL query keyword to the class the parser instantiates and
the value the resulting `Solution` carries.

| FDL keyword | Query class | Arguments | Result (`get_solution()`) |
|---|---|---|---|
| `sat?` | `KbSatisfiableQuery` | — | `bool` — is the KB consistent |
| `max-instance?` | `MaxInstanceQuery` | individual, concept | `float` — greatest membership degree |
| `min-instance?` | `MinInstanceQuery` | individual, concept | `float` — least membership degree |
| `all-instances?` | `AllInstancesQuery` | concept | per-individual minimum membership |
| `max-related?` | `MaxRelatedQuery` | a, b, role | `float` — greatest relation degree |
| `min-related?` | `MinRelatedQuery` | a, b, role | `float` — least relation degree |
| `max-subs?` / `min-subs?` | `MaxSubsumesQuery` / `MinSubsumesQuery` (Łukasiewicz if the KB logic is Łukasiewicz, otherwise Zadeh) | concept, concept | `float` — subsumption degree |
| `max-g-subs?` / `min-g-subs?` | `MaxSubsumesQuery` / `MinSubsumesQuery` (Gödel) | concept, concept | `float` |
| `max-l-subs?` / `min-l-subs?` | `MaxSubsumesQuery` / `MinSubsumesQuery` (Łukasiewicz) | concept, concept | `float` |
| `max-kd-subs?` / `min-kd-subs?` | `MaxSubsumesQuery` / `MinSubsumesQuery` (Kleene-Dienes) | concept, concept | `float` |
| `max-sat?` / `min-sat?` | `MaxSatisfiableQuery` / `MinSatisfiableQuery` | concept, optional individual | `float` — best/worst satisfiability |
| `max-var?` / `min-var?` | `MaxQuery` / `MinQuery` | linear expression | `float` — optimal value of the expression |
| `defuzzify-lom?` | `LomDefuzzifyQuery` | concept, individual, feature | `float` — largest of maxima |
| `defuzzify-mom?` | `MomDefuzzifyQuery` | concept, individual, feature | `float` — middle of maxima |
| `defuzzify-som?` | `SomDefuzzifyQuery` | concept, individual, feature | `float` — smallest of maxima |
| `bnp?` | `BnpQuery` | fuzzy number | `float` — Best Non-Fuzzy Performance |

### Inheritance

The classes are organised by what they compute, not by `max`/`min`:

* `InstanceQuery` — base of `MaxInstanceQuery` / `MinInstanceQuery`
  (concept + individual).
* `SubsumptionQuery` — base of `MaxSubsumesQuery` / `MinSubsumesQuery`. The
  fuzzy implication variant is selected with a
  `LogicOperatorType` (`LUKASIEWICZ` for Łukasiewicz, `GOEDEL` for Gödel,
  `KLEENE_DIENES`, `ZADEH`), which
  is why a single pair of classes covers the plain, `g-`, `l-` and `kd-`
  subsumption keywords.
* `SatisfiableQuery` — base of `MaxSatisfiableQuery` / `MinSatisfiableQuery`;
  the individual argument is optional (overloaded constructor).
* `RelatedQuery` — base of `MaxRelatedQuery` / `MinRelatedQuery`.
* `DefuzzifyQuery` — base of `LomDefuzzifyQuery` / `MomDefuzzifyQuery` /
  `SomDefuzzifyQuery` (concept + individual + concrete feature name).
* `MaxQuery` / `MinQuery` — optimise a linear `Expression` (the `max-var?` /
  `min-var?` keywords) subject to KB consistency.
* `KbSatisfiableQuery`, `AllInstancesQuery`, `BnpQuery` derive directly from
  `Query`.

> `ClassificationQuery` also exists in the package but is not produced by any
> FDL keyword; it is used internally for concept classification.

## The `Solution` object

`solve` returns a `fuzzy_dl_owl2.fuzzydl.milp.solution.Solution`. Read it before
acting on the value:

| Member | Returns | Meaning |
|---|---|---|
| `is_consistent_kb()` | `bool` | Whether the KB was consistent. If `False`, the answer to *any* query is `1.0` and `get_solution()` is not meaningful. |
| `get_solution()` | `bool` \| `float` | The query answer — a boolean for `sat?`, a float degree/value otherwise. |
| `get_showed_variables()` | `dict[str, float]` | Variable values requested via `show-variables` (and similar show-statements). |
| `add_showed_variable(name, value)` | `None` | Records a shown variable (used by the solver). |

`str(solution)` is the solved value when the KB is consistent, or the literal
`"Inconsistent KB"` otherwise. The class constants `Solution.CONSISTENT_KB`
(`True`) and `Solution.INCONSISTENT_KB` (`False`) name the two consistency
states.

### Reading a result safely

```python
result = query.solve(kb)
if not result.is_consistent_kb():
    # Inconsistent KB: every query trivially answers 1.0
    print("KB inconsistent")
else:
    answer = result.get_solution()      # bool for sat?, float otherwise
    print(answer)
```

## Notes

* Solve the knowledge base once with `kb.solve_kb()` before iterating the
  queries; each `query.solve(kb)` then reuses the prepared KB.
* `all-instances?` over a KB with no individuals short-circuits — `DLParserFast.main`
  emits *"There are no individuals in the fuzzy KB"* instead of solving.
* For the mathematical definition of each query (the `sup`/`inf` it computes),
  see the *Queries* section of [Grammatics](grammar.md).