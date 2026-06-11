# Summary

A class representing a linear term defined by a coefficient and a variable, designed to construct mathematical expressions within fuzzy description logic ontologies.

## Description

The software implements a fundamental algebraic component used to build linear expressions, specifically tailored for representing concept satisfaction degrees in fuzzy description logic ontologies. By encapsulating a numerical coefficient and a variable, the design allows for the construction of complex mathematical models where terms can be manipulated through standard arithmetic operations such as negation, addition, subtraction, and scalar multiplication. Strict type checking and validation are enforced during initialization to ensure that terms are constructed correctly, either with an explicit coefficient or with a default value of 1.0. To maintain mathematical integrity, operations like addition and subtraction are restricted to terms sharing the same variable, while scalar operations return new instances to preserve the immutability of the original objects. The implementation also includes hashing and equality comparisons, enabling these objects to be used effectively within sets and dictionaries as part of larger optimization algorithms.
