fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_number.triangular_fuzzy_number
===========================================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_number.triangular_fuzzy_number


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_number.triangular_fuzzy_number.TriangularFuzzyNumber


Module Contents
---------------

.. py:class:: TriangularFuzzyNumber(name: str, a: float, b: float, c: float)
              TriangularFuzzyNumber(a: float, b: float, c: float)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.concept.concrete.triangular_concrete_concept.TriangularConcreteConcept`


   Fuzzy number defined with a triangular function.


   .. py:method:: __add__(other: Self) -> Self


   .. py:method:: __and__(value: Self) -> Self


   .. py:method:: __eq__(other: Self) -> bool


   .. py:method:: __hash__() -> int


   .. py:method:: __mul__(other: Self) -> Self


   .. py:method:: __ne__(other: Self) -> bool


   .. py:method:: __neg__() -> TriangularFuzzyNumber


   .. py:method:: __or__(value: Self) -> Self


   .. py:method:: __sub__(other: Self) -> Self


   .. py:method:: __truediv__(other: Self) -> Self


   .. py:method:: add(t1: Self, t2: Self) -> Self
      :staticmethod:


      Adds two triangular fuzzy numbers.



   .. py:method:: clone() -> Self


   .. py:method:: compute_name() -> str


   .. py:method:: divided_by(t1: Self, t2: Self) -> Self
      :staticmethod:


      Divides two triangular fuzzy numbers.



   .. py:method:: get_best_non_fuzzy_performance() -> float

      Gets the Best Non fuzzy Performance (BNP) of the fuzzy number.



   .. py:method:: has_defined_range() -> bool
      :staticmethod:


      Checks if the range of the fuzzy numbers has been defined.



   .. py:method:: is_concrete() -> bool


   .. py:method:: is_number() -> bool


   .. py:method:: minus(t1: Self, t2: Self) -> Self
      :staticmethod:


      Subtracts two triangular fuzzy numbers.



   .. py:method:: set_range(min_range: float, max_range: float) -> None
      :staticmethod:



   .. py:method:: times(t1: Self, t2: Self) -> Self
      :staticmethod:


      Multiplies two triangular fuzzy numbers.



   .. py:attribute:: K1
      :type:  float


   .. py:attribute:: K2
      :type:  float


