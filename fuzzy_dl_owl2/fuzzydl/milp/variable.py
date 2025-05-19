import typing

from fuzzy_dl_owl2.fuzzydl.util.constants import VariableType


class Variable:
    VARIABLE_NAME: str = "y"
    VARIABLE_NUMBER: int = 0

    def __init__(self, name: str, v_type: VariableType) -> None:
        self.lower_bound: float = 0.0
        self.upper_bound: float = 0.0
        self.name: str = name
        self.type: VariableType = None
        self.datatype_filler: bool = False
        self.set_type(v_type)

    @staticmethod
    def get_binary_variable(name: str) -> typing.Self:
        return Variable(name, VariableType.BINARY)

    @staticmethod
    def get_continuous_variable(name: str) -> typing.Self:
        return Variable(name, VariableType.CONTINUOUS)

    @staticmethod
    def get_semi_continuous_variable(name: str) -> typing.Self:
        return Variable(name, VariableType.SEMI_CONTINUOUS)

    @staticmethod
    def get_integer_variable(name: str) -> typing.Self:
        return Variable(name, VariableType.INTEGER)

    def get_lower_bound(self) -> float:
        return self.lower_bound

    def get_type(self) -> VariableType:
        return self.type

    def get_datatype_filler_type(self) -> bool:
        return self.datatype_filler

    def get_upper_bound(self) -> float:
        return self.upper_bound

    def set_binary_variable(self) -> None:
        self.set_type(VariableType.BINARY)

    def set_datatype_filler_variable(self) -> None:
        self.datatype_filler = True

    def set_name(self, name: str) -> None:
        self.name = name

    def set_type(self, v_type: VariableType) -> None:
        if v_type in (VariableType.BINARY, VariableType.SEMI_CONTINUOUS):
            self.lower_bound = 0.0
            self.upper_bound = 1.0
        else:
            assert v_type in (VariableType.CONTINUOUS, VariableType.INTEGER)
            self.lower_bound = float("-inf")
            self.upper_bound = float("inf")
        self.type = v_type

    @staticmethod
    def get_new_variable(v_type: VariableType) -> typing.Self:
        Variable.VARIABLE_NUMBER += 1
        return Variable(f"{Variable.VARIABLE_NAME}{Variable.VARIABLE_NUMBER}", v_type)

    def clone(self) -> typing.Self:
        return Variable(self.name, self.type)

    def __eq__(self, value: typing.Self) -> bool:
        return str(self) == str(value)

    def __ne__(self, value: object) -> bool:
        return not (self == value)

    def __hash__(self) -> int:
        return hash(str(self))

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return self.name


BinaryVar = Variable.get_binary_variable
IntegerVar = Variable.get_integer_variable
UpVar = Variable.get_semi_continuous_variable
FreeVar = Variable.get_continuous_variable
