fuzzy_dl_owl2.fuzzydl.concept.value_concept
===========================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.value_concept



.. ── LLM-GENERATED DESCRIPTION START ──

Implements a specialized concept class for representing numerical value restrictions, such as "at most" or "at least," within a fuzzy description logic system.


Description
-----------


The software provides a mechanism to encapsulate numerical constraints associated with specific roles, supporting logic such as upper bounds, lower bounds, and exact matches. By inheriting from a base concept class and a value interface, it integrates seamlessly into a broader hierarchy of logical constructs while ensuring that specific constraint types are strictly validated during initialization. Static factory methods are employed to simplify the instantiation of these constraints, allowing for readable code that clearly defines the nature of the restriction without requiring manual specification of enumeration types. As a terminal node within the concept structure, it handles operations like cloning and replacement by returning itself or shallow copies, while logical conjunctions, disjunctions, and negations are delegated to a separate operator handler to maintain separation of concerns.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.concept.value_concept.ValueConcept


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_value_concept_ValueConcept.png
       :alt: UML Class Diagram for ValueConcept
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **ValueConcept**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_value_concept_ValueConcept.pdf
       :alt: UML Class Diagram for ValueConcept
       :align: center
       :width: 13.1cm
       :class: uml-diagram

       UML Class Diagram for **ValueConcept**

