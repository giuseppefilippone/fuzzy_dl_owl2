# Summary

Implements a data structure for handling quasi-Sugeno integral concepts within a fuzzy ontology framework.

## Description

The software defines a specialized component that models the quasi-Sugeno integral, a fuzzy logic operator used for weighted aggregation of multiple criteria. By extending a base definition class, it encapsulates a collection of numerical weights alongside a corresponding list of concept identifiers to represent the importance and structure of the aggregated elements. The implementation ensures that the specific operator type is registered during initialization and exposes the internal data through accessor methods to support downstream logical processing. Furthermore, the logic includes a string serialization mechanism that formats the weights and concepts into a parenthetical expression suitable for parsing or display within the broader system.
