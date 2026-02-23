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

A comprehensive framework for executing reasoning tasks over fuzzy description logic knowledge bases, utilizing Mixed-Integer Linear Programming to resolve complex logical queries.


Description
-----------


The architecture relies on a hierarchy of abstract base classes that define standard interfaces for various operations, including instance retrieval, classification, subsumption checks, and satisfiability verification. By translating fuzzy logic constructs into mathematical optimization problems, the system calculates precise membership degrees, truth values, and crisp defuzzified outputs while ensuring the underlying ontology remains consistent. To maintain data integrity during these intensive computations, the design frequently operates on cloned instances of the knowledge base, isolating solver modifications from the original data source. Specialized sub-modules further refine this approach by implementing specific strategies for minimization, maximization, and the conversion of fuzzy values into representative crisp numbers.


Modules
-------


* ``fuzzy_dl_owl2.fuzzydl.query.all_instances_query`` — Retrieves all individuals from a knowledge base that are instances of a specified concept and calculates their respective fuzzy membership degrees.
* ``fuzzy_dl_owl2.fuzzydl.query.bnp_query`` — Encapsulates the logic for determining the best non-fuzzy performance value of a triangular fuzzy number within a standardized query structure.
* ``fuzzy_dl_owl2.fuzzydl.query.classification_query`` — Encapsulates the logic for executing a classification operation on a knowledge base within a query framework.
* ``fuzzy_dl_owl2.fuzzydl.query.instance_query`` — An abstract base class that defines a framework for querying the membership degree of a specific individual relative to a given concept.
* ``fuzzy_dl_owl2.fuzzydl.query.kb_satisfiable_query`` — Determines the satisfiability of a knowledge base by checking for logical consistency through optimization and ABox solving.
* ``fuzzy_dl_owl2.fuzzydl.query.query`` — An abstract base class establishes a standard interface for executing and timing queries against a fuzzy knowledge base.
* ``fuzzy_dl_owl2.fuzzydl.query.related_query`` — An abstract base class defining the structure for queries that evaluate role assertions and relationships between individuals within a fuzzy description logic framework.
* ``fuzzy_dl_owl2.fuzzydl.query.satisfiable_query`` — A base class representing min/max satisfiability queries for fuzzy concepts within a logic framework.
* ``fuzzy_dl_owl2.fuzzydl.query.subsumption_query`` — An abstract base class defines the structure for evaluating fuzzy subsumption relationships between two concepts.


Sub-packages
------------


* ``fuzzy_dl_owl2.fuzzydl.query.defuzzify`` — A framework for converting fuzzy membership degrees into crisp numerical values using Mixed-Integer Linear Programming strategies.
* ``fuzzy_dl_owl2.fuzzydl.query.max`` — A suite of reasoning components that computes maximum degrees of membership, truth, and subsumption within fuzzy ontologies by formulating and solving mixed-integer linear programming problems.
* ``fuzzy_dl_owl2.fuzzydl.query.min`` — A set of optimization mechanisms for fuzzy description logic that determine minimum truth values and lower bounds by transforming logical queries into Mixed-Integer Linear Programming problems.

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

