import typing

from fuzzy_dl_owl2.fuzzydl.util import constants
from fuzzy_dl_owl2.fuzzydl.util.constants import ConcreteFeatureType


class ConcreteFeature:

    @typing.overload
    def __init__(self, name: str) -> None: ...

    @typing.overload
    def __init__(self, name: str, is_boolean: bool) -> None: ...

    @typing.overload
    def __init__(self, name: str, k1: int, k2: int) -> None: ...

    @typing.overload
    def __init__(self, name: str, k1: float, k2: float) -> None: ...

    def __init__(self, *args) -> None:
        assert len(args) in [1, 2, 3]

        assert isinstance(args[0], str)
        if len(args) == 1:
            self.__concrete_feature_init_1(*args)
        elif len(args) == 2:
            assert isinstance(args[1], bool)
            self.__concrete_feature_init_2(*args)
        elif len(args) == 3:
            if isinstance(args[1], int) and isinstance(args[2], int):
                self.__concrete_feature_init_3(*args)
            elif isinstance(args[1], constants.NUMBER) and isinstance(
                args[2], constants.NUMBER
            ):
                self.__concrete_feature_init_4(*args)
            else:
                raise ValueError
        else:
            raise ValueError

    def __concrete_feature_init_1(self, name: str) -> None:
        self.name: str = name
        self.k1: typing.Optional[typing.Union[float, int]] = None
        self.k2: typing.Optional[typing.Union[float, int]] = None
        self.type: ConcreteFeatureType = ConcreteFeatureType.STRING

    def __concrete_feature_init_2(self, name: str, is_boolean: bool) -> None:
        self.__concrete_feature_init_1(name)
        if is_boolean:
            self.type: ConcreteFeatureType = ConcreteFeatureType.BOOLEAN

    def __concrete_feature_init_3(self, name: str, k1: int, k2: int) -> None:
        self.__concrete_feature_init_1(name)
        self.k1: typing.Optional[typing.Union[float, int]] = k1
        self.k2: typing.Optional[typing.Union[float, int]] = k2
        self.type: ConcreteFeatureType = ConcreteFeatureType.INTEGER

    def __concrete_feature_init_4(self, name: str, k1: float, k2: float) -> None:
        self.__concrete_feature_init_1(name)
        self.k1: typing.Optional[typing.Union[float, int]] = k1
        self.k2: typing.Optional[typing.Union[float, int]] = k2
        self.type: ConcreteFeatureType = ConcreteFeatureType.REAL

    def clone(self) -> typing.Self:
        if self.type == ConcreteFeatureType.BOOLEAN:
            return ConcreteFeature(self.name, is_boolean=True)
        elif self.type == ConcreteFeatureType.STRING:
            return ConcreteFeature(self.name)

        return ConcreteFeature(self.name, self.k1, self.k2)

    def get_type(self) -> ConcreteFeatureType:
        return self.type

    def set_type(self, new_type: ConcreteFeatureType) -> None:
        self.type = new_type

    def get_k1(self) -> typing.Optional[typing.Union[float, int]]:
        return self.k1

    def get_k2(self) -> typing.Optional[typing.Union[float, int]]:
        return self.k2

    def set_range(
        self,
        k1: typing.Optional[typing.Union[float, int]],
        k2: typing.Optional[typing.Union[float, int]],
    ) -> None:
        self.k1 = k1
        self.k2 = k2

    def get_name(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return self.get_name()
