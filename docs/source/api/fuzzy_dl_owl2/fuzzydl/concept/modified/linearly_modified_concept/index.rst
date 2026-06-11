fuzzy_dl_owl2.fuzzydl.concept.modified.linearly_modified_concept
================================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.modified.linearly_modified_concept



.. ── LLM-GENERATED DESCRIPTION START ──

A specialized implementation of a fuzzy description logic concept that applies a linear transformation to the degree of satisfaction of a base concept.


Description
-----------


The software models a specific type of fuzzy concept where the truth value is scaled or shifted according to a linear modifier, effectively representing a structure like ``(modifier C)``. By inheriting from a base modified concept class, it encapsulates a core concept and a modifier object, allowing the system to represent nuanced degrees of membership. Logical operations such as negation, conjunction, and disjunction are supported through operator overloading, which delegates the actual construction of complex expressions to a central operator handler. Additionally, structural integrity is maintained through methods that allow for the cloning of instances and the replacement of sub-concepts, facilitating dynamic manipulation of the concept hierarchy without mutating the original objects. The implementation also defines a hashing mechanism based on the internal components to ensure consistent object identity within collections.

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
       :width: 9.2cm
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

      Return a hash value for this object, computed from its string representation. This approach ensures that the hash value reflects the structural identity of the object without relying on cached values or additional methods. The hash is derived from the output of the `__str__` method, which provides a consistent and unique representation of the concept's structure. This implementation does not utilize any internal caching mechanism and directly computes the hash each time it is called.

      :return: An integer hash value representing the structural identity of this object.

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


