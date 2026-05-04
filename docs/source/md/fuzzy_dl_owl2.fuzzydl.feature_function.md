# Summary

A class representing mathematical expressions over features that supports arithmetic operations and converts them into linear programming constraints.

## Description

Software components representing mathematical expressions over features are defined here, supporting atomic variables, constants, and arithmetic operations such as summation, subtraction, and scalar multiplication. The design utilizes a polymorphic initialization strategy where the specific structure of the expression is determined by the types of arguments provided, allowing the creation of complex hierarchical trees from simple building blocks. This intermediate representation serves as a bridge between high-level feature definitions and low-level optimization constraints. To facilitate integration with optimization solvers, the logic includes functionality to recursively traverse the expression tree and extract all dependent feature names. Furthermore, the core capability involves converting these abstract definitions into concrete linear programming expressions by resolving atomic features to specific variables within the context of a given individual. This transformation relies on external helpers to map relationships between individuals to solver variables, ensuring that the mathematical model accurately reflects the semantic structure of the defined features.
