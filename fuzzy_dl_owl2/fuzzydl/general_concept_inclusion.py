from __future__ import annotations

import typing

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.degree.degree import Degree
from fuzzy_dl_owl2.fuzzydl.util.constants import LogicOperatorType


class GeneralConceptInclusion:
    """
    Represents a fuzzy logic axiom stating that one concept is included within another to a specific degree of truth. It defines a relationship between a subsumed concept and a subsumer concept, utilizing a specific logic operator type (such as Łukasiewicz or Gödel) to determine the implication semantics. Users can instantiate this class to define axioms, modify the degree or concepts via setter methods, and compare instances for equality or ordering. The object is mutable, allowing updates to the underlying concepts or the degree of inclusion after creation.

    :param subsumer: The general concept or super-category that encompasses the subsumed concept.
    :type subsumer: Concept
    :param subsumed: The concept that is included within the subsumer concept.
    :type subsumed: Concept
    :param degree: The lower bound truth value specifying the minimum extent to which the subsumed concept is included in the subsumer concept.
    :type degree: Degree
    :param type: Specifies the fuzzy implication operator (e.g., Łukasiewicz, Gödel, Product) used to evaluate the truth of the inclusion.
    :type type: LogicOperatorType
    """


    def __init__(
        self,
        subsumer: Concept,
        subsumed: Concept,
        degree: Degree,
        type_: LogicOperatorType,
    ):
        # Subsumer concept
        """
        Initializes a General Concept Inclusion (GCI) instance representing a graded subsumption relationship between two concepts. This constructor assigns the provided subsumer (super-concept), subsumed (sub-concept), and the specific logic operator type to the instance attributes. It also stores the degree, which functions as a lower bound truth value indicating the strength or certainty of the inclusion relationship.

        :param subsumer: The broader or more general concept that encompasses the subsumed concept.
        :type subsumer: Concept
        :param subsumed: The concept that is being generalized by the subsumer.
        :type subsumed: Concept
        :param degree: The lower bound degree representing the truth value of the subsumption relationship.
        :type degree: Degree
        :param type_: The specific logic operator type used to define the fuzzy implication.
        :type type_: LogicOperatorType
        """

        self.subsumer: Concept = subsumer
        # Subsumed concept
        self.subsumed: Concept = subsumed
        # Lower bound degree
        self.degree: Degree = degree
        # Type (depends on the fuzzy implication)
        self.type: LogicOperatorType = type_

    def clone(self) -> typing.Self:
        """
        Creates and returns a new instance of the class that replicates the state of the current object. The new object is initialized with the same `subsumer`, `subsumed`, `degree`, and `type` attributes as the original. This method performs a shallow copy of the attributes, meaning that if they are mutable objects, modifications to those objects in the clone will affect the original instance. The operation does not modify the state of the current object.

        :return: A new instance of the class with the same attribute values as the current object.

        :rtype: typing.Self
        """

        return GeneralConceptInclusion(
            self.subsumer, self.subsumed, self.degree, self.type
        )

    def get_subsumer(self) -> Concept:
        """
        Retrieves the super-concept, or subsumer, associated with this general concept inclusion. This represents the concept on the right-hand side of the inclusion relationship, effectively the broader category that the sub-concept falls under. The method acts as a simple accessor for the internal `subsumer` attribute and does not modify the object's state.

        :return: The concept that subsumes the current object.

        :rtype: Concept
        """

        return self.subsumer

    def get_subsumed(self) -> Concept:
        """
        Returns the concept that is subsumed within this general concept inclusion axiom. In the context of the inclusion relationship, this represents the subclass or the left-hand side of the statement. The method acts as a simple accessor for the internal `subsumed` attribute and does not modify the state of the object or perform any computations.

        :return: The concept that is subsumed by this instance.

        :rtype: Concept
        """

        return self.subsumed

    def get_type(self) -> LogicOperatorType:
        """
        Retrieves the specific logic operator type associated with this general concept inclusion instance. This method acts as a getter for the internal `type` attribute, returning the classification of the logical operator without modifying the object's state.

        :return: The logic operator type associated with this instance.

        :rtype: LogicOperatorType
        """

        return self.type

    def get_degree(self) -> Degree:
        """
        Returns the degree associated with this general concept inclusion. This method serves as an accessor to retrieve the internal attribute representing the weight, confidence, or specific metric of the inclusion relationship. It performs a read-only operation and does not alter the state of the object.

        :return: The `Degree` object associated with this instance.

        :rtype: Degree
        """

        return self.degree

    def set_degree(self, deg: Degree) -> None:
        """
        Assigns the specified degree value to the `GeneralConceptInclusion` instance, replacing any existing value stored in the `degree` attribute. This method acts as a direct setter for the internal state, accepting a `Degree` object as input. Since it performs a direct assignment without validation logic, callers should ensure that the provided `deg` argument is valid and appropriate for the context of the concept inclusion, as this mutation occurs in place and affects subsequent operations that rely on the degree property.

        :param deg: The degree value to assign to the instance.
        :type deg: Degree
        """

        self.degree = deg

    def set_subsumer(self, new_concept: Concept) -> None:
        """
        Updates the super-concept, or subsumer, associated with this General Concept Inclusion. The method accepts a `Concept` instance which replaces the current value of the `subsumer` attribute. This operation directly mutates the object's state, overwriting any previously defined subsumer without performing validation or checks on the new concept.

        :param new_concept: The concept to assign as the subsumer.
        :type new_concept: Concept
        """

        self.subsumer = new_concept

    def set_subsumed(self, new_concept: Concept) -> None:
        """
        Assigns the provided concept as the subsumed entity within this general concept inclusion relationship. This method directly overwrites the existing `subsumed` attribute with the new value, effectively updating the left-hand side of the inclusion statement. It performs no validation on the input type beyond the type hint, so passing an incompatible object may lead to errors in subsequent operations.

        :param new_concept: The concept to assign to the subsumed attribute.
        :type new_concept: Concept
        """

        self.subsumed = new_concept

    def __eq__(self, other: typing.Self) -> bool:
        """
        Determines structural equality between the current instance and another object by verifying that the other object is an instance of the same class and that all critical attributes are identical. The comparison specifically checks that the `subsumed`, `subsumer`, `degree`, and `type` attributes of both objects match exactly. If the other object is not a `GeneralConceptInclusion` or if any of these attributes differ, the method returns `False`.

        :param other: The object to compare for equality.
        :type other: typing.Self

        :return: True if the other object is an instance of GeneralConceptInclusion and all attributes (subsumed, subsumer, degree, and type) are equal; otherwise, False.

        :rtype: bool
        """

        return (
            isinstance(other, GeneralConceptInclusion)
            and self.subsumed == other.subsumed
            and self.subsumer == other.subsumer
            and self.degree == other.degree
            and self.type == other.type
        )

    def __ne__(self, other: typing.Self) -> bool:
        """
        Checks for inequality between the current instance and another `GeneralConceptInclusion` object. The method returns `True` if the two instances are not considered equal, and `False` otherwise. This implementation relies on the `__eq__` method, effectively returning the logical negation of the equality comparison. Consequently, any specific logic or edge cases handled by the equality operator are implicitly applied here in reverse.

        :param other: The object to compare against.
        :type other: typing.Self

        :return: True if the object is not equal to the other object, False otherwise.

        :rtype: bool
        """

        return not (self == other)

    def __lt__(self, other: typing.Self) -> bool:
        """
        Determines whether the current instance is considered less than another object based on their hash values. The method first checks if the `other` argument is an instance of `GeneralConceptInclusion`; if the types do not match, it returns `False`. When both objects are of the same type, the comparison is performed by evaluating if the hash of the current instance is strictly less than the hash of the `other` instance. Note that because this relies on hash values, the ordering is arbitrary and may vary between Python runs, and distinct objects with identical hash values will not be strictly ordered relative to one another.

        :param other: The object to compare against.
        :type other: typing.Self

        :return: True if `other` is an instance of `GeneralConceptInclusion` and the hash of the current instance is less than the hash of `other`; otherwise, False.

        :rtype: bool
        """

        return isinstance(other, GeneralConceptInclusion) and hash(self) < hash(other)

    def __le__(self, other: typing.Self) -> bool:
        """
        Checks if the current instance is less than or equal to another instance by inverting the result of the greater-than comparison. This implementation relies on the `__gt__` method to define the ordering relationship, returning `True` whenever the instance is not greater than the provided argument. The method performs no side effects and simply returns a boolean value based on the existing comparison logic.

        :param other: The object to compare against the current instance.
        :type other: typing.Self

        :return: True if the instance is less than or equal to the other instance, False otherwise.

        :rtype: bool
        """

        return not (self > other)

    def __gt__(self, other: typing.Self) -> bool:
        """
        Determines whether this instance is considered greater than another object by comparing their hash values. The method returns `True` if the provided argument is an instance of `GeneralConceptInclusion` and the hash of the current instance is strictly greater than the hash of the argument. If the argument is not an instance of the same class or if its hash value is equal to or less than the current instance's hash, the method returns `False`.

        :param other: Another instance of the same class to compare against based on hash value.
        :type other: typing.Self

        :return: True if `other` is an instance of `GeneralConceptInclusion` and the hash of the current object is greater than the hash of `other`; otherwise, False.

        :rtype: bool
        """

        return isinstance(other, GeneralConceptInclusion) and hash(self) > hash(other)

    def __ge__(self, other: typing.Self) -> bool:
        """
        Implements the greater-than-or-equal-to comparison operator for the instance. The method determines the result by negating the outcome of the less-than comparison (`self < other`), effectively checking if the current object is not strictly less than the other. This implementation relies entirely on the `__lt__` method; any exceptions raised during the less-than comparison will be propagated, and if `__lt__` returns `NotImplemented`, this method will return `False` rather than allowing the interpreter to try the reflected comparison.

        :param other: The object to compare against the current instance.
        :type other: typing.Self

        :return: True if the object is greater than or equal to the other object, False otherwise.

        :rtype: bool
        """

        return not (self < other)

    def __hash__(self) -> int:
        """
        Returns the hash value of the object by calculating the hash of its string representation. This allows instances of this class to be used as dictionary keys or stored in sets. Because the hash is derived from the string output, any changes to the object's state that affect its string representation will alter its hash, which may lead to unexpected behavior if the object is used in hash-based collections after modification.

        :return: An integer hash value computed from the string representation of the object.

        :rtype: int
        """

        return hash(str(self))

    def __repr__(self) -> str:
        """
        Returns a string representation of the concept inclusion by delegating to the `__str__` method. Consequently, the output is identical to the informal string representation, prioritizing human readability over a machine-parseable format. This behavior ensures that the object appears consistently whether printed directly or inspected in a debugger.

        :return: Returns the string representation of the object.

        :rtype: str
        """

        return str(self)

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the concept inclusion relationship, formatted to display the logical structure and its associated degree of truth. The representation concatenates the subsumed concept, the first character of the inclusion type's name, the subsumer concept, and the degree value into a specific notation: "subsumed =>_{type} subsumer >= degree". This method has no side effects, though it requires the internal attributes to be properly initialized to avoid errors during string interpolation.

        :return: A formatted string representing the subsumption relationship, displaying the subsumed item, the first letter of the type, the subsumer, and the degree.

        :rtype: str
        """

        return (
            f"{self.subsumed} =>_{self.type.name[0]} {self.subsumer} >= {self.degree}"
        )
