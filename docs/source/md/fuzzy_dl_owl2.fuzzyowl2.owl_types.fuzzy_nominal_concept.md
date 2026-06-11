# Summary

Models fuzzy nominal concepts by associating a named individual with a specific degree of membership.

## Description

The implementation extends the base concept definition to handle assertions where a specific named individual is associated with a particular concept using a numerical truth value. By storing a floating-point membership degree alongside a string identifier for the individual, the logic allows for the precise modeling of fuzzy logic statements within an ontology. Internal state management ensures that the numerical degree and the individual's name are encapsulated, while accessors provide read-only retrieval of these core components. Integration with the broader framework is achieved through inheritance and type registration, enabling the system to distinguish this specific fuzzy nominal type from other concept definitions during processing.
