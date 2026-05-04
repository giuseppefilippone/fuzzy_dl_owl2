# Summary

Defines a data structure for representing fuzzy datatypes that have been altered by specific linguistic modifiers.

## Description

Extending the base fuzzy datatype functionality, this component models how a standard property is transformed by linguistic hedges such as "very" or "somewhat" within the FuzzyOWL2 framework. By associating a specific modifier string with a target datatype name, the implementation allows for the creation of nuanced fuzzy concepts where the meaning of the base property is altered. Instances encapsulate these two elements—the modifier and the underlying datatype—and expose them through accessor methods to facilitate further processing or querying. The string representation is formatted as a parenthesized pair, clearly indicating the modification applied to the original datatype.
