# Summary

A framework for transforming fuzzy logic membership degrees through abstract interfaces and concrete mathematical implementations such as linear and triangular functions.

## Description

An abstract base class establishes a foundational blueprint for linguistic hedges and operators, enforcing a consistent contract for altering concept structures and recalculating membership degrees within the fuzzy description logic system. Concrete implementations utilize this interface to apply specific mathematical transformations, such as piecewise linear functions defined by configurable coefficients or triangular shapes characterized by lower, peak, and upper bounds. These transformations wrap base concepts into specialized objects that clamp input values between zero and one, ensuring outputs remain within valid probability bounds while supporting complex reasoning through logical operations like conjunction and disjunction. The architecture facilitates the extension of the knowledge base with custom rules by managing string identifiers and object cloning, thereby enabling the system to handle linguistic nuances by mapping real-valued inputs to normalized membership intervals.

## Modules

- [`fuzzy_dl_owl2.fuzzydl.modifier.linear_modifier`](./fuzzydl_modifier_linear_modifier.md) — A class that implements a piecewise linear transformation for fuzzy logic membership degrees based on a configurable coefficient.
- [`fuzzy_dl_owl2.fuzzydl.modifier.modifier`](./fuzzydl_modifier_modifier.md) — An abstract base class defines the interface for fuzzy logic modifiers that transform concepts and calculate membership degrees.
- [`fuzzy_dl_owl2.fuzzydl.modifier.triangular_modifier`](./fuzzydl_modifier_triangular_modifier.md) — Implements a triangular fuzzy logic modifier that applies a piecewise linear membership function to concepts based on defined boundary parameters.
