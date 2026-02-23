# Summary

A reasoning query that computes the maximum degree of membership for a specific individual within a given concept by solving a mixed-integer linear programming optimization problem.

## Description

Extending the base instance query functionality, this component focuses on determining the highest possible truth value supported by the knowledge base for a specific entity belonging to a particular class. The design relies on constructing a mathematical optimization problem where the objective is to maximize the variable representing the membership degree, which involves transforming the logic into a mixed-integer linear programming format. To ensure the integrity of the original data, the reasoning process operates on a cloned version of the knowledge base, allowing for the addition of specific assertions and the application of dynamic blocking strategies required for handling complex logical constructs like universal quantification. Execution involves solving the ABox constraints first, followed by the optimization step, with robust error handling to return a specific status if the underlying ontology is found to be inconsistent.
