# Summary

A Python class representing a linear term consisting of a coefficient and a variable for use in fuzzy description logic MILP formulations.

## Description

The software models a fundamental algebraic component used to construct linear expressions within fuzzy description logic ontologies, specifically representing the product of a numerical coefficient and a variable. Designed to facilitate mathematical operations on concept satisfaction degrees, the implementation supports standard arithmetic such as negation, addition, subtraction, and scalar multiplication or division. To maintain mathematical integrity, addition and subtraction operations are strictly constrained to ensure that only terms sharing the same variable can be combined, raising an error otherwise. Instances can be initialized either with an explicit coefficient and variable or with a variable alone, which implies a coefficient of 1.0, while the design also includes functionality for cloning objects and generating string representations for debugging or display.
