# Summary

Abstract base classes define standard interfaces for managing conceptual entities, roles, and associated values within a fuzzy description logic system.

## Description

These interfaces leverage the Abstract Base Class pattern to enforce a consistent structure across components that need to store and manipulate logical data. By encapsulating references to single concepts, collections of entities, or specific roles, the architecture allows subclasses to initialize with specific data and dynamically update it without re-implementing storage mechanisms. The design utilizes property decorators to control access to internal state, ensuring that data like numerical weights or string identifiers remain private yet accessible through a clean API. Through inheritance and composition, these structural blueprints enable the creation of complex fuzzy logic constructs, such as binary relations or weighted expressions, by combining distinct capabilities like role handling and concept management into cohesive contracts.

## Modules

- [`fuzzy_dl_owl2.fuzzydl.concept.interface.has_concept_interface`] — An abstract base class providing a standard interface for objects to manage and update a mutable reference to a specific conceptual entity.
- [`fuzzy_dl_owl2.fuzzydl.concept.interface.has_concepts_interface`] — An abstract base class that standardizes the storage and management of a collection of conceptual entities within the fuzzy description logic system.
- [`fuzzy_dl_owl2.fuzzydl.concept.interface.has_role_concept_interface`] — An abstract interface that unifies role and concept management capabilities for fuzzy description logic entities.
- [`fuzzy_dl_owl2.fuzzydl.concept.interface.has_role_interface`] — An abstract base class that defines a standard interface for managing a role attribute associated with a concept.
- [`fuzzy_dl_owl2.fuzzydl.concept.interface.has_value_interface`] — An abstract interface is provided for managing concepts that require both a specific role and an associated generic value.
- [`fuzzy_dl_owl2.fuzzydl.concept.interface.has_weighted_concepts_interface`] — An abstract interface extending the basic concept management contract to include support for numerical weights associated with each concept.
