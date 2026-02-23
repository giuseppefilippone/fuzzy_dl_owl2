# Summary

A Python class representing a linear term defined by a coefficient and a variable, designed to construct mathematical expressions for fuzzy description logic ontologies.

## Description

The software models a fundamental algebraic component used within mixed-integer linear programming formulations for fuzzy description logic ontologies. It encapsulates a numerical coefficient and a variable, allowing instances to be created either with an explicit multiplier or by defaulting to a coefficient of 1.0 when only a variable is provided. Arithmetic operations such as negation, scalar multiplication, and division are fully supported to facilitate the construction of complex linear expressions. However, addition and subtraction are strictly constrained to ensure mathematical consistency, raising an error if an attempt is made to combine terms that reference different variables. The implementation also includes functionality for cloning instances and generating hash values based on string representations, enabling the use of these objects within sets and dictionaries.
