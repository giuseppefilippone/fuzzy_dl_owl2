fuzzy_dl_owl2.fuzzydl.query.max.max_query
=========================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.query.max.max_query


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.query.max.max_query.MaxQuery


Module Contents
---------------

.. py:class:: MaxQuery(expr: fuzzy_dl_owl2.fuzzydl.milp.expression.Expression)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.query.query.Query`


   Maximize expression query


   .. py:method:: __str__() -> str

      Solves the query over a fuzzy KB



   .. py:method:: preprocess(kb: fuzzy_dl_owl2.fuzzydl.knowledge_base.KnowledgeBase) -> None

      Performs some preprocessing steps of the query over a fuzzy KB.



   .. py:method:: solve(kb: fuzzy_dl_owl2.fuzzydl.knowledge_base.KnowledgeBase) -> fuzzy_dl_owl2.fuzzydl.milp.solution.Solution

      Solve the query using given knowledge base



   .. py:attribute:: obj_expr
      :type:  fuzzy_dl_owl2.fuzzydl.milp.expression.Expression


