# Summary

Calculates the minimal degree of satisfiability for a fuzzy concept using Mixed-Integer Linear Programming optimization.

## Description

The software determines the lowest possible truth degree at which a specific fuzzy concept remains satisfiable within a given ontology, either in isolation or relative to a particular individual. By extending the standard satisfiability logic, it transforms the logical verification process into a mathematical optimization problem that minimizes a variable representing the satisfiability threshold. During execution, the system clones the underlying knowledge base to preserve the original state, activates dynamic blocking if existential quantifiers are present, and constructs a specific objective expression to guide the solver. The optimization process ultimately yields a non-negative solution representing the minimal degree, or signals an inconsistency if the ontology cannot be satisfied under the given constraints.
