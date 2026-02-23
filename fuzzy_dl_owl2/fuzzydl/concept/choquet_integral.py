from __future__ import annotations

import typing

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.concept.interface.has_weighted_concepts_interface import (
    HasWeightedConceptsInterface,
)
from fuzzy_dl_owl2.fuzzydl.concept.operator_concept import OperatorConcept
from fuzzy_dl_owl2.fuzzydl.util.constants import ConceptType
from fuzzy_dl_owl2.fuzzydl.util.util import Util


class ChoquetIntegral(Concept, HasWeightedConceptsInterface):
    """
    This class models a complex concept defined by the aggregation of sub-concepts using a Choquet integral mechanism. It serves as a container that pairs a list of floating-point weights with a corresponding list of `Concept` objects, requiring that both lists be of equal length during instantiation. Users can interact with this object to perform logical operations such as conjunction, disjunction, and negation, or to traverse the concept hierarchy to retrieve atomic concepts and roles. Additionally, the class provides functionality to clone the structure or replace specific internal concepts within the aggregation.

    :param name: The string representation of the concept, formatted as a Choquet integral containing its weights and sub-concepts.
    :type name: str
    :param weights: A list of numerical values representing the importance or contribution of each associated concept in the integral.
    :type weights: typing.Any
    """


    def __init__(self, weights: list[float], concepts: list[Concept]) -> None:
        """
        Initializes a Choquet Integral concept, registering it as a specific type within the Concept hierarchy and configuring the weighted concepts interface. This constructor accepts a list of numerical weights and a corresponding list of Concept objects, ensuring that the number of weights exactly matches the number of concepts; a mismatch triggers an error. The instance's name is automatically assigned based on its string representation. If the weights argument is provided as None, the weights attribute is reset to an empty list.

        :param weights: A list of numerical values representing the weights for the concepts. The number of weights must match the number of concepts provided.
        :type weights: list[float]
        :param concepts: A list of concepts to be associated with the provided weights. The number of concepts must match the number of weights.
        :type concepts: list[Concept]
        """

        Concept.__init__(self, ConceptType.CHOQUET_INTEGRAL)
        HasWeightedConceptsInterface.__init__(self, weights, concepts)

        if weights is not None:
            if len(weights) != len(concepts):
                Util.error(
                    "Error: The number of weights and the number of concepts should be the same"
                )
            self.name: str = str(self)
        else:
            self.weights = list()

    def clone(self) -> typing.Self:
        """
        Creates and returns a new instance of the ChoquetIntegral that is a copy of the current object. The method performs a shallow copy of the internal `weights` and `concepts` lists, ensuring that the new object contains independent list containers. This allows the clone to be modified without affecting the original object's list structures, although changes to mutable elements within those lists will be reflected in both instances.

        :return: A new instance of the class that is a copy of the current object, containing copies of the weights and concepts.

        :rtype: typing.Self
        """

        return ChoquetIntegral(self.weights[:], [c for c in self.concepts])

    def compute_atomic_concepts(self) -> set[Concept]:
        """
        Aggregates the atomic concepts derived from the constituent concepts within the Choquet Integral by iterating through the collection stored in the instance. For each concept, it delegates the computation to the concept's own `compute_atomic_concepts` method and collects the results into a unified set, ensuring that duplicate atomic concepts are removed. This method operates as a read-only aggregation, returning an empty set if the instance contains no constituent concepts.

        :return: A set of all atomic concepts derived from the object's concepts.

        :rtype: set[Concept]
        """

        concept_list = set()
        for c in self.concepts:
            concept_list.update(c.compute_atomic_concepts())
        return concept_list

    def get_roles(self) -> set[str]:
        """
        Retrieves the union of roles defined across all concepts associated with this ChoquetIntegral instance. It iterates over the internal collection of concepts, aggregating the results of their individual `get_roles` methods into a single set to ensure uniqueness. The method returns an empty set if no concepts are present or if none define roles, and it does not modify the state of the instance or its concepts.

        :return: A set of unique role names aggregated from all concepts.

        :rtype: set[str]
        """

        role_list = set()
        for c in self.concepts:
            role_list.update(c.get_roles())
        return role_list

    def replace(self, a: Concept, c: Concept) -> Concept:
        """
        Recursively replaces all occurrences of the concept `a` with the concept `c` within the list of concepts held by this integral. A new Choquet integral is instantiated using the original weights and the modified list of concepts, ensuring that the original object remains unmodified. The method returns the arithmetic negation of this newly constructed integral.

        :param a: The concept to be replaced by `c`.
        :type a: Concept
        :param c: The concept to substitute for 'a' in the underlying concepts.
        :type c: Concept

        :return: A new Concept representing the negation of a Choquet Integral constructed by replacing every occurrence of concept `a` with concept `c` in the original integral's sub-concepts.

        :rtype: Concept
        """

        return -ChoquetIntegral(
            self.weights, [ci.replace(a, c) for ci in self.concepts]
        )

    def compute_name(self) -> str:
        """
        Generates a formatted string representation of the Choquet integral instance, intended for identification or display purposes. The method constructs the output by joining the string values of the instance's concepts and, if present, its weights, separating them with spaces. If the weights attribute is None, the weights section of the resulting string is left empty. The final string follows the specific syntax "(choquet (weights) (concepts))", encapsulating the integral's configuration within a parenthetical structure.

        :return: A string representation of the Choquet model, formatted to include the weights and concepts.

        :rtype: str
        """

        str_weights: str = ""
        if self.weights is not None:
            str_weights = " ".join(list(str, self.weights))
        str_concepts: str = " ".join(list(str, self.concepts))
        name = f"(choquet ({str_weights}) ({str_concepts}))"
        return name

    def __neg__(self) -> Concept:
        """
        Implements the unary negation operator for the Choquet integral, enabling the use of the minus sign (`-`) to represent logical negation. This method returns a new `Concept` object that encapsulates the complement of the current integral, effectively delegating the creation of this negated representation to `OperatorConcept.not_`. The operation does not modify the original instance in place but instead produces a distinct object representing the negated state.

        :return: The logical negation of the current concept.

        :rtype: Concept
        """

        return OperatorConcept.not_(self)

    def __and__(self, value: typing.Self) -> typing.Self:
        """
        Computes the logical conjunction of the current instance with another `ChoquetIntegral` by utilizing the bitwise AND operator (`&`). This method delegates the specific combination logic to the `OperatorConcept.and_` static method, abstracting the implementation details of the operation. The result is a new `ChoquetIntegral` object representing the intersection or logical combination of the two inputs, without modifying the original instances.

        :param value: The other operand to perform the AND operation with.
        :type value: typing.Self

        :return: The result of the logical AND operation between this instance and the provided value.

        :rtype: typing.Self
        """

        return OperatorConcept.and_(self, value)

    def __or__(self, value: typing.Self) -> typing.Self:
        """
        Implements the logical disjunction (OR) operation for the `ChoquetIntegral` class, enabling the use of the pipe operator (`|`) to combine instances. It accepts another instance of the same type and returns a new `ChoquetIntegral` representing the result of the disjunction, leaving the original operands unchanged. The specific logic for the operation is delegated to the `OperatorConcept.or_` method.

        :param value: Another instance of the same class to combine with the current instance using the OR operation.
        :type value: typing.Self

        :return: A new instance representing the logical OR of the current object and the provided value.

        :rtype: typing.Self
        """

        return OperatorConcept.or_(self, value)

    def __hash__(self) -> int:
        """
        Computes the hash value for the instance, allowing it to be used as a key in dictionaries or as an element in sets. The hash is generated by converting the object to its string representation and hashing the resulting string. Consequently, the hash value is dependent on the implementation of the `__str__` method, and any mutation of the object that alters its string representation will result in a different hash, potentially causing issues if the object is used as a dictionary key after modification.

        :return: An integer hash value derived from the string representation of the object.

        :rtype: int
        """

        return hash(str(self))
