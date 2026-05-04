# Summary

A class representing a sigma-count construct within fuzzy description logic that evaluates concepts based on the cardinality of related individuals.

## Description

The implementation models a specialized construct known as a sigma-count, which determines satisfaction by counting the number of individuals reachable via a specific role that also belong to a target concept. It encapsulates a binary role, a target concept definition, a collection of reference individuals, and a fuzzy concrete concept that defines the evaluation criteria within a fuzzy logic framework. By inheriting from the base `Concept` class, the implementation integrates seamlessly into the broader description logic system, providing mechanisms for deep cloning and generating a standardized string representation of the complex logical structure. Logical operations such as negation, conjunction, and disjunction are supported through delegation to an `OperatorConcept` utility, allowing these instances to participate in complex logical expressions while maintaining their specific semantic identity. The design treats the construct as an atomic entity for replacement operations and relies on its string representation for hashing, ensuring consistent behavior when used in collections.
