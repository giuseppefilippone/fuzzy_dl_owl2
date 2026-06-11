fuzzy_dl_owl2.fuzzydl.modifier.triangular_modifier
==================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.modifier.triangular_modifier



.. ── LLM-GENERATED DESCRIPTION START ──

Implements a fuzzy logic modifier that applies a triangular membership function to concepts using three distinct boundary parameters to define degrees of membership.


Description
-----------


The implementation defines a mathematical model where membership degrees increase linearly from a lower bound to a peak and then decrease linearly to an upper bound, effectively modeling vague or imprecise linguistic terms within a fuzzy description logic system. Upon initialization, the logic enforces strict ordering constraints on the boundary parameters to ensure the formation of a valid triangle, raising an error if the configuration is geometrically impossible. By wrapping base concepts into a specialized modified structure, the software allows for the dynamic evaluation of membership values based on the specific triangular shape defined by the instance. Furthermore, the design supports logical composition through operator overloading, enabling the combination or negation of modifiers to construct more complex fuzzy expressions while maintaining immutability and hashability for use in collections.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.modifier.triangular_modifier.TriangularModifier


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_modifier_triangular_modifier_TriangularModifier.png
       :alt: UML Class Diagram for TriangularModifier
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **TriangularModifier**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_modifier_triangular_modifier_TriangularModifier.pdf
       :alt: UML Class Diagram for TriangularModifier
       :align: center
       :width: 10.1cm
       :class: uml-diagram

       UML Class Diagram for **TriangularModifier**

.. py:class:: TriangularModifier(name: str, a: float, b: float, c: float)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.modifier.modifier.Modifier`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.modifier.triangular_modifier.TriangularModifier
      :parts: 1
      :private-bases:


   This class implements a fuzzy logic modifier that applies a triangular membership function to concepts, defining how strongly a specific value belongs to a modified concept. The function is characterized by three parameters: the left boundary `a`, the peak `b`, and the right boundary `c`, which must satisfy the ordering $a \le b \le c$. Membership degrees increase linearly from 0 at `a` to 1 at `b`, and then decrease linearly back to 0 at `c`. To utilize this modifier, instantiate it with a name and the three boundary values, and then apply it to a `Concept` instance via the `modify` method, which produces a `TriangularlyModifiedConcept`. The class also provides a `get_membership_degree` method for calculating the specific membership value of a given input.

   :param _a: The left endpoint of the triangular membership function, marking the lower bound where the membership degree begins to increase from zero.
   :type _a: typing.Any
   :param _b: The x-coordinate of the peak of the triangular membership function, representing the point of maximum membership degree.
   :type _b: typing.Any
   :param _c: The right endpoint of the triangular membership function, defining the upper bound where the membership degree reaches zero.
   :type _c: typing.Any


   .. py:method:: __and__(value: Self) -> Self

      Implements the bitwise AND operation (`&`) for the `TriangularModifier` class, enabling logical conjunction between the current instance and another of the same type. This method delegates the underlying logic to `OperatorConcept.and_` and returns a new `TriangularModifier` instance representing the combined result, ensuring that the operation does not modify the original operands in place.

      :param value: The right-hand operand for the AND operation, which must be an instance of the same class.
      :type value: typing.Self

      :return: The result of the AND operation between the current instance and the provided value.

      :rtype: typing.Self



   .. py:method:: __hash__() -> int

      Return a hash value for this object, computed from its string representation. This approach ensures that the hash value reflects the structural identity of the object without relying on cached values or additional methods. The hash is derived from the output of the `__str__` method, which provides a consistent and unique representation of the concept's structure. This implementation does not utilize any internal caching mechanism and directly computes the hash each time it is called.

      :return: An integer hash value representing the structural identity of this object.

      :rtype: int



   .. py:method:: __neg__() -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept

      Implements the unary negation operator, enabling the use of the minus sign to invert the logic of the triangular modifier. This method returns a new `Concept` instance representing the logical complement of the current modifier by delegating to `OperatorConcept.not_`. The operation is non-destructive, leaving the original modifier unchanged while generating a distinct conceptual entity that encapsulates the negation.

      :return: A Concept representing the logical negation of the current instance.

      :rtype: Concept



   .. py:method:: __or__(value: Self) -> Self

      Implements the bitwise OR operation using the pipe operator (`|`) to combine the current instance with another `TriangularModifier`. This method delegates the logic to `OperatorConcept.or_`, which calculates the union of the two modifiers based on the underlying concept definitions. It returns a new instance of `TriangularModifier` representing the combined result, ensuring that the original operands remain unmodified.

      :param value: The right-hand operand to combine with the current instance using the OR operation.
      :type value: typing.Self

      :return: The result of the OR operation between this instance and the provided value.

      :rtype: typing.Self



   .. py:method:: clone() -> Self

      Creates and returns a new instance of the class that is a copy of the current object. This method instantiates a new object using the current values of the `name`, `a`, `b`, and `c` attributes, ensuring that the returned modifier has the same configuration as the original. The operation has no side effects on the existing instance.

      :return: A new instance of the class with identical attributes to the current instance.

      :rtype: typing.Self



   .. py:method:: compute_name() -> str

      Generates a standardized string representation for the triangular modifier instance based on its defining parameters. The returned value follows the format 'triangular-modifier(a, b, c)', incorporating the current values of the instance's attributes a, b, and c. This method does not modify the object's state and is primarily useful for logging, debugging, or identifying specific modifier configurations.

      :return: A string representing the name of the triangular modifier, formatted with the values of a, b, and c.

      :rtype: str



   .. py:method:: get_membership_degree(x: float) -> float

      Calculates the degree of membership for a given input value x within a triangular fuzzy set defined by the parameters a, b, and c. The function returns 0.0 if the input lies outside the interval [a, c]. For values between a and the peak b, the membership increases linearly, while values between b and c result in a linear decrease. This method performs a pure calculation without modifying internal state or causing side effects.

      :param x: The input value for which to calculate the membership degree.
      :type x: float

      :return: The degree of membership of the input value x to the fuzzy set, ranging from 0.0 (no membership) to 1.0 (full membership).

      :rtype: float



   .. py:method:: modify(concept: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept

      Applies the triangular modification logic encapsulated by this instance to the provided concept. This method does not mutate the original concept directly; instead, it creates and returns a new `TriangularlyModifiedConcept` wrapper that combines the original concept with the current modifier. This allows the modified concept to be evaluated or processed with the specific triangular characteristics defined by the modifier.

      :param concept: The concept to be modified.
      :type concept: Concept

      :return: A new Concept instance that wraps the provided concept and applies a triangular modification using the current object.

      :rtype: Concept



   .. py:attribute:: _a


   .. py:attribute:: _b


   .. py:attribute:: _c


   .. py:property:: a
      :type: float


      Returns the left endpoint of this triangular modifier's membership function, i.e. the lower bound where the membership degree begins rising from zero toward the peak. The value is read from the private ``_a`` attribute without modifying the instance.

      :return: The left endpoint ``a`` of the triangle.

      :rtype: float


   .. py:property:: b
      :type: float


      Returns the peak of this triangular modifier's membership function, i.e. the point where the membership degree reaches its maximum value of ``1``. The value is read from the private ``_b`` attribute without modifying the instance.

      :return: The peak ``b`` of the triangle.

      :rtype: float


   .. py:property:: c
      :type: float


      Returns the right endpoint of this triangular modifier's membership function, i.e. the upper bound where the membership degree falls back to zero. The value is read from the private ``_c`` attribute without modifying the instance.

      :return: The right endpoint ``c`` of the triangle.

      :rtype: float

