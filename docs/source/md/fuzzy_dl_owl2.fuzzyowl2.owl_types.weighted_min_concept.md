# Summary

Implements a weighted minimum aggregation operator within the FuzzyOWL2 framework to construct complex fuzzy concepts by combining a collection of sub-concepts.

## Description

The software models a specific type of fuzzy logic operator that aggregates multiple concept definitions using a weighted minimum strategy. By inheriting from the base definition class, it integrates seamlessly into the broader ontology structure while specifically identifying itself as a weighted minimum type. Internally, the logic maintains a collection of component concepts that serve as the operands for the aggregation, allowing these elements to be retrieved and manipulated as a group. For display and serialization purposes, the implementation generates a human-readable string representation that prefixes the aggregated components with "w-min" to clearly denote the operation being performed.
