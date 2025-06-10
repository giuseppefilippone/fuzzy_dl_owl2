fuzzy_dl_owl2.fuzzydl.concept.quasi_sugeno_integral
===================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.quasi_sugeno_integral


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.concept.quasi_sugeno_integral.QsugenoIntegral


Module Contents
---------------

.. py:class:: QsugenoIntegral(weights: list[float], concepts: list[fuzzy_dl_owl2.fuzzydl.concept.concept.Concept])

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.concept.sugeno_integral.SugenoIntegral`


   Quasi Sugeno integral concept.


   .. py:method:: __and__(value: Self) -> Self


   .. py:method:: __hash__() -> int


   .. py:method:: __neg__() -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept


   .. py:method:: __or__(value: Self) -> Self


   .. py:method:: clone() -> Self


   .. py:method:: compute_name() -> str


   .. py:method:: replace(a: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept


   .. py:attribute:: type


