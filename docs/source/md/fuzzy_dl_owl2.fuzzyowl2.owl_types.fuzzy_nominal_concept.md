# Summary

A class representing a fuzzy nominal concept that associates a specific individual with a degree of membership within an ontology.

## Description

It extends the base definition for concepts to model assertions where a named individual belongs to a concept with a specific truth value. The implementation stores a floating-point number representing the membership degree alongside a string identifier for the individual entity. By registering the entity type as FUZZY_NOMINAL during initialization, the design integrates seamlessly into the broader type system used for fuzzy description logic. Accessor methods allow the retrieval of the numerical degree and the individual name, while a string representation provides a human-readable format combining these two components.
