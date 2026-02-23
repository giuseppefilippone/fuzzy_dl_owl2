fuzzy_dl_owl2.fuzzydl.concept.concept
=====================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.concept



.. ── LLM-GENERATED DESCRIPTION START ──

A foundational framework for fuzzy description logic that defines abstract and concrete representations of logical entities, supporting complex manipulations like normalization and operator overloading.


Description
-----------


The architecture centers around an abstract base class that establishes a comprehensive interface for constructing, analyzing, and transforming logical formulas within a formal system. It provides utilities for structural inspection and logical manipulation, including support for converting expressions into various normal forms such as Conjunctive and Disjunctive Normal Forms for classic, Gödel, and Łukasiewicz logics. Extending this foundation, a concrete implementation represents the fundamental building blocks of fuzzy description logic ontologies, capable of handling both primitive atomic concepts and complex structures formed through logical composition. By overloading standard Python operators, the design enables intuitive syntax for performing logical operations like negation, conjunction, and implication, while automatically managing naming conventions and equality comparisons based on structural representation.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.concept.concept.Concept
   fuzzy_dl_owl2.fuzzydl.concept.concept.Thing


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_concept_Concept.png
       :alt: UML Class Diagram for Concept
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **Concept**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_concept_Concept.pdf
       :alt: UML Class Diagram for Concept
       :align: center
       :width: 9.7cm
       :class: uml-diagram

       UML Class Diagram for **Concept**

