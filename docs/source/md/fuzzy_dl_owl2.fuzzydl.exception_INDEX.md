# Summary

A specialized exception hierarchy for handling errors and logical inconsistencies within fuzzy description logic frameworks.

## Description

Custom error types are defined to distinguish between general framework issues, such as invalid concept definitions, and specific logical conflicts like contradictory or unsatisfiable concepts. By extending the standard Python `Exception` class, these classes integrate seamlessly with native error handling workflows while enabling developers to implement granular control flow and debugging strategies. The architecture focuses on providing context-specific error messages that help identify the root cause of failures during ontology manipulation. This separation of concerns ensures that applications can manage domain-specific failures distinctly from generic runtime errors, leading to more robust and maintainable code.

## Modules

- [`fuzzy_dl_owl2.fuzzydl.exception.fuzzy_ontology_exception`](./fuzzydl_exception_fuzzy_ontology_exception.md) — A custom exception class designed to handle errors specific to the fuzzy description logic framework.
- [`fuzzy_dl_owl2.fuzzydl.exception.inconsistent_ontology_exception`](./fuzzydl_exception_inconsistent_ontology_exception.md) — A custom exception class designed to signal logical inconsistencies within fuzzy ontologies.
