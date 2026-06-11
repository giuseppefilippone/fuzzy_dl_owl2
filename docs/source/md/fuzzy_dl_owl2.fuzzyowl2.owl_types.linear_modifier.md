# Summary

A fuzzy logic modifier class that applies a linear transformation to membership degrees using a specific coefficient.

## Description

The implementation extends the base fuzzy modifier functionality to support linear scaling operations within the FuzzyOWL2 framework. By storing a floating-point coefficient, the logic allows for the adjustment of membership degrees through multiplication or scaling, which is a fundamental requirement for defining custom fuzzy sets. Encapsulation is handled by keeping the coefficient private and exposing it via a dedicated accessor, ensuring that the internal state remains controlled while allowing external retrieval of the transformation factor. Additionally, the object provides a human-readable string representation that clearly indicates the modifier type and its associated coefficient, facilitating debugging and logging.
