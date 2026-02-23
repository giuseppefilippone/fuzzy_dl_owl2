# Summary

An abstract base class defines the structure and behavior for fuzzy concepts operating over specific numerical intervals.

## Description

Designed to serve as a foundational template for fuzzy logic operations, the class manages a numerical domain characterized by a lower bound and an upper bound. It ensures data integrity by validating that the upper bound is never set lower than the lower bound, preventing the creation of invalid mathematical ranges. As a concrete concept type, it distinguishes itself from abstract concepts by operating directly on numerical data rather than logical relationships, and it explicitly signals its nature through a dedicated type identifier. The core functionality relies on an abstract method that forces subclasses to define the specific mathematical function used to calculate the degree of membership for a given value, allowing for various fuzzy shapes like triangular or trapezoidal distributions. Standard operations for retrieving atomic concepts or roles are implemented to return empty collections, reflecting the fact that these concrete numerical entities do not decompose into further conceptual hierarchies.
