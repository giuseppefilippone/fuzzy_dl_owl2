# Summary

A class that retrieves all individuals belonging to a specific concept within a fuzzy knowledge base and calculates their respective degrees of membership.

## Description

The implementation focuses on identifying all entities within a knowledge base that satisfy a given abstract concept, quantifying the relationship through fuzzy membership values rather than binary classification. By leveraging the underlying fuzzy logic framework, the logic evaluates the extent to which each individual satisfies the concept criteria, ensuring that concrete concepts are rejected during initialization. Two distinct algorithms are provided for determining these degrees: an iterative approach that solves a minimum instance query for each entity sequentially, and an optimized method that utilizes Mixed-Integer Linear Programming (MILP) to calculate all degrees in a single optimization pass by introducing semi-continuous variables. Throughout the process, the logic maintains consistency checks on the ABox and filters out dynamically created individuals, ultimately aggregating the results into accessible lists of entities and their corresponding membership scores.
