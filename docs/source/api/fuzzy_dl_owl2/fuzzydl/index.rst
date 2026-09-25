fuzzy_dl_owl2.fuzzydl
=====================

.. only:: html

    .. figure:: /_uml/module_fuzzy_dl_owl2_fuzzydl.png
       :alt: UML Class Diagram for fuzzy_dl_owl2.fuzzydl
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **fuzzy_dl_owl2.fuzzydl**

.. only:: latex

    .. figure:: /_uml/module_fuzzy_dl_owl2_fuzzydl.pdf
       :alt: UML Class Diagram for fuzzy_dl_owl2.fuzzydl
       :align: center
       :width: 4.7cm
       :class: uml-diagram

       UML Class Diagram for **fuzzy_dl_owl2.fuzzydl**

.. py:module:: fuzzy_dl_owl2.fuzzydl



.. ── LLM-GENERATED DESCRIPTION START ──

A fuzzy description-logic reasoning engine that parses textual knowledge bases, represents graded concepts, roles, and individuals under multiple fuzzy semantics, and reduces every reasoning question to a mixed-integer linear optimization problem dispatched to pluggable solver backends.


Description
-----------


Fuzzy description logics extend classical ontologies by letting concept membership, role participation, and subsumption carry degrees of truth in the [0, 1] interval rather than crisp verdicts, and answering a question therefore means computing the tightest truth value a knowledge base can justify — how strongly an individual belongs to a concept, how strongly two individuals are related through a role, to what degree one concept subsumes another, or which crisp value best represents a fuzzy feature. The pipeline is layered end to end and reproduces the surface syntax of the original Java fuzzyDL reasoner. A parsing front end turns source files into token streams through interchangeable pure-Python or compiled-C scanners and feeds them to either a legacy pyparsing grammar or a faster hand-written recursive-descent parser, both sharing a single semantic-action layer that validates as it parses — checking weights, reference rules, and the configured fuzzy logic, whether Łukasiewicz, Zadeh/Gödel, or classical — while incrementally populating the knowledge base and accumulating the queries to be answered. That knowledge base is assembled from a rich expression vocabulary: atomic concepts and nominals, quantified role restrictions, weighted aggregations, OWA operators, Sugeno and Choquet integrals, linguistic hedges such as *very*, and concrete-domain membership functions ranging from triangular and trapezoidal curves to triangular fuzzy numbers carrying their own arithmetic, all bound together by inclusion axioms, primitive definitions, domain and range constraints, and assertions of many kinds.

The unifying technical idea is the reduction of fuzzy reasoning to mixed-integer linear programming. Degrees of truth are polymorphic — resolved numbers, solver variables, or symbolic linear expressions — and each knows how to fold itself into algebraic expressions and inequations, so graded logical relationships compile directly into linear constraints; a central manager maps every concept or role assertion to a lazily created decision variable, embeds reusable encoding idioms such as sorting networks for cardinality reasoning and Big-M relaxations for nominals, and hands the finished problem to whichever backend is installed — Gurobi, Python-MIP, or PuLP with CBC, GLPK, HiGHS, or CPLEX — importing each lazily and optionally splitting weakly coupled problems into independent connected components. Queries follow a template-method lifecycle of preprocessing, solving, and rendering, with each concrete query contributing only its particular encoding while validation and timing are inherited; they always run against deep clones of the knowledge base, so reasoning is side-effect free, inconsistency is caught and returned as an explicit verdict rather than an exception, and defuzzification queries bridge graded membership back to crisp feature values.

Supporting machinery completes the design. Tableau-style individual nodes accumulate concepts, role relations, and datatype restrictions during inference, with dynamically generated nodes tracking lineage and blocking status so that reasoning over cyclic or unbounded role expansions terminates, while a minimal adjacency-dictionary directed graph supplies fast cycle detection for TBox acyclicity checks. Dedicated exception types separate routine ontology errors from genuine logical inconsistencies, a centralized configuration manager aligns precision and solver constants with the chosen backend, and an exporter translates the fuzzy ontology into OWL2. Value-object semantics pervade everything — hashing and equality derive from structure, operations return fresh objects rather than mutating their operands, and operator overloading lets any two concepts combine through conjunction, disjunction, and negation — so expressions deduplicate safely and compose uniformly however different their internal mathematics.


Modules
-------


* [``fuzzy_dl_owl2.fuzzydl.classification_node``] — 
* [``fuzzy_dl_owl2.fuzzydl.concept_equivalence``] — 
* [``fuzzy_dl_owl2.fuzzydl.concrete_feature``] — 
* [``fuzzy_dl_owl2.fuzzydl.domain_axiom``] — 
* [``fuzzy_dl_owl2.fuzzydl.feature_function``] — 
* [``fuzzy_dl_owl2.fuzzydl.fuzzydl_to_owl2``] — 
* [``fuzzy_dl_owl2.fuzzydl.general_concept_inclusion``] — 
* [``fuzzy_dl_owl2.fuzzydl.knowledge_base``] — 
* [``fuzzy_dl_owl2.fuzzydl.label``] — 
* [``fuzzy_dl_owl2.fuzzydl.primitive_concept_definition``] — 
* [``fuzzy_dl_owl2.fuzzydl.range_axiom``] — 
* [``fuzzy_dl_owl2.fuzzydl.relation``] — 
* [``fuzzy_dl_owl2.fuzzydl.role_parent_with_degree``] — 


Sub-packages
------------


