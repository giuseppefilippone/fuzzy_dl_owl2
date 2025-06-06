import typing

from fuzzy_dl_owl2.fuzzydl.util import constants


class Solution:
    # Indicates whether the fuzzy KB is consistent
    CONSISTENT_KB: bool = True
    # Indicates whether the fuzzy KB is inconsistent
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
        # Numerical value of the solution
        self.sol: typing.Union[bool, float] = 0.0
        # Consistency of the fuzzy KB
        self.consistent: bool = consistent
        # Value of the showed variables
        self.showed_variables: dict[str, float] = dict()

    def __solution_init_2(self, sol: float) -> None:
        # Numerical value of the solution
        self.sol: typing.Union[bool, float] = sol
        # Consistency of the fuzzy KB
        self.consistent: bool = True
        # Value of the showed variables
        self.showed_variables: dict[str, float] = dict()

    def is_consistent_kb(self) -> bool:
        """Indicates whether the original KB is consistent or not."""
        return self.consistent

    def get_solution(self) -> typing.Union[bool, float]:
        """Gets the solution to some query over a consistent KB."""
        return self.sol

    def get_showed_variables(self) -> dict[str, float]:
        """Gets the values of some variables after solving a query over a consistent KB."""
        return self.showed_variables

    def add_showed_variable(self, var_name: str, value: float) -> None:
        """Sets the value of a showed variable."""
        self.showed_variables[var_name] = value

    def __hash__(self) -> int:
        return hash(str(self))

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        if self.consistent:
            return str(self.sol)
        return "Inconsistent KB"
