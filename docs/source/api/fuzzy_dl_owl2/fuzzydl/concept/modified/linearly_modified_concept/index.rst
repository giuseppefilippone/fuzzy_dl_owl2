fuzzy_dl_owl2.fuzzydl.concept.modified.linearly_modified_concept
================================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.modified.linearly_modified_concept







.. ── LLM-GENERATED DESCRIPTION START ──

Models a fuzzy description-logic concept whose degree of satisfaction is linearly transformed by a modifier, producing expressions of the form (modifier C).


Description
-----------


``LinearlyModifiedConcept`` pairs a base concept with a linear modifier that scales or shifts the concept's truth value, enabling fuzzy ontologies to express hedged notions such as "very" or "more or less" applied to arbitrary concepts. Instances behave as immutable values: cloning, sub-concept replacement, and every logical operation return fresh objects rather than mutating the original, so modified concepts can be shared safely throughout a knowledge base without aliasing side effects. Negation, conjunction, and disjunction are exposed through Python's operator protocol (``-``, ``&``, ``|``) and delegated to a central operator-concept factory, keeping the concept algebra consistent and allowing modified expressions to compose seamlessly with all other concept types. Substitution of a sub-concept deliberately diverges from the original Java implementation, whose version negated its result — apparently a copy-paste of the complement operation — and instead preserves polarity in line with the replacement contract honoured by every other concept. Hashing is derived from the base concept, the modifier, the concept's name, and its type, so objects compare by structure rather than identity and behave correctly as dictionary keys or set members.

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
