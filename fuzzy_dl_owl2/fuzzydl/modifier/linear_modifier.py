from __future__ import annotations

import typing

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.concept.modified.linearly_modified_concept import (
    LinearlyModifiedConcept,
)
from fuzzy_dl_owl2.fuzzydl.concept.operator_concept import OperatorConcept
from fuzzy_dl_owl2.fuzzydl.modifier.modifier import Modifier


class LinearModifier(Modifier):

    def __init__(self, name: str, c: float) -> None:
        super().__init__(name)
        self._c: float = c
        self._a: float = c / (c + 1.0)
        self._b: float = 1.0 / (c + 1.0)

    @property
    def a(self) -> float:
        return self._a

    @a.setter
    def a(self, value: float) -> None:
        self._a = value

    @property
    def b(self) -> float:
        return self._b

    @b.setter
    def b(self, value: float) -> None:
        self._b = value

    @property
    def c(self) -> float:
        return self._c

    @c.setter
    def c(self, value: float) -> None:
        self._c = value

    def clone(self) -> typing.Self:
        return LinearModifier(self.name, self.c)

    def modify(self, concept: Concept) -> LinearlyModifiedConcept:
        return LinearlyModifiedConcept(concept, self)

    def compute_name(self) -> str:
        return f"linear-modifier({self.c})"

    def get_membership_degree(self, value: float) -> float:
        if value <= 0.0:
            return 0.0
        if value >= 1.0:
            return 1.0
        if value <= self.a:
            return self.b / self.a * value
        return (value * (1.0 - self.b) + self.b - self.a) / (1.0 - self.a)

    def __neg__(self) -> Concept:
        return OperatorConcept.not_(self)

    def __and__(self, value: typing.Self) -> typing.Self:
        return OperatorConcept.and_(self, value)

    def __or__(self, value: typing.Self) -> typing.Self:
        return OperatorConcept.or_(self, value)

    def __hash__(self) -> int:
        return hash(str(self))

    # def __str__(self) -> str:
    #     return self.compute_name()
