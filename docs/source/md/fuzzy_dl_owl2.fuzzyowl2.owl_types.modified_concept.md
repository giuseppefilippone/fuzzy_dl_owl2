# Summary

A specialised fuzzy concept definition that pairs a base concept with a linguistic hedge (fuzzy modifier) to express graded notions such as "very Hot" within the FuzzyOWL2 framework.

## Description

The `ModifiedConcept` class extends the generic `ConceptDefinition` type and registers itself under the `MODIFIED_CONCEPT` concept type, allowing the rest of the framework to distinguish hedged concepts from ordinary ones during parsing, serialisation, and reasoning. Its design is deliberately minimal: the modifier and the underlying concept name are captured as two private string attributes at construction time, and the class offers nothing beyond read-only accessors for retrieving them, which keeps the *representation* of a modified concept fully decoupled from the *semantics* of how the modifier actually reshapes membership degrees — that interpretation is delegated to the reasoning layer. Because the object is effectively immutable once created, it behaves as a simple value object that can be safely shared and inspected wherever fuzzy ontologies are manipulated. The string form renders the pair as a parenthesised expression, `(modifier concept)`, matching the concrete syntax conventions used when fuzzy ontologies are written out, so the object can be embedded directly into textual serialisations without further processing.
