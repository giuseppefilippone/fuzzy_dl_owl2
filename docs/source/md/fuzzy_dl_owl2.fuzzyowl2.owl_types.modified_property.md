# Summary

Represents a property within the FuzzyOWL2 framework that has been altered by a fuzzy modifier or linguistic hedge.

## Description

Extending the base `FuzzyProperty` structure, this component enables the representation of nuanced relationships where a standard property is subjected to a linguistic hedge or fuzzy modifier. By accepting a modifier string and a property name during instantiation, the software captures the specific alteration applied to the relationship, allowing for distinctions such as "very" or "somewhat" to be preserved alongside the core property identifier. Internal storage maintains these two distinct elements, and dedicated accessors expose the underlying property and its associated modifier without modifying the object's state. String representations are generated to display the combined entity as a parenthesized pair, ensuring that the modified nature of the property is clearly communicated in textual outputs.
