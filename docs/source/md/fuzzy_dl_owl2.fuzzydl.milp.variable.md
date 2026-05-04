# Summary

A symbolic variable class for linear expressions that manages types, bounds, and naming within mixed-integer linear programming contexts.

## Description

Symbolic variables used within linear expressions are modeled to represent degrees of satisfaction in fuzzy description logic ontologies. The implementation encapsulates essential properties such as a unique identifier, a specific domain type, and corresponding lower and upper bounds that are automatically adjusted based on the variable's classification. By supporting various types including binary, integer, continuous, and semi-continuous, the design ensures that constraints are applied correctly without requiring manual configuration of numeric limits for every instance. Instantiation can be performed directly or through static factory methods that streamline the creation of specific variable types, while a class-level counter facilitates the automatic generation of unique sequential names. The logic includes functionality to flag specific instances as datatype fillers and supports cloning to create independent copies, which is useful for maintaining state integrity during complex manipulations. Equality and hashing operations rely on the string representation of the variable, ensuring that instances are distinguished primarily by their assigned names within hash-based collections.
