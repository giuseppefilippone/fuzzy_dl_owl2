fuzzy_dl_owl2.fuzzydl.concept.concrete.linear_concrete_concept
==============================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.concrete.linear_concrete_concept



.. ── LLM-GENERATED DESCRIPTION START ──

A fuzzy concrete concept whose membership function is a two-segment linear ramp over a feature domain, rising from degree zero at the lower bound to degree one at the upper bound through a configurable knee point.


Description
-----------


``LinearConcreteConcept`` expresses a fuzzy linguistic value over a concrete feature interval ``[k1, k2]``: membership is 0 at and below ``k1``, climbs linearly to a knee point ``(a, b)``, and then climbs linearly again to 1 at and above ``k2``. The shape is deliberately chosen to coincide exactly with the constraints that the MILP encoding of the concept enforces in the knowledge base, so evaluating a degree in Python reproduces the same value the solver's linear equations imply. Two deliberate divergences from the original Java implementation are documented inline: the constructor rejects degenerate configurations (an empty or reversed domain, a knee coinciding with a domain bound, or a knee degree outside ``[0, 1]``) because a vertical ramp has no well-defined slope, and membership evaluation is carried out in the feature's own units rather than assuming a normalised ``[0, 1]`` domain, which fixes a latent defect in the Java version that only produced correct results when the domain happened to be ``[0, 1]``.

The knee coordinates are exposed through float-coercing properties so they can be inspected and adjusted, while the underlying parameters remain plain floats. The concept integrates with the wider fuzzy description-logic framework by delegating negation, conjunction, and disjunction — exposed through the unary minus, ``&``, and ``|`` operators — to ``OperatorConcept``, which builds new composite concepts and leaves the operands untouched. Structural identity is provided by a hash computed from the name, the domain bounds, the knee, and the concept type, allowing instances to participate safely in sets and dictionaries, and cloning yields an independent copy carrying the same parameters. A deterministic, human-readable label of the form "linear(k1, k2, a, b)" is generated from the current state, giving the concept a stable printable identity for logging and debugging.

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


   This class models a fuzzy concept characterized by a piecewise linear membership function on the feature domain `[k1, k2]`. The function is defined by a "knee" point `(a, b)`, with `a` in the units of the feature and `b` the membership degree reached at `a`: a linear ramp from `(k1, 0)` to `(a, b)` and a second linear ramp from `(a, b)` to `(k2, 1)`. This is the same shape the MILP encoding of the concept enforces. Instantiate it with a name and the four float parameters, with `k1 < a < k2` and `0 <= b <= 1`; the membership degree of a value can then be retrieved with `get_membership_degree`, and the object supports the usual fuzzy operations (negation, conjunction, disjunction).

   :param k1: Lower bound of the feature domain; the membership degree is 0 at and below `k1`.
   :type k1: float
   :param k2: Upper bound of the feature domain; the membership degree is 1 at and above `k2`.
   :type k2: float
   :param _a: Abscissa of the knee, in feature units, strictly between `k1` and `k2`.
   :type _a: float
   :param _b: The membership degree at the knee `a`, in `[0, 1]`.
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

      Calculates the degree of membership of a feature value: 0.0 at and below `k1`, a linear ramp from `(k1, 0)` to the knee `(a, b)`, a second linear ramp from `(a, b)` to `(k2, 1)`, and 1.0 at and above `k2`. This is exactly the function the MILP encoding of the concept enforces, expressed in the units of the feature. This method does not modify the state of the object.

      :param value: The feature value to evaluate, in the units of the feature domain `[k1, k2]`.
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

