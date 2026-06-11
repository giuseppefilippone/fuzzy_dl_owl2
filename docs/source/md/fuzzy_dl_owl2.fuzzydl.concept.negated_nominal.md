# Summary

Defines a class representing the logical complement of a named individual within a fuzzy description logic framework.

## Description

The software models a specific type of concept that represents the exclusion of a particular named individual from a domain, often utilized in range restrictions. By inheriting from the base `Concept` class, it establishes itself as an atomic concept type while storing the identifier of the individual being negated and generating a standardized string representation for that exclusion. Logical operations such as conjunction and disjunction are supported through delegation to an `OperatorConcept` utility, allowing these negated nominals to participate in complex expressions. However, the implementation enforces a strict constraint against double negation, raising an exception if an attempt is made to complement an already negated nominal, thereby preserving the integrity of the logical structure. Additionally, the implementation includes mechanisms for cloning instances and generating hash values based on structural identity to facilitate use in collections and comparisons.
