import typing

from fuzzy_dl_owl2.fuzzydl.milp.expression import Expression
from fuzzy_dl_owl2.fuzzydl.milp.term import Term
from fuzzy_dl_owl2.fuzzydl.util.constants import InequalityType


class Inequation:
    def __init__(self, exp: Expression, i_type: InequalityType) -> None:
        assert exp is not None and len(exp.get_terms()) > 0
        self.type: InequalityType = i_type
        self.expr: Expression = exp

    @staticmethod
    def greater_then(exp: Expression) -> typing.Self:
        return Inequation(exp, InequalityType.GREATER_THAN)

    @staticmethod
    def less_than(exp: Expression) -> typing.Self:
        return Inequation(exp, InequalityType.LESS_THAN)

    @staticmethod
    def equal_to(exp: Expression) -> typing.Self:
        return Inequation(exp, InequalityType.EQUAL)

    def clone(self) -> typing.Self:
        return Inequation(self.expr, self.type)

    def get_terms(self) -> list[Term]:
        return self.expr.get_terms()

    def get_constant(self) -> float:
        return -self.expr.get_constant()

    def get_type(self) -> InequalityType:
        return self.type

    def get_string_type(self) -> str:
        if self.type == InequalityType.EQUAL:
            return self.type.value
        elif self.type == InequalityType.LESS_THAN:
            return "<="
        assert self.type == InequalityType.GREATER_THAN
        return ">="

    def is_zero(self) -> bool:
        return all(term.get_coeff() == 0 for term in self.expr.get_terms()) and self.expr.get_constant() == 0

    def __hash__(self) -> int:
        return hash(str(self))

    def __eq__(self, value: typing.Self) -> bool:
        return self.expr == value.expr and self.type == value.type

    def __ne__(self, value: typing.Self) -> bool:
        return not (self == value)

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return f"{self.expr} {self.get_string_type()} 0"


GreaterThan = Inequation.greater_then
LessThan = Inequation.less_than
EqualTo = Inequation.equal_to
