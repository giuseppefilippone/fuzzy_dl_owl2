# Summary

Encapsulates the outcome of a query performed on a fuzzy knowledge base, distinguishing between a numerical degree of satisfaction and the consistency status of the base itself.

## Description

The design allows the object to represent two distinct states: a valid query result where the knowledge base is consistent, or a state indicating inconsistency. When initialized with a floating-point number, the instance stores the satisfaction value and assumes the underlying knowledge base is consistent, providing a container for the numerical outcome. Conversely, initialization with a boolean flag explicitly marks the knowledge base as inconsistent, rendering the numerical solution irrelevant and resetting the internal state to reflect this failure. To support detailed analysis, the structure maintains a dictionary of variable bindings that can be populated and retrieved, allowing users to inspect specific values determined during the resolution process. Accessor methods provide a clean interface for retrieving the consistency status, the primary solution value, and the associated variable mappings, while standard string representation methods offer human-readable summaries of the result state.
