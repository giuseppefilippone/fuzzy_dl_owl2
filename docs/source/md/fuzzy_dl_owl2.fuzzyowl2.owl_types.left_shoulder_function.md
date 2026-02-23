# Summary

Implements a left-shoulder membership function used within fuzzy logic systems to model concepts where membership values decrease as input values increase.

## Description

The class models a specific type of fuzzy set where membership is maximized for lower numerical values and gradually declines as the input increases, eventually reaching zero. By extending the base `FuzzyDatatype`, it inherits domain boundaries defined by `k1` and `k2` while introducing specific parameters `a` and `b` to delineate the transition zone where the membership value drops from one to zero. This design encapsulates the mathematical definition of a left-shoulder curve, allowing the fuzzy logic system to represent linguistic terms such as "low" or "small" within a continuous domain. Accessor methods expose the defining coefficients, and a custom string representation provides a human-readable format that includes both the inherited bounds and the specific transition parameters for debugging and logging purposes.
