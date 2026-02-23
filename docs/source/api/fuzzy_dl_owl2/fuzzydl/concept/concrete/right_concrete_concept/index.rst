fuzzy_dl_owl2.fuzzydl.concept.concrete.right_concrete_concept
=============================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.concrete.right_concrete_concept



.. ── LLM-GENERATED DESCRIPTION START ──

Implements a right-shoulder fuzzy membership function where truth values increase linearly from zero to one over a specified interval.


Description
-----------


The implementation models concepts that become increasingly true as a variable grows, such as "high temperature," by defining a geometric shape where membership is zero up to a certain point, ramps up linearly, and then stays at one. It enforces strict ordering constraints during initialization to ensure the domain boundaries correctly encapsulate the transition interval, preventing invalid logical states. By overriding standard Python operators, the class seamlessly integrates with a larger fuzzy logic framework to support negation, conjunction, and disjunction operations. Additional utility features include the ability to generate string representations, clone instances to preserve state, and compute hash values for use in collections.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.concept.concrete.right_concrete_concept.RightConcreteConcept


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_concrete_right_concrete_concept_RightConcreteConcept.png
       :alt: UML Class Diagram for RightConcreteConcept
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **RightConcreteConcept**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_concrete_right_concrete_concept_RightConcreteConcept.pdf
       :alt: UML Class Diagram for RightConcreteConcept
       :align: center
       :width: 12.1cm
       :class: uml-diagram

       UML Class Diagram for **RightConcreteConcept**