.. py:class:: ValueConcept(c_type: fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType, role: str, value: Any)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.concept.concept.Concept`, :py:obj:`fuzzy_dl_owl2.fuzzydl.concept.interface.has_value_interface.HasValueInterface`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.concept.value_concept.ValueConcept
      :parts: 1
      :private-bases:


   This class represents a value restriction used to define numerical constraints on the fillers of a specific role within a description logic system. It encapsulates concepts such as "at most," "at least," or "exactly" a certain number of related individuals, allowing for the precise definition of cardinality restrictions. Users can instantiate this object by specifying a concept type, a role, and a value, or utilize the provided static factory methods for more readable creation. The class automatically generates a string representation of the constraint and integrates with the broader concept hierarchy, supporting logical operations while acting as a terminal node that does not decompose into sub-concepts.

   :param name: The string representation of the concept, formatted as a parenthesized expression combining the operator, role, and value.
   :type name: typing.Any


   .. py:method:: __and__(value: Self) -> Self

      Performs a logical conjunction or intersection by implementing the bitwise AND operator (`&`) for the instance. This method delegates the core logic to `OperatorConcept.and_`, passing the current object and the provided value to generate the result. The operation returns a new instance of the same type representing the combined concept, leaving the original operands unmodified, and expects the input value to be compatible with the underlying implementation.

      :param value: Another instance of the same class to perform the AND operation with.
      :type value: typing.Self

      :return: The result of the AND operation between the current instance and the provided value.

      :rtype: typing.Self



   .. py:method:: __hash__() -> int

      Return a hash value for this object, computed from its string representation. This approach ensures that the hash value reflects the structural identity of the object without relying on cached values or additional methods. The hash is derived from the output of the `__str__` method, which provides a consistent and unique representation of the concept's structure. This implementation does not utilize any internal caching mechanism and directly computes the hash each time it is called.

      :return: An integer hash value representing the structural identity of this object.

      :rtype: int



   .. py:method:: __neg__() -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept

      Implements the unary negation operator for the value concept, enabling the use of the minus sign to invert the instance. It returns a new `Concept` object representing the logical negation of the current object by delegating to `OperatorConcept.not_`. This operation does not modify the original instance but instead produces a distinct concept that encapsulates the NOT logic.

      :return: A new Concept representing the logical negation of the current instance.

      :rtype: Concept



   .. py:method:: __or__(value: Self) -> Self

      Implements the bitwise OR operation for the `ValueConcept` class, allowing instances to be combined using the `|` operator. This method takes another instance of the same type and delegates the logic to `OperatorConcept.or_` to compute the disjunction. It returns a new `ValueConcept` instance representing the result of the operation, leaving the original operands unchanged.

      :param value: Another instance of the same type to perform the OR operation with.
      :type value: typing.Self

      :return: The result of the logical OR operation between this instance and the provided value.

      :rtype: typing.Self



   .. py:method:: at_least_value(role: str, o: Any) -> Self
      :staticmethod:


      This static method acts as a factory for creating a specific type of constraint object, instantiating a `ValueConcept` that represents a minimum threshold or "greater than or equal to" condition. It accepts a string defining the role of the concept and an arbitrary object representing the target value, which are passed to the constructor along with the `AT_LEAST_VALUE` type indicator. The function returns a new instance of the class, encapsulating the provided data within the context of this specific constraint logic without modifying any global state.

      :param role: The identifier or name of the role that the minimum value constraint applies to.
      :type role: str
      :param o: The threshold value or object defining the lower bound of the concept.
      :type o: typing.Any

      :return: Returns an instance representing a concept where the value associated with the specified role is greater than or equal to the provided object.

      :rtype: typing.Self



   .. py:method:: at_most_value(role: str, o: Any) -> Self
      :staticmethod:


      Constructs a `ValueConcept` instance representing a constraint where the value associated with a specific role is less than or equal to a given limit. This static method accepts a string identifying the role and an arbitrary object representing the maximum value, initializing the concept with the `AT_MOST_VALUE` type. The method acts as a factory that wraps the provided value directly without performing validation or side effects.

      :param role: The role or identifier for the value within the concept.
      :type role: str
      :param o: The value representing the upper bound or maximum limit.
      :type o: typing.Any

      :return: Returns a ValueConcept instance representing an "at most" constraint for the specified role and value.

      :rtype: typing.Self



   .. py:method:: clone() -> Self

      Creates and returns a new instance of `ValueConcept` that is a copy of the current object. The new instance is initialized with the same `type`, `role`, and `value` attributes as the original. This method performs a shallow copy, meaning that if the `value` attribute is a mutable object, the clone will reference the same underlying object as the original; therefore, modifications to that mutable object will be reflected in both instances. The original object remains unmodified by this operation.

      :return: A new instance of the class with the same type, role, and value as the current object.

      :rtype: typing.Self



   .. py:method:: compute_atomic_concepts() -> set[fuzzy_dl_owl2.fuzzydl.concept.concept.Concept]

      Computes the set of atomic concepts associated with this entity. Since this is a `ValueConcept`, representing a concrete value rather than a complex type or class definition, it does not decompose into further atomic concepts. Consequently, the method always returns an empty set, indicating that no atomic concepts are derived from this specific node. This operation has no side effects.

      :return: A set of atomic concepts associated with the object.

      :rtype: set[Concept]



   .. py:method:: compute_name() -> Optional[str]

      Generates a formatted string representation of the concept based on its type, role, and value attributes. For 'at most' constraints, it returns a string formatted as '(<= role value)', while 'at least' constraints produce '(>= role value)' and exact values produce '(= role value)'. If the concept type does not correspond to one of these specific value constraints, the method returns None. This operation does not modify the object's state.

      :return: A string representing the concept as a logical constraint (e.g., '(<= role value)') based on its type, role, and value, or None if the type is not a specific value constraint.

      :rtype: typing.Optional[str]



   .. py:method:: exact_value(role: str, o: Any) -> Self
      :staticmethod:


      Creates a `ValueConcept` instance representing an exact value by wrapping a provided object and role string. This static method serves as a specialized factory that tags the resulting concept with the `EXACT_VALUE` type, distinguishing it from other concept types. It accepts any Python object as the value payload and has no side effects, simply returning a new instance initialized with the specified arguments.

      :param role: The role or identifier for the exact value.
      :type role: str
      :param o: The specific value or object to be encapsulated by the concept.
      :type o: typing.Any

      :return: A new instance representing an exact value concept associated with the specified role and object.

      :rtype: typing.Self



   .. py:method:: get_roles() -> set[str]

      Retrieves the set of roles associated with the `ValueConcept` instance. This implementation returns an empty set, indicating that the base concept does not possess any specific roles. The method has no side effects and does not rely on the object's internal state.

      :return: A set of strings representing the roles associated with the object.

      :rtype: set[str]



   .. py:method:: replace(a: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept

      Returns the current instance unmodified, acting as a terminal case for replacement operations within a concept hierarchy. Since a ValueConcept represents an atomic value that does not contain nested concepts, it cannot perform a substitution of sub-components. As a result, the arguments `a` and `c` are ignored, and the method returns `self` to preserve the structure when traversing or transforming composite concepts.

      :param a: The concept to be replaced.
      :type a: Concept
      :param c: The concept to substitute in place of `a`.
      :type c: Concept

      :return: The concept itself, returned unchanged.

      :rtype: Concept



   .. py:attribute:: name

