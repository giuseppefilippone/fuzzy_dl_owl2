# Summary

Defines a weighted sum concept for the FuzzyOWL2 framework, aggregating a list of fuzzy concept definitions into a single composite concept.

## Description

**WeightedSumConcept** is a specialized **ConceptDefinition** that models fuzzy concepts constructed by combining several existing concepts through weighted summation. Its constructor registers the concept under the `WEIGHTED_SUM` type in the shared concept-type taxonomy and retains the supplied list of component concepts, allowing arbitrarily complex fuzzy expressions to be composed from simpler building blocks. A deliberate design choice is that the component list is stored and returned by reference rather than copied, keeping the object lightweight and live-linked to external changes, but placing the responsibility for immutability on the caller. The class also provides a human-readable serialization that renders the concept as a parenthesized expression prefixed with "w-sum", which supports debugging and textual export of fuzzy ontologies. Together these behaviours make it a small but essential aggregation primitive within the broader fuzzy OWL 2 modelling toolkit.
