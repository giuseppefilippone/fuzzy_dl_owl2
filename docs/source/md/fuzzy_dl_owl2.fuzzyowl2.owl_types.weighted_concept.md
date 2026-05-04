# Summary

Defines a data structure for representing weighted concepts in the FuzzyOWL2 ontology language by associating a numerical weight with a named fuzzy concept.

## Description

Serving as a concrete implementation within the FuzzyOWL2 framework, the structure models concepts that carry a specific numerical weight or degree of membership. By extending the base `ConceptDefinition` class, the implementation integrates into the broader type hierarchy and explicitly registers instances as weighted concepts during initialization. The structure encapsulates a floating-point value representing the weight and a string identifier for the concept, storing them as private attributes to ensure data integrity. Accessor methods allow the retrieval of the numerical weight and the associated concept label, while a custom string representation provides a human-readable format combining both elements.
