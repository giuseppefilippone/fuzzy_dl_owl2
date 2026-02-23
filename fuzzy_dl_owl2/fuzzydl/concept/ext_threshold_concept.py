import typing

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.concept.interface.has_concept_interface import (
    HasConceptInterface,
)
from fuzzy_dl_owl2.fuzzydl.concept.operator_concept import OperatorConcept
from fuzzy_dl_owl2.fuzzydl.milp.variable import Variable
from fuzzy_dl_owl2.fuzzydl.util.constants import ConceptType


class ExtThresholdConcept(Concept, HasConceptInterface):
    """
    This class models a logical construct that imposes a variable-based threshold on the satisfaction degree of another concept. It defines conditions where an individual satisfies the concept if the degree of satisfaction of a nested concept is either greater than or equal to, or less than or equal to, a specific variable value. The class provides static factory methods to easily create positive or negative threshold concepts and supports standard logical operations such as negation, conjunction, and disjunction. Additionally, it allows for the modification of the threshold variable and the replacement of nested concepts, while delegating the retrieval of atomic concepts and roles to the underlying concept structure.

    :param _weight_variable: Internal storage for the threshold value $w$ in the extended threshold concept expression.
    :type _weight_variable: Variable
    :param name: The computed string representation of the extended threshold concept, formatted according to the threshold operator and weight variable.
    :type name: str
    """


    def __init__(
        self, c_type: ConceptType, c: Concept, weight_variable: Variable
    ) -> None:
        """
        Initializes an instance representing a concept with an external threshold, configuring it with a specific concept type, a base concept, and a weight variable. The method enforces that the provided concept type must be either a positive or negative external threshold, raising an error otherwise. It performs initialization for the parent `Concept` and `HasConceptInterface` classes, stores the weight variable, and automatically computes the instance's name.

        :param c_type: The type of the concept, which must be either a positive or negative external threshold.
        :type c_type: ConceptType
        :param c: The concept instance to be associated with this object.
        :type c: Concept
        :param weight_variable: The variable defining the weight or threshold value for the concept.
        :type weight_variable: Variable
        """

        Concept.__init__(self, c_type)
        HasConceptInterface.__init__(self, c)

        assert c_type in (
            ConceptType.EXT_POS_THRESHOLD,
            ConceptType.EXT_NEG_THRESHOLD,
        )
        self._weight_variable: Variable = weight_variable
        self.name: str = self.compute_name()

    @property
    def weight_variable(self) -> Variable:
        """
        Sets the weight variable associated with this concept instance. This method accepts a Variable object and assigns it to the internal `_weight_variable` attribute, replacing any existing value. It serves as the setter for the `weight_variable` property, enabling external modification of the concept's internal state.

        :param value: The instance to assign as the weight variable.
        :type value: Variable
        """

        return self._weight_variable

    @weight_variable.setter
    def weight_variable(self, value: Variable) -> None:
        self._weight_variable = value

    @staticmethod
    def extended_pos_threshold(v: Variable, c: typing.Self) -> typing.Self:
        """
        Creates a new instance of `ExtThresholdConcept` representing an extended positive threshold. This static method takes a `Variable` and an existing `ExtThresholdConcept` as inputs to construct the new object. It returns the newly created concept configured with the type `EXT_POS_THRESHOLD`, combining the provided variable and the existing concept without modifying the original arguments.

        :param v: The variable representing the threshold value.
        :type v: Variable
        :param c: The concept instance to be wrapped by the extended positive threshold.
        :type c: typing.Self

        :return: An `ExtThresholdConcept` instance representing an extended positive threshold involving the provided variable and concept.

        :rtype: typing.Self
        """

        return ExtThresholdConcept(ConceptType.EXT_POS_THRESHOLD, c, v)

    @staticmethod
    def extended_neg_threshold(v: Variable, c: typing.Self) -> typing.Self:
        """
        Constructs a new instance representing an extended negative threshold concept by combining a variable with an existing concept. This static method acts as a factory that initializes an `ExtThresholdConcept` with the specific type identifier `EXT_NEG_THRESHOLD`, passing the provided concept and variable to the constructor. The operation does not modify the input arguments but rather creates a new object that encapsulates the logical relationship defined by the negative threshold.

        :param v: The variable component of the extended negative threshold concept.
        :type v: Variable
        :param c: The constant value defining the threshold boundary.
        :type c: typing.Self

        :return: Returns a new instance representing an extended negative threshold concept derived from the provided variable and concept.

        :rtype: typing.Self
        """

        return ExtThresholdConcept(ConceptType.EXT_NEG_THRESHOLD, c, v)

    def clone(self):
        """Generates a duplicate of the current object by creating a new instance of `ExtThresholdConcept` initialized with the existing `type`, `curr_concept`, and `weight_variable` attributes. This method ensures that the original object remains unmodified, effectively providing a snapshot of the object's state at the time of the call. Note that because the constructor receives direct references to the attributes, the resulting clone performs a shallow copy, meaning any mutable objects referenced by these attributes will be shared between the original and the new instance."""

        return ExtThresholdConcept(self.type, self.curr_concept, self.weight_variable)

    def replace(self, a: Concept, c: Concept) -> Concept:
        """
        Returns a new `ExtThresholdConcept` instance with all occurrences of concept `a` replaced by concept `c` within the underlying `curr_concept` structure. This method preserves the original instance's type and weight variable attributes while delegating the recursive substitution logic to the nested concept. The operation is side-effect free, ensuring the original object remains unmodified, and returns a distinct object reflecting the updated conceptual structure.

        :param a: The concept to be replaced within the current structure.
        :type a: Concept
        :param c: The concept to replace `a` with.
        :type c: Concept

        :return: A new `ExtThresholdConcept` instance where the underlying concept has been updated by replacing occurrences of `a` with `c`.

        :rtype: Concept
        """

        return ExtThresholdConcept(
            self.type, self.curr_concept.replace(a, c), self.weight_variable
        )

    def compute_name(self) -> typing.Optional[str]:
        """
        Generates a descriptive string representation for the threshold concept by formatting the weight variable and current concept into a conditional expression. The specific operator used in the expression depends on the concept type: a positive threshold results in a 'greater than or equal to' operator, while other types default to a 'less than or equal to' operator. This method performs no side effects and relies entirely on the existing attributes of the instance.

        :return: A formatted string representing the concept combined with a threshold condition on the weight variable.

        :rtype: typing.Optional[str]
        """

        if self.type == ConceptType.EXT_POS_THRESHOLD:
            return f"([>= {self.weight_variable}] {self.curr_concept})"
        else:
            return f"([<= {self.weight_variable}] {self.curr_concept})"

    def compute_atomic_concepts(self) -> set[Concept]:
        """
        Computes the set of atomic concepts associated with the current object by delegating the operation to the underlying `curr_concept` attribute. This method returns a collection of the fundamental, indivisible concepts that constitute the current state. As the logic is forwarded, the specific behavior, including potential side effects or exceptions, is determined by the implementation of `compute_atomic_concepts` within the referenced `curr_concept` object.

        :return: A set of atomic concepts that constitute the current concept.

        :rtype: set[Concept]
        """

        return self.curr_concept.compute_atomic_concepts()

    def get_roles(self) -> set[str]:
        """
        Retrieves the collection of roles associated with the current concept instance. This method acts as a delegation to the `get_roles` method of the internal `curr_concept` object, returning the resulting set of role identifiers. The operation has no side effects on the `ExtThresholdConcept` instance itself, though the behavior depends entirely on the state and implementation of the wrapped concept object.

        :return: A set of strings representing the roles associated with the current concept.

        :rtype: set[str]
        """

        return self.curr_concept.get_roles()

    def __neg__(self) -> Concept:
        """
        Returns the logical negation of the current concept instance, allowing the use of the unary minus operator (e.g., `-concept`). This method delegates the operation to `OperatorConcept.not_` to generate a new `Concept` representing the logical NOT of the original object without modifying it.

        :return: A new Concept representing the logical negation of this instance.

        :rtype: Concept
        """

        return OperatorConcept.not_(self)

    def __and__(self, value: typing.Self) -> typing.Self:
        """
        Implements the bitwise AND operation (`&`) for the `ExtThresholdConcept` class, enabling logical conjunction between two instances. This method accepts another instance of the same type and delegates the actual computation to the `OperatorConcept.and_` static method. The operation returns a new instance of `ExtThresholdConcept` representing the result of the conjunction.

        :param value: The right-hand operand of the AND operation.
        :type value: typing.Self

        :return: Returns a new instance representing the result of the logical AND operation between this object and the provided value.

        :rtype: typing.Self
        """

        return OperatorConcept.and_(self, value)

    def __or__(self, value: typing.Self) -> typing.Self:
        """
        Performs a logical OR operation between the current instance and another instance of the same type, typically invoked using the pipe operator (`|`). This method delegates the actual logic to `OperatorConcept.or_`, combining the two concepts to produce a new result. The operation is non-destructive, returning a new instance of `ExtThresholdConcept` rather than modifying the original operands. The `value` argument must be compatible with the current instance type to ensure the operation succeeds.

        :param value: The right-hand operand for the OR operation, expected to be of the same type as the current instance.
        :type value: typing.Self

        :return: A new instance representing the result of the OR operation between the current object and the provided value.

        :rtype: typing.Self
        """

        return OperatorConcept.or_(self, value)

    def __hash__(self) -> int:
        """
        Computes the hash value for the instance by delegating to the hash of its string representation. This allows the object to be used as a dictionary key or stored in a set. The resulting integer hash depends entirely on the output of the object's `__str__` method.

        :return: An integer hash value computed from the string representation of the object, intended for use in hashed collections.

        :rtype: int
        """

        return hash(str(self))


ExtendedPosThreshold = ExtThresholdConcept.extended_pos_threshold
ExtendedNegThreshold = ExtThresholdConcept.extended_neg_threshold
