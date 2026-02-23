# Summary

A query implementation that applies the Smallest of Maxima defuzzification strategy to resolve fuzzy feature values into crisp numerical outputs.

## Description

The logic operates by identifying the domain values that correspond to the highest degree of membership for a specific individual within a given concept and selecting the smallest among those maxima. Accepting a target concept, an individual instance, and a feature name defines the scope of the fuzzy evaluation required to determine the crisp output. To facilitate this calculation within a mathematical optimization context, the implementation constructs a linear objective expression that assigns a unit coefficient to a decision variable, effectively instructing an underlying solver to minimize this variable. Inheritance from a base defuzzification query class allows this strategy to fit seamlessly into a broader framework where different defuzzification methods can be utilized depending on the analytical requirements.
