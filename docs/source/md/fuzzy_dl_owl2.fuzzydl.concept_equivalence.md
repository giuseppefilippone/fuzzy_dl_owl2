# Summary

Encapsulates the logical axiom asserting equivalence between two distinct concepts.

## Description

It functions as a structural container for a pair of `Concept` objects, enabling the definition of relationships where two entities are treated as interchangeable within a specific context. By storing these two entities internally, the implementation allows for the assertion of equality without performing immediate validation or modification of the underlying data. Users can retrieve the stored concepts through dedicated accessors and generate independent copies of the relationship via a shallow cloning mechanism, ensuring that the original state remains unmodified during operations. This design prioritizes a clear representation of semantic equivalence, serving as a foundational component for constructing complex logical statements in fuzzy description logics.
