fuzzy_dl_owl2.fuzzydl.degree.degree_variable
============================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.degree.degree_variable


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.degree.degree_variable.DegreeVariable


Module Contents
---------------

.. py:class:: DegreeVariable(variable: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.degree.degree.Degree`


   Helper class that provides a standard way to create an ABC using
   inheritance.


   .. py:method:: __eq__(degree: fuzzy_dl_owl2.fuzzydl.degree.degree.Degree) -> bool


   .. py:method:: __str__() -> str


   .. py:method:: add_to_expression(expr: fuzzy_dl_owl2.fuzzydl.milp.expression.Expression) -> fuzzy_dl_owl2.fuzzydl.milp.expression.Expression


   .. py:method:: clone() -> Self


   .. py:method:: create_inequality_with_degree_rhs(expr: fuzzy_dl_owl2.fuzzydl.milp.expression.Expression, inequality_type: fuzzy_dl_owl2.fuzzydl.util.constants.InequalityType) -> fuzzy_dl_owl2.fuzzydl.milp.inequation.Inequation


   .. py:method:: get_degree(value: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable) -> Self
      :staticmethod:



   .. py:method:: get_variable() -> fuzzy_dl_owl2.fuzzydl.milp.variable.Variable


   .. py:method:: is_number_not_one() -> bool


   .. py:method:: is_number_zero() -> bool


   .. py:method:: is_numeric() -> bool


   .. py:method:: multiply_constant(constant: float) -> fuzzy_dl_owl2.fuzzydl.milp.expression.Expression


   .. py:method:: subtract_from_expression(expr: fuzzy_dl_owl2.fuzzydl.milp.expression.Expression) -> fuzzy_dl_owl2.fuzzydl.milp.expression.Expression


   .. py:attribute:: variable
      :type:  fuzzy_dl_owl2.fuzzydl.milp.variable.Variable


