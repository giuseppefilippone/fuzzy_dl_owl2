fuzzy_dl_owl2.fuzzydl.query.max.max_query
=========================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.query.max.max_query



.. ── LLM-GENERATED DESCRIPTION START ──

A query operation that determines the maximum possible value of a specific expression within a fuzzy knowledge base by transforming the problem into a minimization task.


Description
-----------


The logic revolves around converting a maximization objective into a minimization problem, which is achieved by negating the target expression during initialization. During execution, the process first validates the consistency of the ABox to ensure the ontology is logically sound before proceeding with optimization. To preserve the integrity of the original data, the implementation operates on a cloned instance of the knowledge base rather than modifying the source directly. Error handling is integrated to manage scenarios where the ontology is inconsistent, returning a specific solution state instead of a numerical result, while the workflow includes timing measurements to track the total duration of the reasoning and optimization phases.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.query.max.max_query.MaxQuery


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_query_max_max_query_MaxQuery.png
       :alt: UML Class Diagram for MaxQuery
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **MaxQuery**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_query_max_max_query_MaxQuery.pdf
       :alt: UML Class Diagram for MaxQuery
       :align: center
       :width: 11.2cm
       :class: uml-diagram

       UML Class Diagram for **MaxQuery**

.. py:class:: MaxQuery(expr: fuzzy_dl_owl2.fuzzydl.milp.expression.Expression)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.query.query.Query`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.query.max.max_query.MaxQuery
      :parts: 1
      :private-bases:


   This class represents a query operation designed to determine the maximum possible value of a specific expression while maintaining consistency with the provided knowledge base. During execution, the system first verifies the consistency of the ABox and then performs an optimization on a cloned instance of the knowledge base. Internally, the target expression is negated before being passed to the optimizer, indicating that the underlying mechanism relies on minimization to achieve the maximization goal. If the knowledge base is found to be inconsistent, the query returns a solution indicating this state rather than a numerical result.

   :param obj_expr: The negated expression passed to the solver to find the maximum value.
   :type obj_expr: Expression


   .. py:method:: __str__() -> str

      Returns a string representation of the maximum query object. This representation concatenates the object's expression attribute with the less-than-or-equal-to operator and a trailing space. The resulting string is typically used to display the constraint or condition defined by the query.

      :return: A string representing the object expression followed by the 'less than or equal to' operator.

      :rtype: str



   .. py:method:: preprocess(kb: fuzzy_dl_owl2.fuzzydl.knowledge_base.KnowledgeBase) -> None

      Prepares the `MaxQuery` instance for execution by analyzing or indexing the provided `KnowledgeBase`. This method typically involves initializing internal state, optimizing the query structure, or setting up necessary bindings based on the schema and contents of the knowledge base. Since it returns `None`, the operation is performed in place, modifying the object's internal attributes to facilitate efficient computation of the maximum value during the subsequent evaluation phase.

      :param kb: The knowledge base to be prepared for further processing.
      :type kb: KnowledgeBase



   .. py:method:: solve(kb: fuzzy_dl_owl2.fuzzydl.knowledge_base.KnowledgeBase) -> fuzzy_dl_owl2.fuzzydl.milp.solution.Solution

      Executes the optimization query against the provided KnowledgeBase by first performing ABox reasoning to ensure consistency and materialize inferences. The method creates a clone of the KnowledgeBase to preserve the original state and then runs an optimization routine on this clone using the query's objective expression. It measures and records the total execution time before returning the resulting Solution. If the KnowledgeBase is found to be inconsistent during the initial ABox solving phase, the method catches the exception and returns a Solution object indicating an inconsistent KB.

      :param kb: The knowledge base containing the ontology and data to be solved and optimized.
      :type kb: KnowledgeBase

      :return: A Solution object representing the optimization result of the knowledge base, or a Solution indicating inconsistency if the ontology cannot be solved.

      :rtype: Solution



   .. py:attribute:: obj_expr
      :type:  fuzzy_dl_owl2.fuzzydl.milp.expression.Expression

