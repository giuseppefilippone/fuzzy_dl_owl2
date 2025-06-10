fuzzy_dl_owl2.fuzzydl.individual.representative_individual
==========================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.individual.representative_individual


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.individual.representative_individual.RepresentativeIndividual


Module Contents
---------------

.. py:class:: RepresentativeIndividual(c_type: fuzzy_dl_owl2.fuzzydl.util.constants.RepresentativeIndividualType, f_name: str, f: fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_number.triangular_fuzzy_number.TriangularFuzzyNumber, ind: fuzzy_dl_owl2.fuzzydl.individual.created_individual.CreatedIndividual)

   New concrete individual being a representative of a set of individuals.
   Given an individual p and a fuzzy number F, a representative individual is the set of individuals that are greater or equal (or less or equal) than F. Then, p is related to the representative individual in some way.


   .. py:method:: get_feature_name() -> str


   .. py:method:: get_fuzzy_number() -> fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_number.triangular_fuzzy_number.TriangularFuzzyNumber


   .. py:method:: get_individual() -> fuzzy_dl_owl2.fuzzydl.individual.created_individual.CreatedIndividual


   .. py:method:: get_type() -> fuzzy_dl_owl2.fuzzydl.util.constants.RepresentativeIndividualType


   .. py:attribute:: f
      :type:  fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_number.triangular_fuzzy_number.TriangularFuzzyNumber


   .. py:attribute:: f_name
      :type:  str


   .. py:attribute:: ind
      :type:  fuzzy_dl_owl2.fuzzydl.individual.created_individual.CreatedIndividual


   .. py:attribute:: type
      :type:  fuzzy_dl_owl2.fuzzydl.util.constants.RepresentativeIndividualType


