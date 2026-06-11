fuzzy_dl_owl2.fuzzydl.concept.ext_threshold_concept
===================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.ext_threshold_concept



.. ── LLM-GENERATED DESCRIPTION START ──

Implements a logical construct for fuzzy description logic that applies a variable-based threshold to the satisfaction degree of a nested concept.


Description
-----------


The software models a specific type of fuzzy logic constraint where the satisfaction degree of a base concept is compared against a dynamic threshold represented by a solver variable. Unlike fixed thresholds, this approach allows the reasoning engine to determine the optimal boundary value during the solving process, supporting both positive and negative logical conditions. By inheriting from core concept interfaces, the implementation integrates seamlessly into the broader description logic framework while maintaining the ability to nest complex conceptual structures. Functionality includes static factory methods for instantiating positive or negative threshold constraints, as well as support for standard logical operators such as negation, conjunction, and disjunction. The design ensures that structural manipulations, like cloning or replacing nested components, propagate correctly through the concept hierarchy without side effects, while delegating the extraction of atomic concepts and roles to the underlying nested concept to maintain consistent structural metadata.

.. ── LLM-GENERATED DESCRIPTION END ──

Attributes
----------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.concept.ext_threshold_concept.ExtendedNegThreshold
   fuzzy_dl_owl2.fuzzydl.concept.ext_threshold_concept.ExtendedPosThreshold


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.concept.ext_threshold_concept.ExtThresholdConcept


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_ext_threshold_concept_ExtThresholdConcept.png
       :alt: UML Class Diagram for ExtThresholdConcept
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **ExtThresholdConcept**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_ext_threshold_concept_ExtThresholdConcept.pdf
       :alt: UML Class Diagram for ExtThresholdConcept
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **ExtThresholdConcept**

