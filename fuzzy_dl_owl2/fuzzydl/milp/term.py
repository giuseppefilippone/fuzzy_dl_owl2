import typing

from fuzzy_dl_owl2.fuzzydl.milp.variable import Variable
from fuzzy_dl_owl2.fuzzydl.util import constants


class Term:

    @typing.overload
    def __init__(self, coeff: float, var: Variable) -> None: ...

    @typing.overload
    def __init__(self, var: Variable) -> None: ...

    def __init__(self, *args) -> None:
        assert len(args) in [1, 2]
        if len(args) == 1:
            assert isinstance(args[0], Variable)
            self.__term_init_2(*args)
        else:
            assert isinstance(args[0], constants.NUMBER)
            assert isinstance(args[1], Variable)
            self.__term_init_1(*args)

    def __term_init_1(self, coeff: typing.Union[int, float], var: Variable) -> None:
        self.var: Variable = var
        self.coeff: float = coeff

    def __term_init_2(self, var: Variable) -> None:
        self.__term_init_1(1.0, var)

    def clone(self) -> typing.Self:
        return Term(self.coeff, self.var)

    def get_var(self) -> Variable:
        return self.var

    def get_coeff(self) -> float:
        return self.coeff

    def clone(self) -> typing.Self:
        return Term(self.coeff, self.var)

    def __neg__(self) -> typing.Self:
        return Term(-self.coeff, self.var)

    def __add__(self, term: typing.Self) -> typing.Self:
        if self.var != term.var:
            raise ValueError("Cannot add terms with different variables")
        return Term(self.coeff + term.coeff, self.var)

    def __sub__(self, term: typing.Self) -> typing.Self:
        return self + (-term)

    def __mul__(self, scalar: float) -> typing.Self:
        return Term(self.coeff * scalar, self.var)

    def __rmul__(self, scalar: float) -> typing.Self:
        return self * scalar

    def __truediv__(self, scalar: float) -> typing.Self:
        return self * (1 / scalar)

    def __eq__(self, term: typing.Self) -> bool:
        if not isinstance(term, Term):
            return False
        return self.var == term.var and self.coeff == term.coeff

    def __ne__(self, term: typing.Self) -> bool:
        return not (self == term)

    def __hash__(self) -> int:
        return hash(str(self))

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return f"{self.coeff} * {self.var}"
