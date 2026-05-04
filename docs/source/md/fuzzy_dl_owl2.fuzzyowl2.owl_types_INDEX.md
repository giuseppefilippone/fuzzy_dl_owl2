# Summary

Core data structures and abstract interfaces for defining fuzzy logic concepts, properties, and datatypes within the FuzzyOWL2 ontology framework.

## Description

The software provides a comprehensive type system for representing fuzzy logic constructs, enabling the modeling of uncertainty and vagueness within ontologies through specialized classes for concepts, properties, and datatypes. It relies on a hierarchy of abstract base classes that establish foundational contracts for concept definitions, fuzzy properties, and datatypes, which are then extended by concrete implementations to handle specific mathematical operations and linguistic hedges. Concrete implementations encapsulate complex aggregation operators such as Choquet and Sugeno integrals, Ordered Weighted Averaging, and various weighted sums, alongside geometric membership functions like triangular, trapezoidal, and shoulder shapes. The architecture further supports the modification of these core elements through linguistic hedges and linear transformations, allowing for nuanced expressions where standard properties or concepts are adjusted by specific degrees or modifiers to reflect graded truth values.

## Modules

- [`fuzzy_dl_owl2.fuzzyowl2.owl_types.choquet_concept`] — A specialized implementation of a fuzzy concept definition that utilizes the Choquet integral to aggregate multiple underlying concepts based on a specific set of weights.
- [`fuzzy_dl_owl2.fuzzyowl2.owl_types.concept_definition`] — An abstract base class representing concept definitions within the FuzzyOWL2 framework.
- [`fuzzy_dl_owl2.fuzzyowl2.owl_types.crisp_function`] — A specialized datatype class representing a crisp function within the FuzzyOWL2 framework to model precise mathematical intervals or linear transformations.
- [`fuzzy_dl_owl2.fuzzyowl2.owl_types.fuzzy_datatype`] — An abstract base class defines the structural foundation for fuzzy datatypes by managing a range characterized by lower and upper bounds.
- [`fuzzy_dl_owl2.fuzzyowl2.owl_types.fuzzy_modifier`] — An abstract base class is established to define the structural contract for fuzzy modifiers that alter membership degrees within the FuzzyOWL2 framework.
- [`fuzzy_dl_owl2.fuzzyowl2.owl_types.fuzzy_nominal_concept`] — A class representing a fuzzy nominal concept that associates a specific individual with a degree of membership within an ontology.
- [`fuzzy_dl_owl2.fuzzyowl2.owl_types.fuzzy_property`] — Defines an abstract base class that serves as a structural blueprint for properties governed by fuzzy logic principles within the FuzzyOWL2 ontology framework.
- [`fuzzy_dl_owl2.fuzzyowl2.owl_types.left_shoulder_function`] — A specialized data structure representing a left-shoulder membership function for fuzzy logic systems where membership values decrease as input values increase.
- [`fuzzy_dl_owl2.fuzzyowl2.owl_types.linear_function`] — Implements a linear membership function used to calculate degrees of membership in fuzzy sets.
- [`fuzzy_dl_owl2.fuzzyowl2.owl_types.linear_modifier`] — A fuzzy logic modifier that applies a linear transformation to membership degrees using a specific coefficient.
- [`fuzzy_dl_owl2.fuzzyowl2.owl_types.modified_concept`] — Encapsulates a fuzzy concept that has been modified by a specific linguistic hedge or modifier within the FuzzyOWL2 framework.
- [`fuzzy_dl_owl2.fuzzyowl2.owl_types.modified_function`] — Defines a data structure for representing fuzzy datatypes that have been altered by specific linguistic modifiers.
- [`fuzzy_dl_owl2.fuzzyowl2.owl_types.modified_property`] — Represents a property within the FuzzyOWL2 framework that has been altered by a fuzzy modifier or linguistic hedge.
- [`fuzzy_dl_owl2.fuzzyowl2.owl_types.owa_concept`] — Models an Ordered Weighted Averaging (OWA) operation within a fuzzy ontology framework by aggregating a list of concepts using a specific set of numerical weights.
- [`fuzzy_dl_owl2.fuzzyowl2.owl_types.property_definition`] — Encapsulates a property name and its associated fuzzy modifier to define linguistic hedges within the FuzzyOWL2 ontology framework.
- [`fuzzy_dl_owl2.fuzzyowl2.owl_types.qowa_concept`] — Encapsulates the definition of a Quantified Ordered Weighted Averaging (OWA) concept used in fuzzy logic ontology modeling.
- [`fuzzy_dl_owl2.fuzzyowl2.owl_types.quasi_sugeno_concept`] — Implements a data structure for handling quasi-Sugeno integral concepts within a fuzzy ontology framework.
- [`fuzzy_dl_owl2.fuzzyowl2.owl_types.right_shoulder_function`] — A Python class implementation modeling a right-shoulder fuzzy membership function within the FuzzyOWL2 framework.
- [`fuzzy_dl_owl2.fuzzyowl2.owl_types.sugeno_concept`] — A specialized data structure representing a Sugeno fuzzy integral concept that aggregates multiple fuzzy concepts using a corresponding set of weights.
- [`fuzzy_dl_owl2.fuzzyowl2.owl_types.trapezoidal_function`] — A Python implementation of a trapezoidal membership function that models fuzzy sets with a flat top region.
- [`fuzzy_dl_owl2.fuzzyowl2.owl_types.triangular_function`] — Implements a triangular membership function for fuzzy logic systems, characterized by three defining points.
- [`fuzzy_dl_owl2.fuzzyowl2.owl_types.triangular_modifer`] — A specialized class representing a triangular membership function used to apply fuzzy logic modifications within the FuzzyOWL2 framework.
- [`fuzzy_dl_owl2.fuzzyowl2.owl_types.weighted_concept`] — Defines a data structure for representing weighted concepts in the FuzzyOWL2 ontology language by associating a numerical weight with a named fuzzy concept.
- [`fuzzy_dl_owl2.fuzzyowl2.owl_types.weighted_max_concept`] — A specialized class representing a weighted maximum aggregation operator used within the FuzzyOWL2 ontology framework to combine fuzzy concepts.
- [`fuzzy_dl_owl2.fuzzyowl2.owl_types.weighted_min_concept`] — Implements a weighted minimum aggregation operator within the FuzzyOWL2 framework to construct complex fuzzy concepts from a collection of sub-concepts.
- [`fuzzy_dl_owl2.fuzzyowl2.owl_types.weighted_sum_concept`] — A specialized class representing a weighted sum concept that aggregates multiple concept definitions within the FuzzyOWL2 framework.
- [`fuzzy_dl_owl2.fuzzyowl2.owl_types.weighted_sum_zero_concept`] — A specialized class within the FuzzyOWL2 framework represents a fuzzy logic constraint defined by a weighted sum of component concepts equating to zero.
