# Summary

A suite of concrete fuzzy logic implementations that model various membership functions and support fuzzy arithmetic operations.

## Description

These components provide the mathematical foundation for representing uncertainty and imprecision by defining specific geometric shapes for membership degrees, ranging from crisp binary intervals to triangular and trapezoidal sets. The architecture relies on an abstract base class that enforces structural integrity regarding numerical intervals, allowing subclasses to implement specific algorithms for calculating truth values based on linear interpolation or geometric parameters. Beyond simple shapes, the system utilizes a wrapper pattern to apply linguistic modifiers to existing concepts, transforming membership degrees to model intensifiers or hedges within a description logic framework. Logical operations such as conjunction, disjunction, and negation are handled through delegation to a central operator framework, while a dedicated sub-package extends these capabilities to support fuzzy arithmetic and defuzzification for triangular fuzzy numbers.

## Modules

- [`fuzzy_dl_owl2.fuzzydl.concept.concrete.crisp_concrete_concept`] — A crisp concrete concept implementation that applies binary membership logic to determine if a value lies within a specified satisfaction interval.
- [`fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_concrete_concept`] — An abstract base class defines the structure and behavior for fuzzy concepts operating within specific numerical intervals.
- [`fuzzy_dl_owl2.fuzzydl.concept.concrete.left_concrete_concept`] — Implements a left shoulder fuzzy set concept where membership degrees are maximized at lower values and decrease linearly towards zero based on defined interval parameters.
- [`fuzzy_dl_owl2.fuzzydl.concept.concrete.linear_concrete_concept`] — A concrete implementation of a fuzzy concept that utilizes a piecewise linear membership function defined over a normalized domain.
- [`fuzzy_dl_owl2.fuzzydl.concept.concrete.modified_concrete_concept`] — A fuzzy concrete concept wrapper that applies a specific modifier to an underlying concept to transform membership degrees.
- [`fuzzy_dl_owl2.fuzzydl.concept.concrete.right_concrete_concept`] — A Python implementation of a fuzzy logic concept that utilizes a right-shoulder membership function to model values where truth increases linearly over a specific interval.
- [`fuzzy_dl_owl2.fuzzydl.concept.concrete.trapezoidal_concrete_concept`] — Defines a trapezoidal concrete concept that models fuzzy membership degrees using a geometric shape defined by four distinct parameters.
- [`fuzzy_dl_owl2.fuzzydl.concept.concrete.triangular_concrete_concept`] — Implements a fuzzy logic concept using a triangular membership function to determine the degree of membership for numeric values within a defined domain.

## Sub-packages

- [`fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_number`] — A concrete implementation of triangular fuzzy numbers that supports fuzzy arithmetic, logical operations, and defuzzification.
