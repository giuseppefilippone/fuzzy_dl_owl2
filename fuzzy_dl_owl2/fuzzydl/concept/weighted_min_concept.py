import typing

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.concept.interface.has_weighted_concepts_interface import (
    HasWeightedConceptsInterface,
)
from fuzzy_dl_owl2.fuzzydl.concept.operator_concept import OperatorConcept
from fuzzy_dl_owl2.fuzzydl.util.constants import ConceptType
from fuzzy_dl_owl2.fuzzydl.util.util import Util


class WeightedMinConcept(Concept, HasWeightedConceptsInterface):
    """
    This class models a composite concept defined by a weighted minimum operation over a collection of sub-concepts, typically used in fuzzy or description logic contexts. It is constructed by providing parallel lists of concepts and their associated floating-point weights, with the strict requirement that at least one weight must be equal to 1.0 to maintain semantic meaning. Once initialized, the object automatically generates a string representation and supports various structural manipulations, including cloning, replacing specific sub-concepts, and performing logical operations such as negation, conjunction, and disjunction.

    :param name: Computed string representation of the weighted minimum concept, automatically generated during initialization.
    :type name: typing.Any
    """


    def __init__(self, weights: list[float], concepts: list[Concept]) -> None:
        """
        Initializes a new instance of the WeightedMinConcept class using the provided lists of weights and concepts. This constructor configures the instance as a weighted minimum concept by invoking the initializers of the `Concept` and `HasWeightedConceptsInterface` base classes. It performs validation to ensure that the number of weights corresponds exactly to the number of concepts and that the list of weights contains at least one value equal to 1.0; failure to meet these conditions results in an error. Additionally, the method automatically computes and sets the instance's name attribute based on the input data.

        :param weights: List of numerical weights corresponding to the provided concepts. Must match the length of the concepts list and contain at least one value equal to 1.0.
        :type weights: list[float]
        :param concepts: A list of Concept objects corresponding to the provided weights. The length of this list must match the length of the weights list.
        :type concepts: list[Concept]
        """

        Concept.__init__(self, ConceptType.W_MIN)
        HasWeightedConceptsInterface.__init__(self, weights, concepts)

        if len(weights) != len(concepts):
            Util.error("Error: The number of weights and concepts should be the same")
        if 1.0 not in weights:
            Util.error("Error: Some weights must be 1.0")

        self.name = self.compute_name()

    def clone(self) -> typing.Self:
        """
        Returns a new `WeightedMinConcept` instance that is a shallow copy of the current object. This method creates independent copies of the internal `weights` and `concepts` lists, ensuring that modifications to the list structures in the clone do not affect the original instance. However, because the copy is shallow, any mutable objects contained within these lists remain shared references between the original and the clone.

        :return: A new instance of the class that is a copy of the current object, containing independent copies of the internal weights and concepts lists.

        :rtype: typing.Self
        """

        return WeightedMinConcept(self.weights[:], [c for c in self.concepts])

    def compute_atomic_concepts(self) -> set[Concept]:
        """
        Computes and returns the set of atomic concepts that constitute this weighted minimum concept. The method iterates over the internal collection of concepts, recursively retrieving the atomic concepts from each child and aggregating them into a single set to ensure uniqueness. This process effectively flattens the composite structure to its most fundamental components.

        :return: A set of all atomic concepts derived from the concepts contained within this object.

        :rtype: set[Concept]
        """

        concept_list: set[Concept] = set()
        for c in self.concepts:
            concept_list.update(c.compute_atomic_concepts())
        return concept_list

    def get_roles(self) -> set[str]:
        """
        Aggregates and returns a set of role strings derived from all underlying concepts managed by this instance. This method iterates through the internal collection of concepts, invoking `get_roles` on each element and merging the results into a single set to ensure uniqueness. If the instance contains no concepts, an empty set is returned.

        :return: A set of unique roles aggregated from all concepts.

        :rtype: set[str]
        """

        role_list: set[str] = set()
        for c in self.concepts:
            role_list.update(c.get_roles())
        return role_list

    def replace(self, a: Concept, c: Concept) -> Concept:
        """
        Returns the negation of a new `WeightedMinConcept` where every sub-concept has been transformed by replacing instances of concept `a` with concept `c`. The replacement is applied recursively to the nested concepts, and the original weights are retained in the new instance. This method does not modify the current object in place.

        :param a: The concept to be replaced.
        :type a: Concept
        :param c: The concept to replace `a` with.
        :type c: Concept

        :return: A new Concept resulting from the substitution of every occurrence of concept `a` with concept `c`.

        :rtype: Concept
        """

        return -WeightedMinConcept(
            self.weights, [ci.replace(a, c) for ci in self.concepts]
        )

    def compute_name(self) -> str:
        """
        Generates a string representation of the weighted minimum concept by formatting the internal concepts and their associated weights. The method iterates over the paired concepts and weights, creating a space-separated list of parenthesized values, and wraps this list within a '(w-min ...)' prefix. This provides a descriptive identifier that reflects the specific configuration of the concept without modifying the object's state.

        :return: Returns a string representing the weighted minimum configuration, formatted as '(w-min (concept weight) ...)'.

        :rtype: str
        """

        return f"(w-min {' '.join([f'({concept} {weight})' for concept, weight in zip(self.concepts, self.weights)])})"

    def __neg__(self) -> Concept:
        """
        Implements the unary negation operator to return the logical complement of the current concept. This method delegates the creation of the negated concept to `OperatorConcept.not_`, resulting in a new `Concept` instance that represents the inverse of the original. The operation is non-destructive, leaving the original instance unmodified while producing a distinct object representing the negated state.

        :return: A new Concept representing the logical negation of the current concept.

        :rtype: Concept
        """

        return OperatorConcept.not_(self)

    def __and__(self, value: typing.Self) -> typing.Self:
        """
        Performs a logical conjunction operation between the current instance and another instance of the same type, typically invoked via the `&` operator. This method delegates the core logic to the `and_` class method within `OperatorConcept`, ensuring that the combination follows the specific rules defined for the concept hierarchy. The operation returns a new instance representing the result of the conjunction, leaving the original operands unmodified.

        :param value: The right-hand operand for the AND operation, which must be an instance of the same class.
        :type value: typing.Self

        :return: The result of the AND operation between this object and the provided value.

        :rtype: typing.Self
        """

        return OperatorConcept.and_(self, value)

    def __or__(self, value: typing.Self) -> typing.Self:
        """
        Implements the bitwise OR operator (`|`) to perform a logical disjunction between the current instance and another `WeightedMinConcept` object. This method delegates the underlying logic to the `OperatorConcept.or_` static method, which handles the specific combination rules for the concepts. The operation returns a new instance representing the result of the union, ensuring that the original operands remain unchanged.

        :param value: The right-hand operand for the OR operation.
        :type value: typing.Self

        :return: Returns the result of the OR operation between the current instance and the provided value.

        :rtype: typing.Self
        """

        return OperatorConcept.or_(self, value)

    def __hash__(self) -> int:
        """
        Computes the hash value for the instance by hashing its string representation, enabling the object to be used in hash-based collections such as dictionaries and sets. This implementation relies on the `__str__` method to generate a unique identifier for the object, ensuring that instances with identical string representations produce the same hash code. It assumes that the string representation is stable and consistent with the object's equality comparison.

        :return: An integer hash value computed from the string representation of the object.

        :rtype: int
        """

        return hash(str(self))
