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

A parsing engine that translates textual Fuzzy Description Logic definitions into a structured knowledge base and executable queries for reasoning tasks.


Description
-----------


A comprehensive grammar implemented via the ``pyparsing`` library interprets a domain-specific language for Fuzzy Description Logic, transforming raw text into a structured object model. Support covers a diverse range of fuzzy logic constructs—such as abstract and concrete concepts, modifiers, and weighted aggregations—while dynamically adjusting to various logic semantics including Zadeh, Lukasiewicz, and classical logic. Static callback methods validate input and instantiate domain-specific entities like ``Concept``, ``Individual``, and ``Degree``, registering them within a central ``KnowledgeBase`` to maintain global state. Beyond constructing the domain model, extracted query definitions—ranging from satisfiability checks to instance retrieval—are compiled into executable objects ready for processing by the underlying reasoning engine and Mixed-Integer Linear Programming solver.


Modules
-------


* [``fuzzy_dl_owl2.fuzzydl.parser.dl_parser``] — A comprehensive parser for Fuzzy Description Logic that utilizes the pyparsing library to transform textual definitions into a structured knowledge base and executable queries.

.. ── LLM-GENERATED DESCRIPTION END ──

Submodules
----------

.. toctree::
   :maxdepth: 1

   /api/fuzzy_dl_owl2/fuzzydl/parser/dl_parser/index

