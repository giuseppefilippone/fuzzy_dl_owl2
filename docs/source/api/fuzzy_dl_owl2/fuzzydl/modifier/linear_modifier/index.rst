fuzzy_dl_owl2.fuzzydl.modifier.linear_modifier
==============================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.modifier.linear_modifier


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.modifier.linear_modifier.LinearModifier


Module Contents
---------------

.. py:class:: LinearModifier(name: str, c: float)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.modifier.modifier.Modifier`


   Linear modifier with parameter c


   .. py:method:: __and__(value: Self) -> Self


   .. py:method:: __hash__() -> int


   .. py:method:: __neg__() -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept


   .. py:method:: __or__(value: Self) -> Self


   .. py:method:: clone() -> Self


   .. py:method:: compute_name() -> str


   .. py:method:: get_membership_degree(value: float) -> float

      Gets the image in [0,1] of a real number to the modifier.

      :param value: A real number in the range of values of the modifier function.
      :type value: float

      :returns: Image in [0,1] of x to the explicit modifier function.
      :rtype: float



   .. py:method:: modify(concept: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> fuzzy_dl_owl2.fuzzydl.concept.modified.linearly_modified_concept.LinearlyModifiedConcept

      Modifies a fuzzy concept.

      :param concept: A fuzzy concept
      :type concept: Concept

      :returns: Fuzzy concept resulting from the application of the modifier to c.
      :rtype: Concept



   .. py:property:: a
      :type: float



   .. py:property:: b
      :type: float



   .. py:property:: c
      :type: float



