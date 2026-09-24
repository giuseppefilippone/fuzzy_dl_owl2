# Summary

Defines a `ModifiedFunction` fuzzy datatype that pairs a linguistic modifier with a base datatype to express hedged fuzzy concepts such as "very tall" within the FuzzyOWL2 framework.

## Description

In fuzzy ontology modelling, linguistic hedges like "very" or "somewhat" reshape the membership function of an underlying fuzzy concept, and capturing that pairing is the sole purpose here: the modifier's name and the identifier of the datatype it alters are stored as the object's entire state. Because the class derives from `FuzzyDatatype`, an instance can be treated polymorphically anywhere the framework expects a generic fuzzy datatype, while still carrying the extra modifier information that distinguishes it from plain datatypes. Both values are held in private attributes and exposed only through getter methods, leaving the object effectively immutable after construction and consistent with the encapsulation conventions used throughout the surrounding owl_types package. The constructor performs no validation — whatever is passed in is stored as-is — so semantic correctness is deferred to the layers that actually interpret the ontology. A string representation formatted as `modified(modifier, datatype)` rounds out the behaviour, making instances easy to print, log, or embed in textual output while keeping the modifier–datatype relationship immediately visible.
