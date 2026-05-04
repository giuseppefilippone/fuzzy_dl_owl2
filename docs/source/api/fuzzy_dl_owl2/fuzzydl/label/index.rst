fuzzy_dl_owl2.fuzzydl.label
===========================

.. py:module:: fuzzy_dl_owl2.fuzzydl.label



.. ── LLM-GENERATED DESCRIPTION START ──

A data structure representing a weighted fuzzy concept that pairs a semantic category with a specific degree of satisfaction.


Description
-----------


The software implements a mechanism for annotating entities within a fuzzy logic framework by associating a specific semantic concept with a quantitative degree of truth. This pairing allows for nuanced representation where an individual does not simply belong to a category but does so with a certain strength or probability. Equality comparisons are handled with strict type checking to ensure that two labels are considered identical only if their underlying concepts match and their weights are of the same class and value. The design supports both numeric and non-numeric degrees, providing flexibility in how truth values are calculated and compared while maintaining a consistent string representation for debugging and display.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.label.Label


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_label_Label.png
       :alt: UML Class Diagram for Label
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **Label**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_label_Label.pdf
       :alt: UML Class Diagram for Label
       :align: center
       :width: 10.4cm
       :class: uml-diagram

       UML Class Diagram for **Label**

.. py:class:: Label(concept: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, weight: fuzzy_dl_owl2.fuzzydl.degree.degree.Degree)

   Represents a weighted fuzzy concept used to annotate individuals, pairing a specific concept with a degree of satisfaction. To use this class, instantiate it with a `Concept` object and a `Degree` value between 0 and 1, where the degree indicates the extent to which the concept applies. The class provides logic for comparing instances, ensuring that two objects are equal only if their concepts are identical and their weights share the same type and numerical value.

   :param concept: The fuzzy concept instance defining the label's semantic category.
   :type concept: Concept
   :param weight: The degree to which the associated concept is satisfied for the individual, represented as a value between 0 and 1.
   :type weight: Degree


   .. py:method:: __eq__(cw: Self) -> bool

      Determines if the current `Label` instance is equal to another instance by comparing their internal state. The method first performs a strict equality check on the `concept` attribute; if the concepts differ, it immediately returns `False`. If the concepts match, the method relies on the `weights_equal` helper function to evaluate the equality of the `weight` attributes, returning the result of that comparison. This operation does not modify the state of either object.

      :param cw: The other instance to compare for equality.
      :type cw: typing.Self

      :return: True if the concepts and weights of the two instances are equal, False otherwise.

      :rtype: bool



   .. py:method:: __ne__(cw: Self) -> bool

      Implements the inequality comparison for the `Label` object, determining whether the current instance differs from the specified `Label` instance (`cw`). It returns `True` if the two instances are not equal and `False` otherwise, effectively inverting the result of the equality check. This method has no side effects and relies entirely on the logic defined in the `__eq__` method to determine equality.

      :param cw: The object to compare against for inequality.
      :type cw: typing.Self

      :return: True if the current instance is not equal to the specified object, False otherwise.

      :rtype: bool



   .. py:method:: __str__() -> str

      Returns a human-readable string representation of the label instance by concatenating the `concept` and `weight` attributes with a single space. This method is implicitly invoked by the built-in `str()` function and print operations to provide a concise summary of the object's state. It has no side effects and relies on the string conversion of the underlying attributes, meaning that non-string values for `concept` or `weight` will be implicitly formatted as strings.

      :return: A human-readable string representation of the object, formatted as 'concept weight'.

      :rtype: str



   .. py:method:: weights_equal(w1: fuzzy_dl_owl2.fuzzydl.degree.degree.Degree, w2: fuzzy_dl_owl2.fuzzydl.degree.degree.Degree) -> bool
      :staticmethod:


      Determines whether two `Degree` instances represent equivalent weights by first verifying that they are instances of the exact same class. If the classes differ, the method returns False immediately. For instances of the same class, non-numeric degrees are considered equal, while numeric degrees are compared based on their specific numerical values. This method performs a strict type check and does not modify the input objects.

      :param w1: The first Degree instance to compare.
      :type w1: Degree
      :param w2: The second degree to compare against the first argument.
      :type w2: Degree

      :return: True if the two Degree objects are of the same class and have equal numerical values (if numeric), otherwise False.

      :rtype: bool



   .. py:attribute:: concept
      :type:  fuzzy_dl_owl2.fuzzydl.concept.concept.Concept


   .. py:attribute:: weight
      :type:  fuzzy_dl_owl2.fuzzydl.degree.degree.Degree

