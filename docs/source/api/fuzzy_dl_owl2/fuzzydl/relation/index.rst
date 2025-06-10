fuzzy_dl_owl2.fuzzydl.relation
==============================

.. py:module:: fuzzy_dl_owl2.fuzzydl.relation


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.relation.Relation


Module Contents
---------------

.. py:class:: Relation(role_name: str, ind1: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, ind2: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, degree: fuzzy_dl_owl2.fuzzydl.degree.degree.Degree)

   Represents a role assertion of the form (object individual, role, lower bound for the degree) with respect to a subject individual.


   .. py:method:: __repr__() -> str


   .. py:method:: __str__() -> str


   .. py:method:: clone() -> Self


   .. py:method:: get_degree() -> fuzzy_dl_owl2.fuzzydl.degree.degree.Degree


   .. py:method:: get_name_without_degree() -> str

      Gets a printable name of the role assertion without the lower bound



   .. py:method:: get_object_individual() -> fuzzy_dl_owl2.fuzzydl.individual.individual.Individual


   .. py:method:: get_role_name() -> str


   .. py:method:: get_subject_individual() -> fuzzy_dl_owl2.fuzzydl.individual.individual.Individual


   .. py:method:: set_object_individual(ind: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual) -> None


   .. py:method:: set_subject_individual(ind: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual) -> None


   .. py:attribute:: degree
      :type:  fuzzy_dl_owl2.fuzzydl.degree.degree.Degree


   .. py:attribute:: ind_a
      :type:  fuzzy_dl_owl2.fuzzydl.individual.individual.Individual


   .. py:attribute:: ind_b
      :type:  fuzzy_dl_owl2.fuzzydl.individual.individual.Individual


   .. py:attribute:: role_name
      :type:  str


