# Summary

An abstract base class that defines a framework for querying the membership degree of a specific individual within a given concept.

## Description

This class serves as a foundational component for determining how strongly a particular individual belongs to a specific concept within a fuzzy description logic system. By inheriting from the abstract query base, it enforces a strict validation during initialization to ensure that the target concept is abstract rather than concrete, raising an error if this constraint is violated. The design stores the provided concept and individual as core attributes while initializing a placeholder for the membership expression, which subclasses are expected to populate with specific logic for calculating or retrieving degrees. This structure allows for specialized implementations, such as finding minimum or maximum membership degrees, to build upon a consistent and validated data model.
