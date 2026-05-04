# Summary

Defines a graph node entity for modeling concepts in a classification hierarchy with shared global state for names and weighted relationships.

## Description

The software models individual concepts within a classification hierarchy, acting as the primary data structure for a fuzzy description logic reasoner. Instead of maintaining instance-specific data, the implementation relies on class-level attributes to store equivalent names and weighted directed edges, meaning that all instances share a single global state for the graph topology and nomenclature. This design allows the system to manage relationships such as inheritance or association by tracking input and output connections with floating-point weights, while also supporting the identification of universal and empty concepts through specific naming conventions. Functionality includes the ability to add or remove edges based on threshold values, retrieve immediate predecessors or successors, and generate string representations that account for single or multiple synonymous labels.
