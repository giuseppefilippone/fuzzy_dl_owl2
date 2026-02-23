# Summary

A Python class representing a sigma-count construct within fuzzy description logic that evaluates concept satisfaction based on the cardinality of related individuals.

## Description

Sigma-count logic is encapsulated by modeling a concept that is satisfied when the number of individuals reachable via a specific role and belonging to a target concept meets a fuzzy concrete domain constraint relative to a reference set. It maintains references to the role, the target concept, the list of reference individuals, and the fuzzy concrete concept, effectively acting as a composite node within a broader description logic framework. Logical operations such as negation, conjunction, and disjunction are supported through operator overloading, which delegates the creation of new concept instances to a dedicated operator factory to ensure consistent handling of complex expressions. To facilitate use in collections and comparisons, it generates a deterministic string representation and implements deep cloning to ensure the independence of copied instances. Structural queries for atomic components or roles return empty sets, indicating that this construct is treated as a terminal node during specific graph traversals or analyses.
