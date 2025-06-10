fuzzy_dl_owl2.fuzzydl.general_concept_inclusion
===============================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.general_concept_inclusion


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.general_concept_inclusion.GeneralConceptInclusion


Module Contents
---------------

.. py:class:: GeneralConceptInclusion(subsumer: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, subsumed: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, degree: fuzzy_dl_owl2.fuzzydl.degree.degree.Degree, type_: fuzzy_dl_owl2.fuzzydl.util.constants.LogicOperatorType)

   General concept inclusion axiom.


   .. py:method:: __eq__(other: Self) -> bool


   .. py:method:: __ge__(other: Self) -> bool


   .. py:method:: __gt__(other: Self) -> bool


   .. py:method:: __hash__() -> int


   .. py:method:: __le__(other: Self) -> bool


   .. py:method:: __lt__(other: Self) -> bool


   .. py:method:: __ne__(other: Self) -> bool


   .. py:method:: __repr__() -> str


   .. py:method:: __str__() -> str


   .. py:method:: clone() -> Self


   .. py:method:: get_degree() -> fuzzy_dl_owl2.fuzzydl.degree.degree.Degree


   .. py:method:: get_subsumed() -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept


   .. py:method:: get_subsumer() -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept


   .. py:method:: get_type() -> fuzzy_dl_owl2.fuzzydl.util.constants.LogicOperatorType


   .. py:method:: set_degree(deg: fuzzy_dl_owl2.fuzzydl.degree.degree.Degree) -> None


   .. py:method:: set_subsumed(new_concept: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> None


   .. py:method:: set_subsumer(new_concept: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> None


   .. py:attribute:: degree
      :type:  fuzzy_dl_owl2.fuzzydl.degree.degree.Degree


   .. py:attribute:: subsumed
      :type:  fuzzy_dl_owl2.fuzzydl.concept.concept.Concept


   .. py:attribute:: subsumer
      :type:  fuzzy_dl_owl2.fuzzydl.concept.concept.Concept


   .. py:attribute:: type
      :type:  fuzzy_dl_owl2.fuzzydl.util.constants.LogicOperatorType


