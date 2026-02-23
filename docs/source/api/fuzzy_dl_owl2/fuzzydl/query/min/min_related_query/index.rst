fuzzy_dl_owl2.fuzzydl.query.min.min_related_query
=================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.query.min.min_related_query



.. ── LLM-GENERATED DESCRIPTION START ──

A query mechanism that determines the minimum membership degree of a role relationship between two individuals within a fuzzy ontology using mixed-integer linear programming.


Description
-----------


The software implements a specific type of fuzzy description logic query designed to compute the minimum truth value associated with a role assertion between two distinct individuals. By leveraging mixed-integer linear programming, the logic constructs a mathematical model where the objective is to minimize the degree to which the first individual participates in a specific role with the second individual. To ensure the integrity of the original data, the process operates on a cloned version of the provided knowledge base, thereby preventing unintended side effects during the optimization phase. The implementation dynamically generates necessary constraints and assertions, such as those involving negation and existential restrictions, before invoking the solver to derive the final result. Error handling mechanisms are integrated to gracefully manage scenarios where the underlying ontology is found to be inconsistent, returning a specific status rather than failing abruptly.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.query.min.min_related_query.MinRelatedQuery


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_query_min_min_related_query_MinRelatedQuery.png
       :alt: UML Class Diagram for MinRelatedQuery
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **MinRelatedQuery**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_query_min_min_related_query_MinRelatedQuery.pdf
       :alt: UML Class Diagram for MinRelatedQuery
       :align: center
       :width: 11.7cm
       :class: uml-diagram

       UML Class Diagram for **MinRelatedQuery**

.. py:class:: MinRelatedQuery(a: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, b: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, role_name: str)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.query.related_query.RelatedQuery`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.query.min.min_related_query.MinRelatedQuery
      :parts: 1
      :private-bases:


   Represents a query that retrieves the minimum degree to which two individuals are related through a specific role within a knowledge base. To use this class, instantiate it with the two individuals and the role name, then invoke the solve method with a KnowledgeBase instance. Internally, the query clones the knowledge base to avoid side effects, constructs a corresponding concept expression, and utilizes mixed-integer linear programming to optimize and determine the minimum membership degree of the role assertion. The result is encapsulated in a Solution object, which accounts for potential inconsistencies in the ontology.

   :param ind1: The first individual involved in the role assertion, representing the subject of the relationship.
   :type ind1: Individual
   :param ind2: The target individual in the role assertion, corresponding to 'b' in the query (min-related? a b R).
   :type ind2: Individual
   :param role: The name of the role or relationship type connecting the two individuals.
   :type role: str


   .. py:method:: __str__() -> str

      Returns a human-readable string representation of the query object. The output is formatted as a question asking whether the first individual is related to the second individual through a specific role, followed by a ' >= ' operator. This method is primarily used for debugging or displaying the current state of the query parameters.

      :return: A string representation of the object, formatted as a question asking if `ind1` is related to `ind2` through `role`.

      :rtype: str



   .. py:method:: preprocess(kb: fuzzy_dl_owl2.fuzzydl.knowledge_base.KnowledgeBase) -> None

      Prepares the query for execution by constructing a `HasValueConcept` based on the query's role and secondary individual, and integrating it into the provided `KnowledgeBase`. It retrieves a MILP variable representing the degree of membership of the primary individual in this concept and sets the query's objective expression to target this variable. The method adds assertions to the knowledge base to link the individual to both the concept and its negation, enforcing a constraint where the degree of the negation is derived from the degree of the concept. As a side effect, it increments the knowledge base's counter for legacy variables and enables dynamic blocking if the concept involves existential restrictions. Finally, it triggers the solving of all added assertions to update the solver's state.

      :param kb: The knowledge base instance containing the MILP model, used to retrieve variables, add assertions, and trigger solving.
      :type kb: KnowledgeBase



   .. py:method:: solve(kb: fuzzy_dl_owl2.fuzzydl.knowledge_base.KnowledgeBase) -> fuzzy_dl_owl2.fuzzydl.milp.solution.Solution

      Executes the optimization process for the query using the provided Knowledge Base. The method initiates timing, modifies the input Knowledge Base by incrementing its binary variable counter, and resolves the ABox. A clone of the Knowledge Base is then preprocessed and optimized according to the query's objective expression to generate a solution. If the ontology is found to be inconsistent during this process, the method catches the exception and returns a solution indicating inconsistency rather than raising an error.

      :param kb: The knowledge base containing the ontology and constraints to be solved and optimized.
      :type kb: KnowledgeBase

      :return: The Solution object resulting from the optimization of the knowledge base, or a specific status indicating the ontology is inconsistent.

      :rtype: Solution



   .. py:attribute:: ind1
      :type:  fuzzy_dl_owl2.fuzzydl.individual.individual.Individual


   .. py:attribute:: ind2
      :type:  fuzzy_dl_owl2.fuzzydl.individual.individual.Individual


   .. py:attribute:: role
      :type:  str

