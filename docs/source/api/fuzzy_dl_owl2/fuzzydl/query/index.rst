fuzzy_dl_owl2.fuzzydl.query
===========================

.. only:: html

    .. figure:: /_uml/module_fuzzy_dl_owl2_fuzzydl_query.png
       :alt: UML Class Diagram for fuzzy_dl_owl2.fuzzydl.query
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **fuzzy_dl_owl2.fuzzydl.query**

.. only:: latex

    .. figure:: /_uml/module_fuzzy_dl_owl2_fuzzydl_query.pdf
       :alt: UML Class Diagram for fuzzy_dl_owl2.fuzzydl.query
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **fuzzy_dl_owl2.fuzzydl.query**

.. py:module:: fuzzy_dl_owl2.fuzzydl.query



.. ── LLM-GENERATED DESCRIPTION START ──

A query framework for a fuzzy description-logic reasoner that answers graded reasoning questions — how strongly an individual belongs to a concept, how strongly two individuals are related through a role, to what degree a concept is satisfiable or subsumes another, and which crisp value best represents a fuzzy feature — by reducing each question to a mixed-integer linear optimisation over a knowledge base.


Description
-----------


Fuzzy description logics treat concept membership, role participation, and subsumption as matters of degree rather than binary facts, so answering a question means computing the tightest truth value the knowledge base can justify. Every query follows a uniform lifecycle defined by an abstract base contract: a preprocessing step adapts the problem to the knowledge base, a solving step performs the actual reasoning and returns a result object, and a string conversion renders the question human-readably, with high-resolution timing instrumentation built into the common ancestor so the cost of optimisation-based reasoning is reported consistently across every variant. Between that root contract and the concrete queries sit intermediate abstract classes — one per family of questions — that capture the shared inputs (a concept and an individual, a role and two individuals, a concept with an optional individual, or a pair of concepts together with a fuzzy implication operator), reject concrete datatype-style concepts wherever graded membership is meaningless, and hold a placeholder objective expression for subclasses to populate when the question is compiled into an optimisation problem. The arrangement is a classic **template method**: each concrete query contributes only its particular encoding, while validation, state management, and lifecycle are inherited.

The unifying technical idea is the reduction of logical questions to numerical optimisation. A query introduces a fresh semi-continuous variable standing for the degree being sought, injects assertions that tie that variable to the logical relationship — typically by asserting membership in a concept or its negation at a degree of one minus the variable — and then optimises, so the program's optimum is precisely the tightest bound derivable from the knowledge base. Because the underlying mixed-integer linear programming solver performs minimisation only, the maximisation variants invert their objectives at formulation time, negating the expression or attaching a negative coefficient to the degree variable, so that minimising the negation effectively maximises the quantity of interest; the minimisation and maximisation sub-families are otherwise symmetric, spanning instance membership, role relations, satisfiability, subsumption under any supported fuzzy logic such as *Łukasiewicz*, *Gödel*, *Kleene-Dienes*, or *Zadeh*, and the extremes of arbitrary arithmetic expressions.

Robustness and safety are treated as cross-cutting concerns. Queries operate on clones of the knowledge base so that assertions, solver state, and internal bookkeeping added during setup never mutate the caller's ontology, making reasoning side-effect free and safe to repeat or run concurrently against the same knowledge base. Inconsistency discovered anywhere in the pipeline is caught and translated into a solution object explicitly flagged as inconsistent rather than propagating upward as an exception, so callers always receive a uniform result and can distinguish a genuine optimum from a failed premise. Termination is safeguarded by enabling dynamic blocking whenever existential or universal restrictions would otherwise prevent the reasoning procedure from finishing, and preprocessing keeps each optimisation problem as small as correctness allows — for instance by consulting precomputed classification results when a subsumption test involves two atomic concepts in an already-classified knowledge base, bypassing the solver entirely.

Beyond degree computation, the same interface accommodates simple triggers — classification and global satisfiability checks that reuse the pipeline while doing little more than invoking the corresponding reasoner routine and converting the outcome into a standard solution — as well as queries that bridge fuzzy and concrete knowledge. Defuzzification converts an individual's graded membership into a single crisp feature value, offering three interchangeable strategies for resolving the plateau where a membership function peaks: **Smallest of Maxima**, **Mean of Maxima**, and **Largest of Maxima** share a common pipeline that computes the individual's maximal membership degree, asserts it into a clone, locates the feature's underlying variable through the individual's role relations, and optimises, with each strategy contributing only its objective expression while the mean variant departs from the inherited skeleton to bracket both edges of the plateau and average them. A best-non-fuzzy-performance query acts as a thin adapter that delegates defuzzification of a triangular fuzzy number to the number itself, and an all-instances query illustrates the interface's flexibility by offering two strategies for enumerating a concept's members together with their degrees: composing per-individual minimum queries iteratively, or encoding the entire problem as a single optimisation pass with one variable per individual.


