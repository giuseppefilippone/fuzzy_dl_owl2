# Summary

A class representing a triangular membership function used to define fuzzy modifiers within the FuzzyOWL2 framework.

## Description

The software models the degree of membership for fuzzy concepts using a geometric shape defined by three specific floating-point parameters. These parameters represent the left endpoint of the support, the peak point indicating maximum membership, and the right endpoint marking the end of the support. By inheriting from a base fuzzy modifier class, the implementation ensures integration into the broader FuzzyOWL2 architecture while encapsulating the specific logic required for triangular distributions. Accessor methods expose the internal state, and a custom string representation provides a human-readable format for debugging or logging purposes.
