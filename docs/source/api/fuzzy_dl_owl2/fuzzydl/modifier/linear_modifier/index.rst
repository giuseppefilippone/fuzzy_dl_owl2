fuzzy_dl_owl2.fuzzydl.modifier.linear_modifier
==============================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.modifier.linear_modifier



.. ── LLM-GENERATED DESCRIPTION START ──

A class that implements a piecewise linear transformation for fuzzy logic membership degrees based on a configurable coefficient.


Description
-----------


The software provides a mechanism to alter the membership degrees of fuzzy concepts using a piecewise linear function defined by a configurable coefficient. By initializing with a specific coefficient, the logic calculates derived weights that determine the slope and intercept of the transformation, effectively shifting the intensity of the membership values. When applied to a concept, the transformation clamps input values between zero and one and interpolates the result based on the calculated weights, ensuring the output remains within valid probability bounds. Integration with the broader fuzzy logic framework is achieved through the creation of modified concept objects and the delegation of logical operations like conjunction and disjunction to a central operator handler.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.modifier.linear_modifier.LinearModifier


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_modifier_linear_modifier_LinearModifier.png
       :alt: UML Class Diagram for LinearModifier
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **LinearModifier**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_modifier_linear_modifier_LinearModifier.pdf
       :alt: UML Class Diagram for LinearModifier
       :align: center
       :width: 10.8cm
       :class: uml-diagram

       UML Class Diagram for **LinearModifier**

