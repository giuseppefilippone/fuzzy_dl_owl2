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

A translation framework that converts OWL2 ontologies annotated with fuzzy logic into the specific syntax required by Fuzzy Description Logic reasoners.


Description
-----------


The software processes OWL2 ontology files to extract fuzzy logic semantics defined through annotations, transforming them into a format compatible with Fuzzy Description Logic reasoners. It relies on a comprehensive type system of abstract base classes and concrete implementations to model complex fuzzy constructs, such as triangular functions, linear modifiers, and aggregation operators like OWA or Sugeno integrals. Specialized parsing logic utilizing both pyparsing and standard XML analysis interprets these fuzzy elements, converting raw text or tokens into strongly typed domain objects while a central dispatch mechanism orchestrates the translation flow. Foundational utilities manage the fuzzy logic vocabulary, generate compliant XML, and organize ontology statements to ensure the output adheres to specification standards and maintains a consistent order for downstream processing.


Modules
-------


* [``fuzzy_dl_owl2.fuzzyowl2.fuzzyowl2``] — A translator that converts OWL2 ontologies annotated with fuzzy logic into a Fuzzy Description Logic representation for use in reasoning systems.
* [``fuzzy_dl_owl2.fuzzyowl2.fuzzyowl2_to_fuzzydl``] — A converter that transforms ontologies defined in the FuzzyOWL2 format into the specific syntax required by the FuzzyDL reasoner.


Sub-packages
------------


* [``fuzzy_dl_owl2.fuzzyowl2.owl_types``] — Core data structures and abstract interfaces for defining fuzzy logic concepts, properties, and datatypes within the FuzzyOWL2 ontology framework.
* [``fuzzy_dl_owl2.fuzzyowl2.parser``] — Specialized parsing logic transforms Fuzzy OWL 2 XML annotations and grammar-based strings into internal knowledge bases and fuzzy logic objects.
* [``fuzzy_dl_owl2.fuzzyowl2.util``] — Foundational utilities for managing fuzzy logic vocabulary, generating compliant XML, and organizing ontology statements according to specification standards.

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

