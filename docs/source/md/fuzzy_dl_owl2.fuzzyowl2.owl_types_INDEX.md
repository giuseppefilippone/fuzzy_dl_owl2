# Summary

A comprehensive type system for the FuzzyOWL2 ontology framework that models fuzzy logic concepts, datatypes, properties, and aggregation operators through an inheritance-based architecture.

## Description

The software provides a hierarchical structure of abstract base classes and concrete implementations to represent various fuzzy logic constructs, ranging from basic membership functions to complex aggregation integrals. Core abstractions define the interfaces for fuzzy concepts, datatypes, and properties, allowing specific mathematical models—such as triangular, trapezoidal, or linear functions—to inherit common behaviors like bound management and type identification. Advanced fuzzy logic operations, including Sugeno and Choquet integrals as well as Ordered Weighted Averaging, are modeled as specialized concept definitions that encapsulate weights and sub-concepts to perform non-linear aggregations. Linguistic hedges and modifiers are implemented as distinct components that can be applied to concepts, datatypes, and properties, enabling the representation of nuanced logical relationships where truth values are adjusted by specific coefficients or geometric shapes.

## Modules

- [`fuzzy_dl_owl2.fuzzyowl2.owl_types.choquet_concept`] — A specialized fuzzy concept definition that aggregates multiple underlying concepts using the Choquet integral with specific weights.
- [`fuzzy_dl_owl2.fuzzyowl2.owl_types.concept_definition`] — An abstract base class that establishes a common interface and type categorization for fuzzy concept definitions within the FuzzyOWL2 framework.
- [`fuzzy_dl_owl2.fuzzyowl2.owl_types.crisp_function`] — A specialized datatype class that models crisp functions using linear coefficients to integrate precise mathematical logic into a fuzzy ontology framework.
- [`fuzzy_dl_owl2.fuzzyowl2.owl_types.fuzzy_datatype`] — An abstract base class that defines the structure for fuzzy datatypes characterized by lower and upper bounds within the FuzzyOWL2 framework.
- [`fuzzy_dl_owl2.fuzzyowl2.owl_types.fuzzy_modifier`] — Defines an abstract base class that structures fuzzy modifiers acting as linguistic hedges to alter the membership degree of fuzzy concepts.
- [`fuzzy_dl_owl2.fuzzyowl2.owl_types.fuzzy_nominal_concept`] — Models fuzzy nominal concepts by associating a named individual with a specific degree of membership.
- [`fuzzy_dl_owl2.fuzzyowl2.owl_types.fuzzy_property`] — Defines the structural blueprint for properties operating within the FuzzyOWL2 ontology framework under fuzzy logic principles.
- [`fuzzy_dl_owl2.fuzzyowl2.owl_types.left_shoulder_function`] — A Python class representing a left-shoulder membership function used within fuzzy logic systems to model concepts where membership decreases as values increase.
- [`fuzzy_dl_owl2.fuzzyowl2.owl_types.linear_function`] — Implements a linear membership function for the FuzzyOWL2 framework by defining geometric parameters and bounds.
- [`fuzzy_dl_owl2.fuzzyowl2.owl_types.linear_modifier`] — A fuzzy logic modifier class that applies a linear transformation to membership degrees using a specific coefficient.
- [`fuzzy_dl_owl2.fuzzyowl2.owl_types.modified_concept`] — Defines a specialized data structure for representing fuzzy logic concepts that have been altered by linguistic hedges or modifiers.
- [`fuzzy_dl_owl2.fuzzyowl2.owl_types.modified_function`] — Defines a data structure for representing fuzzy datatypes that have been altered by specific linguistic modifiers.
- [`fuzzy_dl_owl2.fuzzyowl2.owl_types.modified_property`] — Defines a FuzzyOWL2 property subjected to a fuzzy modification or linguistic hedge.
- [`fuzzy_dl_owl2.fuzzyowl2.owl_types.owa_concept`] — A specialized definition for Ordered Weighted Averaging operations within the FuzzyOWL2 framework that aggregates fuzzy concepts using a specific set of weights.
- [`fuzzy_dl_owl2.fuzzyowl2.owl_types.property_definition`] — Encapsulates a property name and its associated fuzzy modifier to support the definition of fuzzy logic constraints within the FuzzyOWL2 ontology framework.
- [`fuzzy_dl_owl2.fuzzyowl2.owl_types.qowa_concept`] — Defines a specialized data structure for modeling **Quantified Ordered Weighted Averaging (OWA)** concepts within the FuzzyOWL2 ontology language.
- [`fuzzy_dl_owl2.fuzzyowl2.owl_types.quasi_sugeno_concept`] — A specialized implementation of a fuzzy logic operator that models the quasi-Sugeno integral by aggregating weighted concepts.
- [`fuzzy_dl_owl2.fuzzyowl2.owl_types.right_shoulder_function`] — A Python class representing a right-shoulder fuzzy membership function used to model concepts where membership increases linearly to full certainty after a specific threshold.
- [`fuzzy_dl_owl2.fuzzyowl2.owl_types.sugeno_concept`] — A specialized implementation of a fuzzy concept definition that models the Sugeno fuzzy integral by aggregating linguistic terms with corresponding numerical weights.
- [`fuzzy_dl_owl2.fuzzyowl2.owl_types.trapezoidal_function`] — A Python implementation of a trapezoidal membership function that models fuzzy sets using four defining coordinates.
- [`fuzzy_dl_owl2.fuzzyowl2.owl_types.triangular_function`] — Implements a triangular membership function to model vague concepts within the FuzzyOWL2 framework.
- [`fuzzy_dl_owl2.fuzzyowl2.owl_types.triangular_modifier`] — A class representing a triangular membership function used to define fuzzy modifiers within the FuzzyOWL2 framework.
- [`fuzzy_dl_owl2.fuzzyowl2.owl_types.weighted_concept`] — Defines a data structure that associates a numerical weight with a fuzzy concept identifier within the FuzzyOWL2 ontology language.
- [`fuzzy_dl_owl2.fuzzyowl2.owl_types.weighted_max_concept`] — Implements a fuzzy logic operator that performs a weighted maximum aggregation over a collection of concept definitions.
- [`fuzzy_dl_owl2.fuzzyowl2.owl_types.weighted_min_concept`] — Implements a weighted minimum aggregation operator within the FuzzyOWL2 framework to construct complex fuzzy concepts by combining a collection of sub-concepts.
- [`fuzzy_dl_owl2.fuzzyowl2.owl_types.weighted_sum_concept`] — A specialized definition that aggregates multiple fuzzy concepts into a weighted sum structure within the FuzzyOWL2 framework.
- [`fuzzy_dl_owl2.fuzzyowl2.owl_types.weighted_sum_zero_concept`] — Defines a fuzzy logic constraint where a weighted sum of concepts equals zero within the FuzzyOWL2 framework.
