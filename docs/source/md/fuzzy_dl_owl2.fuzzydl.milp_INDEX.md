# Summary

A mathematical modeling framework that translates fuzzy description logic constructs into mixed-integer linear programming problems for optimization and consistency checking.

## Description

Algebraic primitives such as symbolic variables, linear terms, and mathematical expressions form the foundational layer, enabling the representation of satisfaction degrees and constraints through operator overloading and automatic term consolidation. A central management layer bridges the gap between abstract fuzzy logic entities and mathematical optimization models by generating unique identifiers, enforcing specific constraints like crispness and cardinality, and abstracting interactions with external solver backends such as Gurobi, Python-MIP, and PuLP. To handle complex scenarios, the architecture supports graph-based partitioning for decomposing large models into manageable sub-problems while maintaining granular control over variable visibility and display settings through configuration management. Query outcomes are encapsulated to distinguish between numerical satisfaction degrees and knowledge base consistency, providing access to variable bindings and detailed result states for analysis.

## Modules

- [`fuzzy_dl_owl2.fuzzydl.milp.expression`] — A linear mathematical expression model represents the degree of satisfaction of concepts within fuzzy description logic ontologies.
- [`fuzzy_dl_owl2.fuzzydl.milp.inequation`] — Encapsulates mathematical inequalities of the form expression compared to zero for use in fuzzy description logic ontologies.
- [`fuzzy_dl_owl2.fuzzydl.milp.milp_helper`] — A comprehensive manager for Mixed-Integer Linear Programming (MILP) problems that translates high-level fuzzy logic constructs into mathematical optimization models and interfaces with various solver backends.
- [`fuzzy_dl_owl2.fuzzydl.milp.show_variables_helper`] — A configuration manager controls the visibility and display settings of variables, concepts, individuals, and role fillers within a fuzzy description logic system.
- [`fuzzy_dl_owl2.fuzzydl.milp.solution`] — Encapsulates the outcome of a query performed on a fuzzy knowledge base, distinguishing between a numerical degree of satisfaction and the consistency status of the base itself.
- [`fuzzy_dl_owl2.fuzzydl.milp.term`] — A Python class representing a linear term consisting of a coefficient and a variable for use in fuzzy description logic MILP formulations.
- [`fuzzy_dl_owl2.fuzzydl.milp.variable`] — A symbolic variable class for linear expressions that manages types, bounds, and naming within mixed-integer linear programming contexts.
