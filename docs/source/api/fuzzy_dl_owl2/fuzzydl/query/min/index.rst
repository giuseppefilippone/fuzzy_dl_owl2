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

A set of optimization mechanisms for fuzzy description logic that determine minimum truth values and lower bounds by transforming logical queries into Mixed-Integer Linear Programming problems.


Description
-----------


Optimization routines transform various fuzzy description logic queries into Mixed-Integer Linear Programming problems to calculate the lowest possible truth values for concepts, roles, and expressions. By translating logical constructs such as implication, negation, and existential quantifiers into mathematical constraints, the system supports a range of fuzzy logic operators including Łukasiewicz and Zadeh. To ensure data integrity during the optimization process, the architecture operates on cloned versions of the knowledge base, thereby isolating the solver's modifications from the original data. The implementation also incorporates robust error handling for inconsistent ontologies and employs dynamic blocking strategies to manage complex logical structures during the solving phase.


Modules
-------


* ``fuzzy_dl_owl2.fuzzydl.query.min.min_instance_query`` — Calculates the greatest lower bound of membership for a specific individual relative to a given concept by transforming the logical query into a Mixed-Integer Linear Programming (MILP) optimization problem.
* ``fuzzy_dl_owl2.fuzzydl.query.min.min_query`` — Implements a minimization query designed to find the lowest possible value of a specific objective expression within a fuzzy description logic knowledge base.
* ``fuzzy_dl_owl2.fuzzydl.query.min.min_related_query`` — A query mechanism that determines the minimum membership degree of a role relationship between two individuals within a fuzzy ontology using mixed-integer linear programming.
* ``fuzzy_dl_owl2.fuzzydl.query.min.min_satisfiable_query`` — Calculates the minimal degree to which a fuzzy concept is satisfiable, either generally or for a specific individual, by transforming the logical problem into a Mixed-Integer Linear Programming optimization task.
* ``fuzzy_dl_owl2.fuzzydl.query.min.min_subsumes_query`` — Calculates the minimum degree of subsumption between two fuzzy concepts within a knowledge base using mixed-integer linear programming.

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

