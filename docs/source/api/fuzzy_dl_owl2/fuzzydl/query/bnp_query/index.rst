fuzzy_dl_owl2.fuzzydl.query.bnp_query
=====================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.query.bnp_query



.. ── LLM-GENERATED DESCRIPTION START ──

Encapsulates the logic for determining the best non-fuzzy performance value of a triangular fuzzy number within a standardized query structure.


Description
-----------


The software defines a specific query type designed to extract a representative crisp value, known as the best non-fuzzy performance, from a triangular fuzzy number. By extending the base query interface, it integrates into a larger framework while delegating the actual mathematical calculation to the fuzzy number instance itself. Although the solving mechanism accepts a knowledge base argument to maintain consistency with the broader API, the computation is performed independently of the knowledge base contents. The result is encapsulated within a solution object, providing a standardized output format that includes a descriptive label for the calculated metric.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.query.bnp_query.BnpQuery


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_query_bnp_query_BnpQuery.png
       :alt: UML Class Diagram for BnpQuery
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **BnpQuery**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_query_bnp_query_BnpQuery.pdf
       :alt: UML Class Diagram for BnpQuery
       :align: center
       :width: 11.2cm
       :class: uml-diagram

       UML Class Diagram for **BnpQuery**

.. py:class:: BnpQuery(c: fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_number.triangular_fuzzy_number.TriangularFuzzyNumber)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.query.query.Query`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.query.bnp_query.BnpQuery
      :parts: 1
      :private-bases:


   This class encapsulates a query to determine the best non-fuzzy performance (BNP) of a given triangular fuzzy number, which is the specific value within the fuzzy set that possesses the highest degree of membership. It serves as a wrapper around a `TriangularFuzzyNumber` instance, delegating the calculation of this representative crisp value to the number itself. To utilize this functionality, instantiate the object with the desired fuzzy number and invoke the `solve` method, which returns a `Solution` containing the computed BNP. Note that while the solving interface accepts a knowledge base, the current implementation performs the calculation independently of the knowledge base contents.

   :param c: The triangular fuzzy number for which the best non-fuzzy performance is determined.
   :type c: TriangularFuzzyNumber


   .. py:method:: __str__() -> str

      Returns a human-readable string representation of the query object, formatted as a label for the best non-fuzzy performance metric. The string includes the name of the computation obtained from the internal component and ends with an equals sign, suggesting it is designed to precede the actual performance value. This method relies on the `compute_name` method of the internal component and does not modify the object's state.

      :return: A string label representing the best non-fuzzy performance metric for the computed name.

      :rtype: str



   .. py:method:: preprocess(kb: fuzzy_dl_owl2.fuzzydl.knowledge_base.KnowledgeBase) -> None

      Prepares the query instance for execution by performing necessary initialization and validation steps using the provided `KnowledgeBase`. This method typically involves resolving identifiers, checking schema compatibility, or constructing an internal execution plan based on the structure of the knowledge base. It modifies the state of the query object in place and should generally be called once before the main query logic is executed. Subsequent calls may re-initialize the state or be ignored depending on the specific implementation.

      :param kb: The knowledge base instance to be prepared or transformed for subsequent operations.
      :type kb: KnowledgeBase



   .. py:method:: solve(kb: fuzzy_dl_owl2.fuzzydl.knowledge_base.KnowledgeBase) -> fuzzy_dl_owl2.fuzzydl.milp.solution.Solution

      Resolves the query by retrieving the best precise performance metric from the internal solver component. It accepts a KnowledgeBase as input to satisfy the solving interface, and returns the identified non-fuzzy result encapsulated within a Solution object.

      :param kb: The KnowledgeBase instance containing the problem definition or context.
      :type kb: KnowledgeBase

      :return: A Solution object representing the best non-fuzzy performance.

      :rtype: Solution



   .. py:attribute:: c
      :type:  fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_number.triangular_fuzzy_number.TriangularFuzzyNumber