.. py:class:: Concept(c_type: fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType = ConceptType.ATOMIC, name: str = '')

   Bases: :py:obj:`Thing`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept
      :parts: 1
      :private-bases:


   This entity serves as the foundational building block for fuzzy description logic ontologies, capable of representing either primitive atomic concepts or complex structures formed through logical composition. It enables the construction of intricate logical expressions by overloading standard Python operators, allowing conjunction, disjunction, and implication to be performed directly between instances. When instantiated, the object automatically manages naming conventions, generating unique identifiers if a specific name is not provided, while exposing properties to inspect and modify its type and label. Equality comparisons are based on the string representation of the entity, facilitating structural checks within the logical framework.

   :param SPECIAL_STRING: Special character used as a delimiter in the default naming convention for concepts.
   :type SPECIAL_STRING: typing.Any
   :param DEFAULT_NAME: Default prefix used for generating names for new concepts.
   :type DEFAULT_NAME: typing.Any
   :param num_new_concepts: Counter used to generate unique default names for concepts.
   :type num_new_concepts: typing.Any
   :param _type: Determines the classification of the concept, distinguishing between primitive atomic concepts and complex structures formed by logical operators.
   :type _type: fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType
   :param _name: Internal storage for the concept's identifier, used as its string representation and computed from the structure if not explicitly provided.
   :type _name: str


   .. py:method:: __and__(value: Self) -> Self

      Computes the intersection or logical conjunction of this concept with another concept. When the bitwise AND operator (`&`) is applied to an instance of this class, this method is invoked to combine the current instance with the provided value, returning a new instance that represents the shared characteristics or the greatest lower bound of the two concepts. This operation is typically pure, meaning it does not modify the original operands but instead produces a distinct result.

      :param value: The value to perform the bitwise AND operation with.
      :type value: typing.Self

      :return: The result of the bitwise AND operation between this instance and the provided value.

      :rtype: typing.Self



   .. py:method:: __eq__(value: Self) -> bool

      Determines equality between the current instance and another object by comparing their string representations. The method returns True if the string output of the current object exactly matches the string output of the provided value. This behavior implies that two distinct instances are considered equal if they serialize to the same string, regardless of their internal memory addresses or specific attribute implementations, provided those attributes result in identical string representations.

      :param value: The object to compare against, where equality is determined by comparing string representations.
      :type value: typing.Self

      :return: True if the string representation of the current instance is equal to the string representation of the provided value, otherwise False.

      :rtype: bool



   .. py:method:: __iand__(value: Self) -> Self

      Implements the in-place bitwise AND operation (using the `&=` operator) to combine the current instance with another instance of the same type. This method typically modifies the state of the object in place to reflect the intersection or logical conjunction of the two concepts, depending on the specific domain logic. It returns the updated instance, allowing for chained operations, and may raise a TypeError if the provided value is not compatible with the expected type.

      :param value: The right-hand operand for the in-place bitwise AND operation.
      :type value: typing.Self

      :return: Returns the instance after performing an in-place bitwise AND operation with the provided value.

      :rtype: typing.Self



   .. py:method:: __ior__(value: Self) -> Self

      Implements the in-place bitwise OR operation, allowing the current instance to be updated using the union or combination logic with another instance of the same type. This method modifies the object's state directly to incorporate the provided value and returns the updated instance. It is typically invoked via the augmented assignment operator `|=`.

      :param value: The right-hand operand for the in-place bitwise OR operation.
      :type value: typing.Self

      :return: Returns the instance after performing the in-place bitwise OR operation.

      :rtype: typing.Self



   .. py:method:: __irshift__(value: Self) -> Self

      Implements the in-place right shift operation (`>>=`) for the `Concept` class. This method accepts another instance of the same class as `value` and updates the current object accordingly. The operation modifies the instance in place and returns the modified object, allowing for the standard assignment syntax associated with in-place operators.

      :param value: The right-hand operand for the in-place right shift operation.
      :type value: typing.Self

      :return: Returns the object after applying the in-place right shift operation.

      :rtype: typing.Self



   .. py:method:: __ne__(value: Self) -> bool

      Checks for inequality between the current instance and another object of the same type. This method implements the behavior for the `!=` operator by delegating to the `__eq__` method and returning the logical negation of its result. Consequently, the outcome depends entirely on the equality comparison logic, and any exceptions raised during that comparison will propagate through this call.

      :param value: The object to compare with the current instance.
      :type value: typing.Self

      :return: True if the object is not equal to the provided value, False otherwise.

      :rtype: bool



   .. py:method:: __or__(value: Self) -> Self

      Implements the bitwise OR operation using the pipe operator (`|`) to combine this instance with another `Concept`. This method returns a new instance representing the logical disjunction or union of the two operands, ensuring that the original objects remain unmodified. It enables a syntax where concepts can be merged or aggregated directly within expressions.

      :param value: Another instance of the same class to combine with the current instance using the bitwise OR operation.
      :type value: typing.Self

      :return: The result of the bitwise OR or union operation between the current instance and the provided value.

      :rtype: typing.Self



   .. py:method:: __rshift__(value: Self) -> Self

      Implements the right-shift operator (`>>`) for the Concept class, enabling the use of the `>>` syntax to combine or relate two Concept instances. This method accepts another Concept as the right-hand operand and returns a new Concept instance, typically representing a logical implication, entailment, or a specific directional relationship defined by the domain logic. The operation is expected to be side-effect free, producing a new object rather than modifying the existing instances.

      :param value: The right-hand operand for the right-shift operation, which is an instance of the same class.
      :type value: typing.Self

      :return: The result of the right-shift operation, returning a new instance of the class.

      :rtype: typing.Self



   .. py:method:: __str__() -> str

      Returns a human-readable string representation of the Concept, typically used for display purposes. The method ensures that the `name` attribute is populated by checking if it is currently `None`; if so, it invokes `self.compute_name()` to generate the name and stores it on the instance. This process involves a side effect where the object's state is mutated to cache the computed name, preventing redundant calculations on subsequent calls.

      :return: The string representation of the object, which is its name.

      :rtype: str



   .. py:method:: is_atomic() -> bool

      Checks if the current concept is classified as an atomic type within the system's ontology. This is determined by verifying whether the instance's type attribute exactly matches the ATOMIC enumeration value. The operation is read-only and returns a boolean flag indicating the result of this comparison.

      :return: True if the concept is atomic, False otherwise.

      :rtype: bool



   .. py:method:: is_complemented_atomic() -> bool

      Determines whether the concept is a complemented atomic concept, serving as a predicate to identify specific structural types within a logical hierarchy. In this base implementation, the method consistently returns False, indicating that the generic concept does not satisfy the criteria for being both complemented and atomic. This behavior is typically intended to be overridden by subclasses that represent negated or complemented base elements.

      :return: True if the object is complemented atomic, otherwise False.

      :rtype: bool



   .. py:attribute:: DEFAULT_NAME
      :value: 'Concept@'



   .. py:attribute:: SPECIAL_STRING
      :value: '@'



   .. py:attribute:: _name
      :type:  str
      :value: ''



   .. py:attribute:: _type
      :type:  fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType


   .. py:property:: name
      :type: str


      Updates the name of the Concept instance to the specified string value. This setter modifies the object's internal state by assigning the provided value to the private `_name` attribute, effectively replacing any previously stored name.

      :param value: The new name to assign to the object.
      :type value: str


   .. py:attribute:: num_new_concepts
      :value: 1



   .. py:property:: type
      :type: fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType


      Updates the type classification of the Concept instance to the specified value. This setter method assigns the provided `ConceptType` to the internal `_type` attribute, effectively overwriting the previous type definition. The operation modifies the object's state in place and does not return a value.

      :param new_type: The classification or category to assign to the concept.
      :type new_type: fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType


