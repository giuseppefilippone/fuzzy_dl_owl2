fuzzy_dl_owl2.fuzzydl.concept.weighted_min_concept
==================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.weighted_min_concept


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.concept.weighted_min_concept.WeightedMinConcept


Module Contents
---------------

.. py:class:: WeightedMinConcept(weights: list[float], concepts: list[fuzzy_dl_owl2.fuzzydl.concept.concept.Concept])

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.concept.concept.Concept`, :py:obj:`fuzzy_dl_owl2.fuzzydl.concept.interface.has_weighted_concepts_interface.HasWeightedConceptsInterface`


   Helper class that provides a standard way to create an ABC using
   inheritance.


   .. py:method:: __and__(value: Self) -> Self


   .. py:method:: __hash__() -> int


   .. py:method:: __neg__() -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept


   .. py:method:: __or__(value: Self) -> Self


   .. py:method:: clone() -> Self


   .. py:method:: compute_atomic_concepts() -> set[fuzzy_dl_owl2.fuzzydl.concept.concept.Concept]


   .. py:method:: compute_name() -> str


   .. py:method:: get_roles() -> set[str]


   .. py:method:: replace(a: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept


   .. py:attribute:: name
      :value: '(w-min )'



