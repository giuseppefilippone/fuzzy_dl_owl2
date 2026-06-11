# Summary

A collection of utility decorators designed to facilitate debugging through method tracing and to handle deep recursion by dynamically adjusting system limits.

## Description

The software provides a suite of high-level decorators intended to instrument code for diagnostic purposes and to overcome Python's default recursion depth constraints. A debugging mechanism allows for automatic tracing of method calls within a class, logging entry arguments and return values based on a global configuration flag, while intelligently distinguishing between static and instance methods to ensure accurate argument reporting. To support algorithms that require deep call stacks, a recursion management wrapper intercepts depth limit errors, progressively increases the interpreter's recursion limit, and guarantees that the system state is restored after execution, regardless of success or failure. These tools rely on a central configuration reader to control output verbosity and integrate seamlessly with existing logging utilities to provide visibility into complex execution flows without modifying core logic.
