fuzzy_dl_owl2.fuzzydl.parser
============================

.. only:: html

    .. figure:: /_uml/module_fuzzy_dl_owl2_fuzzydl_parser.png
       :alt: UML Class Diagram for fuzzy_dl_owl2.fuzzydl.parser
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **fuzzy_dl_owl2.fuzzydl.parser**

.. only:: latex

    .. raw:: latex

       \begin{landscape}

       \vspace*{\fill}

    .. figure:: /_uml/module_fuzzy_dl_owl2_fuzzydl_parser.pdf
       :alt: UML Class Diagram for fuzzy_dl_owl2.fuzzydl.parser
       :align: center
       :width: 18.7cm
       :class: uml-diagram

       UML Class Diagram for **fuzzy_dl_owl2.fuzzydl.parser**

    .. raw:: latex

       \vspace*{\fill}

       \end{landscape}

.. py:module:: fuzzy_dl_owl2.fuzzydl.parser



.. ── LLM-GENERATED DESCRIPTION START ──

A specialized parser for Fuzzy Description Logic that interprets textual input to construct a knowledge base and a set of executable queries using the pyparsing library.


Description
-----------


Leveraging the pyparsing library, the software defines a comprehensive grammar for a Fuzzy Description Logic language to handle complex constructs such as fuzzy concepts, modifiers, roles, and axioms. Through syntax rules and parse actions, raw string tokens are transformed into domain-specific objects while simultaneously validating semantic constraints to enforce logic-specific rules for operators. The interpretation process populates a central ``KnowledgeBase`` instance with the structured data and accumulates a list of queries intended for reasoning tasks like subsumption checking, instance retrieval, and satisfiability analysis. Support for multiple fuzzy logic semantics, including Zadeh and Lukasiewicz, provides a flexible framework for defining and reasoning about fuzzy ontologies.


Modules
-------


* ``fuzzy_dl_owl2.fuzzydl.parser.dl_parser`` — A specialized parser for Fuzzy Description Logic that interprets textual input to construct a knowledge base and a set of executable queries using the pyparsing library.

.. ── LLM-GENERATED DESCRIPTION END ──

Submodules
----------

.. toctree::
   :maxdepth: 1

   /api/fuzzy_dl_owl2/fuzzydl/parser/dl_parser/index

