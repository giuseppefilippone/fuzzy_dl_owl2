fuzzy_dl_owl2.fuzzydl.concept.concrete.left_concrete_concept
============================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.concrete.left_concrete_concept





.. ── LLM-GENERATED DESCRIPTION START ──

A left-shoulder fuzzy concrete concept that grants full membership to concrete values up to a first breakpoint and tapers linearly to zero at a second one, serving as a building block for fuzzy description-logic knowledge bases.


Description
-----------


LeftConcreteConcept specialises FuzzyConcreteConcept to model the classic left-shoulder membership function, in which small values of a concrete domain are fully compatible with the concept and larger ones progressively less so. The shape is pinned down by a validity interval [*k1*, *k2*] together with a satisfaction interval [*a*, *b*]: inputs at or below *a* score 1.0, inputs at or above *b* score 0.0, and anything strictly in between is interpolated linearly, producing a descending ramp. Construction validates the ordering *k1* ≤ *a* ≤ *b* ≤ *k2* and reports an error whenever the constraints are violated, so every instance is guaranteed to describe a well-formed shoulder; the breakpoints are additionally exposed as float properties, and a canonical name of the form left-shoulder(k1, k2, a, b) is derived from the parameters to support consistent printing and structural comparison.

Because fuzzy concepts are routinely combined while authoring a knowledge base, the standard Python operators are overloaded: unary minus, ``&``, and ``|`` delegate to OperatorConcept's negation, conjunction, and disjunction helpers, returning new composite expressions while leaving the operands unmodified. Hashing is computed from the concept's name, domain bounds, and breakpoints rather than from object identity, so structurally identical concepts behave correctly as dictionary keys and set members during reasoning. A cloning operation produces an independent copy carrying the same parameters, which supports the copy-and-transform patterns used elsewhere in the framework. Together these decisions yield a small, value-like type that plugs directly into the wider machinery for reasoning over fuzzy concrete domains.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.concept.concrete.left_concrete_concept.LeftConcreteConcept


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_concrete_left_concrete_concept_LeftConcreteConcept.png
       :alt: UML Class Diagram for LeftConcreteConcept
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **LeftConcreteConcept**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_concrete_left_concrete_concept_LeftConcreteConcept.pdf
       :alt: UML Class Diagram for LeftConcreteConcept
       :align: center
       :width: 12.1cm
       :class: uml-diagram

       UML Class Diagram for **LeftConcreteConcept**

