fuzzy_dl_owl2.fuzzydl.query.min.min_instance_query
==================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.query.min.min_instance_query


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.query.min.min_instance_query.MinInstanceQuery


Module Contents
---------------

.. py:class:: MinInstanceQuery(concept: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, individual: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.query.instance_query.InstanceQuery`


   Greatest lower bound of a concept assertion.


   .. py:method:: __str__() -> str

      Solves the query over a fuzzy KB



   .. py:method:: preprocess(kb: fuzzy_dl_owl2.fuzzydl.knowledge_base.KnowledgeBase) -> None

      Performs some preprocessing steps of the query over a fuzzy KB.



   .. py:method:: solve(kb: fuzzy_dl_owl2.fuzzydl.knowledge_base.KnowledgeBase) -> fuzzy_dl_owl2.fuzzydl.milp.solution.Solution

      Solve the query using given knowledge base



