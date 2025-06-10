fuzzy_dl_owl2.fuzzydl.query.min.min_query
=========================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.query.min.min_query


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.query.min.min_query.MinQuery


Module Contents
---------------

.. py:class:: MinQuery(expr: fuzzy_dl_owl2.fuzzydl.milp.expression.Expression)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.query.query.Query`


   Minimize expression query.


   .. py:method:: __str__() -> str

      Solves the query over a fuzzy KB



   .. py:method:: preprocess(kb: fuzzy_dl_owl2.fuzzydl.knowledge_base.KnowledgeBase) -> None

      Performs some preprocessing steps of the query over a fuzzy KB.



   .. py:method:: solve(kb: fuzzy_dl_owl2.fuzzydl.knowledge_base.KnowledgeBase) -> None

      Solve the query using given knowledge base



   .. py:attribute:: obj_expr


