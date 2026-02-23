# Summary

A Python class that models triangular fuzzy numbers, providing arithmetic and logical operations alongside utilities for defuzzification and range management.

## Description

The software models uncertain numerical values using a triangular membership function defined by three distinct parameters representing the lower bound, the peak, and the upper bound. It supports flexible initialization, allowing instances to be created either with or without an explicit string identifier, while enforcing strict validation on the input types and argument counts. Arithmetic operations such as addition, subtraction, multiplication, and division are implemented to produce new instances based on interval arithmetic principles, ensuring that the original operands remain unmodified. Furthermore, the logic integrates with a broader framework by delegating fuzzy logical operations like conjunction and disjunction to an external operator handler, while also providing utilities for defuzzification through the calculation of the Best Non-Fuzzy Performance. Class-level configuration allows for the definition of a global range or universe of discourse, which influences how these fuzzy numbers are identified and managed within the system.
