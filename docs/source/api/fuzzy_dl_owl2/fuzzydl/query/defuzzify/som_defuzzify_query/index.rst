fuzzy_dl_owl2.fuzzydl.query.defuzzify.som_defuzzify_query
=========================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.query.defuzzify.som_defuzzify_query


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.query.defuzzify.som_defuzzify_query.SomDefuzzifyQuery


Module Contents
---------------

.. py:class:: SomDefuzzifyQuery(c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, ind: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, f_name: str)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.query.defuzzify.defuzzify_query.DefuzzifyQuery`


   Smallest of maxima defuzzification query.


   .. py:method:: __str__() -> str

      Solves the query over a fuzzy KB



   .. py:method:: get_obj_expression(q: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable) -> fuzzy_dl_owl2.fuzzydl.milp.expression.Expression


