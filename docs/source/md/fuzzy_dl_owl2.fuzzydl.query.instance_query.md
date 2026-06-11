# Summary

An abstract base class provides a framework for querying the membership degree of a specific individual within a given concept.

## Description

Extending the generic `Query` interface, this abstract class establishes a structural foundation for evaluating how strongly a specific individual belongs to a particular concept. It enforces a strict design constraint by validating that the provided concept is abstract, raising an error if a concrete concept is supplied, which ensures that only appropriate data types are processed during instance retrieval. During initialization, the component stores the target concept and individual as attributes while initializing an expression placeholder intended to represent the degree of membership. This architecture allows subclasses to focus on populating the expression with specific logic for identifying instances with minimum or maximum membership degrees without needing to re-implement the validation or storage mechanisms.
