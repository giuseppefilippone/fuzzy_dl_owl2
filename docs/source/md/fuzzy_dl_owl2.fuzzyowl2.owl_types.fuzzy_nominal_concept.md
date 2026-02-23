# Summary

Defines a data structure representing a fuzzy nominal concept that associates a specific individual with a degree of membership within an ontology.

## Description

The implementation extends the base concept definition to model assertions where a named individual is associated with a specific truth value or membership degree. By storing a floating-point number alongside a string identifier, the structure allows for the precise representation of fuzzy logic assertions regarding specific entities within an ontology. Accessor methods are provided to retrieve the numerical degree and the individual's name, ensuring that the internal state remains encapsulated while allowing external components to query the fuzzy assertion details. Furthermore, a string representation is generated to display the relationship in a human-readable format, combining the degree and the individual identifier within parentheses.
