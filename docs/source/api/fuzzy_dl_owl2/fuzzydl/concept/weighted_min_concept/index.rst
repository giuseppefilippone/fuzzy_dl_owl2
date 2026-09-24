fuzzy_dl_owl2.fuzzydl.concept.weighted_min_concept
==================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.weighted_min_concept





.. ── LLM-GENERATED DESCRIPTION START ──

A weighted-minimum aggregation concept for fuzzy description logics that combines a list of sub-concepts with floating-point weights into a single composite expression.


Description
-----------


Fuzzy description logics frequently need to aggregate several concepts with differing degrees of importance, and ``WeightedMinConcept`` provides exactly that construct by pairing each sub-concept with a weight, inheriting core concept behaviour from the ``Concept`` base class and the shared weighted-collection machinery from ``HasWeightedConceptsInterface``. Construction is deliberately defensive: the number of weights must exactly match the number of sub-concepts, and at least one weight must equal 1.0, a constraint that keeps the weighted minimum semantically well-formed rather than degenerate. A canonical display name of the form ``(w-min (concept weight) ...)`` is computed eagerly at initialisation, so the object always carries a stable string representation of its configuration. Because the concept is a composite, queries for atomic concepts and roles are answered by recursing into the children and merging the results into sets, and cloning yields a new instance whose weight and concept lists are independent copies of the originals.

Structural manipulation follows the same recursive pattern: substituting one concept for another rebuilds the weighted minimum over the transformed children, and the result is returned wrapped in a negation, a design choice consistent with the usual duality between weighted minima and weighted maxima in fuzzy logic. The operator overloads for conjunction, disjunction, and negation are thin wrappers that delegate to ``OperatorConcept`` factory methods, which keeps the rules for combining concepts in one place and ensures the operands themselves are never mutated. Hashing is structural rather than identity-based, mixing the hash of each weighted child with the computed name and the concept type, so structurally equivalent expressions behave consistently when used as dictionary keys or set members.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.concept.weighted_min_concept.WeightedMinConcept


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_weighted_min_concept_WeightedMinConcept.png
       :alt: UML Class Diagram for WeightedMinConcept
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **WeightedMinConcept**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_weighted_min_concept_WeightedMinConcept.pdf
       :alt: UML Class Diagram for WeightedMinConcept
       :align: center
       :width: 11.7cm
       :class: uml-diagram

       UML Class Diagram for **WeightedMinConcept**

