import typing
from abc import ABC, abstractmethod

from fuzzy_dl_owl2.fuzzydl.milp.expression import Expression
from fuzzy_dl_owl2.fuzzydl.milp.inequation import Inequation
from fuzzy_dl_owl2.fuzzydl.util.constants import InequalityType


class Degree(ABC):

    @staticmethod
    @abstractmethod
    def get_degree(value) -> typing.Self:
        raise NotImplementedError

    # @typing.overload
    # @staticmethod
    # def get_degree(value: float) -> typing.Self:
    #     return DegreeNumeric(value)

    # @typing.overload
    # @staticmethod
    # def get_degree(value: Variable) -> typing.Self:
    #     return DegreeVariable(value)

    # @typing.overload
    # @staticmethod
    # def get_degree(value: Expression) -> typing.Self:
    #     return DegreeExpression(value)

    @abstractmethod
    def clone(self) -> typing.Self:
        pass

    @abstractmethod
    def is_numeric(self) -> bool:
        pass

    @abstractmethod
    def create_inequality_with_degree_rhs(
        self,
        expression: Expression,
        inequation_type: InequalityType,
    ) -> Inequation:
        pass

    @abstractmethod
    def add_to_expression(self, expression: Expression) -> Expression:
        pass

    @abstractmethod
    def subtract_from_expression(self, expression: Expression) -> Expression:
        pass

    @abstractmethod
    def multiply_constant(self, double: float) -> Expression:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def __eq__(self, degree: typing.Self) -> bool:
        pass

    def __ne__(self, value: typing.Self) -> bool:
        return not (self == value)

    @abstractmethod
    def is_number_not_one(self) -> bool:
        pass

    @abstractmethod
    def is_number_zero(self) -> bool:
        pass

    def __repr__(self) -> str:
        return str(self)
