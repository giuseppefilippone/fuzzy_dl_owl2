fuzzy_dl_owl2.fuzzydl.concept.sigma_concept
===========================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.sigma_concept


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.concept.sigma_concept.SigmaConcept


Module Contents
---------------

.. py:class:: SigmaConcept(concept: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, role: str, individuals: list[fuzzy_dl_owl2.fuzzydl.individual.individual.Individual], concrete_concept: fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_concrete_concept.FuzzyConcreteConcept)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.concept.concept.Concept`


   Sigma-count concept.


   .. py:method:: __and__(value: Self) -> Self


   .. py:method:: __hash__() -> int


   .. py:method:: __neg__() -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept


   .. py:method:: __or__(value: Self) -> Self


   .. py:method:: clone() -> Self


   .. py:method:: compute_atomic_concepts() -> set[fuzzy_dl_owl2.fuzzydl.concept.concept.Concept]


   .. py:method:: compute_name() -> str | None


   .. py:method:: get_concept() -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept


   .. py:method:: get_fuzzy_concept() -> fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_concrete_concept.FuzzyConcreteConcept


   .. py:method:: get_individuals() -> list[fuzzy_dl_owl2.fuzzydl.individual.individual.Individual]


   .. py:method:: get_role() -> str


   .. py:method:: get_roles() -> set[str]


   .. py:method:: replace(a: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept


   .. py:attribute:: concept
      :type:  fuzzy_dl_owl2.fuzzydl.concept.concept.Concept


   .. py:attribute:: concrete_concept
      :type:  fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_concrete_concept.FuzzyConcreteConcept


   .. py:attribute:: individuals
      :type:  list[fuzzy_dl_owl2.fuzzydl.individual.individual.Individual]


   .. py:attribute:: name
      :type:  str
      :value: '(sigma-count Uninferable Uninferable {} Uninferable)'



   .. py:attribute:: role
      :type:  str


