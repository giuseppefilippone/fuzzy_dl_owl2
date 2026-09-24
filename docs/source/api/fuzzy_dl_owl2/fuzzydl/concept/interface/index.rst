fuzzy_dl_owl2.fuzzydl.concept.interface
=======================================

.. only:: html

    .. figure:: /_uml/module_fuzzy_dl_owl2_fuzzydl_concept_interface.png
       :alt: UML Class Diagram for fuzzy_dl_owl2.fuzzydl.concept.interface
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **fuzzy_dl_owl2.fuzzydl.concept.interface**

.. only:: latex

    .. figure:: /_uml/module_fuzzy_dl_owl2_fuzzydl_concept_interface.pdf
       :alt: UML Class Diagram for fuzzy_dl_owl2.fuzzydl.concept.interface
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **fuzzy_dl_owl2.fuzzydl.concept.interface**

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.interface





.. ── LLM-GENERATED DESCRIPTION START ──

A family of abstract mixin interfaces that standardise how fuzzy description-logic concept expressions store, inspect, and replace the operands they carry, whether a single concept, a collection of concepts, a role, a filler value, or a weighted set of concepts.


Description
-----------


Concept constructors in a fuzzy description-logic framework — unary modifiers, compound expressions, qualified restrictions such as ∃R.C, and weighted aggregations — all need somewhere to keep the operands they operate on, and rather than duplicating that state-management boilerplate across every concrete class, a set of small abstract base classes factors it out into reusable, mixin-style contracts. Each contract is declared abstract, contributes no behaviour beyond storage, and funnels all reads and writes through property pairs, giving downstream code one consistent API for inspecting or swapping an operand regardless of which kind of operand-bearing concept it encounters.

The contracts are designed to compose: role-and-concept ownership is expressed by merging the role-holding and concept-holding abstractions into a single pairing that mirrors the inseparable role–concept structure of qualified restrictions, value-carrying concepts layer a deliberately untyped filler value on top of role handling, and weighted aggregations extend the multi-concept contract with an optional list of numerical weights, where an explicitly unset weight collection is kept distinct from an empty one so callers can distinguish "no weighting applied" from "all weights are zero". Initialisation is kept explicit and predictable — parent constructors are invoked directly in a fixed order rather than through cooperative super() calls, sidestepping method-resolution-order subtleties — while storage itself remains minimal and permissive: iterables are materialised into plain lists to protect against one-shot generators being consumed, but no validation or deep copying is performed, so mutable operands assigned through the properties stay shared with the caller and later mutations remain visible through the getters. The result is a layered, modular foundation in which role handling, concept handling, and value handling can evolve independently, while every concrete concept class inherits a predictable, encapsulated way to track the operands it manipulates.


Modules
-------


* [``fuzzy_dl_owl2.fuzzydl.concept.interface.has_concept_interface``] — An abstract interface that lets implementing classes wrap, inspect, and replace a single fuzzy ``Concept`` object through a managed property.
* [``fuzzy_dl_owl2.fuzzydl.concept.interface.has_concepts_interface``] — An abstract base class that provides its subclasses with shared, mutable storage for a collection of fuzzy concepts, along with a property for reading and replacing them.
* [``fuzzy_dl_owl2.fuzzydl.concept.interface.has_role_concept_interface``] — An abstract base class that combines role and concept ownership into a single contract, requiring concrete subclasses to manage both a string-based role and an associated ``Concept`` object.
* [``fuzzy_dl_owl2.fuzzydl.concept.interface.has_role_interface``] — An abstract base class equips description-logic concepts with a uniform way to store, read, and update the role (binary relation) they are associated with.
* [``fuzzy_dl_owl2.fuzzydl.concept.interface.has_value_interface``] — An abstract base class that augments role-based fuzzy description-logic concepts with the ability to carry and expose an arbitrary filler value.
* [``fuzzy_dl_owl2.fuzzydl.concept.interface.has_weighted_concepts_interface``] — An abstract interface that augments basic concept management with an optional collection of numerical weights, enabling objects to represent weighted aggregations of concepts in a fuzzy description-logic setting.

.. ── LLM-GENERATED DESCRIPTION END ──

Submodules
----------

.. toctree::
   :maxdepth: 1

   /api/fuzzy_dl_owl2/fuzzydl/concept/interface/has_concept_interface/index
   /api/fuzzy_dl_owl2/fuzzydl/concept/interface/has_concepts_interface/index
   /api/fuzzy_dl_owl2/fuzzydl/concept/interface/has_role_concept_interface/index
   /api/fuzzy_dl_owl2/fuzzydl/concept/interface/has_role_interface/index
   /api/fuzzy_dl_owl2/fuzzydl/concept/interface/has_value_interface/index
   /api/fuzzy_dl_owl2/fuzzydl/concept/interface/has_weighted_concepts_interface/index
