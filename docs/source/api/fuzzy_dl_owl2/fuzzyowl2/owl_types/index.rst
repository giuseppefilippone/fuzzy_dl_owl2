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

A type vocabulary for the FuzzyOWL2 fuzzy ontology framework, providing fuzzy concept definitions, membership-function datatypes, linguistic modifiers, and graded properties that let OWL 2 ontologies express degrees of truth instead of all-or-nothing membership.


Description
-----------


The architecture rests on four parallel class hierarchies, each anchored by a deliberately non-instantiable abstract base class — ``ConceptDefinition``, ``FuzzyDatatype``, ``FuzzyModifier``, and ``FuzzyProperty`` — so that parsers, serialisers, and reasoners can handle every construct polymorphically through a shared contract rather than through concrete classes. Concept definitions follow a type-tag pattern in which each subclass registers a ``ConceptType`` discriminator at construction time, which is how the rest of the framework distinguishes a hedged concept from a weighted aggregation or a graded nominal assertion without knowing the concrete class it is looking at. The datatype hierarchy models fuzzy numbers as bounded intervals, and the concrete membership-function shapes — triangular, trapezoidal, shoulder-shaped, linear, and crisp — derive their specific geometry from those inherited bounds, while a corresponding "modified" construct appears across concepts, datatypes, and properties to pair any element with the linguistic hedge that reshapes it.

A second major theme is fuzzy aggregation: a substantial family of concept definitions pairs numeric weights or linguistic quantifiers with the concepts they combine, ranging from simple weighted sums, minima, and maxima through ordered weighted averaging to the Choquet, Sugeno, and quasi-Sugeno integral families, which can capture interactions between criteria — such as redundancy or synergy — that plain weighted averages cannot express. The unifying design philosophy throughout is that of a thin, typed data holder: constructors perform no validation, state lives in private attributes exposed through read-only accessors that often return internal lists by reference rather than copy, and no evaluation logic exists inside the objects themselves, so semantic correctness is deferred entirely to the downstream reasoning and serialisation machinery. Every class renders itself in a compact, s-expression-like parenthesised syntax, keeping printed output uniform across the hierarchy and allowing any construct to be embedded directly into textual ontology serialisations or inspected during debugging. The result is a representation-only layer that captures the structure of graded knowledge — hedged concepts, shaped membership functions, weighted aggregation, and graded properties — while leaving its interpretation to the rest of the framework.


Modules
-------


