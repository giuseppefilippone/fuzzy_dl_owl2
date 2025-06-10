fuzzy_dl_owl2.fuzzydl.milp.inequation
=====================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.milp.inequation


Attributes
----------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.milp.inequation.EqualTo
   fuzzy_dl_owl2.fuzzydl.milp.inequation.GreaterThan
   fuzzy_dl_owl2.fuzzydl.milp.inequation.LessThan


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.milp.inequation.Inequation


Module Contents
---------------

.. py:class:: Inequation(exp: fuzzy_dl_owl2.fuzzydl.milp.expression.Expression, i_type: fuzzy_dl_owl2.fuzzydl.util.constants.InequalityType)

   Inequality of the form c + c1 * x1 + c2 * x2 + ...  (>= | <= | =) 0.


   .. py:method:: __eq__(value: Self) -> bool


   .. py:method:: __hash__() -> int


   .. py:method:: __ne__(value: Self) -> bool


   .. py:method:: __repr__() -> str


   .. py:method:: __str__() -> str

      Gets a printable name of the object.



   .. py:method:: clone() -> Self


   .. py:method:: equal_to(exp: fuzzy_dl_owl2.fuzzydl.milp.expression.Expression) -> Self
      :staticmethod:



   .. py:method:: get_constant() -> float


   .. py:method:: get_string_type() -> str

      Gets a string representation of the type.



   .. py:method:: get_terms() -> list[fuzzy_dl_owl2.fuzzydl.milp.term.Term]


   .. py:method:: get_type() -> fuzzy_dl_owl2.fuzzydl.util.constants.InequalityType


   .. py:method:: greater_then(exp: fuzzy_dl_owl2.fuzzydl.milp.expression.Expression) -> Self
      :staticmethod:



   .. py:method:: is_zero() -> bool


   .. py:method:: less_than(exp: fuzzy_dl_owl2.fuzzydl.milp.expression.Expression) -> Self
      :staticmethod:



   .. py:attribute:: expr
      :type:  fuzzy_dl_owl2.fuzzydl.milp.expression.Expression


   .. py:attribute:: type
      :type:  fuzzy_dl_owl2.fuzzydl.util.constants.InequalityType


.. py:data:: EqualTo

.. py:data:: GreaterThan

.. py:data:: LessThan

