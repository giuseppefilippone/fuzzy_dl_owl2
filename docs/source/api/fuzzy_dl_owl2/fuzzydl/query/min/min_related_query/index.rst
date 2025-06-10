fuzzy_dl_owl2.fuzzydl.query.min.min_related_query
=================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.query.min.min_related_query


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.query.min.min_related_query.MinRelatedQuery


Module Contents
---------------

.. py:class:: MinRelatedQuery(a: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, b: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, role_name: str)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.query.related_query.RelatedQuery`


   Greatest lower bound of a role assertion (ind1, ind2, role).


   .. py:method:: __str__() -> str

      Solves the query over a fuzzy KB



   .. py:method:: preprocess(kb: fuzzy_dl_owl2.fuzzydl.knowledge_base.KnowledgeBase) -> None

      Performs some preprocessing steps of the query over a fuzzy KB.



   .. py:method:: solve(kb: fuzzy_dl_owl2.fuzzydl.knowledge_base.KnowledgeBase) -> fuzzy_dl_owl2.fuzzydl.milp.solution.Solution

      Solve the query using given knowledge base



   .. py:attribute:: ind1
      :type:  fuzzy_dl_owl2.fuzzydl.individual.individual.Individual


   .. py:attribute:: ind2
      :type:  fuzzy_dl_owl2.fuzzydl.individual.individual.Individual


   .. py:attribute:: role
      :type:  str


