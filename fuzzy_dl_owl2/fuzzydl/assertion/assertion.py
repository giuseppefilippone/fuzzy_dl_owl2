from __future__ import annotations

import typing

if typing.TYPE_CHECKING:
    from fuzzy_dl_owl2.fuzzydl.individual.individual import Individual

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.degree.degree import Degree
from fuzzy_dl_owl2.fuzzydl.degree.degree_numeric import DegreeNumeric
from fuzzy_dl_owl2.fuzzydl.util.constants import ConceptType


class Assertion:

    def __init__(self, ind: Individual, c: Concept, d: Degree) -> None:
        self.individual: Individual = ind
        self.concept: Concept = c
        self.degree: Degree = d

    def clone(self) -> typing.Self:
        return Assertion(self.individual, self.concept, self.degree)

    def get_type(self) -> ConceptType:
        return self.concept.type

    def get_lower_limit(self) -> Degree:
        return self.degree

    def get_concept(self) -> Concept:
        return self.concept

    def get_individual(self) -> Individual:
        return self.individual

    def set_individual(self, ind: Individual) -> None:
        self.individual = ind

    def set_lower_limit(self, deg: Degree) -> None:
        self.degree = deg

    def get_name_without_degree(self) -> str:
        return f"{self.individual}:{self.concept}"

    def equals(self, ass: typing.Self) -> bool:
        return self == ass

    def __eq__(self, value: typing.Self) -> bool:
        if not isinstance(value, Assertion):
            return False

        same: bool = False
        if str(self) == str(value):
            same = True
        elif (
            self.get_name_without_degree() == value.get_name_without_degree()
            and isinstance(self.get_lower_limit(), DegreeNumeric)
            and isinstance(value.get_lower_limit(), DegreeNumeric)
            and typing.cast(DegreeNumeric, self.get_lower_limit()).get_numerical_value()
            < typing.cast(DegreeNumeric, value.get_lower_limit()).get_numerical_value()
        ):
            same = True
        return same

    def __ne__(self, value: typing.Self) -> bool:
        return not (self == value)

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return f"{self.get_name_without_degree()} >= {self.degree}"
