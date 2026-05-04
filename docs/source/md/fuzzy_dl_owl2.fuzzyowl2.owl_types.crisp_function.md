# Summary

A specialized datatype class representing a crisp function within the FuzzyOWL2 framework to model precise mathematical intervals or linear transformations.

## Description

Acting as a bridge between non-fuzzy, exact logic and a broader fuzzy system, the implementation models precise mathematical intervals or linear transformations using specific coefficients. The logic is driven by two primary numerical parameters, `a` and `b`, which are supplied during instantiation to define the function's behavior, while operating within conceptual lower and upper bounds inherited from the parent datatype. Accessor methods are provided to retrieve these coefficients without modifying the internal state, ensuring encapsulation of the mathematical properties. Furthermore, a string representation formats the current configuration, including the bounds and coefficients, to facilitate debugging and display within the ontology context.
