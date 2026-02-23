# Summary

Implements a triangular membership function used to define fuzzy modifiers within the FuzzyOWL2 framework.

## Description

Software components within the FuzzyOWL2 framework utilize this implementation to model fuzzy concepts through a geometric triangular shape defined by three distinct numerical parameters. By inheriting from a base fuzzy modifier class, the logic establishes a specific membership function where the degree of truth increases linearly from a left endpoint to a central peak and then decreases linearly to a right endpoint. The design encapsulates these three floating-point values—representing the support start, the maximum membership point, and the support end—to allow for the precise calculation of membership degrees for a given concept. Encapsulation is further supported by accessor methods that retrieve the specific boundary and peak values, alongside a string representation that aids in debugging and logging by clearly displaying the modifier's configuration.
