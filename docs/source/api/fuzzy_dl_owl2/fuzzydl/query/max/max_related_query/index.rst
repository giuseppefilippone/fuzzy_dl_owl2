fuzzy_dl_owl2.fuzzydl.query.max.max_related_query
=================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.query.max.max_related_query



.. ── LLM-GENERATED DESCRIPTION START ──

A query type that computes the maximum degree of truth to which two individuals are related through a given role in a fuzzy description-logic knowledge base.


Description
-----------


``MaxRelatedQuery`` extends the shared ``RelatedQuery`` interface to answer questions of the form "is individual A related to individual B through role R, and to what maximal degree?" against a fuzzy ontology. Rather than evaluating the assertion directly, it compiles the question into a mixed-integer linear programming problem: during preprocessing, the role assertion is recast as a has-value concept attached to the first individual, the MILP variable representing that assertion's degree is retrieved and asserted into the knowledge base, and the objective expression is built from that variable with a negative coefficient so that the solver's minimisation effectively maximises the relationship's degree of truth. The solving routine deliberately clones the knowledge base before injecting these query-specific constraints, which keeps the original ontology untouched and makes the query safe to run repeatedly or alongside other queries; it also records execution time and, if resolving the ABox reveals an inconsistency, catches the exception and returns a dedicated inconsistent-knowledge-base solution instead of propagating the failure. The overall design keeps the query logic thin, delegating the heavy lifting — assertion solving, MILP optimisation, and consistency checking — to the knowledge base and its solver, while the query itself contributes only the problem formulation, the non-destructive cloning strategy, and graceful handling of inconsistent input. For presentation purposes, the query renders itself as a natural-language question about the two individuals and the role connecting them.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.query.max.max_related_query.MaxRelatedQuery


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_query_max_max_related_query_MaxRelatedQuery.png
       :alt: UML Class Diagram for MaxRelatedQuery
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **MaxRelatedQuery**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_query_max_max_related_query_MaxRelatedQuery.pdf
       :alt: UML Class Diagram for MaxRelatedQuery
       :align: center
       :width: 11.7cm
       :class: uml-diagram

       UML Class Diagram for **MaxRelatedQuery**

.. py:class:: MaxRelatedQuery(a: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, b: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, role_name: str)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.query.related_query.RelatedQuery`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.query.max.max_related_query.MaxRelatedQuery
      :parts: 1
      :private-bases:


   This class models a query designed to determine the maximum degree of truth for a specific relationship between two individuals within a fuzzy knowledge base. It operates by formulating an optimization problem where the goal is to maximize the membership degree of the assertion that the first individual is related to the second individual via a specified role. To use this class, instantiate it with the two individuals involved and the name of the role, then invoke the solve method with a knowledge base instance to retrieve the optimal solution. The implementation handles potential ontology inconsistencies gracefully by returning a specific solution state.

   :param ind1: The first individual in the role assertion, representing the subject of the relationship.
   :type ind1: Individual
   :param ind2: The second individual in the role assertion, representing the target of the relationship.
   :type ind2: Individual
   :param role: The name of the role through which the two individuals are related.
   :type role: str


   .. py:method:: __str__() -> str

      Returns a human-readable string representation of the query object, formatted as a question regarding the relationship between two individuals. The method constructs the string by interpolating the first individual, the second individual, and the relationship role into a template that asks if the first is related to the second through the specified role. The output string concludes with a prompt indicator ('<= ') and relies on the standard string conversion of the object's attributes, ensuring that the method does not modify the object's state.

      :return: A string representation of the relationship query, formatted as a question asking if the first individual is related to the second through the specified role.

      :rtype: str



   .. py:method:: preprocess(kb: fuzzy_dl_owl2.fuzzydl.knowledge_base.KnowledgeBase) -> None

      Prepares the query for execution by translating a specific relationship constraint into a Mixed-Integer Linear Programming (MILP) formulation within the provided Knowledge Base. It constructs a `HasValueConcept` representing the restriction that an individual must have a specific value for a given role, retrieves the corresponding MILP variable, and asserts this relationship with a degree derived from that variable. As a side effect, this method increments the knowledge base's counter for legacy variables, initializes the instance's objective expression to optimize the relationship's degree, and triggers the solving of all current assertions to update the system state.

      :param kb: The knowledge base context used to access the MILP model, add assertions, update variable counters, and trigger the solver.
      :type kb: KnowledgeBase



   .. py:method:: solve(kb: fuzzy_dl_owl2.fuzzydl.knowledge_base.KnowledgeBase) -> fuzzy_dl_owl2.fuzzydl.milp.solution.Solution

      Executes the optimization query by first resolving the ABox of the provided Knowledge Base to ensure consistency. Upon successful resolution, the method clones the Knowledge Base to preserve the original state, applies necessary preprocessing, and runs an optimization routine using the defined objective expression. The process includes tracking the total execution time. If the Knowledge Base is determined to be inconsistent during the initial resolution step, the method intercepts the exception and returns a Solution object specifically marked as inconsistent.

      :param kb: The knowledge base containing the ontology and data to be solved and optimized.
      :type kb: KnowledgeBase

      :return: The Solution object resulting from the optimization process, or a specific solution state indicating the knowledge base is inconsistent.

      :rtype: Solution



   .. py:attribute:: ind1
      :type:  fuzzy_dl_owl2.fuzzydl.individual.individual.Individual


   .. py:attribute:: ind2
      :type:  fuzzy_dl_owl2.fuzzydl.individual.individual.Individual


   .. py:attribute:: role
      :type:  str

