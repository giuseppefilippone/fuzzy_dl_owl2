# Summary

Implements a mathematical framework for handling uncertain values through triangular fuzzy numbers, supporting arithmetic operations, logical comparisons, and defuzzification.

## Description

Uncertainty is modeled using a triangular membership function defined by lower, peak, and upper bounds, allowing for the representation of imprecise data within a structured framework. The architecture relies on inheritance from a concrete concept base to manage data structures and enforce strict type validation, ensuring that all instances adhere to defined constraints. Mathematical operations are handled through operator overloading and interval arithmetic principles, which generate new immutable objects rather than modifying existing states, while logical conjunctions and disjunctions are facilitated by integration with an operator concept handler. To bridge the gap between fuzzy and crisp values, the system calculates the Best Non-Fuzzy Performance (BNP), and class-level attributes establish a global universe of discourse to maintain consistent boundaries across the application.

## Modules

- [`fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_number.triangular_fuzzy_number`] — A Python class representing triangular fuzzy numbers that supports arithmetic operations, logical comparisons, and defuzzification.
