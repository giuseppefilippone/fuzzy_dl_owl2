# Summary

Defines an Ordered Weighted Averaging (OWA) fuzzy concept that pairs a vector of numerical weights with the list of fuzzy concepts it aggregates within a FuzzyOWL2 ontology.

## Description

**OwaConcept** extends the generic concept-definition base type and registers itself under the *OWA* concept type, allowing the surrounding fuzzy ontology framework to recognise it as an aggregation operator rather than an ordinary atomic or compound concept. Its purpose is to carry the two pieces of data an OWA operator requires — a sequence of floating-point weights and the identifiers of the fuzzy concepts being averaged — and to expose them through straightforward accessors so that serialisers and reasoners can retrieve the aggregation parameters when processing the ontology. Design-wise it behaves as a plain data holder: the constructor stores the incoming lists by reference and performs no validation, so the weights are not checked to sum to one, and any later mutation of the caller's original lists remains visible through the object's state. The string rendering follows the framework's s-expression-like syntax, emitting an expression of the form `(owa (weights) (concepts))` with weights and concept names joined by spaces, which lets the operator's full configuration be written out verbatim when the fuzzy ontology is exported or displayed.
