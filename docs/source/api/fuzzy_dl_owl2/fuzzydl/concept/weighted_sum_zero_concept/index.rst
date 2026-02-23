fuzzy_dl_owl2.fuzzydl.concept.weighted_sum_zero_concept
=======================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.weighted_sum_zero_concept



.. ── LLM-GENERATED DESCRIPTION START ──

A class representing a weighted sum of concepts within a fuzzy description logic system where the total weight is constrained to not exceed 1.0.


Description
-----------


The implementation models a specific type of fuzzy logic constraint by aggregating multiple sub-concepts, each assigned a numerical weight, into a single composite structure. During initialization, the logic validates that the provided lists of weights and concepts are of equal length and strictly enforces that the sum of all weights does not exceed 1.0, ensuring the resulting concept remains within defined probabilistic or logical bounds. By inheriting from base classes that define core concept behaviors and weighted interfaces, the class integrates seamlessly into a broader description logic framework, allowing it to participate in complex logical hierarchies. Standard logical operations such as negation, conjunction, and disjunction are supported through operator overloading, which delegates to a central ``OperatorConcept`` factory to maintain consistency across the system. Furthermore, the structure provides utility methods for traversing the concept hierarchy to retrieve atomic components or roles, cloning the instance to preserve state, and recursively replacing specific sub-concepts to facilitate transformations.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.concept.weighted_sum_zero_concept.WeightedSumZeroConcept


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_weighted_sum_zero_concept_WeightedSumZeroConcept.png
       :alt: UML Class Diagram for WeightedSumZeroConcept
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **WeightedSumZeroConcept**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_weighted_sum_zero_concept_WeightedSumZeroConcept.pdf
       :alt: UML Class Diagram for WeightedSumZeroConcept
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **WeightedSumZeroConcept**

