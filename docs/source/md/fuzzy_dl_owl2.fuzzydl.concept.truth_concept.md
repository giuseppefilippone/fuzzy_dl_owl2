# Summary

A Python implementation of the universal and contradictory concepts within a fuzzy description logic framework, modeling the extreme truth values Top and Bottom.

## Description

The software defines a specialized class representing the two boundary elements of a concept lattice: the universal concept (Top) and the contradictory concept (Bottom). These entities serve as logical constants where Top acts as an identity for conjunction and an absorbing element for disjunction, while Bottom behaves inversely. The implementation enforces immutability and atomicity, ensuring that these entities cannot be decomposed or modified through structural replacement operations. Standard logical operators such as negation, conjunction, and disjunction are overridden to adhere to the algebraic properties of these truth values, allowing them to interact seamlessly with other concepts in the system. Global instances are provided to facilitate easy access to these logical constants throughout the application.
