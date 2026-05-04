# Summary

An abstract base class representing concept definitions within the FuzzyOWL2 framework.

## Description

Designed to serve as a foundational interface for various fuzzy logic constructs, this class enforces a standard structure for concept definitions by requiring a specific classification upon initialization. Subclasses are expected to inherit from this base to implement specific behaviors, while the base class itself manages the storage and retrieval of the associated `ConceptType` enumeration. By encapsulating the type information and providing an accessor method, the design ensures that every concept definition can be categorized and identified consistently throughout the system. The implementation relies on Python's abstract base class module to prevent direct instantiation, thereby guiding developers to create concrete implementations for specific logical scenarios.
