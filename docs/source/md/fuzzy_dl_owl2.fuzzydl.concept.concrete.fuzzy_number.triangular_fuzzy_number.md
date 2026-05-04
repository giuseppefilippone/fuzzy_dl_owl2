# Summary

A Python class representing triangular fuzzy numbers that supports arithmetic operations, logical comparisons, and defuzzification.

## Description

The software models uncertain values using a triangular membership function defined by three distinct parameters: a lower bound, a peak value where membership is absolute, and an upper bound. Instances can be created with or without a specific identifier, and the implementation relies on inheritance from a concrete concept base to manage the underlying data structure while enforcing strict type validation during initialization. Arithmetic capabilities are provided through operator overloading, allowing for addition, subtraction, multiplication, and division that generate new instances based on interval arithmetic principles rather than modifying the original objects. Beyond basic math, the implementation integrates with an operator concept handler to perform logical conjunctions, disjunctions, and negations, while also offering utilities to calculate a defuzzified crisp value known as the Best Non-Fuzzy Performance (BNP). Class-level attributes allow for the definition of a global range or universe of discourse, affecting how these numbers are identified and bounded across the system.
