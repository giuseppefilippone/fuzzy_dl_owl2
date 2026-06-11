# Summary

A specialized implementation of a fuzzy logic operator that models the quasi-Sugeno integral by aggregating weighted concepts.

## Description

Extending the base definition for fuzzy concepts, the software models the quasi-Sugeno integral by maintaining a collection of numerical weights alongside a list of associated concept identifiers. Encapsulation of the parameters required for weighted aggregation ensures that the coefficients determine the influence of each corresponding concept within the fuzzy logic operation. External logic can retrieve the specific coefficients and criteria through dedicated accessors that expose the internal state without modification. To support serialization and interoperability, the data is formatted into a parenthetical string representation that explicitly labels the operator type and lists the weights and concepts in sequence.
