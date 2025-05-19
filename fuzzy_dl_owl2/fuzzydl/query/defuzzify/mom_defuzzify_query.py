from __future__ import annotations

import traceback
import typing

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.degree.degree_numeric import DegreeNumeric
from fuzzy_dl_owl2.fuzzydl.exception.fuzzy_ontology_exception import (
    FuzzyOntologyException,
)
from fuzzy_dl_owl2.fuzzydl.exception.inconsistent_ontology_exception import (
    InconsistentOntologyException,
)
from fuzzy_dl_owl2.fuzzydl.individual.created_individual import CreatedIndividual
from fuzzy_dl_owl2.fuzzydl.individual.individual import Individual
from fuzzy_dl_owl2.fuzzydl.knowledge_base import KnowledgeBase
from fuzzy_dl_owl2.fuzzydl.milp.expression import Expression
from fuzzy_dl_owl2.fuzzydl.milp.solution import Solution
from fuzzy_dl_owl2.fuzzydl.milp.term import Term
from fuzzy_dl_owl2.fuzzydl.milp.variable import Variable
from fuzzy_dl_owl2.fuzzydl.query.defuzzify.defuzzify_query import DefuzzifyQuery
from fuzzy_dl_owl2.fuzzydl.query.max.max_satisfiable_query import MaxSatisfiableQuery
from fuzzy_dl_owl2.fuzzydl.relation import Relation
from fuzzy_dl_owl2.fuzzydl.util.util import Util


class MomDefuzzifyQuery(DefuzzifyQuery):

    def __init__(self, c: Concept, ind: Individual, feature_name: str) -> None:
        super().__init__(c, ind, feature_name)

    def preprocess(self, kb: KnowledgeBase) -> None:
        pass

    def solve(self, kb: KnowledgeBase) -> Solution:
        try:
            kb.solve_abox()
            cloned: KnowledgeBase = kb.clone()
            cloned.set_dynamic_blocking()
            s: Solution = MaxSatisfiableQuery(self.conc, self.a).solve(cloned)
            if not s.is_consistent_kb():
                return s
            d: float = s.get_solution()
            # LOM
            cloned: KnowledgeBase = kb.clone()
            ind: Individual = cloned.individuals.get(str(self.a))
            cloned.set_dynamic_blocking()
            cloned.add_assertion(self.a, self.conc, DegreeNumeric.get_degree(d))
            cloned.solve_assertions()
            if self.f_name not in ind.role_relations:
                Util.warning("Warning: Problem in defuzzification. Answer is 0.")
                return None
        except InconsistentOntologyException:
            return Solution(False)

        rel_set: list[Relation] = ind.role_relations.get(self.f_name)
        b: CreatedIndividual = typing.cast(
            CreatedIndividual, rel_set[0].get_object_individual()
        )
        q: Variable = cloned.milp.get_variable(b)
        if q is None:
            Util.warning("Warning: Problem in defuzzification. Answer is 0.")
            return None

        try:
            obj_expr: Expression = Expression(Term(-1.0, q))
            sol1: Solution = cloned.optimize(obj_expr)
            if sol1.get_solution() < 0.0:
                sol1 = Solution(sol1.get_solution())

            # SOM
            obj_expr: Expression = Expression(Term(1.0, q))
            sol2: Solution = cloned.optimize(obj_expr)
            if sol2.get_solution() < 0.0:
                sol2 = Solution(sol2.get_solution())

            # MOM
            if sol1.is_consistent_kb() and sol2.is_consistent_kb():
                value = (sol1.get_solution() + sol2.get_solution()) / 2.0
                kb.milp.print_instance_of_labels(self.f_name, str(self.a), value)
                return Solution(value)

            # Returns an inconsistent KB solution
            return sol1
        except FuzzyOntologyException as e:
            traceback.print_exc()
        except InconsistentOntologyException as e:
            traceback.print_exc()
        return Solution(False)

    def get_obj_expression(self, variable: Variable) -> Expression:
        return Expression(Term(-1.0, variable))

    def __str__(self) -> str:
        return f"Middle of the maxima defuzzification of feature {self.f_name} for instance {self.a} = "
