fuzzy_dl_owl2.fuzzydl.query.max.max_related_query
=================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.query.max.max_related_query


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.query.max.max_related_query.MaxRelatedQuery


Module Contents
---------------

.. py:class:: MaxRelatedQuery(a: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, b: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, role_name: str)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.query.related_query.RelatedQuery`


   Lowest upper bound of a role assertion (ind1, ind2, role)


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


