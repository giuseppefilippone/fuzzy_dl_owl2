# Summary

A custom exception class designed to signal logical inconsistencies within fuzzy description logic ontologies.

## Description

It acts as a specific error signal for when a fuzzy ontology contains logical contradictions or unsatisfiable concepts during processing. By extending the standard Python exception hierarchy, it allows developers to catch and manage domain-specific errors related to fuzzy description logic frameworks separately from generic runtime errors. The implementation accepts a descriptive string argument to provide context about the specific conflict, ensuring that debugging and error reporting are precise and informative. This approach facilitates robust error handling in ontology management systems by clearly distinguishing logical failures from other types of exceptions.