.. py:class:: WeightedMinConcept(weights: list[float], concepts: list[fuzzy_dl_owl2.fuzzydl.concept.concept.Concept])

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.concept.concept.Concept`, :py:obj:`fuzzy_dl_owl2.fuzzydl.concept.interface.has_weighted_concepts_interface.HasWeightedConceptsInterface`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.concept.weighted_min_concept.WeightedMinConcept
      :parts: 1
      :private-bases:


   This class models a composite concept defined by a weighted minimum operation over a collection of sub-concepts, typically used in fuzzy or description logic contexts. It is constructed by providing parallel lists of concepts and their associated floating-point weights, with the strict requirement that at least one weight must be equal to 1.0 to maintain semantic meaning. Once initialized, the object automatically generates a string representation and supports various structural manipulations, including cloning, replacing specific sub-concepts, and performing logical operations such as negation, conjunction, and disjunction.

   :param name: Computed string representation of the weighted minimum concept, automatically generated during initialization.
   :type name: typing.Any


   .. py:method:: __and__(value: Self) -> Self

      Performs a logical conjunction operation between the current instance and another instance of the same type, typically invoked via the `&` operator. This method delegates the core logic to the `and_` class method within `OperatorConcept`, ensuring that the combination follows the specific rules defined for the concept hierarchy. The operation returns a new instance representing the result of the conjunction, leaving the original operands unmodified.

      :param value: The right-hand operand for the AND operation, which must be an instance of the same class.
      :type value: typing.Self

      :return: The result of the AND operation between this object and the provided value.

      :rtype: typing.Self



   .. py:method:: __hash__() -> int

      Return a hash value for this object, computed from its string representation. This approach ensures that the hash value reflects the structural identity of the object without relying on cached values or additional methods. The hash is derived from the output of the `__str__` method, which provides a consistent and unique representation of the concept's structure. This implementation does not utilize any internal caching mechanism and directly computes the hash each time it is called.

      :return: An integer hash value representing the structural identity of this object.

      :rtype: int



   .. py:method:: __neg__() -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept

      Implements the unary negation operator to return the logical complement of the current concept. This method delegates the creation of the negated concept to `OperatorConcept.not_`, resulting in a new `Concept` instance that represents the inverse of the original. The operation is non-destructive, leaving the original instance unmodified while producing a distinct object representing the negated state.

      :return: A new Concept representing the logical negation of the current concept.

      :rtype: Concept



   .. py:method:: __or__(value: Self) -> Self

      Implements the bitwise OR operator (`|`) to perform a logical disjunction between the current instance and another `WeightedMinConcept` object. This method delegates the underlying logic to the `OperatorConcept.or_` static method, which handles the specific combination rules for the concepts. The operation returns a new instance representing the result of the union, ensuring that the original operands remain unchanged.

      :param value: The right-hand operand for the OR operation.
      :type value: typing.Self

      :return: Returns the result of the OR operation between the current instance and the provided value.

      :rtype: typing.Self



   .. py:method:: clone() -> Self

      Returns a new `WeightedMinConcept` instance that is a shallow copy of the current object. This method creates independent copies of the internal `weights` and `concepts` lists, ensuring that modifications to the list structures in the clone do not affect the original instance. However, because the copy is shallow, any mutable objects contained within these lists remain shared references between the original and the clone.

      :return: A new instance of the class that is a copy of the current object, containing independent copies of the internal weights and concepts lists.

      :rtype: typing.Self



   .. py:method:: compute_atomic_concepts() -> set[fuzzy_dl_owl2.fuzzydl.concept.concept.Concept]

      Computes and returns the set of atomic concepts that constitute this weighted minimum concept. The method iterates over the internal collection of concepts, recursively retrieving the atomic concepts from each child and aggregating them into a single set to ensure uniqueness. This process effectively flattens the composite structure to its most fundamental components.

      :return: A set of all atomic concepts derived from the concepts contained within this object.

      :rtype: set[Concept]



   .. py:method:: compute_name() -> str

      Generates a string representation of the weighted minimum concept by formatting the internal concepts and their associated weights. The method iterates over the paired concepts and weights, creating a space-separated list of parenthesized values, and wraps this list within a '(w-min ...)' prefix. This provides a descriptive identifier that reflects the specific configuration of the concept without modifying the object's state.

      :return: Returns a string representing the weighted minimum configuration, formatted as '(w-min (concept weight) ...)'.

      :rtype: str



   .. py:method:: get_roles() -> set[str]

      Aggregates and returns a set of role strings derived from all underlying concepts managed by this instance. This method iterates through the internal collection of concepts, invoking `get_roles` on each element and merging the results into a single set to ensure uniqueness. If the instance contains no concepts, an empty set is returned.

      :return: A set of unique roles aggregated from all concepts.

      :rtype: set[str]



   .. py:method:: replace(a: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept

      Returns the negation of a new `WeightedMinConcept` where every sub-concept has been transformed by replacing instances of concept `a` with concept `c`. The replacement is applied recursively to the nested concepts, and the original weights are retained in the new instance. This method does not modify the current object in place.

      :param a: The concept to be replaced.
      :type a: Concept
      :param c: The concept to replace `a` with.
      :type c: Concept

      :return: A new Concept resulting from the substitution of every occurrence of concept `a` with concept `c`.

      :rtype: Concept



   .. py:attribute:: name
      :value: '(w-min )'

