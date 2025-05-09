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
    def __init__(self, weights: list[float], concepts: list[Concept]) -> None:
        Concept.__init__(self, ConceptType.CHOQUET_INTEGRAL)
        HasWeightedConceptsInterface.__init__(self, weights, concepts)

        if weights is not None:
            if len(weights) != len(concepts):
                Util.error(
                    "Error: The number of weights and the number of concepts should be the same"
                )
            self.name: str = str(self)

    def clone(self) -> typing.Self:
        return ChoquetIntegral(self.weights[:], [c for c in self.concepts])

    def compute_atomic_concepts(self) -> set[Concept]:
        concept_list = set()
        for c in self.concepts:
            concept_list.update(c.compute_atomic_concepts())
        return concept_list

    def get_roles(self) -> set[str]:
        role_list = set()
        for c in self.concepts:
            role_list.update(c.get_roles())
        return role_list

    def replace(self, a: Concept, c: Concept) -> Concept:
        return -ChoquetIntegral(
            self.weights, [ci.replace(a, c) for ci in self.concepts]
        )

    def compute_name(self) -> str:
        str_weights: str = ""
        if self.weights is not None:
            str_weights = " ".join(list(str, self.weights))
        str_concepts: str = " ".join(list(str, self.concepts))
        name = f"(choquet ({str_weights}) ({str_concepts}))"
        return name

    def __neg__(self) -> Concept:
        return OperatorConcept.not_(self)

    def __and__(self, value: typing.Self) -> typing.Self:
        return OperatorConcept.and_(self, value)

    def __or__(self, value: typing.Self) -> typing.Self:
        return OperatorConcept.or_(self, value)

    def __hash__(self) -> int:
        return hash(str(self))
