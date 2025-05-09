from __future__ import annotations

from fuzzy_dl_owl2.fuzzydl.degree.degree import Degree
from fuzzy_dl_owl2.fuzzydl.restriction.restriction import Restriction


class HasValueRestriction(Restriction):
    def __init__(self, role_name: str, individual: str, degree: Degree) -> None:
        super().__init__(role_name, None, degree)
        self.ind_name: str = individual

    def get_individual(self) -> str:
        return self.ind_name

    def get_name_without_degree(self) -> str:
        return f"(not (b-some {self.role_name} {self.ind_name}))"
