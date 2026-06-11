fuzzy_dl_owl2.fuzzydl.concept.concrete.trapezoidal_concrete_concept
===================================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.concrete.trapezoidal_concrete_concept



.. ── LLM-GENERATED DESCRIPTION START ──

Defines a trapezoidal concrete concept that models fuzzy membership degrees using a geometric shape defined by four distinct parameters.


Description
-----------


The implementation extends the base fuzzy concrete concept to represent a specific type of membership function characterized by a trapezoidal shape. By utilizing four distinct parameters to define the support and core intervals, the logic ensures that membership degrees transition linearly from zero to one and back to zero, creating a plateau of full certainty in the center. Initialization includes strict validation to guarantee that the geometric parameters are ordered correctly and that the definition domain fully encompasses the support interval, preventing invalid mathematical states. Beyond calculating membership for specific values, the class integrates with broader logical operations by delegating conjunctions, disjunctions, and negations to an operator handler, allowing these concepts to be combined within complex fuzzy expressions. Property accessors and a cloning mechanism are provided to manage the internal state and facilitate the creation of independent instances without side effects.

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

      Return a hash value for this object, computed from its string representation. This approach ensures that the hash value reflects the structural identity of the object without relying on cached values or additional methods. The hash is derived from the output of the `__str__` method, which provides a consistent and unique representation of the concept's structure. This implementation does not utilize any internal caching mechanism and directly computes the hash each time it is called.

      :return: An integer hash value representing the structural identity of this object.

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


      Returns the left-most breakpoint of the trapezoidal membership function, i.e. the start of the support interval where the membership degree begins rising from zero. The value is held internally as a float and is read without modifying the instance.

      :return: The lower support bound ``a`` of the trapezoid.

      :rtype: float


   .. py:property:: b
      :type: float


      Returns the second breakpoint of the trapezoidal membership function, i.e. the lower bound of the core plateau where the membership degree first reaches ``1``. The value is held internally as a float and is read without modifying the instance.

      :return: The lower core bound ``b`` of the trapezoid.

      :rtype: float


   .. py:property:: c
      :type: float


      Returns the third breakpoint of the trapezoidal membership function, i.e. the upper bound of the core plateau where the membership degree starts dropping below ``1``. The value is held internally as a float and is read without modifying the instance.

      :return: The upper core bound ``c`` of the trapezoid.

      :rtype: float


   .. py:property:: d
      :type: float


      Returns the right-most breakpoint of the trapezoidal membership function, i.e. the end of the support interval where the membership degree falls back to zero. The value is held internally as a float and is read without modifying the instance.

      :return: The upper support bound ``d`` of the trapezoid.

      :rtype: float


   .. py:attribute:: k1
      :type:  float


   .. py:attribute:: k2
      :type:  float


   .. py:attribute:: name
      :type:  str

