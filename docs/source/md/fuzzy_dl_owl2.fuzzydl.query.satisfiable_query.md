# Summary

A base class representing min/max satisfiability queries for fuzzy concepts within a logic framework.

## Description

Designed to function as an abstract interface, the software evaluates the degree to which a specific fuzzy concept is satisfied, optionally within the context of a particular individual. Strict validation rules ensure that the target concept is not concrete, thereby maintaining logical consistency during the evaluation process. Method overloading supports flexible initialization, allowing queries to be constructed with just a concept or with both a concept and an individual. Internal state management stores the relevant concept, individual, and a placeholder for the resulting objective expression, preparing the groundwork for subsequent satisfiability checks and bound calculations.