* [``fuzzy_dl_owl2.fuzzyowl2.owl_types.choquet_concept``] — A fuzzy OWL 2 concept definition that aggregates several named concepts using the Choquet integral, holding the fuzzy measure weights and concept identifiers that drive the aggregation.
* [``fuzzy_dl_owl2.fuzzyowl2.owl_types.concept_definition``] — An abstract base class that anchors the hierarchy of fuzzy concept definitions in the FuzzyOWL2 framework by tagging each definition with a ``ConceptType`` and exposing that tag through a common interface.
* [``fuzzy_dl_owl2.fuzzyowl2.owl_types.crisp_function``] — A crisp function datatype for the FuzzyOWL2 framework that stores two numeric coefficients and renders itself as a ``crisp(...)`` expression bounded by inherited interval limits.
* [``fuzzy_dl_owl2.fuzzyowl2.owl_types.fuzzy_datatype``] — An abstract base class that models a fuzzy datatype as a bounded interval, storing a lower and upper value that concrete subclasses in the FuzzyOWL2 framework interpret to shape their membership functions.
* [``fuzzy_dl_owl2.fuzzyowl2.owl_types.fuzzy_modifier``] — An abstract base class, ``FuzzyModifier``, that establishes the contract for linguistic hedges which mathematically transform the membership degrees of fuzzy concepts within the FuzzyOWL2 framework.
* [``fuzzy_dl_owl2.fuzzyowl2.owl_types.fuzzy_nominal_concept``] — Defines a fuzzy nominal concept that binds a named ontology individual to a graded degree of membership, extending the FuzzyOWL2 concept-definition hierarchy.
* [``fuzzy_dl_owl2.fuzzyowl2.owl_types.fuzzy_property``] — An abstract base class that establishes the common contract for fuzzy properties — ontology relationships that hold with a degree of truth rather than binary certainty — within the FuzzyOWL2 framework.
* [``fuzzy_dl_owl2.fuzzyowl2.owl_types.left_shoulder_function``] — Defines a left-shoulder membership function for fuzzy OWL 2 ontologies in which the degree of membership stays at one for low input values and linearly falls to zero as values increase.
* [``fuzzy_dl_owl2.fuzzyowl2.owl_types.linear_function``] — A linear membership function datatype for the FuzzyOWL2 fuzzy ontology framework, characterised by two floating-point coefficients that determine the line's slope and position when assigning degrees of membership.
* [``fuzzy_dl_owl2.fuzzyowl2.owl_types.linear_modifier``] — A concrete fuzzy modifier that applies a linear transformation, parameterised by a single floating-point coefficient, to membership degrees within the FuzzyOWL2 framework.
* [``fuzzy_dl_owl2.fuzzyowl2.owl_types.modified_concept``] — A specialised fuzzy concept definition that pairs a base concept with a linguistic hedge (fuzzy modifier) to express graded notions such as "very Hot" within the FuzzyOWL2 framework.
* [``fuzzy_dl_owl2.fuzzyowl2.owl_types.modified_function``] — Defines a ``ModifiedFunction`` fuzzy datatype that pairs a linguistic modifier with a base datatype to express hedged fuzzy concepts such as "very tall" within the FuzzyOWL2 framework.
* [``fuzzy_dl_owl2.fuzzyowl2.owl_types.modified_property``] — Defines a ``ModifiedProperty`` class that pairs a fuzzy property with a linguistic modifier, such as "very" or "somewhat", within the FuzzyOWL2 framework.
* [``fuzzy_dl_owl2.fuzzyowl2.owl_types.owa_concept``] — Defines an Ordered Weighted Averaging (OWA) fuzzy concept that pairs a vector of numerical weights with the list of fuzzy concepts it aggregates within a FuzzyOWL2 ontology.
* [``fuzzy_dl_owl2.fuzzyowl2.owl_types.property_definition``] — A minimal value object that binds a property name to its associated fuzzy modifier so the pair can travel together when expressing fuzzy axioms in the FuzzyOWL2 ontology framework.
* [``fuzzy_dl_owl2.fuzzyowl2.owl_types.qowa_concept``] — Defines a Quantified Ordered Weighted Averaging (OWA) concept for the FuzzyOWL2 ontology language, binding a linguistic quantifier to the collection of fuzzy concepts it aggregates.
* [``fuzzy_dl_owl2.fuzzyowl2.owl_types.quasi_sugeno_concept``] — Defines a quasi-Sugeno integral concept for FuzzyOWL2 ontologies, holding the numeric weights and fuzzy concept names that together specify a weighted fuzzy aggregation.
* [``fuzzy_dl_owl2.fuzzyowl2.owl_types.right_shoulder_function``] — A right-shoulder fuzzy membership function that assigns zero membership below a lower threshold, a linearly increasing degree between two parameters, and full membership at or above the upper threshold, for use in fuzzy OWL 2 ontologies.
* [``fuzzy_dl_owl2.fuzzyowl2.owl_types.sugeno_concept``] — Defines a Sugeno fuzzy integral concept for the FuzzyOWL2 framework by pairing a list of numeric weights with the fuzzy concepts they aggregate.
* [``fuzzy_dl_owl2.fuzzyowl2.owl_types.trapezoidal_function``] — A trapezoidal membership function datatype for the FuzzyOWL2 fuzzy ontology framework, defined by four x-coordinates that shape a fuzzy set with a linear rising edge, a flat plateau of full membership, and a linear falling edge.
* [``fuzzy_dl_owl2.fuzzyowl2.owl_types.triangular_function``] — A triangular membership function for fuzzy OWL 2 ontologies, defining a vague or imprecise concept through three points: a left endpoint where membership begins rising, a peak where membership reaches its maximum, and a right endpoint where it falls back to zero.
* [``fuzzy_dl_owl2.fuzzyowl2.owl_types.triangular_modifier``] — A fuzzy modifier that models a triangular membership function for the FuzzyOWL2 framework, defined by a left endpoint, a peak point of maximum membership, and a right endpoint.
* [``fuzzy_dl_owl2.fuzzyowl2.owl_types.weighted_concept``] — A weighted concept definition for the FuzzyOWL2 ontology language that pairs a numeric weight with a named fuzzy concept.
* [``fuzzy_dl_owl2.fuzzyowl2.owl_types.weighted_max_concept``] — Defines a weighted-maximum fuzzy concept that aggregates a list of concept definitions under the weighted max operator for use in the FuzzyOWL2 ontology framework.
* [``fuzzy_dl_owl2.fuzzyowl2.owl_types.weighted_min_concept``] — Defines a weighted minimum aggregation operator that combines several fuzzy concept definitions into a single composite fuzzy concept within the FuzzyOWL2 framework.
* [``fuzzy_dl_owl2.fuzzyowl2.owl_types.weighted_sum_concept``] — Defines a weighted sum concept for the FuzzyOWL2 framework, aggregating a list of fuzzy concept definitions into a single composite concept.
* [``fuzzy_dl_owl2.fuzzyowl2.owl_types.weighted_sum_zero_concept``] — Defines a fuzzy ontology concept expressing a weighted sum of component concepts that must equal zero, serving as a typed container for the operand concept definitions.

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
   /api/fuzzy_dl_owl2/fuzzyowl2/owl_types/triangular_modifier/index
   /api/fuzzy_dl_owl2/fuzzyowl2/owl_types/weighted_concept/index
   /api/fuzzy_dl_owl2/fuzzyowl2/owl_types/weighted_max_concept/index
   /api/fuzzy_dl_owl2/fuzzyowl2/owl_types/weighted_min_concept/index
   /api/fuzzy_dl_owl2/fuzzyowl2/owl_types/weighted_sum_concept/index
   /api/fuzzy_dl_owl2/fuzzyowl2/owl_types/weighted_sum_zero_concept/index