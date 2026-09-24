# Summary

An abstract base class that establishes the common contract for fuzzy properties — ontology relationships that hold with a degree of truth rather than binary certainty — within the FuzzyOWL2 framework.

## Description

In a fuzzy extension of OWL 2, properties such as roles and attributes need not hold absolutely; they can link individuals or values with varying degrees of membership, and `FuzzyProperty` anchors the type hierarchy that represents such graded relationships. By building on Python's abstract-base-class machinery, the class is deliberately non-instantiable, signalling that only concrete subclasses implementing specific fuzzy property types are meant to exist at runtime. Its body is intentionally empty apart from documentation, so instead of prescribing methods or state it serves purely as a shared type identity — a way for the rest of the ontology framework to recognise and handle every fuzzy property uniformly, whatever its concrete flavour. The result is an extensible contract: new kinds of fuzzy properties can plug into the knowledge representation system while consistency across the property hierarchy is preserved.
