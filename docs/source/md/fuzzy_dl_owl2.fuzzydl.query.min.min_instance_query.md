# Summary

Calculates the greatest lower bound of membership for a specific individual relative to a given concept by transforming the logical query into a Mixed-Integer Linear Programming (MILP) optimization problem.

## Description

The software implements a mechanism to determine the minimum truth value indicating how strongly a specific individual belongs to a particular concept within a fuzzy description logic framework. By extending the base instance query functionality, it transforms the logical problem into a mathematical optimization task, specifically utilizing a semi-continuous variable within a Mixed-Integer Linear Programming (MILP) solver to represent the degree of membership. During the preprocessing phase, the system introduces a linear constraint that links the negation of the target concept to this variable, ensuring the optimization process correctly minimizes the membership degree while respecting the ontology's axioms. To maintain data integrity and prevent unintended side effects, the execution process operates on a cloned version of the provided knowledge base, applying dynamic blocking strategies when existential quantifiers are detected and gracefully handling potential inconsistencies in the ontology.
