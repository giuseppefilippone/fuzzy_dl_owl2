# Summary

Implements a trapezoidal membership function for fuzzy logic concepts, defining degrees of membership based on specific geometric parameters.

## Description

The software models a fuzzy logic concept using a trapezoidal membership function, where the degree of truth for a given value is determined by its position relative to four defining parameters. It enforces strict geometric constraints during initialization to ensure the shape parameters are ordered correctly and that the definition domain fully encompasses the support interval. Membership calculations return zero for values outside the support range, one for values within the core plateau, and linearly interpolated values for the rising and falling edges. Logical operations such as conjunction, disjunction, and negation are supported through operator overloading, which delegates the computation to a separate operator utility to maintain consistency across the fuzzy logic framework. The implementation also includes mechanisms for object cloning and hashing based on the specific configuration of the trapezoid, facilitating use in collections and data structures.
