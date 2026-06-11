# Summary

Defines a symbolic variable structure used to represent degrees of satisfaction within linear expressions for fuzzy description logic ontologies.

## Description

Symbolic variables are modeled to encapsulate essential properties such as a unique identifier, a specific domain type, and numeric constraints defined by lower and upper bounds. The design automatically adjusts these numeric boundaries based on the variable type, ensuring that binary and semi-continuous variables are constrained between zero and one, while continuous and integer types default to infinite ranges. To facilitate the construction of optimization models, static factory methods provide convenient interfaces for generating specific variable types, and a class-level counter enables the automatic creation of unique sequential names. Equality comparisons rely primarily on the variable's name, while hashing incorporates the full state including type and bounds to ensure consistent behavior within hash-based collections. Additionally, the implementation supports cloning for independent copies and includes flags to identify variables acting as datatype fillers within the broader fuzzy logic framework.
