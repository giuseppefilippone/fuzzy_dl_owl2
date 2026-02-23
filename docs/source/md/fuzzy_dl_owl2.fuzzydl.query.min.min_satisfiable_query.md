# Summary

Calculates the minimal degree to which a fuzzy concept is satisfiable, either generally or for a specific individual, by transforming the logical problem into a Mixed-Integer Linear Programming optimization task.

## Description

The implementation extends the base satisfiability logic to function as a minimization problem, where the goal is to find the lowest truth value for a given concept within a fuzzy description logic ontology. By cloning the knowledge base before execution, the process prevents unintended side effects on the original data structure while allowing for optional inclusion or exclusion of the ABox based on configuration settings. To handle complex logical constructs, the system detects existential quantifiers to enable dynamic blocking and introduces a semi-continuous variable into the solver that serves as the objective for the optimization. The final solution is derived by minimizing this variable under constraints that link the negation of the concept to the variable's degree, with error handling in place to manage inconsistent ontologies and ensure the result is non-negative.
