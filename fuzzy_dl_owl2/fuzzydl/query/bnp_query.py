from __future__ import annotations

from fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_number.triangular_fuzzy_number import (
    TriangularFuzzyNumber,
)
from fuzzy_dl_owl2.fuzzydl.knowledge_base import KnowledgeBase
from fuzzy_dl_owl2.fuzzydl.milp.solution import Solution
from fuzzy_dl_owl2.fuzzydl.query.query import Query


class BnpQuery(Query):
    def __init__(self, c: TriangularFuzzyNumber) -> None:
        self.c: TriangularFuzzyNumber = c

    def preprocess(self, kb: KnowledgeBase) -> None:
        pass

    def solve(self, kb: KnowledgeBase) -> Solution:
        return Solution(self.c.get_best_non_fuzzy_performance())

    def __str__(self) -> str:
        return f"Best non-fuzzy performance of {self.c.compute_name()} = "
