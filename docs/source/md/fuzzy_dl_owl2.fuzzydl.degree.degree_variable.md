# Summary

A symbolic wrapper for algebraic variables allows degrees of satisfaction in a fuzzy logic system to be treated as unknowns that must be solved for rather than fixed constants.

## Description

By encapsulating a `Variable` instance, the implementation enables the degree to participate in linear mathematical operations, such as addition, subtraction, and scalar multiplication, by generating the necessary `Term` and `Expression` objects required by the underlying solver. The design explicitly distinguishes symbolic degrees from numeric values, ensuring that type-checking methods correctly identify the entity as non-numeric while still allowing it to act as a right-hand side operand in inequality constraints. Through factory methods and cloning capabilities, the class facilitates the construction of complex constraint systems where satisfaction levels are dynamically determined during the solving process. Equality and hashing behaviors are delegated directly to the underlying variable to ensure consistency within hash-based collections used during constraint generation.
