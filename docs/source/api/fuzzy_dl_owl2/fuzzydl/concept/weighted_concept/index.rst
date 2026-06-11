fuzzy_dl_owl2.fuzzydl.concept.weighted_concept
==============================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.weighted_concept



.. ── LLM-GENERATED DESCRIPTION START ──

A Python class representing a fuzzy description logic concept modified by a numerical weight to denote importance or relevance.


Description
-----------


The software implements a wrapper for logical concepts within a fuzzy description logic framework, allowing a numerical weight to be associated with a base concept to represent its significance or priority. By inheriting from a base concept class and utilizing an interface for concept containment, the design ensures that the weighted entity behaves like a standard concept while maintaining a distinct scalar value. Structural queries, such as retrieving atomic concepts or roles, are delegated directly to the encapsulated inner concept, ensuring that the wrapper remains transparent to the underlying logical structure. The implementation also supports standard logical operations like negation, conjunction, and disjunction through operator overloading, which relies on a separate operator utility to construct new concept instances. Furthermore, the logic includes mechanisms for cloning the object and replacing internal components, while the hashing strategy ensures that the identity of the object is determined by a combination of its weight, the hash of its inner concept, and its type.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.concept.weighted_concept.WeightedConcept


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_weighted_concept_WeightedConcept.png
       :alt: UML Class Diagram for WeightedConcept
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **WeightedConcept**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_weighted_concept_WeightedConcept.pdf
       :alt: UML Class Diagram for WeightedConcept
       :align: center
       :width: 8.9cm
       :class: uml-diagram

       UML Class Diagram for **WeightedConcept**

