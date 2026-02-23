fuzzy_dl_owl2.fuzzydl.concept.concrete.trapezoidal_concrete_concept
===================================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.concrete.trapezoidal_concrete_concept



.. ── LLM-GENERATED DESCRIPTION START ──

Implements a trapezoidal concrete concept that models fuzzy membership degrees using a four-point geometric shape within a defined domain.


Description
-----------


The logic calculates membership values by defining a support interval where the degree is zero, a core interval where the degree is one, and linear transitions between these states based on specific vertex parameters. Strict validation ensures that the geometric parameters adhere to the required ordering and that the universe of discourse fully contains the trapezoid's shape to prevent mathematical inconsistencies. By overriding standard operators, the implementation enables logical combinations such as AND, OR, and NOT, delegating the complex computations to a dedicated operator utility. Additional functionality includes generating string representations for identification and creating independent copies of the instance to preserve state integrity during manipulation.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.concept.concrete.trapezoidal_concrete_concept.TrapezoidalConcreteConcept


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_concrete_trapezoidal_concrete_concept_TrapezoidalConcreteConcept.png
       :alt: UML Class Diagram for TrapezoidalConcreteConcept
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **TrapezoidalConcreteConcept**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_concrete_trapezoidal_concrete_concept_TrapezoidalConcreteConcept.pdf
       :alt: UML Class Diagram for TrapezoidalConcreteConcept
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **TrapezoidalConcreteConcept**

