# Summary

A specialized query that executes the classification process on a knowledge base to verify consistency.

## Description

Extending the base `Query` interface, the logic focuses specifically on triggering the classification routine within a given knowledge base. During execution, the system invokes the classification method of the provided knowledge base, returning a successful solution with a maximum score if the process completes without error. Any exceptions raised during this operation are caught and interpreted as an indication that the knowledge base is inconsistent, resulting in a specific error state rather than propagating the failure. Unlike other query types that might require parameter resolution or setup, the design bypasses preprocessing steps entirely, relying solely on the internal state of the knowledge base to perform the operation.
