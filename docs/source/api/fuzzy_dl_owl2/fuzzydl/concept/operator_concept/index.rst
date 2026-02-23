fuzzy_dl_owl2.fuzzydl.concept.operator_concept
==============================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.operator_concept



.. ── LLM-GENERATED DESCRIPTION START ──

A Python class representing logical conjunctions, disjunctions, and negations within a fuzzy description logic framework, supporting various semantics and normalization techniques.


Description
-----------


It serves as the core mechanism for constructing and manipulating complex logical expressions by extending the base ``Concept`` class to handle binary operations like AND and OR, as well as unary negation, across different fuzzy logic systems such as classical, Łukasiewicz, and Gödel. The implementation utilizes static factory methods to instantiate operator nodes, automatically selecting the appropriate semantic variant based on global configuration while flattening nested structures to maintain a canonical form. Beyond simple construction, the logic includes sophisticated algorithms for expression simplification, applying De Morgan's laws, eliminating double negations, distributing operators, and reducing quantifiers to transform expressions into Conjunctive or Disjunctive Normal Forms. To facilitate natural usage, the class overloads standard bitwise operators for conjunction, disjunction, and negation, allowing developers to write intuitive logical expressions while the underlying system handles the complexities of fuzzy logic algebraic rules.

.. ── LLM-GENERATED DESCRIPTION END ──

Attributes
----------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.concept.operator_concept.And
   fuzzy_dl_owl2.fuzzydl.concept.operator_concept.GoedelAnd
   fuzzy_dl_owl2.fuzzydl.concept.operator_concept.GoedelOr
   fuzzy_dl_owl2.fuzzydl.concept.operator_concept.LukasiewiczAnd
   fuzzy_dl_owl2.fuzzydl.concept.operator_concept.LukasiewiczOr
   fuzzy_dl_owl2.fuzzydl.concept.operator_concept.Not
   fuzzy_dl_owl2.fuzzydl.concept.operator_concept.Or


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.concept.operator_concept.OperatorConcept


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_operator_concept_OperatorConcept.png
       :alt: UML Class Diagram for OperatorConcept
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OperatorConcept**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_operator_concept_OperatorConcept.pdf
       :alt: UML Class Diagram for OperatorConcept
       :align: center
       :width: 5.8cm
       :class: uml-diagram

       UML Class Diagram for **OperatorConcept**

