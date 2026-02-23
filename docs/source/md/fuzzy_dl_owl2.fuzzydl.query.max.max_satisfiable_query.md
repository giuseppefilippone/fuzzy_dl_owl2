# Summary

A query mechanism that calculates the maximal degree of satisfiability for a fuzzy concept within a fuzzy description logic knowledge base, optionally scoped to a specific individual.

## Description

Software defined here extends standard satisfiability checking by formulating a Mixed-Integer Linear Programming (MILP) optimization problem to find the highest possible truth value for a given concept. The implementation supports two modes of operation: general satisfiability, where a new individual is generated to test the concept in isolation, and instance checking, where the query is scoped to a specific existing individual. To ensure the integrity of the original data, execution operates on a cloned version of the knowledge base, applying preprocessing steps such as dynamic blocking for complex logical constructs like universal quantifiers. Core optimization involves constructing an objective expression that maximizes the variable associated with the concept and individual, ultimately returning a solution that represents the optimal satisfaction degree or indicates an inconsistent ontology.