* [``fuzzy_dl_owl2.fuzzydl.assertion``] — 
* [``fuzzy_dl_owl2.fuzzydl.concept``] — A comprehensive vocabulary of fuzzy description-logic concept expressions — spanning atomic concepts, quantified role restrictions, weighted aggregations and fuzzy integrals, linguistic modifiers, and concrete-domain membership functions — through which knowledge bases express graded membership over both symbolic and numeric features.
* [``fuzzy_dl_owl2.fuzzydl.degree``] — A polymorphic hierarchy of *degrees of truth* for a fuzzy description-logic reasoner, allowing graded concept-satisfaction values to be represented and manipulated uniformly whether they materialise as resolved numbers, solver variables, or symbolic linear expressions.
* [``fuzzy_dl_owl2.fuzzydl.exception``] — A pair of lightweight, domain-specific exceptions that give the fuzzy description logic framework dedicated error channels for distinguishing ontology-related failures — both general operating errors and logical inconsistencies — from generic runtime problems.
* [``fuzzy_dl_owl2.fuzzydl.graph``] — A minimal directed-graph component that provides the fuzzy description-logic engine with fast cycle detection for TBox acyclicity checks, serving as a **drop-in replacement** for the small slice of networkx the reasoner previously relied on.
* [``fuzzy_dl_owl2.fuzzydl.individual``] — Node-level abstractions for tableau-based fuzzy description-logic reasoning, modelling the individuals of a completion graph through a foundational named-entity type that accumulates concepts, role relations, and datatype restrictions during inference, a dynamically generated node variant that tracks lineage and blocking status, and a lightweight proxy that pairs concrete individuals with triangular fuzzy numbers.
* [``fuzzy_dl_owl2.fuzzydl.milp``] — A mixed-integer linear programming layer for a fuzzy description-logic reasoner that translates fuzzy concepts, roles, and assertions into decision variables and linear constraints, dispatches the resulting optimization problem to pluggable solver backends such as Gurobi, Python-MIP, and PuLP, and packages the outcome as degrees of satisfaction paired with consistency verdicts.
* [``fuzzy_dl_owl2.fuzzydl.modifier``] — Fuzzy-logic modifiers that serve as linguistic hedges — intensifiers and dilators such as *very* or *somewhat* — transforming fuzzy concepts by remapping their membership degrees across the normalized [0, 1] interval within a fuzzy description-logic knowledge base.
* [``fuzzy_dl_owl2.fuzzydl.parser``] — A parsing front end for the fuzzy description-logic (FDL) language that reads textual knowledge base files and produces a fully populated knowledge base together with the list of queries to be answered against it, using interchangeable parser and tokenizer implementations that range from a pure-Python pyparsing grammar to compiled C scanners.
* [``fuzzy_dl_owl2.fuzzydl.query``] — A query framework for a fuzzy description-logic reasoner that answers graded reasoning questions — how strongly an individual belongs to a concept, how strongly two individuals are related through a role, to what degree a concept is satisfiable or subsumes another, and which crisp value best represents a fuzzy feature — by reducing each question to a mixed-integer linear optimisation over a knowledge base.
* [``fuzzy_dl_owl2.fuzzydl.restriction``] — A small set of value objects that model role restrictions in a fuzzy description logic, binding a role to either a target concept or a specific named individual together with a minimum degree of truth.
* [``fuzzy_dl_owl2.fuzzydl.util``] — A support layer for a fuzzy description-logic reasoner that centralizes runtime configuration, defines the shared vocabulary behind ontology parsing and mixed-integer optimization, and supplies the logging, numeric, and debugging utilities the reasoning engine depends on.

.. ── LLM-GENERATED DESCRIPTION END ──

Submodules
----------

.. toctree::
   :maxdepth: 1

   /api/fuzzy_dl_owl2/fuzzydl/assertion/index
   /api/fuzzy_dl_owl2/fuzzydl/classification_node/index
   /api/fuzzy_dl_owl2/fuzzydl/concept/index
   /api/fuzzy_dl_owl2/fuzzydl/concept_equivalence/index
   /api/fuzzy_dl_owl2/fuzzydl/concrete_feature/index
   /api/fuzzy_dl_owl2/fuzzydl/degree/index
   /api/fuzzy_dl_owl2/fuzzydl/domain_axiom/index
   /api/fuzzy_dl_owl2/fuzzydl/exception/index
   /api/fuzzy_dl_owl2/fuzzydl/feature_function/index
   /api/fuzzy_dl_owl2/fuzzydl/fuzzydl_to_owl2/index
   /api/fuzzy_dl_owl2/fuzzydl/general_concept_inclusion/index
   /api/fuzzy_dl_owl2/fuzzydl/graph/index
   /api/fuzzy_dl_owl2/fuzzydl/individual/index
   /api/fuzzy_dl_owl2/fuzzydl/knowledge_base/index
   /api/fuzzy_dl_owl2/fuzzydl/label/index
   /api/fuzzy_dl_owl2/fuzzydl/milp/index
   /api/fuzzy_dl_owl2/fuzzydl/modifier/index
   /api/fuzzy_dl_owl2/fuzzydl/parser/index
   /api/fuzzy_dl_owl2/fuzzydl/primitive_concept_definition/index
   /api/fuzzy_dl_owl2/fuzzydl/query/index
   /api/fuzzy_dl_owl2/fuzzydl/range_axiom/index
   /api/fuzzy_dl_owl2/fuzzydl/relation/index
   /api/fuzzy_dl_owl2/fuzzydl/restriction/index
   /api/fuzzy_dl_owl2/fuzzydl/role_parent_with_degree/index
   /api/fuzzy_dl_owl2/fuzzydl/util/index

