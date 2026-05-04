# Summary

Retrieves all individuals from a knowledge base that satisfy a specified concept and calculates their corresponding fuzzy membership degrees.

## Description

Software designed to retrieve all entities from a knowledge base that satisfy a specific conceptual definition, operating within a fuzzy logic framework where membership is represented by a degree rather than a binary value. It extends the base query functionality to handle complex retrieval tasks by accepting a target concept and evaluating every individual in the ontology to determine the extent to which they satisfy the criteria. The implementation ensures that the input concept is abstract rather than concrete, enforcing structural constraints on the query definition to maintain logical validity.

The core logic involves iterating through the individuals of the knowledge base and calculating the minimum degree of membership for each relative to the target concept. Two distinct solving strategies are provided: a standard approach that executes a minimum instance query for every individual sequentially, and an advanced optimization method that constructs a Mixed Integer Linear Programming (MILP) model to solve for all degrees simultaneously. The optimization approach introduces semi-continuous variables for each individual, links them to the concept via assertions, and maximizes the sum of these variables to determine the most accurate membership values.

Consistency checks are performed prior to calculation to ensure the ABox of the knowledge base is valid, returning a specific error state if the ontology is found to be inconsistent. Results are stored internally, mapping individuals to their calculated degrees, and can be accessed to view the fuzzy classification of the entire population. The design integrates tightly with the underlying MILP solver and knowledge base structure, allowing for efficient batch processing of instance retrieval queries.