.. py:class:: OperatorConcept(c_type: fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType, concepts: Iterable[fuzzy_dl_owl2.fuzzydl.concept.concept.Concept])

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.concept.concept.Concept`, :py:obj:`fuzzy_dl_owl2.fuzzydl.concept.interface.has_concepts_interface.HasConceptsInterface`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.concept.operator_concept.OperatorConcept
      :parts: 1
      :private-bases:


   This class serves as a representation of logical operators—specifically conjunctions, disjunctions, and negations—within a fuzzy description logic system. It extends the base `Concept` class to support the construction and manipulation of complex logical expressions using various fuzzy logic semantics, such as classical, Lukasiewicz, and Zadeh (Goedel). Users can create operator concepts through static factory methods like `and_`, `or_`, and `not_`, which dynamically determine the specific operator type based on the global knowledge base semantics or allow for explicit selection of fuzzy variants. Beyond construction, the class offers a suite of methods for logical simplification and normalization, including the application of De Morgan's laws, reduction of double negations, distribution of operators, and conversion to Conjunctive or Disjunctive Normal Forms (CNF/DNF). It also integrates with quantifier logic by merging `AllSomeConcept` instances and supports operator overloading for `&`, `|`, and unary `-` to enable syntactically natural logical operations.

   :param AND_OPERATORS: Concept types identifying conjunction operators for classical, Lukasiewicz, and Goedel fuzzy logic semantics.
   :type AND_OPERATORS: list[fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType]
   :param OR_OPERATORS: A list of ConceptType values representing all supported disjunction operators, covering classical, Gödel, and Łukasiewicz semantics.
   :type OR_OPERATORS: list[fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType]
   :param BINARY_OPERATORS: A list of concept types representing all binary logical operators, encompassing both conjunction and disjunction variants.
   :type BINARY_OPERATORS: list[fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType]
   :param COMPLEMENT_LAW_OPERATORS: Operators for which the complement law holds, allowing the simplification of expressions containing a concept and its negation.
   :type COMPLEMENT_LAW_OPERATORS: list[fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType]
   :param DISTRIBUTIVE_OPERATORS: A list of operator types that satisfy distributive laws, comprising classical and Goedel conjunctions and disjunctions.
   :type DISTRIBUTIVE_OPERATORS: list[fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType]
   :param ABSORPTION_OPERATORS: A list of operator types (AND, OR, and their Gödel variants) for which absorption laws apply, used during logical simplification.
   :type ABSORPTION_OPERATORS: list[fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType]
   :param ALL_OPERATORS: A list of all valid operator concept types, including binary conjunctions and disjunctions across various fuzzy logic semantics, as well as the complement operator.
   :type ALL_OPERATORS: list[fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType]
   :param OPERATORS: Maps each binary operator type to its logical dual (e.g., AND to OR), used for applying De Morgan's laws and distribution.
   :type OPERATORS: dict[fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType, fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType]
   :param type: The specific logical operator and fuzzy semantics (e.g., AND, OR, COMPLEMENT, or their variants) defining the concept's behavior in logical operations, simplifications, and string representation.
   :type type: fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType
   :param name: Computed string representation of the operator concept, automatically generated based on the operator type and its operands.
   :type name: typing.Any

   :raises NotImplementedError: Raised when attempting to negate an operator concept whose type is not one of the recognized logical operators (AND, OR, COMPLEMENT, or their fuzzy variants).


   .. py:method:: __and__(value: Self) -> Self

      Implements the bitwise AND operation (`&`) to combine the current `OperatorConcept` instance with another instance of the same type. The behavior varies based on the type of the current instance: if it represents an AND operation, the method merges the new value directly; if it represents an OR operation, it retrieves the specific operator logic to combine the operands. For any other type, the method defaults to creating a new AND operation that includes both the current instance and the provided value, returning the resulting `OperatorConcept`.

      :param value: The right-hand operand to combine with the current instance using the AND operator.
      :type value: typing.Self

      :return: A new instance representing the logical AND of the current concept and the provided value.

      :rtype: typing.Self



   .. py:method:: __eq__(value: Self) -> bool

      Determines equality by verifying that the provided value is an instance of the same class and that its string representation matches that of the current instance. This comparison relies entirely on the output of the string conversion method, meaning two distinct objects are considered equal if they produce identical strings. Comparisons against objects of different types will result in a value of False.

      :param value: The object to compare against the current instance, where equality is determined by comparing the string representations.
      :type value: typing.Self

      :return: True if the provided value is an instance of OperatorConcept and its string representation matches that of this instance; otherwise, False.

      :rtype: bool



   .. py:method:: __hash__() -> int

      Computes the hash value for the instance, enabling its use as a key in dictionaries or as an element in sets. The implementation derives the hash from the string representation of the object, ensuring that instances with identical string representations produce the same hash code. This method delegates the calculation to the built-in hash function applied to the result of the object's string conversion.

      :return: An integer hash value derived from the string representation of the object.

      :rtype: int



   .. py:method:: __ne__(value: Self) -> bool

      Determines whether the current instance is not equal to the provided value by negating the result of the equality comparison. This method delegates the logic to the `__eq__` implementation, meaning its behavior, including any raised exceptions or handling of incompatible types, is defined by that method. If the equality check returns the `NotImplemented` singleton, this implementation will treat it as a falsy value, resulting in a return value of `True`.

      :param value: The object to compare against the current instance.
      :type value: typing.Self

      :return: True if the instance is not equal to the provided value, False otherwise.

      :rtype: bool



   .. py:method:: __neg__() -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept

      Computes the logical negation of the operator concept by applying De Morgan's laws. This process recursively negates all child concepts and inverts the logical operator type, transforming conjunctions (AND) into disjunctions (OR) and vice versa. The implementation supports standard logical operators alongside specific fuzzy logic variants, such as Gödel and Łukasiewicz. When applied to a COMPLEMENT operator, the method effectively resolves a double negation by returning the inner child concept. If the concept's operator type is unsupported, the method raises a NotImplementedError.

      :raises NotImplementedError: Raised if negation is not defined for the current concept type.

      :return: Returns the logical negation of the concept, applying De Morgan's laws to distribute the negation over the underlying operator and resolving double negations.

      :rtype: Concept



   .. py:method:: __op(c_type: fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType, concepts: Iterable[fuzzy_dl_owl2.fuzzydl.concept.concept.Concept]) -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept
      :staticmethod:


      Constructs a `Concept` representing the specified logical operation applied to the provided iterable of concepts, performing normalization to ensure a canonical form. If the operation type is not a complement and only a single concept is provided, the method returns that concept directly rather than wrapping it. For binary operators, the method recursively flattens the structure by merging any nested operators of the same type into the current list of arguments. The final list of concepts is sorted before being encapsulated in a new `OperatorConcept` instance, and an assertion error is raised if the input iterable is empty.

      :param c_type: The type of the operator concept to create, determining how the input concepts are combined or flattened.
      :type c_type: fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType
      :param concepts: The concepts to be combined into the resulting operator concept. The iterable is flattened to merge nested concepts of the same type and sorted before construction.
      :type concepts: typing.Iterable[Concept]

      :return: A normalized `Concept` representing the logical operation defined by `c_type` applied to `concepts`, where nested operators of the same type are flattened and the resulting concepts are sorted.

      :rtype: Concept



   .. py:method:: __or__(value: Self) -> Self

      Implements the bitwise OR operation (`|`) to combine the current `OperatorConcept` with another instance of the same type. The behavior varies based on the internal type of the current concept: if it is already an OR operation, the value is merged using the existing type; if it is an AND operation, a specific operator logic is retrieved and applied; otherwise, a standard OR relationship is established between the two concepts. This method returns a new `OperatorConcept` representing the resulting logical expression without modifying the original instances.

      :param value: The right-hand operand to combine with the current instance using the OR operator.
      :type value: typing.Self

      :return: A new instance representing the result of the OR operation between the current instance and the provided value.

      :rtype: typing.Self



   .. py:method:: and_(*concepts: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept
      :staticmethod:


      Creates a new `Concept` representing the logical conjunction of the provided input concepts. The specific semantic interpretation of the conjunction is determined by the global `KNOWLEDGE_BASE_SEMANTICS` setting. If the semantics are set to `CLASSICAL`, it returns a concept in classical Conjunctive Normal Form. For `LUKASIEWICZ` semantics, it applies Lukasiewicz fuzzy logic, and for `ZADEH` semantics, it applies Goedel fuzzy logic. This method acts as a factory for `OperatorConcept` instances, adapting the underlying operator based on the current configuration.

      :param concepts: The Concept instances to be combined using logical conjunction.
      :type concepts: Concept

      :return: A Concept representing the logical conjunction of the input concepts, calculated according to the active knowledge base semantics.

      :rtype: Concept



   .. py:method:: clone() -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept

      Generates a shallow copy of the current `OperatorConcept` instance, preserving its type and associated concepts. The returned object is a new instance containing a shallow copy of the original's concept list, ensuring that structural modifications to the list do not affect the source object. However, because the copy is shallow, any mutable objects referenced within the concepts list remain shared between the original and the clone.

      :return: A new Concept instance that is a copy of the current object.

      :rtype: Concept



   .. py:method:: compute_atomic_concepts() -> set[fuzzy_dl_owl2.fuzzydl.concept.concept.Concept]

      Computes and returns the set of atomic concepts that constitute this operator concept by recursively aggregating the atomic concepts of its immediate children. The method iterates through the collection of concepts associated with this operator, invoking their respective `compute_atomic_concepts` methods and merging the results into a unified set to ensure uniqueness. This process effectively flattens the conceptual hierarchy, returning the base-level concepts found at the leaves of the structure. If the operator contains no child concepts, an empty set is returned. The operation does not modify the state of the current instance or its children.

      :return: A set containing the union of atomic concepts derived from the object's internal concepts.

      :rtype: set[Concept]



   .. py:method:: compute_name() -> Optional[str]

      Generates a string representation of the logical operator concept based on its specific type and the list of constituent concepts. The method joins the string values of the underlying concepts and formats them within parentheses, prefixed by a label corresponding to the logic operation, such as 'and', 'or', or 'not', including specific variants for Gödel and Łukasiewicz logics. If the concept type does not match any of the defined operators, the method returns None. This function performs a read-only operation and does not modify the object's state.

      :return: A string representation of the concept formatted according to its logical type, or None if the type is not recognized.

      :rtype: typing.Optional[str]



   .. py:method:: de_morgan() -> Self

      Recursively applies De Morgan's laws to the logical expression tree represented by this concept. The method first normalizes all child concepts by invoking `de_morgan` on them. If the current node is a negation of a binary operator (such as AND or OR), it performs a structural transformation: the operator is inverted (swapping AND with OR) and the negation is pushed down to the operands, resulting in a new `OperatorConcept` instance. If the current node does not match the pattern for De Morgan's laws, the method returns the current instance with its updated children.

      :return: Returns the concept after recursively applying De Morgan's laws to push negations inward.

      :rtype: typing.Self



   .. py:method:: distribute(c_type: fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType) -> Self

      Recursively distributes the specified operator type over its dual operator within the logical expression tree represented by this concept. The method traverses the structure bottom-up, applying distribution rules if the current node's type matches `c_type` and it contains children of the dual operator type; for instance, distributing AND over OR transforms `A & (B | C)` into `(A & B) | (A & C)`. If the concept is a Complement, the operation is delegated to its single child, while non-distributive operators are left untouched. This process modifies the concept's internal list of children in place but returns the resulting concept, which may be a new instance if the root node is restructured during distribution.

      :param c_type: The operator type to distribute over its dual (e.g., AND over OR) to expand the expression.
      :type c_type: fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType

      :return: Returns the concept after recursively distributing the specified operator type over its structure.

      :rtype: typing.Self



   .. py:method:: get_atom() -> Optional[Self]

      Retrieves the underlying atomic concept if the current instance represents a complement operation. When the concept type is `ConceptType.COMPLEMENT`, this method returns the first element from the internal `concepts` collection. For any other concept type, it returns `None`, indicating that no specific atom is associated with this instance.

      :return: Returns the first concept if the instance type is COMPLEMENT, or None otherwise.

      :rtype: typing.Optional[typing.Self]



   .. py:method:: get_atoms() -> list[Self]

      Recursively traverses the concept structure to return a list of all atomic concepts that constitute this concept. If the current concept is a complement of an atomic concept, it returns a list containing itself; if it is a complement of a complex concept, it returns the atoms of the inner concept. For other concept types, it aggregates the atomic results from all child concepts into a single list. This method effectively flattens the concept tree to its base elements, handling negation by looking through the complement operator to the underlying structure.

      :return: A list of the atomic concepts that constitute this concept.

      :rtype: list[typing.Self]



   .. py:method:: get_clauses(is_type: Callable) -> list[fuzzy_dl_owl2.fuzzydl.concept.concept.Concept]

      Retrieves the clauses associated with the operator concept. When the concept type is COMPLEMENT, the method returns a singleton list containing the current instance. For any other concept type, it returns the list of child concepts managed by the operator. Note that the `is_type` argument is currently ignored by the logic.

      :param is_type: A callable predicate used to filter or identify concepts based on their type.
      :type is_type: typing.Callable

      :return: A list of Concept objects. If the concept type is COMPLEMENT, returns a list containing the current concept; otherwise, returns the list of associated sub-concepts.

      :rtype: list[Concept]



   .. py:method:: get_roles() -> set[str]

      Aggregates and returns a unique set of role strings from all underlying concepts associated with this operator. This method iterates through the internal collection of concepts, retrieves the roles for each, and combines them into a single set to eliminate duplicates. The operation is non-destructive and returns an empty set if the operator contains no constituent concepts.

      :return: A set of unique role strings aggregated from all associated concepts.

      :rtype: set[str]



   .. py:method:: goedel_and(*concepts: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept
      :staticmethod:


      Constructs a logical conjunction using Gödel logic semantics from a variable number of input concepts. This static method instantiates an `OperatorConcept` representing the AND operation and immediately normalizes the result into Conjunctive Normal Form (CNF) before returning it. The behavior ensures that the resulting structure is flattened and standardized according to the framework's logic rules, regardless of the complexity or quantity of the input concepts.

      :param concepts: The Concept instances to be combined using the Gödel AND operator.
      :type concepts: Concept

      :return: A Concept representing the Gödel logic conjunction of the input concepts, converted to Conjunctive Normal Form (CNF).

      :rtype: Concept



   .. py:method:: goedel_or(*concepts: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept
      :staticmethod:


      Constructs a logical concept representing the Gödelian disjunction (OR) of the provided input concepts. This static method accepts a variable number of Concept instances and generates an `OperatorConcept` defined by the `GOEDEL_OR` type. Crucially, the resulting concept is immediately transformed into Conjunctive Normal Form (CNF) before being returned, which standardizes the structure for subsequent logical operations. The method expects at least one operand; providing zero arguments may lead to unexpected behavior or errors depending on the internal implementation of the operator factory.

      :param concepts: One or more Concept instances to be combined using the Gödel OR operation.
      :type concepts: Concept

      :return: A Concept representing the Gödel OR of the input concepts, converted to Conjunctive Normal Form (CNF).

      :rtype: Concept



   .. py:method:: is_and(c_type: fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType) -> bool
      :staticmethod:


      Determines whether the provided concept type represents a logical AND operation by verifying its presence in the class's collection of AND operators. This method returns `True` if the input matches one of the defined AND operator types, and `False` otherwise. It performs a read-only check without modifying any state, and it safely returns `False` for any input type that is not explicitly listed as an AND operator.

      :param c_type: The concept type to verify if it represents an AND operator.
      :type c_type: fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType

      :return: True if the provided concept type is an AND operator, False otherwise.

      :rtype: bool



   .. py:method:: is_atomic() -> bool

      Determines whether the operator is considered atomic, meaning it cannot be decomposed into simpler sub-operators. This implementation returns False by default, indicating that the operator is a composite structure rather than a primitive building block. Subclasses representing fundamental or indivisible operations are expected to override this method to return True. The function performs no side effects and is primarily used to distinguish between complex operators and their atomic counterparts during analysis or traversal.

      :return: True if the object is atomic, False otherwise.

      :rtype: bool



   .. py:method:: is_complemented_atomic() -> bool

      Determines whether the current concept represents a complement operation applied to a single atomic concept. This method returns true only if the concept's type is identified as a complement and its immediate child concept is considered atomic according to the child's own definition. The operation assumes the internal list of concepts is non-empty and does not modify the object's state.

      :return: True if this concept is a complement of an atomic concept, False otherwise.

      :rtype: bool



   .. py:method:: is_concrete() -> bool

      Determines whether the operator concept is considered concrete based on its internal state and type. The method returns True if the concept is identified as not being a concrete type or not being a fuzzy number. If the concept is flagged as not modified, the concrete status is determined by recursively calling this method on the first concept in the `concepts` list. In all other scenarios, the method returns False.

      :return: True if the concept is not a concrete concept or not a fuzzy number. If the concept is not modified, returns the concreteness of the first concept. Returns False for modified concepts that are both concrete concepts and fuzzy numbers.

      :rtype: bool



   .. py:method:: is_not_at_least_value(op: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> bool
      :staticmethod:


      Determines whether the provided `Concept` object does not represent an "at least value" operator. This static method acts as a specific type guard by delegating the type comparison to the `is_not_type` method, passing `ConceptType.AT_LEAST_VALUE` as the target type to exclude. It returns `True` if the concept's type differs from the specified value, and `False` if it matches.

      :param op: The concept instance to verify is not of type AT_LEAST_VALUE.
      :type op: Concept

      :return: True if the provided concept is not of type AT_LEAST_VALUE, otherwise False.

      :rtype: bool



   .. py:method:: is_not_at_most_value(op: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> bool
      :staticmethod:


      Determines whether the provided concept is not of the AT_MOST_VALUE type. This static method evaluates the input concept and returns True if its type differs from AT_MOST_VALUE, effectively filtering out concepts that represent this specific constraint. The check is performed by delegating to the is_not_type method, ensuring consistent type validation logic without modifying the input object.

      :param op:
      :type op: Concept

      :return: True if the provided concept is not of type AT_MOST_VALUE, False otherwise.

      :rtype: bool



   .. py:method:: is_not_choquet(op: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> bool
      :staticmethod:


      Determines whether the provided concept is not a Choquet integral operator. This static method evaluates the input object to verify that its type does not correspond to `ConceptType.CHOQUET_INTEGRAL`. It returns `True` if the concept is of a different type, and `False` if it is identified as a Choquet integral.

      :param op: The concept to check against the Choquet integral type.
      :type op: Concept

      :return: True if the concept is not a Choquet integral, False otherwise.

      :rtype: bool



   .. py:method:: is_not_concrete(op: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> bool
      :staticmethod:


      Determines whether the provided `Concept` instance is not classified as a concrete type. This static method acts as a specific predicate that delegates to the underlying `is_not_type` utility, passing the `ConceptType.CONCRETE` enum value to perform the check. It returns `True` if the concept is abstract, undefined, or any other non-concrete type, and `False` only if the concept is explicitly concrete.

      :param op: The concept to check for non-concreteness.
      :type op: Concept

      :return: True if the concept is not concrete, False otherwise.

      :rtype: bool



   .. py:method:: is_not_exact_value(op: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> bool
      :staticmethod:


      Determines whether the provided concept does not represent an exact value. This method serves as a specific type guard, checking if the concept's type differs from `ConceptType.EXACT_VALUE` by delegating to the generic `is_not_type` method. It returns `True` for concepts that are operators, variables, or other non-literal entities, and `False` only if the concept is explicitly classified as an exact value. The operation is read-only and does not modify the input object.

      :param op: The concept to verify is not an exact value.
      :type op: Concept

      :return: True if the concept is not an exact value, False otherwise.

      :rtype: bool



   .. py:method:: is_not_ext_neg_threshold(op: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> bool
      :staticmethod:


      Determines whether the provided concept is not classified as an external negative threshold. This static method acts as a specific type guard, delegating to the general type-checking logic to verify that the concept's type does not match `ConceptType.EXT_NEG_THRESHOLD`. It returns `True` if the concept is of any other type, and `False` only if the concept is explicitly identified as an external negative threshold.

      :param op: The concept to verify is not of type EXT_NEG_THRESHOLD.
      :type op: Concept

      :return: True if the concept is not of type EXT_NEG_THRESHOLD, otherwise False.

      :rtype: bool



   .. py:method:: is_not_ext_pos_threshold(op: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> bool
      :staticmethod:


      Determines whether the provided concept is not of the external positive threshold type. This static method acts as a specific type check, returning `True` if the concept's type differs from `ConceptType.EXT_POS_THRESHOLD` and `False` if it matches. It delegates the actual comparison logic to the `is_not_type` method.

      :param op: The concept to verify is not of type EXT_POS_THRESHOLD.
      :type op: Concept

      :return: True if the provided concept is not an external positive threshold, otherwise False.

      :rtype: bool



   .. py:method:: is_not_fuzzy_number(op: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> bool
      :staticmethod:


      Determines whether the provided concept is not classified as a fuzzy number. This static method serves as a specific type guard, verifying that the input concept does not correspond to the `FUZZY_NUMBER` category within the system's type hierarchy. It returns `True` if the concept is of any other type, and `False` if it is specifically identified as a fuzzy number.

      :param op: The concept to verify is not a fuzzy number.
      :type op: Concept

      :return: True if the provided concept is not a fuzzy number, False otherwise.

      :rtype: bool



   .. py:method:: is_not_goedel_implies(op: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> bool
      :staticmethod:


      Determines whether the provided concept is not a Gödel implication operator. This static method checks the type of the input concept against the `ConceptType.GOEDEL_IMPLIES` enumeration value. It returns `True` if the concept's type does not match the Gödel implication type, and `False` if it does. The function performs a read-only check and does not modify the state of the input concept.

      :param op: The concept to verify is not a Gödel implication.
      :type op: Concept

      :return: True if the concept is not a Gödel implies operator, False otherwise.

      :rtype: bool



   .. py:method:: is_not_has_value(op: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> bool
      :staticmethod:


      Determines whether the provided concept is not of the `HAS_VALUE` type. This static method acts as a specific predicate, delegating to the underlying type-checking logic to verify the concept's classification. It returns `True` if the concept's type differs from `HAS_VALUE`, and `False` otherwise, without modifying the input object.

      :param op: The concept to verify is not of type HAS_VALUE.
      :type op: Concept

      :return: True if the concept is not of type HAS_VALUE, False otherwise.

      :rtype: bool



   .. py:method:: is_not_modified(op: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> bool
      :staticmethod:


      Checks if the specified concept is not of the modified type. This static method evaluates the input concept and returns `True` if its type is not `ConceptType.MODIFIED`, effectively determining that the concept has not been modified. It performs a read-only check without altering the state of the concept.

      :param op: The concept to check against the MODIFIED type.
      :type op: Concept

      :return: True if the concept is not of type MODIFIED, False otherwise.

      :rtype: bool



   .. py:method:: is_not_neg_threshold(op: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> bool
      :staticmethod:


      Determines whether the provided concept is not classified as a negative threshold. This method acts as a specific type guard, returning True if the concept's type differs from `ConceptType.NEG_THRESHOLD`. It performs a read-only check without modifying the input object or any external state.

      :param op: The concept to check against the NEG_THRESHOLD type.
      :type op: Concept

      :return: True if the concept is not a negative threshold, False otherwise.

      :rtype: bool



   .. py:method:: is_not_owa(op: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> bool
      :staticmethod:


      Determines whether the provided concept is not an Ordered Weighted Averaging (OWA) operator. This static method acts as a specific type guard, delegating to the generic `is_not_type` method to verify that the concept's type does not match `ConceptType.OWA`. It returns `True` if the concept is of a different type, and `False` if it is identified as an OWA operator. The operation is read-only and does not modify the input object.

      :param op: The concept to verify is not of type OWA.
      :type op: Concept

      :return: True if the provided concept is not an OWA operator, False otherwise.

      :rtype: bool



   .. py:method:: is_not_pos_threshold(op: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> bool
      :staticmethod:


      Determines whether the provided concept is not classified as a positive threshold. This static method evaluates the input concept against the `POS_THRESHOLD` type definition, returning `True` if the concept differs from this specific type and `False` otherwise. It acts as a specific predicate wrapper, delegating the actual type comparison to the underlying `is_not_type` method. The function does not modify the input object and has no side effects.

      :param op: The concept to verify is not of type POS_THRESHOLD.
      :type op: Concept

      :return: True if the concept is not of type POS_THRESHOLD, False otherwise.

      :rtype: bool



   .. py:method:: is_not_qowa(op: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> bool
      :staticmethod:


      Determines whether the provided concept is not a Quantified Open World Assumption (QOWA) operator. This static method acts as a specific type guard, delegating the verification logic to the underlying `is_not_type` method with the `QUANTIFIED_OWA` classification. It returns a boolean value indicating that the concept does not belong to the QOWA category, facilitating type filtering within the broader operator concept hierarchy. The function performs a pure check without modifying the input concept.

      :param op: The concept to verify is not of type QUANTIFIED_OWA.
      :type op: Concept

      :return: True if the concept is not a Quantified OWA, False otherwise.

      :rtype: bool



   .. py:method:: is_not_quasi_sugeno(op: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> bool
      :staticmethod:


      Determines whether the provided operator concept is not a Quasi-Sugeno integral. This static method accepts a Concept object and returns True if the concept's type does not match the Quasi-Sugeno Integral classification. It functions as a specific type-checking utility that delegates the underlying comparison logic to the `is_not_type` method.

      :param op: The concept to check against the Quasi-Sugeno integral type.
      :type op: Concept

      :return: True if the provided concept is not a Quasi-Sugeno integral, False otherwise.

      :rtype: bool



   .. py:method:: is_not_self(op: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> bool
      :staticmethod:


      Determines whether the provided concept is not classified as a "self" concept. This method acts as a specific type check, delegating to the general type verification logic to ensure the concept's type does not match `ConceptType.SELF`. It returns a boolean result without modifying the input object or causing side effects.

      :param op: The concept to check against the SELF type.
      :type op: Concept

      :return: True if the provided concept is not of type SELF, False otherwise.

      :rtype: bool



   .. py:method:: is_not_sigma_concept(op: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> bool
      :staticmethod:


      Determines whether the provided concept is not a sigma concept. This static method accepts a `Concept` object and returns `True` if the concept's type does not match `ConceptType.SIGMA_CONCEPT`, returning `False` otherwise. It relies on the `is_not_type` helper method to perform the underlying type verification.

      :param op: The concept to check.
      :type op: Concept

      :return: True if the concept is not a sigma concept, False otherwise.

      :rtype: bool



   .. py:method:: is_not_sugeno(op: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> bool
      :staticmethod:


      Determines whether the provided operator concept is not a Sugeno integral. This static method acts as a specific predicate that delegates to the generic type-checking logic, verifying that the concept's type attribute does not correspond to the Sugeno integral category. It returns `True` if the concept is of a different type, and `False` if it is identified as a Sugeno integral.

      :param op: The concept to verify is not a Sugeno integral.
      :type op: Concept

      :return: True if the provided concept is not a Sugeno integral, False otherwise.

      :rtype: bool



   .. py:method:: is_not_type(op: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, c_type: fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType) -> bool
      :staticmethod:


      Determines whether a given concept represents a logical negation of a specific concept type. The method first verifies that the input `op` is an instance of `OperatorConcept` and that its type is `COMPLEMENT`. If these structural conditions are not met, the function returns `False`. Otherwise, it checks if the type of the first nested concept within the operator matches the provided `c_type` argument and returns the result of that comparison.

      :param op: The concept to check, which should represent a logical complement (negation) of the specified type.
      :type op: Concept
      :param c_type: The specific type to match against the operand of the complement operator.
      :type c_type: fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType

      :return: True if the provided concept is a complement operator acting on a concept of the specified type, otherwise False.

      :rtype: bool



   .. py:method:: is_not_weighted(op: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> bool
      :staticmethod:


      Determines whether the provided operator concept is not classified as a weighted operator. This static method acts as a specific predicate that checks if the concept's type differs from `ConceptType.WEIGHTED`. It delegates the actual type verification to the `is_not_type` method, returning `True` if the concept is not weighted and `False` otherwise.

      :param op: The concept to verify is not of type WEIGHTED.
      :type op: Concept

      :return: True if the concept is not weighted, False otherwise.

      :rtype: bool



   .. py:method:: is_not_weighted_max(op: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> bool
      :staticmethod:


      Determines whether the provided operator concept is not a weighted maximum operator. This static method checks the concept's type against `ConceptType.W_MAX` and returns `True` if they do not match, indicating that the concept represents a different kind of operation. The function performs a read-only check and does not modify the input object.

      :param op: The concept to verify is not a weighted maximum operator.
      :type op: Concept

      :return: True if the provided concept is not a weighted maximum operator, False otherwise.

      :rtype: bool



   .. py:method:: is_not_weighted_min(op: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> bool
      :staticmethod:


      Determines whether the provided operator concept is not classified as a weighted minimum. This static method evaluates the type of the input concept and returns True if it does not correspond to the weighted minimum operator type (`ConceptType.W_MIN`). The function performs a read-only check and does not modify the state of the input object.

      :param op: The concept to verify is not a weighted minimum operator.
      :type op: Concept

      :return: True if the concept is not a weighted minimum operator, False otherwise.

      :rtype: bool



   .. py:method:: is_not_weighted_sum(op: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> bool
      :staticmethod:


      Determines whether the provided concept is not a weighted sum operation. This static method serves as a specific type check, evaluating the input concept against the `ConceptType.W_SUM` identifier. It returns `True` if the concept is of any type other than a weighted sum, and `False` if it matches that specific classification.

      :param op: The concept to verify is not a weighted sum operation.
      :type op: Concept

      :return: True if the input concept is not a weighted sum operation, False otherwise.

      :rtype: bool



   .. py:method:: is_not_weighted_sum_zero(op: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> bool
      :staticmethod:


      Determines whether the provided `Concept` instance does not represent a weighted sum zero operation. This static method checks the type of the input concept against `ConceptType.W_SUM_ZERO` and returns `True` if the types do not match. It serves as a specific type guard to identify concepts that are not weighted sum zero, performing no modifications to the input object.

      :param op: The concept to verify is not of the weighted sum zero type.
      :type op: Concept

      :return: True if the concept is not a weighted sum zero, False otherwise.

      :rtype: bool



   .. py:method:: is_not_zadeh_implies(op: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> bool
      :staticmethod:


      Determines whether the provided concept is not specifically a Zadeh implication operator. This static method evaluates the input concept and returns true if its type differs from the Zadeh implies definition, and false otherwise. It serves as a type guard within the `OperatorConcept` module, relying on the underlying `is_not_type` utility to perform the actual comparison against the `ZADEH_IMPLIES` enum value. The operation is read-only and does not modify the input concept.

      :param op: The concept to evaluate.
      :type op: Concept

      :return: True if the given concept is not a Zadeh implication operator, False otherwise.

      :rtype: bool



   .. py:method:: is_or(c_type: fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType) -> bool
      :staticmethod:


      Determines whether the provided concept type represents a logical OR operation by verifying its membership in the class-level collection of OR operators. This static method returns `True` if the input type is found within `OperatorConcept.OR_OPERATORS` and `False` otherwise, serving as a type-checking utility without causing any side effects.

      :param c_type: The concept type to check if it represents an OR operator.
      :type c_type: fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType

      :return: True if the concept type is an OR operator, False otherwise.

      :rtype: bool



   .. py:method:: is_simplified() -> bool

      Determines whether the current logical formula node is considered simplified based on the types of its immediate children. The method returns true if the node is a negated atomic proposition or if none of its direct child concepts share the same operator type as the current node. This logic effectively verifies that the formula is flattened at this level, ensuring that operators are not nested within other operators of the same type (e.g., an AND operation directly containing another AND operation).

      :return: True if the formula is a negated atomic proposition or if the current logical operator is not nested within itself (i.e., the structure is flat at the current level).

      :rtype: bool



   .. py:method:: lukasiewicz_and(*concepts: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept
      :staticmethod:


      Creates a new Concept representing the Łukasiewicz logical conjunction of the provided input concepts. This static method instantiates an operator node of type LUKASIEWICZ_AND and immediately converts the resulting structure into Conjunctive Normal Form (CNF) to standardize its representation. It accepts a variable number of Concept arguments, returning a single Concept that encapsulates the combined logic in its normalized form.

      :param concepts: The concepts to be combined using the Łukasiewicz AND operation.
      :type concepts: Concept

      :return: A Concept representing the Łukasiewicz logical conjunction of the provided concepts.

      :rtype: Concept



   .. py:method:: lukasiewicz_or(*concepts: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept
      :staticmethod:


      Computes the Łukasiewicz disjunction (bounded sum) for a variable number of input concepts. This method constructs an operator node representing the logical operation and immediately normalizes the result into Conjunctive Normal Form (CNF) specific to the Łukasiewicz logic system. It returns a new `Concept` instance representing this normalized logical expression without modifying the original input concepts.

      :param concepts: Variable number of concepts to be combined using the Łukasiewicz OR logic.
      :type concepts: Concept

      :return: A Concept representing the Łukasiewicz disjunction of the provided concepts, converted to Conjunctive Normal Form.

      :rtype: Concept



   .. py:method:: normal_form(is_type: Callable) -> Self

      Converts the concept into a normal form determined by the `is_type` predicate, which selects the primary binary operator for distribution. The method repeatedly applies a suite of logical transformations—such as De Morgan's laws, double negation elimination, distribution, idempotency reduction, truth value reduction, and quantifier reduction—until the expression stabilizes and no further simplifications are possible. This operation modifies the instance in place and returns the updated object.

      :param is_type: A predicate function used to identify the specific binary operator type (e.g., conjunction or disjunction) that defines the target normal form structure.
      :type is_type: typing.Callable

      :return: Returns the current instance after iteratively applying logical equivalences and reductions to achieve a simplified normal form.

      :rtype: typing.Self



   .. py:method:: not_(concept: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept
      :staticmethod:


      Computes the logical complement of the provided concept, performing immediate simplifications where possible. If the input concept represents the universal set (Top), the method returns the empty set (Bottom), and vice versa. In cases of double negation, where the input is already a complement operator, the method unwraps and returns the original inner concept. For all other inputs, it constructs and returns a new complement operator node wrapping the provided concept.

      :param concept: The concept to apply logical negation to.
      :type concept: Concept

      :return: The logical complement of the input concept, handling double negation and specific truth values.

      :rtype: Concept



   .. py:method:: or_(*concepts: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept
      :staticmethod:


      Constructs a new Concept representing the logical disjunction of the provided input concepts. The specific logic applied depends on the global `constants.KNOWLEDGE_BASE_SEMANTICS` setting, supporting Classical, Lukasiewicz, and Zadeh (Gödel) semantics. The resulting operator concept is transformed into Conjunctive Normal Form (CNF) using the method corresponding to the active logic before being returned. This method relies on external configuration state to determine its behavior.

      :param concepts: A variable number of Concept instances to be combined via logical disjunction.
      :type concepts: Concept

      :return: A Concept representing the logical disjunction of the input concepts, calculated according to the current knowledge base semantics.

      :rtype: Concept



   .. py:method:: reduce_double_negation() -> Self

      Recursively simplifies the logical structure by eliminating double negations, applying the equivalence ~(~A) = A. The method first processes all child concepts to ensure the entire subtree is reduced. If the current concept is a negation and its immediate child is also a negation, the method returns the grandchild concept, effectively canceling out both operators. If no double negation is found at the current level, the method returns the current instance with its updated children.

      :return: Returns the concept after recursively eliminating double negations.

      :rtype: typing.Self



   .. py:method:: reduce_idempotency(is_type: Callable) -> Self

      Recursively simplifies the logical structure of the operator concept by applying Boolean algebra reduction rules, including idempotency, domination, complement, and identity laws. The method traverses the tree of child concepts to reduce them first, then removes duplicate operands for operators that support idempotency. It checks for domination conditions, returning the top truth value if the operator is OR and contains top, or the bottom truth value if the operator is AND and contains bottom. Furthermore, it evaluates complement laws to detect contradictions or tautologies where a concept appears alongside its negation. Identity elements that do not trigger short-circuiting are removed, and the method returns the reconstructed, normalized concept, or the original instance if it is an atomic complement.

      :param is_type: A callable function passed recursively to child concepts to assist in type identification or classification during the reduction process.
      :type is_type: typing.Callable

      :return: The simplified concept resulting from recursively applying idempotency, absorption, and complement laws to the operator's children.

      :rtype: typing.Self



   .. py:method:: reduce_quantifiers() -> Self

      Recursively simplifies the logical structure by consolidating quantifiers based on the operator type. First, it applies the reduction process to all child concepts to ensure the tree is normalized from the bottom up. If the current node represents a conjunction (AND or Goedel AND), the method merges multiple universal quantifiers (ALL) sharing the same role into a single quantifier whose restriction is the conjunction of the original restrictions, while filtering out trivial existential quantifiers (SOME). Conversely, if the node represents a disjunction (OR or Goedel OR), it merges multiple existential quantifiers (SOME) sharing the same role into a single quantifier whose restriction is the disjunction of the original restrictions, leaving universal quantifiers unchanged. The method modifies the list of child concepts in place and returns the resulting concept structure, or returns the instance itself if the operator type does not support quantifier reduction.

      :return: Returns a new concept with reduced quantifiers by merging 'ALL' concepts under conjunctions and 'SOME' concepts under disjunctions that share the same role.

      :rtype: typing.Self



   .. py:method:: reduce_truth_values() -> Self

      Recursively traverses and simplifies the logical expression tree represented by the concept by applying reduction rules to its children. For complement operations, it resolves negations of absolute truth values, converting negated Top concepts to Bottom and vice versa. For binary operators, it performs algebraic simplification: conjunctions reduce to Bottom if they contain a Bottom operand or a contradiction (A and not A) under classical logic, while disjunctions reduce to Top if they contain a Top operand or a tautology (A or not A). Additionally, the method removes identity elements (Top from conjunctions, Bottom from disjunctions) and eliminates redundant operands through deduplication for operators supporting absorption. The operation modifies the concept's internal state in place and returns the simplified instance.

      :return: Returns a simplified version of the concept by recursively applying logical reduction rules to resolve identities, annihilators, and contradictions involving Top and Bottom concepts.

      :rtype: typing.Self



   .. py:method:: replace(a: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept

      Recursively replaces occurrences of concept `a` with concept `c` within the structure of the current `OperatorConcept` and transforms the current node into the type of `c`. The method first traverses all child concepts to perform the replacement. If `c` is a logical operator such as AND, OR, or their fuzzy logic variants (Gödel, Łukasiewicz), the method returns a new `OperatorConcept` of that specific type containing the updated children. If `c` is a COMPLEMENT, the method checks if the current concept's first child matches `a`; if so, it returns the negation of `c`, otherwise it returns the current concept unchanged without modifying its children. If `c` is an atomic concept or an unsupported type, the method implicitly returns `None`.

      :param a: The concept to be replaced.
      :type a: Concept
      :param c: The concept to substitute in place of `a`. Its type determines the operator type of the resulting concept structure.
      :type c: Concept

      :return: A new Concept where all occurrences of `a` are recursively replaced by `c`, with the operator type of the resulting concept determined by the type of `c`.

      :rtype: Concept



   .. py:attribute:: ABSORPTION_OPERATORS
      :type:  list[fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType]


   .. py:attribute:: ALL_OPERATORS
      :type:  list[fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType]


   .. py:attribute:: AND_OPERATORS
      :type:  list[fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType]


   .. py:attribute:: BINARY_OPERATORS
      :type:  list[fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType]


   .. py:attribute:: COMPLEMENT_LAW_OPERATORS
      :type:  list[fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType]


   .. py:attribute:: DISTRIBUTIVE_OPERATORS
      :type:  list[fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType]


   .. py:attribute:: OPERATORS
      :type:  dict[fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType, fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType]


   .. py:attribute:: OR_OPERATORS
      :type:  list[fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType]


   .. py:property:: concepts
      :type: list[fuzzy_dl_owl2.fuzzydl.concept.concept.Concept]


      Updates the collection of concepts associated with the operator by accepting an iterable of Concept objects. The provided iterable is converted to a list and stored internally, ensuring that the underlying data structure is mutable and indexable. As a side effect of this assignment, the operator's name is automatically recalculated to reflect the new set of concepts.

      :param value: The collection of Concept objects to assign to the instance, replacing the current concepts and triggering a name update.
      :type value: typing.Iterable[Concept]


   .. py:attribute:: name
      :value: '(and )'


      Updates the name of the Concept instance to the specified string value. This setter modifies the object's internal state by assigning the provided value to the private `_name` attribute, effectively replacing any previously stored name.

      :param value: The new name to assign to the object.
      :type value: str


   .. py:attribute:: type
      :type:  fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType

      Updates the type classification of the Concept instance to the specified value. This setter method assigns the provided `ConceptType` to the internal `_type` attribute, effectively overwriting the previous type definition. The operation modifies the object's state in place and does not return a value.

      :param new_type: The classification or category to assign to the concept.
      :type new_type: fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType


.. py:data:: And

.. py:data:: GoedelAnd

.. py:data:: GoedelOr

.. py:data:: LukasiewiczAnd

.. py:data:: LukasiewiczOr

.. py:data:: Not

.. py:data:: Or
