import typing

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_concrete_concept import (
    FuzzyConcreteConcept,
)
from fuzzy_dl_owl2.fuzzydl.concept.operator_concept import OperatorConcept
from fuzzy_dl_owl2.fuzzydl.concept.owa_concept import OwaConcept
from fuzzy_dl_owl2.fuzzydl.util.constants import ConceptType


class QowaConcept(OwaConcept):
    def __init__(
        self, quantifier: FuzzyConcreteConcept, concepts: list[Concept]
    ) -> None:
        super().__init__(None, concepts)

        self.type = ConceptType.QUANTIFIED_OWA
        self._quantifier: FuzzyConcreteConcept = quantifier
        self.compute_weights(len(concepts))
        self.name = self.compute_name()

    @property
    def quantifier(self) -> FuzzyConcreteConcept:
        return self._quantifier

    @quantifier.setter
    def quantifier(self, value: FuzzyConcreteConcept) -> None:
        self._quantifier = value
        self.name = self.compute_name()

    def clone(self) -> typing.Self:
        return QowaConcept(self.quantifier, [c for c in self.concepts])

    def compute_weights(self, n: int) -> None:
        if n <= 0:
            return
        if self.weights is None:
            self.weights = []
        previous: float = 0.0
        for i in range(1, n + 1):
            w: float = i / n
            self.weights.append(self.quantifier.get_membership_degree(w - previous))
            previous: float = w

    def replace(self, a: Concept, c: Concept) -> typing.Optional[Concept]:
        return -OwaConcept(self.quantifier, [ci.replace(a, c) for ci in self.concepts])

    def compute_name(self) -> str:
        return f"(q-owa {self.quantifier} {' '.join(map(str, self.concepts))})"

    def __neg__(self) -> Concept:
        return OperatorConcept.not_(OwaConcept(self.weights, self.concepts))

    def __and__(self, value: typing.Self) -> typing.Self:
        return OperatorConcept.and_(self, value)

    def __or__(self, value: typing.Self) -> typing.Self:
        return OperatorConcept.or_(self, value)

    def __hash__(self) -> int:
        return hash(str(self))
