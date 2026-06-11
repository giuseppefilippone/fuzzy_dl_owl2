fuzzy_dl_owl2.fuzzydl.query.defuzzify
=====================================

.. only:: html

    .. figure:: /_uml/module_fuzzy_dl_owl2_fuzzydl_query_defuzzify.png
       :alt: UML Class Diagram for fuzzy_dl_owl2.fuzzydl.query.defuzzify
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **fuzzy_dl_owl2.fuzzydl.query.defuzzify**

.. only:: latex

    .. raw:: latex

       \begin{landscape}

       \vspace*{\fill}

    .. figure:: /_uml/module_fuzzy_dl_owl2_fuzzydl_query_defuzzify.pdf
       :alt: UML Class Diagram for fuzzy_dl_owl2.fuzzydl.query.defuzzify
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **fuzzy_dl_owl2.fuzzydl.query.defuzzify**

    .. raw:: latex

       \vspace*{\fill}

       \end{landscape}

.. py:module:: fuzzy_dl_owl2.fuzzydl.query.defuzzify



.. ── LLM-GENERATED DESCRIPTION START ──

A framework for converting fuzzy membership degrees into crisp numerical values using Mixed-Integer Linear Programming strategies.


Description
-----------


The software architecture separates the general workflow of ontology manipulation from specific mathematical optimization techniques by utilizing an abstract base class to handle knowledge base cloning, consistency checks, and variable retrieval. By asserting the maximum degree of membership for a specific individual and concept back into the system, the framework establishes a constrained environment where Mixed-Integer Linear Programming solvers can determine valid crisp values for target features. Concrete implementations extend this foundation to apply distinct defuzzification heuristics, such as identifying the smallest or largest values within the plateau of maximum membership, or calculating the arithmetic mean of these boundaries. This design pattern allows for flexible selection of optimistic, pessimistic, or average estimates while ensuring that error handling and solution normalization remain consistent across different mathematical approaches.


Modules
-------


* [``fuzzy_dl_owl2.fuzzydl.query.defuzzify.defuzzify_query``] — An abstract base class that implements the logic for converting fuzzy membership degrees into crisp values for a specific individual and feature using Mixed-Integer Linear Programming.
* [``fuzzy_dl_owl2.fuzzydl.query.defuzzify.lom_defuzzify_query``] — Implements the Largest of Maxima defuzzification strategy to convert fuzzy membership values into crisp numbers by maximizing the target variable within an optimization framework.
* [``fuzzy_dl_owl2.fuzzydl.query.defuzzify.mom_defuzzify_query``] — Implements the Mean of Maxima defuzzification strategy to derive a crisp numerical value for a specific feature of an individual within a fuzzy ontology.
* [``fuzzy_dl_owl2.fuzzydl.query.defuzzify.som_defuzzify_query``] — Implements the Smallest of Maxima defuzzification strategy to convert fuzzy logic values into crisp numerical outputs.

.. ── LLM-GENERATED DESCRIPTION END ──

Submodules
----------

.. toctree::
   :maxdepth: 1

   /api/fuzzy_dl_owl2/fuzzydl/query/defuzzify/defuzzify_query/index
   /api/fuzzy_dl_owl2/fuzzydl/query/defuzzify/lom_defuzzify_query/index
   /api/fuzzy_dl_owl2/fuzzydl/query/defuzzify/mom_defuzzify_query/index
   /api/fuzzy_dl_owl2/fuzzydl/query/defuzzify/som_defuzzify_query/index

