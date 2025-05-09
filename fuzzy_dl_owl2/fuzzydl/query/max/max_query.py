from __future__ import annotations

from fuzzy_dl_owl2.fuzzydl.exception.inconsistent_ontology_exception import (
    InconsistentOntologyException,
)
from fuzzy_dl_owl2.fuzzydl.knowledge_base import KnowledgeBase
from fuzzy_dl_owl2.fuzzydl.milp.expression import Expression
from fuzzy_dl_owl2.fuzzydl.milp.solution import Solution
from fuzzy_dl_owl2.fuzzydl.query.query import Query


class MaxQuery(Query):
    def __init__(self, expr: Expression) -> None:
        self.obj_expr: Expression = Expression.negate_expression(expr)

    def preprocess(self, kb: KnowledgeBase) -> None:
        pass

    def solve(self, kb: KnowledgeBase) -> Solution:
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
        return f"{self.obj_expr} <= "
