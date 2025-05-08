from __future__ import annotations

from fuzzy_reasoner.fuzzydl.concept.concept import Concept
from fuzzy_reasoner.fuzzydl.degree.degree_variable import DegreeVariable
from fuzzy_reasoner.fuzzydl.exception.inconsistent_ontology_exception import (
    InconsistentOntologyException,
)
from fuzzy_reasoner.fuzzydl.individual.individual import Individual
from fuzzy_reasoner.fuzzydl.knowledge_base import KnowledgeBase
from fuzzy_reasoner.fuzzydl.milp.expression import Expression
from fuzzy_reasoner.fuzzydl.milp.solution import Solution
from fuzzy_reasoner.fuzzydl.milp.term import Term
from fuzzy_reasoner.fuzzydl.milp.variable import Variable
from fuzzy_reasoner.fuzzydl.query.instance_query import InstanceQuery


class MaxInstanceQuery(InstanceQuery):
    def __init__(self, concept: Concept, individual: Individual) -> None:
        super().__init__(concept, individual)

    def preprocess(self, kb: KnowledgeBase) -> None:
        q: Variable = kb.milp.get_variable(self.ind, self.conc)
        kb.old_01_variables += 1
        self.obj_expr: Expression = Expression(Term(-1.0, q))

        if "(all " in str(self.conc) or "(not (b-some " in str(self.conc):
            kb.set_dynamic_blocking()

        kb.add_assertion(self.ind, self.conc, DegreeVariable.get_degree(q))
        kb.solve_assertions()

    def solve(self, kb: KnowledgeBase) -> Solution:
        try:
            self.set_initial_time()
            kb.solve_abox()
            cloned: KnowledgeBase = kb.clone()
            self.preprocess(cloned)
            sol: Solution = cloned.optimize(self.obj_expr)
            self.set_total_time()
            return sol
        except InconsistentOntologyException:
            return Solution(False)

    def __str__(self) -> str:
        return f"Is {self.ind} instance of {self.conc} ? <= "
