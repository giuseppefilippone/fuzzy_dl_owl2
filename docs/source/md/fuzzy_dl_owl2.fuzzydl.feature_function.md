# Summary

A class representing mathematical expressions over features that supports arithmetic operations and conversion into linear programming constraints.

## Description

Software components defined here provide a mechanism to construct and manipulate mathematical expressions involving atomic features, constants, and arithmetic operations such as summation, subtraction, and scalar multiplication. The design utilizes a polymorphic initialization strategy where the specific structure of the expression—whether it is a simple variable, a numeric constant, or a complex composite operation—is determined dynamically based on the types and quantities of arguments provided during instantiation. This intermediate representation allows for recursive traversal to extract dependencies, such as collecting all unique feature names referenced within the expression tree. Furthermore, the logic includes functionality to translate these abstract definitions into concrete linear programming expressions by resolving atomic features to solver variables using the relational context of a specific individual and a helper utility for mixed-integer linear programming (MILP) models.
