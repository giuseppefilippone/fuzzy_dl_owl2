fuzzy_dl_owl2.fuzzydl.concept.modified.linearly_modified_concept
================================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.modified.linearly_modified_concept



.. ── LLM-GENERATED DESCRIPTION START ──

Represents a fuzzy description logic concept whose truth value is adjusted by a linear modifier, enabling the construction of modified concepts within a logical hierarchy.


Description
-----------


Construction relies on a base concept and a specific modifier object, delegating initialization logic to the parent class to establish the core relationship between the two components. Logical operations such as negation, conjunction, and disjunction are supported through operator overloading, which delegates the creation of complex logical expressions to a central ``OperatorConcept`` utility. Structural manipulation is facilitated by methods for cloning the instance and replacing sub-concepts within the base structure, ensuring that modifications result in new independent instances rather than mutating existing ones. Hashing is derived from the string representation to allow these concepts to be used effectively within sets and as dictionary keys.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.concept.modified.linearly_modified_concept.LinearlyModifiedConcept


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_modified_linearly_modified_concept_LinearlyModifiedConcept.png
       :alt: UML Class Diagram for LinearlyModifiedConcept
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **LinearlyModifiedConcept**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_modified_linearly_modified_concept_LinearlyModifiedConcept.pdf
       :alt: UML Class Diagram for LinearlyModifiedConcept
       :align: center
       :width: 11.8cm
       :class: uml-diagram

       UML Class Diagram for **LinearlyModifiedConcept**

.. py:class:: LinearlyModifiedConcept(c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, mod: fuzzy_dl_owl2.fuzzydl.modifier.modifier.Modifier)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.concept.modified.modified_concept.ModifiedConcept`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.concept.modified.linearly_modified_concept.LinearlyModifiedConcept
      :parts: 1
      :private-bases:


   This class models a concept whose degree of satisfaction is adjusted by a linear modifier, representing a structure of the form (modifier C). It is instantiated by providing a base concept and a specific linear modifier that scales or shifts the concept's truth value in a linear fashion. The class supports standard logical operations, including negation, conjunction, and disjunction, enabling the integration of modified concepts into complex logical expressions. Furthermore, it provides utility methods for cloning the instance and replacing sub-concepts within the underlying structure, allowing for dynamic manipulation of the concept hierarchy.


   .. py:method:: __and__(value: Self) -> Self

      Implements the bitwise AND operation for the concept, allowing the use of the `&` operator to combine it with another instance of the same type. This method delegates the actual computation to `OperatorConcept.and_`, ensuring that the logic for conjunction is handled centrally within the module. The operation returns a new instance representing the result of the combination, without modifying the original objects.

      :param value: The right-hand operand for the AND operation.
      :type value: typing.Self

      :return: The result of the AND operation between this instance and the provided value.

      :rtype: typing.Self



   .. py:method:: __hash__() -> int

      Computes the hash value for the instance by delegating to the hash of the object's string representation. This behavior allows instances of `LinearlyModifiedConcept` to be used as dictionary keys or stored in sets, provided that the string representation remains consistent for equal objects and does not change over the object's lifetime. The implementation relies on the `__str__` method to generate the input for the hash function.

      :return: An integer hash value derived from the object's string representation.

      :rtype: int



   .. py:method:: __neg__() -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept

      Returns the logical negation of the current concept, effectively representing the 'not' operation. This method is invoked when the unary minus operator (`-`) is applied to an instance of the class. It delegates the construction of the resulting concept to `OperatorConcept.not_`, returning a new `Concept` object without modifying the original instance.

      :return: A new Concept representing the logical negation of the current concept.

      :rtype: Concept



   .. py:method:: __or__(value: Self) -> Self

      Performs a logical OR or union operation between the current instance and another instance of the same type, enabling the use of the pipe operator (`|`). This method delegates the underlying logic to `OperatorConcept.or_`, which handles the specific combination rules. It returns a new instance representing the combined concept without modifying the original operands. The operation expects the provided value to be a compatible instance of the same class.

      :param value: The other operand to perform the OR operation with.
      :type value: typing.Self

      :return: An instance representing the result of the OR operation between this instance and the provided value.

      :rtype: typing.Self



   .. py:method:: clone() -> Self

      Creates and returns a new instance of `LinearlyModifiedConcept` that duplicates the state of the current object. The clone is initialized with the same `curr_concept` and `modifier` attributes as the original, ensuring that subsequent modifications to the new instance do not affect the source. This method provides a mechanism for obtaining an independent copy of the object without altering the original's internal state.

      :return: A new instance of the class that is a copy of the current object, initialized with the same concept and modifier.

      :rtype: typing.Self



   .. py:method:: replace(a: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> Self

      Returns a new instance of the class where the underlying concept has been updated by replacing occurrences of concept `a` with concept `c`. The replacement operation is delegated to the underlying concept, and the modifier associated with the current instance is preserved in the result. This method does not mutate the original instance but instead returns a modified copy.

      :param a: The concept to find and replace.
      :type a: Concept
      :param c: The concept to substitute in place of `a`.
      :type c: Concept

      :return: A new instance of the class where the underlying concept has `a` replaced by `c`, retaining the current modifier.

      :rtype: typing.Self


