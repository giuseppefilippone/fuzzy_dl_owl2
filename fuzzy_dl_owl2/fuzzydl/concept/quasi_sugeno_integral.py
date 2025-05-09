from __future__ import annotations

import typing

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.concept.operator_concept import OperatorConcept
from fuzzy_dl_owl2.fuzzydl.concept.sugeno_integral import SugenoIntegral
from fuzzy_dl_owl2.fuzzydl.util.constants import ConceptType
from fuzzy_dl_owl2.fuzzydl.util.util import Util


class QsugenoIntegral(SugenoIntegral):

    def __init__(self, weights: list[float], concepts: list[Concept]) -> None:
        super().__init__(weights, concepts)
        self.type = ConceptType.QUASI_SUGENO_INTEGRAL

        if weights is not None:
            if len(weights) != len(concepts):
                Util.error(
                    "Error: The number of weights and the number of concepts should be the same"
                )
            self.name = self.compute_name()

    def clone(self) -> typing.Self:
        return QsugenoIntegral(self.weights[:], [c for c in self.concepts])

    def replace(self, a: Concept, c: Concept) -> Concept:
        return -QsugenoIntegral(
            self.weights, [ci.replace(a, c) for ci in self.concepts]
        )

    def compute_name(self) -> str:
        return f"(qsugeno ({' '.join(map(str, self.weights))}) ({' '.join(map(str, self.concepts))}))"

    def __neg__(self) -> Concept:
        return OperatorConcept.not_(self)

    def __and__(self, value: typing.Self) -> typing.Self:
        return OperatorConcept.and_(self, value)

    def __or__(self, value: typing.Self) -> typing.Self:
        return OperatorConcept.or_(self, value)

    def __hash__(self) -> int:
        return hash(str(self))
