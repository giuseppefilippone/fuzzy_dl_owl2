import typing

from fuzzy_dl_owl2.fuzzydl.degree.degree import Degree
from fuzzy_dl_owl2.fuzzydl.milp.expression import Expression
from fuzzy_dl_owl2.fuzzydl.milp.inequation import Inequation
from fuzzy_dl_owl2.fuzzydl.util.constants import InequalityType


class DegreeExpression(Degree):
    def __init__(self, expr: Expression) -> None:
        self.expr: Expression = expr

    def get_expression(self) -> Expression:
        return self.expr

    @staticmethod
    def get_degree(value: Expression) -> typing.Self:
        return DegreeExpression(value)

    def clone(self) -> typing.Self:
        return DegreeExpression.get_degree(self.expr)

    def create_inequality_with_degree_rhs(
        self,
        expr: Expression,
        inequality_type: InequalityType,
    ) -> Inequation:
        return Inequation(
            expr - self.expr,
            inequality_type,
        )

    def is_numeric(self) -> bool:
        return False

    def add_to_expression(self, expr: Expression) -> Expression:
        return expr + self.expr

    def subtract_from_expression(self, expr: Expression) -> Expression:
        return expr - self.expr

    def multiply_constant(self, constant: float) -> Expression:
        return self.expr * constant

    def is_number_not_one(self) -> bool:
        return False

    def is_number_zero(self) -> bool:
        return False

    def __eq__(self, d: Degree) -> bool:
        if isinstance(d, DegreeExpression):
            return d == self.get_expression()
        return False

    def __str__(self) -> str:
        return f"Degree({self.expr})"
