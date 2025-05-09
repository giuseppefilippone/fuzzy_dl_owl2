import typing

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.concept.interface.has_weighted_concepts_interface import (
    HasWeightedConceptsInterface,
)
from fuzzy_dl_owl2.fuzzydl.concept.operator_concept import OperatorConcept
from fuzzy_dl_owl2.fuzzydl.util.constants import ConceptType
from fuzzy_dl_owl2.fuzzydl.util.util import Util


class WeightedMaxConcept(Concept, HasWeightedConceptsInterface):

    def __init__(self, weights: list[float], concepts: list[Concept]) -> None:
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
        return WeightedMaxConcept(self.weights[:], [c for c in self.concepts])

    def compute_atomic_concepts(self) -> set[Concept]:
        concept_list: set[Concept] = set()
        for c in self.concepts:
            concept_list.update(c.compute_atomic_concepts())
        return concept_list

    def get_roles(self) -> set[str]:
        role_list: set[str] = set()
        for c in self.concepts:
            role_list.update(c.get_roles())
        return role_list

    def replace(self, a: Concept, c: Concept) -> Concept:
        return -WeightedMaxConcept(
            self.weights, [ci.replace(a, c) for ci in self.concepts]
        )

    def compute_name(self) -> str:
        return f"(w-max {' '.join([f'({concept} {weight})' for concept, weight in zip(self.concepts, self.weights)])})"

    def __neg__(self) -> Concept:
        return OperatorConcept.not_(self)

    def __and__(self, value: typing.Self) -> typing.Self:
        return OperatorConcept.and_(self, value)

    def __or__(self, value: typing.Self) -> typing.Self:
        return OperatorConcept.or_(self, value)

    def __hash__(self) -> int:
        return hash(str(self))
