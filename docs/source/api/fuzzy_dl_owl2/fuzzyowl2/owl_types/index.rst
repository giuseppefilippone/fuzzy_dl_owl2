fuzzy_dl_owl2.fuzzyowl2.owl_types
=================================

.. only:: html

    .. figure:: /_uml/module_fuzzy_dl_owl2_fuzzyowl2_owl_types.png
       :alt: UML Class Diagram for fuzzy_dl_owl2.fuzzyowl2.owl_types
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **fuzzy_dl_owl2.fuzzyowl2.owl_types**

.. only:: latex

    .. figure:: /_uml/module_fuzzy_dl_owl2_fuzzyowl2_owl_types.pdf
       :alt: UML Class Diagram for fuzzy_dl_owl2.fuzzyowl2.owl_types
       :align: center
       :width: 11.8cm
       :class: uml-diagram

       UML Class Diagram for **fuzzy_dl_owl2.fuzzyowl2.owl_types**

.. py:module:: fuzzy_dl_owl2.fuzzyowl2.owl_types



.. ── LLM-GENERATED DESCRIPTION START ──

Core type definitions and data structures for modeling fuzzy logic concepts, properties, and mathematical functions within the FuzzyOWL2 ontology framework.


Description
-----------


An object-oriented hierarchy of abstract base classes establishes a structural blueprint for representing fuzzy logic entities, ensuring that all derived implementations share a consistent interface for categorization and data access. Concrete components extend these foundations to model complex logical operations, including various aggregation methods like Sugeno and Choquet integrals, weighted sums, and ordered weighted averaging, which combine multiple sub-concepts based on specific importance weights. Mathematical membership functions, such as triangular, trapezoidal, and linear shapes, define the degrees of truth for fuzzy sets, while linguistic hedges and modifiers provide mechanisms to dynamically adjust these membership values or alter properties and datatypes. Encapsulating parameters like coefficients, bounds, and weights within these specialized objects facilitates the serialization, processing, and reasoning required for handling uncertainty and imprecision in knowledge representation.


Modules
-------


* ``fuzzy_dl_owl2.fuzzyowl2.owl_types.choquet_concept`` — A specialized implementation of a fuzzy concept definition that aggregates multiple sub-concepts using the Choquet integral based on a set of fuzzy measure weights.
* ``fuzzy_dl_owl2.fuzzyowl2.owl_types.concept_definition`` — An abstract base class that establishes a common interface for representing fuzzy concept definitions within the FuzzyOWL2 framework.
* ``fuzzy_dl_owl2.fuzzyowl2.owl_types.crisp_function`` — Defines a crisp function data structure for modeling precise mathematical intervals within the FuzzyOWL2 ontology framework.
* ``fuzzy_dl_owl2.fuzzyowl2.owl_types.fuzzy_datatype`` — An abstract base class defines the structure for fuzzy datatypes characterized by a lower and an upper bound within the FuzzyOWL2 framework.
* ``fuzzy_dl_owl2.fuzzyowl2.owl_types.fuzzy_modifier`` — Establishes an abstract base class for fuzzy modifiers that act as linguistic hedges to adjust membership degrees.
* ``fuzzy_dl_owl2.fuzzyowl2.owl_types.fuzzy_nominal_concept`` — Defines a data structure representing a fuzzy nominal concept that associates a specific individual with a degree of membership within an ontology.
* ``fuzzy_dl_owl2.fuzzyowl2.owl_types.fuzzy_property`` — Establishes an abstract structural blueprint for properties governed by fuzzy logic principles within the FuzzyOWL2 ontology framework.
* ``fuzzy_dl_owl2.fuzzyowl2.owl_types.left_shoulder_function`` — Implements a left-shoulder membership function used within fuzzy logic systems to model concepts where membership values decrease as input values increase.
* ``fuzzy_dl_owl2.fuzzyowl2.owl_types.linear_function`` — Extends the base fuzzy datatype to model a linear membership function used for defining fuzzy sets within the FuzzyOWL2 framework.
* ``fuzzy_dl_owl2.fuzzyowl2.owl_types.linear_modifier`` — Defines a class that applies linear transformations to fuzzy logic membership degrees within the FuzzyOWL2 framework.
* ``fuzzy_dl_owl2.fuzzyowl2.owl_types.modified_concept`` — Defines a specialized logical entity representing a concept altered by a fuzzy modifier or linguistic hedge within the FuzzyOWL2 framework.
* ``fuzzy_dl_owl2.fuzzyowl2.owl_types.modified_function`` — Defines a data structure for representing fuzzy datatypes that have been altered by linguistic modifiers within the FuzzyOWL2 framework.
* ``fuzzy_dl_owl2.fuzzyowl2.owl_types.modified_property`` — Defines a data structure for representing fuzzy properties that have been altered by linguistic modifiers within the FuzzyOWL2 framework.
* ``fuzzy_dl_owl2.fuzzyowl2.owl_types.owa_concept`` — Defines a specialized data structure for representing Ordered Weighted Averaging (OWA) operations in fuzzy logic ontologies.
* ``fuzzy_dl_owl2.fuzzyowl2.owl_types.property_definition`` — Encapsulates an ontology property name alongside its corresponding fuzzy modifier to define linguistic hedges within the FuzzyOWL2 framework.
* ``fuzzy_dl_owl2.fuzzyowl2.owl_types.qowa_concept`` — A specialized class representing a Quantified Ordered Weighted Averaging (OWA) concept within the FuzzyOWL2 ontology language.
* ``fuzzy_dl_owl2.fuzzyowl2.owl_types.quasi_sugeno_concept`` — Defines a class representing a quasi-Sugeno integral fuzzy logic operator that aggregates multiple concepts using specific weights within the FuzzyOWL2 ontology framework.
* ``fuzzy_dl_owl2.fuzzyowl2.owl_types.right_shoulder_function`` — A Python class representing a right shoulder fuzzy membership function used to model concepts where membership increases linearly to a maximum value.
* ``fuzzy_dl_owl2.fuzzyowl2.owl_types.sugeno_concept`` — Defines a specialized data structure for representing Sugeno fuzzy integral concepts within a fuzzy ontology framework, aggregating multiple concepts using specific weights.
* ``fuzzy_dl_owl2.fuzzyowl2.owl_types.trapezoidal_function`` — Implements a trapezoidal membership function within the FuzzyOWL2 framework to model fuzzy sets with a flat top region.
* ``fuzzy_dl_owl2.fuzzyowl2.owl_types.triangular_function`` — Implements a triangular membership function for fuzzy logic ontologies by defining geometric parameters for shape calculation.
* ``fuzzy_dl_owl2.fuzzyowl2.owl_types.triangular_modifer`` — Implements a triangular membership function used to define fuzzy modifiers within the FuzzyOWL2 framework.
* ``fuzzy_dl_owl2.fuzzyowl2.owl_types.weighted_concept`` — Defines a data structure for representing weighted concepts within the FuzzyOWL2 ontology language by associating a numerical weight with a named fuzzy concept.
* ``fuzzy_dl_owl2.fuzzyowl2.owl_types.weighted_max_concept`` — Implements a fuzzy logic operator that performs weighted maximum aggregation over a collection of concepts.
* ``fuzzy_dl_owl2.fuzzyowl2.owl_types.weighted_min_concept`` — Models a weighted minimum aggregation operator within the FuzzyOWL2 framework to construct complex fuzzy concepts from a collection of sub-concepts.
* ``fuzzy_dl_owl2.fuzzyowl2.owl_types.weighted_sum_concept`` — Defines a specialized concept structure that aggregates multiple underlying definitions into a weighted sum representation for fuzzy logic operations.
* ``fuzzy_dl_owl2.fuzzyowl2.owl_types.weighted_sum_zero_concept`` — Defines a fuzzy logic concept within the FuzzyOWL2 framework that enforces a constraint where a weighted sum of component concepts equals zero.

