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

A translation framework converts OWL2 ontologies annotated with fuzzy logic semantics into a Fuzzy Description Logic representation suitable for reasoning engines.


Description
-----------


An inheritance-based type system models complex mathematical constructs, ranging from basic membership functions to advanced aggregation operators like Choquet and Sugeno integrals, providing the structural foundation for representing uncertainty. Specialized XML parsing logic extracts these semantic definitions from input files, instantiating corresponding Python objects that encapsulate linguistic modifiers and axiom degrees while safely handling configuration and error states. The translation process extends these base structures to map OWL entities such as classes and properties into their fuzzy logic equivalents, managing complex expressions like weighted sums and Ordered Weighted Averaging. Ultimately, utility components enforce a canonical hierarchy on the output, ensuring that the serialized syntax adheres to the specific requirements of the target reasoning engine.


Modules
-------


* [``fuzzy_dl_owl2.fuzzyowl2.fuzzyowl2``] — A translator that converts OWL2 ontologies annotated with fuzzy logic semantics into a Fuzzy Description Logic representation suitable for reasoning engines.
* [``fuzzy_dl_owl2.fuzzyowl2.fuzzyowl2_to_fuzzydl``] — A converter that transforms ontologies defined in the FuzzyOWL2 format into the specific syntax required by the FuzzyDL reasoner.


Sub-packages
------------


* [``fuzzy_dl_owl2.fuzzyowl2.owl_types``] — A comprehensive type system for the FuzzyOWL2 ontology framework that models fuzzy logic concepts, datatypes, properties, and aggregation operators through an inheritance-based architecture.
* [``fuzzy_dl_owl2.fuzzyowl2.parser``] — Specialized XML parsing logic transforms FuzzyOWL2 annotations into corresponding Python data structures for fuzzy logic concepts, datatypes, and properties.
* [``fuzzy_dl_owl2.fuzzyowl2.util``] — Foundational utilities support the parsing, construction, and canonical ordering of FuzzyOWL2 and fuzzy-DL logic.

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

