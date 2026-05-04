# Summary

A query mechanism that determines the minimum degree to which two individuals are related through a specific role within a fuzzy description logic knowledge base.

## Description

The software implements a specialized query for fuzzy description logic ontologies, specifically designed to compute the minimum membership degree of a role assertion between two distinct individuals. By leveraging mixed-integer linear programming, the system constructs an optimization problem where the objective is to minimize the degree variable associated with the relationship. To ensure the integrity of the original data, the process operates on a cloned instance of the knowledge base, allowing for the addition of temporary assertions and constraints without side effects. The logic involves transforming the role relationship into a concept expression, integrating it into the solver, and handling potential ontology inconsistencies by returning a specific status rather than raising an error.
