# Summary

A symbolic wrapper for algebraic expressions that functions as a non-numeric degree within a fuzzy logic system, enabling dynamic satisfaction measures through mathematical manipulation.

## Description

The software implements a mechanism to handle degrees of truth or satisfaction that are not fixed numbers but are instead defined by symbolic algebraic expressions. By encapsulating an `Expression` object, the implementation allows these degrees to participate in complex mathematical operations such as addition, subtraction, and scalar multiplication, which are essential for formulating constraints in mixed-integer linear programming models. Unlike concrete numeric degrees, this symbolic approach treats the degree as a dynamic entity that can be compared against other expressions to generate inequalities, thereby facilitating the construction of logical constraints within the broader fuzzy logic framework. The design explicitly identifies these entities as non-numeric to ensure correct handling during type checking and evaluation, while still supporting standard object-oriented features like cloning, hashing, and equality comparison based on the underlying expression.
