fuzzy_dl_owl2.fuzzydl.concept.modified.triangularly_modified_concept
====================================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.modified.triangularly_modified_concept


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.concept.modified.triangularly_modified_concept.TriangularlyModifiedConcept


Module Contents
---------------

.. py:class:: TriangularlyModifiedConcept(c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, mod: fuzzy_dl_owl2.fuzzydl.modifier.modifier.Modifier)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.concept.modified.modified_concept.ModifiedConcept`


   Fuzzy concept modified with a triangular modifier.


   .. py:method:: __and__(value: Self) -> Self


   .. py:method:: __hash__() -> int


   .. py:method:: __neg__() -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept


   .. py:method:: __or__(value: Self) -> Self


   .. py:method:: clone() -> Self


   .. py:method:: replace(a: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept


