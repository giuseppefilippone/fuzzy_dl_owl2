# Summary

A lightweight value class that pairs a fuzzy concept with a degree of satisfaction, allowing individuals in a fuzzy description-logic knowledge base to be annotated with weighted concept memberships.

## Description

The **Label** class binds a Concept to a Degree — nominally a value in the interval [0, 1] — expressing the extent to which the concept applies to a given individual. Construction deliberately performs no range validation on the weight, trusting the caller to supply a well-formed degree and keeping object creation cheap and side-effect free. Equality semantics are intentionally strict: two labels are considered equal only when their concepts are identical and their weights are instances of the exact same concrete Degree class, with numeric degrees additionally compared by their numerical values while non-numeric degrees of the same class are treated as equal. This distinction matters because the framework supports both numeric and symbolic degrees, and conflating different degree representations would produce unsound comparisons during reasoning. Inequality is defined as the straightforward negation of equality, and a human-readable string representation is formed by joining the concept and its weight with a space, making labels convenient to embed in solver output, logging, and debugging traces.
