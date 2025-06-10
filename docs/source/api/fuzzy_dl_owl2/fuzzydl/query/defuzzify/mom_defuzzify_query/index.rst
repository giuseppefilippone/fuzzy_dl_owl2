fuzzy_dl_owl2.fuzzydl.query.defuzzify.mom_defuzzify_query
=========================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.query.defuzzify.mom_defuzzify_query


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.query.defuzzify.mom_defuzzify_query.MomDefuzzifyQuery


Module Contents
---------------

.. py:class:: MomDefuzzifyQuery(c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, ind: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, feature_name: str)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.query.defuzzify.defuzzify_query.DefuzzifyQuery`


   Middle of maxima defuzzification query.


   .. py:method:: __str__() -> str

      Solves the query over a fuzzy KB



   .. py:method:: get_obj_expression(variable: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable) -> fuzzy_dl_owl2.fuzzydl.milp.expression.Expression


   .. py:method:: preprocess(kb: fuzzy_dl_owl2.fuzzydl.knowledge_base.KnowledgeBase) -> None

      Performs some preprocessing steps of the query over a fuzzy KB.



   .. py:method:: solve(kb: fuzzy_dl_owl2.fuzzydl.knowledge_base.KnowledgeBase) -> fuzzy_dl_owl2.fuzzydl.milp.solution.Solution

      Solve the query using given knowledge base



