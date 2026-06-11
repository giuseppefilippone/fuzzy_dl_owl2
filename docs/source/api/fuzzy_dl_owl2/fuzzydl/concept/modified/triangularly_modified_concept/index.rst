fuzzy_dl_owl2.fuzzydl.concept.modified.triangularly_modified_concept
====================================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.modified.triangularly_modified_concept



.. ── LLM-GENERATED DESCRIPTION START ──

A specialized class representing a fuzzy logic concept that has been transformed by a triangular modifier to adjust its membership degree.


Description
-----------


The implementation extends the general framework for modified concepts to specifically handle triangular transformations, which are used to non-linearly adjust the degree of membership or satisfaction of a base concept. By associating a specific modifier with a conceptual entity, the structure allows for the dynamic alteration of fuzzy logic values while maintaining the integrity of the original concept hierarchy. Logical operations such as negation, conjunction, and disjunction are supported through delegation to a central operator handler, enabling these modified concepts to participate in complex logical expressions. Furthermore, the design includes mechanisms for cloning the instance and recursively replacing sub-concepts, with the replacement process specifically applying a logical negation to the updated structure to ensure consistent behavior during manipulation. Hashing is implemented based on the internal attributes to facilitate the use of these objects within collections that require unique identification.

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
       :width: 8.9cm
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

      Return a hash value for this object, computed from its string representation. This approach ensures that the hash value reflects the structural identity of the object without relying on cached values or additional methods. The hash is derived from the output of the `__str__` method, which provides a consistent and unique representation of the concept's structure. This implementation does not utilize any internal caching mechanism and directly computes the hash each time it is called.

      :return: An integer hash value representing the structural identity of this object.

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


