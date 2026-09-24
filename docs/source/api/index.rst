API Reference
=============

This page contains auto-generated API reference documentation [#f1]_.




.. ── LLM-GENERATED DESCRIPTION START ──

A fuzzy description-logic toolkit that answers graded ontology questions — how strongly an individual belongs to a concept, how strongly two individuals are related through a role, and to what degree one concept subsumes another — by reducing fuzzy reasoning to mixed-integer linear optimization over pluggable solver backends, and that translates fuzzy OWL 2 ontologies into the textual knowledge-base format the reasoning engine consumes.


Description
-----------


Fuzzy description logics extend classical ontologies by letting concept membership, role participation, and subsumption carry degrees of truth in the [0, 1] interval rather than crisp verdicts, and answering a question therefore means computing the tightest truth value a knowledge base can justify. Two cooperating halves serve that goal. A complete reasoning engine parses textual knowledge bases written in the surface syntax of the original Java fuzzyDL reasoner, assembles graded concepts, roles, and individuals under several fuzzy semantics — Łukasiewicz, Zadeh/Gödel, or classical — and answers queries against them. A translation framework converts fuzzy-logic-annotated OWL 2 ontologies into the S-expression command language that engine reads, while an exporter moves in the opposite direction, so fuzzy knowledge can flow between the OWL 2 world and the reasoner both ways.

On the reasoning side, a parsing front end turns source files into token streams through interchangeable pure-Python or compiled-C scanners and feeds them to either a legacy pyparsing grammar or a faster hand-written recursive-descent parser, both sharing a single semantic-action layer that validates weights, reference rules, and the configured fuzzy logic while incrementally populating the knowledge base. The expression vocabulary those parsers build is deliberately rich, spanning atomic concepts and nominals, quantified role restrictions, weighted aggregations, ordered weighted averaging operators, Sugeno and Choquet integrals, linguistic hedges such as *very*, and concrete-domain membership functions from triangular and trapezoidal curves to triangular fuzzy numbers with their own arithmetic, all bound together by inclusion axioms, primitive definitions, domain and range constraints, and assertions of many kinds. The unifying technical idea is the reduction of fuzzy reasoning to mixed-integer linear programming: degrees of truth are polymorphic — resolved numbers, solver variables, or symbolic linear expressions — and each knows how to fold itself into algebraic expressions and inequations, so graded logical relationships compile directly into linear constraints. A central manager maps every concept or role assertion to a lazily created decision variable, embeds reusable encoding idioms such as sorting networks for cardinality reasoning and Big-M relaxations for nominals, and hands the finished problem to whichever backend is installed — Gurobi, Python-MIP, or PuLP with CBC, GLPK, HiGHS, or CPLEX — importing each lazily and optionally splitting weakly coupled problems into independent connected components. Queries follow a template-method lifecycle of preprocessing, solving, and rendering, always running against deep clones of the knowledge base, so reasoning is side-effect free, inconsistency is returned as an explicit verdict rather than an exception, and defuzzification queries bridge graded membership back to crisp feature values. Tableau-style individual nodes accumulate concepts, role relations, and datatype restrictions during inference, with dynamically generated nodes tracking lineage and blocking status so that reasoning over cyclic or unbounded role expansions terminates, while a minimal directed-graph component supplies fast cycle detection for TBox acyclicity checks.

The translation framework is organized as a layered pipeline in which parsing, representation, orchestration, and serialization are kept deliberately separate. Its representation layer is a family of typed data holders arranged in four parallel class hierarchies — concept definitions, fuzzy datatypes, modifiers, and properties — each anchored by a non-instantiable abstract base, with every concrete subclass tagging itself with a type discriminator so that parsers, serialisers, and reasoners handle all constructs polymorphically through a shared contract; the objects are intentionally thin, deferring validation and evaluation entirely to downstream machinery. A stateless parsing layer, hardened with *defusedxml* for untrusted input, turns XML annotations into those typed objects, while an orchestrator walks the ontology in stages, harvesting fuzzy annotations from the header, datatype, class, and property declarations first, then processing TBox, RBox, and ABox axioms in two passes so that graded axioms are emitted before crisp ones, with deduplication preventing redundant output. The concrete serializer emits real commands, coping with the target language through IRI name mangling, keyword-clash avoidance, lazy declaration of data properties, mapping of XML Schema datatypes onto built-in numeric, boolean, and string types, and explicit error reporting — never silent dropping — for constructs the reasoner cannot express, such as cardinality restrictions, property chains, or fuzzy nominals. A utilities layer acts as a single source of truth for the language's vocabulary, binding every keyword to a ready-made grammar element so that grammars and markup are assembled from one registry, and a data-driven sorter reorders the generated statements to mirror the page-by-page command sequence of the reference manual, keeping the output human-readable.

Value-object semantics pervade the whole design: hashing and equality derive from structure, operations return fresh objects rather than mutating their operands, and operator overloading lets any two concepts combine through conjunction, disjunction, and negation, so expressions deduplicate safely and compose uniformly however different their internal mathematics. A centralized configuration manager aligns precision and solver constants with the chosen backend, dedicated exception types separate routine ontology errors from genuine logical inconsistencies, and the overall philosophy is declarative and side-effect free, which makes the supported fuzzy vocabulary easy to audit and extend.


Sub-packages
------------


* [``fuzzy_dl_owl2.fuzzydl``] — A fuzzy description-logic reasoning engine that parses textual knowledge bases, represents graded concepts, roles, and individuals under multiple fuzzy semantics, and reduces every reasoning question to a mixed-integer linear optimization problem dispatched to pluggable solver backends.
* [``fuzzy_dl_owl2.fuzzyowl2``] — A translation framework that converts fuzzy-logic-annotated OWL 2 ontologies into the S-expression knowledge-base format consumed by the FuzzyDL fuzzy description-logic reasoner.

.. ── LLM-GENERATED DESCRIPTION END ──

.. toctree::
   :titlesonly:

   /api/fuzzy_dl_owl2/index

.. [#f1] Created with `sphinx-autoapi <https://github.com/readthedocs/sphinx-autoapi>`_