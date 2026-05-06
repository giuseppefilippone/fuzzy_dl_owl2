# Summary

Implements a triangular membership function used to define fuzzy modifiers within the FuzzyOWL2 framework.

## Description

It models the degree of membership using a geometric shape defined by three specific parameters: a left endpoint representing the start of the support, a peak point indicating maximum membership, and a right endpoint marking the end of the support. By inheriting from a base fuzzy modifier class, this implementation integrates into the broader framework to apply specific fuzzy logic transformations to concepts based on the provided numerical boundaries. The logic encapsulates these values to define the specific characteristics of the modification, providing access to the underlying coordinates while ensuring the object can be easily represented as a string for debugging or logging purposes.
