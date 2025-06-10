fuzzy_dl_owl2.fuzzydl.concept.negated_nominal
=============================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.negated_nominal


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.concept.negated_nominal.NegatedNominal


Module Contents
---------------

.. py:class:: NegatedNominal(ind_name: str)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.concept.concept.Concept`


   Negated nominal concept. Only used in range restrictions for the moment.


   .. py:method:: __and__(value: Self) -> Self


   .. py:method:: __hash__() -> int


   .. py:method:: __neg__() -> Self


   .. py:method:: __or__(value: Self) -> Self


   .. py:method:: clone() -> Self


   .. py:method:: compute_name() -> str | None


   .. py:property:: ind_name
      :type: str



   .. py:attribute:: name
      :type:  str
      :value: '(not { Uninferable } )'



