fuzzy_dl_owl2.fuzzydl.query.max.max_satisfiable_query
=====================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.query.max.max_satisfiable_query



.. ── LLM-GENERATED DESCRIPTION START ──

A query mechanism that calculates the maximal degree of satisfiability for a fuzzy concept within a fuzzy description logic knowledge base, optionally scoped to a specific individual.


Description
-----------


Software defined here extends standard satisfiability checking by formulating a Mixed-Integer Linear Programming (MILP) optimization problem to find the highest possible truth value for a given concept. The implementation supports two modes of operation: general satisfiability, where a new individual is generated to test the concept in isolation, and instance checking, where the query is scoped to a specific existing individual. To ensure the integrity of the original data, execution operates on a cloned version of the knowledge base, applying preprocessing steps such as dynamic blocking for complex logical constructs like universal quantifiers. Core optimization involves constructing an objective expression that maximizes the variable associated with the concept and individual, ultimately returning a solution that represents the optimal satisfaction degree or indicates an inconsistent ontology.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.query.max.max_satisfiable_query.MaxSatisfiableQuery


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_query_max_max_satisfiable_query_MaxSatisfiableQuery.png
       :alt: UML Class Diagram for MaxSatisfiableQuery
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **MaxSatisfiableQuery**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_query_max_max_satisfiable_query_MaxSatisfiableQuery.pdf
       :alt: UML Class Diagram for MaxSatisfiableQuery
       :align: center
       :width: 12.0cm
       :class: uml-diagram

       UML Class Diagram for **MaxSatisfiableQuery**

.. py:class:: MaxSatisfiableQuery(c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept)
              MaxSatisfiableQuery(c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, a: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.query.satisfiable_query.SatisfiableQuery`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.query.max.max_satisfiable_query.MaxSatisfiableQuery
      :parts: 1
      :private-bases:


   This class models a query to determine the maximal degree to which a fuzzy concept is satisfiable within a given knowledge base. It operates by formulating an optimization problem that seeks the highest possible truth value for a given concept, either in general or with respect to a specific individual. To use it, instantiate the object with the target concept and optionally an individual; if the individual is omitted, the query will generate a new one to assess general satisfiability. When executed, the query clones the knowledge base to prevent side effects, preprocesses the concept to handle specific logical constructs like universal quantifiers, and solves a mixed-integer linear program to return the optimal satisfaction degree.


   .. py:method:: __max_sat_query_init_1(c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> None

      Initializes the query instance to evaluate the maximum satisfiability of a specific fuzzy concept. This method delegates the core setup logic to the parent class constructor, passing the provided concept to ensure the query context is correctly established. It prepares the object for subsequent reasoning operations by storing the concept within the inherited query structure.

      :param c: The fuzzy concept to be tested for satisfiability.
      :type c: Concept



   .. py:method:: __max_sat_query_init_2(c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, a: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual) -> None

      Initializes the instance by delegating to the superclass constructor with a specific concept and individual. This setup prepares a satisfiability query designed to evaluate whether the provided individual satisfies the given concept. As a specialized initialization method, it relies on the parent class to handle the actual assignment and validation of the arguments, ensuring the query is correctly configured for subsequent operations.

      :param c: The fuzzy concept to be evaluated for satisfiability.
      :type c: Concept
      :param a: The specific individual instance for which the satisfiability of the concept is being evaluated.
      :type a: Individual



   .. py:method:: __str__() -> str

      Returns a human-readable string representation of the satisfiability query, formatted as a question asking if the stored concept is satisfiable. If the query is constrained by a specific individual, indicated by `self.ind` not being None, the string includes the individual's identifier within brackets. The resulting string always terminates with a less-than-or-equal-to symbol and a space, suggesting it may be used as a prefix for further output or solver interaction.

      :return: Returns a string representation of the satisfiability query, formatted to include the concept and optionally the individual.

      :rtype: str



   .. py:method:: preprocess(kb: fuzzy_dl_owl2.fuzzydl.knowledge_base.KnowledgeBase) -> None

      Prepares the query for optimization by inspecting the conclusion string for specific logical constructs, such as universal quantifiers or negated bounded existential quantifiers. If these patterns are detected, the method enables dynamic blocking on the provided KnowledgeBase to handle the query efficiently. It retrieves the corresponding MILP variable, updates the internal counter for legacy binary variables, and constructs an objective expression designed to maximize the variable's value. Finally, it adds the assertion to the knowledge base and triggers the solving of the current set of assertions, modifying the state of both the query and the knowledge base.

      :param kb: The KnowledgeBase instance managing the MILP model and solver state. It is accessed to retrieve variables, configure blocking strategies, add assertions, and trigger the solving process.
      :type kb: KnowledgeBase



   .. py:method:: solve(kb: fuzzy_dl_owl2.fuzzydl.knowledge_base.KnowledgeBase) -> fuzzy_dl_owl2.fuzzydl.milp.solution.Solution

      Solves the Max-Satisfiability query for the provided Knowledge Base by cloning the input and executing a sequence of logical optimizations. The method determines whether to utilize the ABox based on configuration settings or the presence of a specific individual, initializing a new individual if one is not already defined. It preprocesses the cloned Knowledge Base, resolves the ABox if required, and performs optimization using the instance's objective expression. If the calculated solution value is negative, it is converted to its absolute value before returning. The method handles inconsistent ontologies by returning a specific solution state and updates internal timing metrics as a side effect.

      :param kb: The knowledge base containing the ontology and instance data to be optimized.
      :type kb: KnowledgeBase

      :return: A Solution object representing the result of the optimization process, containing the optimal value (normalized to be non-negative) or a status indicating the knowledge base is inconsistent.

      :rtype: Solution


