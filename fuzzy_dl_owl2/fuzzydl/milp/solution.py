import typing

from fuzzy_dl_owl2.fuzzydl.util import constants


class Solution:
    CONSISTENT_KB: bool = True
    INCONSISTENT_KB: bool = False

    @typing.overload
    def __init__(self, consistent: bool) -> None: ...

    @typing.overload
    def __init__(self, sol: float) -> None: ...

    def __init__(self, *args) -> None:
        assert len(args) == 1
        if isinstance(args[0], bool):
            self.__solution_init_1(*args)
        elif isinstance(args[0], constants.NUMBER):
            self.__solution_init_2(*args)
        else:
            raise ValueError

    def __solution_init_1(self, consistent: bool) -> None:
        self.sol: typing.Union[bool, float] = 0.0
        self.consistent: bool = consistent

    def __solution_init_2(self, sol: float) -> None:
        self.sol: typing.Union[bool, float] = sol
        self.consistent: bool = True

    def is_consistent_kb(self) -> bool:
        return self.consistent

    def get_solution(self) -> typing.Union[bool, float]:
        return self.sol

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        if self.consistent:
            return str(self.sol)
        return "Inconsistent KB"