.. py:class:: WeightedSumZeroConcept(weights: list[float], concepts: list[fuzzy_dl_owl2.fuzzydl.concept.concept.Concept])

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.concept.concept.Concept`, :py:obj:`fuzzy_dl_owl2.fuzzydl.concept.interface.has_weighted_concepts_interface.HasWeightedConceptsInterface`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.concept.weighted_sum_zero_concept.WeightedSumZeroConcept
      :parts: 1
      :private-bases:


   This class models a weighted sum zero concept, defined as a structured aggregation of multiple sub-concepts where each is assigned a specific weight. It enforces a strict constraint that the sum of all provided weights must not exceed 1.0, ensuring the combined concept remains within a specific logical or probabilistic bound. To use this class, instantiate it with two parallel lists: one containing floating-point weights and another containing `Concept` objects. The class automatically generates a string representation in the format `(w-sum-zero (w1 C1) ...)` and supports standard logical operations such as negation, conjunction, and disjunction through operator overloading. Additionally, it provides utility methods for cloning the structure, retrieving atomic components, and recursively replacing specific sub-concepts within the hierarchy.

   :param name: Automatically generated string representation of the concept, derived from the weights and constituent concepts.
   :type name: typing.Any


   .. py:method:: __and__(value: Self) -> Self

      Performs a logical conjunction between the current instance and another `WeightedSumZeroConcept` using the bitwise AND operator (`&`). This method combines the two concepts into a new instance that represents the intersection of their constraints, effectively requiring both conditions to be satisfied simultaneously. The implementation delegates the actual combination logic to the `OperatorConcept.and_` method, ensuring consistent behavior across the concept hierarchy. This operation does not modify the original instances but instead returns a new, combined concept.

      :param value: Another instance of the same class to perform the AND operation with.
      :type value: typing.Self

      :return: The result of the AND operation between the current instance and the provided value.

      :rtype: typing.Self



   .. py:method:: __hash__() -> int

      Computes an integer hash value for the instance, enabling its use in hash-based collections such as dictionaries and sets. The implementation derives the hash from the string representation of the object, effectively hashing the output of its `__str__` method. This implies that the hash value is consistent with the object's string form, but it also means that if the object is mutable and its string representation changes, the hash will change as well, potentially violating the invariants required for dictionary keys.

      :return: An integer hash value derived from the string representation of the object.

      :rtype: int



   .. py:method:: __neg__() -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept

      Implements the unary negation operator for the concept, enabling the use of the minus sign (`-`) to perform logical inversion. This method returns a new `Concept` instance representing the negation of the current `WeightedSumZeroConcept` by delegating to the `OperatorConcept.not_` factory method. The operation does not modify the original instance but instead produces a distinct conceptual object representing the opposite condition.

      :return: A new Concept representing the logical negation of this instance.

      :rtype: Concept



   .. py:method:: __or__(value: Self) -> Self

      Implements the bitwise OR operator (`|`) to perform a logical disjunction between the current concept and another concept of the same type. This method delegates the construction of the resulting concept to the `OperatorConcept.or_` static method, returning a new instance that represents the combination of the two operands without modifying the original objects.

      :param value: The other operand to combine with the current instance using the OR operation.
      :type value: typing.Self

      :return: The result of the OR operation between the current instance and the provided value.

      :rtype: typing.Self



   .. py:method:: clone() -> Self

      Creates and returns a new instance of `WeightedSumZeroConcept` that duplicates the state of the current object. The method performs a shallow copy of the internal `weights` and `concepts` lists, ensuring that modifications to the list structures of the clone do not affect the original instance. This allows for independent manipulation of the cloned object's collections while preserving the original data at the time of cloning.

      :return: A new instance of the class with copies of the weights and concepts.

      :rtype: typing.Self



   .. py:method:: compute_atomic_concepts() -> set[fuzzy_dl_owl2.fuzzydl.concept.concept.Concept]

      Computes and returns the complete set of atomic concepts underlying this composite concept. By iterating over the internal list of concepts and recursively invoking their `compute_atomic_concepts` methods, this function aggregates all fundamental components into a flat set. The use of a set guarantees that the result contains unique concepts, even if multiple sub-concepts share common atomic ancestors. If the internal concept list is empty, an empty set is returned.

      :return: A set of atomic concepts derived from the object's concepts.

      :rtype: set[Concept]



   .. py:method:: compute_name() -> str

      Generates a human-readable string representation of the weighted sum zero concept based on its constituent concepts and weights. The returned string follows a specific syntax, starting with the prefix 'w-sum-zero' followed by space-separated pairs of weights and concepts enclosed in parentheses. This method constructs the representation by iterating over the internal lists of concepts and weights, formatting each pair sequentially without modifying the object's state.

      :return: A formatted string representing the weighted sum zero constraint, listing each concept and its corresponding weight.

      :rtype: str



   .. py:method:: get_roles() -> set[str]

      Retrieves the union of all roles associated with the constituent concepts that define this weighted sum zero concept. By iterating through the internal collection of concepts and aggregating their individual roles, this method provides a comprehensive view of the semantic roles involved in the composite structure. The result is returned as a set of strings, ensuring that duplicate roles across different concepts are automatically deduplicated. If the concept contains no sub-concepts, an empty set is returned.

      :return: A set of unique roles aggregated from all concepts.

      :rtype: set[str]



   .. py:method:: replace(a: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept

      Recursively traverses the constituent concepts of the current instance to replace all occurrences of concept `a` with concept `c`. This method constructs a new `WeightedSumZeroConcept` using the original weights and the modified list of concepts resulting from the recursive replacement. The operation is non-destructive, returning the negation of the newly constructed concept rather than modifying the original instance in place.

      :param a: The concept to be replaced by `c`.
      :type a: Concept
      :param c: The concept to substitute in place of `a`.
      :type c: Concept

      :return: A new Concept where all instances of `a` are replaced by `c`.

      :rtype: Concept



   .. py:attribute:: name
      :value: '(w-sum-zero )'


      Updates the name of the Concept instance to the specified string value. This setter modifies the object's internal state by assigning the provided value to the private `_name` attribute, effectively replacing any previously stored name.

      :param value: The new name to assign to the object.
      :type value: str

