# Summary

A custom exception class designed to signal logical inconsistencies detected within fuzzy ontologies during description logic processing.

## Description

Specialized error handling is provided for fuzzy description logic frameworks where logical conflicts, such as contradictory concept definitions or unsatisfiable concepts, must be explicitly managed. By extending the standard Python exception base class, the implementation ensures that these domain-specific errors integrate seamlessly with native error catching and propagation mechanisms. The constructor accepts a descriptive string argument, allowing developers to pass specific context regarding the nature of the inconsistency to facilitate precise debugging and system recovery. This approach abstracts the complexity of ontology validation failures into a distinct error type, making it easier to distinguish logical flaws from other runtime issues in complex reasoning systems.
