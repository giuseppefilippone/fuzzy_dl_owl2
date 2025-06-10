fuzzy_dl_owl2.fuzzydl.concept.implies_concept
=============================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.implies_concept


Attributes
----------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.concept.implies_concept.GoedelImplies
   fuzzy_dl_owl2.fuzzydl.concept.implies_concept.KleeneDienesImplies
   fuzzy_dl_owl2.fuzzydl.concept.implies_concept.LukasiewiczImplies
   fuzzy_dl_owl2.fuzzydl.concept.implies_concept.ZadehImplies


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.concept.implies_concept.ImpliesConcept


Module Contents
---------------

.. py:class:: ImpliesConcept(c_type: fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType, concepts: list[fuzzy_dl_owl2.fuzzydl.concept.concept.Concept])

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.concept.concept.Concept`, :py:obj:`fuzzy_dl_owl2.fuzzydl.concept.interface.has_concepts_interface.HasConceptsInterface`


   Helper class that provides a standard way to create an ABC using
   inheritance.


   .. py:method:: __and__(value: Self) -> Self


   .. py:method:: __eq__(value: Self) -> bool


   .. py:method:: __hash__() -> int


   .. py:method:: __neg__() -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept


   .. py:method:: __or__(value: Self) -> Self


   .. py:method:: clone() -> Self


   .. py:method:: compute_atomic_concepts() -> set[fuzzy_dl_owl2.fuzzydl.concept.concept.Concept]


   .. py:method:: compute_name() -> Optional[str]


   .. py:method:: get_roles() -> set[str]


   .. py:method:: goedel_implies(c1: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, c2: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept
      :staticmethod:



   .. py:method:: kleene_dienes_implies(c1: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, c2: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept
      :staticmethod:



   .. py:method:: lukasiewicz_implies(c1: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, c2: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept
      :staticmethod:



   .. py:method:: replace(a: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept


   .. py:method:: zadeh_implies(c1: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, c2: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept
      :staticmethod:



   .. py:attribute:: name
      :type:  str


.. py:data:: GoedelImplies

.. py:data:: KleeneDienesImplies

.. py:data:: LukasiewiczImplies

.. py:data:: ZadehImplies

