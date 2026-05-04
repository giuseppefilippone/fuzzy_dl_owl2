# Summary

A specialized class representing a triangular membership function used to apply fuzzy logic modifications within the FuzzyOWL2 framework.

## Description

The implementation extends the base fuzzy modifier functionality to model degrees of membership using a geometric triangle defined by three distinct parameters. By accepting floating-point values for the left endpoint, the peak point, and the right endpoint, the logic determines the specific shape of the fuzzy set, where membership typically increases linearly to the peak and decreases linearly afterwards. Encapsulation of these numerical values allows the system to represent the modification applied to a concept without exposing the internal state directly, relying instead on accessors to retrieve the specific coordinates. The design ensures that the object can be easily identified and debugged through a string representation that explicitly lists the defining parameters, facilitating integration into larger fuzzy ontology processing workflows.
