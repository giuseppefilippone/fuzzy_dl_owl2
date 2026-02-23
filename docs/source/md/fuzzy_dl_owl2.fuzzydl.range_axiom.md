# Summary

Defines a logical constraint that restricts the permissible types of individuals associated with a specific role within a fuzzy description logic system.

## Description

Encapsulating a fundamental rule in description logic, the `RangeAxiom` class dictates the domain of values a specific property or role may assume. By associating a named role with a specific concept, the implementation ensures that any individual linked via that role must belong to the defined concept class. Acting as a building block for knowledge representation, the logic enables reasoning engines to validate relationships and maintain consistency within an ontology. The design relies on simple attribute storage to capture the role identifier and the corresponding concept object, thereby facilitating downstream logical processing and constraint verification.
