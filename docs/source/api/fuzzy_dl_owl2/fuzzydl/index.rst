fuzzy_dl_owl2.fuzzydl
=====================

.. only:: html

    .. figure:: /_uml/module_fuzzy_dl_owl2_fuzzydl.png
       :alt: UML Class Diagram for fuzzy_dl_owl2.fuzzydl
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **fuzzy_dl_owl2.fuzzydl**

.. only:: latex

    .. figure:: /_uml/module_fuzzy_dl_owl2_fuzzydl.pdf
       :alt: UML Class Diagram for fuzzy_dl_owl2.fuzzydl
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **fuzzy_dl_owl2.fuzzydl**

.. py:module:: fuzzy_dl_owl2.fuzzydl



.. ── LLM-GENERATED DESCRIPTION START ──

Implements a fuzzy description logic reasoning engine that manages knowledge bases, processes axioms and concepts, and performs inference using Mixed-Integer Linear Programming solvers.


Description
-----------


The software provides a comprehensive framework for defining and reasoning over fuzzy ontologies, utilizing specialized modules to represent concepts, individuals, and various types of axioms such as general concept inclusions and domain restrictions. Logical structures are parsed and managed within a central knowledge base, allowing for complex queries and assertions that incorporate degrees of truth and modifiers inherent to fuzzy logic systems. Inference capabilities are powered by Mixed-Integer Linear Programming solvers, which handle the mathematical optimization required to determine concept satisfiability and instance relationships. Supporting infrastructure centralizes configuration management, logging, and mathematical utilities to ensure operational stability, while translation components facilitate interoperability with standard OWL2 representations.


Modules
-------


* [``fuzzy_dl_owl2.fuzzydl.classification_node``] — 
* [``fuzzy_dl_owl2.fuzzydl.concept_equivalence``] — 
* [``fuzzy_dl_owl2.fuzzydl.concrete_feature``] — 
* [``fuzzy_dl_owl2.fuzzydl.domain_axiom``] — 
* [``fuzzy_dl_owl2.fuzzydl.feature_function``] — 
* [``fuzzy_dl_owl2.fuzzydl.fuzzydl_to_owl2``] — 
* [``fuzzy_dl_owl2.fuzzydl.general_concept_inclusion``] — 
* [``fuzzy_dl_owl2.fuzzydl.knowledge_base``] — 
* [``fuzzy_dl_owl2.fuzzydl.label``] — 
* [``fuzzy_dl_owl2.fuzzydl.primitive_concept_definition``] — 
* [``fuzzy_dl_owl2.fuzzydl.range_axiom``] — 
* [``fuzzy_dl_owl2.fuzzydl.relation``] — 
* [``fuzzy_dl_owl2.fuzzydl.role_parent_with_degree``] — 


Sub-packages
------------


* [``fuzzy_dl_owl2.fuzzydl.assertion``] — 
* [``fuzzy_dl_owl2.fuzzydl.concept``] — 
* [``fuzzy_dl_owl2.fuzzydl.degree``] — 
* [``fuzzy_dl_owl2.fuzzydl.exception``] — 
* [``fuzzy_dl_owl2.fuzzydl.individual``] — 
* [``fuzzy_dl_owl2.fuzzydl.milp``] — 
* [``fuzzy_dl_owl2.fuzzydl.modifier``] — 
* [``fuzzy_dl_owl2.fuzzydl.parser``] — 
* [``fuzzy_dl_owl2.fuzzydl.query``] — 
* [``fuzzy_dl_owl2.fuzzydl.restriction``] — 
* [``fuzzy_dl_owl2.fuzzydl.util``] — Foundational infrastructure for a fuzzy description logic reasoning engine that centralizes configuration management, logging, debugging instrumentation, and mathematical utilities.

.. ── LLM-GENERATED DESCRIPTION END ──

Submodules
----------

.. toctree::
   :maxdepth: 1

   /api/fuzzy_dl_owl2/fuzzydl/assertion/index
   /api/fuzzy_dl_owl2/fuzzydl/classification_node/index
   /api/fuzzy_dl_owl2/fuzzydl/concept/index
   /api/fuzzy_dl_owl2/fuzzydl/concept_equivalence/index
   /api/fuzzy_dl_owl2/fuzzydl/concrete_feature/index
   /api/fuzzy_dl_owl2/fuzzydl/degree/index
   /api/fuzzy_dl_owl2/fuzzydl/domain_axiom/index
   /api/fuzzy_dl_owl2/fuzzydl/exception/index
   /api/fuzzy_dl_owl2/fuzzydl/feature_function/index
   /api/fuzzy_dl_owl2/fuzzydl/fuzzydl_to_owl2/index
   /api/fuzzy_dl_owl2/fuzzydl/general_concept_inclusion/index
   /api/fuzzy_dl_owl2/fuzzydl/individual/index
   /api/fuzzy_dl_owl2/fuzzydl/knowledge_base/index
   /api/fuzzy_dl_owl2/fuzzydl/label/index
   /api/fuzzy_dl_owl2/fuzzydl/milp/index
   /api/fuzzy_dl_owl2/fuzzydl/modifier/index
   /api/fuzzy_dl_owl2/fuzzydl/parser/index
   /api/fuzzy_dl_owl2/fuzzydl/primitive_concept_definition/index
   /api/fuzzy_dl_owl2/fuzzydl/query/index
   /api/fuzzy_dl_owl2/fuzzydl/range_axiom/index
   /api/fuzzy_dl_owl2/fuzzydl/relation/index
   /api/fuzzy_dl_owl2/fuzzydl/restriction/index
   /api/fuzzy_dl_owl2/fuzzydl/role_parent_with_degree/index
   /api/fuzzy_dl_owl2/fuzzydl/util/index

