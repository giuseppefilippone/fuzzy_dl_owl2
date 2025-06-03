import typing

from fuzzy_dl_owl2.fuzzydl.individual.created_individual import CreatedIndividual
from fuzzy_dl_owl2.fuzzydl.individual.individual import Individual
from fuzzy_dl_owl2.fuzzydl.milp.expression import Expression
from fuzzy_dl_owl2.fuzzydl.milp.milp_helper import MILPHelper
from fuzzy_dl_owl2.fuzzydl.milp.term import Term
from fuzzy_dl_owl2.fuzzydl.milp.variable import Variable
from fuzzy_dl_owl2.fuzzydl.relation import Relation
from fuzzy_dl_owl2.fuzzydl.util import constants
from fuzzy_dl_owl2.fuzzydl.util.constants import FeatureFunctionType


class FeatureFunction:

    @typing.overload
    def __init__(self, feature: typing.Self) -> None: ...

    @typing.overload
    def __init__(self, feature: str) -> None: ...

    @typing.overload
    def __init__(self, n: float) -> None: ...

    @typing.overload
    def __init__(self, feature: list[typing.Self]) -> None: ...

    @typing.overload
    def __init__(self, feature1: typing.Self, feature2: typing.Self) -> None: ...

    @typing.overload
    def __init__(self, n: float, feature: typing.Self) -> None: ...

    def __init__(self, *args) -> None:
        assert len(args) in [1, 2]
        if len(args) == 1:
            if isinstance(args[0], FeatureFunction):
                self.__feature_function_init_6(*args)
            elif isinstance(args[0], str):
                self.__feature_function_init_1(*args)
            elif isinstance(args[0], constants.NUMBER):
                self.__feature_function_init_2(*args)
            elif isinstance(args[0], typing.Sequence) and all(
                isinstance(a, FeatureFunction) for a in args[0]
            ):
                self.__feature_function_init_3(*args)
            else:
                raise ValueError
        elif len(args) == 2:
            if isinstance(args[0], FeatureFunction) and isinstance(
                args[1], FeatureFunction
            ):
                self.__feature_function_init_4(*args)
            elif isinstance(args[0], constants.NUMBER) and isinstance(
                args[1], FeatureFunction
            ):
                self.__feature_function_init_5(*args)
            else:
                raise ValueError
        else:
            raise ValueError

    def __feature_function_init_1(self, feature: str) -> None:
        self.type: FeatureFunctionType = FeatureFunctionType.ATOMIC
        self.f: list[FeatureFunction] = []
        self.feature: str = feature
        self.n: float = 0.0

    def __feature_function_init_2(self, n: float) -> None:
        self.type: FeatureFunctionType = FeatureFunctionType.NUMBER
        self.f: list[FeatureFunction] = []
        self.feature: str = ""
        self.n: float = n

    def __feature_function_init_3(self, feature: list[typing.Self]) -> None:
        self.type: FeatureFunctionType = FeatureFunctionType.SUM
        self.f: list[FeatureFunction] = feature
        self.feature: str = ""
        self.n: float = 0.0

    def __feature_function_init_4(
        self, feature1: typing.Self, feature2: typing.Self
    ) -> None:
        self.type: FeatureFunctionType = FeatureFunctionType.SUBTRACTION
        self.f: list[FeatureFunction] = [feature1, feature2]
        self.feature: str = ""
        self.n: float = 0.0

    def __feature_function_init_5(self, n: float, feature: typing.Self) -> None:
        self.type: FeatureFunctionType = FeatureFunctionType.PRODUCT
        self.f: list[FeatureFunction] = [feature]
        self.feature: str = ""
        self.n: float = n

    def __feature_function_init_6(self, feature: typing.Self) -> None:
        self.type: FeatureFunctionType = feature.type
        self.f: list[FeatureFunction] = feature.f
        self.feature: str = feature.feature
        self.n: float = feature.n

    def get_type(self) -> FeatureFunctionType:
        return self.type

    def get_number(self) -> float:
        return self.n

    def get_features(self) -> set[str]:
        features: set[str] = set()
        if self.type == FeatureFunctionType.ATOMIC:
            features.add(self.feature)
        elif self.type == FeatureFunctionType.PRODUCT:
            features.update(self.f[0].get_features())
        elif self.type == FeatureFunctionType.SUBTRACTION:
            features.update(self.f[0].get_features())
            features.update(self.f[1].get_features())
        elif self.type == FeatureFunctionType.SUM:
            for f in self.f:
                features.update(f.get_features())
        return features

    def to_expression(
        self, a: Individual, milp: MILPHelper
    ) -> typing.Optional[Expression]:
        if self.type == FeatureFunctionType.ATOMIC:
            # Get the filler "b" for feature(a)
            rel_set: list[Relation] = a.role_relations.get(self.feature)
            assert len(rel_set) > 0
            b: CreatedIndividual = typing.cast(
                CreatedIndividual, rel_set[0].get_object_individual()
            )
            # Get the variable xB
            x_b: Variable = milp.get_variable(b)
            return Expression(Term(1.0, x_b))
        elif self.type == FeatureFunctionType.NUMBER:
            return Expression(self.n)
        elif self.type == FeatureFunctionType.PRODUCT:
            assert len(self.f) == 1
            ex: Expression = self.f[0].to_expression(a, milp)
            return ex * self.n
        elif self.type == FeatureFunctionType.SUBTRACTION:
            assert len(self.f) == 2
            ex1: Expression = self.f[0].to_expression(a, milp)
            ex2: Expression = self.f[1].to_expression(a, milp)
            return ex1 - ex2
        elif self.type == FeatureFunctionType.SUM:
            assert len(self.f) >= 1
            ex1: Expression = self.f[0].to_expression(a, milp)
            for i in range(1, len(self.f)):
                ex2: Expression = self.f[i].to_expression(a, milp)
                ex1 = ex1 + ex2
            return ex1
        return None

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        if self.type == FeatureFunctionType.ATOMIC:
            return self.feature
        elif self.type == FeatureFunctionType.NUMBER:
            return str(self.n)
        elif self.type == FeatureFunctionType.PRODUCT:
            return f"({self.n} * {self.f[0]})"
        elif self.type == FeatureFunctionType.SUBTRACTION:
            return f"({self.f[0]} - {self.f[1]})"
        elif self.type == FeatureFunctionType.SUM:
            return f"({' + '.join(map(str, self.f))})"
        return ""
