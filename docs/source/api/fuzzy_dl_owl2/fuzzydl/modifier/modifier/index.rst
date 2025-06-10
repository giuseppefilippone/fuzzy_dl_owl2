fuzzy_dl_owl2.fuzzydl.modifier.modifier
=======================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.modifier.modifier


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.modifier.modifier.Modifier


Module Contents
---------------

.. py:class:: Modifier(name: str)

   Bases: :py:obj:`abc.ABC`


   Fuzzy modifier.


   .. py:method:: __repr__() -> str


   .. py:method:: __str__() -> str


   .. py:method:: clone() -> Self
      :abstractmethod:



   .. py:method:: compute_name() -> str
      :abstractmethod:



   .. py:method:: get_membership_degree(value: float) -> float
      :abstractmethod:


      Gets the image in [0,1] of a real number to the modifier.

      :param value: A real number in the range of values of the modifier function.
      :type value: float

      :returns: Image in [0,1] of x to the explicit modifier function.
      :rtype: float



   .. py:method:: modify(concept: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept
      :abstractmethod:


      Modifies a fuzzy concept.

      :param concept: A fuzzy concept
      :type concept: Concept

      :returns: Fuzzy concept resulting from the application of the modifier to c.
      :rtype: Concept



   .. py:method:: set_name(name: str) -> None


   .. py:attribute:: name
      :type:  str


