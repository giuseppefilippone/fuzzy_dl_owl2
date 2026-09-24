fuzzy_dl_owl2.fuzzydl.exception
===============================

.. only:: html

    .. figure:: /_uml/module_fuzzy_dl_owl2_fuzzydl_exception.png
       :alt: UML Class Diagram for fuzzy_dl_owl2.fuzzydl.exception
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **fuzzy_dl_owl2.fuzzydl.exception**

.. only:: latex

    .. figure:: /_uml/module_fuzzy_dl_owl2_fuzzydl_exception.pdf
       :alt: UML Class Diagram for fuzzy_dl_owl2.fuzzydl.exception
       :align: center
       :width: 7.6cm
       :class: uml-diagram

       UML Class Diagram for **fuzzy_dl_owl2.fuzzydl.exception**

.. py:module:: fuzzy_dl_owl2.fuzzydl.exception





.. ── LLM-GENERATED DESCRIPTION START ──

A pair of lightweight, domain-specific exceptions that give the fuzzy description logic framework dedicated error channels for distinguishing ontology-related failures — both general operating errors and logical inconsistencies — from generic runtime problems.


Description
-----------


Error signalling for fuzzy ontology work is divided between two complementary exception types, **FuzzyOntologyException** and **InconsistentOntologyException**, each of which extends Python's built-in ``Exception`` with nothing more than a single human-readable message. The former covers general problems that arise during fuzzy ontology and fuzzy description logic operations, such as invalid concept definitions or the incorrect application of fuzzy modifiers, while the latter is reserved for genuine logical conflicts like contradictory concept definitions or unsatisfiable concepts. Both classes follow a deliberately minimal design — no additional state or behaviour is layered on top of the base class — because their value lies purely in their distinct types, which allow client code to isolate ontology-related failures at the ``except`` level without accidentally masking unrelated bugs. Splitting general errors from logical inconsistencies also lets callers respond differently depending on the nature of the problem, for instance aborting a reasoning task and reporting a diagnostic when an inconsistency is detected, while treating a malformed concept expression as a more routine failure. Because each message is forwarded unchanged to the superclass constructor, the exceptions behave exactly like standard Python errors in tracebacks, logging output, and exception handling, keeping error handling across the wider fuzzydl system both precise and easy to reason about.


Modules
-------


* [``fuzzy_dl_owl2.fuzzydl.exception.fuzzy_ontology_exception``] — A domain-specific exception for reporting errors that arise during fuzzy ontology and fuzzy description logic operations, such as invalid concept definitions or the incorrect application of fuzzy modifiers.
* [``fuzzy_dl_owl2.fuzzydl.exception.inconsistent_ontology_exception``] — A custom exception that signals logical inconsistencies detected in fuzzy ontologies, such as contradictory concept definitions or unsatisfiable concepts.

.. ── LLM-GENERATED DESCRIPTION END ──

Submodules
----------

.. toctree::
   :maxdepth: 1

   /api/fuzzy_dl_owl2/fuzzydl/exception/fuzzy_ontology_exception/index
   /api/fuzzy_dl_owl2/fuzzydl/exception/inconsistent_ontology_exception/index
