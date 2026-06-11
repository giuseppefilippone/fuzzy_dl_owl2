# Summary

Implements a fuzzy logic concept using a triangular membership function to determine the degree of membership for numeric values within a defined domain.

## Description

The software models a specific type of fuzzy set where membership degrees follow a triangular shape, rising linearly to a peak and then falling back to zero. It requires defining a domain interval alongside three specific points that determine the start, peak, and end of the triangle, enforcing strict validation to ensure the geometric constraints are met during instantiation. Central to the implementation is the calculation of membership degrees, which evaluates a given numeric value against the triangle's vertices to return a value between zero and one based on linear interpolation. To support complex fuzzy logic reasoning, the implementation overloads standard logical operators such as negation, conjunction, and disjunction, delegating these operations to a separate handler while maintaining the ability to clone instances and generate unique hash identifiers based on the defining parameters.
