# Summary

A query mechanism that computes the minimum degree of subsumption between two fuzzy concepts within a knowledge base by formulating and solving a mixed-integer linear programming problem.

## Description

The software determines the infimum truth value for the assertion that one concept is subsumed by another, supporting various fuzzy logic operators such as Łukasiewicz, Gödel, Kleene-Dienes, and Zadeh. To achieve this, the implementation translates the subsumption relationship into a logical implication specific to the selected logic operator and formulates a mixed-integer linear programming problem to minimize the resulting degree. Performance is optimized by checking if the knowledge base is pre-classified and the concepts are atomic, allowing the system to retrieve results directly from the classification hierarchy without full optimization. When direct retrieval is not possible, the system clones the knowledge base, introduces a semi-continuous variable to represent the degree of subsumption, and adds necessary assertions before executing the optimization routine to compute the final solution or flag inconsistencies.
