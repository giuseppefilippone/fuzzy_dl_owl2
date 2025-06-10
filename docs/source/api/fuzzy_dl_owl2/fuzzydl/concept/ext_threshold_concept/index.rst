fuzzy_dl_owl2.fuzzydl.concept.ext_threshold_concept
===================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.ext_threshold_concept


Attributes
----------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.concept.ext_threshold_concept.ExtendedNegThreshold
   fuzzy_dl_owl2.fuzzydl.concept.ext_threshold_concept.ExtendedPosThreshold


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.concept.ext_threshold_concept.ExtThresholdConcept


Module Contents
---------------

.. py:class:: ExtThresholdConcept(c_type: fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType, c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, weight_variable: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.concept.concept.Concept`, :py:obj:`fuzzy_dl_owl2.fuzzydl.concept.interface.has_concept_interface.HasConceptInterface`


   Helper class that provides a standard way to create an ABC using
   inheritance.


   .. py:method:: __and__(value: Self) -> Self


   .. py:method:: __hash__() -> int


   .. py:method:: __neg__() -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept


   .. py:method:: __or__(value: Self) -> Self


   .. py:method:: clone()


   .. py:method:: compute_atomic_concepts() -> set[fuzzy_dl_owl2.fuzzydl.concept.concept.Concept]


   .. py:method:: compute_name() -> Optional[str]


   .. py:method:: extended_neg_threshold(v: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, c: Self) -> Self
      :staticmethod:



   .. py:method:: extended_pos_threshold(v: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, c: Self) -> Self
      :staticmethod:



   .. py:method:: get_roles() -> set[str]


   .. py:method:: replace(a: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept


   .. py:attribute:: name
      :type:  str
      :value: '([>= Uninferable] Uninferable)'



   .. py:property:: weight_variable
      :type: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable



.. py:data:: ExtendedNegThreshold

.. py:data:: ExtendedPosThreshold

