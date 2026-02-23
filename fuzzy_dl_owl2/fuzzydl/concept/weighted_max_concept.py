import typing

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.concept.interface.has_weighted_concepts_interface import (
    HasWeightedConceptsInterface,
)
from fuzzy_dl_owl2.fuzzydl.concept.operator_concept import OperatorConcept
from fuzzy_dl_owl2.fuzzydl.util.constants import ConceptType
from fuzzy_dl_owl2.fuzzydl.util.util import Util


class WeightedMaxConcept(Concept, HasWeightedConceptsInterface):
    """
    This class models a weighted maximum operation within a conceptual logic framework, defined by pairing a collection of sub-concepts with a corresponding list of numerical weights. It enforces strict validation during initialization, requiring that the number of weights exactly matches the number of concepts and that at least one weight is equal to 1.0 to ensure the operation is meaningful. Once instantiated, the object automatically generates a string representation of the structure and supports standard logical operations such as conjunction, disjunction, and negation through operator overloading. Furthermore, it provides utility methods for traversing the concept hierarchy, allowing users to retrieve atomic concepts and roles, clone the instance, or replace specific sub-concepts with alternatives.

    :param name: Automatically generated string representation of the concept in the format (w-max (C1 w1) (C2 w2) ...).
    :type name: typing.Any
    """


    def __init__(self, weights: list[float], concepts: list[Concept]) -> None:
        """
        Initializes a weighted maximum concept by associating a list of floating-point weights with a list of child concepts. The constructor validates that the input lists are of equal length and that at least one weight is exactly 1.0, raising an error if these conditions are not met. It initializes the base concept type and the weighted concepts interface before computing and assigning a generated name to the instance.

        :param weights: A list of numerical weights corresponding to the provided concepts. Must be the same length as the concepts list and contain at least one value equal to 1.0.
        :type weights: list[float]
        :param concepts: A list of concepts corresponding to the provided weights. The number of concepts must equal the number of weights.
        :type concepts: list[Concept]
        """

        Concept.__init__(self, ConceptType.W_MAX)
        HasWeightedConceptsInterface.__init__(self, weights, concepts)

        if len(weights) != len(concepts):
            Util.error(
                "Error: The number of weights and the number of concepts should be the same"
            )

        if not any(w == 1.0 for w in weights):
            Util.error(
                "Error: Some of the weights of the weighted max concept must be 1.0."
            )

        self.name = self.compute_name()

    def clone(self) -> typing.Self:
        """
        Returns a new instance of `WeightedMaxConcept` that is a shallow copy of the current object. The method constructs the clone using new list objects for the `weights` and `concepts` attributes, ensuring that modifications to the lists themselves in the clone do not affect the original instance. Note that because the copy is shallow, any mutable elements contained within these lists remain shared between the original and the clone.

        :return: A new instance of the class with copies of the weights and concepts.

        :rtype: typing.Self
        """

        return WeightedMaxConcept(self.weights[:], [c for c in self.concepts])

    def compute_atomic_concepts(self) -> set[Concept]:
        """
        Computes and returns the set of all atomic concepts contained within the weighted max concept by recursively resolving its internal collection of concepts. This method iterates over the sub-concepts, aggregates their individual atomic constituents into a unified set to ensure uniqueness, and returns the result. If the internal collection is empty or resolves to no atomic concepts, an empty set is returned, and the operation does not modify the state of the object or its sub-concepts.

        :return: A set of all atomic concepts derived from the concepts associated with this instance.

        :rtype: set[Concept]
        """

        concept_list: set[Concept] = set()
        for c in self.concepts:
            concept_list.update(c.compute_atomic_concepts())
        return concept_list

    def get_roles(self) -> set[str]:
        """
        Returns a set containing the unique roles associated with all concepts managed by this instance. This method aggregates the results of calling `get_roles` on each individual concept in the internal collection, effectively computing the union of their role sets. If the internal collection of concepts is empty, an empty set is returned. The operation does not modify the state of the instance or its contained concepts, though it relies on the behavior of the `get_roles` method of the individual concept objects.

        :return: A set of unique role names found across all associated concepts.

        :rtype: set[str]
        """

        role_list: set[str] = set()
        for c in self.concepts:
            role_list.update(c.get_roles())
        return role_list

    def replace(self, a: Concept, c: Concept) -> Concept:
        """
        Recursively replaces all occurrences of the concept `a` with the concept `c` within the collection of sub-concepts maintained by this instance. This operation creates a new `WeightedMaxConcept` object that preserves the original weights but incorporates the modified sub-concepts resulting from the recursive replacement. The final result is the negation of this newly constructed concept, meaning the method returns the additive inverse of the structure containing the replacements.

        :param a: The concept to be replaced by `c`.
        :type a: Concept
        :param c: The concept to substitute in place of `a`.
        :type c: Concept

        :return: A new Concept resulting from replacing occurrences of `a` with `c` in the internal concepts, preserving weights and negating the resulting weighted maximum.

        :rtype: Concept
        """

        return -WeightedMaxConcept(
            self.weights, [ci.replace(a, c) for ci in self.concepts]
        )

    def compute_name(self) -> str:
        """
        Generates a string representation of the weighted maximum concept by formatting the internal concepts and their corresponding weights into a specific parenthetical syntax. The output string is constructed by iterating over the paired concepts and weights, enclosing each pair in parentheses, joining them with spaces, and prefixing the result with "(w-max ...)". If the lists of concepts and weights are of unequal lengths, elements from the longer list are ignored due to the behavior of the `zip` function. This method does not modify the object's state and returns a newly constructed string.

        :return: A formatted string representing the weighted maximization of the concepts and their associated weights.

        :rtype: str
        """

        return f"(w-max {' '.join([f'({concept} {weight})' for concept, weight in zip(self.concepts, self.weights)])})"

    def __neg__(self) -> Concept:
        """
        Returns the logical negation of the current concept, corresponding to the behavior of the unary minus operator. This operation creates and returns a new `Concept` instance by delegating to `OperatorConcept.not_`, leaving the original `WeightedMaxConcept` instance unchanged.

        :return: The logical negation of the current concept.

        :rtype: Concept
        """

        return OperatorConcept.not_(self)

    def __and__(self, value: typing.Self) -> typing.Self:
        """
        Implements the bitwise AND operator (`&`) to perform a logical conjunction or intersection between the current instance and another `WeightedMaxConcept`. The operation delegates the calculation to `OperatorConcept.and_`, returning a new instance that represents the combined result without altering the original objects.

        :param value: The right-hand operand for the AND operation.
        :type value: typing.Self

        :return: An instance representing the result of the 'and' operation between this instance and the provided value.

        :rtype: typing.Self
        """

        return OperatorConcept.and_(self, value)

    def __or__(self, value: typing.Self) -> typing.Self:
        """
        Implements the bitwise OR operation (`|`) for the concept, allowing the current instance to be combined with another `WeightedMaxConcept` object. This method delegates the actual computation to `OperatorConcept.or_`, which defines the specific semantics of the disjunction operation within the module's algebraic framework. The operation returns a new instance of the same type representing the result of the combination, leaving the original operands unmodified.

        :param value: The right-hand operand to combine with the current instance using the OR operation.
        :type value: typing.Self

        :return: The result of the OR operation between this instance and the provided value.

        :rtype: typing.Self
        """

        return OperatorConcept.or_(self, value)

    def __hash__(self) -> int:
        """
        Returns the integer hash value for the instance, enabling its use as a dictionary key or set element. The hash is derived from the string representation of the object, meaning that any changes to the output of the `__str__` method will alter the hash value. Consequently, the object should be treated as immutable if used in hash-based collections, as modifying the state that affects the string representation would result in a different hash and break lookup invariants.

        :return: An integer hash value derived from the string representation of the object.

        :rtype: int
        """

        return hash(str(self))
