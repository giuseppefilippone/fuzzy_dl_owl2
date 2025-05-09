from __future__ import annotations

import typing
from abc import abstractmethod

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.degree.degree_numeric import DegreeNumeric
from fuzzy_dl_owl2.fuzzydl.exception.inconsistent_ontology_exception import (
    InconsistentOntologyException,
)
from fuzzy_dl_owl2.fuzzydl.individual.created_individual import CreatedIndividual
from fuzzy_dl_owl2.fuzzydl.individual.individual import Individual
from fuzzy_dl_owl2.fuzzydl.knowledge_base import KnowledgeBase
from fuzzy_dl_owl2.fuzzydl.milp.expression import Expression
from fuzzy_dl_owl2.fuzzydl.milp.milp_helper import MILPHelper
from fuzzy_dl_owl2.fuzzydl.milp.solution import Solution
from fuzzy_dl_owl2.fuzzydl.milp.variable import Variable
from fuzzy_dl_owl2.fuzzydl.query.max.max_satisfiable_query import MaxSatisfiableQuery
from fuzzy_dl_owl2.fuzzydl.query.query import Query
from fuzzy_dl_owl2.fuzzydl.relation import Relation
from fuzzy_dl_owl2.fuzzydl.util.util import Util


class DefuzzifyQuery(Query):

    def __init__(self, c: Concept, ind: Individual, feature_name: str) -> None:
        self.conc: Concept = c
        self.a: Individual = ind
        self.f_name: str = feature_name
        self.obj_expr: Expression = None
        MILPHelper.PRINT_VARIABLES = False
        MILPHelper.PRINT_LABELS = False

    def preprocess(self, kb: KnowledgeBase) -> None:
        kb.set_dynamic_blocking()
        s: Solution = MaxSatisfiableQuery(self.conc, self.a).solve(kb)

        if s is not None and s.is_consistent_kb():
            self.a = kb.individuals[str(self.a)]
            kb.set_dynamic_blocking()
            kb.add_assertion(
                self.a, self.conc, DegreeNumeric.get_degree(s.get_solution())
            )
            kb.solve_assertions()

            if self.f_name in self.a.role_relations:
                rel_set: list[Relation] = self.a.role_relations[self.f_name]
                b: CreatedIndividual = typing.cast(
                    CreatedIndividual, rel_set[0].get_object_individual()
                )
                q: Variable = kb.milp.get_variable(b)
                self.obj_expr = self.get_obj_expression(q)

    def solve(self, kb: KnowledgeBase) -> typing.Optional[Solution]:
        try:
            kb.solve_abox()
            cloned: KnowledgeBase = kb.clone()
            self.preprocess(cloned)

            if self.obj_expr is not None:
                MILPHelper.PRINT_LABELS = True
                MILPHelper.PRINT_VARIABLES = True

                sol: Solution = cloned.optimize(self.obj_expr)
                if sol.get_solution() < 0.0:
                    return Solution(-sol.get_solution())
                return sol

            Util.warning("Warning: Problem in defuzzification. Answer is 0.")
            return None
        except InconsistentOntologyException:
            return Solution(False)

    @abstractmethod
    def get_obj_expression(self, variable: Variable) -> Expression:
        pass
