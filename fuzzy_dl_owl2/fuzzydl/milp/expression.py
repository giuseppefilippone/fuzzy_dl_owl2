import typing

import trycast

from fuzzy_dl_owl2.fuzzydl.milp.term import Term
from fuzzy_dl_owl2.fuzzydl.milp.variable import Variable
from fuzzy_dl_owl2.fuzzydl.util import constants


class Expression:

    @typing.overload
    def __init__(self, constant: typing.Union[int, float]) -> None: ...

    @typing.overload
    def __init__(self, constant: typing.Union[int, float], *terms: Term) -> None: ...

    @typing.overload
    def __init__(self, *terms: Term) -> None: ...

    @typing.overload
    def __init__(self, expr: typing.Self) -> None: ...

    @typing.overload
    def __init__(self, v: typing.Union[list[Variable], set[Variable]]) -> None: ...

    def __init__(self, *args) -> None:
        if len(args) == 0:
            self.__expression_init_1(0)
        elif len(args) == 1:
            if isinstance(args[0], constants.NUMBER):
                self.__expression_init_1(*args)
            elif isinstance(args[0], Expression):
                self.__expression_init_4(*args)
            elif trycast.trycast(typing.Union[list[Variable], set[Variable]], args[0]):
                self.__expression_init_5(*args)
            elif isinstance(args[0], Term):
                self.__expression_init_3(*args)
            else:
                raise ValueError
        else:
            if isinstance(args[0], constants.NUMBER) and all(
                isinstance(a, Term) for a in args[1:]
            ):
                self.__expression_init_2(*args)
            elif all(isinstance(a, Term) for a in args):
                self.__expression_init_3(*args)
            else:
                raise ValueError

    def __expression_init_1(self, constant: typing.Union[int, float]) -> None:
        assert isinstance(constant, constants.NUMBER)
        self.constant: typing.Union[int, float] = constant
        self.terms: list[Term] = []

    def __expression_init_2(
        self, constant: typing.Union[int, float], *terms: Term
    ) -> None:
        assert len(terms) > 0
        self.__expression_init_1(constant)
        self.terms: list[Term] = [t for t in terms]

    def __expression_init_3(self, *terms: Term) -> None:
        self.__expression_init_2(0.0, *terms)

    def __expression_init_4(self, expr: typing.Self) -> None:
        self.__expression_init_2(expr.constant, *expr.terms)

    def __expression_init_5(
        self, v: typing.Union[list[Variable], set[Variable]]
    ) -> None:
        self.__expression_init_2(0.0, *[Term(1.0, var) for var in v])

    def get_terms(self) -> list[Term]:
        return self.terms

    def get_constant(self) -> typing.Union[int, float]:
        return self.constant

    def set_constant(self, constant: typing.Union[int, float]) -> None:
        self.constant = constant

    def clone(self) -> typing.Self:
        return Expression(self.constant, *self.terms)

    @staticmethod
    def negate_expression(expr: typing.Self) -> typing.Self:
        return -expr

    @staticmethod
    def add_constant(
        expr: typing.Self, constant: typing.Union[int, float]
    ) -> typing.Self:
        return constant + expr

    def increment_constant(self) -> None:
        self.constant += 1

    def add_term(self, term: Term) -> None:
        for idx, t in enumerate(self.terms):
            if t.get_var() == term.get_var():
                self.terms[idx] = t + term
                return
        self.terms.append(term)
        assert len(self.terms) > 0

    @staticmethod
    def add_term_(exp: typing.Self, term: Term) -> typing.Self:
        curr_expr: Expression = exp
        curr_expr.add_term(term)
        return curr_expr

    @staticmethod
    def add_expressions(expr1: typing.Self, expr2: typing.Self) -> typing.Self:
        return expr1 + expr2

    @staticmethod
    def subtract_expressions(expr1: typing.Self, expr2: typing.Self) -> typing.Self:
        return expr1 - expr2

    @staticmethod
    def multiply_constant(
        expr: typing.Self, constant: typing.Union[int, float]
    ) -> typing.Self:
        return expr * constant

    def get_constant_term(self, var: Variable) -> typing.Union[int, float]:
        for term in self.terms:
            if term.get_var() == var:
                return term.get_coeff()
        return 0.0

    def __neg__(self) -> typing.Self:
        return Expression(-self.get_constant(), *[-t for t in self.get_terms()])

    def __add__(
        self, value: typing.Union[int, float, typing.Self, Term]
    ) -> typing.Self:
        if isinstance(value, constants.NUMBER):
            return Expression(self.get_constant() + value, *self.get_terms())
        elif isinstance(value, Term):
            result: Expression = self
            result.add_term(value)
            return result
        result: Expression = self
        for term in value.get_terms():
            result.add_term(term)
        result.constant += value.get_constant()
        return result

    def __radd__(self, scalar: typing.Union[int, float]) -> typing.Self:
        return self + scalar

    def __sub__(self, expr: typing.Union[int, float, typing.Self, Term]) -> typing.Self:
        return self + (-expr)

    def __rsub__(self, scalar: typing.Union[int, float]) -> typing.Self:
        return -self + scalar

    def __mul__(self, scalar: typing.Union[int, float]) -> typing.Self:
        return Expression(
            self.get_constant() * scalar,
            *[t * scalar for t in self.get_terms()],
        )

    def __rmul__(self, scalar: typing.Union[int, float]) -> typing.Self:
        return self * scalar

    def __truediv__(self, scalar: typing.Union[int, float]) -> typing.Self:
        return self * (1 / scalar)

    def __hash__(self) -> int:
        return hash(str(self))

    def __eq__(self, value: typing.Self) -> bool:
        if not isinstance(value, Expression):
            return False
        return len(self.terms) == len(value.terms) and all(term in value.terms for term in self.terms)

    def __ne__(self, value: typing.Self) -> bool:
        return not (self == value)

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        parts: list[str] = []
        if self.constant != 0.0:
            parts.append(str(self.constant))

        for term in self.terms:
            n: float = float(term.get_coeff())
            if n == 1.0:
                parts.append(f"+ {term.get_var()}")
            elif n == -1.0:
                parts.append(f"- {term.get_var()}")
            else:
                parts.append(f"{'+ ' if n >= 0 else '- '}{abs(n)} {term.get_var()}")
        return " ".join(parts)
