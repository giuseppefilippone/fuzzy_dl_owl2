# Summary

Encapsulates a fuzzy concept that has been modified by a specific linguistic hedge or modifier within the FuzzyOWL2 framework.

## Description

Inheriting from the core definition structure allows this component to represent nuanced or graded logical expressions where a standard concept is qualified by a fuzzy modifier. The design stores the modifier and the underlying concept name as distinct string attributes, ensuring that the specific linguistic hedge applied to the logic is preserved alongside the core concept. Access to these internal components is provided through dedicated retrieval methods, allowing external logic to inspect the specific nature of the modification while maintaining encapsulation. Finally, the textual representation is formatted to clearly display the relationship between the modifier and the concept, typically appearing as a parenthesized pair to reflect the logical structure.
