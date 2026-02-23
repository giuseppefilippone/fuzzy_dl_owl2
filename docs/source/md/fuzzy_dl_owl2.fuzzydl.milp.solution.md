# Summary

Encapsulates the outcome of a query performed on a fuzzy knowledge base, distinguishing between numerical satisfaction degrees and the consistency status of the base itself.

## Description

The software provides a data structure to capture query results, specifically designed to handle the dual nature of fuzzy logic outputs where a result can be a specific degree of satisfaction or a failure due to inconsistency. By utilizing constructor overloading, the implementation allows instantiation via a boolean flag to indicate an inconsistent knowledge base or via a floating-point number to represent a valid solution, automatically setting the consistency state accordingly. Internally, the object maintains a dictionary to track variable bindings that were highlighted during the resolution process, enabling the retrieval of specific parameter values alongside the primary result. Standard object behaviors such as string representation and hashing are customized to reflect the current state, displaying the numerical value when consistent or a specific inconsistency message otherwise.
