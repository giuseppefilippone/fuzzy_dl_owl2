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

A reasoning engine for fuzzy description logic that executes complex queries—such as consistency checks, membership evaluation, and subsumption—using mixed-integer linear programming optimization.


Description
-----------


The software provides a structured framework for performing automated reasoning on fuzzy knowledge bases, utilizing a hierarchy of abstract base classes to define standard interfaces for various logical operations. By leveraging mixed-integer linear programming, the system transforms complex fuzzy logic tasks—such as determining minimum and maximum membership degrees, subsumption relationships, and concept satisfiability—into solvable mathematical optimization problems. Specialized sub-organizations handle distinct reasoning strategies, including the calculation of upper and lower bounds for truth values, the conversion of fuzzy sets into crisp numbers through defuzzification, and the verification of global consistency across the ontology. To ensure data integrity during these intensive computations, the architecture consistently clones the knowledge base before execution, allowing for isolated modifications and dynamic blocking strategies without affecting the original state.


Modules
-------


* [``fuzzy_dl_owl2.fuzzydl.query.all_instances_query``] — A class that retrieves all individuals belonging to a specific concept within a fuzzy knowledge base and calculates their respective degrees of membership.
* [``fuzzy_dl_owl2.fuzzydl.query.bnp_query``] — Encapsulates a query to calculate the best non-fuzzy performance value for a specific triangular fuzzy number.
* [``fuzzy_dl_owl2.fuzzydl.query.classification_query``] — A specialized query that executes the classification process on a knowledge base to verify consistency.
* [``fuzzy_dl_owl2.fuzzydl.query.instance_query``] — An abstract base class provides a framework for querying the membership degree of a specific individual within a given concept.
* [``fuzzy_dl_owl2.fuzzydl.query.kb_satisfiable_query``] — A query implementation that determines the logical consistency and satisfiability of a fuzzy knowledge base by verifying if at least one valid interpretation exists for all defined axioms.
* [``fuzzy_dl_owl2.fuzzydl.query.query``] — An abstract base class defines the standard interface and timing utilities for executing queries against a fuzzy knowledge base.
* [``fuzzy_dl_owl2.fuzzydl.query.related_query``] — An abstract base class defines a foundational interface for evaluating role assertions and determining degrees of membership between individuals in a fuzzy logic system.
* [``fuzzy_dl_owl2.fuzzydl.query.satisfiable_query``] — An abstract base class that defines the structure for evaluating the satisfiability of fuzzy concepts within a fuzzy description logic system.
* [``fuzzy_dl_owl2.fuzzydl.query.subsumption_query``] — An abstract base class designed to structure and validate fuzzy subsumption queries between two abstract concepts.


Sub-packages
------------


* [``fuzzy_dl_owl2.fuzzydl.query.defuzzify``] — A framework for converting fuzzy membership degrees into crisp numerical values using Mixed-Integer Linear Programming strategies.
* [``fuzzy_dl_owl2.fuzzydl.query.max``] — A reasoning framework that calculates maximum truth values, membership degrees, and subsumption levels within fuzzy ontologies by formulating and solving mixed-integer linear programming problems.
* [``fuzzy_dl_owl2.fuzzydl.query.min``] — A collection of mixed-integer linear programming solvers that determine the minimum degrees of instance membership, subsumption, satisfiability, and role relationships within a fuzzy description logic framework.

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

