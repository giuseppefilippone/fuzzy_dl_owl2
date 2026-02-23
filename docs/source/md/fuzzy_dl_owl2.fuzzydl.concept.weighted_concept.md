# Summary

A class representing a concept modified by a numerical weight within a fuzzy description logic framework.

## Description

Software logic for handling graded or prioritized concepts is encapsulated by wrapping a standard concept object with a numerical weight value. By inheriting from the base `Concept` class and utilizing the `HasConceptInterface` mixin, the implementation ensures that structural queries, such as retrieving atomic concepts or roles, are seamlessly delegated to the underlying concept while maintaining the specific weight modifier. The design supports standard logical operations like negation, conjunction, and disjunction through operator overloading, which offloads the complex logic to a dedicated `OperatorConcept` utility. Furthermore, the functionality includes mechanisms for cloning instances and replacing internal components, ensuring that the weight remains consistent during structural transformations while the inner concept hierarchy is updated.
