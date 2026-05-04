# Summary

A fuzzy concept implementation that models a piecewise linear membership function operating on a normalized domain between zero and one.

## Description

The implementation extends the base fuzzy concrete concept to represent a specific type of membership function characterized by a piecewise linear shape. It relies on a normalized domain ranging from zero to one, where the shape of the function is determined by a specific "knee" point defined by parameters `a` and `b`, creating a linear ramp from the origin to this point and a second ramp to the maximum value. While the constructor accepts interval bounds, the core membership calculation logic strictly utilizes the normalized input and the internal coefficients to determine the degree of truth through linear interpolation. Validation logic ensures that the definition parameters adhere to mathematical constraints, specifically requiring that the lower bound does not exceed the threshold and that the membership degree at the threshold remains within valid limits. Beyond calculating membership degrees, the design integrates with broader fuzzy logic operations by delegating tasks like negation, conjunction, and disjunction to an external operator handler to support complex logical expressions.
