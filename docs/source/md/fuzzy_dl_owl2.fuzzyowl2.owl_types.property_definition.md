# Summary

Encapsulates a property name and its associated fuzzy modifier to support the definition of fuzzy logic constraints within the FuzzyOWL2 ontology framework.

## Description

It acts as a container that links a specific property to a fuzzy modifier, allowing the application of linguistic hedges or truth values to object or data properties. By storing these two distinct elements together, the design enables the precise construction of complex fuzzy axioms where the strictness or leniency of comparisons can be controlled. The implementation relies on simple internal storage of string values, providing read-only access through dedicated methods to ensure that the underlying data remains immutable after initialization. This structure serves as a foundational component for the broader system, facilitating the representation of nuanced relationships that go beyond standard binary logic.
