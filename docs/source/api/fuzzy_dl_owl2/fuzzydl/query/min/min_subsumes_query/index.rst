fuzzy_dl_owl2.fuzzydl.query.min.min_subsumes_query
==================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.query.min.min_subsumes_query


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.query.min.min_subsumes_query.MinSubsumesQuery


Module Contents
---------------

.. py:class:: MinSubsumesQuery(c1: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, c2: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, type_: fuzzy_dl_owl2.fuzzydl.util.constants.LogicOperatorType)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.query.subsumption_query.SubsumptionQuery`


   Minimize subsumption query.


   .. py:method:: __str__() -> str

      Solves the query over a fuzzy KB



   .. py:method:: preprocess(kb: fuzzy_dl_owl2.fuzzydl.knowledge_base.KnowledgeBase) -> None

      Performs some preprocessing steps of the query over a fuzzy KB.



   .. py:method:: solve(kb: fuzzy_dl_owl2.fuzzydl.knowledge_base.KnowledgeBase) -> fuzzy_dl_owl2.fuzzydl.milp.solution.Solution

      Solve the query using given knowledge base



