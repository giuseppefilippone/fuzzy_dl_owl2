fuzzy_dl_owl2.fuzzydl.concept.concrete.linear_concrete_concept
==============================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.concrete.linear_concrete_concept



.. ── LLM-GENERATED DESCRIPTION START ──

A fuzzy concrete concept defined by a piecewise linear membership function operating on a normalized domain between zero and one.


Description
-----------


Extending the base fuzzy concrete concept functionality, this implementation models a specific type of fuzzy logic where membership degrees are calculated using a piecewise linear function defined over a normalized interval from zero to one. The mathematical behavior is governed by a "knee" point determined by parameters ``a`` and ``b``, creating a linear ramp from the origin to the point (a, b) and a second ramp from (a, b) to (1, 1), ensuring smooth transitions between non-membership and full membership. Input validation is enforced during initialization to guarantee that the lower bound ``k1`` does not exceed the threshold ``a`` and that the intermediate membership degree ``b`` remains within the valid range of 1.0 or less. Beyond calculating membership degrees, the implementation supports standard fuzzy logic operations such as negation, conjunction, and disjunction by delegating to an external operator handler, while also providing capabilities for object cloning and consistent hashing based on the string representation of the concept's parameters.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.concept.concrete.linear_concrete_concept.LinearConcreteConcept


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_concrete_linear_concrete_concept_LinearConcreteConcept.png
       :alt: UML Class Diagram for LinearConcreteConcept
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **LinearConcreteConcept**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_concrete_linear_concrete_concept_LinearConcreteConcept.pdf
       :alt: UML Class Diagram for LinearConcreteConcept
       :align: center
       :width: 12.1cm
       :class: uml-diagram

       UML Class Diagram for **LinearConcreteConcept**

