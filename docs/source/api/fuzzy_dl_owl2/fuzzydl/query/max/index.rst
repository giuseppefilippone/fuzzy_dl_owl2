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

    .. raw:: latex

       \begin{landscape}

       \vspace*{\fill}

    .. figure:: /_uml/module_fuzzy_dl_owl2_fuzzydl_query_max.pdf
       :alt: UML Class Diagram for fuzzy_dl_owl2.fuzzydl.query.max
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **fuzzy_dl_owl2.fuzzydl.query.max**

    .. raw:: latex

       \vspace*{\fill}

       \end{landscape}

.. py:module:: fuzzy_dl_owl2.fuzzydl.query.max



.. ── LLM-GENERATED DESCRIPTION START ──

A suite of reasoning components that computes maximum degrees of membership, truth, and subsumption within fuzzy ontologies by formulating and solving mixed-integer linear programming problems.


Description
-----------


These reasoning components leverage mixed-integer linear programming to determine the highest possible truth values for various logical constructs, including concept membership, role relationships, and subsumption hierarchies. To ensure data integrity during complex optimization tasks, the architecture operates on cloned instances of the knowledge base rather than modifying the source data directly. The underlying logic transforms fuzzy description logic problems into mathematical constraints, often converting maximization objectives into minimization tasks through negation or constructing specific implication concepts based on the chosen logical operator. Robustness is built into the workflow through consistency checks of the ABox and exception handling for contradictory ontologies, ensuring that the solver returns valid solution states or appropriate error indicators.


Modules
-------


* ``fuzzy_dl_owl2.fuzzydl.query.max.max_instance_query`` — A reasoning query that computes the maximum degree of membership for a specific individual within a given concept by solving a mixed-integer linear programming optimization problem.
* ``fuzzy_dl_owl2.fuzzydl.query.max.max_query`` — A query operation that determines the maximum possible value of a specific expression within a fuzzy knowledge base by transforming the problem into a minimization task.
* ``fuzzy_dl_owl2.fuzzydl.query.max.max_related_query`` — A software component that calculates the maximum truth degree of a role relationship between two individuals in a fuzzy ontology.
* ``fuzzy_dl_owl2.fuzzydl.query.max.max_satisfiable_query`` — A query mechanism that calculates the maximal degree of satisfiability for a fuzzy concept within a fuzzy description logic knowledge base, optionally scoped to a specific individual.
* ``fuzzy_dl_owl2.fuzzydl.query.max.max_subsumes_query`` — Determines the maximum degree to which one fuzzy concept is subsumed by another by transforming the logical relationship into a minimization problem within a knowledge base.

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

