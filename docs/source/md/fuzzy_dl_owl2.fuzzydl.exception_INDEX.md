# Summary

Specialized exception handling mechanisms for managing errors specific to fuzzy description logic and ontology operations.

## Description

These components extend the standard Python exception hierarchy to isolate domain-specific failures from generic system errors. One class addresses general issues arising from concept manipulation, such as invalid definitions or improper modifier application, while another specifically targets logical contradictions and unsatisfiable concepts found within the ontology structure. By accepting descriptive string arguments during instantiation, the architecture facilitates precise debugging and logging, allowing developers to implement targeted error handling strategies. This separation of concerns ensures that complex fuzzy logic computations can clearly distinguish between semantic failures and other runtime exceptions, thereby enhancing the robustness and clarity of error reporting.

## Modules

- [`fuzzy_dl_owl2.fuzzydl.exception.fuzzy_ontology_exception`] — Defines a specialized exception for handling errors specific to fuzzy ontology operations.
- [`fuzzy_dl_owl2.fuzzydl.exception.inconsistent_ontology_exception`] — A custom exception class designed to signal logical inconsistencies within fuzzy description logic ontologies.
