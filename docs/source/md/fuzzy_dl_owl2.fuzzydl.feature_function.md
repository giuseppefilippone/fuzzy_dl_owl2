# Summary

A polymorphic class representing mathematical expressions over features that can be recursively traversed to extract dependencies and converted into linear programming constraints.

## Description

It acts as an intermediate representation for mathematical logic involving atomic features, constants, and arithmetic operations like summation, subtraction, and scalar multiplication. The design relies on a flexible initialization strategy where the specific structure of the expression—whether it is a simple variable, a constant, or a complex composite operation—is determined by the types and quantities of arguments provided at instantiation. Internally, these expressions form a tree-like structure that allows for recursive traversal to gather all unique feature names required for evaluation. Crucially, the software bridges the gap between abstract feature definitions and concrete optimization models by translating these symbolic expressions into solver-compatible linear expressions, resolving atomic features against specific individuals and their relations within a mixed-integer linear programming context.
