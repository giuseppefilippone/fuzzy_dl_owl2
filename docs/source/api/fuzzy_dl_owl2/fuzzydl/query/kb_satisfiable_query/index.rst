fuzzy_dl_owl2.fuzzydl.query.kb_satisfiable_query
================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.query.kb_satisfiable_query


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.query.kb_satisfiable_query.KbSatisfiableQuery


Module Contents
---------------

.. py:class:: KbSatisfiableQuery

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.query.query.Query`


   Knowledge base satisfiability degree


   .. py:method:: __str__() -> str

      Solves the query over a fuzzy KB



   .. py:method:: is_consistent_kb(kb: fuzzy_dl_owl2.fuzzydl.knowledge_base.KnowledgeBase) -> bool


   .. py:method:: preprocess(kb: fuzzy_dl_owl2.fuzzydl.knowledge_base.KnowledgeBase) -> None

      Performs some preprocessing steps of the query over a fuzzy KB.



   .. py:method:: solve(kb: fuzzy_dl_owl2.fuzzydl.knowledge_base.KnowledgeBase) -> fuzzy_dl_owl2.fuzzydl.milp.solution.Solution

      Solve the query using given knowledge base



