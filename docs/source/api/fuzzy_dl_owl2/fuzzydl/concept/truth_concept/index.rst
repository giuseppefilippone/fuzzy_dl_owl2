fuzzy_dl_owl2.fuzzydl.concept.truth_concept
===========================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.truth_concept



.. ── LLM-GENERATED DESCRIPTION START ──

Defines the logical constants Top and Bottom within a fuzzy description logic hierarchy to represent universal truth and contradiction.


Description
-----------


The implementation models the two extreme truth values, known as the universal concept (Top) and the contradictory concept (Bottom), which serve as the boundary conditions for the logical framework. By employing a singleton pattern, the design ensures that only a single shared instance exists for each truth value, optimizing memory usage and guaranteeing immutability across the ontology. Logical operations such as conjunction, disjunction, and negation are overridden to adhere to standard mathematical laws, where Top acts as an identity for conjunction and Bottom acts as an absorbing element. These constants are treated as atomic entities that cannot be decomposed further, providing a stable foundation for constructing more complex concept expressions within the system.

.. ── LLM-GENERATED DESCRIPTION END ──

Attributes
----------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.concept.truth_concept.BOTTOM
   fuzzy_dl_owl2.fuzzydl.concept.truth_concept.TOP


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.concept.truth_concept.TruthConcept


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_truth_concept_TruthConcept.png
       :alt: UML Class Diagram for TruthConcept
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **TruthConcept**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_truth_concept_TruthConcept.pdf
       :alt: UML Class Diagram for TruthConcept
       :align: center
       :width: 10.3cm
       :class: uml-diagram

       UML Class Diagram for **TruthConcept**

