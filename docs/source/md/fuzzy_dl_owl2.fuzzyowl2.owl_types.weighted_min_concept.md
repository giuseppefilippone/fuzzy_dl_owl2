# Summary

Models a weighted minimum aggregation operator within the FuzzyOWL2 framework to construct complex fuzzy concepts from a collection of sub-concepts.

## Description

Extending the base definition for fuzzy concepts, the class implements the logic required to represent a weighted minimum aggregation, which is a fundamental operation in fuzzy description logics for combining multiple criteria with varying importance. The design centers around holding a collection of sub-concepts that act as operands, allowing the framework to evaluate the minimum membership degree across these weighted components. By initializing with a specific type identifier, the implementation integrates seamlessly into the broader type system used for parsing and reasoning over fuzzy ontologies. Furthermore, the logic includes a mechanism to generate a human-readable string representation that encapsulates the internal structure using a specific prefix notation, facilitating debugging and textual output.
