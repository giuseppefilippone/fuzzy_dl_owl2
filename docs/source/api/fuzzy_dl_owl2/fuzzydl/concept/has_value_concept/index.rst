fuzzy_dl_owl2.fuzzydl.concept.has_value_concept
===============================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.has_value_concept





.. ── LLM-GENERATED DESCRIPTION START ──

Defines a fuzzy description-logic concept expressing a "has-value" existential restriction — the form *(b-some r v)* — satisfied by any individual connected to one specific value through a given role.


Description
-----------


HasValueConcept is the concrete realisation of one of the simplest forms of existential quantification supported by the fuzzy DL framework: rather than requiring a role filler drawn from an entire class expression, it pins the filler down to a single concrete value, which may be a string, a number, or any other object. It is assembled through multiple inheritance, combining the generic Concept machinery (which tags instances with the HAS_VALUE concept type) with the HasValueInterface mixin that supplies the role and value attributes, keeping the role/value pairing logic in one place so it can be shared with other value-based constructs. At construction time a canonical name of the form *(b-some role value)* is derived automatically, giving every instance a stable, printable identity; hashing is likewise computed from the concept type, role, and value together, so two restrictions with identical role and value behave as equal inside sets and dictionaries.

Because a has-value restriction is semantically atomic — it contains no nested sub-concepts to traverse or rewrite — the implementation deliberately treats it as a leaf node: it reports no atomic concepts and no roles, and it refuses to perform concept substitution, logging an error instead of attempting a replacement. Composition with other class expressions is still fully supported through operator overloading, with unary minus, ``&``, and ``|`` delegating to OperatorConcept to build negations, conjunctions, and disjunctions, so has-value restrictions can participate freely in larger logical formulas. A factory-style static constructor and a clone method round out the API; cloning currently produces a fresh instance that shares the original value rather than deep-copying it, a trade-off that keeps duplication cheap at the cost of aliasing the underlying value object.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.concept.has_value_concept.HasValueConcept


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_has_value_concept_HasValueConcept.png
       :alt: UML Class Diagram for HasValueConcept
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **HasValueConcept**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_has_value_concept_HasValueConcept.pdf
       :alt: UML Class Diagram for HasValueConcept
       :align: center
       :width: 9.4cm
       :class: uml-diagram

       UML Class Diagram for **HasValueConcept**

