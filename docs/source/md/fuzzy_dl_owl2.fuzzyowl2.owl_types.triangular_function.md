# Summary

Implements a triangular membership function for fuzzy logic ontologies by defining geometric parameters for shape calculation.

## Description

A triangular membership function is modeled to represent vague or imprecise concepts within fuzzy logic systems by defining a specific geometric shape. Inheriting from a base fuzzy datatype allows the logic to integrate into the FuzzyOWL2 framework, enabling ontological reasoners to process constraints and sets defined by imprecise boundaries. The shape of the function is determined by three floating-point parameters representing the left endpoint, the peak, and the right endpoint, which are stored as private attributes to maintain encapsulation. Accessor methods expose these geometric values for external use, while a custom string representation offers a concise summary of the object's configuration for debugging or logging.
