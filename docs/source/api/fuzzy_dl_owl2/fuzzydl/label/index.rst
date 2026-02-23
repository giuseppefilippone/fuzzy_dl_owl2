fuzzy_dl_owl2.fuzzydl.label
===========================

.. py:module:: fuzzy_dl_owl2.fuzzydl.label



.. ── LLM-GENERATED DESCRIPTION START ──

Encapsulates a fuzzy concept paired with a degree of satisfaction to represent weighted annotations.


Description
-----------


The software defines a data structure that associates a semantic category with a quantitative truth value, enabling the representation of fuzzy logic annotations where membership is not strictly binary. By storing a specific concept alongside a weight between zero and one, it allows for the nuanced description of individuals based on the extent to which they satisfy a particular property. Equality comparisons are implemented with strict type checking to ensure that two instances are considered identical only if their underlying concepts match and their weights share both the same class and numerical value. A static helper method handles the complexity of weight comparison by distinguishing between numeric degrees, which require value checks, and non-numeric degrees, which rely on type identity. This design supports the broader fuzzy description logic system by providing a fundamental unit for expressing graded relationships and ensuring consistent behavior during logical operations.

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

