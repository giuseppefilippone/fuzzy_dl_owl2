import typing

from fuzzy_dl_owl2.fuzzydl.degree.degree import Degree
from fuzzy_dl_owl2.fuzzydl.milp.expression import Expression
from fuzzy_dl_owl2.fuzzydl.milp.inequation import Inequation
from fuzzy_dl_owl2.fuzzydl.milp.term import Term
from fuzzy_dl_owl2.fuzzydl.milp.variable import Variable
from fuzzy_dl_owl2.fuzzydl.util.constants import InequalityType


class DegreeVariable(Degree):
    def __init__(self, variable: Variable) -> None:
        self.variable: Variable = variable

    @staticmethod
    def get_degree(value: Variable) -> typing.Self:
        return DegreeVariable(value)

    def get_variable(self) -> Variable:
        return self.variable

    def clone(self) -> typing.Self:
        return DegreeVariable.get_degree(self.variable)

    def create_inequality_with_degree_rhs(
        self, expr: Expression, inequality_type: InequalityType
    ) -> Inequation:
        return Inequation(expr + Term(-1.0, self.variable), inequality_type)

    def is_numeric(self) -> bool:
        return False

    def add_to_expression(self, expr: Expression) -> Expression:
        return expr + Term(1.0, self.variable)

    def subtract_from_expression(self, expr: Expression) -> Expression:
        return expr + Term(-1.0, self.variable)

    def multiply_constant(self, constant: float) -> Expression:
        return Expression(Term(constant, self.variable))

    def is_number_not_one(self) -> bool:
        return False

    def is_number_zero(self) -> bool:
        return False

    def __eq__(self, degree: Degree) -> bool:
        if isinstance(degree, DegreeVariable):
            return degree.get_variable() == self.get_variable()
        return False

    def __str__(self) -> str:
        return f"Degree({self.variable})"