.. py:class:: LinearConcreteConcept(name: str, k1: float, k2: float, a: float, b: float)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_concrete_concept.FuzzyConcreteConcept`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.concept.concrete.linear_concrete_concept.LinearConcreteConcept
      :parts: 1
      :private-bases:


   This class models a fuzzy concept characterized by a piecewise linear membership function operating on a normalized domain from 0 to 1. The function is defined by a specific "knee" point determined by parameters `a` and `b`, creating a linear ramp from (0, 0) to (a, b) and a second linear ramp from (a, b) to (1, 1). While the constructor accepts parameters `k1` and `k2` to denote the definition interval, the membership calculation logic strictly relies on the normalized input value and the `a` and `b` parameters. To use this class, instantiate it with a name and the required float parameters, ensuring that `k1` is less than or equal to `a` and `b` does not exceed 1.0 to avoid validation errors. Once instantiated, the membership degree of a specific value can be retrieved using the `get_membership_degree` method, and the object supports standard fuzzy logic operations such as negation, conjunction, and disjunction.

   :param k1: Lower bound of the interval for which the concept is defined.
   :type k1: float
   :param k2: The upper bound of the interval for which the concept is defined.
   :type k2: float
   :param _a: The lower bound of the interval for which the concept is satisfied, acting as a threshold in the piecewise linear membership function.
   :type _a: float
   :param _b: The membership degree at the threshold `a`, defining the slope of the linear membership function. Must be less than or equal to 1.0.
   :type _b: float


   .. py:method:: __and__(value: Self) -> Self

      Computes the logical conjunction or intersection of the current concept with another instance of the same type. This method enables the use of the bitwise AND operator (`&`) to combine concepts, delegating the specific logic to the `OperatorConcept.and_` method. The operation returns a new instance representing the result, leaving the original operands unchanged.

      :param value: The right-hand operand for the AND operation, which must be an instance of the same type.
      :type value: typing.Self

      :return: The result of the AND operation between this instance and the provided value.

      :rtype: typing.Self



   .. py:method:: __hash__() -> int

      Computes the hash value for the instance based on its string representation, enabling the object to be used as a key in dictionaries or as a member of sets. The implementation delegates to the built-in hash function applied to the result of `str(self)`, meaning the hash value is intrinsically linked to the object's string output. Consequently, if the object is mutable and its string representation changes during its lifetime, the hash value will also change, which violates the standard contract for hashable objects and can lead to errors if the instance is used as a dictionary key after modification. Furthermore, the efficiency of this operation depends on the computational cost of generating the string representation.

      :return: An integer hash value computed from the string representation of the object.

      :rtype: int



   .. py:method:: __neg__() -> fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_concrete_concept.FuzzyConcreteConcept

      Implements the unary negation operator, allowing the concept to be inverted using the `-` prefix. This method delegates the logic to `OperatorConcept.not_` to compute the logical complement of the current instance. The operation returns a new `FuzzyConcreteConcept` representing the negation, rather than modifying the original object.

      :return: A new FuzzyConcreteConcept representing the logical negation of the current concept.

      :rtype: FuzzyConcreteConcept



   .. py:method:: __or__(value: Self) -> Self

      Performs a logical OR operation between the current concept and another concept of the same type. This method enables the use of the pipe operator (`|`) to combine concepts, delegating the underlying logic to the `OperatorConcept.or_` method. It returns a new instance representing the result of the operation, leaving the original operands unchanged.

      :param value: The right-hand operand to combine with the current instance using the OR operation.
      :type value: typing.Self

      :return: Returns a new instance representing the logical OR of this object and the provided value.

      :rtype: typing.Self



   .. py:method:: clone() -> Self

      Creates and returns a new instance of the class that is a distinct copy of the current object. This method initializes the new instance using the values of the `name`, `k1`, `k2`, `a`, and `b` attributes from the original object. The operation does not modify the state of the existing instance, ensuring that the original and the clone are independent objects with identical initial data.

      :return: A new instance of the class initialized with the same attribute values as the current object.

      :rtype: typing.Self



   .. py:method:: compute_name() -> str

      Constructs a descriptive name for the linear concept instance by interpolating its key parameters into a standardized string format. The method retrieves the values of `k1`, `k2`, `a`, and `b` from the instance state and returns them formatted as "linear(k1, k2, a, b)". This function is purely deterministic and has no side effects, relying solely on the current state of the object's attributes.

      :return: A string representation of the linear function formatted with the current parameters.

      :rtype: str



   .. py:method:: get_membership_degree(value: float) -> float

      Calculates the degree of membership for a given input value based on a piecewise linear function defined by the concept's parameters. The input is treated as a normalized value, where any input less than or equal to zero results in a membership of 0.0, and any input greater than or equal to one results in a membership of 1.0. Between zero and the internal threshold `self.a`, the membership increases linearly from 0.0 to `self.b`. For values between `self.a` and 1.0, the membership increases linearly from `self.b` to 1.0. This method does not modify the state of the object.

      :param value: The input value to evaluate against the membership function. Values less than or equal to 0 return 0, and values greater than or equal to 1 return 1.
      :type value: float

      :return: The calculated degree of membership for the input value, bounded between 0.0 and 1.0.

      :rtype: float



   .. py:attribute:: _a
      :type:  float


   .. py:attribute:: _b
      :type:  float


   .. py:property:: a
      :type: float


      Sets the value of the coefficient 'a' for the linear concept. This method accepts a value, converts it to a float, and assigns it to the internal attribute `_a`. It ensures type consistency by forcing the storage format to be a float, which may raise a `ValueError` or `TypeError` if the input is not a valid number. Modifying this property updates the internal state of the object, which may influence subsequent calculations or behaviors relying on this coefficient.

      :param value: The new value to assign to the internal attribute, converted to a float.
      :type value: float


   .. py:property:: b
      :type: float


      Updates the internal state of the instance by assigning a new value to the underlying attribute. The input is coerced to a floating-point number before storage to ensure type consistency, regardless of whether the original input was an integer or a numeric string. This setter modifies the private attribute `_b` and will propagate standard exceptions if the provided value cannot be converted to a float.

      :param value: The new value for the 'b' attribute, converted to a float.
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

