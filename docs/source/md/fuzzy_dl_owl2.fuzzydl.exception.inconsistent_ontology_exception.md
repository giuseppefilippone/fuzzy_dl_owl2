# Summary

A custom exception that signals logical inconsistencies detected in fuzzy ontologies, such as contradictory concept definitions or unsatisfiable concepts.

## Description

**InconsistentOntologyException** extends Python's built-in `Exception` to provide a dedicated error type for a fuzzy description logic framework, allowing reasoning and ontology-management code to distinguish genuine logical conflicts from ordinary runtime failures. Because it carries a single human-readable message that is forwarded directly to the superclass constructor, the exception integrates seamlessly with standard Python error handling, appearing correctly in tracebacks, logging output, and `except` clauses. Raising a specialised type rather than a generic `Exception` lets callers catch ontology inconsistencies selectively, so they can respond to logical problems — for example, by aborting a reasoning task or reporting a diagnostic — without masking unrelated bugs. The minimal, message-only design keeps the class lightweight while still giving developers the contextual detail needed to pinpoint the exact source of an inconsistency during debugging.
