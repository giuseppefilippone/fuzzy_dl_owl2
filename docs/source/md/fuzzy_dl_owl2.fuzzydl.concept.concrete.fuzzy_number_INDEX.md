# Summary

Models uncertain numerical values using triangular membership functions to support arithmetic, logical operations, and defuzzification within a fuzzy logic framework.

## Description

Uncertainty is represented through a triangular membership function defined by lower, peak, and upper bounds, ensuring strict validation during initialization to maintain data integrity. Arithmetic manipulations rely on interval arithmetic principles to generate new instances without modifying the originals, while fuzzy logical tasks such as conjunction and disjunction are handled by delegating to an external operator system. To bridge the gap between fuzzy and crisp values, utilities for calculating the Best Non-Fuzzy Performance are included, alongside class-level mechanisms for defining a global universe of discourse that governs range management.

## Modules

- [`fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_number.triangular_fuzzy_number`](./fuzzydl_concept_concrete_fuzzy_number_triangular_fuzzy_number.md) — A Python class that models triangular fuzzy numbers, providing arithmetic and logical operations alongside utilities for defuzzification and range management.
