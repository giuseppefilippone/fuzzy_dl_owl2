# Summary

A fuzzy logic modifier that applies a linear transformation to membership degrees using a specific coefficient.

## Description

Extending the base fuzzy modifier functionality, this implementation handles linear transformations required to scale or adjust membership degrees within the FuzzyOWL2 framework. The logic encapsulates a single floating-point coefficient that defines the specific linear operation, ensuring that the mathematical parameter is stored securely and remains accessible for reasoning tasks. By inheriting from the parent class, the design integrates seamlessly into the broader hierarchy while providing a distinct string representation that clearly identifies the modifier type and its associated value. This approach allows for precise manipulation of fuzzy set semantics through a simple, coefficient-based model.