.. ── LLM-GENERATED DESCRIPTION END ──

Submodules
----------

.. toctree::
   :maxdepth: 1

   /api/fuzzy_dl_owl2/fuzzyowl2/owl_types/choquet_concept/index
   /api/fuzzy_dl_owl2/fuzzyowl2/owl_types/concept_definition/index
   /api/fuzzy_dl_owl2/fuzzyowl2/owl_types/crisp_function/index
   /api/fuzzy_dl_owl2/fuzzyowl2/owl_types/fuzzy_datatype/index
   /api/fuzzy_dl_owl2/fuzzyowl2/owl_types/fuzzy_modifier/index
   /api/fuzzy_dl_owl2/fuzzyowl2/owl_types/fuzzy_nominal_concept/index
   /api/fuzzy_dl_owl2/fuzzyowl2/owl_types/fuzzy_property/index
   /api/fuzzy_dl_owl2/fuzzyowl2/owl_types/left_shoulder_function/index
   /api/fuzzy_dl_owl2/fuzzyowl2/owl_types/linear_function/index
   /api/fuzzy_dl_owl2/fuzzyowl2/owl_types/linear_modifier/index
   /api/fuzzy_dl_owl2/fuzzyowl2/owl_types/modified_concept/index
   /api/fuzzy_dl_owl2/fuzzyowl2/owl_types/modified_function/index
   /api/fuzzy_dl_owl2/fuzzyowl2/owl_types/modified_property/index
   /api/fuzzy_dl_owl2/fuzzyowl2/owl_types/owa_concept/index
   /api/fuzzy_dl_owl2/fuzzyowl2/owl_types/property_definition/index
   /api/fuzzy_dl_owl2/fuzzyowl2/owl_types/qowa_concept/index
   /api/fuzzy_dl_owl2/fuzzyowl2/owl_types/quasi_sugeno_concept/index
   /api/fuzzy_dl_owl2/fuzzyowl2/owl_types/right_shoulder_function/index
   /api/fuzzy_dl_owl2/fuzzyowl2/owl_types/sugeno_concept/index
   /api/fuzzy_dl_owl2/fuzzyowl2/owl_types/trapezoidal_function/index
   /api/fuzzy_dl_owl2/fuzzyowl2/owl_types/triangular_function/index
   /api/fuzzy_dl_owl2/fuzzyowl2/owl_types/triangular_modifer/index
   /api/fuzzy_dl_owl2/fuzzyowl2/owl_types/weighted_concept/index
   /api/fuzzy_dl_owl2/fuzzyowl2/owl_types/weighted_max_concept/index
   /api/fuzzy_dl_owl2/fuzzyowl2/owl_types/weighted_min_concept/index
   /api/fuzzy_dl_owl2/fuzzyowl2/owl_types/weighted_sum_concept/index
   /api/fuzzy_dl_owl2/fuzzyowl2/owl_types/weighted_sum_zero_concept/index

