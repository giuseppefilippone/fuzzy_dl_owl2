fuzzy_dl_owl2.fuzzydl.concept.atomic_concept
============================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.atomic_concept



.. ── LLM-GENERATED DESCRIPTION START ──

Defines the AtomicConcept class as an indivisible base unit within a conceptual hierarchy, serving as the fundamental building block for constructing complex logical expressions.


Description
-----------


The class represents the most granular element in the system, identified uniquely by a string name, and functions as a leaf node that cannot be decomposed further into sub-concepts. To facilitate the construction of complex logical structures, it overloads standard Python operators for conjunction, disjunction, and negation, delegating the actual creation of composite objects to a separate operator class. Identity and comparison rely strictly on the assigned name, ensuring that distinct instances with identical labels are treated as the same entity, which is crucial for hashing and storage in collections. Traversal and manipulation methods, such as retrieving atomic components or performing replacements, consistently return the instance itself or a singleton collection, acting as the base case for recursive algorithms operating on the concept graph. Additionally, a static factory method enables the automatic generation of unique identifiers using a global counter, supporting the dynamic creation of concepts during runtime.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.concept.atomic_concept.AtomicConcept


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_atomic_concept_AtomicConcept.png
       :alt: UML Class Diagram for AtomicConcept
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **AtomicConcept**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_atomic_concept_AtomicConcept.pdf
       :alt: UML Class Diagram for AtomicConcept
       :align: center
       :width: 11.8cm
       :class: uml-diagram

       UML Class Diagram for **AtomicConcept**

