from __future__ import annotations

import typing

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.concept.interface.has_weighted_concepts_interface import (
    HasWeightedConceptsInterface,
)
from fuzzy_dl_owl2.fuzzydl.concept.operator_concept import OperatorConcept
from fuzzy_dl_owl2.fuzzydl.util.constants import ConceptType
from fuzzy_dl_owl2.fuzzydl.util.util import Util


class OwaConcept(Concept, HasWeightedConceptsInterface):
    """
    This entity models an Ordered Weighted Averaging (OWA) concept, serving as a composite structure that aggregates a list of sub-concepts using a corresponding list of numerical weights. To utilize this class, instantiate it with two parallel lists: one of floating-point weights and another of `Concept` objects, ensuring they are of the same length to satisfy validation requirements. The class automatically generates a standardized string representation and supports operations such as cloning, retrieving atomic concepts and roles, and replacing specific nested components. By inheriting from `Concept` and `HasWeightedConceptsInterface`, it integrates seamlessly into a broader system of logical or semantic operators, allowing for weighted combinations of complex conceptual definitions.

    :param name: The canonical string representation of the OWA concept, automatically generated during initialization.
    :type name: typing.Any
    """


    def __init__(self, weights: list[float], concepts: list[Concept]) -> None:
        """
        Initializes a new instance representing an Ordered Weighted Averaging (OWA) concept by configuring the base `Concept` class with the OWA type and initializing the `HasWeightedConceptsInterface` with the provided weights and concepts. The method performs a validation check to ensure that the number of weights exactly matches the number of concepts; if these lists differ in length, an error is raised. Additionally, it triggers the computation of the concept's name based on the input parameters.

        :param weights: A list of numerical values representing the weight assigned to each concept. The number of weights must match the number of concepts provided.
        :type weights: list[float]
        :param concepts: A list of concepts to be associated with the weights. The length of this list must match the length of the weights list.
        :type concepts: list[Concept]
        """

        Concept.__init__(self, ConceptType.OWA)
        HasWeightedConceptsInterface.__init__(self, weights, concepts)

        if weights is not None:
            if len(weights) != len(concepts):
                Util.error(
                    "Error: The number of weights and the number of concepts should be the same"
                )
            self.name = self.compute_name()

    def clone(self) -> typing.Self:
        """
        Creates and returns a new instance of `OwaConcept` that serves as a shallow copy of the current object. The method constructs the clone by creating independent copies of the internal `weights` and `concepts` lists, ensuring that structural modifications to these lists in the clone do not affect the original instance. However, because the copy is shallow, the elements contained within the lists are shared by reference, meaning mutations to the actual concept objects or weight values will be reflected in both the original and the clone.

        :return: A new instance of the class with copies of the weights and concepts.

        :rtype: typing.Self
        """

        return OwaConcept(self.weights[:], [c for c in self.concepts])

    def compute_atomic_concepts(self) -> set[Concept]:
        """
        Computes and returns the set of atomic concepts represented by this entity by aggregating the atomic concepts of its immediate children. The method iterates through the collection of concepts stored in the `concepts` attribute, recursively invoking `compute_atomic_concepts` on each element and collecting the results into a unified set. Since the return value is a set, duplicate atomic concepts are automatically removed. If the instance contains no sub-concepts, an empty set is returned.

        :return: A set of all atomic concepts derived from the concepts contained in this object.

        :rtype: set[Concept]
        """

        concept_list: set[Concept] = set()
        for c in self.concepts:
            concept_list.update(c.compute_atomic_concepts())
        return concept_list

    def get_roles(self) -> set[str]:
        """
        Retrieves the union of roles associated with the underlying concepts contained within this instance. It iterates through the collection of concepts, aggregating the results of their individual role retrieval calls into a single set to ensure uniqueness. This method does not modify the internal state of the object or its sub-concepts, and it returns an empty set if no concepts are present.

        :return: A set of unique roles aggregated from all concepts.

        :rtype: set[str]
        """

        role_list: set[str] = set()
        for c in self.concepts:
            role_list.update(c.get_roles())
        return role_list

    def replace(self, a: Concept, c: Concept) -> typing.Optional[Concept]:
        """
        Returns a new instance of `OwaConcept` where every sub-concept within `self.concepts` has been transformed by recursively replacing occurrences of concept `a` with concept `c`. The method preserves the original weights of the current instance while constructing the new object, but applies a logical negation to the final result before returning it. This operation does not modify the original object in place, ensuring that side effects are avoided.

        :param a: The concept to be replaced.
        :type a: Concept
        :param c: The concept to replace `a` with.
        :type c: Concept

        :return: The negation of the concept resulting from replacing all occurrences of `a` with `c`.

        :rtype: typing.Optional[Concept]
        """

        return -OwaConcept(self.weights, [ci.replace(a, c) for ci in self.concepts])

    def compute_name(self) -> str:
        """
        Generates a string representation of the Ordered Weighted Averaging (OWA) concept by formatting the internal weights and concepts into a specific parenthesized syntax. The method joins the string representations of the weights and concepts with spaces, embedding them within a structure that follows the pattern `(owa (<weights>) (<concepts>))`. This output serves as a computed name or identifier for the concept based on its current state.

        :return: A string representation of the OWA operator formatted as '(owa (weights) (concepts))'.

        :rtype: str
        """

        return f"(owa ({' '.join(map(str, self.weights))}) ({' '.join(map(str, self.concepts))}))"

    def __neg__(self) -> Concept:
        """
        Implements the unary negation operator, enabling the use of the minus sign to represent the logical complement of the concept. This method returns a new `Concept` instance that corresponds to the logical NOT of the current object, effectively delegating the operation to `OperatorConcept.not_`. It does not modify the original instance in place but rather produces a new representation of the negated concept.

        :return: The logical negation of the current concept.

        :rtype: Concept
        """

        return OperatorConcept.not_(self)

    def __and__(self, value: typing.Self) -> typing.Self:
        """
        Implements the behavior of the bitwise AND operator (`&`) for the concept, allowing it to be combined with another instance of the same type. The operation delegates the actual computation to the `OperatorConcept.and_` method, which determines the specific logic for merging the two concepts. This method returns a new instance representing the combined result and does not modify the original objects in place.

        :param value: The right-hand operand of the bitwise AND operation.
        :type value: typing.Self

        :return: A new instance representing the result of the AND operation between the current instance and the provided value.

        :rtype: typing.Self
        """

        return OperatorConcept.and_(self, value)

    def __or__(self, value: typing.Self) -> typing.Self:
        """
        Implements the bitwise OR operation for the concept, enabling the use of the pipe operator (`|`) to combine two instances. This method delegates the logic to `OperatorConcept.or_`, passing the current instance and the provided value to perform the disjunction. It returns a new instance of the same type, representing the result of the operation without modifying the original operands.

        :param value: The right-hand operand to combine with the current instance using the OR operation.
        :type value: typing.Self

        :return: The result of the OR operation between the current instance and the provided value.

        :rtype: typing.Self
        """

        return OperatorConcept.or_(self, value)

    def __hash__(self) -> int:
        """
        Computes an integer hash value for the instance based on its string representation, enabling the object to be used as a key in dictionaries or as an element in sets. The implementation delegates to the built-in hash function applied to the result of the object's string conversion. It is critical that the string representation remains consistent throughout the object's lifetime; if the string output changes due to internal state mutation, the hash value will also change, potentially causing the object to become inaccessible or behave incorrectly within hash-based collections.

        :return: An integer hash value derived from the string representation of the object.

        :rtype: int
        """

        return hash(str(self))
