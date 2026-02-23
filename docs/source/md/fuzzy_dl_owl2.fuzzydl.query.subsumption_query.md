# Summary

An abstract base class defines the structure for evaluating fuzzy subsumption relationships between two concepts.

## Description

Designed to operate within a fuzzy description logic framework, the software establishes a foundational structure for determining the degree to which one concept is subsumed by another. By accepting a pair of concepts and a specific fuzzy implication operator, it prepares the necessary context for evaluating logical relationships where validity is measured on a spectrum rather than as a binary state. A critical design aspect involves strict validation during initialization to ensure that both the subsumed and the subsumer are abstract concepts, as concrete concepts are incompatible with this type of hierarchical query. Once validated, the components are stored alongside a placeholder for the objective expression, allowing concrete subclasses to perform the actual mathematical formulation of the subsumption degree.
