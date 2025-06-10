fuzzy_dl_owl2.fuzzydl.concept.concrete.modified_concrete_concept
================================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.concrete.modified_concrete_concept


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.concept.concrete.modified_concrete_concept.ModifiedConcreteConcept


Module Contents
---------------

.. py:class:: ModifiedConcreteConcept(name: str, modifier: fuzzy_dl_owl2.fuzzydl.modifier.modifier.Modifier, f: fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_concrete_concept.FuzzyConcreteConcept)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_concrete_concept.FuzzyConcreteConcept`


   Modified concrete concept.


   .. py:method:: __and__(value: Self) -> Self


   .. py:method:: __hash__() -> int


   .. py:method:: __neg__() -> fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_concrete_concept.FuzzyConcreteConcept


   .. py:method:: __or__(value: Self) -> Self


   .. py:method:: clone() -> Self


   .. py:method:: compute_name() -> str


   .. py:method:: get_membership_degree(x: float) -> float

      Get membership degree for a value



   .. py:attribute:: k1
      :type:  float
      :value: 0.0



   .. py:attribute:: k2
      :type:  float
      :value: 1.0



   .. py:property:: modified
      :type: fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_concrete_concept.FuzzyConcreteConcept



   .. py:property:: modifier
      :type: fuzzy_dl_owl2.fuzzydl.modifier.modifier.Modifier



