# Summary

A framework for applying mathematical transformations to fuzzy logic membership degrees through abstract and concrete modifier implementations.

## Description

An abstract base class establishes the structural contract for linguistic hedges and logical operators, mandating that concrete implementations define specific mathematical logic for mapping input values to a normalized range while supporting object cloning and consistent hashing. Concrete strategies utilize this foundation to apply distinct geometric transformations, such as piecewise linear adjustments controlled by shape coefficients or triangular distributions defined by strict boundary parameters. By encapsulating base concepts within specialized wrapper objects, the architecture enables dynamic evaluation of membership values based on the specific transformation rules defined at initialization. Logical composition is facilitated through operator overloading for conjunction, disjunction, and negation, allowing complex fuzzy expressions to be constructed by combining or negating modifiers while maintaining immutability.

## Modules

- [`fuzzy_dl_owl2.fuzzydl.modifier.linear_modifier`] — Implements a fuzzy logic modifier that transforms concept membership degrees using a configurable piecewise linear function.
- [`fuzzy_dl_owl2.fuzzydl.modifier.modifier`] — An abstract base class that defines the interface for fuzzy logic modifiers capable of transforming concepts and calculating adjusted membership degrees.
- [`fuzzy_dl_owl2.fuzzydl.modifier.triangular_modifier`] — Implements a fuzzy logic modifier that applies a triangular membership function to concepts using three distinct boundary parameters to define degrees of membership.
