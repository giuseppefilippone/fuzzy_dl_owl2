# Summary

Defines a fuzzy logic concept representing an existential restriction where an entity must have a specific value for a given role.

## Description

Models a specific type of existential restriction, often termed a "has-value" concept, which asserts that an individual must be related to a specific value through a defined role. Structurally, it represents the logical form `(b-some r v)`, meaning an entity satisfies this concept if it participates in the relationship `r` with a target entity that corresponds to `v`. Instantiation requires a string representing the role and a target value of arbitrary type, after which the object automatically derives a canonical name for identification. Composition with other logical constructs is supported through operator overloading for conjunction, disjunction, and negation, while the architecture explicitly prevents the replacement of internal components to maintain atomic integrity. Identity comparisons rely on a hashing mechanism that combines the concept type, role, and value to ensure consistency within the broader system.
