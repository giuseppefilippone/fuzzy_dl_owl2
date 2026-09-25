fuzzy_dl_owl2.fuzzydl.concept.concrete.triangular_concrete_concept
==================================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.concrete.triangular_concrete_concept



.. ── LLM-GENERATED DESCRIPTION START ──

Defines a fuzzy concrete concept whose membership degree follows a triangular function, rising linearly from zero at ``a`` to a peak of one at ``b`` and falling back to zero at ``c``, all contained within an outer domain interval ``[k1, k2]``.


Description
-----------


TriangularConcreteConcept extends FuzzyConcreteConcept to model linguistic terms such as "approximately x" or "medium" in a fuzzy description-logic ontology, where the degree to which a numeric value belongs to the concept is given by a piecewise-linear triangular shape. The constructor enforces the geometric constraints required for a well-formed triangle — the breakpoints must satisfy ``a ≤ b ≤ c``, and the domain bounds must enclose the support interval (``k1 ≤ a`` and ``k2 ≥ c``) — raising a FuzzyOntologyException when these are violated, so malformed fuzzy sets are rejected at creation time rather than silently producing wrong degrees later. Membership evaluation is a pure, side-effect-free computation: values outside ``[a, c]`` score 0.0, values between ``a`` and ``b`` are interpolated linearly up to 1.0, and values between ``b`` and ``c`` are interpolated back down to 0. The three breakpoints are exposed through read/write properties that coerce assignments to floats, keeping the internal representation consistent even after construction.

Instances are designed to behave like values rather than mutable identities: they can be cloned into fully independent copies, they generate a canonical ``triangular(k1, k2, a, b, c)`` string for naming and serialization, and their hash is derived from the numeric parameters so that structurally identical triangles act as interchangeable dictionary keys. Logical composition is supported through operator overloading — unary negation, ``&``, and ``|`` all delegate to the corresponding helpers on OperatorConcept — which lets triangular concepts be combined into compound fuzzy expressions while leaving the original operands unmodified.

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

      Return a hash value for this object, computed from its string representation. This approach ensures that the hash value reflects the structural identity of the object without relying on cached values or additional methods. The hash is derived from the output of the `__str__` method, which provides a consistent and unique representation of the concept's structure. This implementation does not utilize any internal caching mechanism and directly computes the hash each time it is called.

      :return: An integer hash value representing the structural identity of this object.

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


      Returns the left breakpoint of the triangular membership function, i.e. the start of the support interval where the membership degree begins rising from zero toward the peak. The value is held internally as a float and is read without modifying the instance.

      :return: The lower support bound ``a`` of the triangle.

      :rtype: float


   .. py:property:: b
      :type: float


      Returns the peak breakpoint of the triangular membership function, i.e. the single point where the membership degree reaches its maximum value of ``1``. The value is held internally as a float and is read without modifying the instance.

      :return: The peak ``b`` of the triangle.

      :rtype: float


   .. py:property:: c
      :type: float


      Returns the right breakpoint of the triangular membership function, i.e. the end of the support interval where the membership degree falls back to zero. The value is held internally as a float and is read without modifying the instance.

      :return: The upper support bound ``c`` of the triangle.

      :rtype: float


   .. py:attribute:: k1
      :type:  float


   .. py:attribute:: k2
      :type:  float

