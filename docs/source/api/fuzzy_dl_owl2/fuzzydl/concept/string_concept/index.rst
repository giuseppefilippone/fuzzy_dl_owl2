fuzzy_dl_owl2.fuzzydl.concept.string_concept
============================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.string_concept



.. ── LLM-GENERATED DESCRIPTION START ──

An atomic representation of string literals designed for use within a fuzzy description logic system.


Description
-----------


The software extends the base concept hierarchy to encapsulate textual data, such as names or labels, as indivisible leaf nodes within the logic framework. By design, it enforces strict semantic rules that forbid logical negation or complementation, raising an exception if such operations are attempted to maintain the integrity of the system. Structural replacement operations are supported by returning the instance itself, ensuring that the object maintains its identity throughout transformations. Identity comparisons and hashing rely on a standardized, quoted format of the internal string value, allowing the component to function consistently as a fundamental building block in broader logical expressions.

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

      Return a hash value for this object, computed from its string representation. This approach ensures that the hash value reflects the structural identity of the object without relying on cached values or additional methods. The hash is derived from the output of the `__str__` method, which provides a consistent and unique representation of the concept's structure. This implementation does not utilize any internal caching mechanism and directly computes the hash each time it is called.

      :return: An integer hash value representing the structural identity of this object.

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

