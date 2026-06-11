# Summary

A specialized definition that aggregates multiple fuzzy concepts into a weighted sum structure within the FuzzyOWL2 framework.

## Description

Extending the base definition for fuzzy logic constructs, the software facilitates the creation of complex concepts by combining a collection of existing definitions into a single aggregated entity. It specifically targets scenarios where a concept is defined through a weighted summation, distinguishing this logical operation from other types of relationships within the ontology. During initialization, the entity is explicitly marked with a type identifier corresponding to a weighted sum, which allows reasoning engines or serialization tools to correctly interpret the structure. The stored collection of concepts can be retrieved for further processing, and the internal state is represented textually using a specific notation that encapsulates the components within a parenthesized prefix.
