fuzzy_dl_owl2.fuzzyowl2.util
============================

.. only:: html

    .. figure:: /_uml/module_fuzzy_dl_owl2_fuzzyowl2_util.png
       :alt: UML Class Diagram for fuzzy_dl_owl2.fuzzyowl2.util
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **fuzzy_dl_owl2.fuzzyowl2.util**

.. only:: latex

    .. figure:: /_uml/module_fuzzy_dl_owl2_fuzzyowl2_util.pdf
       :alt: UML Class Diagram for fuzzy_dl_owl2.fuzzyowl2.util
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **fuzzy_dl_owl2.fuzzyowl2.util**

.. py:module:: fuzzy_dl_owl2.fuzzyowl2.util



.. ── LLM-GENERATED DESCRIPTION START ──

Foundational utilities for parsing and serializing FuzzyOWL2 ontologies by centralizing vocabulary definitions and abstracting XML construction.


Description
-----------


To support the processing of the FuzzyOWL2 language, the software separates concerns into distinct layers for lexical analysis and data serialization. One component establishes a robust parsing framework by enumerating fuzzy logic concept types and mapping specific syntax keywords to parsing objects, thereby eliminating scattered string literals and ensuring semantic correctness during token identification. Complementing the parsing logic, a builder pattern implementation abstracts the manual creation of XML elements, transforming high-level inputs like class expressions and truth degrees into a hierarchical format that strictly adheres to the FuzzyOWL2 schema. Finally, a serialization mechanism converts these generated XML trees into clean, human-readable strings, facilitating debugging and storage while maintaining a separation between the logical structure of the ontology and its physical representation.


Modules
-------


* ``fuzzy_dl_owl2.fuzzyowl2.util.constants`` — Centralizes the definition of fuzzy concept types and parsing keywords required for processing the FuzzyOWL2 ontology language.
* ``fuzzy_dl_owl2.fuzzyowl2.util.fuzzy_xml`` — A builder utility class that generates XML elements conforming to the FuzzyOWL2 ontology specification.

.. ── LLM-GENERATED DESCRIPTION END ──

Submodules
----------

.. toctree::
   :maxdepth: 1

   /api/fuzzy_dl_owl2/fuzzyowl2/util/constants/index
   /api/fuzzy_dl_owl2/fuzzyowl2/util/fuzzy_xml/index

