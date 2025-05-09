from __future__ import annotations

import typing

from fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_concrete_concept import (
    FuzzyConcreteConcept,
)
from fuzzy_dl_owl2.fuzzydl.concept.operator_concept import OperatorConcept
from fuzzy_dl_owl2.fuzzydl.exception.fuzzy_ontology_exception import (
    FuzzyOntologyException,
)


class TriangularConcreteConcept(FuzzyConcreteConcept):
    def __init__(
        self, name: str, k1: float, k2: float, a: float, b: float, c: float
    ) -> None:
        super().__init__(name)
        if a > b or b > c:
            raise FuzzyOntologyException(
                f"Error: Triangular functions require {a} <= {b} <= {c}"
            )
        if k1 > a:
            raise FuzzyOntologyException(
                f"Error: Triangular functions require {k1} <= {a}"
            )
        if k2 < b:
            raise FuzzyOntologyException(
                f"Error: Triangular functions require {k2} >= {b}"
            )
        self.k1: float = k1
        self.k2: float = k2
        self._a: float = float(a)
        self._b: float = float(b)
        self._c: float = float(c)

    @property
    def a(self) -> float:
        return self._a

    @a.setter
    def a(self, value: float) -> None:
        self._a = float(value)

    @property
    def b(self) -> float:
        return self._b

    @b.setter
    def b(self, value: float) -> None:
        self._b = float(value)

    @property
    def c(self) -> float:
        return self._c

    @c.setter
    def c(self, value: float) -> None:
        self._c = float(value)

    def clone(self) -> typing.Self:
        return TriangularConcreteConcept(
            self.name, self.k1, self.k2, self.a, self.b, self.c
        )

    def get_membership_degree(self, x: float) -> float:
        if x <= self.a or x >= self.c:
            return 0.0
        if x <= self.b:
            return (x - self.a) / (self.b - self.a)
        return (self.c - x) / (self.c - self.b)

    def compute_name(self) -> str:
        return f"triangular({self.k1}, {self.k2}, {self.a}, {self.b}, {self.c})"

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
