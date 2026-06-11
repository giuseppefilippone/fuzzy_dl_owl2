fuzzy_dl_owl2.fuzzydl.concept.owa_concept
=========================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.owa_concept



.. ── LLM-GENERATED DESCRIPTION START ──

Defines an **Ordered Weighted Averaging (OWA)** concept structure that aggregates a collection of sub-concepts using corresponding numerical weights to support fuzzy logic operations.


Description
-----------


The software models an **Ordered Weighted Averaging (OWA)** operator, which functions as a composite structure designed to aggregate multiple sub-concepts by applying a specific set of numerical weights to each component. By inheriting from base classes that define conceptual behavior and weighted interfaces, the implementation ensures that the number of provided weights strictly matches the number of associated concepts, raising an error if these parallel lists are misaligned during initialization. The design supports complex logical manipulations by overloading standard operators such as negation, conjunction, and disjunction, delegating the actual computation to a central operator utility while maintaining the specific OWA structure. Furthermore, the logic includes capabilities for recursive traversal to extract atomic concepts and roles from nested structures, as well as a mechanism to generate a standardized string representation that reflects the internal weights and concept hierarchy. A custom hashing strategy is employed to establish structural identity based on the tuple of weights, the hashes of nested concepts, and the object type, ensuring that instances can be reliably compared and stored in hash-based collections.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.concept.owa_concept.OwaConcept


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_owa_concept_OwaConcept.png
       :alt: UML Class Diagram for OwaConcept
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OwaConcept**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_owa_concept_OwaConcept.pdf
       :alt: UML Class Diagram for OwaConcept
       :align: center
       :width: 11.8cm
       :class: uml-diagram

       UML Class Diagram for **OwaConcept**

.. py:class:: OwaConcept(weights: list[float], concepts: list[fuzzy_dl_owl2.fuzzydl.concept.concept.Concept])

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.concept.concept.Concept`, :py:obj:`fuzzy_dl_owl2.fuzzydl.concept.interface.has_weighted_concepts_interface.HasWeightedConceptsInterface`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.concept.owa_concept.OwaConcept
      :parts: 1
      :private-bases:


   This entity models an Ordered Weighted Averaging (OWA) concept, serving as a composite structure that aggregates a list of sub-concepts using a corresponding list of numerical weights. To utilize this class, instantiate it with two parallel lists: one of floating-point weights and another of `Concept` objects, ensuring they are of the same length to satisfy validation requirements. The class automatically generates a standardized string representation and supports operations such as cloning, retrieving atomic concepts and roles, and replacing specific nested components. By inheriting from `Concept` and `HasWeightedConceptsInterface`, it integrates seamlessly into a broader system of logical or semantic operators, allowing for weighted combinations of complex conceptual definitions.

   :param name: The canonical string representation of the OWA concept, automatically generated during initialization.
   :type name: typing.Any


   .. py:method:: __and__(value: Self) -> Self

      Implements the behavior of the bitwise AND operator (`&`) for the concept, allowing it to be combined with another instance of the same type. The operation delegates the actual computation to the `OperatorConcept.and_` method, which determines the specific logic for merging the two concepts. This method returns a new instance representing the combined result and does not modify the original objects in place.

      :param value: The right-hand operand of the bitwise AND operation.
      :type value: typing.Self

      :return: A new instance representing the result of the AND operation between the current instance and the provided value.

      :rtype: typing.Self



   .. py:method:: __hash__() -> int

      Return a hash value for this object, computed from its string representation. This approach ensures that the hash value reflects the structural identity of the object without relying on cached values or additional methods. The hash is derived from the output of the `__str__` method, which provides a consistent and unique representation of the concept's structure. This implementation does not utilize any internal caching mechanism and directly computes the hash each time it is called.

      :return: An integer hash value representing the structural identity of this object.

      :rtype: int



   .. py:method:: __neg__() -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept

      Implements the unary negation operator, enabling the use of the minus sign to represent the logical complement of the concept. This method returns a new `Concept` instance that corresponds to the logical NOT of the current object, effectively delegating the operation to `OperatorConcept.not_`. It does not modify the original instance in place but rather produces a new representation of the negated concept.

      :return: The logical negation of the current concept.

      :rtype: Concept



   .. py:method:: __or__(value: Self) -> Self

      Implements the bitwise OR operation for the concept, enabling the use of the pipe operator (`|`) to combine two instances. This method delegates the logic to `OperatorConcept.or_`, passing the current instance and the provided value to perform the disjunction. It returns a new instance of the same type, representing the result of the operation without modifying the original operands.

      :param value: The right-hand operand to combine with the current instance using the OR operation.
      :type value: typing.Self

      :return: The result of the OR operation between the current instance and the provided value.

      :rtype: typing.Self



   .. py:method:: clone() -> Self

      Creates and returns a new instance of `OwaConcept` that serves as a shallow copy of the current object. The method constructs the clone by creating independent copies of the internal `weights` and `concepts` lists, ensuring that structural modifications to these lists in the clone do not affect the original instance. However, because the copy is shallow, the elements contained within the lists are shared by reference, meaning mutations to the actual concept objects or weight values will be reflected in both the original and the clone.

      :return: A new instance of the class with copies of the weights and concepts.

      :rtype: typing.Self



   .. py:method:: compute_atomic_concepts() -> set[fuzzy_dl_owl2.fuzzydl.concept.concept.Concept]

      Computes and returns the set of atomic concepts represented by this entity by aggregating the atomic concepts of its immediate children. The method iterates through the collection of concepts stored in the `concepts` attribute, recursively invoking `compute_atomic_concepts` on each element and collecting the results into a unified set. Since the return value is a set, duplicate atomic concepts are automatically removed. If the instance contains no sub-concepts, an empty set is returned.

      :return: A set of all atomic concepts derived from the concepts contained in this object.

      :rtype: set[Concept]



   .. py:method:: compute_name() -> str

      Generates a string representation of the Ordered Weighted Averaging (OWA) concept by formatting the internal weights and concepts into a specific parenthesized syntax. The method joins the string representations of the weights and concepts with spaces, embedding them within a structure that follows the pattern `(owa (<weights>) (<concepts>))`. This output serves as a computed name or identifier for the concept based on its current state.

      :return: A string representation of the OWA operator formatted as '(owa (weights) (concepts))'.

      :rtype: str



   .. py:method:: get_roles() -> set[str]

      Retrieves the union of roles associated with the underlying concepts contained within this instance. It iterates through the collection of concepts, aggregating the results of their individual role retrieval calls into a single set to ensure uniqueness. This method does not modify the internal state of the object or its sub-concepts, and it returns an empty set if no concepts are present.

      :return: A set of unique roles aggregated from all concepts.

      :rtype: set[str]



   .. py:method:: replace(a: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> Optional[fuzzy_dl_owl2.fuzzydl.concept.concept.Concept]

      Returns a new instance of `OwaConcept` where every sub-concept within `self.concepts` has been transformed by recursively replacing occurrences of concept `a` with concept `c`. The method preserves the original weights of the current instance while constructing the new object, but applies a logical negation to the final result before returning it. This operation does not modify the original object in place, ensuring that side effects are avoided.

      :param a: The concept to be replaced.
      :type a: Concept
      :param c: The concept to replace `a` with.
      :type c: Concept

      :return: The negation of the concept resulting from replacing all occurrences of `a` with `c`.

      :rtype: typing.Optional[Concept]


