# Summary

Retrieves all individuals from a knowledge base that are instances of a specified concept and calculates their respective fuzzy membership degrees.

## Description

The software provides a mechanism to query a knowledge base for all entities that belong to a given abstract concept, determining the extent to which each entity satisfies the concept criteria using fuzzy logic principles. Instead of a binary classification, the system calculates a specific membership degree for every individual, allowing for nuanced retrieval based on partial satisfaction of the concept definition. Two distinct algorithms are implemented to perform these calculations: an iterative approach that solves a minimum instance query for each entity sequentially, and an optimization-based approach that utilizes Mixed-Integer Linear Programming (MILP) to maximize the sum of membership variables across all individuals simultaneously. Before execution, the system ensures the underlying ontology is consistent, and it dynamically manages the creation of variables and assertions within the mathematical model to accurately reflect the relationships between individuals and the target concept.
