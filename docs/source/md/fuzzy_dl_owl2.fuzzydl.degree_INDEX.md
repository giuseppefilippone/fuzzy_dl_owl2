# Summary

Defines a polymorphic architecture for representing degrees of satisfaction in fuzzy description logic systems using numeric, variable, or algebraic expression metrics.

## Description

An abstract base class establishes a unified interface for quantifying the extent to which a concept is satisfied, enabling the system to handle various underlying representations such as raw numbers, symbolic variables, or complex mathematical expressions interchangeably. Concrete implementations bridge high-level logical concepts with low-level mathematical requirements by encapsulating floating-point values, algebraic variables, or symbolic expressions, all of which support arithmetic manipulation like addition, subtraction, and scaling. These components facilitate the formulation of optimization problems by generating inequality constraints and participating in mixed-integer linear programming (MILP) models, ensuring that dynamic satisfaction levels can be solved rather than hardcoded. A static factory method ensures correct instantiation based on input type, while utility checks for specific states like zero or one support the logical reasoning required by the broader fuzzy logic framework.

## Modules

- [`fuzzy_dl_owl2.fuzzydl.degree.degree`](./fuzzydl_degree_degree.md) — An abstract base class defines the interface for a degree metric used to quantify the extent to which a concept is satisfied within a fuzzy description logic system.
- [`fuzzy_dl_owl2.fuzzydl.degree.degree_expression`](./fuzzydl_degree_degree_expression.md) — A symbolic representation of a degree that wraps an algebraic expression to support dynamic, non-numeric calculations within a fuzzy logic framework.
- [`fuzzy_dl_owl2.fuzzydl.degree.degree_numeric`](./fuzzydl_degree_degree_numeric.md) — Encapsulates a specific numeric value to represent the satisfaction level of a concept within a fuzzy description logic framework.
- [`fuzzy_dl_owl2.fuzzydl.degree.degree_variable`](./fuzzydl_degree_degree_variable.md) — Encapsulates a symbolic variable to represent a dynamic degree of satisfaction for use in algebraic expressions and constraints.
