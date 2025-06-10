fuzzy_dl_owl2.fuzzydl.concept.atomic_concept
============================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.atomic_concept


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.concept.atomic_concept.AtomicConcept


Module Contents
---------------

.. py:class:: AtomicConcept(name: str)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.concept.concept.Concept`


   Helper class that provides a standard way to create an ABC using
   inheritance.


   .. py:method:: __and__(value: Self) -> Self


   .. py:method:: __eq__(value: Self) -> bool


   .. py:method:: __hash__() -> int


   .. py:method:: __invert__() -> Self


   .. py:method:: __ne__(value: Self) -> bool


   .. py:method:: __neg__() -> Self


   .. py:method:: __or__(value: Self) -> Self


   .. py:method:: __repr__() -> str


   .. py:method:: __rshift__(value: Self) -> Self


   .. py:method:: clone() -> Self


   .. py:method:: compute_atomic_concepts() -> set[Self]


   .. py:method:: compute_name() -> str


   .. py:method:: get_atomic_concepts() -> set[Self]


   .. py:method:: get_atoms() -> list[Self]


   .. py:method:: get_clauses(is_type: Callable) -> set[Self]


   .. py:method:: get_roles() -> set[str]


   .. py:method:: is_atomic() -> bool


   .. py:method:: is_complemented_atomic() -> bool


   .. py:method:: is_concrete() -> bool


   .. py:method:: new_atomic_concept() -> Self
      :staticmethod:



   .. py:method:: reduce_idempotency(is_type: Callable) -> Self


   .. py:method:: replace(a: Self, c: Self) -> Optional[Self]


