# Summary

A weighted concept definition for the FuzzyOWL2 ontology language that pairs a numeric weight with a named fuzzy concept.

## Description

WeightedConcept is a concrete subclass of the ConceptDefinition hierarchy, registering itself under the WEIGHTED_CONCEPT type at construction time so that the surrounding fuzzy ontology framework can distinguish it from other kinds of concept definitions during parsing, serialization, and reasoning. Its entire state consists of two private attributes — a floating-point weight and a string naming the fuzzy concept — both supplied at instantiation and exposed afterwards through simple read-only accessors. The pairing captures a degree of membership or importance attached to the concept, which is the core mechanism by which fuzzy ontologies express graded rather than purely Boolean membership. Because no mutators are provided, an instance is effectively immutable once created, keeping the weight–concept association stable throughout the object's lifetime. A human-readable string representation renders the pair in the parenthesized form "(weight concept)", which supports debugging and the production of readable ontology dumps.