.. py:class:: HasValueConcept(role: str, value: Any)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.concept.concept.Concept`, :py:obj:`fuzzy_dl_owl2.fuzzydl.concept.interface.has_value_interface.HasValueInterface`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.concept.has_value_concept.HasValueConcept
      :parts: 1
      :private-bases:


   This class models a specific type of existential restriction, often referred to as a "has-value" concept, which asserts that an individual must be related to a specific value through a defined role. Structurally, it represents the logical form `(b-some r v)`, meaning an entity satisfies this concept if it participates in the relationship `r` with a target entity that corresponds to `v`. To utilize this class, instantiate it by providing a string representing the role and the target value, which can be of various types such as strings or numbers. Once created, the concept can be combined with other concepts using standard logical operators like conjunction, disjunction, and negation, and it automatically generates a standardized string representation for identification. Note that attempting to replace sub-concepts within this specific concept type will result in an error, as it is treated as an atomic unit in that context.

   :param name: String representation of the concept in the format (b-some role value).
   :type name: str


   .. py:method:: __and__(value: Self) -> Self

      Performs a bitwise AND operation between the current instance and another value of the same type, enabling the use of the `&` operator. The logic is delegated to `OperatorConcept.and_`, which constructs and returns a new instance representing the conjunction of the two operands. This method generally does not modify the original instances, but may raise an error if the provided value is not a compatible type.

      :param value: The other operand to combine with the current instance using the AND operation.
      :type value: typing.Self

      :return: The result of the AND operation between the current instance and the provided value.

      :rtype: typing.Self



   .. py:method:: __hash__() -> int

      Return a hash value for this object, computed from its string representation. This approach ensures that the hash value reflects the structural identity of the object without relying on cached values or additional methods. The hash is derived from the output of the `__str__` method, which provides a consistent and unique representation of the concept's structure. This implementation does not utilize any internal caching mechanism and directly computes the hash each time it is called.

      :return: An integer hash value representing the structural identity of this object.

      :rtype: int



   .. py:method:: __neg__() -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept

      Overloads the unary minus operator to provide the logical negation of the current concept. This method returns a new `Concept` instance representing the inverse condition of the original object, effectively wrapping it in a logical 'NOT' operation by delegating to `OperatorConcept.not_`. The operation is side-effect free, leaving the original instance unmodified.

      :return: The logical negation of this concept.

      :rtype: Concept



   .. py:method:: __or__(value: Self) -> Self

      Performs a logical OR operation between the current concept and another value using the bitwise OR operator (`|`). This method delegates the logic to `OperatorConcept.or_`, constructing and returning a new instance that represents the combination of the two operands. It allows for the chaining or composition of concepts without modifying the original objects.

      :param value: The right-hand operand for the OR operation, which must be an instance of the same class.
      :type value: typing.Self

      :return: A new instance representing the logical OR of the current object and the provided value.

      :rtype: typing.Self



   .. py:method:: clone() -> Self

      Creates and returns a new instance of the class that is a deep copy of the current object. The new instance preserves the `role` attribute from the original, while the `value` attribute is recursively copied using `copy.deepcopy` to ensure that modifications to the new object's value do not affect the original. This method is useful for creating independent duplicates of the concept without altering the source data, though it may raise an exception if the value contains objects that cannot be deep-copied.

      :return: A new instance of the class with the same role and a deep copy of the value.

      :rtype: typing.Self



   .. py:method:: compute_atomic_concepts() -> set[fuzzy_dl_owl2.fuzzydl.concept.concept.Concept]

      Returns an empty set, as a `HasValueConcept` does not decompose into or reference any atomic named concepts. Unlike complex class expressions that might be unions or intersections of other classes, a `HasValue` restriction is defined solely by a property and a specific filler value, meaning there are no atomic concepts to extract. This method has no side effects and consistently returns an empty set regardless of the internal state of the concept.

      :return: A set of atomic concepts computed by the object.

      :rtype: set[Concept]



   .. py:method:: compute_name() -> Optional[str]

      Constructs a string identifier for the concept by interpolating its role and value attributes into a specific parenthetical format. The output follows the pattern '(b-some role value)', serving as a computed name for the entity. This method does not modify the object's state and assumes that the `role` and `value` attributes are available for string formatting.

      :return: A string representing the computed name, formatted as "(b-some {role} {value})".

      :rtype: typing.Optional[str]



   .. py:method:: get_roles() -> set[str]

      Retrieves the set of roles associated with the current concept. This default implementation returns an empty set, signifying that no roles are inherently defined for this base concept. The method is designed to be overridden by subclasses to return specific role identifiers as strings, allowing for the extension of functionality within the broader module hierarchy. Because a new set instance is created on every invocation, the operation has no side effects on the object's state.

      :return: A set of strings representing the roles assigned to the object.

      :rtype: set[str]



   .. py:method:: has_value(role: str, i: Any) -> Self
      :staticmethod:


      Creates and returns a new instance of the `HasValueConcept` class, associating a specific value with a defined role. This static method acts as a factory function, allowing for the instantiation of the concept using a role identifier and an arbitrary value of any type. Since the method simply delegates to the class constructor, it has no side effects and relies on the underlying class implementation for any input validation or processing.

      :param role: A string identifying the role or name of the value.
      :type role: str
      :param i: The value to be associated with the specified role.
      :type i: typing.Any

      :return: An instance of HasValueConcept initialized with the provided role and value.

      :rtype: typing.Self



   .. py:method:: replace(a: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept

      This method attempts to replace a specified concept `a` with another concept `c` within the current object's structure. However, this functionality is not supported for `HasValueConcept` instances; invoking it results in an error being reported and the method returning `None` rather than performing a substitution.

      :param a: The concept to be replaced within the current structure.
      :type a: Concept
      :param c: The concept to use as the replacement.
      :type c: Concept

      :return: None, after logging an error indicating that the replacement operation is not supported.

      :rtype: Concept



   .. py:attribute:: name
      :type:  str
