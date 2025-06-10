fuzzy_dl_owl2.fuzzydl.concept.modified.modified_concept
=======================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.modified.modified_concept


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.concept.modified.modified_concept.ModifiedConcept


Module Contents
---------------

.. py:class:: ModifiedConcept(c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, mod: fuzzy_dl_owl2.fuzzydl.modifier.modifier.Modifier)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.concept.concept.Concept`, :py:obj:`fuzzy_dl_owl2.fuzzydl.concept.interface.has_concept_interface.HasConceptInterface`, :py:obj:`abc.ABC`


   Modified fuzzy concept.


   .. py:method:: __and__() -> Self


   .. py:method:: __neg__() -> Self


   .. py:method:: __or__() -> Self


   .. py:method:: __repr__() -> str


   .. py:method:: __str__() -> str


   .. py:method:: compute_atomic_concepts() -> set[Self]


   .. py:method:: compute_name() -> str | None


   .. py:method:: get_roles() -> set[str]


   .. py:method:: is_concrete() -> bool


   .. py:method:: replace(concept1: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, concept2: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept


   .. py:property:: modifier
      :type: fuzzy_dl_owl2.fuzzydl.modifier.modifier.Modifier



