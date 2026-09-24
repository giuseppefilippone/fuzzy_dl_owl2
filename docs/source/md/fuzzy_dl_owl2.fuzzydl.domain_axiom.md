# Summary

A minimal value object expressing a fuzzy description-logic domain axiom, binding a role name to a Concept that constrains which individuals may act as subjects of that role.

## Description

DomainAxiom models the standard description-logic construct dom(R) ⊑ C: whenever the role is asserted between two individuals, the axiom enforces type consistency by requiring the subject to belong to the associated concept. Within the fuzzydl_owl2 toolkit, such axioms are gathered as part of an ontology's definition and later consumed by a fuzzy DL reasoner or translated into an OWL 2 representation. The design is deliberately minimal — the constructor performs no validation or transformation, simply storing the role identifier and the Concept reference as instance attributes, so the object remains a pure declarative statement rather than an active component. That simplicity shifts responsibility for correctness onto the caller, while keeping each axiom a small, self-contained unit of ontological knowledge that other parts of the system can enumerate, serialize, or reason over.
