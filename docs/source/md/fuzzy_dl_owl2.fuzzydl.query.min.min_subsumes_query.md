# Summary

A query mechanism that determines the minimum degree of subsumption between two fuzzy concepts within a knowledge base by solving a mixed-integer linear programming problem.

## Description

Software designed to compute the infimum truth value of a subsumption relationship between two concepts in a fuzzy description logic setting. It supports multiple fuzzy logic operators, including Łukasiewicz, Gödel, Kleene-Dienes, and Zadeh, translating the subsumption assertion into a corresponding logical implication for the selected logic. The reasoning process leverages mixed-integer linear programming to minimize the degree of implication, introducing specific variables and constraints to model the fuzzy logic rules within the knowledge base. Performance optimizations are integrated to bypass complex calculations when the knowledge base is pre-classified and the concepts are atomic, allowing for direct retrieval of results from the classification hierarchy. If the ontology is inconsistent or requires full computation, the system clones the knowledge base, applies preprocessing to formulate the optimization problem, and returns the calculated solution or an inconsistency flag.
