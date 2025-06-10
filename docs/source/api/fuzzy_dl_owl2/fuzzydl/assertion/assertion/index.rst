fuzzy_dl_owl2.fuzzydl.assertion.assertion
=========================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.assertion.assertion


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion


Module Contents
---------------

.. py:class:: Assertion(ind: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, d: fuzzy_dl_owl2.fuzzydl.degree.degree.Degree)

   .. py:method:: __eq__(value: Self) -> bool


   .. py:method:: __ne__(value: Self) -> bool


   .. py:method:: __repr__() -> str


   .. py:method:: __str__() -> str


   .. py:method:: clone() -> Self


   .. py:method:: equals(ass: Self) -> bool


   .. py:method:: get_concept() -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept


   .. py:method:: get_individual() -> fuzzy_dl_owl2.fuzzydl.individual.individual.Individual


   .. py:method:: get_lower_limit() -> fuzzy_dl_owl2.fuzzydl.degree.degree.Degree


   .. py:method:: get_name_without_degree() -> str


   .. py:method:: get_type() -> fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType


   .. py:method:: set_individual(ind: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual) -> None


   .. py:method:: set_lower_limit(deg: fuzzy_dl_owl2.fuzzydl.degree.degree.Degree) -> None


   .. py:attribute:: concept
      :type:  fuzzy_dl_owl2.fuzzydl.concept.concept.Concept


   .. py:attribute:: degree
      :type:  fuzzy_dl_owl2.fuzzydl.degree.degree.Degree


   .. py:attribute:: individual
      :type:  fuzzy_dl_owl2.fuzzydl.individual.individual.Individual


