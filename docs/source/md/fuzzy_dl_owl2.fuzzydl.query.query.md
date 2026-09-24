# Summary

An abstract base class that defines the interface every query must follow when evaluated against a fuzzy knowledge base, complete with built-in execution-time measurement.

## Description

The `Query` class is the foundational contract for all concrete query types in the fuzzy description-logic reasoner, guaranteeing that every query shares a uniform lifecycle regardless of its specific purpose. Subclasses are required to implement three operations: a preprocessing step that prepares or normalizes the query in the context of a given `KnowledgeBase`, a solving step that performs the actual reasoning and returns a `Solution`, and a string conversion for human-readable display. Declaring these as abstract methods ensures that no query can be instantiated without complete reasoning logic, while leaving the algorithms themselves entirely to the concrete implementations. Separating preprocessing from solving also allows knowledge-base-specific setup to happen once, before the reasoning step runs.

A second responsibility is performance instrumentation. The base class records a high-resolution monotonic timestamp when a query starts and computes the elapsed duration in nanoseconds when it finishes, exposing the result as a floating-point number of seconds. Embedding this timing in the common ancestor means every query variant reports execution cost consistently, which is useful for benchmarking the underlying optimization-based reasoning. The timing state is deliberately minimal—two integer attributes initialized to zero—so subclasses incur no overhead beyond what they actively use, and repeated invocations recompute the measurement from the original start point rather than accumulating intervals.
