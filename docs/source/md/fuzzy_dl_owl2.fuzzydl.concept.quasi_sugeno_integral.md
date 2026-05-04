# Summary

Implements a Quasi-Sugeno integral operator that aggregates a collection of fuzzy concepts using specific weights.

## Description

The implementation extends the standard Sugeno integral logic to handle a specific variant of fuzzy aggregation, requiring a strict correspondence between a list of numerical weights and a list of input concepts. By inheriting from a base integral class, it reuses core initialization logic while defining a unique type identifier and a specific string serialization format that encapsulates both the weights and the constituent concepts. Logical operations such as negation, conjunction, and disjunction are supported through operator overloading, which delegates the actual computation to a central utility class to ensure consistency across different fuzzy logic constructs. Furthermore, the design includes mechanisms for creating independent copies of the instance and recursively replacing specific concepts within the structure, facilitating complex manipulations of the fuzzy logic hierarchy without altering the original state.
