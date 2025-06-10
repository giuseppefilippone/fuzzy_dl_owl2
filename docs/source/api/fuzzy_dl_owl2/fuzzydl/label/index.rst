fuzzy_dl_owl2.fuzzydl.label
===========================

.. py:module:: fuzzy_dl_owl2.fuzzydl.label


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.label.Label


Module Contents
---------------

.. py:class:: Label(concept: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, weight: fuzzy_dl_owl2.fuzzydl.degree.degree.Degree)

   Label (weighted concept used in created individuals)


   .. py:method:: __eq__(cw: Self) -> bool


   .. py:method:: __ne__(cw: Self) -> bool


   .. py:method:: __str__() -> str


   .. py:method:: weights_equal(w1: fuzzy_dl_owl2.fuzzydl.degree.degree.Degree, w2: fuzzy_dl_owl2.fuzzydl.degree.degree.Degree) -> bool
      :staticmethod:


      Checks if two degrees are equal



   .. py:attribute:: concept
      :type:  fuzzy_dl_owl2.fuzzydl.concept.concept.Concept


   .. py:attribute:: weight
      :type:  fuzzy_dl_owl2.fuzzydl.degree.degree.Degree


