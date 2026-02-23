# Summary

Encapsulates a mathematical inequality of the form expression compared to zero, typically used within fuzzy description logic ontologies.

## Description

Mathematical inequalities of the form expression compared to zero are modeled to support fuzzy description logic ontologies, specifically for representing the degree of satisfaction of a concept by an individual. The implementation normalizes constraints by storing a linear expression and a comparison operator, ensuring the right-hand side is always zero to simplify solver integration. Static factory methods are provided to conveniently instantiate specific inequality types, such as greater than or less than, without requiring manual specification of the operator enumeration. Functionality includes cloning instances, accessing underlying terms and constants, and checking for zero-valued expressions, alongside standard Python protocols for hashing, equality, and string representation to enable use in collections and debugging scenarios.
