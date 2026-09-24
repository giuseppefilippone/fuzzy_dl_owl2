# Changelog

Notable changes to fuzzy-dl-owl2. Entries marked **[divergence]** deliberately
depart from the original Java fuzzyDL reasoner, which shares the defect; see
the `DELIBERATE DIVERGENCE` comments at the edit sites.

## 1.0.32 — 2026-09-24

### Fixed

- **`min-instance?` on a `w-sum-zero` concept always reported an inconsistent
  KB** (`max-instance?` worked). In
  `KnowledgeBase.solve_w_sum_zero_complemented_assertion` the two rows
  `x_{a:¬WSZ} ≥ 1 − Σ wᵢxᵢ − y` and `x_{a:¬WSZ} ≤ 1 − Σ wᵢxᵢ + y` were built
  without the constant 1, so with `y = 0` (all components positive) the second
  row forced `x_{a:¬WSZ} ≤ −Σ wᵢxᵢ` and the model became infeasible. Porting
  bug: the Java oracle (`WeightedSumZeroConcept.solveComplementedAssertion`)
  has `new Expression(1, terms)` in both rows; parity restored.
  Regression KBs `examples/TestSuite/weightedSumZero1-8.txt` (the two
  pre-existing ones were never wired into a test), cases in
  `test/test_weighted_sum.py`.

## 1.0.31 — 2026-09-23

### Fixed

- **Trapezoidal membership: descending side returned the ascending slope**
  **[divergence]**. `TrapezoidalConcreteConcept.get_membership_degree` never
  reached the `(d - x) / (d - c)` branch. Display-only: the MILP encoding
  uses the breakpoints and never calls this function.
- **`(min-sat? C)` (one argument) raised and killed the whole KB load.**
  `SatisfiableQuery` re-entered `self.__init__` virtually; the private
  initialiser is now called directly (Java `this(c, null)` semantics) and
  `MinSatisfiableQuery` accepts a `None` individual.
- **A modifier over a complex concept collapsed `min-instance?` to 0**
  **[divergence]**. `solve_modifier_complemented_assertion` now also asserts
  the complement of the modifier's child (complex or TBox-defined).
- **`Concept.replace` polarity** **[divergence]**. Modified/OWA concepts no
  longer negate the substitution result; `OperatorConcept.replace` dispatches
  on the receiver's type. Dead code in the reasoning paths.
- Parser error messages carry the exception type; the legacy pyparsing
  parser tries `queries` before `concept` in `gformula`.

### Changed

- `ModifiedConcept.replace` is abstract, matching the Java oracle.