.. py:class:: ExtThresholdConcept(c_type: fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType, c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, weight_variable: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.concept.concept.Concept`, :py:obj:`fuzzy_dl_owl2.fuzzydl.concept.interface.has_concept_interface.HasConceptInterface`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.concept.ext_threshold_concept.ExtThresholdConcept
      :parts: 1
      :private-bases:


   This class models a logical construct that imposes a variable-based threshold on the satisfaction degree of another concept. It defines conditions where an individual satisfies the concept if the degree of satisfaction of a nested concept is either greater than or equal to, or less than or equal to, a specific variable value. The class provides static factory methods to easily create positive or negative threshold concepts and supports standard logical operations such as negation, conjunction, and disjunction. Additionally, it allows for the modification of the threshold variable and the replacement of nested concepts, while delegating the retrieval of atomic concepts and roles to the underlying concept structure.

   :param _weight_variable: Internal storage for the threshold value $w$ in the extended threshold concept expression.
   :type _weight_variable: Variable
   :param name: The computed string representation of the extended threshold concept, formatted according to the threshold operator and weight variable.
   :type name: str


   .. py:method:: __and__(value: Self) -> Self

      Implements the bitwise AND operation (`&`) for the `ExtThresholdConcept` class, enabling logical conjunction between two instances. This method accepts another instance of the same type and delegates the actual computation to the `OperatorConcept.and_` static method. The operation returns a new instance of `ExtThresholdConcept` representing the result of the conjunction.

      :param value: The right-hand operand of the AND operation.
      :type value: typing.Self

      :return: Returns a new instance representing the result of the logical AND operation between this object and the provided value.

      :rtype: typing.Self



   .. py:method:: __hash__() -> int

      Return a hash value for this object, computed from its string representation. This approach ensures that the hash value reflects the structural identity of the object without relying on cached values or additional methods. The hash is derived from the output of the `__str__` method, which provides a consistent and unique representation of the concept's structure. This implementation does not utilize any internal caching mechanism and directly computes the hash each time it is called.

      :return: An integer hash value representing the structural identity of this object.

      :rtype: int



   .. py:method:: __neg__() -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept

      Returns the logical negation of the current concept instance, allowing the use of the unary minus operator (e.g., `-concept`). This method delegates the operation to `OperatorConcept.not_` to generate a new `Concept` representing the logical NOT of the original object without modifying it.

      :return: A new Concept representing the logical negation of this instance.

      :rtype: Concept



   .. py:method:: __or__(value: Self) -> Self

      Performs a logical OR operation between the current instance and another instance of the same type, typically invoked using the pipe operator (`|`). This method delegates the actual logic to `OperatorConcept.or_`, combining the two concepts to produce a new result. The operation is non-destructive, returning a new instance of `ExtThresholdConcept` rather than modifying the original operands. The `value` argument must be compatible with the current instance type to ensure the operation succeeds.

      :param value: The right-hand operand for the OR operation, expected to be of the same type as the current instance.
      :type value: typing.Self

      :return: A new instance representing the result of the OR operation between the current object and the provided value.

      :rtype: typing.Self



   .. py:method:: clone()

      Generates a duplicate of the current object by creating a new instance of `ExtThresholdConcept` initialized with the existing `type`, `curr_concept`, and `weight_variable` attributes. This method ensures that the original object remains unmodified, effectively providing a snapshot of the object's state at the time of the call. Note that because the constructor receives direct references to the attributes, the resulting clone performs a shallow copy, meaning any mutable objects referenced by these attributes will be shared between the original and the new instance.

      :return: A shallow copy of this concept.

      :rtype: ExtThresholdConcept



   .. py:method:: compute_atomic_concepts() -> set[fuzzy_dl_owl2.fuzzydl.concept.concept.Concept]

      Computes the set of atomic concepts associated with the current object by delegating the operation to the underlying `curr_concept` attribute. This method returns a collection of the fundamental, indivisible concepts that constitute the current state. As the logic is forwarded, the specific behavior, including potential side effects or exceptions, is determined by the implementation of `compute_atomic_concepts` within the referenced `curr_concept` object.

      :return: A set of atomic concepts that constitute the current concept.

      :rtype: set[Concept]



   .. py:method:: compute_name() -> Optional[str]

      Generates a descriptive string representation for the threshold concept by formatting the weight variable and current concept into a conditional expression. The specific operator used in the expression depends on the concept type: a positive threshold results in a 'greater than or equal to' operator, while other types default to a 'less than or equal to' operator. This method performs no side effects and relies entirely on the existing attributes of the instance.

      :return: A formatted string representing the concept combined with a threshold condition on the weight variable.

      :rtype: typing.Optional[str]



   .. py:method:: extended_neg_threshold(v: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, c: Self) -> Self
      :staticmethod:


      Constructs a new instance representing an extended negative threshold concept by combining a variable with an existing concept. This static method acts as a factory that initializes an `ExtThresholdConcept` with the specific type identifier `EXT_NEG_THRESHOLD`, passing the provided concept and variable to the constructor. The operation does not modify the input arguments but rather creates a new object that encapsulates the logical relationship defined by the negative threshold.

      :param v: The variable component of the extended negative threshold concept.
      :type v: Variable
      :param c: The constant value defining the threshold boundary.
      :type c: typing.Self

      :return: Returns a new instance representing an extended negative threshold concept derived from the provided variable and concept.

      :rtype: typing.Self



   .. py:method:: extended_pos_threshold(v: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, c: Self) -> Self
      :staticmethod:


      Creates a new instance of `ExtThresholdConcept` representing an extended positive threshold. This static method takes a `Variable` and an existing `ExtThresholdConcept` as inputs to construct the new object. It returns the newly created concept configured with the type `EXT_POS_THRESHOLD`, combining the provided variable and the existing concept without modifying the original arguments.

      :param v: The variable representing the threshold value.
      :type v: Variable
      :param c: The concept instance to be wrapped by the extended positive threshold.
      :type c: typing.Self

      :return: An `ExtThresholdConcept` instance representing an extended positive threshold involving the provided variable and concept.

      :rtype: typing.Self



   .. py:method:: get_roles() -> set[str]

      Retrieves the collection of roles associated with the current concept instance. This method acts as a delegation to the `get_roles` method of the internal `curr_concept` object, returning the resulting set of role identifiers. The operation has no side effects on the `ExtThresholdConcept` instance itself, though the behavior depends entirely on the state and implementation of the wrapped concept object.

      :return: A set of strings representing the roles associated with the current concept.

      :rtype: set[str]



   .. py:method:: replace(a: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept

      Returns a new `ExtThresholdConcept` instance with all occurrences of concept `a` replaced by concept `c` within the underlying `curr_concept` structure. This method preserves the original instance's type and weight variable attributes while delegating the recursive substitution logic to the nested concept. The operation is side-effect free, ensuring the original object remains unmodified, and returns a distinct object reflecting the updated conceptual structure.

      :param a: The concept to be replaced within the current structure.
      :type a: Concept
      :param c: The concept to replace `a` with.
      :type c: Concept

      :return: A new `ExtThresholdConcept` instance where the underlying concept has been updated by replacing occurrences of `a` with `c`.

      :rtype: Concept



   .. py:attribute:: _weight_variable
      :type:  fuzzy_dl_owl2.fuzzydl.milp.variable.Variable


   .. py:attribute:: name
      :type:  str


   .. py:property:: weight_variable
      :type: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable


      Returns the MILP :class:`Variable` that carries the threshold weight of this extended-threshold concept. Unlike the plain :class:`ThresholdConcept`, the weight here is a solver variable rather than a fixed constant, allowing the reasoner to determine it. The value is read from the private ``_weight_variable`` attribute without modifying the instance.

      :return: The variable holding the threshold weight.

      :rtype: Variable


.. py:data:: ExtendedNegThreshold

.. py:data:: ExtendedPosThreshold
