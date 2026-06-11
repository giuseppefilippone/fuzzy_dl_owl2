# Summary

A Python class representing a left-shoulder membership function used within fuzzy logic systems to model concepts where membership decreases as values increase.

## Description

The implementation models a specific type of fuzzy set where membership is full for low values and tapers off linearly as the input grows. It relies on two primary floating-point parameters to define the transition zone where the degree of membership drops from one to zero, while also utilizing inherited bounds to establish the overall domain of the fuzzy set. By extending the base fuzzy datatype, the class encapsulates the geometric properties of this shape and provides mechanisms to retrieve the defining coefficients. A string representation is included to offer a human-readable format of the current configuration, which aids in debugging and logging within the broader fuzzy logic framework.
