from __future__ import annotations

from fuzzy_dl_owl2.fuzzydl.exception.inconsistent_ontology_exception import (
    InconsistentOntologyException,
)
from fuzzy_dl_owl2.fuzzydl.knowledge_base import KnowledgeBase
from fuzzy_dl_owl2.fuzzydl.milp.solution import Solution
from fuzzy_dl_owl2.fuzzydl.query.query import Query


class KbSatisfiableQuery(Query):
    """
    Knowledge base satisfiability degree
    """

    def __init__(self) -> None:
        super().__init__()

    def preprocess(self, kb: KnowledgeBase) -> None:
        pass

    def solve(self, kb: KnowledgeBase) -> Solution:
        try:
            return (
                Solution(1.0)
                if self.is_consistent_kb(kb)
                else Solution(Solution.INCONSISTENT_KB)
            )
        except InconsistentOntologyException:
            return Solution(Solution.INCONSISTENT_KB)

    def is_consistent_kb(self, kb: KnowledgeBase) -> bool:
        kb.solve_abox()
        cloned: KnowledgeBase = kb.clone()
        if len(cloned.individuals) == 0:
            cloned.get_new_individual()
            cloned.solve_assertions()
        sol: Solution = cloned.optimize(None)
        return sol is not None and sol.is_consistent_kb()

    def __str__(self) -> str:
        return "Is KnowledgeBase satisfiable? = "
