from __future__ import annotations

import typing

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.degree.degree import Degree
from fuzzy_dl_owl2.fuzzydl.util.constants import LogicOperatorType


class GeneralConceptInclusion:
    def __init__(
        self,
        subsumer: Concept,
        subsumed: Concept,
        degree: Degree,
        type_: LogicOperatorType,
    ):
        self.subsumer: Concept = subsumer
        self.subsumed: Concept = subsumed
        self.degree: Degree = degree
        self.type: LogicOperatorType = type_

    def clone(self) -> typing.Self:
        return GeneralConceptInclusion(
            self.subsumer, self.subsumed, self.degree, self.type
        )

    def get_subsumer(self) -> Concept:
        return self.subsumer

    def get_subsumed(self) -> Concept:
        return self.subsumed

    def get_type(self) -> LogicOperatorType:
        return self.type

    def get_degree(self) -> Degree:
        return self.degree

    def set_degree(self, deg: Degree) -> None:
        self.degree = deg

    def set_subsumer(self, new_concept: Concept) -> None:
        self.subsumer = new_concept

    def set_subsumed(self, new_concept: Concept) -> None:
        self.subsumed = new_concept

    def __eq__(self, other: typing.Self) -> bool:
        return (
            isinstance(other, GeneralConceptInclusion)
            and self.subsumed == other.subsumed
            and self.subsumer == other.subsumer
            and self.degree == other.degree
            and self.type == other.type
        )

    def __ne__(self, other: typing.Self) -> bool:
        return not (self == other)

    def __lt__(self, other: typing.Self) -> bool:
        return isinstance(other, GeneralConceptInclusion) and hash(self) < hash(other)

    def __le__(self, other: typing.Self) -> bool:
        return not (self > other)

    def __gt__(self, other: typing.Self) -> bool:
        return isinstance(other, GeneralConceptInclusion) and hash(self) > hash(other)

    def __ge__(self, other: typing.Self) -> bool:
        return not (self < other)

    def __hash__(self) -> int:
        return hash(str(self))

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return (
            f"{self.subsumed} =>_{self.type.name[0]} {self.subsumer} >= {self.degree}"
        )
