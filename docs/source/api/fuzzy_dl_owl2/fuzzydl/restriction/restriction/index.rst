fuzzy_dl_owl2.fuzzydl.restriction.restriction
=============================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.restriction.restriction


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.restriction.restriction.Restriction


Module Contents
---------------

.. py:class:: Restriction(role_name: str, concept: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, degree: fuzzy_dl_owl2.fuzzydl.degree.degree.Degree)

   Universal restriction formed by a role, a concept and a lower bound degree.


   .. py:method:: __repr__() -> str


   .. py:method:: __str__() -> str


   .. py:method:: clone() -> Self


   .. py:method:: get_concept() -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept


   .. py:method:: get_degree() -> fuzzy_dl_owl2.fuzzydl.degree.degree.Degree


   .. py:method:: get_name_without_degree() -> str

      Gets the name of the restriction without the degree.



   .. py:method:: get_role_name() -> str


   .. py:attribute:: concept
      :type:  fuzzy_dl_owl2.fuzzydl.concept.concept.Concept


   .. py:attribute:: degree
      :type:  fuzzy_dl_owl2.fuzzydl.degree.degree.Degree


   .. py:attribute:: role_name
      :type:  str


