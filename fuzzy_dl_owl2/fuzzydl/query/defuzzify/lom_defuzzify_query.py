from __future__ import annotations

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.individual.individual import Individual
from fuzzy_dl_owl2.fuzzydl.milp.expression import Expression
from fuzzy_dl_owl2.fuzzydl.milp.term import Term
from fuzzy_dl_owl2.fuzzydl.milp.variable import Variable
from fuzzy_dl_owl2.fuzzydl.query.defuzzify.defuzzify_query import DefuzzifyQuery


class LomDefuzzifyQuery(DefuzzifyQuery):
    def __init__(self, c: Concept, ind: Individual, feature_name: str) -> None:
        super().__init__(c, ind, feature_name)

    def __str__(self) -> str:
        return f"Largest of the maxima defuzzification of feature {self.f_name} for instance {self.a} = "

    def get_obj_expression(self, variable: Variable) -> Expression:
        return Expression(Term(-1.0, variable))
