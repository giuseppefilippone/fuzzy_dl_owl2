# Summary

Utility decorators are provided to facilitate debugging through method tracing and to manage deep recursion by dynamically adjusting system limits.

## Description

The debugging infrastructure includes a wrapper that logs method entry and exit details, such as arguments and return values, while intelligently distinguishing between static and instance methods to ensure accurate context reporting. A class-level decorator automates this instrumentation by iterating through class attributes and applying the wrapper to all functions, controlled by a global flag that enables or disables the verbose logging. Furthermore, a recursion handling mechanism intercepts stack overflow errors to progressively double the recursion limit until the operation succeeds, thereby preventing premature termination of complex logical computations while restoring the original limit upon completion.
