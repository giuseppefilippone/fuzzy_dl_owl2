from __future__ import annotations

import typing

from fuzzy_dl_owl2.fuzzydl.concept.concrete.triangular_concrete_concept import (
    TriangularConcreteConcept,
)
from fuzzy_dl_owl2.fuzzydl.concept.operator_concept import OperatorConcept
from fuzzy_dl_owl2.fuzzydl.util import constants
from fuzzy_dl_owl2.fuzzydl.util.constants import ConceptType
from fuzzy_dl_owl2.fuzzydl.util.util import Util


class TriangularFuzzyNumber(TriangularConcreteConcept):
    K1: float = float("-inf")
    K2: float = float("inf")

    @typing.overload
    def __init__(self, name: str, a: float, b: float, c: float) -> None: ...

    @typing.overload
    def __init__(self, a: float, b: float, c: float) -> None: ...

    def __init__(self, *args) -> None:
        assert len(args) in [3, 4]
        if len(args) == 3:
            assert all(isinstance(a, constants.NUMBER) for a in args)
            self.__tringular_fn_init_2(*args)
        else:
            assert isinstance(args[0], str)
            assert all(isinstance(a, constants.NUMBER) for a in args[1:])
            self.__tringular_fn_init_1(*args)

    def __tringular_fn_init_1(self, name: str, a: float, b: float, c: float) -> None:
        super().__init__(name, self.K1, self.K2, a, b, c)
        self.type = ConceptType.FUZZY_NUMBER
        self.name = name or self.compute_name()

    def __tringular_fn_init_2(self, a: float, b: float, c: float) -> None:
        self.__init__(f"({a}, {b}, {c})", a, b, c)

    @staticmethod
    def add(t1: typing.Self, t2: typing.Self) -> typing.Self:
        return t1 + t2

    @staticmethod
    def minus(t1: typing.Self, t2: typing.Self) -> typing.Self:
        return t1 - t2

    @staticmethod
    def times(t1: typing.Self, t2: typing.Self) -> typing.Self:
        return t1 * t2

    @staticmethod
    def divided_by(t1: typing.Self, t2: typing.Self) -> typing.Self:
        return t1 / t2

    @staticmethod
    def set_range(min_range: float, max_range: float) -> None:
        TriangularFuzzyNumber.K1 = min_range
        TriangularFuzzyNumber.K2 = max_range

    @staticmethod
    def has_defined_range() -> bool:
        return TriangularFuzzyNumber.K1 != float("-inf")

    def clone(self) -> typing.Self:
        return TriangularFuzzyNumber(self.name, self.a, self.b, self.c)

    def is_concrete(self) -> bool:
        return True

    def get_best_non_fuzzy_performance(self) -> float:
        return Util.round((self.a + self.b + self.c) / 3.0)

    def is_number(self) -> bool:
        return self.a == self.b == self.c

    def compute_name(self) -> str:
        return f"({self.k1}, {self.k2}; {self.a}, {self.b}, {self.c})"

    def __add__(self, other: typing.Self) -> typing.Self:
        return TriangularFuzzyNumber(
            self.a + other.a, self.b + other.b, self.c + other.c
        )

    def __sub__(self, other: typing.Self) -> typing.Self:
        return TriangularFuzzyNumber(
            self.a - other.c, self.b - other.b, self.c - other.a
        )

    def __mul__(self, other: typing.Self) -> typing.Self:
        return TriangularFuzzyNumber(
            self.a * other.a, self.b * other.b, self.c * other.c
        )

    def __truediv__(self, other: typing.Self) -> typing.Self:
        if 0.0 in (other.a, other.b, other.c):
            Util.error(
                f"Error: Cannot divide by zero in fuzzy number ({other.a}, {other.b}, {other.c})."
            )
            return None
        return TriangularFuzzyNumber(
            self.a / other.c, self.b / other.b, self.c / other.a
        )

    def __neg__(self) -> TriangularFuzzyNumber:
        return OperatorConcept.not_(self)

    def __and__(self, value: typing.Self) -> typing.Self:
        return OperatorConcept.and_(self, value)

    def __or__(self, value: typing.Self) -> typing.Self:
        return OperatorConcept.or_(self, value)

    def __hash__(self) -> int:
        return hash(str(self))

    def __eq__(self, other: typing.Self) -> bool:
        return (
            type(self) == type(other)
            and self.a == other.a
            and self.b == other.b
            and self.c == other.c
        )

    def __ne__(self, other: typing.Self) -> bool:
        return not (self == other)