.. py:class:: TruthConcept(c_type: fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.concept.concept.Concept`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.concept.truth_concept.TruthConcept
      :parts: 1
      :private-bases:


   This class models the two extreme truth values within a logical concept hierarchy: the universal concept (Top) and the contradictory concept (Bottom). The Top concept represents a state that is always satisfied, acting as an identity element for conjunction and an absorbing element for disjunction, while the Bottom concept represents a state that is never satisfied, acting inversely. Instances can be created directly using a specific concept type or conveniently retrieved via the static factory methods `get_top` and `get_bottom`. It supports standard logical operations such as negation, conjunction, and disjunction, and is treated as an atomic entity that remains immutable during sub-concept replacement operations.

   :param name: The canonical string representation of the concept, which is "*top*" for the top concept and "*bottom*" for the bottom concept.
   :type name: typing.Any


   .. py:method:: __and__(value: Self) -> Self

      Implements the bitwise AND operation (`&`) for the concept, performing a logical conjunction with another instance. If the current instance represents the "Top" concept, the method returns the provided value, effectively acting as an identity element. If the current instance is not "Top," the method returns the bottom concept, resulting in the minimal element of the lattice regardless of the input value. This operation does not modify the state of the current instance or the provided value.

      :param value: The other operand in the logical conjunction.
      :type value: typing.Self

      :return: Returns the provided value if the current instance is the Top concept, otherwise returns the Bottom concept.

      :rtype: typing.Self



   .. py:method:: __eq__(value: Self) -> bool

      Determines equality between the current instance and another object by checking both type and string representation. The method returns True only if the provided value is an instance of the same class and its string representation matches that of the current instance. If the value is of a different type or the string representations differ, the method returns False.

      :param value: The object to compare against. Equality is determined by verifying the object is an instance of the same class and has an identical string representation.
      :type value: typing.Self

      :return: True if the provided value is an instance of TruthConcept and has the same string representation as this instance, otherwise False.

      :rtype: bool



   .. py:method:: __hash__() -> int

      Return a hash value for this object, computed from its string representation. This approach ensures that the hash value reflects the structural identity of the object without relying on cached values or additional methods. The hash is derived from the output of the `__str__` method, which provides a consistent and unique representation of the concept's structure. This implementation does not utilize any internal caching mechanism and directly computes the hash each time it is called.

      :return: An integer hash value representing the structural identity of this object.

      :rtype: int



   .. py:method:: __ne__(value: Self) -> bool

      Determines whether the current instance is not equal to the provided value by negating the result of the equality comparison. This method delegates the actual comparison logic to the `__eq__` method, meaning its behavior is directly tied to how equality is defined for the class. If the equality check returns `True`, this method returns `False`, and vice versa, ensuring consistency between the two operations.

      :param value: The object to compare against the current instance.
      :type value: typing.Self

      :return: True if the current instance is not equal to the specified value, False otherwise.

      :rtype: bool



   .. py:method:: __neg__() -> Self

      Implements the unary negation operator for the truth concept, effectively inverting its logical state. If the current instance represents the top concept (universal truth), this method returns a new instance representing the bottom concept (falsehood), and vice versa. This operation does not modify the original instance in place but instead returns a new `TruthConcept` object with the inverted type.

      :return: The logical negation of the concept, swapping Top for Bottom and vice versa.

      :rtype: typing.Self



   .. py:method:: __or__(value: Self) -> Self

      Implements the logical disjunction (OR) operation for the concept using the bitwise OR operator syntax. If the current instance represents the 'top' concept (often interpreted as 'true' or 'universal'), the method returns the top concept, effectively short-circuiting the result regardless of the other operand. Otherwise, the method returns the provided value. This operation does not modify the state of the current instance or the provided value.

      :param value: The right-hand operand for the disjunction operation, returned if the current instance is not Top.
      :type value: typing.Self

      :return: Returns the top concept if the current instance is the top concept; otherwise, returns the provided value.

      :rtype: typing.Self



   .. py:method:: __rshift__(value: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept

      Implements the right-shift operator (`>>`) to interact with another Concept. If the current instance is of type 'Top', the method returns the provided value. In all other cases, it returns the 'Top' concept.

      :param value: The Concept instance on the right-hand side of the operator.
      :type value: Concept

      :return: The result of the right-shift operation. Returns the provided value if the current concept is of type TOP; otherwise, returns the top concept.

      :rtype: Concept



   .. py:method:: clone() -> Self

      Creates and returns a new instance of `TruthConcept` that replicates the current object. The clone is initialized using the `type` attribute of the original instance, ensuring the new object shares the same type definition. This method does not modify the state of the original object, although if the `type` attribute is a mutable object, both the original and the clone will reference the same object.

      :return: A new instance of the class that is a copy of the current object.

      :rtype: typing.Self



   .. py:method:: compute_atomic_concepts() -> set[fuzzy_dl_owl2.fuzzydl.concept.concept.Concept]

      Computes the set of atomic concepts that constitute this entity. Since a `TruthConcept` represents a tautology or universal truth that does not decompose into specific atomic components, this method always returns an empty set. This implementation serves as a specific case where no further decomposition is required, and it does not modify the state of the object.

      :return: A set of the atomic concepts computed for this instance.

      :rtype: set[Concept]



   .. py:method:: compute_name() -> Optional[str]

      Calculates the canonical string name for the concept based on its type attribute. If the concept type is identified as TOP, the method returns the specific string '*top*', while a type of BOTTOM results in '*bottom*'. For any other concept types not explicitly handled by the logic, the method returns None.

      :return: Returns '*top*' if the concept type is TOP, '*bottom*' if it is BOTTOM, or None otherwise.

      :rtype: typing.Optional[str]



   .. py:method:: get_atomic_concepts() -> set[Self]

      Returns a singleton set containing the current instance, representing the atomic concepts that make up this object. This behavior indicates that the concept is indivisible or primitive, as it cannot be broken down into smaller constituent concepts. The operation has no side effects and consistently returns a set with exactly one element: the instance itself.

      :return: A set containing the current instance as the sole atomic concept.

      :rtype: set[typing.Self]



   .. py:method:: get_atoms() -> list[Self]

      Returns a list containing the current instance, representing the fundamental atomic components of the concept. This method signifies that the `TruthConcept` is an indivisible unit within the logical system, as opposed to composite structures that might decompose into multiple sub-concepts. The operation has no side effects and consistently returns a singleton list regardless of the internal state of the object.

      :return: A list containing the current instance.

      :rtype: list[typing.Self]



   .. py:method:: get_bottom()
      :staticmethod:


      Returns the shared singleton representing the bottom element of the conceptual hierarchy (a contradiction / the least defined state). The instance is created lazily on first access and cached.

      :return: The singleton Bottom concept.

      :rtype: TruthConcept



   .. py:method:: get_roles() -> set[str]

      Retrieves the set of string-based roles associated with this TruthConcept instance. The current implementation returns an empty set, signifying that no roles are assigned to this specific concept.

      :return: A set of strings representing the roles associated with the object.

      :rtype: set[str]



   .. py:method:: get_top()
      :staticmethod:


      Returns the shared singleton representing the universal ("Top") concept. The instance is created lazily on first access and cached, signifying the set of all possible individuals or the most general supertype in the ontology.

      :return: The singleton Top concept.

      :rtype: TruthConcept



   .. py:method:: is_atomic() -> bool

      Indicates whether the concept is atomic, representing a fundamental, indivisible unit of truth rather than a compound or derived expression. This method unconditionally returns `True`, signifying that instances of this class are always treated as base-level entities within the logical framework. As the return value is constant, there are no edge cases or side effects associated with this check.

      :return: True if the object is atomic.

      :rtype: bool



   .. py:method:: is_complemented_atomic() -> bool

      Indicates whether the truth concept represents a complemented atomic proposition, such as a negated literal. This implementation returns False, signifying that the concept is not of this specific type, though subclasses representing negated atomic variables may override this behavior. The method performs no side effects and serves as a predicate for logical classification or pattern matching within the module.

      :return: True if the object is a complemented atomic element.

      :rtype: bool



   .. py:method:: replace(a: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept

      Returns the current instance unchanged, acting as a no-op for the replacement operation. Because a `TruthConcept` is a terminal node representing a logical constant, it contains no internal structure or sub-concepts to traverse or modify. Consequently, regardless of the specific concepts provided as arguments, the method simply returns `self` to indicate that no substitution occurred.

      :param a: The concept to be replaced.
      :type a: Concept
      :param c: The concept to replace `a` with.
      :type c: Concept

      :return: The instance itself.

      :rtype: Concept



   .. py:attribute:: _BOTTOM
      :type:  Optional[Self]
      :value: None



   .. py:attribute:: _TOP
      :type:  Optional[Self]
      :value: None



   .. py:attribute:: name
      :value: '*top*'



.. py:data:: BOTTOM
   :type:  fuzzy_dl_owl2.fuzzydl.concept.concept.Concept
   :value: None


.. py:data:: TOP
   :type:  fuzzy_dl_owl2.fuzzydl.concept.concept.Concept
   :value: None

