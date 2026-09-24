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

A family of fuzzy description-logic queries that compute the greatest lower bound of membership degrees — for concept instances, role relations, satisfiability, subsumption, and arbitrary objective expressions — by reducing each logical question to a mixed-integer linear programming minimization.


Description
-----------


Answering a question against a fuzzy ontology rarely means producing a simple yes or no; what is usually wanted is the *infimum* degree to which some logical relationship — an individual belonging to a concept, two individuals being linked by a role, a concept being satisfiable, one concept subsuming another, or an arbitrary expression — can be shown to hold. The minimization queries cover this full spectrum of standard question kinds, including subsumption under any of the supported fuzzy logics such as Łukasiewicz, Gödel, Kleene-Dienes, or Zadeh, where the chosen operators dictate how the relationship is rewritten into its corresponding fuzzy implication. The unifying architectural idea is the **reduction of logical questions to numerical optimization**: each query introduces a fresh semi-continuous variable into the underlying MILP solver to stand for the degree being sought, injects assertions that tie that variable to the logical relationship — typically by asserting membership in a concept or its negation with a degree of one minus the variable — and then minimizes that variable, so that the program's optimum is precisely the tightest lower bound derivable from the knowledge base. Every query specializes a corresponding generic query abstraction, keeping construction separate from execution and retaining the shared interface's preprocessing hooks, which lets callers treat all query kinds uniformly while each subclass contributes only its particular encoding.

Robustness and safety are treated as cross-cutting concerns throughout. Solving is deliberately side-effect free: the ABox is materialized on the original knowledge base, which is then cloned before any preprocessing constraints are applied, so the caller's ontology is never mutated by a running query. Inconsistency discovered anywhere in the pipeline is caught and translated into a dedicated solution object flagged with an inconsistent-knowledge-base status rather than propagating as a raw exception, allowing callers to distinguish a genuine optimization result from a failed premise. Termination is safeguarded by enabling dynamic blocking whenever the queried concepts contain existential restrictions, since such constructs would otherwise prevent the reasoning procedure from finishing. Efficiency is further addressed through a two-tier strategy in the subsumption case — precomputed classification results are consulted directly when the knowledge base has already been classified and both concepts are atomic, bypassing the solver entirely — while timing instrumentation is recorded around every solve to support performance reporting, and human-readable string renderings round out each query for logging and debugging purposes.


Modules
-------


* [``fuzzy_dl_owl2.fuzzydl.query.min.min_instance_query``] — A fuzzy description-logic query that computes the greatest lower bound of the degree to which a given individual is an instance of a concept, by translating the logical question into a mixed-integer linear program and minimizing a semi-continuous membership variable.
* [``fuzzy_dl_owl2.fuzzydl.query.min.min_query``] — A minimization query that computes the smallest value attainable by a given objective expression over a fuzzy description-logic knowledge base.
* [``fuzzy_dl_owl2.fuzzydl.query.min.min_related_query``] — Defines a query that computes the minimum degree to which two individuals are related through a given role in a fuzzy description-logic knowledge base, reducing the question to a mixed-integer linear programming optimisation.
* [``fuzzy_dl_owl2.fuzzydl.query.min.min_satisfiable_query``] — Defines a fuzzy description-logic query that computes the minimal degree to which a fuzzy concept is satisfiable, either in general or with respect to a specific individual, by recasting the logical question as a mixed-integer linear optimization problem.
* [``fuzzy_dl_owl2.fuzzydl.query.min.min_subsumes_query``] — A query that computes the minimum degree to which one fuzzy concept subsumes another in a fuzzy description logic knowledge base, casting the question as a mixed-integer linear programming problem.

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