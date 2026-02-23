import typing

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.util.constants import ConceptType


class TruthConcept(Concept):
    """
    This class models the two extreme truth values within a logical concept hierarchy: the universal concept (Top) and the contradictory concept (Bottom). The Top concept represents a state that is always satisfied, acting as an identity element for conjunction and an absorbing element for disjunction, while the Bottom concept represents a state that is never satisfied, acting inversely. Instances can be created directly using a specific concept type or conveniently retrieved via the static factory methods `get_top` and `get_bottom`. It supports standard logical operations such as negation, conjunction, and disjunction, and is treated as an atomic entity that remains immutable during sub-concept replacement operations.

    :param name: The canonical string representation of the concept, which is "*top*" for the top concept and "*bottom*" for the bottom concept.
    :type name: typing.Any
    """


    def __init__(self, c_type: ConceptType) -> None:
        """
        Initializes a new instance representing a universal or empty concept, restricting the input type to strictly `ConceptType.TOP` or `ConceptType.BOTTOM`. The method validates the provided argument, raising an `AssertionError` if any other value is supplied. It then delegates the core initialization to the parent class and computes the instance's human-readable name by invoking the `compute_name` method.

        :param c_type: The conceptual type of the instance, constrained to be either TOP or BOTTOM.
        :type c_type: ConceptType
        """

        assert c_type in (ConceptType.TOP, ConceptType.BOTTOM)
        if c_type == ConceptType.TOP:
            super().__init__(ConceptType.TOP)
        else:
            super().__init__(ConceptType.BOTTOM)
        self.name = self.compute_name()

    @staticmethod
    def get_top():
        """Returns a new instance representing the universal or "Top" concept within the logical framework. This concept typically signifies the set of all possible individuals or the most general supertype in the ontology. The method acts as a static factory, instantiating a `TruthConcept` object initialized specifically with the `ConceptType.TOP` identifier, and it has no side effects."""

        return TruthConcept(ConceptType.TOP)

    @staticmethod
    def get_bottom():
        """Returns a `TruthConcept` instance representing the bottom element of the conceptual hierarchy. This static method constructs a new object initialized with `ConceptType.BOTTOM`, typically signifying a contradiction or the least defined state. The operation has no side effects and does not depend on instance state."""

        return TruthConcept(ConceptType.BOTTOM)

    def is_atomic(self) -> bool:
        """
        Indicates whether the concept is atomic, representing a fundamental, indivisible unit of truth rather than a compound or derived expression. This method unconditionally returns `True`, signifying that instances of this class are always treated as base-level entities within the logical framework. As the return value is constant, there are no edge cases or side effects associated with this check.

        :return: True if the object is atomic.

        :rtype: bool
        """

        return True

    def is_complemented_atomic(self) -> bool:
        """
        Indicates whether the truth concept represents a complemented atomic proposition, such as a negated literal. This implementation returns False, signifying that the concept is not of this specific type, though subclasses representing negated atomic variables may override this behavior. The method performs no side effects and serves as a predicate for logical classification or pattern matching within the module.

        :return: True if the object is a complemented atomic element.

        :rtype: bool
        """

        return False

    def clone(self) -> typing.Self:
        """
        Creates and returns a new instance of `TruthConcept` that replicates the current object. The clone is initialized using the `type` attribute of the original instance, ensuring the new object shares the same type definition. This method does not modify the state of the original object, although if the `type` attribute is a mutable object, both the original and the clone will reference the same object.

        :return: A new instance of the class that is a copy of the current object.

        :rtype: typing.Self
        """

        return TruthConcept(self.type)

    def replace(self, a: Concept, c: Concept) -> Concept:
        """
        Returns the current instance unchanged, acting as a no-op for the replacement operation. Because a `TruthConcept` is a terminal node representing a logical constant, it contains no internal structure or sub-concepts to traverse or modify. Consequently, regardless of the specific concepts provided as arguments, the method simply returns `self` to indicate that no substitution occurred.

        :param a: The concept to be replaced.
        :type a: Concept
        :param c: The concept to replace `a` with.
        :type c: Concept

        :return: The instance itself.

        :rtype: Concept
        """

        return self

    def compute_name(self) -> typing.Optional[str]:
        """
        Calculates the canonical string name for the concept based on its type attribute. If the concept type is identified as TOP, the method returns the specific string '*top*', while a type of BOTTOM results in '*bottom*'. For any other concept types not explicitly handled by the logic, the method returns None.

        :return: Returns '*top*' if the concept type is TOP, '*bottom*' if it is BOTTOM, or None otherwise.

        :rtype: typing.Optional[str]
        """

        if self.type == ConceptType.TOP:
            return "*top*"
        elif self.type == ConceptType.BOTTOM:
            return "*bottom*"

    def compute_atomic_concepts(self) -> set[Concept]:
        """
        Computes the set of atomic concepts that constitute this entity. Since a `TruthConcept` represents a tautology or universal truth that does not decompose into specific atomic components, this method always returns an empty set. This implementation serves as a specific case where no further decomposition is required, and it does not modify the state of the object.

        :return: A set of the atomic concepts computed for this instance.

        :rtype: set[Concept]
        """

        return set()

    def get_atomic_concepts(self) -> set[typing.Self]:
        """
        Returns a singleton set containing the current instance, representing the atomic concepts that make up this object. This behavior indicates that the concept is indivisible or primitive, as it cannot be broken down into smaller constituent concepts. The operation has no side effects and consistently returns a set with exactly one element: the instance itself.

        :return: A set containing the current instance as the sole atomic concept.

        :rtype: set[typing.Self]
        """

        return set([self])

    def get_atoms(self) -> list[typing.Self]:
        """
        Returns a list containing the current instance, representing the fundamental atomic components of the concept. This method signifies that the `TruthConcept` is an indivisible unit within the logical system, as opposed to composite structures that might decompose into multiple sub-concepts. The operation has no side effects and consistently returns a singleton list regardless of the internal state of the object.

        :return: A list containing the current instance.

        :rtype: list[typing.Self]
        """

        return [self]

    def get_roles(self) -> set[str]:
        """
        Retrieves the set of string-based roles associated with this TruthConcept instance. The current implementation returns an empty set, signifying that no roles are assigned to this specific concept.

        :return: A set of strings representing the roles associated with the object.

        :rtype: set[str]
        """

        return set()

    def __and__(self, value: typing.Self) -> typing.Self:
        """
        Implements the bitwise AND operation (`&`) for the concept, performing a logical conjunction with another instance. If the current instance represents the "Top" concept, the method returns the provided value, effectively acting as an identity element. If the current instance is not "Top," the method returns the bottom concept, resulting in the minimal element of the lattice regardless of the input value. This operation does not modify the state of the current instance or the provided value.

        :param value: The other operand in the logical conjunction.
        :type value: typing.Self

        :return: Returns the provided value if the current instance is the Top concept, otherwise returns the Bottom concept.

        :rtype: typing.Self
        """

        return value if self.type == ConceptType.TOP else TruthConcept.get_bottom()

    def __or__(self, value: typing.Self) -> typing.Self:
        """
        Implements the logical disjunction (OR) operation for the concept using the bitwise OR operator syntax. If the current instance represents the 'top' concept (often interpreted as 'true' or 'universal'), the method returns the top concept, effectively short-circuiting the result regardless of the other operand. Otherwise, the method returns the provided value. This operation does not modify the state of the current instance or the provided value.

        :param value: The right-hand operand for the disjunction operation, returned if the current instance is not Top.
        :type value: typing.Self

        :return: Returns the top concept if the current instance is the top concept; otherwise, returns the provided value.

        :rtype: typing.Self
        """

        return TruthConcept.get_top() if self.type == ConceptType.TOP else value

    def __rshift__(self, value: Concept) -> Concept:
        """
        Implements the right-shift operator (`>>`) to interact with another Concept. If the current instance is of type 'Top', the method returns the provided value. In all other cases, it returns the 'Top' concept.

        :param value: The Concept instance on the right-hand side of the operator.
        :type value: Concept

        :return: The result of the right-shift operation. Returns the provided value if the current concept is of type TOP; otherwise, returns the top concept.

        :rtype: Concept
        """

        if self.type == ConceptType.TOP:
            return value
        else:
            return TruthConcept.get_top()

    def __neg__(self) -> typing.Self:
        """
        Implements the unary negation operator for the truth concept, effectively inverting its logical state. If the current instance represents the top concept (universal truth), this method returns a new instance representing the bottom concept (falsehood), and vice versa. This operation does not modify the original instance in place but instead returns a new `TruthConcept` object with the inverted type.

        :return: The logical negation of the concept, swapping Top for Bottom and vice versa.

        :rtype: typing.Self
        """

        if self.type == ConceptType.TOP:
            return TruthConcept(ConceptType.BOTTOM)
        else:
            return TruthConcept(ConceptType.TOP)

    def __hash__(self) -> int:
        """
        Computes the integer hash value for the instance based on the `name` attribute. This allows `TruthConcept` objects to be used as dictionary keys or elements within sets. The implementation ensures that two instances with identical names will produce the same hash value, which is a requirement for consistent behavior in hash-based collections.

        :return: An integer hash value derived from the object's name attribute.

        :rtype: int
        """

        return hash(self.name)

    def __eq__(self, value: typing.Self) -> bool:
        """
        Determines equality between the current instance and another object by checking both type and string representation. The method returns True only if the provided value is an instance of the same class and its string representation matches that of the current instance. If the value is of a different type or the string representations differ, the method returns False.

        :param value: The object to compare against. Equality is determined by verifying the object is an instance of the same class and has an identical string representation.
        :type value: typing.Self

        :return: True if the provided value is an instance of TruthConcept and has the same string representation as this instance, otherwise False.

        :rtype: bool
        """

        return isinstance(value, TruthConcept) and str(self) == str(value)

    def __ne__(self, value: typing.Self) -> bool:
        """
        Determines whether the current instance is not equal to the provided value by negating the result of the equality comparison. This method delegates the actual comparison logic to the `__eq__` method, meaning its behavior is directly tied to how equality is defined for the class. If the equality check returns `True`, this method returns `False`, and vice versa, ensuring consistency between the two operations.

        :param value: The object to compare against the current instance.
        :type value: typing.Self

        :return: True if the current instance is not equal to the specified value, False otherwise.

        :rtype: bool
        """

        return not (self == value)


TOP: Concept = TruthConcept.get_top()
BOTTOM: Concept = TruthConcept.get_bottom()
