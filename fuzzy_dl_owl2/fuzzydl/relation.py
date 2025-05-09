from __future__ import annotations

import typing

if typing.TYPE_CHECKING:
    from fuzzy_dl_owl2.fuzzydl.degree.degree import Degree
    from fuzzy_dl_owl2.fuzzydl.individual.individual import Individual


class Relation:
    def __init__(
        self, role_name: str, ind1: Individual, ind2: Individual, degree: Degree
    ):
        self.role_name: str = role_name
        self.ind_a: Individual = ind1
        self.ind_b: Individual = ind2
        self.degree: Degree = degree

    def clone(self) -> typing.Self:
        return Relation(self.role_name, self.ind_a, self.ind_b, self.degree)

    def get_subject_individual(self) -> Individual:
        return self.ind_a

    def get_object_individual(self) -> Individual:
        return self.ind_b

    def set_object_individual(self, ind: Individual) -> None:
        self.ind_b = ind

    def set_subject_individual(self, ind: Individual) -> None:
        self.ind_a = ind

    def get_role_name(self) -> str:
        return self.role_name

    def get_degree(self) -> Degree:
        return self.degree

    def get_name_without_degree(self) -> str:
        return f"({self.ind_a}, {self.ind_b}): {self.role_name}"

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return f"{self.get_name_without_degree()} >= {self.degree}"
