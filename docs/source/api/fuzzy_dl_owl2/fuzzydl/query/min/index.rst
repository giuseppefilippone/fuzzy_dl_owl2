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

    .. raw:: latex

       \begin{landscape}

       \vspace*{\fill}

    .. figure:: /_uml/module_fuzzy_dl_owl2_fuzzydl_query_min.pdf
       :alt: UML Class Diagram for fuzzy_dl_owl2.fuzzydl.query.min
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **fuzzy_dl_owl2.fuzzydl.query.min**

    .. raw:: latex

       \vspace*{\fill}

       \end{landscape}

.. py:module:: fuzzy_dl_owl2.fuzzydl.query.min



.. ── LLM-GENERATED DESCRIPTION START ──

Specialized query implementations that compute minimum degrees of membership, subsumption, and satisfiability within fuzzy description logic knowledge bases using Mixed-Integer Linear Programming.


Description
-----------


These components transform logical verification tasks into mathematical optimization problems, specifically utilizing Mixed-Integer Linear Programming to minimize variables representing degrees of truth or membership. To preserve the integrity of the underlying data, the architecture operates on cloned instances of the knowledge base, allowing for the temporary application of constraints and assertions without affecting the original state. The logic supports a wide range of fuzzy logic operators and handles complex scenarios such as existential restrictions, role relationships between individuals, and concept subsumption. Robust error management is integrated to handle ontology inconsistencies by returning designated failure solutions, while performance is enhanced by checking pre-classified hierarchies to bypass full optimization when possible.


Modules
-------


* [``fuzzy_dl_owl2.fuzzydl.query.min.min_instance_query``] — Calculates the greatest lower bound of membership for a specific individual relative to a given concept using Mixed-Integer Linear Programming optimization.
* [``fuzzy_dl_owl2.fuzzydl.query.min.min_query``] — A query implementation that calculates the minimum possible value of a specific expression within a fuzzy description logic knowledge base.
* [``fuzzy_dl_owl2.fuzzydl.query.min.min_related_query``] — A query mechanism that determines the minimum degree to which two individuals are related through a specific role within a fuzzy description logic knowledge base.
* [``fuzzy_dl_owl2.fuzzydl.query.min.min_satisfiable_query``] — Calculates the minimal degree of satisfiability for a fuzzy concept using Mixed-Integer Linear Programming optimization.
* [``fuzzy_dl_owl2.fuzzydl.query.min.min_subsumes_query``] — A query mechanism that computes the minimum degree of subsumption between two fuzzy concepts within a knowledge base by formulating and solving a mixed-integer linear programming problem.

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

