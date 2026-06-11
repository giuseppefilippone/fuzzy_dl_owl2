# Summary

Defines a FuzzyOWL2 property subjected to a fuzzy modification or linguistic hedge.

## Description

Extending the base `FuzzyProperty` class, this implementation allows for the representation of nuanced relationships where the truth value of a property is altered by a specific factor. It encapsulates two distinct string components: a linguistic hedge or modifier and the name of the underlying property being modified. By storing these values internally, the logic provides access to the specific modifier and the base property through dedicated retrieval methods. The string representation is designed to display the relationship as a parenthesized pair, ensuring that the modified nature of the property is clearly visible in textual outputs.
