fuzzy_dl_owl2.fuzzydl.concept.value_concept
===========================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.value_concept


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.concept.value_concept.ValueConcept


Module Contents
---------------

.. py:class:: ValueConcept(c_type: fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType, role: str, value: Any)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.concept.concept.Concept`, :py:obj:`fuzzy_dl_owl2.fuzzydl.concept.interface.has_value_interface.HasValueInterface`


   Helper class that provides a standard way to create an ABC using
   inheritance.


   .. py:method:: __and__(value: Self) -> Self


   .. py:method:: __hash__() -> int


   .. py:method:: __neg__() -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept


   .. py:method:: __or__(value: Self) -> Self


   .. py:method:: at_least_value(role: str, o: Any) -> Self
      :staticmethod:



   .. py:method:: at_most_value(role: str, o: Any) -> Self
      :staticmethod:



   .. py:method:: clone() -> Self


   .. py:method:: compute_atomic_concepts() -> set[fuzzy_dl_owl2.fuzzydl.concept.concept.Concept]


   .. py:method:: compute_name() -> Optional[str]


   .. py:method:: exact_value(role: str, o: Any) -> Self
      :staticmethod:



   .. py:method:: get_roles() -> set[str]


   .. py:method:: replace(a: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept


   .. py:attribute:: name


