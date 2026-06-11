# Summary

A comprehensive fuzzy description logic reasoner that manages knowledge bases and performs automated reasoning by translating fuzzy axioms into Mixed-Integer Linear Programming constraints.

## Description

The architecture constructs complex logical expressions—ranging from standard conjunctions and disjunctions to advanced aggregations like Choquet integrals and Ordered Weighted Averaging—through a composite object model that supports operator overloading and linguistic modifiers. Reasoning is facilitated by a central engine that employs tableau-based algorithms to normalize terminologies and manage assertional data, ultimately bridging the gap between abstract fuzzy logic and concrete optimization models. To support interoperability and high-performance processing, the system includes a high-performance parser for textual definitions and a translation engine that exports fuzzy knowledge bases to standard OWL2 ontologies via XML annotations.

## Modules

- [`fuzzy_dl_owl2.fuzzydl.classification_node`] — A graph node entity that models concepts within a classification hierarchy, managing global collections of equivalent names and weighted directed edges for a fuzzy description logic reasoner.
- [`fuzzy_dl_owl2.fuzzydl.concept_equivalence`] — Encapsulates the logical equivalence between two distinct concepts within a fuzzy description logic framework.
- [`fuzzy_dl_owl2.fuzzydl.concrete_feature`] — A class that models a specific attribute of an individual characterized by a name and a data type such as string, boolean, integer, or real.
- [`fuzzy_dl_owl2.fuzzydl.domain_axiom`] — Encapsulates a logical constraint defining the domain of a specific role within an ontology by associating it with a concept.
- [`fuzzy_dl_owl2.fuzzydl.feature_function`] — A polymorphic class representing mathematical expressions over features that can be recursively traversed to extract dependencies and converted into linear programming constraints.
- [`fuzzy_dl_owl2.fuzzydl.fuzzydl_to_owl2`] — A translation engine that converts FuzzyDL knowledge bases into OWL2 ontologies by embedding fuzzy logic semantics as XML annotations within standard semantic web structures.
- [`fuzzy_dl_owl2.fuzzydl.general_concept_inclusion`] — A Python class representing a fuzzy logic axiom that defines the graded inclusion of one concept within another.
- [`fuzzy_dl_owl2.fuzzydl.knowledge_base`] — The `KnowledgeBase` class acts as the central engine for a fuzzy description logic knowledge base, managing the TBox, ABox, and RBox components. It implements a tableau-based reasoning algorithm that translates fuzzy axioms into constraints for a Mixed-Integer Linear Programming (MILP) solver. The class handles the preprocessing of the Terminological Box (TBox), including normalization and absorption of axioms based on the configured fuzzy logic semantics (Lukasiewicz, Zadeh, Gödel, Kleene-Dienes). It manages the Assertional Box (ABox) by iteratively applying inference rules to assertions, creating and merging individuals to satisfy existential and universal restrictions, and enforcing blocking strategies to ensure algorithm termination. The system supports multiple fuzzy logic types and optimizations such as lazy unfolding and absorption to improve reasoning efficiency. It also provides functionality to serialize the knowledge base to and from files, compute the Description Logic expressivity of the ontology, and interface with an MILP solver to determine truth degrees and optimize expressions.
- [`fuzzy_dl_owl2.fuzzydl.label`] — Encapsulates a fuzzy concept paired with a specific degree of satisfaction to form a weighted annotation.
- [`fuzzy_dl_owl2.fuzzydl.primitive_concept_definition`] — A Python class representing a primitive concept definition within a fuzzy logic system, encapsulating the relationship between a named concept and its definition using specific implication operators and truth degrees.
- [`fuzzy_dl_owl2.fuzzydl.range_axiom`] — Encapsulates a range axiom to enforce that individuals related by a specific role must belong to a defined concept.
- [`fuzzy_dl_owl2.fuzzydl.relation`] — Defines a data structure for representing fuzzy role assertions connecting two individuals through a specific relationship type constrained by a lower bound degree.
- [`fuzzy_dl_owl2.fuzzydl.role_parent_with_degree`] — Encapsulates a weighted relationship between a role and its parent by storing the parent's identifier and an associated degree of inclusion.

## Sub-packages

- [`fuzzy_dl_owl2.fuzzydl.assertion`] — A framework for modeling fuzzy logic constraints that enforce minimum membership thresholds for individuals and concepts.
- [`fuzzy_dl_owl2.fuzzydl.concept`] — A comprehensive framework for fuzzy description logic that provides the structural foundation and operational mechanics for constructing, manipulating, and normalizing logical concepts.
- [`fuzzy_dl_owl2.fuzzydl.degree`] — A polymorphic framework for representing fuzzy logic degrees as concrete numeric values or symbolic algebraic entities to support arithmetic operations and constraint generation within mixed-integer linear programming models.
- [`fuzzy_dl_owl2.fuzzydl.exception`] — Specialized exception handling mechanisms for fuzzy description logic frameworks and ontology validation.
- [`fuzzy_dl_owl2.fuzzydl.graph`] — A high-performance directed graph implementation optimized for rapid cycle detection and edge construction during knowledge base acyclicity checks.
- [`fuzzy_dl_owl2.fuzzydl.individual`] — A framework for modeling individual entities, dynamic node generation, and fuzzy constraint representation within tableau-based fuzzy description logic reasoning.
- [`fuzzy_dl_owl2.fuzzydl.milp`] — A Mixed-Integer Linear Programming framework designed to translate fuzzy description logic constructs into solvable mathematical optimization models.
- [`fuzzy_dl_owl2.fuzzydl.modifier`] — A framework for applying mathematical transformations to fuzzy logic membership degrees through abstract and concrete modifier implementations.
- [`fuzzy_dl_owl2.fuzzydl.parser`] — A comprehensive parsing framework for Fuzzy Description Logic that transforms textual definitions into executable knowledge bases and queries through a multi-layered architecture supporting both standard and high-performance execution modes.
- [`fuzzy_dl_owl2.fuzzydl.query`] — A reasoning engine for fuzzy description logic that executes complex queries—such as consistency checks, membership evaluation, and subsumption—using mixed-integer linear programming optimization.
- [`fuzzy_dl_owl2.fuzzydl.restriction`] — A framework for modeling fuzzy description logic restrictions that enforce constraints on roles, concepts, and specific individuals with varying degrees of certainty.
- [`fuzzy_dl_owl2.fuzzydl.util`] — Foundational infrastructure supporting a fuzzy description logic reasoning engine by centralizing configuration management, defining core operational constants, and providing cross-cutting utilities for logging, mathematics, and runtime instrumentation.
