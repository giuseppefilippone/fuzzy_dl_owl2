# Summary

Fuzzy description-logic assertions that express graded concept membership, serving as the fundamental knowledge primitives of a fuzzy ontology reasoner.

## Description

Assertions capture graded membership statements rather than the crisp true/false claims of classical description logic, coupling three components — an individual, a concept, and a degree acting as a lower-bound threshold — such that an assertion is satisfied whenever the individual's actual membership in the concept meets or exceeds that threshold. A leaner atomic variant pairs just a concept with a degree, behaving as a plain, declarative value object with no validation, mutation, or evaluation logic of its own. Both forms are deliberately kept as cheap, mutable containers: getters and setters let reasoning components rewrite or refine assertions in place, copies are shallow so duplicates continue to share their underlying individual, concept, and degree objects, and all actual satisfaction checking is delegated elsewhere in the reasoning engine.

The most distinctive design decision lies in the asymmetric equality semantics. Two assertions compare as equal either when their full string representations coincide, or when they name the same individual and concept and the first one's degree is strictly *smaller* than the second's — an order-sensitive rule that effectively treats a stronger assertion (higher threshold) as subsuming a weaker one, which is useful when a reasoner absorbs new knowledge or checks whether an incoming assertion is already entailed by a stricter one on record, at the cost that *a == b* no longer implies *b == a*. Supporting helpers expose the concept's internal type so downstream logic can dispatch on atomic versus structured concepts, and human-readable renderings follow the conventional fuzzy-DL notation *individual:concept >= degree*, keeping logs, debugging sessions, and knowledge-base dumps easy to trace, while circular imports are sidestepped by bringing in dependent types only under *TYPE_CHECKING*.

## Modules

- [`fuzzy_dl_owl2.fuzzydl.assertion.assertion`] — A fuzzy description-logic assertion stating that an individual belongs to a concept with at least a given membership degree, rendered in the conventional form *individual:concept >= degree*.
- [`fuzzy_dl_owl2.fuzzydl.assertion.atomic_assertion`] — A minimal value object representing an atomic fuzzy assertion, namely that an atomic concept must hold with a membership degree greater than or equal to a given threshold.
