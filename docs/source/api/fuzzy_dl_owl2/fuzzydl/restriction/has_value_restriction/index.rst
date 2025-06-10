fuzzy_dl_owl2.fuzzydl.restriction.has_value_restriction
=======================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.restriction.has_value_restriction


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.restriction.has_value_restriction.HasValueRestriction


Module Contents
---------------

.. py:class:: HasValueRestriction(role_name: str, individual: str, degree: fuzzy_dl_owl2.fuzzydl.degree.degree.Degree)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.restriction.restriction.Restriction`


   Universal restriction formed by a role, a individual and a lower bound degree.


   .. py:method:: get_individual() -> str


   .. py:method:: get_name_without_degree() -> str

      Gets the name of the restriction without the degree.



   .. py:attribute:: ind_name
      :type:  str


