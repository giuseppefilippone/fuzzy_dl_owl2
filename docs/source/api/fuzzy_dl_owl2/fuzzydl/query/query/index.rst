fuzzy_dl_owl2.fuzzydl.query.query
=================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.query.query


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.query.query.Query


Module Contents
---------------

.. py:class:: Query

   Bases: :py:obj:`abc.ABC`


   Helper class that provides a standard way to create an ABC using
   inheritance.


   .. py:method:: __str__() -> str
      :abstractmethod:


      Solves the query over a fuzzy KB



   .. py:method:: get_total_time() -> float


   .. py:method:: preprocess(knowledge_base: fuzzy_dl_owl2.fuzzydl.knowledge_base.KnowledgeBase) -> None
      :abstractmethod:


      Performs some preprocessing steps of the query over a fuzzy KB.



   .. py:method:: set_initial_time() -> None


   .. py:method:: set_total_time() -> None


   .. py:method:: solve(knowledge_base: fuzzy_dl_owl2.fuzzydl.knowledge_base.KnowledgeBase) -> fuzzy_dl_owl2.fuzzydl.milp.solution.Solution
      :abstractmethod:


      Solve the query using given knowledge base



   .. py:attribute:: initial_time
      :type:  int
      :value: 0



   .. py:attribute:: total_time
      :type:  int
      :value: 0



