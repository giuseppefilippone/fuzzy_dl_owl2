# Summary

A collection of abstract interfaces defining the structural contracts for managing concepts, roles, values, and weights within a fuzzy description logic system.

## Description

These interfaces establish a foundational architecture by separating the definition of data relationships from their concrete implementation. Specific extensions allow for the association of arbitrary values with roles while enforcing strict state isolation through deep copy operations to prevent unintended side effects. Furthermore, the design supports the representation of magnitude or significance by integrating numerical weights directly into concept management structures. Together, these abstract contracts ensure consistency and encapsulation across the system, enabling robust handling of complex fuzzy logic operations.

## Modules

- [`fuzzy_dl_owl2.fuzzydl.concept.interface.has_concept_interface`] — 
- [`fuzzy_dl_owl2.fuzzydl.concept.interface.has_concepts_interface`] — 
- [`fuzzy_dl_owl2.fuzzydl.concept.interface.has_role_concept_interface`] — 
- [`fuzzy_dl_owl2.fuzzydl.concept.interface.has_role_interface`] — 
- [`fuzzy_dl_owl2.fuzzydl.concept.interface.has_value_interface`] — An abstract base class that extends role management capabilities by incorporating a generic value attribute protected by deep copy operations to ensure state isolation.
- [`fuzzy_dl_owl2.fuzzydl.concept.interface.has_weighted_concepts_interface`] — An abstract interface that extends concept management to include associated numerical weights.