.. py:class:: AtomicConcept(name: str)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.concept.concept.Concept`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.concept.atomic_concept.AtomicConcept
      :parts: 1
      :private-bases:


   This entity serves as a fundamental, indivisible unit within a conceptual hierarchy, representing a base concept that is not defined by or composed of other concepts. It can be instantiated directly with a specific string name or generated automatically via the static factory method to ensure unique identifiers. As a leaf node in the structure, it supports standard logical operations such as conjunction, disjunction, and negation, where negation transforms it into a complex operator concept. The class defines equality and hashing based strictly on its name, ensuring that two instances with the same name are considered identical, and it provides methods for cloning, replacement, and traversal that consistently return itself or a singleton set containing itself.


   .. py:method:: __and__(value: Self) -> Self

      Computes the logical conjunction of the current concept with another concept, enabling the use of the `&` operator. This method delegates the evaluation to `OperatorConcept.and_`, which handles the specific logic for combining the two atomic concepts and returns a new instance representing the result. The operation is non-destructive, leaving the original operands unchanged, and relies on the underlying implementation of `OperatorConcept` to handle potential simplifications or edge cases inherent to the conjunction logic.

      :param value: The right-hand operand for the AND operation, which must be of the same type as the current instance.
      :type value: typing.Self

      :return: A new instance representing the result of the AND operation between this instance and the provided value.

      :rtype: typing.Self



   .. py:method:: __eq__(value: Self) -> bool

      Determines whether the provided object is equal to the current instance by first verifying that the object is an instance of the same class. If the type check passes, the method compares the string representations of the two instances to determine equality. This implementation ensures that objects of different types are never considered equal, even if their string representations happen to match.

      :param value: The object to compare against. Equality is determined by matching string representations, provided the object is an instance of the same class.
      :type value: typing.Self

      :return: True if the provided value is an instance of AtomicConcept and has the same string representation as this instance, otherwise False.

      :rtype: bool



   .. py:method:: __hash__() -> int

      Computes the hash value for the instance based on the `name` attribute, allowing `AtomicConcept` objects to be used as dictionary keys or stored in sets. The method delegates the hashing operation to the `name` property, ensuring that instances with identical names produce the same hash. It is important that the `name` attribute remains immutable for the lifetime of the object, as modifying it would change the hash value and potentially corrupt hash-based collections.

      :return: An integer representing the hash of the object's `name` attribute.

      :rtype: int



   .. py:method:: __invert__() -> Self

      Implements the behavior of the bitwise NOT operator (tilde `~`) for the concept, returning the negation of the current instance. This method effectively delegates to the unary minus operator, producing a new object that represents the inverse of the original value without modifying the instance in place. If the underlying data structure does not support negation, this operation will raise a TypeError.

      :return: The arithmetic negation of the instance.

      :rtype: typing.Self



   .. py:method:: __ne__(value: Self) -> bool

      Determines whether the current instance is not equal to the provided value by returning the negation of the equality comparison. This method ensures that the inequality operator behaves consistently with the class's definition of equality. It does not modify the state of the object, though it may propagate exceptions raised by the underlying equality check if the types are incompatible.

      :param value: The instance to compare against for inequality.
      :type value: typing.Self

      :return: True if the current instance is not equal to the specified value, False otherwise.

      :rtype: bool



   .. py:method:: __neg__() -> Self

      Implements the unary negation operator, providing a syntactic shortcut to represent the logical complement of the concept. When invoked, this method delegates to the `OperatorConcept.not_` class method to generate a new object that encapsulates the negation of the current instance. This operation is side-effect free with respect to the original object, as it produces a new entity rather than modifying the existing state.

      :return: A new instance representing the logical negation of the current concept.

      :rtype: typing.Self



   .. py:method:: __or__(value: Self) -> Self

      Implements the bitwise OR operator (`|`) to perform a logical disjunction between the current concept and another provided concept. This method delegates the actual construction of the resulting concept to `OperatorConcept.or_`, returning a new instance that represents the combination of the two operands without modifying the original objects.

      :param value: The right-hand operand to perform the OR operation with.
      :type value: typing.Self

      :return: An instance representing the logical OR of the current object and the provided value.

      :rtype: typing.Self



   .. py:method:: __repr__() -> str

      Returns the official string representation of the `AtomicConcept` instance. This implementation delegates directly to the `__str__` method, ensuring that the output is identical to the informal string representation. As a result, the representation is primarily intended for human readability rather than providing a strictly unambiguous or machine-parseable description of the object's state.

      :return: A string representation of the object.

      :rtype: str



   .. py:method:: __rshift__(value: Self) -> Self

      Overloads the right-shift operator to represent a logical implication relationship between this concept and another value. It constructs and returns a new `ImpliesConcept` instance representing the statement that this concept implies the provided value, utilizing Gödel implication semantics. This method does not modify the original concepts but instead produces a new composite concept representing the conditional logic.

      :param value: The right-hand operand representing the consequent in the logical implication.
      :type value: typing.Self

      :return: Returns a new instance representing the logical implication of the current object by the provided value.

      :rtype: typing.Self



   .. py:method:: clone() -> Self

      Creates and returns a new instance of `AtomicConcept` initialized with the same name as the current object. This method provides a lightweight copy mechanism that is side-effect free, leaving the original instance unmodified. The resulting object is a distinct entity, allowing for independent manipulation while preserving the core identifier defined by the name.

      :return: A new instance of the class that is a copy of the current object.

      :rtype: typing.Self



   .. py:method:: compute_atomic_concepts() -> set[Self]

      Returns a set containing the atomic concepts that constitute this entity. Because this class represents an atomic concept, which is indivisible by definition, the resulting set contains only the instance itself. The operation is pure and does not modify the state of the object.

      :return: A set containing the current instance, indicating it is an atomic concept.

      :rtype: set[typing.Self]



   .. py:method:: compute_name() -> str

      Retrieves the primary identifier or label for the atomic concept by returning the value stored in the instance's `name` attribute. This method is a read-only operation and does not modify the internal state of the object. It assumes the `name` attribute is already defined; otherwise, an `AttributeError` will be raised upon invocation.

      :return: The name associated with the object.

      :rtype: str



   .. py:method:: get_atomic_concepts() -> set[Self]

      Retrieves the set of atomic concepts that constitute this instance, returning a collection of objects of the same type. This method serves as a public interface that delegates the actual calculation logic to the `compute_atomic_concepts` method, which may involve recursion or caching to resolve the underlying components. Depending on the specific implementation of the compute method, calling this function could trigger side effects such as populating a cache or resolving complex expressions into their base elements.

      :return: A set of atomic concepts represented as instances of the same class.

      :rtype: set[typing.Self]



   .. py:method:: get_atoms() -> list[Self]

      Returns a list containing the current instance as the sole element. This behavior reflects the definition of an atomic concept, which is considered indivisible and therefore acts as its own fundamental component. The method does not modify the object's state or produce side effects.

      :return: A list containing the current instance.

      :rtype: list[typing.Self]



   .. py:method:: get_clauses(is_type: Callable) -> set[Self]

      Returns a set containing only the current instance, representing the atomic concept as a single, indivisible clause. The `is_type` callable argument is accepted to maintain a consistent interface with potentially complex concept types but is not utilized during execution. This method has no side effects and serves as the base case for traversing or decomposing concept structures.

      :param is_type: A callable predicate used to filter the clauses.
      :type is_type: typing.Callable

      :return: A set containing the current instance.

      :rtype: set[typing.Self]



   .. py:method:: get_roles() -> set[str]

      Retrieves the set of roles associated with this atomic concept. Since atomic concepts represent fundamental, indivisible entities within the system, they do not possess associated roles or relations. Consequently, this method always returns an empty set, indicating the absence of such attributes.

      :return: A set of strings representing the roles associated with the object.

      :rtype: set[str]



   .. py:method:: is_atomic() -> bool

      Returns a boolean value indicating that the current concept is atomic. As this method is defined within the `AtomicConcept` class, it unconditionally returns `True`, serving as a definitive marker for atomicity within a potentially larger hierarchy of concepts. This allows calling code to distinguish between indivisible, base-level concepts and those that might be composed of other parts.

      :return: True if the object is atomic.

      :rtype: bool



   .. py:method:: is_complemented_atomic() -> bool

      Indicates whether the concept represents a negated atomic concept. Since this class defines a base atomic concept, it inherently returns False, distinguishing it from complemented concepts or complex descriptions. The method performs no computation and has no side effects.

      :return: True if the object is a complemented atomic element, False otherwise.

      :rtype: bool



   .. py:method:: is_concrete() -> bool

      Indicates whether the concept represents a concrete entity or implementation. In the context of the `AtomicConcept` class, this method always returns False, signifying that atomic concepts are abstract definitions rather than specific, instantiated objects. This distinction is typically used to differentiate between general conceptual schemas and concrete data points within the broader module logic.

      :return: False, indicating that the class is abstract and not intended to be instantiated.

      :rtype: bool



   .. py:method:: new_atomic_concept() -> Self
      :staticmethod:


      Creates and returns a new instance of `AtomicConcept` with a unique, auto-generated name. The name is constructed by combining a static prefix, a class-level special string, and a running counter of total concepts created. As a side effect, this method increments the global `Concept.num_new_concepts` counter prior to instantiation, ensuring that each invocation produces a distinct identifier.

      :return: A new AtomicConcept instance with a unique name generated from the concept counter.

      :rtype: typing.Self



   .. py:method:: reduce_idempotency(is_type: Callable) -> Self

      Returns the current instance unchanged, as atomic concepts are fundamental units that cannot be simplified further through idempotency reduction. This method acts as a no-op implementation within the concept hierarchy, accepting a type-checking callable for interface compatibility but performing no logic. It serves as the base case for reduction algorithms that would otherwise simplify compound structures by removing redundant elements.

      :param is_type: A callable that determines whether an object matches the specific type criteria for which idempotency reduction should be applied.
      :type is_type: typing.Callable

      :return: Returns the instance itself.

      :rtype: typing.Self



   .. py:method:: replace(a: Self, c: Self) -> Optional[Self]

      Replaces an occurrence of a specific atomic concept with another atomic concept. If the current instance is identical to the target concept `a`, the method returns the replacement concept `c`. If the current instance does not match `a`, it returns itself unchanged. The operation requires that the replacement concept `c` be of type `ATOMIC`; if this condition is not met, an error is triggered.

      :param a: The target instance to be replaced by `c`.
      :type a: typing.Self
      :param c: The replacement concept instance to return if the current instance matches `a`. Must be of type ATOMIC.
      :type c: typing.Self

      :return: The concept resulting from the replacement operation. Returns `c` if `self` matches `a` and `c` is atomic; otherwise, returns `self`. Returns `None` if `c` is not atomic.

      :rtype: typing.Optional[typing.Self]


