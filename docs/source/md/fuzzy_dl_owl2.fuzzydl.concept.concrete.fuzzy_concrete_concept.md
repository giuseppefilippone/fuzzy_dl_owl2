# Summary

An abstract base class defines fuzzy concepts operating over numerical intervals with configurable lower and upper bounds.

## Description

It serves as a foundational template for evaluating the degree of membership for specific numerical values within a defined range, distinguishing concrete data handling from abstract conceptual relationships. The implementation manages interval parameters through properties that enforce structural integrity, specifically ensuring that the upper bound is never less than the lower bound. By declaring an abstract method for calculating membership degrees, the design delegates the specific mathematical logic—such as triangular or trapezoidal functions—to subclasses while centralizing common state management. It integrates into the broader fuzzy description logic framework by identifying itself as a concrete entity type, thereby enabling the system to process quantitative data rather than purely qualitative or structural definitions.
