fuzzy_dl_owl2.fuzzyowl2
=======================

.. only:: html

    .. figure:: /_uml/module_fuzzy_dl_owl2_fuzzyowl2.png
       :alt: UML Class Diagram for fuzzy_dl_owl2.fuzzyowl2
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **fuzzy_dl_owl2.fuzzyowl2**

.. only:: latex

    .. figure:: /_uml/module_fuzzy_dl_owl2_fuzzyowl2.pdf
       :alt: UML Class Diagram for fuzzy_dl_owl2.fuzzyowl2
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **fuzzy_dl_owl2.fuzzyowl2**

.. py:module:: fuzzy_dl_owl2.fuzzyowl2



.. ── LLM-GENERATED DESCRIPTION START ──

A translation framework that converts OWL2 ontologies annotated with fuzzy logic semantics into a Fuzzy Description Logic representation suitable for reasoning engines.


Description
-----------


Software designed to bridge standard OWL2 ontologies extended with fuzzy logic annotations and specific Fuzzy Description Logic formats used by reasoning engines achieves this by parsing logic definitions from either custom annotation syntax or standard XML, transforming them into a structured object model that encapsulates complex fuzzy operators, mathematical membership functions, and linguistic hedges. An object-oriented hierarchy of abstract base classes and concrete components models these entities, supporting operations like weighted sums, OWA, and Choquet integrals while ensuring consistent interfaces for data access. Architectural design separates concerns into distinct layers for lexical analysis, data serialization, and translation, allowing the system to handle class expressions, property characteristics, and datatypes while maintaining a separation between the logical structure of the ontology and its physical representation. By systematically processing ontology annotations and axioms, the system generates a serialized text output that encapsulates the fuzzy semantics required for downstream inference tasks.


Modules
-------


* ``fuzzy_dl_owl2.fuzzyowl2.fuzzyowl2`` — A translator that converts OWL2 ontologies annotated with fuzzy logic semantics into a Fuzzy Description Logic representation suitable for reasoning.
* ``fuzzy_dl_owl2.fuzzyowl2.fuzzyowl2_to_fuzzydl`` — A translator that converts FuzzyOWL2 ontology structures into the text-based syntax required by the FuzzyDL reasoner.


Sub-packages
------------


* ``fuzzy_dl_owl2.fuzzyowl2.owl_types`` — Core type definitions and data structures for modeling fuzzy logic concepts, properties, and mathematical functions within the FuzzyOWL2 ontology framework.
* ``fuzzy_dl_owl2.fuzzyowl2.parser`` — Parsing utilities interpret Fuzzy OWL 2 logic definitions provided in either a custom annotation syntax or standard XML format, transforming them into a structured object model suitable for reasoning.
* ``fuzzy_dl_owl2.fuzzyowl2.util`` — Foundational utilities for parsing and serializing FuzzyOWL2 ontologies by centralizing vocabulary definitions and abstracting XML construction.

.. ── LLM-GENERATED DESCRIPTION END ──

Submodules
----------

.. toctree::
   :maxdepth: 1

   /api/fuzzy_dl_owl2/fuzzyowl2/fuzzyowl2/index
   /api/fuzzy_dl_owl2/fuzzyowl2/fuzzyowl2_to_fuzzydl/index
   /api/fuzzy_dl_owl2/fuzzyowl2/owl_types/index
   /api/fuzzy_dl_owl2/fuzzyowl2/parser/index
   /api/fuzzy_dl_owl2/fuzzyowl2/util/index

