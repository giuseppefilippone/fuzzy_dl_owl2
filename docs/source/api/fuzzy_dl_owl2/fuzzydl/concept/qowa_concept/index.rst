fuzzy_dl_owl2.fuzzydl.concept.qowa_concept
==========================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.qowa_concept


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.concept.qowa_concept.QowaConcept


Module Contents
---------------

.. py:class:: QowaConcept(quantifier: fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_concrete_concept.FuzzyConcreteConcept, concepts: list[fuzzy_dl_owl2.fuzzydl.concept.concept.Concept])

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.concept.owa_concept.OwaConcept`


   Quantified-guided OWA concept.


   .. py:method:: __and__(value: Self) -> Self


   .. py:method:: __hash__() -> int


   .. py:method:: __neg__() -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept


   .. py:method:: __or__(value: Self) -> Self


   .. py:method:: clone() -> Self


   .. py:method:: compute_name() -> str


   .. py:method:: compute_weights(n: int) -> None


   .. py:method:: replace(a: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> Optional[fuzzy_dl_owl2.fuzzydl.concept.concept.Concept]


   .. py:attribute:: name
      :value: '(q-owa Uninferable )'



   .. py:property:: quantifier
      :type: fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_concrete_concept.FuzzyConcreteConcept



   .. py:attribute:: type


