fuzzy_dl_owl2.fuzzydl.concept.concrete.crisp_concrete_concept
=============================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.concrete.crisp_concrete_concept



.. ── LLM-GENERATED DESCRIPTION START ──

A crisp concrete concept implementation that applies binary membership logic to determine if a value lies within a specified satisfaction interval.


Description
-----------


The software defines a specialized concept that operates within a fuzzy logic environment but enforces strict binary membership, effectively distinguishing between complete satisfaction and non-satisfaction based on numerical intervals. By establishing a validity domain defined by boundaries ``k1`` and ``k2``, alongside a narrower satisfaction interval bounded by ``a`` and ``b``, the implementation ensures that any evaluated value yields a membership degree of 1.0 only if it falls strictly within the inner range, returning 0.0 otherwise. During initialization, rigorous validation logic enforces structural integrity by verifying that the satisfaction interval is properly contained within the validity domain, raising errors if the bounds are misconfigured. To facilitate complex logical reasoning, the class integrates with an operator framework to support negation, conjunction, and disjunction, allowing these crisp concepts to be combined or manipulated while maintaining their distinct binary characteristics.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.concept.concrete.crisp_concrete_concept.CrispConcreteConcept


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_concrete_crisp_concrete_concept_CrispConcreteConcept.png
       :alt: UML Class Diagram for CrispConcreteConcept
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **CrispConcreteConcept**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_concrete_crisp_concrete_concept_CrispConcreteConcept.pdf
       :alt: UML Class Diagram for CrispConcreteConcept
       :align: center
       :width: 12.1cm
       :class: uml-diagram

       UML Class Diagram for **CrispConcreteConcept**

.. py:class:: CrispConcreteConcept(name: str, k1: float, k2: float, a: float, b: float)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_concrete_concept.FuzzyConcreteConcept`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.concept.concrete.crisp_concrete_concept.CrispConcreteConcept
      :parts: 1
      :private-bases:


   This class models a crisp concrete concept within a fuzzy logic framework, implementing a binary membership function that distinguishes strictly between satisfaction and non-satisfaction. It is defined by a validity interval [k1, k2] representing the domain of the concept, and a nested satisfaction interval [a, b] where the concept holds true. When evaluating a specific value, the class returns a membership degree of 1.0 if the value falls within the satisfaction interval [a, b] and 0.0 otherwise. The initialization process includes validation logic to ensure that the satisfaction interval is valid and fully contained within the validity interval, raising a ValueError if these constraints are violated. Furthermore, the class supports logical operations such as negation, conjunction, and disjunction, allowing for the composition of complex concepts.

   :param k1: Lower bound of the definition interval [k1, k2], representing the minimum value for which the concept is valid.
   :type k1: float
   :param k2: The upper bound of the interval defining the domain of the concept.
   :type k2: float
   :param _a: Stores the lower bound of the interval for which the concept is satisfied, defining the start of the range where the membership degree is 1.
   :type _a: float
   :param _b: The upper bound of the interval for which the concept is satisfied.
   :type _b: float

   :raises ValueError: Raised when the satisfaction interval [a, b] is invalid or not contained within the definition interval [k1, k2]. This happens if a > b, a < k1, or b > k2.


   .. py:method:: __and__(value: Self) -> Self

      Performs a logical conjunction or intersection between the current instance and another concept of the same type. This method enables the use of the bitwise AND operator (`&`) to combine concepts, delegating the underlying logic to the `OperatorConcept.and_` static method. It returns a new instance of the same class representing the result of the operation, leaving the original operands unchanged.

      :param value: The right-hand operand to perform the AND operation with.
      :type value: typing.Self

      :return: A new instance representing the logical conjunction of this concept and the provided value.

      :rtype: typing.Self



   .. py:method:: __hash__() -> int

      Return a hash value for this object, computed from its string representation. This approach ensures that the hash value reflects the structural identity of the object without relying on cached values or additional methods. The hash is derived from the output of the `__str__` method, which provides a consistent and unique representation of the concept's structure. This implementation does not utilize any internal caching mechanism and directly computes the hash each time it is called.

      :return: An integer hash value representing the structural identity of this object.

      :rtype: int



   .. py:method:: __neg__() -> fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_concrete_concept.FuzzyConcreteConcept

      Implements the unary negation operator to compute the logical complement of the concept. This operation delegates to `OperatorConcept.not_` to generate a new representation of the negated concept. The result is returned as a `FuzzyConcreteConcept`, indicating that the negation of a crisp concept is handled within the fuzzy logic framework, potentially promoting the type to accommodate degrees of truth or standardizing the output of logical operations. This method does not modify the current instance in place.

      :return: The logical negation of the current concept.

      :rtype: FuzzyConcreteConcept



   .. py:method:: __or__(value: Self) -> Self

      Performs a logical disjunction between the current concept and another value of the same type, enabling the use of the bitwise OR operator (`|`). This operation returns a new instance representing the union or combination of the two operands, with the specific calculation logic delegated to the `OperatorConcept.or_` method. The method expects the input value to be compatible with the current instance type to ensure the operation is valid.

      :param value: Another instance of the same type to combine with the current instance using the OR operation.
      :type value: typing.Self

      :return: The result of the OR operation between this instance and the provided value.

      :rtype: typing.Self



   .. py:method:: clone() -> Self

      Creates and returns a distinct copy of the current `CrispConcreteConcept` instance. The new object is initialized with the same values for `name`, `k1`, `k2`, `a`, and `b` as the original. This operation has no side effects on the source object, ensuring that modifications to the clone do not affect the original instance.

      :return: A new instance of the class initialized with the same attribute values as the current instance.

      :rtype: typing.Self



   .. py:method:: compute_name() -> str

      Generates a standardized string identifier for the concept instance by interpolating its internal parameters into a specific format. The returned string follows the pattern "crisp(k1, k2, a, b)", where the placeholders are replaced by the string representations of the corresponding attributes `k1`, `k2`, `a`, and `b`. This method performs a read-only operation and does not modify the object's state, though the resulting string's content is dependent on the `__str__` implementation of the stored parameter values.

      :return: A string representation of the object's configuration in the format 'crisp(k1, k2, a, b)'.

      :rtype: str



   .. py:method:: get_membership_degree(x: float) -> float

      Calculates the membership degree of a specific value within the context of this crisp concept. The membership is determined by checking if the input value falls within the closed interval defined by the concept's lower and upper bounds. If the value lies between these bounds (inclusive), the method returns 1.0 to signify full membership; otherwise, it returns 0.0. This method does not modify the state of the object.

      :param x: The input value to evaluate for membership.
      :type x: float

      :return: The degree of membership of the input value, returning 1.0 if it lies within the interval [a, b] and 0.0 otherwise.

      :rtype: float



   .. py:attribute:: _a
      :type:  float


   .. py:attribute:: _b
      :type:  float


   .. py:property:: a
      :type: float


      Returns the lower bound of the crisp satisfaction interval ``[a, b]``, i.e. the smallest value for which the membership degree is ``1``. The value is held internally as a float and is read without modifying the instance.

      :return: The lower bound ``a`` of the satisfaction interval.

      :rtype: float


   .. py:property:: b
      :type: float


      Returns the upper bound of the crisp satisfaction interval ``[a, b]``, i.e. the largest value for which the membership degree is ``1``. The value is held internally as a float and is read without modifying the instance.

      :return: The upper bound ``b`` of the satisfaction interval.

      :rtype: float


   .. py:attribute:: k1
      :type:  float


   .. py:attribute:: k2
      :type:  float

