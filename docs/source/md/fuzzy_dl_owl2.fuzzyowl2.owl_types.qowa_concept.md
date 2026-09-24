# Summary

Defines a Quantified Ordered Weighted Averaging (OWA) concept for the FuzzyOWL2 ontology language, binding a linguistic quantifier to the collection of fuzzy concepts it aggregates.

## Description

QowaConcept is a specialised subclass of ConceptDefinition that registers itself with the QUANTIFIED_OWA concept type at construction time, allowing the wider fuzzy ontology framework to recognise and handle it distinctly from other kinds of concept definitions. Its entire state consists of two pieces: a quantifier string encoding the linguistic term that governs the aggregation's weighting scheme, and an ordered list of concept names over which the OWA operator is applied. The design is deliberately minimal — the constructor performs no validation and the accessors simply return the stored values, with the concept list handed back by reference rather than as a defensive copy — so the class functions as a lightweight data carrier while semantic correctness is delegated to the layers that parse or reason over the ontology. A string rendering is provided in the compact parenthesised form beginning with the "q-owa" identifier, followed by the quantifier and the space-joined concepts, matching the concrete syntax used when such expressions are displayed or serialised into FuzzyOWL2 axioms.
