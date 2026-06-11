# Summary

Encapsulates the logical equivalence between two distinct concepts within a fuzzy description logic framework.

## Description

The software provides a structural representation for asserting that two specific entities are treated as interchangeable, serving as a container for a pair of concept objects. By storing references to two distinct concepts, the implementation allows users to define and manipulate relationships where the semantics of one entity are identical to another within a specific context. Design choices include the ability to generate independent copies of the equivalence statement through a cloning mechanism, which facilitates the reuse of logical axioms without altering the original definitions. Accessor methods enable the retrieval of the individual components involved in the relationship, ensuring that the internal state remains encapsulated while still allowing external inspection of the logical structure.
