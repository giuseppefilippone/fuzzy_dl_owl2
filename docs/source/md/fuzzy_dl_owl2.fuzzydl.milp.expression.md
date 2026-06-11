# Summary

A linear algebraic representation class used to construct and manipulate mathematical expressions within a Mixed-Integer Linear Programming (MILP) framework.

## Description

The software implements a core algebraic structure representing linear forms, serving as the foundational primitive for defining constraints and objective functions in a Mixed-Integer Linear Programming (MILP) system. By encapsulating a constant term and a collection of variable terms, the logic enables the construction of complex mathematical equations through flexible initialization patterns that accept raw numbers, existing terms, or collections of variables. Operator overloading facilitates intuitive arithmetic manipulation, allowing for the addition, subtraction, and scalar multiplication of these linear forms while automatically merging coefficients when identical variables are combined. This design ensures that intermediate quantities are consistently represented as standardized objects before being translated into the specific inequality constraints required by the underlying solver.
