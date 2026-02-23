# Summary

Defines a graph entity for fuzzy description logic concepts that maintains global collections of equivalent names and weighted directed edges.

## Description

The software models individual concepts within a classification hierarchy, acting as the primary data structure for a fuzzy description logic reasoner. Instead of storing graph topology or synonyms on specific instances, the implementation utilizes class-level attributes to maintain a global state, meaning that modifications to names or edge weights affect the entire system rather than a single object. This design allows the entity to manage weighted directed connections representing inheritance or associations, while also supporting the identification of universal and empty concepts through specific naming conventions. Functionality includes adding or removing edges based on weight thresholds, retrieving immediate predecessors and successors, and generating string representations that account for multiple synonymous labels.
