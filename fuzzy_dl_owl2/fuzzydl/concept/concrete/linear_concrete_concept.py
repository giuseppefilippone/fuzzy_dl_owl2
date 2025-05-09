from __future__ import annotations

import typing

from fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_concrete_concept import (
    FuzzyConcreteConcept,
)
from fuzzy_dl_owl2.fuzzydl.concept.operator_concept import OperatorConcept
from fuzzy_dl_owl2.fuzzydl.util.util import Util


class LinearConcreteConcept(FuzzyConcreteConcept):

    def __init__(self, name: str, k1: float, k2: float, a: float, b: float) -> None:
        super().__init__(name)
        if k1 > a:
            Util.error(f"Error: Left functions require {k1} <= {a}")
        if b < 1.0:
            Util.error(f"Error: Left functions require {b} <= 1.0")

        self.k1: float = float(k1)
        self.k2: float = float(k2)
        self._a: float = float(a)
        self._b: float = float(b)

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

    def clone(self) -> typing.Self:
        return LinearConcreteConcept(self.name, self.k1, self.k2, self.a, self.b)

    def get_membership_degree(self, value: float) -> float:
        if value <= 0:
            return 0.0
        if value >= 1.0:
            return 1.0
        if value <= self.a:
            return self.b / self.a * value
        return (value * (1.0 - self.b) + (self.b - self.a)) / (1.0 - self.a)

    def compute_name(self) -> str:
        return f"linear({self.k1}, {self.k2}, {self.a}, {self.b})"

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
