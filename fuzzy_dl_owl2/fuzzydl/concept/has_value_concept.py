import copy
import typing

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.concept.interface.has_value_interface import (
    HasValueInterface,
)
from fuzzy_dl_owl2.fuzzydl.concept.operator_concept import OperatorConcept
from fuzzy_dl_owl2.fuzzydl.util.constants import ConceptType
from fuzzy_dl_owl2.fuzzydl.util.util import Util


class HasValueConcept(Concept, HasValueInterface):
    """
    This class models a specific type of existential restriction, often referred to as a "has-value" concept, which asserts that an individual must be related to a specific value through a defined role. Structurally, it represents the logical form `(b-some r v)`, meaning an entity satisfies this concept if it participates in the relationship `r` with a target entity that corresponds to `v`. To utilize this class, instantiate it by providing a string representing the role and the target value, which can be of various types such as strings or numbers. Once created, the concept can be combined with other concepts using standard logical operators like conjunction, disjunction, and negation, and it automatically generates a standardized string representation for identification. Note that attempting to replace sub-concepts within this specific concept type will result in an error, as it is treated as an atomic unit in that context.

    :param name: String representation of the concept in the format (b-some role value).
    :type name: str
    """


    def __init__(self, role: str, value: typing.Any) -> None:
        """
        Initializes a new instance representing a concept that holds a specific value within a defined role. The constructor accepts a string identifying the role and an arbitrary value to be associated with that role. It configures the instance as a `Concept` of type `HAS_VALUE` and delegates initialization of the role-value pair to the `HasValueInterface`. Additionally, it automatically derives and assigns a canonical name to the instance based on the provided arguments.

        :param role: The semantic role or attribute name associated with the value.
        :type role: str
        :param value: The arbitrary data or object to be associated with the concept, corresponding to the specified role.
        :type value: typing.Any
        """

        Concept.__init__(self, ConceptType.HAS_VALUE)
        HasValueInterface.__init__(self, role, value)

        self.name: str = self.compute_name()

    @staticmethod
    def has_value(role: str, i: typing.Any) -> typing.Self:
        """
        Creates and returns a new instance of the `HasValueConcept` class, associating a specific value with a defined role. This static method acts as a factory function, allowing for the instantiation of the concept using a role identifier and an arbitrary value of any type. Since the method simply delegates to the class constructor, it has no side effects and relies on the underlying class implementation for any input validation or processing.

        :param role: A string identifying the role or name of the value.
        :type role: str
        :param i: The value to be associated with the specified role.
        :type i: typing.Any

        :return: An instance of HasValueConcept initialized with the provided role and value.

        :rtype: typing.Self
        """

        return HasValueConcept(role, i)

    def clone(self) -> typing.Self:
        """
        Creates and returns a new instance of the class that is a deep copy of the current object. The new instance preserves the `role` attribute from the original, while the `value` attribute is recursively copied using `copy.deepcopy` to ensure that modifications to the new object's value do not affect the original. This method is useful for creating independent duplicates of the concept without altering the source data, though it may raise an exception if the value contains objects that cannot be deep-copied.

        :return: A new instance of the class with the same role and a deep copy of the value.

        :rtype: typing.Self
        """

        return HasValueConcept(self.role, copy.deepcopy(self.value))

    def replace(self, a: Concept, c: Concept) -> Concept:
        """
        This method attempts to replace a specified concept `a` with another concept `c` within the current object's structure. However, this functionality is not supported for `HasValueConcept` instances; invoking it results in an error being reported and the method returning `None` rather than performing a substitution.

        :param a: The concept to be replaced within the current structure.
        :type a: Concept
        :param c: The concept to use as the replacement.
        :type c: Concept

        :return: None, after logging an error indicating that the replacement operation is not supported.

        :rtype: Concept
        """

        Util.error(f"Error replacing in concept {self}")
        return None

    def compute_name(self) -> typing.Optional[str]:
        """
        Constructs a string identifier for the concept by interpolating its role and value attributes into a specific parenthetical format. The output follows the pattern '(b-some role value)', serving as a computed name for the entity. This method does not modify the object's state and assumes that the `role` and `value` attributes are available for string formatting.

        :return: A string representing the computed name, formatted as "(b-some {role} {value})".

        :rtype: typing.Optional[str]
        """

        return f"(b-some {self.role} {self.value})"

    def compute_atomic_concepts(self) -> set[Concept]:
        """
        Returns an empty set, as a `HasValueConcept` does not decompose into or reference any atomic named concepts. Unlike complex class expressions that might be unions or intersections of other classes, a `HasValue` restriction is defined solely by a property and a specific filler value, meaning there are no atomic concepts to extract. This method has no side effects and consistently returns an empty set regardless of the internal state of the concept.

        :return: A set of atomic concepts computed by the object.

        :rtype: set[Concept]
        """

        return set()

    def get_roles(self) -> set[str]:
        """
        Retrieves the set of roles associated with the current concept. This default implementation returns an empty set, signifying that no roles are inherently defined for this base concept. The method is designed to be overridden by subclasses to return specific role identifiers as strings, allowing for the extension of functionality within the broader module hierarchy. Because a new set instance is created on every invocation, the operation has no side effects on the object's state.

        :return: A set of strings representing the roles assigned to the object.

        :rtype: set[str]
        """

        return set()

    def __neg__(self) -> Concept:
        """
        Overloads the unary minus operator to provide the logical negation of the current concept. This method returns a new `Concept` instance representing the inverse condition of the original object, effectively wrapping it in a logical 'NOT' operation by delegating to `OperatorConcept.not_`. The operation is side-effect free, leaving the original instance unmodified.

        :return: The logical negation of this concept.

        :rtype: Concept
        """

        return OperatorConcept.not_(self)

    def __and__(self, value: typing.Self) -> typing.Self:
        """
        Performs a bitwise AND operation between the current instance and another value of the same type, enabling the use of the `&` operator. The logic is delegated to `OperatorConcept.and_`, which constructs and returns a new instance representing the conjunction of the two operands. This method generally does not modify the original instances, but may raise an error if the provided value is not a compatible type.

        :param value: The other operand to combine with the current instance using the AND operation.
        :type value: typing.Self

        :return: The result of the AND operation between the current instance and the provided value.

        :rtype: typing.Self
        """

        return OperatorConcept.and_(self, value)

    def __or__(self, value: typing.Self) -> typing.Self:
        """
        Performs a logical OR operation between the current concept and another value using the bitwise OR operator (`|`). This method delegates the logic to `OperatorConcept.or_`, constructing and returning a new instance that represents the combination of the two operands. It allows for the chaining or composition of concepts without modifying the original objects.

        :param value: The right-hand operand for the OR operation, which must be an instance of the same class.
        :type value: typing.Self

        :return: A new instance representing the logical OR of the current object and the provided value.

        :rtype: typing.Self
        """

        return OperatorConcept.or_(self, value)

    def __hash__(self) -> int:
        """
        Returns an integer hash value derived from the string representation of the object, allowing instances to be used as dictionary keys or stored in sets. The calculation is performed by passing the result of `__str__` to the built-in hash function. Because the hash depends on the string output, any mutation of the object that alters its string representation will result in a different hash, which may cause the object to become inaccessible if it is used as a key in a hash-based collection after modification.

        :return: An integer hash of the object's string representation.

        :rtype: int
        """

        return hash(str(self))
