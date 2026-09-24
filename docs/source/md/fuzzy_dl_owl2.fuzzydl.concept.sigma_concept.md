# Summary

A fuzzy description logic concept that models sigma-count quantification, defining membership in terms of how many individuals reachable through a given role also belong to a target concept, evaluated against a fuzzy concrete domain.

## Description

Sigma-count constructs allow fuzzy ontologies to express cardinality-driven conditions such as "most of a person's friends are young" by bundling four components into a single evaluable unit: a binary role, a target concept, a set of reference individuals, and a fuzzy concrete concept. Rather than producing a crisp true/false verdict, the construct measures how many role-related individuals instantiate the target concept and matches that count against the fuzzy concrete concept, which encodes a fuzzy number or qualifier, yielding a degree of satisfaction.

*SigmaConcept* subclasses the core `Concept` type and tags itself with a dedicated concept type, deriving a canonical, parenthesized name string from its components at construction time so that every instance carries a stable, human-readable, structurally meaningful identity. It is deliberately treated as an atomic, terminal node within the reasoner's traversal machinery: it reports no atomic sub-concepts, exposes no roles of its own, and returns itself unchanged from concept-replacement requests, keeping its internal structure opaque to the rewriting and substitution logic used elsewhere.

Despite this atomicity, instances compose naturally with other concepts because the negation, conjunction, and disjunction operators delegate to shared operator factories, building new compound concepts while leaving the operands untouched. Deep cloning recursively duplicates the nested concept, the fuzzy concrete concept, and every reference individual, so copies are fully independent of their originals. Hashing is computed from the structural tuple of the role, nested concept, individuals, concrete concept, name, and type rather than from object identity, which lets structurally equivalent sigma-counts behave correctly as set members and dictionary keys.
