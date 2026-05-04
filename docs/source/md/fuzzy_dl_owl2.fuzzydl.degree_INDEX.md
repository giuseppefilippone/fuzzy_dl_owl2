# Summary

A polymorphic framework for quantifying fuzzy logic satisfaction levels through numeric, variable, and symbolic expression representations designed for constraint solving.

## Description

An abstract base class establishes a unified interface for handling various representations of satisfaction metrics, enabling the system to treat raw numbers, algebraic variables, and complex expressions interchangeably. Concrete implementations wrap floating-point values for fixed constants or utilize symbolic wrappers to represent unknowns and dynamic formulas, ensuring that all types support essential arithmetic operations like addition, subtraction, and scalar multiplication. This polymorphic design facilitates the generation of mathematical inequalities and constraints required by mixed-integer linear programming solvers, allowing the reasoning engine to formulate optimization problems where satisfaction levels act as boundaries or targets. By explicitly distinguishing between numeric and non-numeric entities, the architecture ensures that type-specific logic is applied correctly during the resolution of fuzzy constraints and the construction of linear equations.

## Modules

- [`fuzzy_dl_owl2.fuzzydl.degree.degree`] — An abstract base class defines the interface for a degree metric used to quantify the extent to which a concept is satisfied within a fuzzy logic system.
- [`fuzzy_dl_owl2.fuzzydl.degree.degree_expression`] — A symbolic wrapper for algebraic expressions that represents non-numeric degrees within a fuzzy logic framework, enabling dynamic constraint generation and mathematical manipulation.
- [`fuzzy_dl_owl2.fuzzydl.degree.degree_numeric`] — Encapsulates a specific floating-point value to represent a degree of satisfaction within a fuzzy logic framework.
- [`fuzzy_dl_owl2.fuzzydl.degree.degree_variable`] — Defines a symbolic representation of a degree of satisfaction using an algebraic variable to enable dynamic constraint generation within a fuzzy logic system.
