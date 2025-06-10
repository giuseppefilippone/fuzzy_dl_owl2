fuzzy_dl_owl2.fuzzydl.query.all_instances_query
===============================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.query.all_instances_query


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.query.all_instances_query.AllInstancesQuery


Module Contents
---------------

.. py:class:: AllInstancesQuery(concept: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.query.query.Query`


   Min instance query for every individual of a knowledge base.


   .. py:method:: __str__() -> str

      Solves the query over a fuzzy KB



   .. py:method:: get_degrees() -> list[float]


   .. py:method:: get_individuals() -> list[fuzzy_dl_owl2.fuzzydl.individual.individual.Individual]


   .. py:method:: preprocess(kb: fuzzy_dl_owl2.fuzzydl.knowledge_base.KnowledgeBase) -> None

      Performs some preprocessing steps of the query over a fuzzy KB.



   .. py:method:: solve(kb: fuzzy_dl_owl2.fuzzydl.knowledge_base.KnowledgeBase) -> fuzzy_dl_owl2.fuzzydl.milp.solution.Solution

      Solve the query using given knowledge base



   .. py:method:: solve_new(kb: fuzzy_dl_owl2.fuzzydl.knowledge_base.KnowledgeBase) -> fuzzy_dl_owl2.fuzzydl.milp.solution.Solution

      Specific algorithm to solve the instance retrieval.



   .. py:attribute:: conc


   .. py:attribute:: degrees
      :type:  list[float]
      :value: []



   .. py:attribute:: individuals
      :type:  list[fuzzy_dl_owl2.fuzzydl.individual.individual.Individual]
      :value: []



   .. py:attribute:: name
      :value: 'Instances of Uninferable?'



