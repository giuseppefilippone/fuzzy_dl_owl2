fuzzy_dl_owl2.fuzzydl.query.classification_query
================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.query.classification_query


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.query.classification_query.ClassificationQuery


Module Contents
---------------

.. py:class:: ClassificationQuery

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.query.query.Query`


   Helper class that provides a standard way to create an ABC using
   inheritance.


   .. py:method:: __str__() -> str

      Solves the query over a fuzzy KB



   .. py:method:: preprocess(kb: fuzzy_dl_owl2.fuzzydl.knowledge_base.KnowledgeBase) -> None

      Performs some preprocessing steps of the query over a fuzzy KB.



   .. py:method:: solve(kb: fuzzy_dl_owl2.fuzzydl.knowledge_base.KnowledgeBase) -> fuzzy_dl_owl2.fuzzydl.milp.solution.Solution

      Solve the query using given knowledge base



