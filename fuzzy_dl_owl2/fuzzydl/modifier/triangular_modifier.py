from __future__ import annotations

import typing

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.concept.modified.triangularly_modified_concept import (
    TriangularlyModifiedConcept,
)
from fuzzy_dl_owl2.fuzzydl.concept.operator_concept import OperatorConcept
from fuzzy_dl_owl2.fuzzydl.modifier.modifier import Modifier
from fuzzy_dl_owl2.fuzzydl.util.util import Util


class TriangularModifier(Modifier):
    def __init__(self, name: str, a: float, b: float, c: float) -> None:
        super().__init__(name)
        if a > b or b > c:
            Util.error(f"Error: Triangular functions require {a} <= {b} <= {c}")
        self._a = a
        self._b = b
        self._c = c

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
        return TriangularModifier(self.name, self.a, self.b, self.c)

    def compute_name(self) -> str:
        return f"triangular-modifier({self.a}, {self.b}, {self.c})"

    def get_membership_degree(self, x: float) -> float:
        if x <= self.a or x >= self.c:
            return 0.0
        if x <= self.b:
            return (x - self.a) / (self.b - self.a)
        return (self.c - x) / (self.c - self.b)

    def modify(self, concept: Concept) -> Concept:
        return TriangularlyModifiedConcept(concept, self)

    def __neg__(self) -> Concept:
        return OperatorConcept.not_(self)

    def __and__(self, value: typing.Self) -> typing.Self:
        return OperatorConcept.and_(self, value)

    def __or__(self, value: typing.Self) -> typing.Self:
        return OperatorConcept.or_(self, value)

    def __hash__(self) -> int:
        return hash(str(self))

    # def __str__(self) -> str:
    #     return self.get_name()
