fuzzy_dl_owl2.fuzzydl.query.max
===============================

.. only:: html

    .. figure:: /_uml/module_fuzzy_dl_owl2_fuzzydl_query_max.png
       :alt: UML Class Diagram for fuzzy_dl_owl2.fuzzydl.query.max
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **fuzzy_dl_owl2.fuzzydl.query.max**

.. only:: latex

    .. figure:: /_uml/module_fuzzy_dl_owl2_fuzzydl_query_max.pdf
       :alt: UML Class Diagram for fuzzy_dl_owl2.fuzzydl.query.max
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **fuzzy_dl_owl2.fuzzydl.query.max**

.. py:module:: fuzzy_dl_owl2.fuzzydl.query.max



.. ── LLM-GENERATED DESCRIPTION START ──

A reasoning framework that calculates maximum truth values, membership degrees, and subsumption levels within fuzzy ontologies by formulating and solving mixed-integer linear programming problems.


Description
-----------


These components utilize a unified architecture where optimization tasks are transformed into minimization problems suitable for the underlying engine, often by negating target expressions or minimizing implication assertions. To preserve the integrity of the original data structures, the execution workflow consistently clones the knowledge base before performing any modifications, ensuring that operations such as ABox resolution and dynamic blocking strategies occur on isolated instances. The software supports a variety of fuzzy logic semantics, including Łukasiewicz and Gödel operators, and handles potential ontology inconsistencies by returning designated solution statuses instead of propagating runtime errors. By leveraging mixed-integer linear programming, the system efficiently determines upper bounds for concepts, roles, and specific individuals while managing complex logical constructs like universal quantification.


Modules
-------


* [``fuzzy_dl_owl2.fuzzydl.query.max.max_instance_query``] — A reasoning query that calculates the maximum degree of membership for a specific individual within a given concept by formulating and solving a mixed-integer linear programming optimization problem.
* [``fuzzy_dl_owl2.fuzzydl.query.max.max_query``] — A query operation that calculates the maximum possible value of a specific expression within a fuzzy knowledge base by transforming the maximization problem into a minimization task.
* [``fuzzy_dl_owl2.fuzzydl.query.max.max_related_query``] — Determines the maximum degree of truth for a specific role relationship between two individuals within a fuzzy ontology using mathematical optimization.
* [``fuzzy_dl_owl2.fuzzydl.query.max.max_satisfiable_query``] — Determines the maximal degree to which a fuzzy concept is satisfiable within a given knowledge base using mixed-integer linear programming.
* [``fuzzy_dl_owl2.fuzzydl.query.max.max_subsumes_query``] — A class that calculates the maximum degree to which one fuzzy concept is subsumed by another by formulating the problem as a mixed-integer linear programming optimization task.

.. ── LLM-GENERATED DESCRIPTION END ──

Submodules
----------

.. toctree::
   :maxdepth: 1

   /api/fuzzy_dl_owl2/fuzzydl/query/max/max_instance_query/index
   /api/fuzzy_dl_owl2/fuzzydl/query/max/max_query/index
   /api/fuzzy_dl_owl2/fuzzydl/query/max/max_related_query/index
   /api/fuzzy_dl_owl2/fuzzydl/query/max/max_satisfiable_query/index
   /api/fuzzy_dl_owl2/fuzzydl/query/max/max_subsumes_query/index

