# Summary

A class representing a sigma-count construct within fuzzy description logic that evaluates the cardinality of related individuals against a fuzzy concrete domain.

## Description

The implementation extends the base `Concept` class to model a specific fuzzy logic constraint where satisfaction depends on the number of related individuals belonging to a target concept. By combining a binary role, a reference set of individuals, and a fuzzy concrete domain concept, it defines a complex condition that evaluates the cardinality of relationships within a fuzzy context. To facilitate logical reasoning, the class overrides standard operators to support negation, conjunction, and disjunction, delegating the construction of these composite expressions to a dedicated operator handler. Structural integrity is maintained through a deep cloning mechanism and a custom hashing implementation that relies on the internal components, ensuring that instances behave correctly when used in collections or complex logical structures.
