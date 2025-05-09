from __future__ import annotations

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.individual.individual import Individual
from fuzzy_dl_owl2.fuzzydl.milp.expression import Expression
from fuzzy_dl_owl2.fuzzydl.milp.term import Term
from fuzzy_dl_owl2.fuzzydl.milp.variable import Variable
from fuzzy_dl_owl2.fuzzydl.query.defuzzify.defuzzify_query import DefuzzifyQuery


class SomDefuzzifyQuery(DefuzzifyQuery):

    def __init__(self, c: Concept, ind: Individual, f_name: str) -> None:
        super().__init__(c, ind, f_name)

    def __str__(self) -> str:
        return f"Smallest of the maxima defuzzification of feature {self.f_name} for instance {self.a} = "

    def get_obj_expression(self, q: Variable) -> Expression:
        return Expression(Term(1.0, q))
