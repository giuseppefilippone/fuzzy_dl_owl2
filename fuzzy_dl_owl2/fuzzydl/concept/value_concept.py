import typing

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.concept.interface.has_value_interface import (
    HasValueInterface,
)
from fuzzy_dl_owl2.fuzzydl.concept.operator_concept import OperatorConcept
from fuzzy_dl_owl2.fuzzydl.util.constants import ConceptType


class ValueConcept(Concept, HasValueInterface):
    """
    This class represents a value restriction used to define numerical constraints on the fillers of a specific role within a description logic system. It encapsulates concepts such as "at most," "at least," or "exactly" a certain number of related individuals, allowing for the precise definition of cardinality restrictions. Users can instantiate this object by specifying a concept type, a role, and a value, or utilize the provided static factory methods for more readable creation. The class automatically generates a string representation of the constraint and integrates with the broader concept hierarchy, supporting logical operations while acting as a terminal node that does not decompose into sub-concepts.

    :param name: The string representation of the concept, formatted as a parenthesized expression combining the operator, role, and value.
    :type name: typing.Any
    """


    def __init__(self, c_type: ConceptType, role: str, value: typing.Any) -> None:
        """
        Initializes a value-based concept by setting up the necessary type, role, and value attributes. This constructor validates that the provided concept type is strictly one of the value-related constraints: AT_MOST_VALUE, AT_LEAST_VALUE, or EXACT_VALUE. It chains initialization to the base Concept class and the HasValueInterface mixin to establish the core structure and value storage. Finally, it automatically computes and assigns a descriptive name based on the provided parameters.

        :param c_type: The specific type of the concept, which must be a value-based constraint (AT_MOST_VALUE, AT_LEAST_VALUE, or EXACT_VALUE).
        :type c_type: ConceptType
        :param role: The label or identifier for the value, defining its specific function or attribute within the concept.
        :type role: str
        :param value: The value associated with the concept, used to define the specific instance or constraint.
        :type value: typing.Any
        """

        Concept.__init__(self, c_type)
        HasValueInterface.__init__(self, role, value)

        assert c_type in (
            ConceptType.AT_MOST_VALUE,
            ConceptType.AT_LEAST_VALUE,
            ConceptType.EXACT_VALUE,
        )

        self.name = self.compute_name()

    @staticmethod
    def at_most_value(role: str, o: typing.Any) -> typing.Self:
        """
        Constructs a `ValueConcept` instance representing a constraint where the value associated with a specific role is less than or equal to a given limit. This static method accepts a string identifying the role and an arbitrary object representing the maximum value, initializing the concept with the `AT_MOST_VALUE` type. The method acts as a factory that wraps the provided value directly without performing validation or side effects.

        :param role: The role or identifier for the value within the concept.
        :type role: str
        :param o: The value representing the upper bound or maximum limit.
        :type o: typing.Any

        :return: Returns a ValueConcept instance representing an "at most" constraint for the specified role and value.

        :rtype: typing.Self
        """

        return ValueConcept(ConceptType.AT_MOST_VALUE, role, o)

    @staticmethod
    def at_least_value(role: str, o: typing.Any) -> typing.Self:
        """
        This static method acts as a factory for creating a specific type of constraint object, instantiating a `ValueConcept` that represents a minimum threshold or "greater than or equal to" condition. It accepts a string defining the role of the concept and an arbitrary object representing the target value, which are passed to the constructor along with the `AT_LEAST_VALUE` type indicator. The function returns a new instance of the class, encapsulating the provided data within the context of this specific constraint logic without modifying any global state.

        :param role: The identifier or name of the role that the minimum value constraint applies to.
        :type role: str
        :param o: The threshold value or object defining the lower bound of the concept.
        :type o: typing.Any

        :return: Returns an instance representing a concept where the value associated with the specified role is greater than or equal to the provided object.

        :rtype: typing.Self
        """

        return ValueConcept(ConceptType.AT_LEAST_VALUE, role, o)

    @staticmethod
    def exact_value(role: str, o: typing.Any) -> typing.Self:
        """
        Creates a `ValueConcept` instance representing an exact value by wrapping a provided object and role string. This static method serves as a specialized factory that tags the resulting concept with the `EXACT_VALUE` type, distinguishing it from other concept types. It accepts any Python object as the value payload and has no side effects, simply returning a new instance initialized with the specified arguments.

        :param role: The role or identifier for the exact value.
        :type role: str
        :param o: The specific value or object to be encapsulated by the concept.
        :type o: typing.Any

        :return: A new instance representing an exact value concept associated with the specified role and object.

        :rtype: typing.Self
        """

        return ValueConcept(ConceptType.EXACT_VALUE, role, o)

    def clone(self) -> typing.Self:
        """
        Creates and returns a new instance of `ValueConcept` that is a copy of the current object. The new instance is initialized with the same `type`, `role`, and `value` attributes as the original. This method performs a shallow copy, meaning that if the `value` attribute is a mutable object, the clone will reference the same underlying object as the original; therefore, modifications to that mutable object will be reflected in both instances. The original object remains unmodified by this operation.

        :return: A new instance of the class with the same type, role, and value as the current object.

        :rtype: typing.Self
        """

        return ValueConcept(self.type, self.role, self.value)

    def replace(self, a: Concept, c: Concept) -> Concept:
        """
        Returns the current instance unmodified, acting as a terminal case for replacement operations within a concept hierarchy. Since a ValueConcept represents an atomic value that does not contain nested concepts, it cannot perform a substitution of sub-components. As a result, the arguments `a` and `c` are ignored, and the method returns `self` to preserve the structure when traversing or transforming composite concepts.

        :param a: The concept to be replaced.
        :type a: Concept
        :param c: The concept to substitute in place of `a`.
        :type c: Concept

        :return: The concept itself, returned unchanged.

        :rtype: Concept
        """

        return self

    def compute_name(self) -> typing.Optional[str]:
        """
        Generates a formatted string representation of the concept based on its type, role, and value attributes. For 'at most' constraints, it returns a string formatted as '(<= role value)', while 'at least' constraints produce '(>= role value)' and exact values produce '(= role value)'. If the concept type does not correspond to one of these specific value constraints, the method returns None. This operation does not modify the object's state.

        :return: A string representing the concept as a logical constraint (e.g., '(<= role value)') based on its type, role, and value, or None if the type is not a specific value constraint.

        :rtype: typing.Optional[str]
        """

        if self.type == ConceptType.AT_MOST_VALUE:
            return f"(<= {self.role} {self.value})"
        elif self.type == ConceptType.AT_LEAST_VALUE:
            return f"(>= {self.role} {self.value})"
        elif self.type == ConceptType.EXACT_VALUE:
            return f"(= {self.role} {self.value})"

    def compute_atomic_concepts(self) -> set[Concept]:
        """
        Computes the set of atomic concepts associated with this entity. Since this is a `ValueConcept`, representing a concrete value rather than a complex type or class definition, it does not decompose into further atomic concepts. Consequently, the method always returns an empty set, indicating that no atomic concepts are derived from this specific node. This operation has no side effects.

        :return: A set of atomic concepts associated with the object.

        :rtype: set[Concept]
        """

        return set()

    def get_roles(self) -> set[str]:
        """
        Retrieves the set of roles associated with the `ValueConcept` instance. This implementation returns an empty set, indicating that the base concept does not possess any specific roles. The method has no side effects and does not rely on the object's internal state.

        :return: A set of strings representing the roles associated with the object.

        :rtype: set[str]
        """

        return set()

    def __neg__(self) -> Concept:
        """
        Implements the unary negation operator for the value concept, enabling the use of the minus sign to invert the instance. It returns a new `Concept` object representing the logical negation of the current object by delegating to `OperatorConcept.not_`. This operation does not modify the original instance but instead produces a distinct concept that encapsulates the NOT logic.

        :return: A new Concept representing the logical negation of the current instance.

        :rtype: Concept
        """

        return OperatorConcept.not_(self)

    def __and__(self, value: typing.Self) -> typing.Self:
        """
        Performs a logical conjunction or intersection by implementing the bitwise AND operator (`&`) for the instance. This method delegates the core logic to `OperatorConcept.and_`, passing the current object and the provided value to generate the result. The operation returns a new instance of the same type representing the combined concept, leaving the original operands unmodified, and expects the input value to be compatible with the underlying implementation.

        :param value: Another instance of the same class to perform the AND operation with.
        :type value: typing.Self

        :return: The result of the AND operation between the current instance and the provided value.

        :rtype: typing.Self
        """

        return OperatorConcept.and_(self, value)

    def __or__(self, value: typing.Self) -> typing.Self:
        """
        Implements the bitwise OR operation for the `ValueConcept` class, allowing instances to be combined using the `|` operator. This method takes another instance of the same type and delegates the logic to `OperatorConcept.or_` to compute the disjunction. It returns a new `ValueConcept` instance representing the result of the operation, leaving the original operands unchanged.

        :param value: Another instance of the same type to perform the OR operation with.
        :type value: typing.Self

        :return: The result of the logical OR operation between this instance and the provided value.

        :rtype: typing.Self
        """

        return OperatorConcept.or_(self, value)

    def __hash__(self) -> int:
        """
        Computes a hash value for the instance based on its string representation, enabling the object to be used as a key in dictionaries or as a member of sets. The implementation delegates the hashing logic to the built-in hash function applied to the result of the object's string conversion, ensuring that two instances with identical string representations yield the same hash. Because the hash is derived from the string representation, any internal state changes that alter the output of `str(self)` will result in a different hash value, which may cause issues if the object is used in hash-based collections after being modified.

        :return: An integer hash value derived from the string representation of the object.

        :rtype: int
        """

        return hash(str(self))
