# Summary

A suite of fuzzy logic optimization queries that compute maximum truth values for concepts, individuals, and relationships using mixed-integer linear programming.

## Description

These components operate within a fuzzy description logic framework to determine the upper bounds of truth values for various logical constructs, including concept subsumption, individual instance checking, and relationship assertions. By leveraging Mixed-Integer Linear Programming (MILP), the architecture translates fuzzy semantic constraints into solvable mathematical optimization problems, often cloning the underlying knowledge base to ensure the original state remains unaltered during the calculation. The implementation handles complex logical requirements, such as universal restrictions, through dynamic blocking strategies and supports various fuzzy logic operators like Łukasiewicz and Gödel to define specific implication constraints. Robust error management is integrated throughout to gracefully handle inconsistent ontologies, ensuring that optimization failures return specific status indicators rather than causing runtime errors.

## Modules

- [`fuzzy_dl_owl2.fuzzydl.query.max.max_instance_query`] — A reasoning query that computes the maximum degree of membership for a specific individual within a given concept using mixed-integer linear programming.
- [`fuzzy_dl_owl2.fuzzydl.query.max.max_query`] — A query operation that determines the maximum possible value of a specific expression while maintaining consistency with a fuzzy knowledge base.
- [`fuzzy_dl_owl2.fuzzydl.query.max.max_related_query`] — A query mechanism that calculates the maximum degree of truth for a specific relationship between two individuals within a fuzzy knowledge base.
- [`fuzzy_dl_owl2.fuzzydl.query.max.max_satisfiable_query`] — A fuzzy logic query mechanism that calculates the maximal satisfiability degree of a concept within a knowledge base using mixed-integer linear programming.
- [`fuzzy_dl_owl2.fuzzydl.query.max.max_subsumes_query`] — Determines the maximum degree to which one fuzzy concept is subsumed by another by formulating and solving a Mixed-Integer Linear Programming optimization problem.
