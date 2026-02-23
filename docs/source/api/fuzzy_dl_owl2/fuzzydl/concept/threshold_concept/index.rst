fuzzy_dl_owl2.fuzzydl.concept.threshold_concept
===============================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.threshold_concept



.. ── LLM-GENERATED DESCRIPTION START ──

Implements a logical construct for applying numerical threshold constraints to concepts within a fuzzy description logic framework.


Description
-----------


The software defines a specialized entity that enforces numerical boundaries on the satisfaction degree of a nested concept, supporting both positive and negative threshold conditions to determine fulfillment based on a specific weight. By inheriting from base concept interfaces, it integrates seamlessly into a larger fuzzy logic system, allowing for complex expressions involving conjunctions, disjunctions, and negations through operator overloading that delegates to external operator handlers. Design choices include static factory methods for convenient instantiation of specific threshold types and a delegation pattern for retrieving atomic concepts and roles directly from the encapsulated inner concept. The implementation ensures that structural modifications, such as cloning or recursively replacing sub-concepts, preserve the specific weight and constraint type while maintaining the integrity of the logical hierarchy.

.. ── LLM-GENERATED DESCRIPTION END ──

Attributes
----------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.concept.threshold_concept.NegThreshold
   fuzzy_dl_owl2.fuzzydl.concept.threshold_concept.PosThreshold


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.concept.threshold_concept.ThresholdConcept


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_threshold_concept_ThresholdConcept.png
       :alt: UML Class Diagram for ThresholdConcept
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **ThresholdConcept**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_threshold_concept_ThresholdConcept.pdf
       :alt: UML Class Diagram for ThresholdConcept
       :align: center
       :width: 11.9cm
       :class: uml-diagram

       UML Class Diagram for **ThresholdConcept**

