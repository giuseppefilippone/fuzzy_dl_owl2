fuzzy_dl_owl2.fuzzydl.degree.degree_numeric
===========================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.degree.degree_numeric


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.degree.degree_numeric.DegreeNumeric


Module Contents
---------------

.. py:class:: DegreeNumeric(numeric: float)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.degree.degree.Degree`


   Helper class that provides a standard way to create an ABC using
   inheritance.


   .. py:method:: __eq__(d: fuzzy_dl_owl2.fuzzydl.degree.degree.Degree) -> bool


   .. py:method:: __str__() -> str


   .. py:method:: add_to_expression(expr: fuzzy_dl_owl2.fuzzydl.milp.expression.Expression) -> fuzzy_dl_owl2.fuzzydl.milp.expression.Expression


   .. py:method:: clone() -> Self


   .. py:method:: create_inequality_with_degree_rhs(expr: fuzzy_dl_owl2.fuzzydl.milp.expression.Expression, inequation_type: fuzzy_dl_owl2.fuzzydl.util.constants.InequalityType) -> fuzzy_dl_owl2.fuzzydl.milp.inequation.Inequation


   .. py:method:: get_degree(value: float) -> Self
      :staticmethod:



   .. py:method:: get_numerical_value() -> float


   .. py:method:: get_one() -> Self
      :staticmethod:



   .. py:method:: is_number_not_one() -> bool


   .. py:method:: is_number_zero() -> bool


   .. py:method:: is_numeric() -> bool


   .. py:method:: multiply_constant(constant: float) -> fuzzy_dl_owl2.fuzzydl.milp.expression.Expression


   .. py:method:: subtract_from_expression(expr: fuzzy_dl_owl2.fuzzydl.milp.expression.Expression) -> fuzzy_dl_owl2.fuzzydl.milp.expression.Expression


   .. py:attribute:: value
      :type:  float


