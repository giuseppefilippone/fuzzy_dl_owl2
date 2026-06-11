fuzzy_dl_owl2.fuzzydl.concept.weighted_max_concept
==================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.weighted_max_concept



.. ── LLM-GENERATED DESCRIPTION START ──

Implements a weighted maximum concept structure that pairs sub-concepts with numerical weights to perform fuzzy logic operations.


Description
-----------


The software models a weighted maximum operation by associating a collection of sub-concepts with a corresponding list of numerical weights, ensuring structural integrity through strict validation checks that require matching list lengths and the presence of at least one maximum weight. By inheriting from base concept and interface classes, the implementation integrates seamlessly into a broader fuzzy description logic framework, enabling the representation of complex logical constructs through a standardized parenthetical syntax. Logical operations such as conjunction, disjunction, and negation are supported by delegating to a central operator utility, allowing the weighted maximum structure to participate in algebraic expressions without modifying the original instance. Additionally, the design facilitates recursive traversal and manipulation of the concept hierarchy, providing mechanisms to extract atomic components, retrieve associated roles, and dynamically replace sub-concepts while maintaining the integrity of the weighted relationships.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.concept.weighted_max_concept.WeightedMaxConcept


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_weighted_max_concept_WeightedMaxConcept.png
       :alt: UML Class Diagram for WeightedMaxConcept
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **WeightedMaxConcept**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_weighted_max_concept_WeightedMaxConcept.pdf
       :alt: UML Class Diagram for WeightedMaxConcept
       :align: center
       :width: 11.7cm
       :class: uml-diagram

       UML Class Diagram for **WeightedMaxConcept**

.. py:class:: WeightedMaxConcept(weights: list[float], concepts: list[fuzzy_dl_owl2.fuzzydl.concept.concept.Concept])

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.concept.concept.Concept`, :py:obj:`fuzzy_dl_owl2.fuzzydl.concept.interface.has_weighted_concepts_interface.HasWeightedConceptsInterface`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.concept.weighted_max_concept.WeightedMaxConcept
      :parts: 1
      :private-bases:


   This class models a weighted maximum operation within a conceptual logic framework, defined by pairing a collection of sub-concepts with a corresponding list of numerical weights. It enforces strict validation during initialization, requiring that the number of weights exactly matches the number of concepts and that at least one weight is equal to 1.0 to ensure the operation is meaningful. Once instantiated, the object automatically generates a string representation of the structure and supports standard logical operations such as conjunction, disjunction, and negation through operator overloading. Furthermore, it provides utility methods for traversing the concept hierarchy, allowing users to retrieve atomic concepts and roles, clone the instance, or replace specific sub-concepts with alternatives.

   :param name: Automatically generated string representation of the concept in the format (w-max (C1 w1) (C2 w2) ...).
   :type name: typing.Any


   .. py:method:: __and__(value: Self) -> Self

      Implements the bitwise AND operator (`&`) to perform a logical conjunction or intersection between the current instance and another `WeightedMaxConcept`. The operation delegates the calculation to `OperatorConcept.and_`, returning a new instance that represents the combined result without altering the original objects.

      :param value: The right-hand operand for the AND operation.
      :type value: typing.Self

      :return: An instance representing the result of the 'and' operation between this instance and the provided value.

      :rtype: typing.Self



   .. py:method:: __hash__() -> int

      Return a hash value for this object, computed from its string representation. This approach ensures that the hash value reflects the structural identity of the object without relying on cached values or additional methods. The hash is derived from the output of the `__str__` method, which provides a consistent and unique representation of the concept's structure. This implementation does not utilize any internal caching mechanism and directly computes the hash each time it is called.

      :return: An integer hash value representing the structural identity of this object.

      :rtype: int



   .. py:method:: __neg__() -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept

      Returns the logical negation of the current concept, corresponding to the behavior of the unary minus operator. This operation creates and returns a new `Concept` instance by delegating to `OperatorConcept.not_`, leaving the original `WeightedMaxConcept` instance unchanged.

      :return: The logical negation of the current concept.

      :rtype: Concept



   .. py:method:: __or__(value: Self) -> Self

      Implements the bitwise OR operation (`|`) for the concept, allowing the current instance to be combined with another `WeightedMaxConcept` object. This method delegates the actual computation to `OperatorConcept.or_`, which defines the specific semantics of the disjunction operation within the module's algebraic framework. The operation returns a new instance of the same type representing the result of the combination, leaving the original operands unmodified.

      :param value: The right-hand operand to combine with the current instance using the OR operation.
      :type value: typing.Self

      :return: The result of the OR operation between this instance and the provided value.

      :rtype: typing.Self



   .. py:method:: clone() -> Self

      Returns a new instance of `WeightedMaxConcept` that is a shallow copy of the current object. The method constructs the clone using new list objects for the `weights` and `concepts` attributes, ensuring that modifications to the lists themselves in the clone do not affect the original instance. Note that because the copy is shallow, any mutable elements contained within these lists remain shared between the original and the clone.

      :return: A new instance of the class with copies of the weights and concepts.

      :rtype: typing.Self



   .. py:method:: compute_atomic_concepts() -> set[fuzzy_dl_owl2.fuzzydl.concept.concept.Concept]

      Computes and returns the set of all atomic concepts contained within the weighted max concept by recursively resolving its internal collection of concepts. This method iterates over the sub-concepts, aggregates their individual atomic constituents into a unified set to ensure uniqueness, and returns the result. If the internal collection is empty or resolves to no atomic concepts, an empty set is returned, and the operation does not modify the state of the object or its sub-concepts.

      :return: A set of all atomic concepts derived from the concepts associated with this instance.

      :rtype: set[Concept]



   .. py:method:: compute_name() -> str

      Generates a string representation of the weighted maximum concept by formatting the internal concepts and their corresponding weights into a specific parenthetical syntax. The output string is constructed by iterating over the paired concepts and weights, enclosing each pair in parentheses, joining them with spaces, and prefixing the result with "(w-max ...)". If the lists of concepts and weights are of unequal lengths, elements from the longer list are ignored due to the behavior of the `zip` function. This method does not modify the object's state and returns a newly constructed string.

      :return: A formatted string representing the weighted maximization of the concepts and their associated weights.

      :rtype: str



   .. py:method:: get_roles() -> set[str]

      Returns a set containing the unique roles associated with all concepts managed by this instance. This method aggregates the results of calling `get_roles` on each individual concept in the internal collection, effectively computing the union of their role sets. If the internal collection of concepts is empty, an empty set is returned. The operation does not modify the state of the instance or its contained concepts, though it relies on the behavior of the `get_roles` method of the individual concept objects.

      :return: A set of unique role names found across all associated concepts.

      :rtype: set[str]



   .. py:method:: replace(a: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept

      Recursively replaces all occurrences of the concept `a` with the concept `c` within the collection of sub-concepts maintained by this instance. This operation creates a new `WeightedMaxConcept` object that preserves the original weights but incorporates the modified sub-concepts resulting from the recursive replacement. The final result is the negation of this newly constructed concept, meaning the method returns the additive inverse of the structure containing the replacements.

      :param a: The concept to be replaced by `c`.
      :type a: Concept
      :param c: The concept to substitute in place of `a`.
      :type c: Concept

      :return: A new Concept resulting from replacing occurrences of `a` with `c` in the internal concepts, preserving weights and negating the resulting weighted maximum.

      :rtype: Concept



   .. py:attribute:: name
      :value: '(w-max )'


