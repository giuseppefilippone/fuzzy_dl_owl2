# Summary

Determines the maximum degree to which one fuzzy concept is subsumed by another by formulating and solving a Mixed-Integer Linear Programming optimization problem.

## Description

Functionality is provided to calculate the maximum truth value for which one fuzzy concept implies another, extending standard subsumption reasoning into the fuzzy domain. Support for various fuzzy logic operators, such as Łukasiewicz and Gödel, enables the construction of specific implication concepts that define the semantic constraints of the query. Execution involves cloning the knowledge base to preserve the original state, followed by the creation of an objective expression that minimizes the degree of the derived implication within a Mixed-Integer Linear Programming model. The optimization process yields the precise maximum subsumption degree, while error handling mechanisms manage scenarios involving inconsistent ontologies.
