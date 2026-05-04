# Summary

Implements a weighted minimum aggregation operator within the FuzzyOWL2 framework to construct complex fuzzy concepts from a collection of sub-concepts.

## Description

The software models a specific type of fuzzy logic operator known as a weighted minimum, which is essential for constructing complex concepts by aggregating multiple sub-concepts within the FuzzyOWL2 framework. By inheriting from the base concept definition, it establishes itself as a distinct entity capable of holding a collection of component concepts that are subject to this specific aggregation logic. Internally, the implementation maintains a list of these component definitions, allowing the structure to represent hierarchical relationships where the overall truth value is derived from the weighted minimum of its parts. Functionality includes providing access to the underlying collection of concepts and generating a human-readable string representation that explicitly denotes the weighted minimum operation using a specific parenthetical syntax.
