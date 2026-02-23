fuzzy_dl_owl2.fuzzydl.query.min.min_instance_query
==================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.query.min.min_instance_query



.. ── LLM-GENERATED DESCRIPTION START ──

Calculates the greatest lower bound of membership for a specific individual relative to a given concept by transforming the logical query into a Mixed-Integer Linear Programming (MILP) optimization problem.


Description
-----------


The software implements a mechanism to determine the minimum truth value indicating how strongly a specific individual belongs to a particular concept within a fuzzy description logic framework. By extending the base instance query functionality, it transforms the logical problem into a mathematical optimization task, specifically utilizing a semi-continuous variable within a Mixed-Integer Linear Programming (MILP) solver to represent the degree of membership. During the preprocessing phase, the system introduces a linear constraint that links the negation of the target concept to this variable, ensuring the optimization process correctly minimizes the membership degree while respecting the ontology's axioms. To maintain data integrity and prevent unintended side effects, the execution process operates on a cloned version of the provided knowledge base, applying dynamic blocking strategies when existential quantifiers are detected and gracefully handling potential inconsistencies in the ontology.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.query.min.min_instance_query.MinInstanceQuery


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_query_min_min_instance_query_MinInstanceQuery.png
       :alt: UML Class Diagram for MinInstanceQuery
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **MinInstanceQuery**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_query_min_min_instance_query_MinInstanceQuery.pdf
       :alt: UML Class Diagram for MinInstanceQuery
       :align: center
       :width: 11.4cm
       :class: uml-diagram

       UML Class Diagram for **MinInstanceQuery**

.. py:class:: MinInstanceQuery(concept: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, individual: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.query.instance_query.InstanceQuery`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.query.min.min_instance_query.MinInstanceQuery
      :parts: 1
      :private-bases:


   This class models a query designed to retrieve the greatest lower bound of the degree of membership for a specific individual relative to a given concept. It functions by transforming the logical query into an optimization problem, specifically utilizing a semi-continuous variable to represent the degree of membership. To execute the query, the user must provide a target concept and an individual; the `solve` method then clones the current knowledge base to prevent side effects, applies necessary constraints, and performs an optimization to calculate the result. The implementation includes specific handling for existential restrictions and manages inconsistent ontology states by returning a designated solution type.


   .. py:method:: __str__() -> str

      Returns a human-readable string representation of the query object, formatted to ask whether the individual stored in `self.ind` is an instance of the concept stored in `self.conc`, followed by a threshold comparison indicator. This method is primarily used for debugging or logging purposes to visualize the specific parameters of the query in a structured format.

      :return: A human-readable string representation of the object, formatted as a query regarding whether `ind` is an instance of `conc`.

      :rtype: str



   .. py:method:: preprocess(kb: fuzzy_dl_owl2.fuzzydl.knowledge_base.KnowledgeBase) -> None

      Prepares the minimum instance query for solving by introducing a new semi-continuous variable into the Knowledge Base's MILP solver and setting it as the objective to be minimized. The method inspects the query's conclusion for existential quantifiers, triggering dynamic blocking on the Knowledge Base if specific patterns are detected. It then encodes the logical structure of the query by adding an assertion that links the negation of the conclusion to the new variable via a linear constraint, specifically enforcing that the negated conclusion is greater than or equal to one minus the variable. This process modifies the Knowledge Base state and immediately triggers a solving step for the accumulated assertions.

      :param kb: The knowledge base instance used to manage variables, assertions, and solver state.
      :type kb: KnowledgeBase



   .. py:method:: solve(kb: fuzzy_dl_owl2.fuzzydl.knowledge_base.KnowledgeBase) -> fuzzy_dl_owl2.fuzzydl.milp.solution.Solution

      Orchestrates the resolution of the query by performing ABox reasoning, preprocessing, and optimization on the provided Knowledge Base. The method initiates timing, solves the ABox of the input KB, and then operates on a cloned version to apply preprocessing steps and optimize against the objective expression. It returns the resulting solution after calculating the total execution time. In the event that the ontology is inconsistent, the method catches the exception and returns a Solution object marked as inconsistent rather than propagating the error.

      :param kb: The knowledge base containing the ontology and data to be solved and optimized.
      :type kb: KnowledgeBase

      :return: A Solution object representing the result of optimizing the preprocessed knowledge base. If the knowledge base is inconsistent, returns a Solution indicating an inconsistent state.

      :rtype: Solution


