# Summary

Implements the Smallest of Maxima defuzzification strategy to convert fuzzy logic values into crisp numerical outputs.

## Description

The software defines a specific approach to resolving fuzzy values by identifying the smallest domain value that achieves the maximum membership degree for a given individual and concept. By extending a base query structure, it integrates into a broader fuzzy logic framework that utilizes Mixed-Integer Linear Programming to solve reasoning tasks. The implementation focuses on constructing an objective expression that minimizes the query variable, effectively steering the optimization process toward the smallest valid maximum. This behavior ensures that when multiple domain values share the highest degree of membership, the system consistently selects the lowest one to produce a deterministic crisp result.