.. py:class:: LeftConcreteConcept(name: str, k1: float, k2: float, a: float, b: float)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_concrete_concept.FuzzyConcreteConcept`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.concept.concrete.left_concrete_concept.LeftConcreteConcept
      :parts: 1
      :private-bases:


   This class models a left shoulder fuzzy set, representing a concept where membership is maximized at lower values and decreases linearly towards zero. It is defined by a domain of validity `[k1, k2]` and a satisfaction interval `[a, b]`, where membership is 1 for inputs less than or equal to `a`, 0 for inputs greater than or equal to `b`, and linearly interpolated for values in between. To use this class, instantiate it with a name and the four float parameters, ensuring that `k1` is less than or equal to `a` and `k2` is greater than or equal to `b` to satisfy validation constraints. Once instantiated, the membership degree of a specific value can be retrieved, and the object supports logical operations like negation, conjunction, and disjunction through standard Python operators.

   :param k1: The lower bound of the domain interval [k1, k2] over which the concept is defined.
   :type k1: float
   :param k2: The upper bound of the interval [k1, k2] defining the domain of the concept.
   :type k2: float
   :param _a: The lower bound of the transition interval, defining the point at which the membership degree begins to decrease from 1.0.
   :type _a: float
   :param _b: The upper bound of the satisfaction interval, representing the point at which the membership degree becomes zero.
   :type _b: float


   .. py:method:: __and__(value: Self) -> Self

      Implements the bitwise AND operation (`&`) for the concept, calculating the intersection between the current instance and another instance of the same type. This method delegates the actual computation to `OperatorConcept.and_` and returns a new instance representing the result, ensuring that the original operands remain unmodified. It enables the combination of concepts to identify shared properties or elements.

      :param value: The other operand to perform the AND operation with.
      :type value: typing.Self

      :return: The result of the bitwise AND operation between the instance and the provided value.

      :rtype: typing.Self



   .. py:method:: __hash__() -> int

      Return a hash value for this object, computed from its string representation. This approach ensures that the hash value reflects the structural identity of the object without relying on cached values or additional methods. The hash is derived from the output of the `__str__` method, which provides a consistent and unique representation of the concept's structure. This implementation does not utilize any internal caching mechanism and directly computes the hash each time it is called.

      :return: An integer hash value representing the structural identity of this object.

      :rtype: int



   .. py:method:: __neg__() -> fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_concrete_concept.FuzzyConcreteConcept

      Implements the unary negation operator, allowing the concept to be inverted using the minus sign. This method computes the logical negation of the current instance by delegating to the `OperatorConcept.not_` static method. The operation returns a new `FuzzyConcreteConcept` representing the complement of the original concept, leaving the source instance unmodified.

      :return: A new concept representing the logical negation of the current concept.

      :rtype: FuzzyConcreteConcept



   .. py:method:: __or__(value: Self) -> Self

      Implements the bitwise OR operation for the concept, enabling the use of the pipe operator (`|`) to combine the current instance with another value of the same type. This method delegates the underlying logic to the `OperatorConcept.or_` static method, which calculates the result. The operation returns a new instance of `LeftConcreteConcept` representing the union or disjunction of the operands, ensuring that the original objects remain unmodified.

      :param value: The right-hand operand to combine with the current instance using the OR operation.
      :type value: typing.Self

      :return: The result of the OR operation between the current instance and the provided value.

      :rtype: typing.Self



   .. py:method:: clone() -> Self

      Creates and returns a new instance that is a copy of the current object. The clone is instantiated with the same values for `name`, `k1`, `k2`, `a`, and `b` as the original. This method does not modify the existing instance, though the resulting clone may share references to mutable objects if the constructor does not perform deep copying.

      :return: A new instance of the class with the same attributes as the current object.

      :rtype: typing.Self



   .. py:method:: compute_name() -> str

      Generates a canonical string representation of the concept by formatting the instance's defining parameters into a specific pattern. The returned string follows the format "left-shoulder(k1, k2, a, b)", utilizing the values of the attributes `k1`, `k2`, `a`, and `b`. This method is read-only and does not modify the state of the object.

      :return: A string representation of the left-shoulder function name, including its parameters.

      :rtype: str



   .. py:method:: get_membership_degree(value: float) -> float

      Computes the degree of membership for a given numerical value within a left-shoulder fuzzy set defined by the parameters `a` and `b`. The function returns 1.0 for values less than or equal to `a`, indicating full membership, and returns 0.0 for values greater than or equal to `b`, indicating no membership. For values falling strictly between `a` and `b`, the method performs a linear interpolation to determine a partial membership value between 0.0 and 1.0. This implementation assumes that `a` is strictly less than `b` to avoid division by zero errors during the interpolation step.

      :param value: The numeric input value for which to calculate the membership degree.
      :type value: float

      :return: The degree of membership of the input value, ranging from 0.0 to 1.0. Returns 1.0 for values at or below the lower bound, 0.0 for values at or above the upper bound, and a linearly interpolated value for those in between.

      :rtype: float



   .. py:attribute:: _a
      :type:  float


   .. py:attribute:: _b
      :type:  float


   .. py:property:: a
      :type: float


      Returns the left breakpoint of this left-shoulder membership function, i.e. the point up to which the degree is ``1`` and beyond which it starts decreasing linearly toward zero. The value is held internally as a float and is read without modifying the instance.

      :return: The breakpoint ``a`` where the degree begins to fall from ``1``.

      :rtype: float


   .. py:property:: b
      :type: float


      Returns the right breakpoint of this left-shoulder membership function, i.e. the point at which the degree reaches zero. The value is held internally as a float and is read without modifying the instance.

      :return: The breakpoint ``b`` where the degree reaches ``0``.

      :rtype: float


   .. py:attribute:: k1
      :type:  float


   .. py:attribute:: k2
      :type:  float
