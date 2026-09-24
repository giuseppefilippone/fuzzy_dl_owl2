# Summary

A fuzzy modifier that models a triangular membership function for the FuzzyOWL2 framework, defined by a left endpoint, a peak point of maximum membership, and a right endpoint.

## Description

Fuzzy modifiers in the FuzzyOWL2 framework reshape the degree to which a concept holds, and the triangular form is one of the simplest and most widely used ways to express such a modification. **TriangularModifier**, the central class here, specialises the generic FuzzyModifier base by storing the three floating-point values that fix the triangle's geometry: the middle value marks where membership reaches its maximum, while the two outer values delimit the support over which the concept holds to any degree at all. The design is deliberately minimal and permissive — the constructor performs no ordering or range validation, trusting callers to supply a sensible arrangement of the three values, and the parameters are held as private attributes exposed through simple, side-effect-free accessors. A string representation of the form *"triangular-modifier(a, b, c)"* is produced so that instances render consistently during logging, debugging, and serialisation into the ontology's concrete syntax.
