# Summary

A Mixed-Integer Linear Programming framework designed to translate fuzzy description logic ontologies into solvable mathematical optimization models.

## Description

Mathematical constructs such as variables, terms, and linear expressions are modeled to represent degrees of satisfaction and constraints inherent in fuzzy logic systems. A central management component orchestrates the translation of high-level logical definitions—like concepts, roles, and individuals—into concrete optimization problems while abstracting the interface to various external solver backends. Advanced capabilities include the normalization of inequalities, the partitioning of constraint graphs to enhance performance, and the handling of crisp versus fuzzy elements alongside nominal variables. Query results are encapsulated to distinguish between numerical satisfaction degrees and system inconsistency, while a separate configuration utility controls the visibility and display of ontology components during processing.

## Modules

- [`fuzzy_dl_owl2.fuzzydl.milp.expression`](./fuzzydl_milp_expression.md) — A Python class representing linear mathematical expressions used within fuzzy description logic constraints to model degrees of satisfaction.
- [`fuzzy_dl_owl2.fuzzydl.milp.inequation`](./fuzzydl_milp_inequation.md) — Encapsulates a mathematical inequality of the form expression compared to zero, typically used within fuzzy description logic ontologies.
- [`fuzzy_dl_owl2.fuzzydl.milp.milp_helper`](./fuzzydl_milp_milp_helper.md) — A comprehensive manager for Mixed-Integer Linear Programming problems that translates fuzzy logic constructs into mathematical optimization models and interfaces with various solver backends.
- [`fuzzy_dl_owl2.fuzzydl.milp.show_variables_helper`](./fuzzydl_milp_show_variables_helper.md) — A configuration manager that controls the visibility and display of elements within a fuzzy description logic ontology, including atomic concepts, individuals, abstract roles, and concrete features.
- [`fuzzy_dl_owl2.fuzzydl.milp.solution`](./fuzzydl_milp_solution.md) — Encapsulates the outcome of a query performed on a fuzzy knowledge base, distinguishing between numerical satisfaction degrees and the consistency status of the base itself.
- [`fuzzy_dl_owl2.fuzzydl.milp.term`](./fuzzydl_milp_term.md) — A Python class representing a linear term defined by a coefficient and a variable, designed to construct mathematical expressions for fuzzy description logic ontologies.
- [`fuzzy_dl_owl2.fuzzydl.milp.variable`](./fuzzydl_milp_variable.md) — A symbolic variable class designed for linear expressions within mixed-integer linear programming contexts, specifically to represent degrees of satisfaction in fuzzy description logic ontologies.
