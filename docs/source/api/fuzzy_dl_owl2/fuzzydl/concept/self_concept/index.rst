fuzzy_dl_owl2.fuzzydl.concept.self_concept
==========================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.self_concept



.. ── LLM-GENERATED DESCRIPTION START ──

Implements a self-referential concept within fuzzy description logic that signifies an individual satisfies a relationship with itself through a specified role.


Description
-----------


The software models a specific type of atomic concept used to express reflexivity or local reflexivity properties, ensuring that an entity is linked to itself via a defined role. By inheriting from a base concept class and a role interface, the implementation encapsulates a role string and automatically generates a standardized string representation formatted as a self-referential expression. It supports logical manipulation through operator overloading, allowing instances to be combined using conjunction, disjunction, and negation by delegating these operations to a central operator handler. Additional functionality includes cloning capabilities, role retrieval, and hash computation based on the string representation, enabling the concept to function effectively within larger logical structures and collections like sets or dictionaries.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.concept.self_concept.SelfConcept


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_self_concept_SelfConcept.png
       :alt: UML Class Diagram for SelfConcept
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **SelfConcept**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_self_concept_SelfConcept.pdf
       :alt: UML Class Diagram for SelfConcept
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **SelfConcept**

.. py:class:: SelfConcept(role: str)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.concept.concept.Concept`, :py:obj:`fuzzy_dl_owl2.fuzzydl.concept.interface.has_role_interface.HasRoleInterface`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.concept.self_concept.SelfConcept
      :parts: 1
      :private-bases:


   Represents a self-referential concept within fuzzy description logic, specifically denoting that an individual satisfies a relationship with itself through a given role. This construct is essential for expressing reflexivity or local reflexivity properties, where an entity must be linked to itself via the specified role to satisfy the concept. To utilize this class, instantiate it by providing the specific role name as a string, which will automatically generate a standardized string representation. Once created, it behaves as an atomic concept that can be combined with other concepts using logical operators such as conjunction, disjunction, and negation, and it supports cloning and role retrieval operations.

   :param name: The canonical string representation of the concept, formatted as "(self role)".
   :type name: typing.Any


   .. py:method:: __and__(value: Self) -> Self

      Performs a logical conjunction between the current concept and another provided concept, enabling the use of the bitwise AND operator (`&`) to combine them. This method returns a new instance representing the intersection or combination of the two operands, leaving the original concepts unmodified. The actual logic is delegated to `OperatorConcept.and_`, which handles the specifics of the conjunction operation. While the method expects a value of the same type, specific behaviors regarding incompatible inputs or contradictory concepts are determined by the underlying operator implementation.

      :param value: The right-hand operand for the AND operation.
      :type value: typing.Self

      :return: The result of the bitwise AND operation between this instance and the provided value.

      :rtype: typing.Self



   .. py:method:: __hash__() -> int

      Computes an integer hash value for the object based on its string representation. By delegating to the hash of `str(self)`, this method ensures that the hash is consistent with the object's textual output, allowing instances to be used as dictionary keys or stored in sets. This implementation implies that the hashability of the object is directly tied to the stability and uniqueness of its string representation.

      :return: An integer representing the hash of the object's string representation.

      :rtype: int



   .. py:method:: __neg__() -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept

      Implements the unary negation operator for the concept, allowing the use of the minus sign (`-`) to represent logical negation. This method returns a new `Concept` instance that serves as the logical complement of the current object by delegating the operation to `OperatorConcept.not_`. The original concept remains unmodified, as the operation produces a distinct entity representing the 'not' state.

      :return: A new Concept representing the logical negation (NOT) of the current concept.

      :rtype: Concept



   .. py:method:: __or__(value: Self) -> Self

      Implements the bitwise OR operator (`|`) to perform a logical disjunction or union between the current concept and another concept of the same type. This method delegates the actual computation to `OperatorConcept.or_`, ensuring consistent handling of the operation logic. It returns a new instance representing the combined concept, leaving the original operands unmodified. If the provided value is not a compatible concept, the underlying implementation may raise a TypeError.

      :param value: The right-hand operand to combine with the current instance using the OR operation.
      :type value: typing.Self

      :return: A new instance representing the logical OR of the current instance and the provided value.

      :rtype: typing.Self



   .. py:method:: clone()

      Creates and returns a new `SelfConcept` instance that duplicates the current object, initialized with the same `role` attribute. This method performs a shallow copy of the object's state, meaning the new instance shares the reference to the original `role` object if it is mutable. The operation has no side effects on the original instance.



   .. py:method:: compute_atomic_concepts() -> set[fuzzy_dl_owl2.fuzzydl.concept.concept.Concept]

      Computes and returns the set of atomic concepts that constitute this entity. By returning a set containing only the instance itself, the method indicates that this concept is atomic and cannot be decomposed into smaller constituent concepts. The operation is stateless and has no side effects, as it merely constructs and returns a new set containing the current object.

      :return: A set containing the concept itself.

      :rtype: set[Concept]



   .. py:method:: compute_name() -> Optional[str]

      Constructs and returns a string representation of the self-concept by embedding the instance's role into a specific format. The output follows the pattern '(self {role})', where the placeholder is replaced by the value of the `role` attribute. This method performs a read-only operation and assumes the `role` attribute is accessible on the instance.

      :return: A string representing the computed name, formatted as "(self {role})".

      :rtype: typing.Optional[str]



   .. py:method:: get_roles() -> set[str]

      Retrieves the specific role assigned to the instance and returns it as a set containing a single string element. This method encapsulates the internal `role` attribute, ensuring the return type is always a collection for consistency with other methods that may handle multiple roles. The function has no side effects on the instance's state, and because it returns a new set object, any modifications made to the result will not impact the original data.

      :return: A set containing the role associated with the instance.

      :rtype: set[str]



   .. py:method:: replace(a: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept

      Returns the current instance unchanged, acting as a base case for replacement operations. Since a SelfConcept does not contain nested or child concepts, there are no internal structures to substitute. The method ignores the source and replacement concepts provided as arguments and simply returns the object itself.

      :param a: The concept to be replaced.
      :type a: Concept
      :param c: The concept to substitute for `a`.
      :type c: Concept

      :return: Returns the instance itself.

      :rtype: Concept



   .. py:method:: self(role: str) -> Self
      :staticmethod:


      This static method acts as a factory function for creating new instances of the `SelfConcept` class. It accepts a single string argument representing the role, which is passed directly to the class constructor during initialization. The method returns a new `SelfConcept` object configured with the provided role.

      :param role: The role or persona defining the self-concept.
      :type role: str

      :return: A new instance of the class representing the self concept for the specified role.

      :rtype: typing.Self



   .. py:attribute:: name
      :value: '(self Uninferable)'


      Updates the name of the Concept instance to the specified string value. This setter modifies the object's internal state by assigning the provided value to the private `_name` attribute, effectively replacing any previously stored name.

      :param value: The new name to assign to the object.
      :type value: str

