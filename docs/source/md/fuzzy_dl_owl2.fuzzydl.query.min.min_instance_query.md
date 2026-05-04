# Summary

Calculates the greatest lower bound of membership for a specific individual relative to a given concept using Mixed-Integer Linear Programming optimization.

## Description

The software models a query designed to retrieve the greatest lower bound of the degree of membership for a specific individual relative to a given concept. It functions by transforming the logical query into an optimization problem, specifically utilizing a semi-continuous variable to represent the degree of membership. Execution involves cloning the current knowledge base to prevent side effects, applying necessary constraints, and performing an optimization to calculate the result. The implementation includes specific handling for existential restrictions and manages inconsistent ontology states by returning a designated solution type.
