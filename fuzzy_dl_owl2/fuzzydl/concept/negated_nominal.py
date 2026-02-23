import typing

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.concept.operator_concept import OperatorConcept
from fuzzy_dl_owl2.fuzzydl.exception.fuzzy_ontology_exception import (
    FuzzyOntologyException,
)
from fuzzy_dl_owl2.fuzzydl.util.constants import ConceptType


class NegatedNominal(Concept):
    """
    This class models a negated nominal concept within the framework of fuzzy description logic, specifically representing the complement of a named individual. It is designed to express constraints that exclude specific individuals from a domain, often utilized in range restrictions. To use it, instantiate the object with the name of the individual to be negated; the class automatically generates a standardized string representation for this exclusion. While it supports logical operations like conjunction and disjunction, it enforces a strict limitation where further negation is prohibited, raising an exception if such an operation is attempted.

    :param _ind_name: Internal storage for the identifier of the individual being negated, serving as the backing field for the public property.
    :type _ind_name: str
    :param name: The canonical string representation of the negated nominal, formatted as "(not { ind_name } )".
    :type name: str

    :raises FuzzyOntologyException: Raised when attempting to apply the negation operator to a NegatedNominal instance, as nested negation of nominals is not supported in fuzzy description logic.
    """


    def __init__(self, ind_name: str) -> None:
        """
        Initializes a new instance representing the logical negation of a nominal concept. The method accepts a string identifier for the individual to be negated and configures the instance as an atomic concept type within the parent class hierarchy. It stores the provided identifier internally and generates a formatted string representation for the object's name, explicitly wrapping the input identifier in a negation syntax. While the method assumes the input is a valid string, it does not perform validation on the content of the identifier.

        :param ind_name: The name of the individual concept to be negated.
        :type ind_name: str
        """

        super().__init__(ConceptType.ATOMIC)
        self._ind_name: str = ind_name
        self.name: str = f"(not {{ {ind_name} }} )"

    @property
    def ind_name(self) -> str:
        """
        Sets the value of the `ind_name` property for the `NegatedNominal` instance. This method accepts a string argument and updates the underlying private attribute `_ind_name`, thereby modifying the object's state. It serves as the public interface for mutating the instance's name, overwriting any existing value without performing validation on the input type or content.

        :param value: The string value to assign to the ind_name attribute.
        :type value: str
        """

        return self._ind_name

    @ind_name.setter
    def ind_name(self, value: str) -> None:
        self._ind_name = value

    def clone(self) -> typing.Self:
        """
        Creates and returns a new instance of `NegatedNominal` that is a copy of the current object. The new instance is initialized with the same `ind_name` attribute as the original, ensuring logical equivalence while maintaining object identity separation. This method does not modify the existing instance or have any side effects on the original object's state.

        :return: A new instance of `NegatedNominal` initialized with the same individual name as the current object.

        :rtype: typing.Self
        """

        return NegatedNominal(self.ind_name)

    def compute_name(self) -> str | None:
        """
        Retrieves the name associated with the `NegatedNominal` instance. This method returns the value of the `name` attribute, which may be a string or `None` if no name has been assigned. It serves as a direct accessor without performing additional computation or modification of the instance state.

        :return: The name associated with the instance, or None if it is not set.

        :rtype: str | None
        """

        return self.name

    def __neg__(self) -> typing.Self:
        """
        Implements the unary negation operation for the nominal. However, since the instance already represents a negated concept, applying a further complement is not permitted by the underlying logic. Consequently, this method always raises a FuzzyOntologyException to enforce the constraint that negated nominals cannot be complemented.

        :raises FuzzyOntologyException: Raised when attempting to negate a negated nominal, as negated nominals cannot be complemented.

        :return: Raises FuzzyOntologyException indicating that negated nominals cannot be complemented.

        :rtype: typing.Self
        """

        raise FuzzyOntologyException("Negated nominals cannot be complemented")

    def __hash__(self) -> int:
        """
        Returns an integer hash value for the object, allowing instances to be used as dictionary keys or elements in sets. The hash is calculated by passing the string representation of the instance to the built-in hash function. This means the hash value is strictly dependent on the output of the object's string conversion method, and any exceptions raised during that conversion will propagate to the caller.

        :return: An integer hash value computed from the string representation of the object.

        :rtype: int
        """

        return hash(str(self))

    def __and__(self, value: typing.Self) -> typing.Self:
        """
        Implements the bitwise AND operation (`&`) for the `NegatedNominal` class, enabling logical conjunction between two instances. This method accepts another `NegatedNominal` object as the right-hand operand and delegates the actual computation to the `OperatorConcept.and_` static method. The operation returns a new instance of `NegatedNominal` representing the result of the conjunction, ensuring type consistency with the operands.

        :param value: The other operand to perform the AND operation with, expected to be of the same type as the current instance.
        :type value: typing.Self

        :return: The result of the logical AND operation between this instance and the provided value.

        :rtype: typing.Self
        """

        return OperatorConcept.and_(self, value)

    def __or__(self, value: typing.Self) -> typing.Self:
        """
        Implements the bitwise OR operator (`|`) to combine the current instance with another `NegatedNominal` object. This method delegates the combination logic to `OperatorConcept.or_`, returning a new instance that represents the union or logical disjunction of the two operands. The operation is side-effect free, as it generates a new object rather than modifying the existing instances.

        :param value: The right-hand operand for the OR operation.
        :type value: typing.Self

        :return: Returns the result of the OR operation between this instance and the provided value.

        :rtype: typing.Self
        """

        return OperatorConcept.or_(self, value)
