# Summary

A Mixed-Integer Linear Programming framework designed to translate fuzzy description logic constructs into solvable mathematical optimization models.

## Description

The architecture relies on a hierarchy of algebraic primitives—ranging from symbolic variables and linear terms to complex expressions—to construct objective functions and constraints through intuitive operator overloading. A central management layer bridges the gap between abstract fuzzy logic concepts and concrete solver backends, handling variable registries, constraint translation, and interfacing with external libraries like Gurobi or PuLP. Supporting infrastructure ensures that query results are encapsulated with consistency status and variable bindings, while configuration utilities manage the visibility and display of ontology components during analysis.

## Modules

- [`fuzzy_dl_owl2.fuzzydl.milp.expression`] — A linear algebraic representation class used to construct and manipulate mathematical expressions within a Mixed-Integer Linear Programming (MILP) framework.
- [`fuzzy_dl_owl2.fuzzydl.milp.inequation`] — Encapsulates linear constraints of the form $E \bowtie 0$ within a mixed-integer linear programming framework, normalizing the right-hand side to zero while supporting equality, less-than, and greater-than relations.
- [`fuzzy_dl_owl2.fuzzydl.milp.milp_helper`] — A comprehensive manager for Mixed-Integer Linear Programming problems that translates fuzzy description logic constructs into mathematical optimization models and interfaces with various external solvers.
- [`fuzzy_dl_owl2.fuzzydl.milp.show_variables_helper`] — A configuration manager that controls the visibility and display settings for concepts, individuals, roles, and variables within a fuzzy description logic ontology.
- [`fuzzy_dl_owl2.fuzzydl.milp.solution`] — A data container encapsulates the outcome of a query on a fuzzy knowledge base, distinguishing between a numerical degree of satisfaction and the logical consistency status of the base.
- [`fuzzy_dl_owl2.fuzzydl.milp.term`] — A class representing a linear term defined by a coefficient and a variable, designed to construct mathematical expressions within fuzzy description logic ontologies.
- [`fuzzy_dl_owl2.fuzzydl.milp.variable`] — Defines a symbolic variable structure used to represent degrees of satisfaction within linear expressions for fuzzy description logic ontologies.
