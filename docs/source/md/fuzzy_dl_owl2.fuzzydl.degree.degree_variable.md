# Summary

Encapsulates a symbolic variable to represent a dynamic degree of satisfaction for use in algebraic expressions and constraints.

## Description

The software provides a mechanism to treat degrees of satisfaction as symbolic algebraic variables rather than fixed numeric constants, enabling dynamic constraint solving within a fuzzy logic framework. By wrapping a `Variable` instance, the implementation allows these symbolic degrees to participate in the construction of linear expressions and inequalities, effectively bridging the gap between abstract fuzzy logic concepts and Mixed-Integer Linear Programming (MILP) formulations. Design choices ensure that the entity is explicitly identified as non-numeric, preventing it from being confused with concrete values during type checking or evaluation phases. Furthermore, the logic supports standard algebraic operations such as addition, subtraction, and scalar multiplication, which are essential for building complex constraints where the satisfaction level must be determined by a solver rather than hardcoded.
