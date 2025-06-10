fuzzy_dl_owl2.fuzzydl.query.bnp_query
=====================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.query.bnp_query


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.query.bnp_query.BnpQuery


Module Contents
---------------

.. py:class:: BnpQuery(c: fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_number.triangular_fuzzy_number.TriangularFuzzyNumber)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.query.query.Query`


   Helper class that provides a standard way to create an ABC using
   inheritance.


   .. py:method:: __str__() -> str

      Solves the query over a fuzzy KB



   .. py:method:: preprocess(kb: fuzzy_dl_owl2.fuzzydl.knowledge_base.KnowledgeBase) -> None

      Performs some preprocessing steps of the query over a fuzzy KB.



   .. py:method:: solve(kb: fuzzy_dl_owl2.fuzzydl.knowledge_base.KnowledgeBase) -> fuzzy_dl_owl2.fuzzydl.milp.solution.Solution

      Solve the query using given knowledge base



   .. py:attribute:: c
      :type:  fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_number.triangular_fuzzy_number.TriangularFuzzyNumber


