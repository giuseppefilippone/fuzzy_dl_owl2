# Summary

A utility builder class that programmatically constructs XML elements conforming to the FuzzyOWL2 ontology specification.

## Description

Static methods within this utility programmatically construct XML elements that conform to the FuzzyOWL2 ontology specification, serving as a factory for various node types. Logic definitions, datatypes, modifiers, truth degrees, and concept names are generated through dedicated builders that automatically handle mandatory attributes and allow for the merging of optional metadata. Tag names and attribute keys are centralized via a constant class to ensure consistency, while a helper function converts the resulting element trees into formatted strings for readability.
