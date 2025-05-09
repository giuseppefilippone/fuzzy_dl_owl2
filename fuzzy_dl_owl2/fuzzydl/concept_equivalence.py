from __future__ import annotations

import typing

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept


class ConceptEquivalence:
    def __init__(self, c1: Concept, c2: Concept) -> None:
        self.c1: Concept = c1
        self.c2: Concept = c2

    def clone(self) -> typing.Self:
        return ConceptEquivalence(self.c1, self.c2)

    def get_c1(self) -> Concept:
        return self.c1

    def get_c2(self) -> Concept:
        return self.c2
