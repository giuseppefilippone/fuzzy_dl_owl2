# Summary

Implements a linear membership function for the FuzzyOWL2 framework by defining geometric parameters and bounds.

## Description

The software extends the base fuzzy datatype to model a specific type of membership function characterized by a linear progression between defined points. It relies on two primary coefficients, stored as private attributes, to determine the slope and intercept of the line, which are essential for calculating the degree of membership for a given value. In addition to these linear coefficients, the implementation integrates with inherited lower and upper bounds to fully constrain the domain of the function. Accessor methods are provided to retrieve the specific parameters, while a string representation utility outputs the complete definition including the inherited bounds for debugging or display purposes.
