# Summary

Implements a linear membership function used to calculate degrees of membership in fuzzy sets.

## Description

Extending the base fuzzy datatype, this component models a linear relationship to determine membership degrees within a fuzzy set. It relies on two primary coefficients, representing the slope and intercept, to define the geometric properties of the function and calculate how specific values map to a degree of membership. The implementation encapsulates these parameters to facilitate calculations while providing a string representation that includes inherited boundary values for debugging and serialization purposes. By abstracting the mathematical definition of a line, the logic supports the broader framework's ability to handle fuzzy logic constraints and reasoning.
