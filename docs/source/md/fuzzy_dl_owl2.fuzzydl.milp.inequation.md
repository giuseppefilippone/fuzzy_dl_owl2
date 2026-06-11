# Summary

Encapsulates linear constraints of the form $E \bowtie 0$ within a mixed-integer linear programming framework, normalizing the right-hand side to zero while supporting equality, less-than, and greater-than relations.

## Description

The software defines a structure for representing mathematical linear constraints where the right-hand side is always normalized to zero, simplifying the handling of inequalities within a solver or optimization engine. By encapsulating an algebraic expression alongside a relational operator, it allows for the precise definition of constraints such as less-than, greater-than, or equal-to relationships. Static factory methods are provided to streamline the instantiation of specific inequality types, acting as convenient aliases for the constructor. Furthermore, the implementation includes standard object comparison and hashing mechanisms, enabling these constraints to be used effectively within hash-based collections like sets and dictionaries while ensuring that string representations remain human-readable for debugging purposes.
