# Summary

Defines the logical constants Top and Bottom within a fuzzy description logic hierarchy to represent universal truth and contradiction.

## Description

The implementation models the two extreme truth values, known as the universal concept (Top) and the contradictory concept (Bottom), which serve as the boundary conditions for the logical framework. By employing a singleton pattern, the design ensures that only a single shared instance exists for each truth value, optimizing memory usage and guaranteeing immutability across the ontology. Logical operations such as conjunction, disjunction, and negation are overridden to adhere to standard mathematical laws, where Top acts as an identity for conjunction and Bottom acts as an absorbing element. These constants are treated as atomic entities that cannot be decomposed further, providing a stable foundation for constructing more complex concept expressions within the system.
