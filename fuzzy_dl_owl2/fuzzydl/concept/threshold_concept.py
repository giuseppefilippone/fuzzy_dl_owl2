import typing

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.concept.interface.has_concept_interface import (
    HasConceptInterface,
)
from fuzzy_dl_owl2.fuzzydl.concept.operator_concept import OperatorConcept
from fuzzy_dl_owl2.fuzzydl.util.constants import ConceptType


class ThresholdConcept(Concept, HasConceptInterface):
    """
    This class models a threshold constraint applied to a base concept within a graded or fuzzy logic framework, determining satisfaction based on a numerical boundary. It evaluates whether the degree of fulfillment of a nested concept meets a specific weight, supporting both positive thresholds (greater than or equal to) and negative thresholds (less than or equal to). Users can construct instances via the standard constructor or convenient static factory methods designed for specific threshold directions. Functionally, it integrates into a larger hierarchy of logical constructs, enabling standard operations such as conjunction, disjunction, and negation, while delegating the retrieval of atomic concepts and roles to the encapsulated inner concept.

    :param _weight: Numeric threshold value used to compare against the satisfaction degree of the nested concept.
    :type _weight: float
    :param name: The computed string representation of the threshold concept, formatted as `([>= w] C)` or `([<= w] C)` and generated automatically upon initialization.
    :type name: typing.Any
    """


    def __init__(self, c_type: ConceptType, c: Concept, weight: float) -> None:
        """
        Initializes a threshold concept entity by configuring its type, the underlying concept it references, and a specific weight value. This method enforces a strict constraint on the concept type, requiring it to be either a positive or negative threshold; otherwise, an assertion error is raised. During initialization, it sets up the base `Concept` and `HasConceptInterface` components, stores the provided weight, and automatically computes the instance's name based on these parameters.

        :param c_type: The type of the concept, restricted to either a positive or negative threshold.
        :type c_type: ConceptType
        :param c: The concept object to associate with this instance.
        :type c: Concept
        :param weight: The numerical value defining the threshold's magnitude.
        :type weight: float
        """

        Concept.__init__(self, c_type)
        HasConceptInterface.__init__(self, c)

        assert c_type in (
            ConceptType.POS_THRESHOLD,
            ConceptType.NEG_THRESHOLD,
        )

        self._weight: float = weight
        self.name = self.compute_name()

    @property
    def weight(self) -> float:
        """
        Sets the weight of the `ThresholdConcept` instance to the specified floating-point value. This method updates the internal `_weight` attribute, effectively modifying the object's state without performing additional validation or triggering side effects beyond the assignment. It allows the weight to be redefined dynamically, accepting any float provided as an argument.

        :param value: The new weight value.
        :type value: float
        """

        return self._weight

    @weight.setter
    def weight(self, value: float) -> None:
        self._weight = value

    @staticmethod
    def pos_threshold(w: float, c: typing.Self) -> typing.Self:
        """
        Constructs a new `ThresholdConcept` instance representing a positive threshold condition. This static method acts as a factory, accepting a floating-point weight and an existing concept instance to wrap. It initializes the new object with the `POS_THRESHOLD` type, associating the provided weight and concept with the resulting entity without modifying the original inputs.

        :param w: The numerical value defining the threshold.
        :type w: float
        :param c: The concept to which the positive threshold is applied.
        :type c: typing.Self

        :return: A new instance representing a positive threshold concept, configured with the provided weight and concept.

        :rtype: typing.Self
        """

        return ThresholdConcept(ConceptType.POS_THRESHOLD, c, w)

    @staticmethod
    def neg_threshold(w: float, c: typing.Self) -> typing.Self:
        """
        This static method serves as a factory to instantiate a `ThresholdConcept` specifically defined as a negative threshold. It accepts a weight `w` and a concept `c`, passing them to the constructor along with the `NEG_THRESHOLD` type identifier. The method has no side effects and simply returns a new instance; any validation or errors raised will depend on the underlying `ThresholdConcept` constructor logic.

        :param w: The weight or value defining the negative threshold.
        :type w: float
        :param c: The concept to which the negative threshold is applied.
        :type c: typing.Self

        :return: A new ThresholdConcept instance representing a negative threshold with the specified weight and concept.

        :rtype: typing.Self
        """

        return ThresholdConcept(ConceptType.NEG_THRESHOLD, c, w)

    def clone(self) -> typing.Self:
        """
        Creates and returns a new instance of `ThresholdConcept` that duplicates the state of the current object. The returned object is initialized with the same `type`, `curr_concept`, and `weight` attributes as the original. This method ensures that the returned instance is independent of the source, meaning modifications to the clone will not affect the original object, although it performs a shallow copy of the internal attributes.

        :return: A new instance of the class initialized with the same attributes as the current object.

        :rtype: typing.Self
        """

        return ThresholdConcept(self.type, self.curr_concept, self.weight)

    def replace(self, a: Concept, c: Concept) -> Concept:
        """
        Recursively replaces concept `a` with concept `c` within the nested `curr_concept` and transforms the current node into a new `ThresholdConcept` based on the type of `c`. If the replacement concept `c` is a positive threshold, the method returns a positive threshold concept; if it is a negative threshold, it returns a negative threshold concept. The original weight of the current node is preserved in the returned instance, ensuring that the structural hierarchy is maintained while the substitution is applied to the underlying concept.

        :param a: The target to be replaced by `c`.
        :type a: Concept
        :param c: The concept to replace `a` with.
        :type c: Concept

        :return: A new `Concept` instance resulting from replacing the sub-concept `a` with `c` within the current structure, preserving the current weight.

        :rtype: Concept
        """

        c_type: ConceptType = c.type
        if c_type == ConceptType.POS_THRESHOLD:
            return ThresholdConcept.pos_threshold(
                self.weight, self.curr_concept.replace(a, c)
            )
        elif c_type == ConceptType.NEG_THRESHOLD:
            return ThresholdConcept.neg_threshold(
                self.weight, self.curr_concept.replace(a, c)
            )

    def compute_name(self) -> typing.Optional[str]:
        """
        Generates a formatted string representation of the threshold condition based on the concept's type and weight. For positive thresholds, the output indicates a greater-than-or-equal-to relationship, while negative thresholds indicate a less-than-or-equal-to relationship, embedding the underlying concept name within the result. If the concept type does not correspond to a defined threshold category, the method returns None.

        :return: A formatted string representing the concept with its threshold condition and weight for positive or negative threshold types, or None if the type is not a threshold.

        :rtype: typing.Optional[str]
        """

        if self.type == ConceptType.POS_THRESHOLD:
            return f"([>= {self.weight}] {self.curr_concept})"
        elif self.type == ConceptType.NEG_THRESHOLD:
            return f"([<= {self.weight}] {self.curr_concept})"

    def compute_atomic_concepts(self) -> set[Concept]:
        """
        Computes the set of atomic concepts that constitute the underlying concept stored in `curr_concept`. This method acts as a delegation wrapper, forwarding the call to the `compute_atomic_concepts` method of the `curr_concept` attribute to retrieve the fundamental, indivisible components of the concept. The result is returned as a set of `Concept` objects, ensuring uniqueness among the atomic constituents.

        :return: A set of the atomic concepts that constitute the current concept.

        :rtype: set[Concept]
        """

        return self.curr_concept.compute_atomic_concepts()

    def get_roles(self) -> set[str]:
        """
        Retrieves the set of role identifiers associated with the underlying concept currently referenced by the instance. This method delegates the operation to the `get_roles` method of the internal `curr_concept` object, returning the resulting set of strings directly. Because the return value is a set, callers should be aware that modifying the returned collection may inadvertently alter the state of the underlying concept if the delegated method returns a direct reference to internal data.

        :return: A set of strings representing the roles associated with the current concept.

        :rtype: set[str]
        """

        return self.curr_concept.get_roles()

    def __neg__(self) -> Concept:
        """
        Implements the unary negation operator for the concept, enabling the use of the minus sign to invert its logical state. This method returns a new `Concept` instance representing the logical negation of the current `ThresholdConcept` by delegating to the `OperatorConcept.not_` method. The operation is non-destructive, leaving the original concept unchanged while producing a derived expression that signifies the opposite condition.

        :return: The logical negation of the concept.

        :rtype: Concept
        """

        return OperatorConcept.not_(self)

    def __and__(self, value: typing.Self) -> typing.Self:
        """
        Performs a logical conjunction between the current instance and another value of the same type using the bitwise AND operator. This operation delegates the underlying logic to `OperatorConcept.and_`, returning a new instance that represents the combination of the two concepts without modifying the original operands. The method is designed to work with compatible types, ensuring that the resulting object adheres to the same conceptual constraints as the inputs.

        :param value: The right-hand operand for the AND operation, which must be an instance of the same type.
        :type value: typing.Self

        :return: The result of the conjunction (AND operation) between this instance and the provided value.

        :rtype: typing.Self
        """

        return OperatorConcept.and_(self, value)

    def __or__(self, value: typing.Self) -> typing.Self:
        """
        Performs a logical OR operation between the current concept and another concept, enabling the use of the pipe operator (`|`) to combine them. This method delegates the combination logic to `OperatorConcept.or_`, returning a new composite concept that represents the union of the two operands. The operation is side-effect free, as it does not modify the original instances but produces a new instance of the same type.

        :param value: The right-hand operand to combine with the current instance using the OR operation.
        :type value: typing.Self

        :return: A new instance representing the result of the OR operation between the current instance and the provided value.

        :rtype: typing.Self
        """

        return OperatorConcept.or_(self, value)

    def __hash__(self) -> int:
        """
        Computes the hash value for the instance by hashing its string representation, enabling the object to be used as a key in dictionaries or as a member of sets. The implementation delegates to the built-in hash function applied to the result of `str(self)`. Note that if the object is mutable and its string representation changes over time, the hash value will also change, which can lead to unexpected behavior if the object is modified while stored in a hash-based collection.

        :return: An integer hash value computed from the string representation of the object.

        :rtype: int
        """

        return hash(str(self))


PosThreshold = ThresholdConcept.pos_threshold
NegThreshold = ThresholdConcept.neg_threshold
