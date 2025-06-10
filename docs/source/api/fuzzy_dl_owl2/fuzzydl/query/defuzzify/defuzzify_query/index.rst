fuzzy_dl_owl2.fuzzydl.query.defuzzify.defuzzify_query
=====================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.query.defuzzify.defuzzify_query


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.query.defuzzify.defuzzify_query.DefuzzifyQuery


Module Contents
---------------

.. py:class:: DefuzzifyQuery(c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, ind: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, feature_name: str)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.query.query.Query`


   Helper class that provides a standard way to create an ABC using
   inheritance.


   .. py:method:: get_obj_expression(variable: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable) -> fuzzy_dl_owl2.fuzzydl.milp.expression.Expression
      :abstractmethod:



   .. py:method:: preprocess(kb: fuzzy_dl_owl2.fuzzydl.knowledge_base.KnowledgeBase) -> None

      Performs some preprocessing steps of the query over a fuzzy KB.



   .. py:method:: solve(kb: fuzzy_dl_owl2.fuzzydl.knowledge_base.KnowledgeBase) -> Optional[fuzzy_dl_owl2.fuzzydl.milp.solution.Solution]

      Solve the query using given knowledge base



   .. py:attribute:: a
      :type:  fuzzy_dl_owl2.fuzzydl.individual.individual.Individual


   .. py:attribute:: conc
      :type:  fuzzy_dl_owl2.fuzzydl.concept.concept.Concept


   .. py:attribute:: f_name
      :type:  str


   .. py:attribute:: obj_expr
      :type:  fuzzy_dl_owl2.fuzzydl.milp.expression.Expression
      :value: None



