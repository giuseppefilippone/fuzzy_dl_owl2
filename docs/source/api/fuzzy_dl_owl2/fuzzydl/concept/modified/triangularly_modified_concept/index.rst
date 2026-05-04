fuzzy_dl_owl2.fuzzydl.concept.modified.triangularly_modified_concept
====================================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.modified.triangularly_modified_concept



.. ── LLM-GENERATED DESCRIPTION START ──

A specialized fuzzy logic concept that applies a triangular modifier to a base concept to non-linearly transform its degree of satisfaction.


Description
-----------


The software defines a specific type of fuzzy logic entity where a base concept is transformed by a triangular modifier, altering how membership values are calculated in a non-linear fashion. By inheriting from a generic modified concept base, it integrates into a broader hierarchy of fuzzy description logic elements, allowing for complex expressions involving conjunctions, disjunctions, and negations. Logical operations are handled by delegating to a central operator utility, ensuring consistent behavior across different concept types while keeping the implementation focused on the specific modification logic. Structural manipulation capabilities include cloning the entity and recursively replacing internal sub-concepts, with the replacement logic specifically returning the negated result of the updated structure. Hashing relies on the string representation of the object to facilitate its use within collections like sets and dictionaries.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.concept.modified.triangularly_modified_concept.TriangularlyModifiedConcept


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_modified_triangularly_modified_concept_TriangularlyModifiedConcept.png
       :alt: UML Class Diagram for TriangularlyModifiedConcept
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **TriangularlyModifiedConcept**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_modified_triangularly_modified_concept_TriangularlyModifiedConcept.pdf
       :alt: UML Class Diagram for TriangularlyModifiedConcept
       :align: center
       :width: 11.8cm
       :class: uml-diagram

       UML Class Diagram for **TriangularlyModifiedConcept**

.. py:class:: TriangularlyModifiedConcept(c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, mod: fuzzy_dl_owl2.fuzzydl.modifier.modifier.Modifier)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.concept.modified.modified_concept.ModifiedConcept`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.concept.modified.triangularly_modified_concept.TriangularlyModifiedConcept
      :parts: 1
      :private-bases:


   This class represents a conceptual entity where a base concept is adjusted by a triangular modifier, which transforms the degree of satisfaction or membership value of the concept in a specific, non-linear manner. To utilize this structure, one must instantiate it with the target concept and the desired triangular modifier. The resulting object supports standard logical operations, including negation, conjunction, and disjunction, allowing it to participate in complex logical expressions. Additionally, it offers methods for cloning the instance and recursively replacing sub-concepts within the underlying structure to facilitate dynamic manipulation of the conceptual hierarchy.


   .. py:method:: __and__(value: Self) -> Self

      Implements the bitwise AND operation using the `&` operator for the current instance. This method delegates the actual computation to the `OperatorConcept.and_` static method, passing both the current instance and the provided value. It returns a new instance of the same type representing the result of the conjunction, without modifying the original operands.

      :param value: The other operand to perform the AND operation with.
      :type value: typing.Self

      :return: The result of the logical AND operation between this instance and the provided value.

      :rtype: typing.Self



   .. py:method:: __hash__() -> int

      Computes the integer hash value for the instance, allowing it to be used as a key in dictionaries or stored in sets. The implementation generates the hash by converting the object to its string representation and hashing that result, meaning the hash value is entirely dependent on the output of the `__str__` method. Consequently, the consistency of the hash relies on the stability of the string representation; if the object is mutable and its string form changes, the hash value will change, potentially violating the contract required for hashable objects.

      :return: An integer hash value derived from the string representation of the object.

      :rtype: int



   .. py:method:: __neg__() -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept

      Implements the unary negation operator, enabling the use of the minus sign to represent the logical negation of the concept. This method returns a new `Concept` instance that wraps the current instance within a logical 'NOT' operation by delegating to `OperatorConcept.not_`. The operation does not modify the original object in place.

      :return: A new Concept representing the logical negation of this concept.

      :rtype: Concept



   .. py:method:: __or__(value: Self) -> Self

      Implements the bitwise OR operation for the concept, enabling the use of the pipe operator (`|`) to combine two instances. This method accepts another object of the same type and returns a new instance representing the logical disjunction or union of the two concepts. The operation is delegated to the `OperatorConcept` class to handle the specific calculation logic, ensuring that the original instances remain unmodified.

      :param value: Another instance to combine with the current instance using the OR operation.
      :type value: typing.Self

      :return: The result of the OR operation between the current instance and the provided value.

      :rtype: typing.Self



   .. py:method:: clone() -> Self

      Creates and returns a new instance of `TriangularlyModifiedConcept` that replicates the state of the current object. The clone is constructed using the existing `curr_concept` and `modifier` attributes, ensuring that the original object remains unmodified. Note that because the attributes are passed directly to the new instance, this operation performs a shallow copy; if the underlying concept or modifier objects are mutable, changes to them will be reflected in both the original and the clone.

      :return: A new instance of the class that is a copy of the current object.

      :rtype: typing.Self



   .. py:method:: replace(a: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept

      Performs a substitution operation by replacing every instance of concept `a` with concept `c` within the underlying `curr_concept`. This method preserves the current `modifier` and constructs a new `TriangularlyModifiedConcept` instance containing the updated underlying concept. The final result is the logical negation of this newly constructed instance, ensuring that the original object remains unmodified.

      :param a: The concept to be replaced within the current concept structure.
      :type a: Concept
      :param c: The concept to substitute for the target concept `a`.
      :type c: Concept

      :return: A new Concept representing the result of replacing concept `a` with concept `c` within the current concept, preserving the existing modification context and applying a negation.

      :rtype: Concept