.. py:class:: ThresholdConcept(c_type: fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType, c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, weight: float)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.concept.concept.Concept`, :py:obj:`fuzzy_dl_owl2.fuzzydl.concept.interface.has_concept_interface.HasConceptInterface`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.concept.threshold_concept.ThresholdConcept
      :parts: 1
      :private-bases:


   This class models a threshold constraint applied to a base concept within a graded or fuzzy logic framework, determining satisfaction based on a numerical boundary. It evaluates whether the degree of fulfillment of a nested concept meets a specific weight, supporting both positive thresholds (greater than or equal to) and negative thresholds (less than or equal to). Users can construct instances via the standard constructor or convenient static factory methods designed for specific threshold directions. Functionally, it integrates into a larger hierarchy of logical constructs, enabling standard operations such as conjunction, disjunction, and negation, while delegating the retrieval of atomic concepts and roles to the encapsulated inner concept.

   :param _weight: Numeric threshold value used to compare against the satisfaction degree of the nested concept.
   :type _weight: float
   :param name: The computed string representation of the threshold concept, formatted as `([>= w] C)` or `([<= w] C)` and generated automatically upon initialization.
   :type name: typing.Any


   .. py:method:: __and__(value: Self) -> Self

      Performs a logical conjunction between the current instance and another value of the same type using the bitwise AND operator. This operation delegates the underlying logic to `OperatorConcept.and_`, returning a new instance that represents the combination of the two concepts without modifying the original operands. The method is designed to work with compatible types, ensuring that the resulting object adheres to the same conceptual constraints as the inputs.

      :param value: The right-hand operand for the AND operation, which must be an instance of the same type.
      :type value: typing.Self

      :return: The result of the conjunction (AND operation) between this instance and the provided value.

      :rtype: typing.Self



   .. py:method:: __hash__() -> int

      Computes the hash value for the instance by hashing its string representation, enabling the object to be used as a key in dictionaries or as a member of sets. The implementation delegates to the built-in hash function applied to the result of `str(self)`. Note that if the object is mutable and its string representation changes over time, the hash value will also change, which can lead to unexpected behavior if the object is modified while stored in a hash-based collection.

      :return: An integer hash value computed from the string representation of the object.

      :rtype: int



   .. py:method:: __neg__() -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept

      Implements the unary negation operator for the concept, enabling the use of the minus sign to invert its logical state. This method returns a new `Concept` instance representing the logical negation of the current `ThresholdConcept` by delegating to the `OperatorConcept.not_` method. The operation is non-destructive, leaving the original concept unchanged while producing a derived expression that signifies the opposite condition.

      :return: The logical negation of the concept.

      :rtype: Concept



   .. py:method:: __or__(value: Self) -> Self

      Performs a logical OR operation between the current concept and another concept, enabling the use of the pipe operator (`|`) to combine them. This method delegates the combination logic to `OperatorConcept.or_`, returning a new composite concept that represents the union of the two operands. The operation is side-effect free, as it does not modify the original instances but produces a new instance of the same type.

      :param value: The right-hand operand to combine with the current instance using the OR operation.
      :type value: typing.Self

      :return: A new instance representing the result of the OR operation between the current instance and the provided value.

      :rtype: typing.Self



   .. py:method:: clone() -> Self

      Creates and returns a new instance of `ThresholdConcept` that duplicates the state of the current object. The returned object is initialized with the same `type`, `curr_concept`, and `weight` attributes as the original. This method ensures that the returned instance is independent of the source, meaning modifications to the clone will not affect the original object, although it performs a shallow copy of the internal attributes.

      :return: A new instance of the class initialized with the same attributes as the current object.

      :rtype: typing.Self



   .. py:method:: compute_atomic_concepts() -> set[fuzzy_dl_owl2.fuzzydl.concept.concept.Concept]

      Computes the set of atomic concepts that constitute the underlying concept stored in `curr_concept`. This method acts as a delegation wrapper, forwarding the call to the `compute_atomic_concepts` method of the `curr_concept` attribute to retrieve the fundamental, indivisible components of the concept. The result is returned as a set of `Concept` objects, ensuring uniqueness among the atomic constituents.

      :return: A set of the atomic concepts that constitute the current concept.

      :rtype: set[Concept]



   .. py:method:: compute_name() -> Optional[str]

      Generates a formatted string representation of the threshold condition based on the concept's type and weight. For positive thresholds, the output indicates a greater-than-or-equal-to relationship, while negative thresholds indicate a less-than-or-equal-to relationship, embedding the underlying concept name within the result. If the concept type does not correspond to a defined threshold category, the method returns None.

      :return: A formatted string representing the concept with its threshold condition and weight for positive or negative threshold types, or None if the type is not a threshold.

      :rtype: typing.Optional[str]



   .. py:method:: get_roles() -> set[str]

      Retrieves the set of role identifiers associated with the underlying concept currently referenced by the instance. This method delegates the operation to the `get_roles` method of the internal `curr_concept` object, returning the resulting set of strings directly. Because the return value is a set, callers should be aware that modifying the returned collection may inadvertently alter the state of the underlying concept if the delegated method returns a direct reference to internal data.

      :return: A set of strings representing the roles associated with the current concept.

      :rtype: set[str]



   .. py:method:: neg_threshold(w: float, c: Self) -> Self
      :staticmethod:


      This static method serves as a factory to instantiate a `ThresholdConcept` specifically defined as a negative threshold. It accepts a weight `w` and a concept `c`, passing them to the constructor along with the `NEG_THRESHOLD` type identifier. The method has no side effects and simply returns a new instance; any validation or errors raised will depend on the underlying `ThresholdConcept` constructor logic.

      :param w: The weight or value defining the negative threshold.
      :type w: float
      :param c: The concept to which the negative threshold is applied.
      :type c: typing.Self

      :return: A new ThresholdConcept instance representing a negative threshold with the specified weight and concept.

      :rtype: typing.Self



   .. py:method:: pos_threshold(w: float, c: Self) -> Self
      :staticmethod:


      Constructs a new `ThresholdConcept` instance representing a positive threshold condition. This static method acts as a factory, accepting a floating-point weight and an existing concept instance to wrap. It initializes the new object with the `POS_THRESHOLD` type, associating the provided weight and concept with the resulting entity without modifying the original inputs.

      :param w: The numerical value defining the threshold.
      :type w: float
      :param c: The concept to which the positive threshold is applied.
      :type c: typing.Self

      :return: A new instance representing a positive threshold concept, configured with the provided weight and concept.

      :rtype: typing.Self



   .. py:method:: replace(a: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept

      Recursively replaces concept `a` with concept `c` within the nested `curr_concept` and transforms the current node into a new `ThresholdConcept` based on the type of `c`. If the replacement concept `c` is a positive threshold, the method returns a positive threshold concept; if it is a negative threshold, it returns a negative threshold concept. The original weight of the current node is preserved in the returned instance, ensuring that the structural hierarchy is maintained while the substitution is applied to the underlying concept.

      :param a: The target to be replaced by `c`.
      :type a: Concept
      :param c: The concept to replace `a` with.
      :type c: Concept

      :return: A new `Concept` instance resulting from replacing the sub-concept `a` with `c` within the current structure, preserving the current weight.

      :rtype: Concept



   .. py:attribute:: _weight
      :type:  float


   .. py:attribute:: name
      :value: '([>= Uninferable] Uninferable)'


      Updates the name of the Concept instance to the specified string value. This setter modifies the object's internal state by assigning the provided value to the private `_name` attribute, effectively replacing any previously stored name.

      :param value: The new name to assign to the object.
      :type value: str


   .. py:property:: weight
      :type: float


      Sets the weight of the `ThresholdConcept` instance to the specified floating-point value. This method updates the internal `_weight` attribute, effectively modifying the object's state without performing additional validation or triggering side effects beyond the assignment. It allows the weight to be redefined dynamically, accepting any float provided as an argument.

      :param value: The new weight value.
      :type value: float


.. py:data:: NegThreshold

.. py:data:: PosThreshold
