# Summary

Defines a data structure for representing fuzzy properties that have been altered by linguistic modifiers within the FuzzyOWL2 framework.

## Description

Extending the base functionality of fuzzy properties, the implementation allows for the representation of nuanced relationships where the truth value of a property is adjusted by a specific factor. By storing a linguistic hedge and a target property name as distinct string attributes, the design enables the precise definition of modified concepts such as "very tall" or "somewhat fast." Accessor methods are provided to retrieve the specific modifier and the underlying property, ensuring that the internal state remains encapsulated while remaining accessible for logical operations. Furthermore, the string representation is overridden to display the combination as a parenthesized pair, facilitating easy debugging and textual output within the broader fuzzy logic system.
