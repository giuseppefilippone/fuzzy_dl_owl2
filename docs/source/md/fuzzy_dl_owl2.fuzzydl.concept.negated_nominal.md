# Summary

Defines a class representing the logical complement of a named individual within a fuzzy description logic framework.

## Description

A class is defined to model the complement of a specific named individual, allowing the expression of constraints that exclude particular entities from a domain. By inheriting from the base `Concept` class, it integrates into the broader ontology structure while enforcing specific logical rules, such as the prohibition of nested negation which results in a runtime exception. Logical operations like conjunction and disjunction are supported through operator overloading, which delegates the actual computation to a separate utility class to maintain consistency across different concept types. Instances are made compatible with hash-based collections by deriving their hash value from a standardized string representation of the negated individual.
