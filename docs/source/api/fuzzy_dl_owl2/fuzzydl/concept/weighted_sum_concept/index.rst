fuzzy_dl_owl2.fuzzydl.concept.weighted_sum_concept
==================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.weighted_sum_concept



.. ── LLM-GENERATED DESCRIPTION START ──

Implements a composite fuzzy concept that aggregates sub-concepts using a weighted linear combination.


Description
-----------


The software models a complex fuzzy description logic entity by combining multiple sub-concepts with specific numerical coefficients to represent a linear mixture. It enforces strict validation rules during initialization, ensuring that the number of weights matches the number of constituent concepts and that the total weight sum does not exceed 1.0 to maintain logical consistency. By inheriting from a base concept class and an interface for weighted components, the implementation integrates seamlessly into a broader fuzzy logic framework, supporting standard logical operations such as negation, conjunction, and disjunction through operator overloading. The design facilitates structural manipulation by allowing recursive replacement of specific sub-concepts and the retrieval of atomic components or roles, while also providing a string-based representation for hashing and identification purposes.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.concept.weighted_sum_concept.WeightedSumConcept


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_weighted_sum_concept_WeightedSumConcept.png
       :alt: UML Class Diagram for WeightedSumConcept
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **WeightedSumConcept**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_weighted_sum_concept_WeightedSumConcept.pdf
       :alt: UML Class Diagram for WeightedSumConcept
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **WeightedSumConcept**

.. py:class:: WeightedSumConcept(weights: list[float], concepts: list[fuzzy_dl_owl2.fuzzydl.concept.concept.Concept])

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.concept.concept.Concept`, :py:obj:`fuzzy_dl_owl2.fuzzydl.concept.interface.has_weighted_concepts_interface.HasWeightedConceptsInterface`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.concept.weighted_sum_concept.WeightedSumConcept
      :parts: 1
      :private-bases:


   This entity models a composite concept formed by aggregating a collection of sub-concepts using specific numerical weights, effectively representing a linear combination or mixture. To utilize this class, instantiate it with two parallel lists: one containing floating-point weights and another containing the corresponding `Concept` objects. It is crucial that the number of weights matches the number of concepts and that the total sum of the weights does not exceed 1.0, as exceeding this limit is considered invalid for the model's logic. Upon initialization, the object automatically generates a string representation of its structure. Additionally, this class supports logical operations such as negation, conjunction, and disjunction through standard Python operators, and provides methods for traversing or modifying the underlying concept hierarchy, such as replacing specific sub-concepts or retrieving atomic components.

   :param name: Automatically generated string representation of the weighted sum concept in the format (w-sum (w1 C1) (w2 C2) ...).
   :type name: typing.Any


   .. py:method:: __and__(value: Self) -> Self

      Performs a logical conjunction or combination operation between the current instance and another instance of the same type, enabling the use of the `&` operator. This method delegates the core logic to the `and_` static method defined in `OperatorConcept`, ensuring that the operation adheres to the specific algebraic rules defined for the concept. It returns a new instance representing the result of the operation, leaving the original operands unmodified.

      :param value: The right-hand operand of the AND operation.
      :type value: typing.Self

      :return: The result of the AND operation between the instance and the provided value.

      :rtype: typing.Self



   .. py:method:: __hash__() -> int

      Calculates the hash value of the instance by hashing its string representation, enabling the object to be used in hash-based collections such as dictionaries and sets. The implementation delegates the hashing logic to the result of the `__str__` method, meaning the hash value is directly tied to the textual representation of the object. Consequently, any modifications to the string formatting logic will alter the hash value, potentially affecting lookups in existing hash-based data structures.

      :return: An integer hash value computed from the string representation of the object.

      :rtype: int



   .. py:method:: __neg__() -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept

      Implements the unary negation operator to return the logical negation of the current concept. This method delegates the creation of the negated object to `OperatorConcept.not_`, ensuring that the operation returns a new `Concept` instance rather than modifying the existing one in place. Consequently, applying the minus sign to a `WeightedSumConcept` effectively treats it as a logical NOT operation.

      :return: A Concept representing the logical negation of this concept.

      :rtype: Concept



   .. py:method:: __or__(value: Self) -> Self

      Implements the bitwise OR operator (`|`) to perform a logical disjunction between the current concept and another `WeightedSumConcept`. This method delegates the construction of the resulting concept to `OperatorConcept.or_`, returning a new instance that represents the union of the two operands without modifying the original objects. The operation requires the provided value to be of the same type as the current instance.

      :param value: The other operand to combine with the current instance using the OR operation.
      :type value: typing.Self

      :return: A new instance representing the result of the OR operation between the current instance and the provided value.

      :rtype: typing.Self



   .. py:method:: clone() -> Self

      Returns a shallow copy of the current `WeightedSumConcept` instance. The method instantiates a new object using independent copies of the internal `weights` and `concepts` lists, ensuring that structural modifications to these lists in the clone do not affect the original object. However, because the copy is shallow, the new instance retains references to the same underlying concept objects; therefore, mutations to the concept objects themselves will be reflected in both the original and the clone.

      :return: A new instance of the class with copies of the weights and concepts lists.

      :rtype: typing.Self



   .. py:method:: compute_atomic_concepts() -> set[fuzzy_dl_owl2.fuzzydl.concept.concept.Concept]

      Computes and returns the set of all atomic concepts underlying this weighted sum concept. This method iterates over the internal collection of concepts, recursively invoking their `compute_atomic_concepts` methods and aggregating the results into a single set to ensure uniqueness. The returned set represents the base-level concepts that compose this composite structure.

      :return: A set of all atomic concepts derived from the concepts associated with this object.

      :rtype: set[Concept]



   .. py:method:: compute_name() -> str

      Generates a string representation of the weighted sum concept by iterating over the internal lists of concepts and weights. The returned string follows a specific parenthesized syntax, starting with "(w-sum" and appending space-separated tuples containing the weight and the corresponding concept. This method is read-only and does not modify the object's state; however, if the lists of concepts and weights have mismatched lengths, the `zip` function will truncate the output to the length of the shorter list, ignoring any excess elements.

      :return: A string representation of the weighted sum of concepts and their corresponding weights, formatted as "(w-sum (weight concept) ...)".

      :rtype: str



   .. py:method:: get_roles() -> set[str]

      Retrieves the union of roles associated with the underlying concepts that constitute this weighted sum. It iterates over the collection of concepts stored in the instance, aggregates the roles returned by each sub-concept, and returns them as a unique set of strings. If there are no underlying concepts, an empty set is returned. Since the result is a set, duplicate roles found across different sub-concepts are automatically removed. This operation does not modify the state of the object or its sub-concepts.

      :return: A set of unique roles derived from the object's concepts.

      :rtype: set[str]



   .. py:method:: replace(a: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept

      Replaces all occurrences of a specific concept with another concept within the internal list of component concepts by recursively delegating the replacement operation to each sub-concept. A new instance is constructed using the original weights and the updated list of concepts, and the method returns the logical negation of this new object. This ensures the substitution propagates through nested structures while preserving the original weighting scheme.

      :param a: The concept to be replaced.
      :type a: Concept
      :param c: The concept to substitute in place of `a`.
      :type c: Concept

      :return: A new Concept representing the negation of the weighted sum where every occurrence of concept `a` is replaced by concept `c`.

      :rtype: Concept



   .. py:attribute:: name
      :value: '(w-sum )'


      Updates the name of the Concept instance to the specified string value. This setter modifies the object's internal state by assigning the provided value to the private `_name` attribute, effectively replacing any previously stored name.

      :param value: The new name to assign to the object.
      :type value: str

