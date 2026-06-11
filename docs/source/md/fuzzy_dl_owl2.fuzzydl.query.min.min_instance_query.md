# Summary

A query mechanism that computes the minimum membership degree of an individual for a given concept by formulating and solving a mixed-integer linear programming problem.

## Description

The implementation extends the standard instance query logic to specifically target the greatest lower bound of truth values within a fuzzy description logic framework. To achieve this, the system introduces a semi-continuous variable into the optimization model and establishes a linear constraint that links the negation of the target concept to this variable, effectively minimizing the objective to find the lower bound. The resolution process ensures data integrity by cloning the knowledge base before applying transformations, handles dynamic blocking for existential restrictions, and gracefully manages inconsistent ontology states by returning a specific solution type rather than propagating exceptions.
