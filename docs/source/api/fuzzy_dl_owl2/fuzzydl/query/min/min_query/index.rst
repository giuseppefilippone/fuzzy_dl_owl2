fuzzy_dl_owl2.fuzzydl.query.min.min_query
=========================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.query.min.min_query



.. ── LLM-GENERATED DESCRIPTION START ──

Implements a minimization query designed to find the lowest possible value of a specific objective expression within a fuzzy description logic knowledge base.


Description
-----------


The logic centers on optimizing a mathematical expression provided during initialization to determine the minimum value allowed by the ontology constraints. During execution, the system first resolves the assertional component of the knowledge base to ensure consistency before creating a clone of the data structure. Optimization is performed on this cloned instance to isolate the calculation process, ensuring that the original knowledge base remains unmodified while the solver searches for the optimal solution. Error handling is integrated to manage scenarios where the underlying ontology is inconsistent, returning a specific failure state instead of raising an unhandled exception, while the implementation also tracks the total duration of the solving process to provide performance metrics.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.query.min.min_query.MinQuery


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_query_min_min_query_MinQuery.png
       :alt: UML Class Diagram for MinQuery
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **MinQuery**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_query_min_min_query_MinQuery.pdf
       :alt: UML Class Diagram for MinQuery
       :align: center
       :width: 11.2cm
       :class: uml-diagram

       UML Class Diagram for **MinQuery**

.. py:class:: MinQuery(expr: fuzzy_dl_owl2.fuzzydl.milp.expression.Expression)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.query.query.Query`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.query.min.min_query.MinQuery
      :parts: 1
      :private-bases:


   This class defines a minimization query used to retrieve the smallest possible value of a specific expression subject to the constraints defined in a knowledge base. It operates by accepting an objective expression during initialization and, upon execution, verifying the consistency of the knowledge base before performing an optimization to find the minimum. Users should instantiate this class with the expression they wish to minimize and pass it to a solver, noting that it handles inconsistent knowledge bases by returning a specific failure solution.

   :param obj_expr: The expression representing the objective function to be minimized.
   :type obj_expr: typing.Any


   .. py:method:: __str__() -> str

      Returns a string representation of the minimum query, formatted as a partial expression involving the object's target expression and a greater-than-or-equal-to operator. The output string combines the stored object expression with a question mark and the comparison symbol, providing a human-readable or serialization-friendly version of the query structure. This method has no side effects and does not alter the internal state of the object.

      :return: A string representation of the object, formatted as the object expression followed by a parameter placeholder and the greater-than-or-equal-to operator.

      :rtype: str



   .. py:method:: preprocess(kb: fuzzy_dl_owl2.fuzzydl.knowledge_base.KnowledgeBase) -> None

      Prepares the internal state of the query object based on the provided knowledge base. This method is intended to be overridden by subclasses to perform specific initialization logic, such as validating the knowledge base structure, indexing relevant entities, or constructing intermediate data structures required for efficient query execution. Since it modifies the object's state, it should be invoked prior to executing the main query logic, and subclasses may raise exceptions if the provided knowledge base is incompatible with the specific query requirements.

      :param kb: The knowledge base object to be preprocessed.
      :type kb: KnowledgeBase



   .. py:method:: solve(kb: fuzzy_dl_owl2.fuzzydl.knowledge_base.KnowledgeBase) -> None

      Executes the minimization query by first resolving the ABox of the provided knowledge base and then optimizing a clone of that base against the query's objective expression. The method tracks the total execution time required for these operations. If the knowledge base is found to be inconsistent, the method catches the resulting exception and returns a specific `Solution` object indicating an inconsistent state; otherwise, it returns the `Solution` obtained from the optimization process.

      :param kb: The knowledge base containing the ontology and data to be solved and optimized. The ABox is solved directly on this instance, while optimization is performed on a clone.
      :type kb: KnowledgeBase



   .. py:attribute:: obj_expr

