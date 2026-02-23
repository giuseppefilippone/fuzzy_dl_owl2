# Summary

Encapsulates an ontology property name alongside its corresponding fuzzy modifier to define linguistic hedges within the FuzzyOWL2 framework.

## Description

Acting as a fundamental building block for fuzzy logic constraints, this structure links a specific object or data property with a linguistic hedge or truth value. By storing these two components together, it allows for the precise application of fuzzy modifiers to properties during the construction of complex fuzzy axioms. The design relies on simple internal storage of string identifiers, offering read-only access to the modifier and property name without enforcing validation or triggering side effects during initialization. This approach facilitates the creation of granular logic rules where the strictness or leniency of property comparisons can be explicitly controlled.