.. py:class:: WeightedConcept(weight: float, c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.concept.concept.Concept`, :py:obj:`fuzzy_dl_owl2.fuzzydl.concept.interface.has_concept_interface.HasConceptInterface`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.concept.weighted_concept.WeightedConcept
      :parts: 1
      :private-bases:


   This class models a concept that is modified or qualified by a numerical weight, representing the form (w C) where 'w' signifies importance or relevance and 'C' is the underlying concept. It serves as a wrapper around a standard `Concept` object, allowing the system to handle graded or prioritized concepts within a broader logical or ontological framework. Users can instantiate this class by providing a floating-point weight and a target concept, after which the class automatically generates a string representation and delegates structural queries, such as retrieving atomic concepts or roles, to the encapsulated concept. Additionally, it supports standard logical operations (negation, conjunction, disjunction) through operator overloading and provides functionality for cloning or replacing internal components.

   :param _weight: Internal storage for the weight value, representing the importance or relevance of the concept.
   :type _weight: float
   :param name: String representation of the weighted concept in the format '(weight concept)', generated upon initialization.
   :type name: typing.Any


   .. py:method:: __and__(value: Self) -> Self

      Performs a logical conjunction between the current instance and another instance of the same type by implementing the bitwise AND operator (`&`). This operation delegates the underlying logic to the `OperatorConcept.and_` method, which determines how the concepts are combined or intersected. The method returns a new instance representing the result of the operation, leaving the original operands unchanged.

      :param value: The right-hand operand for the AND operation.
      :type value: typing.Self

      :return: The result of the logical AND operation between this instance and the provided value.

      :rtype: typing.Self



   .. py:method:: __hash__() -> int

      Return a hash value for this object, computed from its string representation. This approach ensures that the hash value reflects the structural identity of the object without relying on cached values or additional methods. The hash is derived from the output of the `__str__` method, which provides a consistent and unique representation of the concept's structure. This implementation does not utilize any internal caching mechanism and directly computes the hash each time it is called.

      :return: An integer hash value representing the structural identity of this object.

      :rtype: int



   .. py:method:: __neg__() -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept

      Returns the logical negation of the current concept, enabling the use of the unary minus operator to represent a NOT operation. This method delegates the construction of the negated expression to `OperatorConcept.not_`, resulting in a new `Concept` object that encapsulates the logical complement of the original instance. The operation is side-effect free, leaving the original `WeightedConcept` unmodified.

      :return: The logical negation of the concept.

      :rtype: Concept



   .. py:method:: __or__(value: Self) -> Self

      Overloads the bitwise OR operator to perform a logical disjunction between the current instance and another `WeightedConcept`. This operation creates and returns a new `WeightedConcept` representing the combination of the two operands, effectively calculating the logical "OR" of their underlying values or weights. The implementation delegates the specific logic to the `OperatorConcept.or_` method, ensuring that the operation does not mutate the original instances but rather produces a distinct result.

      :param value: The right-hand operand to combine with the current instance using the OR operation.
      :type value: typing.Self

      :return: A new instance representing the result of the logical OR operation between this instance and the provided value.

      :rtype: typing.Self



   .. py:method:: clone() -> Self

      Creates and returns a new instance of `WeightedConcept` that duplicates the current object. The new object is initialized with the same `weight` and `curr_concept` values found in the original instance. This operation performs a shallow copy with respect to the attributes; therefore, if `curr_concept` is a mutable object, changes made to it through the clone will affect the original object as well.

      :return: A new instance of the class with the same weight and current concept as the original.

      :rtype: typing.Self



   .. py:method:: compute_atomic_concepts() -> set[fuzzy_dl_owl2.fuzzydl.concept.concept.Concept]

      Computes the set of atomic concepts associated with the underlying concept stored in `curr_concept`. This method acts as a delegation wrapper, forwarding the computation request to the `compute_atomic_concepts` method of the internal concept object. It returns a set of `Concept` instances representing the fundamental, non-decomposable elements that make up the current concept.

      :return: The set of atomic concepts that constitute the current concept.

      :rtype: set[Concept]



   .. py:method:: compute_name() -> Optional[str]

      Generates a formatted string representation that combines the instance's weight and current concept into a parenthetical notation. The output strictly follows the pattern "(weight concept)", utilizing the string conversion of the underlying attributes. This method is a read-only operation with no side effects on the object's state, though it assumes that the `weight` and `curr_concept` attributes are properly initialized to avoid runtime errors.

      :return: A string representing the weight and current concept, formatted as "(weight curr_concept)".

      :rtype: typing.Optional[str]



   .. py:method:: get_roles() -> set[str]

      Retrieves the set of roles associated with the underlying concept object. This method delegates the call to the `curr_concept` attribute, returning the set of strings provided by that object's own `get_roles` implementation. As this is a direct pass-through, the method has no side effects of its own, though it relies on `curr_concept` being properly initialized and may propagate any exceptions raised by the delegated call.

      :return: A set of strings representing the roles associated with the current concept.

      :rtype: set[str]



   .. py:method:: replace(a: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept

      Replaces a specific target concept within the structure with a provided replacement concept, provided the replacement is of type `WEIGHTED`. If the replacement concept is weighted, the method returns a new `WeightedConcept` that preserves the original weight of the current instance while recursively applying the replacement operation to the underlying concept. This ensures that the weight attribute remains unchanged during the transformation, while the internal concept hierarchy is updated according to the replacement logic.

      :param a: The concept to be replaced.
      :type a: Concept
      :param c: The concept to use as the replacement.
      :type c: Concept

      :return: A new Concept representing the result of replacing concept `a` with concept `c`. If `c` is a weighted concept, returns a WeightedConcept preserving the current weight and applying the replacement to the underlying concept.

      :rtype: Concept



   .. py:attribute:: _weight
      :type:  float


   .. py:attribute:: name


   .. py:property:: weight
      :type: float


      Returns the weight applied to the wrapped concept, i.e. the scalar factor by which this weighted concept scales the membership degree of its inner concept in a weighted aggregation. The value is read from the private ``_weight`` attribute without modifying the instance.

      :return: The weight applied to the wrapped concept.

      :rtype: float

