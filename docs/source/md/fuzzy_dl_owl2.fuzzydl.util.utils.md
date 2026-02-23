# Summary

Utility decorators provide debugging instrumentation and automatic recursion limit adjustment for Python classes and functions.

## Description

A debugging mechanism wraps methods to log entry and exit details, including arguments and return values, while intelligently distinguishing between static and instance methods to format output correctly. This instrumentation is applied via a class-level decorator that conditionally activates based on a global flag, allowing developers to trace execution flow across entire classes without modifying individual method definitions. Furthermore, a recursion management decorator intercepts stack overflow errors by dynamically increasing the system recursion limit and retrying execution until success, ensuring that deep recursive algorithms can run to completion while preserving the original system limits afterward.
