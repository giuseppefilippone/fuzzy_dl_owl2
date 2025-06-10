fuzzy_dl_owl2.fuzzydl.concept.approximation_concept
===================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.approximation_concept


Attributes
----------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.concept.approximation_concept.LooseLowerApprox
   fuzzy_dl_owl2.fuzzydl.concept.approximation_concept.LooseUpperApprox
   fuzzy_dl_owl2.fuzzydl.concept.approximation_concept.LowerApprox
   fuzzy_dl_owl2.fuzzydl.concept.approximation_concept.TightLowerApprox
   fuzzy_dl_owl2.fuzzydl.concept.approximation_concept.TightUpperApprox
   fuzzy_dl_owl2.fuzzydl.concept.approximation_concept.UpperApprox


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.concept.approximation_concept.ApproximationConcept


Module Contents
---------------

.. py:class:: ApproximationConcept(c_type: fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType, role: str, c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.concept.concept.Concept`, :py:obj:`fuzzy_dl_owl2.fuzzydl.concept.interface.has_role_concept_interface.HasRoleConceptInterface`


   Helper class that provides a standard way to create an ABC using
   inheritance.


   .. py:method:: __and__(value: Self) -> Self


   .. py:method:: __hash__() -> int


   .. py:method:: __neg__() -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept


   .. py:method:: __or__(value: Self) -> Self


   .. py:method:: clone() -> Self


   .. py:method:: compute_atomic_concepts() -> set[fuzzy_dl_owl2.fuzzydl.concept.concept.Concept]


   .. py:method:: compute_name() -> Optional[str]


   .. py:method:: get_roles() -> set[str]


   .. py:method:: loose_lower_approx(role: str, c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> Self
      :staticmethod:



   .. py:method:: loose_upper_approx(role: str, c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> Self
      :staticmethod:



   .. py:method:: lower_approx(role: str, c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> Self
      :staticmethod:



   .. py:method:: replace(a: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept


   .. py:method:: tight_lower_approx(role: str, c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> Self
      :staticmethod:



   .. py:method:: tight_upper_approx(role: str, c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> Self
      :staticmethod:



   .. py:method:: to_all_some_concept() -> fuzzy_dl_owl2.fuzzydl.concept.all_some_concept.AllSomeConcept


   .. py:method:: upper_approx(role: str, c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> Self
      :staticmethod:



   .. py:attribute:: INVERSE_APPROXIMATION
      :type:  dict[fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType, fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType]


   .. py:attribute:: name


.. py:data:: LooseLowerApprox

.. py:data:: LooseUpperApprox

.. py:data:: LowerApprox

.. py:data:: TightLowerApprox

.. py:data:: TightUpperApprox

.. py:data:: UpperApprox

