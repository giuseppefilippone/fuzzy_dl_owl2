fuzzy_dl_owl2.fuzzydl.milp.expression
=====================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.milp.expression


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.milp.expression.Expression


Module Contents
---------------

.. py:class:: Expression(constant: fuzzy_dl_owl2.fuzzydl.util.constants.NUMBER)
              Expression(constant: fuzzy_dl_owl2.fuzzydl.util.constants.NUMBER, *terms: fuzzy_dl_owl2.fuzzydl.milp.term.Term)
              Expression(*terms: fuzzy_dl_owl2.fuzzydl.milp.term.Term)
              Expression(expr: Self)
              Expression(v: Union[list[fuzzy_dl_owl2.fuzzydl.milp.variable.Variable], set[fuzzy_dl_owl2.fuzzydl.milp.variable.Variable]])

   Linear expression of the form c + c1 * x1 + c2 * x2 + ... + cN * xN


   .. py:method:: __add__(value: Union[int, float, Self, fuzzy_dl_owl2.fuzzydl.milp.term.Term]) -> Self


   .. py:method:: __eq__(value: Self) -> bool


   .. py:method:: __hash__() -> int


   .. py:method:: __mul__(scalar: fuzzy_dl_owl2.fuzzydl.util.constants.NUMBER) -> Self


   .. py:method:: __ne__(value: Self) -> bool


   .. py:method:: __neg__() -> Self


   .. py:method:: __radd__(scalar: fuzzy_dl_owl2.fuzzydl.util.constants.NUMBER) -> Self


   .. py:method:: __repr__() -> str


   .. py:method:: __rmul__(scalar: fuzzy_dl_owl2.fuzzydl.util.constants.NUMBER) -> Self


   .. py:method:: __rsub__(scalar: fuzzy_dl_owl2.fuzzydl.util.constants.NUMBER) -> Self


   .. py:method:: __str__() -> str

      Gets a printable name of the expression.



   .. py:method:: __sub__(expr: Union[int, float, Self, fuzzy_dl_owl2.fuzzydl.milp.term.Term]) -> Self


   .. py:method:: __truediv__(scalar: fuzzy_dl_owl2.fuzzydl.util.constants.NUMBER) -> Self


   .. py:method:: add_constant(expr: Self, constant: fuzzy_dl_owl2.fuzzydl.util.constants.NUMBER) -> Self
      :staticmethod:


      Adds a constant to an expression.



   .. py:method:: add_expressions(expr1: Self, expr2: Self) -> Self
      :staticmethod:


      Adds two expressions.



   .. py:method:: add_term(term: fuzzy_dl_owl2.fuzzydl.milp.term.Term) -> None

      Adds a term to an expression.



   .. py:method:: add_term_(exp: Self, term: fuzzy_dl_owl2.fuzzydl.milp.term.Term) -> Self
      :staticmethod:


      Adds a term to an expression.



   .. py:method:: clone() -> Self


   .. py:method:: get_constant() -> fuzzy_dl_owl2.fuzzydl.util.constants.NUMBER


   .. py:method:: get_constant_term(var: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable) -> fuzzy_dl_owl2.fuzzydl.util.constants.NUMBER

      Given a variable, gets its coefficient in the expression.



   .. py:method:: get_terms() -> list[fuzzy_dl_owl2.fuzzydl.milp.term.Term]


   .. py:method:: increment_constant() -> None

      Increments the constant in one.



   .. py:method:: multiply_constant(expr: Self, constant: fuzzy_dl_owl2.fuzzydl.util.constants.NUMBER) -> Self
      :staticmethod:


      Multiplies a constant and an expression.



   .. py:method:: negate_expression(expr: Self) -> Self
      :staticmethod:


      Changes the sign of all the elements of an expression.



   .. py:method:: set_constant(constant: fuzzy_dl_owl2.fuzzydl.util.constants.NUMBER) -> None


   .. py:method:: subtract_expressions(expr1: Self, expr2: Self) -> Self
      :staticmethod:


      Substracts two expressions.



