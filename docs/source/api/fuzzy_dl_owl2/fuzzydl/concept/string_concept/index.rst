fuzzy_dl_owl2.fuzzydl.concept.string_concept
============================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.string_concept



.. ── LLM-GENERATED DESCRIPTION START ──

Defines an atomic concept representation for string literals that enforces specific logical constraints within a fuzzy description logic system.


Description
-----------


Extending the base concept hierarchy, the implementation models atomic string literals as indivisible leaf nodes within a fuzzy description logic framework. It encapsulates textual data by enforcing a standardized quoted format for identification and ensures that these values cannot be decomposed into sub-concepts or associated with roles. A critical design constraint involves the explicit prohibition of logical negation or complementation, which triggers an exception to uphold the semantic integrity of the logic system. Furthermore, the logic supports structural replacement operations by maintaining its own identity and relies on the formatted string representation to determine hash values and equality comparisons.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.concept.string_concept.StringConcept


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_string_concept_StringConcept.png
       :alt: UML Class Diagram for StringConcept
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **StringConcept**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_string_concept_StringConcept.pdf
       :alt: UML Class Diagram for StringConcept
       :align: center
       :width: 11.3cm
       :class: uml-diagram

       UML Class Diagram for **StringConcept**

.. py:class:: StringConcept(name: str)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.concept.concept.Concept`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.concept.string_concept.StringConcept
      :parts: 1
      :private-bases:


   This class functions as an atomic representation of a specific string literal within a fuzzy description logic framework, designed to encapsulate textual data such as names or labels. It extends the base concept hierarchy to provide a standardized, quoted format for identifying these values, ensuring they are treated as indivisible leaf nodes that cannot be decomposed into sub-concepts or associated roles. A key behavioral constraint is that this entity explicitly forbids logical negation or complementation, raising an exception if such an operation is attempted, thereby enforcing the semantic rules of the logic system. Additionally, it supports structural replacement operations by returning itself, maintaining its identity while relying on its formatted string representation for hashing and equality comparisons.

   :param _name: Internal storage for the raw string literal value encapsulated by the concept.
   :type _name: str

   :raises FuzzyOntologyException: Raised when the negation operator is applied to a StringConcept, as atomic string concepts cannot be complemented in fuzzy description logic.


   .. py:method:: __hash__() -> int

      Calculates the hash value for the instance by delegating to the hash of its string representation. This behavior ensures that the object is hashable, allowing it to be utilized as a key in dictionaries or as a member of sets. The method relies on the `__str__` implementation of the class, meaning that any two instances producing identical string representations will yield the same hash code, which is essential for maintaining consistency with equality comparisons.

      :return: An integer hash value derived from the string representation of the object.

      :rtype: int



   .. py:method:: __neg__() -> Self

      This method defines the behavior of the unary negation operator for the concept, which in this context represents logical complementation. Since string-based concepts do not support complementation, this method always raises a FuzzyOntologyException to signal that the operation is invalid for this type.

      :raises FuzzyOntologyException: Raised when attempting to negate a string, as strings cannot be complemented.

      :return: Raises FuzzyOntologyException because strings cannot be complemented.

      :rtype: typing.Self



   .. py:method:: clone() -> Self

      Creates and returns a distinct copy of the current `StringConcept` instance. The new object is initialized with the same `name` attribute as the original, effectively duplicating its state. Since a new object is constructed, modifications to the returned instance will not affect the original object, and this method has no side effects on the source.

      :return: A new instance of the class initialized with the same name as the current object.

      :rtype: typing.Self



   .. py:method:: compute_atomic_concepts() -> set[Self]

      Calculates and returns the set of atomic concepts that constitute this specific string concept. Since a `StringConcept` is treated as a primitive or indivisible unit within the concept hierarchy, it contains no further sub-concepts, resulting in an empty set being returned. This method has no side effects and consistently returns an empty set regardless of the instance's internal state.

      :return: A set of atomic concepts derived from the current object.

      :rtype: set[typing.Self]



   .. py:method:: compute_name() -> str | None

      Retrieves the internal name attribute of the instance and returns it formatted as a quoted string literal. The method wraps the value of `self.name` in double quotes, producing a string representation suitable for display or serialization. If the `name` attribute is not set on the instance, an `AttributeError` will be raised, while a `None` value for the name will result in the string `"None"`.

      :return: The name enclosed in double quotes.

      :rtype: str | None



   .. py:method:: get_roles() -> set[str]

      Returns a collection of roles associated with the concept. Since this is a base implementation, it always returns an empty set, implying that no roles are currently defined for this specific type of concept. The method has no side effects and is designed to be overridden by subclasses to provide specific role logic.

      :return: A set of strings representing the roles associated with the object.

      :rtype: set[str]



   .. py:method:: replace(a: Self, c: Self) -> Self | None

      Returns the instance itself without performing any replacement operation or modifying the object's state. The method accepts two arguments, `a` and `c`, which are ignored during execution. Consequently, calling this method has no side effects and simply returns the original object.

      :param a: The instance to be replaced.
      :type a: typing.Self
      :param c: The value to substitute for the original element.
      :type c: typing.Self

      :return: Returns the instance itself.

      :rtype: typing.Self | None



   .. py:attribute:: _name
      :type:  str

