fuzzy_dl_owl2.fuzzydl.concept.concrete.left_concrete_concept
============================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.concrete.left_concrete_concept


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.concept.concrete.left_concrete_concept.LeftConcreteConcept


Module Contents
---------------

.. py:class:: LeftConcreteConcept(name: str, k1: float, k2: float, a: float, b: float)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_concrete_concept.FuzzyConcreteConcept`


   Fuzzy concrete concept defined with a left shoulder function


   .. py:method:: __and__(value: Self) -> Self


   .. py:method:: __hash__() -> int


   .. py:method:: __neg__() -> fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_concrete_concept.FuzzyConcreteConcept


   .. py:method:: __or__(value: Self) -> Self


   .. py:method:: clone() -> Self


   .. py:method:: compute_name() -> str


   .. py:method:: get_membership_degree(value: float) -> float

      Get membership degree for a value



   .. py:property:: a
      :type: float



   .. py:property:: b
      :type: float



   .. py:attribute:: k1
      :type:  float


   .. py:attribute:: k2
      :type:  float


