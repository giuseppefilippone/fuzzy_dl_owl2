# Summary

A Python implementation of the Sugeno integral fuzzy aggregation operator that combines weighted sub-concepts within a logical framework.

## Description

The software defines a composite structure for representing the Sugeno integral, a fuzzy logic operator used to aggregate multiple sub-concepts according to a specific set of numerical weights. By inheriting from a base concept class and an interface for weighted components, the implementation ensures that the number of weights strictly corresponds to the number of concepts provided during initialization, enforcing data integrity for the aggregation logic. It supports complex structural manipulations, including the ability to clone the entire configuration, recursively traverse the hierarchy to extract atomic concepts or roles, and replace specific internal components while maintaining the weighted relationships. Furthermore, the class integrates seamlessly with the broader logical framework by overloading standard operators for negation, conjunction, and disjunction, delegating these operations to a centralized handler to ensure consistent behavior across the system.
