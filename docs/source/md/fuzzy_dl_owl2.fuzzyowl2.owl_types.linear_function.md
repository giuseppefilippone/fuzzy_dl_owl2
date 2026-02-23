# Summary

Extends the base fuzzy datatype to model a linear membership function used for defining fuzzy sets within the FuzzyOWL2 framework.

## Description

It initializes with two floating-point parameters that define the slope and intercept of the line, establishing the mathematical relationship for calculating membership degrees. The design leverages inheritance to incorporate domain boundaries, specifically lower and upper limits, which constrain the range of the function. Read-only access to the coefficients is provided to maintain encapsulation, and a string representation is implemented to display the function alongside its domain parameters for debugging and logging.
