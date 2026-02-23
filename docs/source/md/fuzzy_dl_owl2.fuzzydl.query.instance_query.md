# Summary

An abstract base class that defines a framework for querying the membership degree of a specific individual relative to a given concept.

## Description

It serves as a foundational component within a fuzzy description logic system, specifically designed to handle queries that determine the extent to which an individual belongs to a concept. By inheriting from the abstract base class, it enforces a strict validation rule during initialization that prevents the use of concrete concepts, ensuring that only abstract concepts are processed for instance retrieval. The structure stores the provided concept and individual as core attributes while reserving a placeholder for an expression object, which subclasses are expected to populate to represent the specific membership degree logic. This design facilitates the creation of specialized queries, such as those seeking minimum or maximum membership degrees, by providing a consistent interface and validation mechanism for all derived implementations.
