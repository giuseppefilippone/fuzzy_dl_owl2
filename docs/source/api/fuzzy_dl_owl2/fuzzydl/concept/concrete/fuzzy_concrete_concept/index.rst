fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_concrete_concept
=============================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_concrete_concept


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_concrete_concept.FuzzyConcreteConcept


Module Contents
---------------

.. py:class:: FuzzyConcreteConcept(name: str)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.concept.concept.Concept`, :py:obj:`abc.ABC`


   Fuzzy concrete concept defined with an explicit membership function.


   .. py:method:: compute_atomic_concepts() -> set[Self]


   .. py:method:: compute_name() -> str


   .. py:method:: get_membership_degree(value: float) -> float
      :abstractmethod:


      Get membership degree for a value



   .. py:method:: get_roles() -> set[str]


   .. py:method:: is_concrete() -> bool


   .. py:method:: replace(concept1: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, concept2: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept


   .. py:property:: k1
      :type: float



   .. py:property:: k2
      :type: float



   .. py:attribute:: name
      :type:  str


