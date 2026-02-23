fuzzy_dl_owl2.fuzzydl.concept.concrete.triangular_concrete_concept
==================================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.concrete.triangular_concrete_concept



.. ── LLM-GENERATED DESCRIPTION START ──

Implements a fuzzy logic concept characterized by a triangular membership function to evaluate the degree of membership for numeric values within a specific domain.


Description
-----------


Software logic is provided to model fuzzy sets using a triangular membership function, which determines how strongly a specific numeric value belongs to a concept based on its position relative to defined support and core intervals. Strict geometric constraints are enforced during initialization to ensure that domain boundaries encompass the triangular support and that the vertices defining the triangle are correctly ordered to form a valid shape. Membership evaluation relies on linear interpolation, returning a degree of zero outside the support interval, rising linearly to a peak at the central vertex, and then falling back to zero. To facilitate integration within a larger fuzzy description logic system, the logic supports standard logical operations such as negation, conjunction, and disjunction by delegating to an operator handler, while also implementing object cloning and hashing for use in collections.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.concept.concrete.triangular_concrete_concept.TriangularConcreteConcept


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_concrete_triangular_concrete_concept_TriangularConcreteConcept.png
       :alt: UML Class Diagram for TriangularConcreteConcept
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **TriangularConcreteConcept**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_concrete_triangular_concrete_concept_TriangularConcreteConcept.pdf
       :alt: UML Class Diagram for TriangularConcreteConcept
       :align: center
       :width: 13.5cm
       :class: uml-diagram

       UML Class Diagram for **TriangularConcreteConcept**

