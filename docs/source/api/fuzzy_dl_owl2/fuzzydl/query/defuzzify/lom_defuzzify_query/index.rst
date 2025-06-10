fuzzy_dl_owl2.fuzzydl.query.defuzzify.lom_defuzzify_query
=========================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.query.defuzzify.lom_defuzzify_query


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.query.defuzzify.lom_defuzzify_query.LomDefuzzifyQuery


Module Contents
---------------

.. py:class:: LomDefuzzifyQuery(c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, ind: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, feature_name: str)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.query.defuzzify.defuzzify_query.DefuzzifyQuery`


   Largest of maxima defuzzification query


   .. py:method:: __str__() -> str

      Solves the query over a fuzzy KB



   .. py:method:: get_obj_expression(variable: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable) -> fuzzy_dl_owl2.fuzzydl.milp.expression.Expression


