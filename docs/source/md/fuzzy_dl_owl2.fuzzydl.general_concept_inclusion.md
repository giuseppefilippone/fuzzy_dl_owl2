# Summary

A Python class representing a fuzzy logic axiom that defines the graded inclusion of one concept within another.

## Description

The software models a graded subsumption relationship between two concepts, where a sub-concept is included within a super-concept to a specific degree of truth. It encapsulates the logic operator type, such as Łukasiewicz or Gödel, which dictates the semantic implication used to evaluate the inclusion. Instances are mutable, allowing the underlying concepts or the degree of inclusion to be updated after creation, which supports dynamic reasoning scenarios. To facilitate use in data structures like sets and dictionaries, the implementation provides structural equality checks and hash generation based on the internal components. A human-readable string representation is generated to display the logical structure, indicating the subsumed concept, the implication operator, the subsumer, and the lower bound degree.
