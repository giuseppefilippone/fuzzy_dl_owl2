# Summary

A Python class representing a fuzzy logic axiom that defines the inclusion of one concept within another to a specific degree of truth.

## Description

The software models a graded subsumption relationship between two concepts within a fuzzy description logic framework, capturing the extent to which a sub-concept is included in a super-concept. It encapsulates a specific logic operator type, such as Łukasiewicz or Gödel, to determine the semantic implications of the relationship, while storing a degree value that serves as a lower bound for the truth of the inclusion. Designed as a mutable data structure, the implementation allows for the modification of the underlying concepts and the degree of truth after instantiation, facilitating dynamic updates to the logical axioms. To support integration into larger systems, the implementation provides mechanisms for structural equality comparison, hash-based ordering, and a human-readable string representation that visualizes the logical structure and associated truth value.
