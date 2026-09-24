# Summary

A concrete fuzzy modifier that applies a linear transformation, parameterised by a single floating-point coefficient, to membership degrees within the FuzzyOWL2 framework.

## Description

**LinearModifier** specialises the generic *FuzzyModifier* type for the simplest and most common kind of modifier: one whose effect on a fuzzy membership degree is fully determined by a single numeric constant. The coefficient is supplied at construction time, held as a private attribute, and exposed only through a read-only accessor, a design that makes instances effectively immutable and safe to share throughout the ontology model. Deliberately, no input validation or transformation logic lives inside the object itself; it acts purely as a carrier for the parameter, leaving the actual application of the linear function to the reasoning and serialisation machinery elsewhere in the framework. The string representation, rendered in the form "linear-modifier(c)", follows the textual conventions of FuzzyOWL2 so that the modifier can be written directly into ontology serialisations and human-readable debugging output. Because it derives from the shared base modifier class, instances can be handled polymorphically alongside other modifier families wherever modified fuzzy concepts are created, queried, or rendered.