Modules
-------


* [``fuzzy_dl_owl2.fuzzydl.query.all_instances_query``] — A fuzzy description-logic query that finds every individual in a knowledge base belonging to a given abstract concept and reports the minimum degree to which each one satisfies it.
* [``fuzzy_dl_owl2.fuzzydl.query.bnp_query``] — A specialised query that defuzzifies a triangular fuzzy number by computing its **best non-fuzzy performance (BNP)**, i.e. the crisp value holding the highest degree of membership in the fuzzy set.
* [``fuzzy_dl_owl2.fuzzydl.query.classification_query``] — ClassificationQuery is a lightweight query type whose execution triggers classification of a fuzzy description logic knowledge base, yielding a successful solution when classification completes and an inconsistency result if it fails.
* [``fuzzy_dl_owl2.fuzzydl.query.instance_query``] — An abstract base class for fuzzy description-logic queries that determine the degree to which a specific individual is an instance of a given concept, typically to find minimum or maximum membership degrees.
* [``fuzzy_dl_owl2.fuzzydl.query.kb_satisfiable_query``] — A query that checks whether a fuzzy description-logic knowledge base is logically satisfiable, returning a solution scored at 1.0 when the base admits at least one satisfying interpretation and an inconsistency-marked solution otherwise.
* [``fuzzy_dl_owl2.fuzzydl.query.query``] — An abstract base class that defines the interface every query must follow when evaluated against a fuzzy knowledge base, complete with built-in execution-time measurement.
* [``fuzzy_dl_owl2.fuzzydl.query.related_query``] — An abstract query type that captures the shared structure needed to evaluate how strongly a role assertion holds between two individuals in a fuzzy description-logic knowledge base.
* [``fuzzy_dl_owl2.fuzzydl.query.satisfiable_query``] — An abstract base class, **SatisfiableQuery**, that prepares fuzzy satisfiability queries by validating and storing a fuzzy concept, an optional individual, and a placeholder objective expression for later minimum/maximum satisfiability evaluation.
* [``fuzzy_dl_owl2.fuzzydl.query.subsumption_query``] — An abstract base class for fuzzy subsumption queries, capturing the pair of concepts whose containment relationship is to be evaluated along with the fuzzy implication operator used to grade it.


Sub-packages
------------


* [``fuzzy_dl_owl2.fuzzydl.query.defuzzify``] — Defuzzification queries for a fuzzy description-logic reasoner that convert an individual's graded membership in a concept into a single crisp feature value, offering the Smallest of Maxima, Mean of Maxima, and Largest of Maxima strategies on top of a shared mixed-integer linear programming pipeline.
* [``fuzzy_dl_owl2.fuzzydl.query.max``] — A set of fuzzy description-logic query types that compute the maximum degree of truth for concept membership, role relations, concept satisfiability, concept subsumption, and arithmetic expressions by reformulating each maximization as a mixed-integer linear optimization problem over a knowledge base.
* [``fuzzy_dl_owl2.fuzzydl.query.min``] — A family of fuzzy description-logic queries that compute the greatest lower bound of membership degrees — for concept instances, role relations, satisfiability, subsumption, and arbitrary objective expressions — by reducing each logical question to a mixed-integer linear programming minimization.

.. ── LLM-GENERATED DESCRIPTION END ──

Submodules
----------

.. toctree::
   :maxdepth: 1

   /api/fuzzy_dl_owl2/fuzzydl/query/all_instances_query/index
   /api/fuzzy_dl_owl2/fuzzydl/query/bnp_query/index
   /api/fuzzy_dl_owl2/fuzzydl/query/classification_query/index
   /api/fuzzy_dl_owl2/fuzzydl/query/defuzzify/index
   /api/fuzzy_dl_owl2/fuzzydl/query/instance_query/index
   /api/fuzzy_dl_owl2/fuzzydl/query/kb_satisfiable_query/index
   /api/fuzzy_dl_owl2/fuzzydl/query/max/index
   /api/fuzzy_dl_owl2/fuzzydl/query/min/index
   /api/fuzzy_dl_owl2/fuzzydl/query/query/index
   /api/fuzzy_dl_owl2/fuzzydl/query/related_query/index
   /api/fuzzy_dl_owl2/fuzzydl/query/satisfiable_query/index
   /api/fuzzy_dl_owl2/fuzzydl/query/subsumption_query/index

