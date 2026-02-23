# Summary

A framework for converting fuzzy membership degrees into crisp numerical values using Mixed-Integer Linear Programming strategies.

## Description

Defuzzification logic transforms fuzzy membership degrees into precise numbers for specific features within a knowledge base, relying on Mixed-Integer Linear Programming to solve the optimization problems. An abstract base class centralizes the common workflow, such as determining the maximum degree of satisfaction, asserting values into a cloned knowledge base, and managing ontology inconsistencies. By delegating the creation of objective expressions to subclasses, the architecture supports various defuzzification strategies while maintaining a consistent mechanism for retrieving variables and interacting with the solver. Concrete implementations utilize this structure to apply specific mathematical approaches, such as minimizing or maximizing target variables to find the smallest or largest maxima, or calculating the arithmetic mean of boundaries within the plateau of maximum membership.

## Modules

- [`fuzzy_dl_owl2.fuzzydl.query.defuzzify.defuzzify_query`](./fuzzydl_query_defuzzify_defuzzify_query.md) — An abstract base class that implements the logic for converting fuzzy membership degrees into crisp values for specific features within a knowledge base using Mixed-Integer Linear Programming.
- [`fuzzy_dl_owl2.fuzzydl.query.defuzzify.lom_defuzzify_query`](./fuzzydl_query_defuzzify_lom_defuzzify_query.md) — Implements the Largest of Maxima defuzzification strategy to derive crisp numerical values from fuzzy membership functions by maximizing the target variable in an optimization context.
- [`fuzzy_dl_owl2.fuzzydl.query.defuzzify.mom_defuzzify_query`](./fuzzydl_query_defuzzify_mom_defuzzify_query.md) — Implements the Mean of Maxima defuzzification strategy to calculate a crisp feature value for an individual within a fuzzy ontology.
- [`fuzzy_dl_owl2.fuzzydl.query.defuzzify.som_defuzzify_query`](./fuzzydl_query_defuzzify_som_defuzzify_query.md) — A query implementation that applies the Smallest of Maxima defuzzification strategy to resolve fuzzy feature values into crisp numerical outputs.
