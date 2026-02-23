# Summary

Defines a data structure for representing weighted concepts within the FuzzyOWL2 ontology language by associating a numerical weight with a named fuzzy concept.

## Description

Extending the base `ConceptDefinition` class, this implementation captures the relationship between a magnitude and a specific fuzzy concept identifier. During initialization, the constructor accepts a floating-point number and a string, storing them internally while explicitly registering the entity type as `WEIGHTED_CONCEPT` to ensure correct classification within the system hierarchy. Accessor methods are provided to retrieve the numerical value and the concept label separately, allowing other components of the system to query the specific degree of membership or importance associated with the concept. Furthermore, the implementation overrides the default string representation to display the weight and concept name in a parenthesized format, facilitating easier debugging and logging of fuzzy logic expressions.
