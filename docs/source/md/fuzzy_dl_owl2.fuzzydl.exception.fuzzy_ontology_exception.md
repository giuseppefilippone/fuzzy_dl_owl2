# Summary

A domain-specific exception for reporting errors that arise during fuzzy ontology and fuzzy description logic operations, such as invalid concept definitions or the incorrect application of fuzzy modifiers.

## Description

`FuzzyOntologyException` extends Python's built-in `Exception` to give the fuzzy description logic framework a dedicated error channel that can be caught independently of generic language-level exceptions. Callers raise it with a single human-readable message string, which the constructor forwards unchanged to the superclass so that the exception behaves exactly like any standard Python error in tracebacks, logging output, and `except` clauses. The design is deliberately minimal — no additional state or behaviour is layered on top of the base class — because the value lies purely in the distinct type, which allows client code to isolate and handle ontology-related failures without accidentally masking unrelated bugs. The result is error handling across the wider fuzzydl system that is both precise and easy to reason about, since a malformed concept expression or a misused modifier can be distinguished at the `except` level from any other kind of runtime problem.