.. py:class:: TriangularConcreteConcept(name: str, k1: float, k2: float, a: float, b: float, c: float)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_concrete_concept.FuzzyConcreteConcept`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.concept.concrete.triangular_concrete_concept.TriangularConcreteConcept
      :parts: 1
      :private-bases:


   This class implements a fuzzy logic concept characterized by a triangular membership function, defining how strongly a specific value belongs to the concept. It operates within a defined domain interval `[k1, k2]` and establishes a core satisfaction interval `[a, c]`, where the membership degree rises linearly from the lower bound `a` to a peak of 1.0 at `b`, then decreases linearly to the upper bound `c`. Users can instantiate this class with specific boundary parameters to model linguistic variables or fuzzy sets, and subsequently evaluate the membership degree of any given numeric value using the `get_membership_degree` method. The class enforces strict validation to ensure the parameters form a valid triangle and that the definition interval encompasses the satisfaction interval, raising an exception if these constraints are violated.

   :param k1: The lower bound of the domain interval [k1, k2] over which the concept is defined.
   :type k1: float
   :param k2: The upper bound of the domain interval [k1, k2] for which the concept is defined.
   :type k2: float
   :param _a: The lower bound of the support interval for the triangular membership function, representing the point where the membership degree begins to increase from zero.
   :type _a: float
   :param _b: The peak value of the triangular membership function where the concept is fully satisfied, corresponding to a membership degree of 1.
   :type _b: float
   :param _c: The upper bound of the interval for which the concept is satisfied, representing the point where the membership degree drops to zero. It must be greater than or equal to the peak value b.
   :type _c: float

   :raises FuzzyOntologyException: Raised if the provided parameters do not satisfy the constraints for a valid triangular function, specifically if the satisfaction interval bounds are not ordered ($a \le b \le c$) or if the definition interval $[k_1, k_2]$ does not fully encompass the satisfaction interval $[a, c]$ (i.e., $k_1 > a$ or $k_2 < c$).


   .. py:method:: __and__(value: Self) -> Self

      Implements the bitwise or logical AND operation for the class, allowing instances to be combined using the `&` operator. This method accepts another instance of the same type and delegates the calculation to the `OperatorConcept.and_` method to determine the result. The operation returns a new instance of the same type, representing the conjunction of the current instance and the provided value.

      :param value: The right-hand operand to perform the AND operation with.
      :type value: typing.Self

      :return: The result of the AND operation between this instance and the provided value.

      :rtype: typing.Self



   .. py:method:: __hash__() -> int

      Calculates a unique integer identifier for the instance based on its string representation. By delegating to the hash of the string form, this method ensures that objects with identical string outputs produce the same hash, thereby enabling the instance to be used as a dictionary key or stored within a set. It is important to note that the stability of the hash value is contingent upon the implementation of the `__str__` method; if the string representation changes, the hash will change as well.

      :return: An integer representing the hash of the object's string representation.

      :rtype: int



   .. py:method:: __neg__() -> fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_concrete_concept.FuzzyConcreteConcept

      Implements the unary negation operator to compute the logical complement of the current triangular concept. This method delegates the operation to `OperatorConcept.not_`, effectively inverting the membership function associated with the instance. It returns a new `FuzzyConcreteConcept` representing the negated value without modifying the original object.

      :return: The logical negation of the concept.

      :rtype: FuzzyConcreteConcept



   .. py:method:: __or__(value: Self) -> Self

      Implements the bitwise OR operator (`|`) to perform a logical disjunction between the current instance and another `TriangularConcreteConcept`. This method accepts a value of the same type and delegates the computation to the `or_` method of `OperatorConcept`. It returns a new instance of `TriangularConcreteConcept` representing the result of the operation, without modifying the original operands.

      :param value: The right-hand operand for the OR operation, which must be an instance of the same class.
      :type value: typing.Self

      :return: The result of the OR operation between this instance and the provided value.

      :rtype: typing.Self



   .. py:method:: clone() -> Self

      Creates and returns a distinct copy of the current `TriangularConcreteConcept` instance. The new object is instantiated with the exact same values for the `name`, `k1`, `k2`, `a`, `b`, and `c` attributes as the original. This operation does not modify the state of the existing object, ensuring that the original and the clone are independent entities.

      :return: A new instance of the class initialized with the same attributes as the current object.

      :rtype: typing.Self



   .. py:method:: compute_name() -> str

      Generates a standardized string identifier for the triangular concept based on its current configuration. This method formats the instance attributes `k1`, `k2`, `a`, `b`, and `c` into a string that mimics a function invocation syntax. The operation is read-only and produces a unique textual representation of the object's parameters without causing any side effects.

      :return: A string representing the name of the triangular distribution, formatted with its parameters.

      :rtype: str



   .. py:method:: get_membership_degree(x: float) -> float

      Calculates the membership degree of a specific value `x` within the triangular fuzzy set represented by this concept. The membership is determined by the relative position of `x` between the three defining parameters `a` (start), `b` (peak), and `c` (end). If `x` lies outside the interval $[a, c]$, the method returns 0.0. For values in the rising interval between `a` and `b`, the result is a linear interpolation from 0.0 to 1.0, while values in the falling interval between `b` and `c` yield a linear interpolation from 1.0 back to 0.0. This method performs a pure calculation without modifying the object's state.

      :param x: The input value for which the membership degree is calculated.
      :type x: float

      :return: The degree of membership of `x` in the triangular fuzzy set, ranging from 0.0 (no membership) to 1.0 (full membership).

      :rtype: float



   .. py:attribute:: _a
      :type:  float


   .. py:attribute:: _b
      :type:  float


   .. py:attribute:: _c
      :type:  float


   .. py:property:: a
      :type: float


      Sets the value of the property 'a' for the TriangularConcreteConcept instance. The provided value is converted to a float and stored in the private attribute `_a`, ensuring that the internal representation is always a floating-point number. This method will raise an exception if the input cannot be cast to a float.

      :param value: The new value to assign to the attribute, converted to a float.
      :type value: float


   .. py:property:: b
      :type: float


      Updates the internal state of the instance by setting the value of the property 'b'. The method accepts a single argument, which is explicitly converted to a float before being assigned to the private attribute '_b'. This conversion ensures type consistency, though it may raise a ValueError or TypeError if the provided input cannot be parsed as a float.

      :param value: The new value to be stored, converted to a float.
      :type value: float


   .. py:property:: c
      :type: float


      Sets the value of the property 'c' for the triangular concept instance. This method accepts a numeric input, coerces it to a float, and assigns it to the internal `_c` attribute. It modifies the object's state and may raise an exception if the input cannot be successfully converted to a floating-point number.

      :param value: The new value for the attribute, converted to a float.
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

