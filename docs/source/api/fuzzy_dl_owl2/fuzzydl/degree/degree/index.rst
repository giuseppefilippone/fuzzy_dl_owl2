fuzzy_dl_owl2.fuzzydl.degree.degree
===================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.degree.degree


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.degree.degree.Degree


Module Contents
---------------

.. py:class:: Degree

   Bases: :py:obj:`abc.ABC`


   Helper class that provides a standard way to create an ABC using
   inheritance.


   .. py:method:: __eq__(degree: Self) -> bool
      :abstractmethod:



   .. py:method:: __ne__(value: Self) -> bool


   .. py:method:: __repr__() -> str


   .. py:method:: __str__() -> str
      :abstractmethod:



   .. py:method:: add_to_expression(expression: fuzzy_dl_owl2.fuzzydl.milp.expression.Expression) -> fuzzy_dl_owl2.fuzzydl.milp.expression.Expression
      :abstractmethod:



   .. py:method:: clone() -> Self
      :abstractmethod:



   .. py:method:: create_inequality_with_degree_rhs(expression: fuzzy_dl_owl2.fuzzydl.milp.expression.Expression, inequation_type: fuzzy_dl_owl2.fuzzydl.util.constants.InequalityType) -> fuzzy_dl_owl2.fuzzydl.milp.inequation.Inequation
      :abstractmethod:



   .. py:method:: get_degree(value) -> Self
      :staticmethod:

      :abstractmethod:



   .. py:method:: is_number_not_one() -> bool
      :abstractmethod:



   .. py:method:: is_number_zero() -> bool
      :abstractmethod:



   .. py:method:: is_numeric() -> bool
      :abstractmethod:



   .. py:method:: multiply_constant(double: float) -> fuzzy_dl_owl2.fuzzydl.milp.expression.Expression
      :abstractmethod:



   .. py:method:: subtract_from_expression(expression: fuzzy_dl_owl2.fuzzydl.milp.expression.Expression) -> fuzzy_dl_owl2.fuzzydl.milp.expression.Expression
      :abstractmethod:



