# Summary

A fuzzy logic modifier that applies a configurable piecewise linear transformation to the membership degrees of concepts.

## Description

Software designed to adjust the intensity of fuzzy concepts by mapping input membership values through a piecewise linear function. The transformation is governed by a single coefficient that determines the slope and intercept of the function, allowing for precise control over how membership degrees are scaled. By deriving internal parameters from this coefficient, the implementation ensures that the resulting values remain strictly bounded between 0 and 1, effectively clamping inputs that fall outside the valid range. Integration with the broader fuzzy logic framework is achieved through the ability to wrap existing concepts into modified forms and support standard logical operators such as negation, conjunction, and disjunction.
