import abc
import copy
import typing

from fuzzy_dl_owl2.fuzzydl.concept.interface.has_role_interface import HasRoleInterface


class HasValueInterface(HasRoleInterface, abc.ABC):

    def __init__(self, role: str, value: typing.Any) -> None:
        super().__init__(role)

        self._value: typing.Any = value

    @property
    def value(self) -> typing.Any:
        return self._value

    @value.setter
    def value(self, value: typing.Any) -> None:
        self._value = copy.deepcopy(value)
