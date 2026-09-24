# Summary

Defines a `ModifiedProperty` class that pairs a fuzzy property with a linguistic modifier, such as "very" or "somewhat", within the FuzzyOWL2 framework.

## Description

The class models the situation where a fuzzy relationship is qualified by a hedge that alters the degree of truth with which the underlying property holds, a common construct in fuzzy ontologies for expressing graded knowledge. At construction time it simply stores two strings — the modifier and the name of the property being modified — and deliberately performs no validation or transformation, keeping the object a lightweight, passive data carrier that other parts of the framework, such as ontology serialization or reasoning routines, can query through its getter methods. Inheriting from `FuzzyProperty` allows modified properties to be treated polymorphically wherever a generic fuzzy property is expected, which is the key design decision enabling them to flow through the rest of the type hierarchy unchanged. Both the informal and official string representations render the object as a parenthesized pair, "(modifier property)", so that modified properties can be embedded naturally in human-readable renderings of a fuzzy ontology; notably, `__repr__` delegates to `__str__`, meaning the two representations are identical and display-oriented rather than machine-parseable.
