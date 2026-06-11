# Summary

A graph node entity that models concepts within a classification hierarchy, managing global collections of equivalent names and weighted directed edges for a fuzzy description logic reasoner.

## Description

Implementation relies on class-level attributes to store all names and edge weights, creating a shared global state where modifications affect the entire graph structure regardless of the specific instance used. This design facilitates the management of complex relationships, such as inheritance or association, by updating central registries for input and output edges, while also supporting the removal of connections based on specific weight thresholds. Special logic identifies universal and empty concepts through sentinel naming conventions, and the system ensures consistent identity management by deriving hash values and string representations directly from the global set of synonyms.