.. py:class:: RightConcreteConcept(name: str, k1: float, k2: float, a: float, b: float)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_concrete_concept.FuzzyConcreteConcept`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.concept.concrete.right_concrete_concept.RightConcreteConcept
      :parts: 1
      :private-bases:


   This class models a specific type of fuzzy logic concept characterized by a "right shoulder" membership function, where the degree of truth increases linearly from zero to one over a specified interval. It is typically used to represent concepts that become increasingly true as a variable grows larger, such as "high temperature" or "large size." To use this class, instantiate it with a name, the domain boundaries (`k1`, `k2`) defining the valid range of the variable, and the transition boundaries (`a`, `b`) defining the interval over which the membership ramps up. The class ensures structural integrity by validating that the domain fully encompasses the transition interval and that the transition boundaries are ordered correctly. Once instantiated, the membership degree for any value can be calculated using the `get_membership_degree` method, and the concept supports standard fuzzy logic operations like negation, conjunction, and disjunction.

   :param k1: The lower bound of the domain interval over which the concept is defined.
   :type k1: float
   :param k2: The upper bound of the interval [k1, k2] defining the domain of the concept.
   :type k2: float
   :param _a: The lower bound of the interval for which the concept is satisfied, representing the threshold where the membership degree begins to increase from zero.
   :type _a: float
   :param _b: The upper bound of the satisfaction interval, representing the threshold where the membership degree becomes 1.
   :type _b: float


   .. py:method:: __and__(value: Self) -> Self

      Performs a logical or bitwise conjunction between the current instance and another instance of the same type, typically invoked via the `&` operator. This method delegates the core logic to the `and_` static method of the `OperatorConcept` class, ensuring that the operation is handled consistently within the broader module architecture. It returns a new instance of the class representing the result of the conjunction, leaving the original operands unchanged unless the underlying `OperatorConcept` implementation specifies otherwise.

      :param value: The operand to perform the AND operation with.
      :type value: typing.Self

      :return: A new instance representing the logical conjunction of this object and the provided value.

      :rtype: typing.Self



   .. py:method:: __hash__() -> int

      Calculates the hash value of the instance by hashing the string representation of the object. This allows instances of this class to be used as keys in dictionaries or elements in sets. The hash is derived directly from the output of the `__str__` method, meaning that any changes to the object's state that modify its string representation will also change its hash value, potentially affecting its behavior in hash-based collections.

      :return: An integer representing the hash of the object, computed from its string representation.

      :rtype: int



   .. py:method:: __neg__() -> fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_concrete_concept.FuzzyConcreteConcept

      Implements the unary negation operator, allowing the concept to be inverted using the minus sign. This method returns a new FuzzyConcreteConcept representing the logical negation of the current instance, effectively computing the complement of the concept. The operation is performed by delegating to OperatorConcept.not_ and does not modify the original object in place.

      :return: A `FuzzyConcreteConcept` representing the logical negation of the current concept.

      :rtype: FuzzyConcreteConcept



   .. py:method:: __or__(value: Self) -> Self

      Implements the bitwise OR operation using the `|` operator, allowing the instance to be combined with another value of the same type. The method delegates the specific logic of the operation to `OperatorConcept.or_`, passing both the current instance and the provided value as arguments. It returns the resulting instance, which maintains the type of the operands, though any side effects depend on the implementation of the delegated `or_` method.

      :param value: The right-hand operand to combine with the current instance using the OR operation.
      :type value: typing.Self

      :return: The result of the OR operation between this instance and the provided value.

      :rtype: typing.Self



   .. py:method:: clone() -> Self

      Creates and returns a distinct copy of the current instance by instantiating a new `RightConcreteConcept` object. The new object is initialized with the exact same values for the `name`, `k1`, `k2`, `a`, and `b` attributes as the original. This method ensures that the original object remains unmodified while providing a separate entity with identical state.

      :return: A new instance of the class initialized with the same attribute values as the current object.

      :rtype: typing.Self



   .. py:method:: compute_name() -> str

      Generates a standardized string representation of the right-shoulder concept instance by interpolating the object's defining parameters into a specific format. The returned string follows the pattern "right-shoulder(k1, k2, a, b)", utilizing the values of the corresponding attributes. This operation is read-only and does not alter the state of the object, though it requires that the necessary attributes exist on the instance.

      :return: A string representing the name of the right-shoulder function, formatted with the current parameters k1, k2, a, and b.

      :rtype: str



   .. py:method:: get_membership_degree(x: float) -> float

      Calculates the membership degree of a given value `x` within a right-shoulder fuzzy set defined by the parameters `a` and `b`. The function returns 0.0 if `x` is less than or equal to `a`, and 1.0 if `x` is greater than or equal to `b`. For values falling strictly between `a` and `b`, the method computes a linear interpolation, returning a value between 0.0 and 1.0 that represents the proportional distance of `x` from the lower bound `a`. This calculation is stateless and does not modify the object's attributes.

      :param x: The input value to evaluate for membership.
      :type x: float

      :return: The degree of membership of x in the interval [a, b], ranging from 0.0 to 1.0 based on linear interpolation.

      :rtype: float



   .. py:attribute:: _a
      :type:  float


   .. py:attribute:: _b
      :type:  float


   .. py:property:: a
      :type: float


      Sets the value of the property 'a' by converting the provided input to a float and storing it in the internal attribute '_a'. This method ensures that the underlying state is always maintained as a floating-point number, automatically handling type coercion for compatible inputs such as integers or numeric strings. If the provided value cannot be converted to a float, a TypeError or ValueError will be raised.

      :param value: The value to assign, converted to a float.
      :type value: float


   .. py:property:: b
      :type: float


      Sets the value of the property 'b' by converting the provided input to a float and storing it in the internal attribute '_b'. This method ensures that the underlying state is always maintained as a floating-point number, regardless of the input type, provided it is convertible. If the input value cannot be parsed as a float, a ValueError or TypeError will be raised, and the object's state will remain unchanged until the exception is handled.

      :param value: The new value to assign, which will be converted to a float.
      :type value: float


   .. py:attribute:: k1
      :type:  float

      Sets the value of the `k1` attribute for the instance, converting the input to a float to ensure type consistency. This method updates the private `_k1` variable, effectively modifying the internal state of the `FuzzyConcreteConcept` object. Any subsequent operations relying on this parameter will reflect the new value.

      :param value: The new value for the k1 attribute.
      :type value: float


   .. py:attribute:: k2
      :type:  float

      Sets the upper bound parameter k2 for the fuzzy concrete concept. This method enforces a constraint ensuring that the new value is greater than or equal to the existing k1 parameter; if k1 is larger than the provided value, a ValueError is raised. Upon successful validation, the input is converted to a float and stored in the internal state.

      :param value: The value to assign to the k2 parameter, which must be greater than or equal to k1.
      :type value: float

      :raises ValueError: Raised if the provided value is less than `k1`, as `k2` must be greater than or equal to `k1`.