.. py:class:: TrapezoidalConcreteConcept(name: str, k1: float, k2: float, a: float, b: float, c: float, d: float)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_concrete_concept.FuzzyConcreteConcept`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.concept.concrete.trapezoidal_concrete_concept.TrapezoidalConcreteConcept
      :parts: 1
      :private-bases:


   This class represents a trapezoidal concrete concept within a fuzzy logic framework, defining a membership function that follows a trapezoidal shape. It is defined by a universe of discourse interval [k1, k2] and four shape parameters a, b, c, and d, which establish the support [a, d] and the core [b, c] of the concept. The membership degree is 0 for values less than or equal to a or greater than or equal to d, equals 1 for values between b and c, and transitions linearly for values in the intervals (a, b) and (c, d). To use this class, instantiate it with a descriptive name and the required float parameters, ensuring that the shape parameters adhere to the strict ordering a <= b <= c <= d and that the definition interval fully encompasses the support interval (k1 <= a and k2 >= d). The class provides functionality to calculate membership degrees, clone instances, and supports logical operations such as AND, OR, and NOT via operator overloading.

   :param name: Identifier for the concept, used for identification and debugging purposes.
   :type name: str
   :param k1: The lower bound of the interval [k1, k2] defining the domain over which the concept is defined.
   :type k1: float
   :param k2: The upper bound of the interval for which the concept is defined.
   :type k2: float
   :param _a: The lower bound of the support interval, marking the point where the membership degree begins to increase from zero.
   :type _a: float
   :param _b: The lower bound of the plateau region where the membership degree is 1.
   :type _b: float
   :param _c: The upper bound of the plateau where the membership degree is 1.
   :type _c: float
   :param _d: The upper bound of the interval for which the concept is satisfied, representing the point where the membership degree drops to zero.
   :type _d: float


   .. py:method:: __and__(value: Self) -> Self

      Performs a logical conjunction (AND) operation between the current instance and another instance of the same type, typically invoked via the `&` operator. The method delegates the core logic to the `OperatorConcept.and_` function, returning a new instance that represents the result while leaving the original operands unchanged.

      :param value: The right-hand operand to perform the AND operation with.
      :type value: typing.Self

      :return: The result of the AND operation between this instance and the provided value.

      :rtype: typing.Self



   .. py:method:: __hash__() -> int

      Computes the integer hash value for the instance, enabling its use as a key in dictionary lookups or membership in sets. The implementation derives the hash from the string representation of the object, meaning that two instances with identical string outputs will produce the same hash code. Because the hash is based on the string representation, the efficiency of this method is directly tied to the performance of the `__str__` method, and any mutation that alters the string output will result in a different hash value.

      :return: An integer hash value derived from the string representation of the object.

      :rtype: int



   .. py:method:: __neg__() -> fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_concrete_concept.FuzzyConcreteConcept

      Implements the unary negation operator for the trapezoidal fuzzy concept, returning a new concept that represents the logical complement of the current instance. This operation delegates the calculation to the `not_` method of the `OperatorConcept` class, effectively inverting the membership function. The method does not modify the original object but instead produces a new `FuzzyConcreteConcept` instance reflecting the negated state.

      :return: Returns the logical negation of the current concept.

      :rtype: FuzzyConcreteConcept



   .. py:method:: __or__(value: Self) -> Self

      Implements the bitwise OR operation for the concept, allowing the use of the pipe operator (`|`) to combine two instances. This method delegates the logic to the `OperatorConcept.or_` method, which computes the logical disjunction between the current object and the provided value. It returns a new instance of the same type representing the result of the operation, leaving the original operands unchanged.

      :param value: The right-hand operand to combine with the current instance using the OR operator.
      :type value: typing.Self

      :return: The result of the OR operation between the current instance and the provided value.

      :rtype: typing.Self



   .. py:method:: clone() -> Self

      Creates and returns a new instance that is an independent copy of the current object. The method instantiates a new object using the current values of the `name`, `k1`, `k2`, `a`, `b`, `c`, and `d` attributes. This operation has no side effects on the original instance, ensuring that modifications to the returned copy do not affect the source data.

      :return: A new instance of the class initialized with the same attribute values as the current object.

      :rtype: typing.Self



   .. py:method:: compute_name() -> str

      Constructs a human-readable string identifier that encapsulates the specific parameters of the trapezoidal concept. The output is formatted as a function-like string containing the values of the six defining attributes—k1, k2, a, b, c, and d—enclosed in parentheses. This method relies on the existence of these instance attributes and will raise an error if any are undefined.

      :return: A string representation of the trapezoidal configuration with the current parameter values.

      :rtype: str



   .. py:method:: get_membership_degree(x: float) -> float

      Computes the degree of membership for a given input value within a trapezoidal fuzzy set defined by the instance's boundary parameters. The function returns 0.0 if the input lies outside the range defined by the lower and upper bounds, and returns 1.0 if the input falls within the central plateau. For values located on the rising or falling edges of the trapezoid, the method performs linear interpolation to return a fractional membership value between 0.0 and 1.0. This calculation is stateless and does not modify the object's attributes.

      :param x: The input value to evaluate against the membership function.
      :type x: float

      :return: The degree of membership of the input value x, ranging from 0.0 to 1.0.

      :rtype: float



   .. py:attribute:: _a
      :type:  float


   .. py:attribute:: _b
      :type:  float


   .. py:attribute:: _c
      :type:  float


   .. py:attribute:: _d
      :type:  float


   .. py:property:: a
      :type: float


      Sets the value of the property 'a', representing a specific geometric dimension of the trapezoidal concrete concept. The method accepts a numeric input, casts it to a float, and stores the result in the private attribute `_a`. This type conversion ensures that the internal state maintains floating-point precision for subsequent calculations, even if an integer or compatible numeric type is provided.

      :param value: The value to assign to the attribute, converted to a float.
      :type value: float


   .. py:property:: b
      :type: float


      Sets the dimension represented by 'b' for the trapezoidal concrete concept, typically corresponding to a width or base length. The method accepts a value, explicitly converts it to a float, and assigns it to the internal attribute `_b`. This ensures the underlying data type remains consistent, though providing a value that cannot be converted to a float will raise an error.

      :param value: The new value to assign to the b attribute.
      :type value: float


   .. py:property:: c
      :type: float


      Assigns the specified value to the property 'c', which corresponds to a geometric dimension of the trapezoidal concrete concept. The input is explicitly cast to a float to maintain numerical precision and stored in the private attribute `_c`. This setter modifies the object's state and may raise a TypeError or ValueError if the provided value cannot be converted to a float.

      :param value: The new value to assign to the property, converted to a float.
      :type value: float


   .. py:property:: d
      :type: float


      Sets the depth dimension of the trapezoidal concrete concept. This method serves as the setter for the `d` property, converting the provided value to a float and storing it in the private `_d` attribute. While this ensures the internal state is always a float, passing a non-numeric value will result in a `ValueError` or `TypeError` during the conversion process.

      :param value: The numeric value to assign to the attribute, converted to a float.
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


   .. py:attribute:: name
      :type:  str

      Updates the name of the Concept instance to the specified string value. This setter modifies the object's internal state by assigning the provided value to the private `_name` attribute, effectively replacing any previously stored name.

      :param value: The new name to assign to the object.
      :type value: str

