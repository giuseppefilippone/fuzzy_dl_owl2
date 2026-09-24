# Summary

A crisp function datatype for the FuzzyOWL2 framework that stores two numeric coefficients and renders itself as a `crisp(...)` expression bounded by inherited interval limits.

## Description

The `CrispFunction` class extends the `FuzzyDatatype` base type so that exact, non-fuzzy mathematical constraints can be represented alongside genuinely fuzzy datatypes inside a fuzzy OWL 2 ontology. Instances are deliberately lightweight value objects: the constructor stores the two coefficients `a` and `b` as private floats, and a pair of simple getters exposes them without offering any way to mutate them, which keeps the datatype predictable wherever ontology terms are shared. A notable design decision is the split of responsibility with the superclass — the string representation formats the result as `crisp(k1, k2, a, b)`, pulling the lower and upper bounds from inherited attributes rather than duplicating interval logic in the subclass. That human-readable output doubles as a serialisation-friendly form, allowing crisp constraints to be embedded directly into generated ontology markup or inspected during debugging. Together these pieces make the class a small but essential bridge between precise, classical logic and the broader fuzzy modelling framework.