.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_concept_Thing.png
       :alt: UML Class Diagram for Thing
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **Thing**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_concept_Thing.pdf
       :alt: UML Class Diagram for Thing
       :align: center
       :width: 13.6cm
       :class: uml-diagram

       UML Class Diagram for **Thing**

.. py:class:: Thing

   Bases: :py:obj:`abc.ABC`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.concept.concept.Thing
      :parts: 1
      :private-bases:


   This abstract base class serves as the foundational representation for logical entities, such as concepts and operators, within a formal logic system. It defines a comprehensive interface for constructing, analyzing, and transforming logical formulas, offering utilities for structural inspection (e.g., retrieving atoms, clauses, roles, and nominals) and logical manipulation (e.g., simplification, distribution, and the application of De Morgan's laws). The class supports conversion into various normal forms, including standard Conjunctive and Disjunctive Normal Forms (CNF/DNF) as well as variants for fuzzy logic systems like Gödel and Łukasiewicz. While it provides default implementations for many reduction and traversal operations, it is designed to be extended by subclasses, which are required to implement core abstract methods for cloning, negation, equality comparison, and name computation. Additionally, the class overloads standard Python operators to enable intuitive syntax for negation and ordering comparisons between logical expressions.


   .. py:method:: __eq__(value: Self) -> bool
      :abstractmethod:


      This abstract method defines the interface for determining equality between instances of the class. Subclasses must provide a concrete implementation to compare the current instance with another object, which is expected to be of the same type based on the `typing.Self` annotation. The method should return `True` if the objects are considered equivalent and `False` otherwise, thereby customizing the behavior of the equality operator (`==`). Implementations should handle comparisons with incompatible types gracefully, typically by returning `False` or `NotImplemented`, and should avoid modifying the state of either object involved in the comparison.

      :param value: The object to compare with the current instance.
      :type value: typing.Self

      :return: True if the instance is equal to the provided value, False otherwise.

      :rtype: bool



   .. py:method:: __ge__(value: Self) -> Self

      Implements the greater-than-or-equal-to comparison operator (`>=`) for the instance. The method determines the result by returning the logical negation of the less-than comparison (`self < value`). Consequently, it relies on the `__lt__` method to define the actual comparison logic, returning `True` if the instance is not less than the provided value.

      :param value: The object to compare against the current instance.
      :type value: typing.Self

      :return: The result of the comparison indicating whether the object is greater than or equal to the specified value.

      :rtype: typing.Self



   .. py:method:: __gt__(value: Self) -> Self

      Determines if the current instance is greater than the provided value by comparing their string representations after removing all parentheses. The method converts both objects to strings, strips any opening or closing brackets, and performs a lexicographical comparison on the results. Note that despite the type hint suggesting an instance of the class is returned, the actual return value is a boolean indicating the result of the comparison. This implementation prioritizes the textual content of the objects over their structural representation involving parentheses.

      :param value: The object to compare against the current instance. Comparison is based on the string representation of the objects with parentheses removed.
      :type value: typing.Self

      :return: True if the string representation of the current object, with parentheses removed, is lexicographically greater than that of the provided value; otherwise, False.

      :rtype: typing.Self



   .. py:method:: __invert__() -> Self

      Implements the behavior of the unary bitwise NOT operator (`~`) for the instance. Instead of performing a standard bitwise inversion, this method returns the arithmetic negation of the object, effectively making the tilde operator function identically to the unary minus operator. This delegation relies on the class having a defined negation implementation; if the object cannot be negated, this operation will raise an error.

      :return: Returns the arithmetic negation of the current instance.

      :rtype: typing.Self



   .. py:method:: __le__(value: Self) -> Self

      Implements the less-than-or-equal-to comparison operator for the instance, enabling the use of the `<=` syntax. This method determines the comparison result by returning the logical negation of the greater-than operation performed between the current instance and the provided value. The return type is an instance of the class itself, indicating that the operation may produce a new object or state derived from the negation of the `__gt__` logic.

      :param value: The object to compare against.
      :type value: typing.Self

      :return: The result of the less-than-or-equal-to comparison between the instance and the provided value.

      :rtype: typing.Self



   .. py:method:: __lt__(value: Self) -> Self

      Implements the less-than comparison operator by evaluating the lexicographical order of the object's string representation after removing all parentheses. Both the current instance and the provided value are converted to strings and stripped of parentheses characters before being compared. This allows the object to be sorted or compared based on a sanitized version of its string output, ignoring specific formatting characters.

      :param value: The object to compare against. Comparison is determined by the lexicographical order of the string representations of the instances after removing all parentheses.
      :type value: typing.Self

      :return: True if the string representation of the current object, with parentheses removed, is lexicographically less than that of the provided value; otherwise False.

      :rtype: typing.Self



   .. py:method:: __ne__(value: Self) -> bool

      Determines whether the current instance is not equal to the provided value by inverting the result of the equality comparison. This implementation delegates directly to the `__eq__` method, meaning its behavior is entirely dependent on how equality is defined for the class. It returns `True` if the objects are considered unequal and `False` otherwise, propagating any exceptions or non-standard return values generated by the underlying equality check.

      :param value: The object to compare against.
      :type value: typing.Self

      :return: True if the object is not equal to the specified value, False otherwise.

      :rtype: bool



   .. py:method:: __neg__() -> Self
      :abstractmethod:


      This method implements the unary negation operator, enabling the use of the minus sign (`-`) before an instance of the class. As an abstract method, it mandates that subclasses provide a concrete implementation defining how the negation is calculated. The operation is expected to return a new instance of the same type, representing the negated value, and should typically avoid modifying the original object in place.

      :return: Returns a new instance representing the negation of the current object.

      :rtype: typing.Self



   .. py:method:: __repr__() -> str

      Returns the official string representation of the object, intended primarily for debugging and developer use. This implementation delegates the formatting logic directly to the `__str__` method, ensuring that the output produced by `repr()` is identical to the informal string representation. It is automatically invoked by the built-in `repr()` function and when the object is displayed in interactive consoles or collections.

      :return: Returns the string representation of the object.

      :rtype: str



   .. py:method:: classic_cnf() -> Self

      Converts the logical expression represented by this instance into classic Conjunctive Normal Form (CNF). This process restructures the expression so that it consists of a conjunction of disjunctions, effectively distributing logical operators to satisfy the CNF definition. The method delegates the transformation to the underlying `normal_form` utility, specifically targeting the `OR` operator to determine the distribution logic, and returns the resulting normalized expression.

      :return: The expression converted to its classic Conjunctive Normal Form (CNF).

      :rtype: typing.Self



   .. py:method:: classic_dnf() -> Self

      Transforms the current logical expression into its classic Disjunctive Normal Form (DNF). This operation delegates to the underlying `normal_form` utility, passing a predicate that identifies the AND operator to guide the distribution and flattening of the expression structure. The method returns an instance of the same class representing the normalized expression, ensuring the result adheres to the standard DNF definition of a disjunction of conjunctions.

      :return: Returns the expression in Disjunctive Normal Form (DNF).

      :rtype: typing.Self



   .. py:method:: clone() -> Self
      :abstractmethod:


      Creates and returns a distinct copy of the current instance, ensuring the returned object is of the same type as the original. As this is an abstract method, concrete subclasses must provide the specific implementation, defining whether the operation performs a deep or shallow copy of the object's internal state. This method establishes a contract for object replication, allowing the creation of independent duplicates without modifying the source instance.

      :return: A new instance that is a copy of the current object.

      :rtype: typing.Self



   .. py:method:: compute_atomic_concepts() -> set[Self]
      :abstractmethod:


      Computes the set of atomic concepts that constitute the fundamental, indivisible components of this entity. This abstract method requires subclasses to implement the specific logic for decomposing complex structures into their basic elements. The result is a set of instances of the same class, indicating that the atomic concepts are themselves valid entities; typically, if the object is already atomic, the method returns a set containing only the object itself.

      :return: A set of atomic concepts represented by this instance.

      :rtype: set[typing.Self]



   .. py:method:: compute_name() -> Optional[str]
      :abstractmethod:


      This abstract method defines the interface for calculating the name associated with the object. Subclasses must implement this logic to derive a string representation of the name, potentially based on internal attributes or external data sources. The method returns the computed name as a string, or None if the name cannot be determined or is not available for the current state of the object.

      :return: The computed name, or None if it cannot be determined.

      :rtype: typing.Optional[str]



   .. py:method:: contains_negated_subconcept(v: list[Self], cj: Self) -> int
      :staticmethod:


      Determines whether the negation of the provided element `cj` exists within the list `v`. If the negated element is found, the method returns the zero-based index of its first occurrence; otherwise, it returns -1 to indicate that the negated subconcept is not present. This function performs a read-only search and does not modify the input list.

      :param v: A list of concepts to search for the negation of `cj`.
      :type v: list[typing.Self]
      :param cj: The concept to check for the presence of its negation.
      :type cj: typing.Self

      :return: The index of the negated subconcept in the list, or -1 if it is not found.

      :rtype: int



   .. py:method:: contains_subconcept(v: list[Self], cj: Self) -> bool
      :staticmethod:


      Checks for the presence of a specific subconcept within a list of concepts by performing a standard membership test. The method returns True if the provided concept instance `cj` is found within the list `v`, and False otherwise. This operation relies on the equality comparison of the class instances and does not modify the input list or the target concept.

      :param v: A list of objects of the same type to search for the subconcept.
      :type v: list[typing.Self]
      :param cj: The concept instance to check for presence in the list.
      :type cj: typing.Self

      :return: True if the concept `cj` is present in the list `v`, otherwise False.

      :rtype: bool



   .. py:method:: de_morgan() -> Self

      Applies De Morgan's laws to the logical expression represented by the object. Since the current structure is invariant under this transformation or already satisfies the conditions required by the laws, the method returns the instance itself. This operation does not alter the object's state or produce any side effects.

      :return: Returns the instance itself.

      :rtype: typing.Self



   .. py:method:: distribute(c_type: fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType) -> Self

      Returns the current instance without performing any distribution logic or modifying the object's state. The provided `ConceptType` argument is ignored by the implementation, making this method a pass-through operation. By returning `self`, the method supports method chaining and fluent interface patterns without introducing side effects.

      :param c_type: Specifies the type of concept to distribute.
      :type c_type: fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType

      :return: The instance itself.

      :rtype: typing.Self



   .. py:method:: get_atomic_concepts() -> set[Self]

      Retrieves the set of fundamental, indivisible concepts that constitute this entity. This method delegates the actual logic to the `compute_atomic_concepts` method, returning a collection of instances of the same type. It serves as an accessor that does not modify the object's state, though the underlying computation may involve complex logic or recursion depending on the structure of the concept. If the entity is already atomic, the returned set may contain only the object itself.

      :return: A set of atomic concepts represented as instances of the class.

      :rtype: set[typing.Self]



   .. py:method:: get_atomic_concepts_names() -> set[str]

      Retrieves a set of string names representing the atomic concepts associated with this entity. This method relies on `compute_atomic_concepts()` to determine the underlying concepts and converts each one to a string, ensuring that the returned set contains unique names. The specific behavior and performance characteristics depend on the implementation of `compute_atomic_concepts()`, which may involve caching or complex logic.

      :return: A set of strings representing the names of the atomic concepts.

      :rtype: set[str]



   .. py:method:: get_atoms() -> list[Self]

      Returns a list of the atomic constituents of the current object, where the constituents are expected to be instances of the same class. The current implementation returns an empty list, suggesting that the object is treated as a leaf node or that the logic for decomposing the object into smaller parts is intended to be provided by subclasses. This method does not modify the object's state and produces a new list instance on each invocation.

      :return: A list of instances of the same class representing the constituent atoms.

      :rtype: list[typing.Self]



   .. py:method:: get_clauses(is_type: Callable) -> list[Self]

      Returns an empty list of instances of the class. Although the method accepts a callable argument intended to filter or identify specific types of clauses, the current implementation ignores this argument and provides no results. This serves as a default base implementation, likely intended to be overridden by subclasses to provide actual retrieval logic. The method has no side effects and always returns a new list object.

      :param is_type: A predicate function used to filter clauses, returning True for items that match the desired type or criteria.
      :type is_type: typing.Callable

      :return: A list of clauses (instances of the same class) that satisfy the type check provided by `is_type`.

      :rtype: list[typing.Self]



   .. py:method:: get_roles() -> set[str]
      :abstractmethod:


      Retrieves the set of roles associated with this entity, returning them as a collection of unique string identifiers. This method serves as an abstract interface, requiring subclasses to implement the specific logic for determining which roles apply to the instance. The returned set may be empty if no roles are currently assigned.

      :return: A set of strings representing the roles associated with the entity.

      :rtype: set[str]



   .. py:method:: goedel_cnf() -> Self

      Converts the logical expression represented by the object into Conjunctive Normal Form (CNF) using the Gödel disjunction operator. This method invokes the general `normal_form` transformation, specifically targeting `ConceptType.GOEDEL_OR` as the disjunction operator to be used during the conversion process. It returns the transformed expression, ensuring that the structure adheres to the conjunctions-of-disjunctions format required for CNF within the context of Gödel logic.

      :return: Returns the expression converted to Gödel Conjunctive Normal Form.

      :rtype: typing.Self



   .. py:method:: goedel_dnf() -> Self

      Converts the logical structure into its Gödel Disjunctive Normal Form (DNF) by applying a normalization strategy that recognizes `ConceptType.GOEDEL_AND` as the conjunction operator. This method delegates the transformation to the generic `normal_form` function, passing a specific predicate to isolate the appropriate logical connective for the calculation. The result is a new instance of the same type representing the normalized expression.

      :return: The object transformed into its Gödel Disjunctive Normal Form.

      :rtype: typing.Self



   .. py:method:: has_nominals() -> bool

      Determines whether the current instance contains nominal elements by inspecting its string representation. Specifically, it returns `True` if the substring `"(b-some "` is found within the result of `str(self)`, and `False` otherwise. This check relies on the specific formatting of the object's string output, meaning changes to the serialization logic could affect the accuracy of the result.

      :return: True if the object contains nominals, identified by the presence of the substring "(b-some " in its string representation.

      :rtype: bool



   .. py:method:: is_concrete() -> bool

      Determines whether the object represents a concrete, fully realized entity rather than an abstract concept or base type. For the `Thing` class, this method unconditionally returns False, indicating that instances of this class are inherently abstract or conceptual. This implementation serves as a default behavior, typically intended to be overridden by subclasses that represent specific, tangible items. The method performs no state modifications and has no side effects.

      :return: False, indicating that the class is abstract and not concrete.

      :rtype: bool



   .. py:method:: is_simplified() -> bool

      Determines whether the logical formula represented by the object adheres to a specific simplified structural definition. The method verifies that negation is applied exclusively to atomic propositions and that the only logical operators present are AND, OR, and NOT. Additionally, it enforces specific nesting constraints for conjunctions and disjunctions, ensuring that OR operations connect literals or conjunctions of literals, while AND operations connect literals or disjunctions of literals. This check is read-only and does not modify the underlying formula.

      :return: True if the formula is in simplified form, adhering to specific structural constraints regarding negation, AND, and OR operators; otherwise, False.

      :rtype: bool



   .. py:method:: lukasiewicz_cnf() -> Self

      Converts the logical expression represented by this instance into Conjunctive Normal Form (CNF) using the semantics of Lukasiewicz logic. This transformation is performed by delegating to the `normal_form` method, specifically identifying the `LUKASIEWICZ_OR` operator as the target connective for the normalization process. The method returns an instance of the same class containing the resulting expression structure.

      :return: The expression converted to its Conjunctive Normal Form (CNF) using Lukasiewicz logic.

      :rtype: typing.Self



   .. py:method:: lukasiewicz_dnf() -> Self

      Converts the logical expression into its Disjunctive Normal Form (DNF) specifically for Łukasiewicz logic. This transformation is performed by delegating to the `normal_form` method, providing a predicate that identifies the Łukasiewicz conjunction operator (`LUKASIEWICZ_AND`) to guide the distribution process. The method returns the transformed instance, which may be a new object or the modified original, depending on the implementation of the underlying normalization logic.

      :return: Returns the Lukasiewicz disjunctive normal form of the expression.

      :rtype: typing.Self



   .. py:method:: normal_form(is_type: Callable) -> Self

      Returns the instance itself, representing the object's normal form without performing any transformation. The method accepts a callable argument `is_type` to maintain a consistent interface, likely for use in overridden implementations or type checking, but this argument is ignored by the current logic. Consequently, this function has no side effects and preserves the identity of the object.

      :param is_type: A callable used to check or determine types during the normalization process.
      :type is_type: typing.Callable

      :return: Returns the instance itself.

      :rtype: typing.Self



   .. py:method:: reduce_double_negation() -> Self

      This method attempts to simplify the object by resolving any double negation logic present within its structure. In this specific implementation, the object is already in its simplest form or does not contain reducible negations, so the method returns the instance unchanged. The operation has no side effects and serves as a pass-through, potentially to be overridden by subclasses that implement specific reduction logic.

      :return: The current instance.

      :rtype: typing.Self



   .. py:method:: reduce_idempotency(is_type: Callable) -> Self

      This method acts as a no-op implementation for reducing idempotency, returning the instance itself without modification. Although it accepts a callable argument `is_type` intended to define type-specific logic, this argument is ignored in the current implementation. Consequently, calling this method has no side effects and does not alter the state of the object, making it safe for use in method chaining scenarios where idempotency reduction is not required.

      :param is_type: A predicate function used to identify elements of a specific type for the idempotency reduction.
      :type is_type: typing.Callable

      :return: The instance itself.

      :rtype: typing.Self



   .. py:method:: reduce_quantifiers() -> Self

      Returns the instance itself without performing any transformation on the object's state. This indicates that the object is already in a reduced form or that this implementation serves as a default pass-through for quantifier reduction logic. The method has no side effects and is designed to return `Self` to maintain consistency with overriding implementations.

      :return: Returns the instance itself.

      :rtype: typing.Self



   .. py:method:: reduce_truth_values() -> Self

      Returns the instance itself without modification, effectively serving as a no-operation for truth value reduction. This implementation is likely intended as a default behavior or a pass-through in a polymorphic hierarchy, allowing subclasses to override the method with specific logic for aggregating or simplifying boolean states while leaving the current object unchanged.

      :return: Returns the instance itself.

      :rtype: typing.Self



   .. py:method:: remove_element(v: list[Self], i: int) -> None
      :staticmethod:


      Removes the element at the specified index `i` from the list `v` in place. This method checks if the index is strictly less than the length of the list before attempting removal, ensuring that an IndexError is not raised for positive out-of-bounds indices. The list is mutated directly, and the method returns None.

      :param v: The list of instances from which to remove an element at the specified index.
      :type v: list[typing.Self]
      :param i: The zero-based index of the element to remove.
      :type i: int



   .. py:method:: replace(a: Self, c: Self) -> Optional[Self]
      :abstractmethod:


      Replaces a specific target element `a` within the current instance with a new element `c`. This abstract method requires subclasses to define the precise logic for identifying and executing the substitution, often used in the context of traversing or modifying hierarchical structures. The operation returns the modified or new instance, or `None` if the replacement is not applicable or results in the removal of the current node.

      :param a: The instance to be replaced.
      :type a: typing.Self
      :param c: The instance of the same class to use as the replacement.
      :type c: typing.Self

      :return: The instance resulting from replacing `a` with `c`, or `None` if the operation cannot be performed.

      :rtype: typing.Optional[typing.Self]


