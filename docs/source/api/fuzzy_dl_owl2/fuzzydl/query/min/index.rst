fuzzy_dl_owl2.fuzzydl.query.min
===============================

.. only:: html

    .. figure:: /_uml/module_fuzzy_dl_owl2_fuzzydl_query_min.png
       :alt: UML Class Diagram for fuzzy_dl_owl2.fuzzydl.query.min
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **fuzzy_dl_owl2.fuzzydl.query.min**

.. only:: latex

    .. figure:: /_uml/module_fuzzy_dl_owl2_fuzzydl_query_min.pdf
       :alt: UML Class Diagram for fuzzy_dl_owl2.fuzzydl.query.min
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **fuzzy_dl_owl2.fuzzydl.query.min**

.. py:module:: fuzzy_dl_owl2.fuzzydl.query.min



.. ── LLM-GENERATED DESCRIPTION START ──

A collection of mixed-integer linear programming solvers that determine the minimum degrees of instance membership, subsumption, satisfiability, and role relationships within a fuzzy description logic framework.


Description
-----------


These components collectively transform complex fuzzy logic problems—such as determining the greatest lower bound of truth values for concepts, roles, or subsumption relationships—into mathematical optimization tasks solvable via mixed-integer linear programming. To ensure data integrity and isolation during the resolution process, the architecture consistently clones the knowledge base before applying transformations, allowing the system to modify the structure without affecting the original ontology state. Robust error handling is embedded throughout the logic to gracefully manage inconsistent ontology states by returning designated failure solutions instead of propagating exceptions, while dynamic blocking mechanisms are employed to handle existential restrictions efficiently. Furthermore, the implementation supports various fuzzy logic operators, including Łukasiewicz and Gödel, and optimizes performance by leveraging pre-classified hierarchies to bypass complex calculations when atomic concepts are involved.


Modules
-------


* [``fuzzy_dl_owl2.fuzzydl.query.min.min_instance_query``] — A query mechanism that computes the minimum membership degree of an individual for a given concept by formulating and solving a mixed-integer linear programming problem.
* [``fuzzy_dl_owl2.fuzzydl.query.min.min_query``] — Implements a minimization query to find the lowest value of an objective expression subject to constraints in a knowledge base.
* [``fuzzy_dl_owl2.fuzzydl.query.min.min_related_query``] — A specialized query mechanism that computes the minimum degree to which two individuals are related through a specific role within a fuzzy description logic knowledge base.
* [``fuzzy_dl_owl2.fuzzydl.query.min.min_satisfiable_query``] — A query implementation that determines the minimal degree of satisfiability for a fuzzy concept within a knowledge base, optionally scoped to a specific individual.
* [``fuzzy_dl_owl2.fuzzydl.query.min.min_subsumes_query``] — A query mechanism that determines the minimum degree of subsumption between two fuzzy concepts within a knowledge base by solving a mixed-integer linear programming problem.

.. ── LLM-GENERATED DESCRIPTION END ──

Submodules
----------

.. toctree::
   :maxdepth: 1

   /api/fuzzy_dl_owl2/fuzzydl/query/min/min_instance_query/index
   /api/fuzzy_dl_owl2/fuzzydl/query/min/min_query/index
   /api/fuzzy_dl_owl2/fuzzydl/query/min/min_related_query/index
   /api/fuzzy_dl_owl2/fuzzydl/query/min/min_satisfiable_query/index
   /api/fuzzy_dl_owl2/fuzzydl/query/min/min_subsumes_query/index

