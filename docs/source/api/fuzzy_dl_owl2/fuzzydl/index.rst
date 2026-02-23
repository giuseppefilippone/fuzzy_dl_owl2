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
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **fuzzy_dl_owl2.fuzzydl**

.. py:module:: fuzzy_dl_owl2.fuzzydl



.. ── LLM-GENERATED DESCRIPTION START ──

A fuzzy description logic reasoning engine that combines tableau-based algorithms with Mixed-Integer Linear Programming to determine the satisfiability and truth degrees of uncertain assertions.


Description
-----------


The software provides a comprehensive framework for modeling and reasoning under uncertainty by implementing a hybrid architecture that integrates logical inference with mathematical optimization. At its core, a central controller manages the ontology state, separating the logical reasoning layer—which handles TBox preprocessing, ABox expansion, and blocking strategies—from the mathematical optimization layer responsible for solving Mixed-Integer Linear Programming problems. Complex logical constructs, including quantified role restrictions and advanced fuzzy aggregation operators like Choquet and Sugeno integrals, are translated into solvable mathematical expressions through a polymorphic system that handles degrees of satisfaction as numeric values, variables, or algebraic expressions. To support diverse reasoning tasks such as classification, subsumption checking, and instance retrieval, the system parses textual definitions into structured knowledge bases and executes queries on isolated clones of the state to ensure data integrity. Furthermore, the framework facilitates interoperability with semantic web standards by exporting fuzzy ontologies to OWL2 format, embedding fuzzy semantics as XML annotations to bridge the gap between fuzzy logic and standard web technologies.


Modules
-------


* ``fuzzy_dl_owl2.fuzzydl.classification_node`` — Defines a graph entity for fuzzy description logic concepts that maintains global collections of equivalent names and weighted directed edges.
* ``fuzzy_dl_owl2.fuzzydl.concept_equivalence`` — Encapsulates the logical axiom asserting equivalence between two distinct concepts.
* ``fuzzy_dl_owl2.fuzzydl.concrete_feature`` — A data structure representing a typed attribute with optional numeric bounds, supporting string, boolean, integer, and real types.
* ``fuzzy_dl_owl2.fuzzydl.domain_axiom`` — A class representing a domain axiom that restricts the subjects of a specific role to a defined concept.
* ``fuzzy_dl_owl2.fuzzydl.feature_function`` — A class representing mathematical expressions over features that supports arithmetic operations and conversion into linear programming constraints.
* ``fuzzy_dl_owl2.fuzzydl.fuzzydl_to_owl2`` — Converts a FuzzyDL knowledge base into a standard OWL2 ontology by mapping fuzzy logic concepts, roles, and axioms to their semantic web equivalents while preserving fuzzy semantics through XML annotations.
* ``fuzzy_dl_owl2.fuzzydl.general_concept_inclusion`` — Defines a data structure for representing fuzzy General Concept Inclusion axioms, which assert that one concept is subsumed by another to a specific degree of truth using a designated logic operator.
* ``fuzzy_dl_owl2.fuzzydl.knowledge_base`` — This file implements the core engine for a fuzzy description logic reasoner that combines a tableau-based reasoning algorithm with a Mixed-Integer Linear Programming (MILP) solver to determine the satisfiability and truth degrees of fuzzy assertions. The architecture separates the logical reasoning layer from the mathematical optimization layer, with the ``KnowledgeBase`` class acting as the central controller for the ontology state, while the ``MILPHelper`` manages the optimization model. The reasoning process is divided into distinct phases: TBox preprocessing (normalization and absorption), ABox expansion (applying inference rules), and optimization. It supports multiple fuzzy logic semantics, allowing users to choose between different interpretations of implication and conjunction. To ensure termination of the tableau expansion, the system employs blocking strategies that prevent infinite loops in the completion forest. The reasoning process is incremental, updating the MILP model with new constraints as it expands the knowledge base. Helper classes such as ``DatatypeReasoner``, ``LukasiewiczSolver``, ``ZadehSolver``, and ``ClassicalSolver`` implement the specific fuzzy logic semantics for conjunction, disjunction, and quantifiers, while ``IndividualHandler`` and ``CreatedIndividualHandler`` manage the lifecycle of individuals, including their creation, blocking, and unblocking. Additionally, the file includes serialization methods to persist the knowledge base state and cloning capabilities to copy the state without the ABox.
* ``fuzzy_dl_owl2.fuzzydl.label`` — Encapsulates a fuzzy concept paired with a degree of satisfaction to represent weighted annotations.
* ``fuzzy_dl_owl2.fuzzydl.primitive_concept_definition`` — A Python class representing a primitive concept definition within a fuzzy description logic system, encapsulating a named concept, its defining description, a truth degree, and a specific implication operator.
* ``fuzzy_dl_owl2.fuzzydl.range_axiom`` — Defines a logical constraint that restricts the permissible types of individuals associated with a specific role within a fuzzy description logic system.
* ``fuzzy_dl_owl2.fuzzydl.relation`` — Defines a data structure for representing fuzzy role assertions that link two individuals through a named relationship constrained by a lower bound degree.
* ``fuzzy_dl_owl2.fuzzydl.role_parent_with_degree`` — Models a weighted hierarchical relationship between a role and its parent by storing a parent identifier and an associated degree of inclusion.


Sub-packages
------------


* ``fuzzy_dl_owl2.fuzzydl.assertion`` — A collection of data structures for modeling fuzzy logic constraints that associate individuals with concepts based on minimum membership degrees.
* ``fuzzy_dl_owl2.fuzzydl.concept`` — A comprehensive framework for fuzzy description logic that models complex logical constructs, quantified role restrictions, and various fuzzy aggregation operators.
* ``fuzzy_dl_owl2.fuzzydl.degree`` — Defines a polymorphic architecture for representing degrees of satisfaction in fuzzy description logic systems using numeric, variable, or algebraic expression metrics.
* ``fuzzy_dl_owl2.fuzzydl.exception`` — A specialized exception hierarchy for handling errors and logical inconsistencies within fuzzy description logic frameworks.
* ``fuzzy_dl_owl2.fuzzydl.individual`` — A subsystem for managing individual entities within a fuzzy description logic ontology that supports tableau-based reasoning, hierarchical tracking, and fuzzy constraint evaluation.
* ``fuzzy_dl_owl2.fuzzydl.milp`` — A Mixed-Integer Linear Programming framework designed to translate fuzzy description logic ontologies into solvable mathematical optimization models.
* ``fuzzy_dl_owl2.fuzzydl.modifier`` — A framework for transforming fuzzy logic membership degrees through abstract interfaces and concrete mathematical implementations such as linear and triangular functions.
* ``fuzzy_dl_owl2.fuzzydl.parser`` — A specialized parser for Fuzzy Description Logic that interprets textual input to construct a knowledge base and a set of executable queries using the pyparsing library.
* ``fuzzy_dl_owl2.fuzzydl.query`` — A comprehensive framework for executing reasoning tasks over fuzzy description logic knowledge bases, utilizing Mixed-Integer Linear Programming to resolve complex logical queries.
* ``fuzzy_dl_owl2.fuzzydl.restriction`` — Implements fuzzy description logic restrictions that enforce constraints on roles and concepts using specific membership degrees.
* ``fuzzy_dl_owl2.fuzzydl.util`` — A foundational infrastructure for a fuzzy description logic reasoning engine that centralizes configuration management, standardizes logical constants, and provides essential utilities for logging, debugging, and high-precision arithmetic.

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

