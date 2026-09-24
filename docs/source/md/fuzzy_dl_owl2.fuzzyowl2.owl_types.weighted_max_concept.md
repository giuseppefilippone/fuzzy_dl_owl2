# Summary

Defines a weighted-maximum fuzzy concept that aggregates a list of concept definitions under the weighted max operator for use in the FuzzyOWL2 ontology framework.

## Description

**WeightedMaxConcept** extends the base *ConceptDefinition* type to represent one particular fuzzy construct: the weighted maximum aggregation over a collection of concepts. At construction time it tags itself with the `ConceptType.WEIGHTED_MAX` discriminator, which is how the surrounding framework distinguishes it from other fuzzy operators (such as weighted sums or minima) when serialising or reasoning over the ontology. The operands are accepted as a list of concept definitions and stored as-is, with no validation of the input — a deliberate choice that keeps the object a thin data holder and pushes integrity checking to the components that actually evaluate fuzzy membership degrees. The stored list is later exposed by reference rather than by copy, which avoids allocation overhead but means callers share mutable state with the instance, so any external modification is directly visible to the concept itself. A compact textual rendering of the form "(w-max ...)", produced by joining the string forms of the operands with spaces, makes the aggregate easy to inspect in logs and debug output without altering its state.
