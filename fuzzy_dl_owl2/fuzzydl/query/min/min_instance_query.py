from __future__ import annotations

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.degree.degree_expression import DegreeExpression
from fuzzy_dl_owl2.fuzzydl.exception.inconsistent_ontology_exception import (
    InconsistentOntologyException,
)
from fuzzy_dl_owl2.fuzzydl.individual.individual import Individual
from fuzzy_dl_owl2.fuzzydl.knowledge_base import KnowledgeBase
from fuzzy_dl_owl2.fuzzydl.milp.expression import Expression
from fuzzy_dl_owl2.fuzzydl.milp.solution import Solution
from fuzzy_dl_owl2.fuzzydl.milp.term import Term
from fuzzy_dl_owl2.fuzzydl.milp.variable import Variable
from fuzzy_dl_owl2.fuzzydl.query.instance_query import InstanceQuery
from fuzzy_dl_owl2.fuzzydl.util.constants import VariableType


class MinInstanceQuery(InstanceQuery):
    def __init__(self, concept: Concept, individual: Individual) -> None:
        super().__init__(concept, individual)

    def preprocess(self, kb: KnowledgeBase) -> None:
        q: Variable = kb.milp.get_new_variable(VariableType.SEMI_CONTINUOUS)
        kb.old_01_variables += 1
        self.obj_expr: Expression = Expression(Term(1.0, q))

        if "(some " in str(self.conc) or "(b-some " in str(self.conc):
            kb.set_dynamic_blocking()

        kb.add_assertion(
            self.ind,
            -self.conc,
            DegreeExpression.get_degree(Expression(1.0, Term(-1.0, q))),
        )
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
        return f"Is {self.ind} instance of {self.conc} ? >= "
