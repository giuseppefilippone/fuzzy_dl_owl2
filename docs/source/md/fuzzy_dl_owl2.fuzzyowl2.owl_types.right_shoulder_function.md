# Summary

A right-shoulder fuzzy membership function that assigns zero membership below a lower threshold, a linearly increasing degree between two parameters, and full membership at or above the upper threshold, for use in fuzzy OWL 2 ontologies.

## Description

Right-shoulder functions are a standard shape in fuzzy set theory, well suited to linguistic concepts such as "hot" or "expensive" where any value beyond a certain point belongs completely to the set. The **RightShoulderFunction** class extends the framework's base fuzzy datatype so that such a shape can be attached to datatypes in a fuzzy OWL 2 ontology, with the two float parameters `a` and `b` marking the interval over which membership ramps linearly from zero to one. The implementation is deliberately minimal: the constructor simply stores the two endpoints after delegating to the superclass and performs no validation, so the object behaves as a lightweight data carrier whose shape parameters are exposed through simple accessors. A human-readable string representation follows the framework's serialization convention, printing the function as "right-shoulder(k1, k2, a, b)", where the kernel parameters `k1` and `k2` are inherited from the base datatype; sharing this textual format keeps the output consistent with the other shoulder and trapezoidal function types used throughout the FuzzyOWL2 framework.
