fuzzy_dl_owl2.fuzzydl.concept.all_some_concept
==============================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.all_some_concept


Attributes
----------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.concept.all_some_concept.All
   fuzzy_dl_owl2.fuzzydl.concept.all_some_concept.Some


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.concept.all_some_concept.AllSomeConcept


Module Contents
---------------

.. py:class:: AllSomeConcept(role: str, c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, c_type: fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.concept.concept.Concept`, :py:obj:`fuzzy_dl_owl2.fuzzydl.concept.interface.has_role_concept_interface.HasRoleConceptInterface`


   Helper class that provides a standard way to create an ABC using
   inheritance.


   .. py:method:: __hash__() -> int


   .. py:method:: __neg__() -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept


   .. py:method:: all(role: str, concept: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> Self
      :staticmethod:



   .. py:method:: clone() -> Self


   .. py:method:: compute_atomic_concepts() -> set[fuzzy_dl_owl2.fuzzydl.concept.concept.Concept]


   .. py:method:: compute_name() -> str


   .. py:method:: get_atoms() -> list[Self]


   .. py:method:: get_roles() -> set[str]


   .. py:method:: is_complemented_atomic() -> bool


   .. py:method:: new(c_type: fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType, role: str, concept: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> Self
      :staticmethod:



   .. py:method:: replace(a: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept


   .. py:method:: some(role: str, concept: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> Self
      :staticmethod:



.. py:data:: All

.. py:data:: Some

