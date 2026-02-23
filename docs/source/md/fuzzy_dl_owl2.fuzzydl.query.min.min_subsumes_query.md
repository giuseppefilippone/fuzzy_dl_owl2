# Summary

Calculates the minimum degree of subsumption between two fuzzy concepts within a knowledge base using mixed-integer linear programming.

## Description

The software determines the infimum truth value of the assertion that one concept is subsumed by another, supporting various fuzzy logic operators such as Łukasiewicz, Gödel, Kleene-Dienes, and Zadeh. By translating the subsumption relationship into a logical implication, the system formulates a mixed-integer linear programming problem to minimize the degree of the implication. The solving process includes optimizations where pre-classified knowledge bases allow for direct retrieval of results from the classification hierarchy when dealing with atomic concepts. In more complex scenarios, the logic clones the knowledge base, introduces specific variables and assertions to represent the implication constraints, and executes an optimization routine to compute the solution or identify inconsistencies.
