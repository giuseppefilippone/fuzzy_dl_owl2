import typing

from fuzzy_dl_owl2.fuzzydl.degree.degree import Degree
from fuzzy_dl_owl2.fuzzydl.milp.expression import Expression
from fuzzy_dl_owl2.fuzzydl.milp.inequation import Inequation
from fuzzy_dl_owl2.fuzzydl.util.constants import InequalityType


class DegreeNumeric(Degree):

    def __init__(self, numeric: float) -> None:
        self.value: float = float(numeric)

    @staticmethod
    def get_one() -> typing.Self:
        return DegreeNumeric(1.0)

    @staticmethod
    def get_degree(value: float) -> typing.Self:
        return DegreeNumeric(value)

    def clone(self) -> typing.Self:
        return DegreeNumeric.get_degree(self.value)

    def get_numerical_value(self) -> float:
        return self.value

    def create_inequality_with_degree_rhs(
        self, expr: Expression, inequation_type: InequalityType
    ) -> Inequation:
        return Inequation(expr - 1.0 * self.value, inequation_type)

    def is_numeric(self) -> bool:
        return True

    def add_to_expression(self, expr: Expression) -> Expression:
        return expr + self.value

    def subtract_from_expression(self, expr: Expression) -> Expression:
        return expr - self.value

    def multiply_constant(self, constant: float) -> Expression:
        return Expression(self.value * constant)

    def is_number_not_one(self) -> bool:
        return self.value != 1.0

    def is_number_zero(self) -> bool:
        return self.value == 0.0

    def __eq__(self, d: Degree) -> bool:
        if isinstance(d, DegreeNumeric):
            return self.value == d.get_numerical_value()
        return False

    def __str__(self) -> str:
        return f"Degree({self.value})"