.. py:class:: LinearModifier(name: str, c: float)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.modifier.modifier.Modifier`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.modifier.linear_modifier.LinearModifier
      :parts: 1
      :private-bases:


   This class implements a modifier that applies a piecewise linear transformation to the membership degrees of concepts, governed by a configurable parameter 'c'. The value of 'c' determines the inflection point of the linear function, allowing for precise control over the intensity of the modification. To use this class, instantiate it with a name and the desired 'c' value, then apply it to a `Concept` object using the `modify` method to produce a `LinearlyModifiedConcept`. The logic ensures that membership degrees are clamped between 0 and 1, and the class supports logical operations such as negation, conjunction, and disjunction.

   :param _c: The parameter determining the slope and intercept of the linear membership function.
   :type _c: float
   :param _a: The threshold value on the input domain that separates the two linear segments of the membership function.
   :type _a: float
   :param _b: The y-coordinate of the intermediate point $(a, b)$ in the piecewise linear membership function.
   :type _b: float


   .. py:method:: __and__(value: Self) -> Self

      Implements the bitwise AND operation (`&`) for the `LinearModifier` class, enabling the combination of the current instance with another instance of the same type. This method delegates the specific logic for the conjunction to `OperatorConcept.and_`, which determines how the two modifiers interact. The operation returns a new `LinearModifier` instance representing the result, ensuring that the original operands are not modified.

      :param value: The right-hand operand for the AND operation.
      :type value: typing.Self

      :return: The result of the AND operation between this instance and the provided value.

      :rtype: typing.Self



   .. py:method:: __hash__() -> int

      Computes the integer hash value for the `LinearModifier` instance based on its string representation, enabling the object to be used as a key in dictionaries or as a member of sets. The implementation delegates the hashing logic to the result of `str(self)`, ensuring that two instances with identical string representations produce the same hash. However, because the hash is derived from the string form, any changes to the object's state that alter its string representation will result in a different hash value, which violates the immutability requirement for objects used in hashed collections and may lead to lookup errors.

      :return: An integer hash value derived from the string representation of the object.

      :rtype: int



   .. py:method:: __neg__() -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept

      Implements the unary negation operator for the `LinearModifier` instance, returning a new `Concept` that represents the logical negation of the current modifier. This operation delegates the creation of the negated concept to the `OperatorConcept.not_` factory method, ensuring that the resulting object encapsulates the inverse logic without modifying the original instance.

      :return: A Concept representing the logical negation of the current instance.

      :rtype: Concept



   .. py:method:: __or__(value: Self) -> Self

      Implements the bitwise OR operation for the `LinearModifier` class, allowing instances to be combined using the pipe operator (`|`). This method takes another `LinearModifier` instance and delegates the combination logic to `OperatorConcept.or_`, returning a new instance that represents the result of the operation. The original instances remain unmodified, ensuring that the operation is side-effect-free.

      :param value: The right-hand operand to combine with the current instance using the OR operation.
      :type value: typing.Self

      :return: The result of the OR operation between the current instance and the provided value.

      :rtype: typing.Self



   .. py:method:: clone() -> Self

      Creates and returns a new instance of `LinearModifier` that is a copy of the current object. The clone is initialized with the same `name` and `c` attributes as the original, resulting in an independent object that can be modified without affecting the source.

      :return: A new instance of the class that is a copy of the current object.

      :rtype: typing.Self



   .. py:method:: compute_name() -> str

      Generates a string identifier for the linear modifier based on its coefficient attribute. The returned string follows the specific format "linear-modifier(c)", where 'c' is replaced by the string representation of the instance's 'c' attribute. This method performs no state modification and assumes the 'c' attribute is defined and convertible to a string.

      :return: A string representing the name of the linear modifier, formatted as 'linear-modifier({c})'.

      :rtype: str



   .. py:method:: get_membership_degree(value: float) -> float

      Calculates the degree of membership for a given input value using a piecewise linear function defined by the instance attributes `a` and `b`. The function maps the input range [0, 1] to an output range [0, 1], clamping any values outside this interval to the nearest boundary. Specifically, for inputs between 0 and `a`, the result is linearly interpolated from 0 to `b`, whereas inputs between `a` and 1 are interpolated from `b` to 1. This method does not modify the state of the object.

      :param value: The crisp input value for which to calculate the membership degree. Values outside the range [0, 1] are clamped to the nearest boundary.
      :type value: float

      :return: A float representing the degree of membership for the input value, ranging from 0.0 to 1.0.

      :rtype: float



   .. py:method:: modify(concept: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> fuzzy_dl_owl2.fuzzydl.concept.modified.linearly_modified_concept.LinearlyModifiedConcept

      Applies the linear modification logic encapsulated by this instance to a provided concept. This method constructs and returns a new `LinearlyModifiedConcept` object that wraps the original concept alongside the current modifier, effectively binding the two without mutating the original concept.

      :param concept: The Concept instance to be modified.
      :type concept: Concept

      :return: A `LinearlyModifiedConcept` representing the input `concept` modified by the current object.

      :rtype: LinearlyModifiedConcept



   .. py:attribute:: _a
      :type:  float


   .. py:attribute:: _b
      :type:  float


   .. py:attribute:: _c
      :type:  float


   .. py:property:: a
      :type: float


      Sets the value of the 'a' coefficient for the linear modifier. This method updates the object's internal state by assigning the provided floating-point value to the private attribute `_a`. It allows the linear parameter to be modified dynamically after the object has been initialized.

      :param value: The new float value to assign to the property.
      :type value: float


   .. py:property:: b
      :type: float


      Sets the internal coefficient 'b' for the linear modifier to the specified floating-point value. This method updates the object's state by assigning the input directly to the private attribute `_b`. Since no validation logic is present in the implementation, any float value is accepted, potentially including edge cases like infinity or NaN.

      :param value: The new value to assign to the b attribute.
      :type value: float


   .. py:property:: c
      :type: float


      Updates the value of the 'c' property, which likely represents a constant term or coefficient in the linear modification logic. This setter assigns the provided floating-point value to the internal `_c` attribute, thereby modifying the object's state. Since the implementation performs a direct assignment without explicit type enforcement, passing incompatible types may result in unexpected behavior during subsequent calculations that rely on this value.

      :param value: The new value to assign to the internal c attribute.
      :type value: float

