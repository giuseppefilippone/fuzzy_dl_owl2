fuzzy_dl_owl2.fuzzydl.concept.concrete.linear_concrete_concept
==============================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.concrete.linear_concrete_concept



.. ── LLM-GENERATED DESCRIPTION START ──

A concrete implementation of a fuzzy concept that utilizes a piecewise linear membership function defined over a normalized domain.


Description
-----------


This software component models a specific type of fuzzy concept characterized by a piecewise linear membership function operating on a normalized domain ranging from zero to one. The mathematical behavior is governed by a "knee" point defined by parameters ``a`` and ``b``, which creates a linear ramp from the origin to the knee and a second ramp from the knee to full membership, effectively ignoring the interval bounds ``k1`` and ``k2`` during the actual calculation of the membership degree. Validation logic ensures that the definition interval and the knee point adhere to specific constraints, such as requiring the lower bound to be less than or equal to the knee position and the membership degree at the knee to not exceed one. Beyond calculating membership degrees through linear interpolation, the implementation supports standard fuzzy logic operations like negation, conjunction, and disjunction by delegating these tasks to a central operator handler. It also provides functionality for cloning instances and generating a canonical string representation based on its defining parameters.

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

      Return a hash value for this object, computed from its string representation. This approach ensures that the hash value reflects the structural identity of the object without relying on cached values or additional methods. The hash is derived from the output of the `__str__` method, which provides a consistent and unique representation of the concept's structure. This implementation does not utilize any internal caching mechanism and directly computes the hash each time it is called.

      :return: An integer hash value representing the structural identity of this object.

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


      Returns the x-coordinate of the knee of this piecewise-linear membership function, i.e. the threshold on the normalized domain at which the slope of the ramp changes. The value is held internally as a float and is read without modifying the instance.

      :return: The knee position ``a`` of the linear function.

      :rtype: float


   .. py:property:: b
      :type: float


      Returns the membership degree reached at the knee ``a`` of this piecewise-linear function, i.e. the y-coordinate of the breakpoint that fixes the slope of the two linear segments. The value is held internally as a float and is read without modifying the instance.

      :return: The membership degree ``b`` at the knee.

      :rtype: float


   .. py:attribute:: k1
      :type:  float


   .. py:attribute:: k2
      :type:  float

