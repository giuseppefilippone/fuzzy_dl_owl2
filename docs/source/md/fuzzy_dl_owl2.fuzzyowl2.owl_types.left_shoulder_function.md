# Summary

Defines a left-shoulder membership function for fuzzy OWL 2 ontologies in which the degree of membership stays at one for low input values and linearly falls to zero as values increase.

## Description

The `LeftShoulderFunction` class extends the abstract `FuzzyDatatype` hierarchy to capture one of the standard fuzzy set shapes, modelling concepts whose degree of truth is full up to a certain point and then gradually diminishes. It stores two floating-point endpoints that delimit the transition zone where membership decays from one to zero, while the overall domain of the fuzzy set is defined by bounds inherited from the parent datatype. The design keeps these endpoints as private attributes exposed through simple read-only accessors, which preserves encapsulation and keeps the class consistent with the accessor conventions used elsewhere in the datatype hierarchy. A human-readable string representation in the form "left-shoulder(k1, k2, a, b)" combines the inherited domain bounds with the local endpoints, making instances straightforward to inspect during logging, debugging, and serialisation of fuzzy concept definitions.
