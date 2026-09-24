# Summary

A crisp concrete concept for fuzzy description logics that behaves as a binary membership function, granting full membership to values inside a closed satisfaction interval nested within a bounded numeric domain and zero membership to everything else.

## Description

**CrispConcreteConcept** extends FuzzyConcreteConcept to capture the degenerate case of a fuzzy concept whose membership is strictly binary: any value within the satisfaction interval [a, b] belongs with degree 1.0, while every other value belongs with degree 0.0. The concept is anchored to a wider validity interval [k1, k2] that defines the numeric domain over which it is meaningful, and the constructor enforces this nesting invariant up front, raising a ValueError if the satisfaction interval is malformed (a greater than b) or escapes the domain (a below k1 or b above k2). This fail-fast validation guarantees that only well-formed instances reach the reasoning engine, where malformed intervals could otherwise silently corrupt downstream computations.

Although the membership function itself is crisp, the class deliberately lives inside the fuzzy concept hierarchy so it can be freely combined with genuinely fuzzy concrete concepts when building a knowledge base. Logical composition is exposed through overloaded unary negation, bitwise AND, and bitwise OR operators, each delegating to the shared OperatorConcept helper rather than reimplementing set-theoretic logic locally, which keeps the semantics of negation, conjunction, and disjunction uniform across all concept types and always yields new objects so the original operands remain untouched. Instances additionally support cloning, expose the satisfaction bounds through properties, and produce a canonical name of the form crisp(k1, k2, a, b) that makes them readable and distinguishable in generated output.

Hashing is derived from the concept's name, its four numeric bounds, and its type rather than from object identity, so two structurally identical concepts are interchangeable as dictionary keys or set members — a deliberate design choice that enables concept deduplication and caching throughout the reasoning layer.
