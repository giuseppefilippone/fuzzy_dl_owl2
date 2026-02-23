# Summary

A custom exception class designed to signal logical inconsistencies within fuzzy ontologies.

## Description

A specialized error type is utilized within fuzzy description logic frameworks to indicate that a logical conflict has arisen, such as contradictory concept definitions or unsatisfiable concepts. By extending the standard Python exception hierarchy, it allows developers to catch and manage ontology-specific errors distinctly from generic runtime failures. Accepting a descriptive string during instantiation facilitates precise debugging by providing context regarding the specific nature of the inconsistency. Integration of this mechanism ensures that ontology management systems can gracefully handle complex logical errors while maintaining compatibility with standard error handling workflows.
