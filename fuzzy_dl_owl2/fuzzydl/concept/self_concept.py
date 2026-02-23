import typing

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.concept.interface.has_role_interface import HasRoleInterface
from fuzzy_dl_owl2.fuzzydl.concept.operator_concept import OperatorConcept
from fuzzy_dl_owl2.fuzzydl.util.constants import ConceptType


class SelfConcept(Concept, HasRoleInterface):
    """
    Represents a self-referential concept within fuzzy description logic, specifically denoting that an individual satisfies a relationship with itself through a given role. This construct is essential for expressing reflexivity or local reflexivity properties, where an entity must be linked to itself via the specified role to satisfy the concept. To utilize this class, instantiate it by providing the specific role name as a string, which will automatically generate a standardized string representation. Once created, it behaves as an atomic concept that can be combined with other concepts using logical operators such as conjunction, disjunction, and negation, and it supports cloning and role retrieval operations.

    :param name: The canonical string representation of the concept, formatted as "(self role)".
    :type name: typing.Any
    """


    def __init__(self, role: str) -> None:
        """
        Initializes a new instance representing a self-concept, configuring it with the specific type `ConceptType.SELF`. It accepts a string argument defining the role, which is applied via the `HasRoleInterface`, and automatically derives and assigns the instance's name based on the provided role.

        :param role: The specific role or capacity assigned to this instance.
        :type role: str
        """

        Concept.__init__(self, ConceptType.SELF)
        HasRoleInterface.__init__(self, role)
        self.name = self.compute_name()

    @staticmethod
    def self(role: str) -> typing.Self:
        """
        This static method acts as a factory function for creating new instances of the `SelfConcept` class. It accepts a single string argument representing the role, which is passed directly to the class constructor during initialization. The method returns a new `SelfConcept` object configured with the provided role.

        :param role: The role or persona defining the self-concept.
        :type role: str

        :return: A new instance of the class representing the self concept for the specified role.

        :rtype: typing.Self
        """

        return SelfConcept(role)

    def clone(self):
        """Creates and returns a new `SelfConcept` instance that duplicates the current object, initialized with the same `role` attribute. This method performs a shallow copy of the object's state, meaning the new instance shares the reference to the original `role` object if it is mutable. The operation has no side effects on the original instance."""

        return SelfConcept(self.role)

    def replace(self, a: Concept, c: Concept) -> Concept:
        """
        Returns the current instance unchanged, acting as a base case for replacement operations. Since a SelfConcept does not contain nested or child concepts, there are no internal structures to substitute. The method ignores the source and replacement concepts provided as arguments and simply returns the object itself.

        :param a: The concept to be replaced.
        :type a: Concept
        :param c: The concept to substitute for `a`.
        :type c: Concept

        :return: Returns the instance itself.

        :rtype: Concept
        """

        return self

    def compute_name(self) -> typing.Optional[str]:
        """
        Constructs and returns a string representation of the self-concept by embedding the instance's role into a specific format. The output follows the pattern '(self {role})', where the placeholder is replaced by the value of the `role` attribute. This method performs a read-only operation and assumes the `role` attribute is accessible on the instance.

        :return: A string representing the computed name, formatted as "(self {role})".

        :rtype: typing.Optional[str]
        """

        return f"(self {self.role})"

    def compute_atomic_concepts(self) -> set[Concept]:
        """
        Computes and returns the set of atomic concepts that constitute this entity. By returning a set containing only the instance itself, the method indicates that this concept is atomic and cannot be decomposed into smaller constituent concepts. The operation is stateless and has no side effects, as it merely constructs and returns a new set containing the current object.

        :return: A set containing the concept itself.

        :rtype: set[Concept]
        """

        return set([self])

    def get_roles(self) -> set[str]:
        """
        Retrieves the specific role assigned to the instance and returns it as a set containing a single string element. This method encapsulates the internal `role` attribute, ensuring the return type is always a collection for consistency with other methods that may handle multiple roles. The function has no side effects on the instance's state, and because it returns a new set object, any modifications made to the result will not impact the original data.

        :return: A set containing the role associated with the instance.

        :rtype: set[str]
        """

        return set([self.role])

    def __neg__(self) -> Concept:
        """
        Implements the unary negation operator for the concept, allowing the use of the minus sign (`-`) to represent logical negation. This method returns a new `Concept` instance that serves as the logical complement of the current object by delegating the operation to `OperatorConcept.not_`. The original concept remains unmodified, as the operation produces a distinct entity representing the 'not' state.

        :return: A new Concept representing the logical negation (NOT) of the current concept.

        :rtype: Concept
        """

        return OperatorConcept.not_(self)

    def __and__(self, value: typing.Self) -> typing.Self:
        """
        Performs a logical conjunction between the current concept and another provided concept, enabling the use of the bitwise AND operator (`&`) to combine them. This method returns a new instance representing the intersection or combination of the two operands, leaving the original concepts unmodified. The actual logic is delegated to `OperatorConcept.and_`, which handles the specifics of the conjunction operation. While the method expects a value of the same type, specific behaviors regarding incompatible inputs or contradictory concepts are determined by the underlying operator implementation.

        :param value: The right-hand operand for the AND operation.
        :type value: typing.Self

        :return: The result of the bitwise AND operation between this instance and the provided value.

        :rtype: typing.Self
        """

        return OperatorConcept.and_(self, value)

    def __or__(self, value: typing.Self) -> typing.Self:
        """
        Implements the bitwise OR operator (`|`) to perform a logical disjunction or union between the current concept and another concept of the same type. This method delegates the actual computation to `OperatorConcept.or_`, ensuring consistent handling of the operation logic. It returns a new instance representing the combined concept, leaving the original operands unmodified. If the provided value is not a compatible concept, the underlying implementation may raise a TypeError.

        :param value: The right-hand operand to combine with the current instance using the OR operation.
        :type value: typing.Self

        :return: A new instance representing the logical OR of the current instance and the provided value.

        :rtype: typing.Self
        """

        return OperatorConcept.or_(self, value)

    def __hash__(self) -> int:
        """
        Computes an integer hash value for the object based on its string representation. By delegating to the hash of `str(self)`, this method ensures that the hash is consistent with the object's textual output, allowing instances to be used as dictionary keys or stored in sets. This implementation implies that the hashability of the object is directly tied to the stability and uniqueness of its string representation.

        :return: An integer representing the hash of the object's string representation.

        :rtype: int
        """

        return hash(str(self))
