from __future__ import annotations

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.degree.degree import Degree


class AtomicAssertion:
    def __init__(self, c: Concept, degree: Degree) -> None:
        self.c: Concept = c
        self.degree: Degree = degree

    def get_concept_name(self) -> str:
        return str(self.c)

    def get_degree(self) -> Degree:
        return self.degree

    def __str__(self) -> str:
        return f"< {self.c} {self.degree} >"
