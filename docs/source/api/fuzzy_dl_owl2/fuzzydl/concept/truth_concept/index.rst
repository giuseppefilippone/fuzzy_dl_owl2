fuzzy_dl_owl2.fuzzydl.concept.truth_concept
===========================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.truth_concept


Attributes
----------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.concept.truth_concept.BOTTOM
   fuzzy_dl_owl2.fuzzydl.concept.truth_concept.TOP


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.concept.truth_concept.TruthConcept


Module Contents
---------------

.. py:class:: TruthConcept(c_type: fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.concept.concept.Concept`


   Helper class that provides a standard way to create an ABC using
   inheritance.


   .. py:method:: __and__(value: Self) -> Self


   .. py:method:: __eq__(value: Self) -> bool


   .. py:method:: __hash__() -> int


   .. py:method:: __ne__(value: Self) -> bool


   .. py:method:: __neg__() -> Self


   .. py:method:: __or__(value: Self) -> Self


   .. py:method:: __rshift__(value: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept


   .. py:method:: clone() -> Self


   .. py:method:: compute_atomic_concepts() -> set[fuzzy_dl_owl2.fuzzydl.concept.concept.Concept]


   .. py:method:: compute_name() -> Optional[str]


   .. py:method:: get_atomic_concepts() -> set[Self]


   .. py:method:: get_atoms() -> list[Self]


   .. py:method:: get_bottom()
      :staticmethod:



   .. py:method:: get_roles() -> set[str]


   .. py:method:: get_top()
      :staticmethod:



   .. py:method:: is_atomic() -> bool


   .. py:method:: is_complemented_atomic() -> bool


   .. py:method:: replace(a: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept


   .. py:attribute:: name
      :value: '*top*'



.. py:data:: BOTTOM
   :type:  fuzzy_dl_owl2.fuzzydl.concept.concept.Concept

.. py:data:: TOP
   :type:  fuzzy_dl_owl2.fuzzydl.concept.concept.Concept

