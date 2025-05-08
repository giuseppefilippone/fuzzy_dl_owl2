from __future__ import annotations

from fuzzy_reasoner.fuzzydl.exception.inconsistent_ontology_exception import (
    InconsistentOntologyException,
)
from fuzzy_reasoner.fuzzydl.knowledge_base import KnowledgeBase
from fuzzy_reasoner.fuzzydl.milp.expression import Expression
from fuzzy_reasoner.fuzzydl.milp.solution import Solution
from fuzzy_reasoner.fuzzydl.query.query import Query


class MinQuery(Query):
    def __init__(self, expr: Expression) -> None:
        self.obj_expr = expr

    def preprocess(self, kb: KnowledgeBase) -> None:
        pass

    def solve(self, kb: KnowledgeBase) -> None:
        try:
            self.set_initial_time()
            kb.solve_abox()
            cloned: KnowledgeBase = kb.clone()
            sol: Solution = cloned.optimize(self.obj_expr)
            self.set_total_time()
            return sol
        except InconsistentOntologyException:
            return Solution(False)

    def __str__(self) -> str:
        return f"{self.obj_expr} ? >= "
