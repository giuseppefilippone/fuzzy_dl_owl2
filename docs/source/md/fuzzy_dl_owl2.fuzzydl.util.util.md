# Summary

A centralized utility namespace and logging infrastructure for the fuzzy ontology reasoner.

## Description

Execution begins by establishing a robust logging system that organizes output into timestamped directories and files, with the verbosity level dynamically controlled by configuration settings. The `Util` class serves as a static repository for common operations, wrapping standard logging calls to automatically raise custom exceptions upon encountering errors. Mathematical helpers are provided to ensure high precision by using decimal arithmetic for rounding operations, specifically adhering to a "round half up" strategy rather than default binary rounding. Further functionality includes utilities for detecting integer values within floating-point numbers, calculating the ceiling of base-2 logarithms, and in-place sorting of lists based on string conversion.
