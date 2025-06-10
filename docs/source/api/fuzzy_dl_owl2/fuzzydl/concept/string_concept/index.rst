fuzzy_dl_owl2.fuzzydl.concept.string_concept
============================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.string_concept


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.concept.string_concept.StringConcept


Module Contents
---------------

.. py:class:: StringConcept(name: str)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.concept.concept.Concept`


   Helper class that provides a standard way to create an ABC using
   inheritance.


   .. py:method:: __hash__() -> int


   .. py:method:: __neg__() -> Self


   .. py:method:: clone() -> Self


   .. py:method:: compute_atomic_concepts() -> set[Self]


   .. py:method:: compute_name() -> str | None


   .. py:method:: get_roles() -> set[str]


   .. py:method:: replace(a: Self, c: Self) -> Self | None


