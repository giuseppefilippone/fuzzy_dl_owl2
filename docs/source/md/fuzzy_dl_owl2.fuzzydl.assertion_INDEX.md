# Summary

Models fuzzy logic assertions by associating individuals and concepts with minimum membership degree thresholds within a description logic framework.

## Description

The software provides a foundational layer for representing logical constraints in fuzzy description logics, specifically focusing on the relationship between entities, categories, and truth values. It distinguishes between fundamental constraints that bind a concept to a degree and more specific assertions that tie an individual entity to a concept under a threshold. By encapsulating these core components, the architecture supports the construction of complex logical statements while offering mechanisms for data access, object cloning, and custom equality comparisons. The design ensures that the semantic meaning of fuzzy constraints is preserved through precise string representations and internal state management, allowing the system to evaluate whether membership criteria are met.

## Modules

- [`fuzzy_dl_owl2.fuzzydl.assertion.assertion`] — Models a fuzzy logic assertion that associates an individual with a concept subject to a minimum membership degree threshold.
- [`fuzzy_dl_owl2.fuzzydl.assertion.atomic_assertion`] — Defines a fundamental logical constraint within a fuzzy logic framework by associating a specific concept with a minimum membership degree threshold.
