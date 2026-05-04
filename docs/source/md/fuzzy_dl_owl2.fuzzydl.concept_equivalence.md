# Summary

Encapsulates the logical axiom asserting that two distinct concepts are equivalent within a fuzzy description logic system.

## Description

The implementation serves as a container for a pair of `Concept` objects, allowing the definition of relationships where two entities are treated as interchangeable. By storing references to both sides of the equivalence, the structure supports operations that require reasoning about or manipulating the equality of distinct logical entities. The design includes functionality to generate independent copies of the equivalence statement, ensuring that modifications to a cloned instance do not affect the original relationship. Accessor methods are provided to retrieve the specific concepts involved, facilitating the integration of this equivalence axiom into broader logical processing workflows without exposing the internal state directly.
