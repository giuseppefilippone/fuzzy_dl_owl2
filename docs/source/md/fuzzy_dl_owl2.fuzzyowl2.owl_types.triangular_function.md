# Summary

Implements a triangular membership function to model vague concepts within the FuzzyOWL2 framework.

## Description

Inheriting from the base fuzzy datatype, this concrete implementation defines a geometric shape characterized by a left endpoint, a peak, and a right endpoint. These three floating-point parameters determine the support and core of the fuzzy set, allowing the system to calculate membership degrees for imprecise values. Accessor methods expose the internal state to ensure the defining geometric properties remain immutable after initialization, facilitating their use in reasoning tasks. The integration into the broader ontology framework provides a standardized way to represent triangular constraints, enabling the translation of linguistic variables into computational logic.
