# Summary

A symbolic variable class designed for linear expressions within mixed-integer linear programming contexts, specifically to represent degrees of satisfaction in fuzzy description logic ontologies.

## Description

The implementation encapsulates essential properties such as a unique identifier, a specific domain type, and numeric bounds that are automatically configured based on the variable's classification. Design decisions include the use of static factory methods to simplify the instantiation of specific variable types like binary or continuous, while a class-level counter ensures the generation of unique sequential names when explicit identifiers are not provided. Logic for boundary management is tightly coupled with the variable type, where setting a variable to binary or semi-continuous automatically constrains the domain between zero and one, whereas continuous or integer types default to infinite bounds. Equality and hashing behaviors rely entirely on the variable's string representation, allowing instances to be used effectively within hash-based collections, and the class further supports cloning to create independent copies of existing variables.
