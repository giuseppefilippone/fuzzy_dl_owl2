fuzzy_dl_owl2.fuzzydl.milp.term
===============================

.. py:module:: fuzzy_dl_owl2.fuzzydl.milp.term


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.milp.term.Term


Module Contents
---------------

.. py:class:: Term(coeff: float, var: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable)
              Term(var: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable)

   .. py:method:: __add__(term: Self) -> Self


   .. py:method:: __eq__(term: Self) -> bool


   .. py:method:: __hash__() -> int


   .. py:method:: __mul__(scalar: float) -> Self


   .. py:method:: __ne__(term: Self) -> bool


   .. py:method:: __neg__() -> Self


   .. py:method:: __repr__() -> str


   .. py:method:: __rmul__(scalar: float) -> Self


   .. py:method:: __str__() -> str


   .. py:method:: __sub__(term: Self) -> Self


   .. py:method:: __truediv__(scalar: float) -> Self


   .. py:method:: clone() -> Self


   .. py:method:: get_coeff() -> float


   .. py:method:: get_var() -> fuzzy_dl_owl2.fuzzydl.milp.variable.Variable


