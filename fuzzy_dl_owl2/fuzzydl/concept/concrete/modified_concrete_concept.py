from __future__ import annotations

import typing

from fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_concrete_concept import (
    FuzzyConcreteConcept,
)
from fuzzy_dl_owl2.fuzzydl.concept.operator_concept import OperatorConcept
from fuzzy_dl_owl2.fuzzydl.modifier.modifier import Modifier


class ModifiedConcreteConcept(FuzzyConcreteConcept):
    def __init__(self, name: str, modifier: Modifier, f: FuzzyConcreteConcept) -> None:
        super().__init__(name)
        self.k1: float = 0.0
        self.k2: float = 1.0
        self._modifier: Modifier = modifier
        self._modified: FuzzyConcreteConcept = f

    @property
    def modifier(self) -> Modifier:
        return self._modifier

    @modifier.setter
    def modifier(self, value: Modifier) -> None:
        self._modifier = value

    @property
    def modified(self) -> FuzzyConcreteConcept:
        return self._modified

    @modified.setter
    def modified(self, value: FuzzyConcreteConcept) -> None:
        self._modified = value

    def clone(self) -> typing.Self:
        return ModifiedConcreteConcept(self.name, self.modifier, self.modified)

    # def solve_assertion(
    #     self, ind: Individual, lower_limit: Degree, kb: KnowledgeBase
    # ) -> None:
    #     self.modifier.solve_assertion(ind, self, lower_limit, kb)

    def get_membership_degree(self, x: float) -> float:
        if x <= 0.0 or x > 1.0:
            return 0.0
        y: float = self.modified.get_membership_degree(x)
        return self.modifier.get_membership_degree(y)

    def compute_name(self) -> str:
        return f"modified({self.modifier} {self.modified})"

    def __neg__(self) -> FuzzyConcreteConcept:
        return OperatorConcept.not_(self)

    def __and__(self, value: typing.Self) -> typing.Self:
        return OperatorConcept.and_(self, value)

    def __or__(self, value: typing.Self) -> typing.Self:
        return OperatorConcept.or_(self, value)

    def __hash__(self) -> int:
        return hash(str(self))

    # def __str__(self) -> str:
    #     return self.get_name()
