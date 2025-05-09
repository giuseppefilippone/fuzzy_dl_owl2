from __future__ import annotations

import typing

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.degree.degree import Degree


class Restriction:
    def __init__(self, role_name: str, concept: Concept, degree: Degree) -> None:
        self.role_name: str = role_name
        self.concept: Concept = concept
        self.degree: Degree = degree

    def clone(self) -> typing.Self:
        return Restriction(self.role_name, self.concept, self.degree)

    def get_role_name(self) -> str:
        return self.role_name

    def get_degree(self) -> Degree:
        return self.degree

    def get_concept(self) -> Concept:
        return self.concept

    def get_name_without_degree(self) -> str:
        return f"(all {self.role_name} {self.concept})"

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return f"{self.get_name_without_degree()} >= {self.degree}"
