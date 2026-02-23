import typing

from fuzzy_dl_owl2.fuzzydl.util import constants


class Solution:

    """
    This class encapsulates the outcome of a query performed on a fuzzy knowledge base, distinguishing between a numerical degree of satisfaction and the consistency status of the base itself. When initialized with a floating-point number, it represents a valid query result where the knowledge base is consistent, storing the satisfaction value and allowing the retrieval of specific variable bindings. Alternatively, it can be instantiated with a boolean flag to explicitly represent an inconsistent knowledge base, in which case the satisfaction value is disregarded. Users can access the consistency status, the numerical solution, and any associated variable values through dedicated accessor methods, while the string representation provides a human-readable summary of the result.

    :param CONSISTENT_KB: Constant indicating a consistent fuzzy Knowledge Base.
    :type CONSISTENT_KB: bool
    :param INCONSISTENT_KB: Constant flag indicating an inconsistent fuzzy Knowledge Base, used to initialize a solution object.
    :type INCONSISTENT_KB: bool

    :raises ValueError: Raised if the argument provided to the constructor is neither a boolean nor a numeric type.
    """


    # Indicates whether the fuzzy KB is consistent
    CONSISTENT_KB: bool = True
    # Indicates whether the fuzzy KB is inconsistent
    INCONSISTENT_KB: bool = False

    @typing.overload
    def __init__(self, consistent: bool) -> None: ...

    @typing.overload
    def __init__(self, sol: float) -> None: ...

    def __init__(self, *args) -> None:
        """
        Initializes a new instance of the Solution class based on a single provided argument. The constructor validates the input type and delegates the specific initialization logic to private helper methods: boolean arguments are routed to `__solution_init_1`, while numeric arguments are routed to `__solution_init_2`. If the argument is neither a boolean nor a number, a `ValueError` is raised. The method also enforces that exactly one argument is passed, raising an `AssertionError` otherwise.

        :param args: A single argument used to initialize the object, which must be a boolean or a number.
        :type args: typing.Any

        :raises ValueError: Raised if the provided argument is not a boolean or a number.
        """

        assert len(args) == 1
        if isinstance(args[0], bool):
            self.__solution_init_1(*args)
        elif isinstance(args[0], constants.NUMBER):
            self.__solution_init_2(*args)
        else:
            raise ValueError

    def __solution_init_1(self, consistent: bool) -> None:
        # Numerical value of the solution
        """
        Initializes the core state attributes for a solution instance, setting the numerical solution value (`sol`) to a default float of 0.0 and assigning the provided boolean consistency status to the `consistent` attribute. Additionally, it creates an empty dictionary to store variable values (`showed_variables`). This method effectively resets or establishes the initial state of these specific instance variables, overwriting any pre-existing data.

        :param consistent: Indicates whether the fuzzy knowledge base is consistent.
        :type consistent: bool
        """

        self.sol: typing.Union[bool, float] = 0.0
        # Consistency of the fuzzy KB
        self.consistent: bool = consistent
        # Value of the showed variables
        self.showed_variables: dict[str, float] = dict()

    def __solution_init_2(self, sol: float) -> None:
        # Numerical value of the solution
        """
        Initializes the internal state of the solution object by setting the numerical solution value, establishing the consistency of the fuzzy knowledge base, and preparing a container for displayed variables. It assigns the provided numerical value to the solution attribute, defaults the consistency flag to true, and creates an empty dictionary to track the values of variables that have been shown. This method serves as a secondary initialization routine to reset or configure the object's state before further operations.

        :param sol: Numerical value of the solution.
        :type sol: float
        """

        self.sol: typing.Union[bool, float] = sol
        # Consistency of the fuzzy KB
        self.consistent: bool = True
        # Value of the showed variables
        self.showed_variables: dict[str, float] = dict()

    def is_consistent_kb(self) -> bool:
        """
        Returns a boolean flag indicating the consistency status of the original Knowledge Base (KB). This method acts as a direct accessor to the internal `consistent` attribute, reflecting whether the KB was found to be logically sound during prior processing. It does not perform any new computations or modify the object's state.

        :return: True if the original Knowledge Base is consistent, False otherwise.

        :rtype: bool
        """

        return self.consistent

    def get_solution(self) -> typing.Union[bool, float]:
        """
        Retrieves the solution stored within the instance, which represents the outcome of a query over a consistent knowledge base. The returned value can be either a boolean, indicating satisfiability or truth, or a float, representing a numerical metric such as a probability or cost. This method acts as a simple accessor and does not perform any computation or modify the object's state.

        :return: The solution to the query, returned as either a boolean (True/False) or a float (e.g., a probability or confidence score).

        :rtype: typing.Union[bool, float]
        """

        return self.sol

    def get_showed_variables(self) -> dict[str, float]:
        """
        Returns a dictionary containing the values of variables that were highlighted or determined during the query resolution process. This method is intended to be used after a query has been successfully solved over a consistent Knowledge Base. The keys of the dictionary are variable names, and the values are their corresponding floating-point representations. Note that this method returns a direct reference to the internal dictionary, so modifying the returned object will affect the state of the Solution instance.

        :return: A dictionary mapping variable names to their float values, representing the variables resulting from a solved query over a consistent knowledge base.

        :rtype: dict[str, float]
        """

        return self.showed_variables

    def add_showed_variable(self, var_name: str, value: float) -> None:
        """
        Updates the internal collection of variables designated for display by associating a specific name with a floating-point value. This method modifies the instance's `showed_variables` dictionary in place, adding a new entry if the name does not exist or overwriting the existing value if it does. It is typically used to record metrics or parameters that need to be tracked or visualized later in the solution process.

        :param var_name: The name of the showed variable to set.
        :type var_name: str
        :param value: Numeric content to assign to the showed variable.
        :type value: float
        """

        self.showed_variables[var_name] = value

    def __hash__(self) -> int:
        """
        Computes a hash value for the instance by converting the object to its string representation and hashing the resulting string. This enables instances of the class to be used as dictionary keys or stored in sets. The hash value is entirely dependent on the output of the `__str__` method, meaning that the efficiency of this operation is tied to the complexity of generating the string representation. If the object is mutable, modifying it after it has been added to a hash-based collection will lead to inconsistent behavior, as the hash value will change while the object remains in its original bucket.

        :return: An integer hash value derived from the string representation of the object.

        :rtype: int
        """

        return hash(str(self))

    def __repr__(self) -> str:
        """
        Returns the official string representation of the object, which is primarily intended for debugging and developer feedback. This implementation delegates directly to the informal string conversion logic, meaning the output is identical to the result of calling `str()` on the instance. Consequently, the returned string may not strictly adhere to the convention of being a valid Python expression that can be used to recreate the object.

        :return: The string representation of the object.

        :rtype: str
        """

        return str(self)

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the solution object, which varies based on the consistency of the underlying knowledge base. If the solution is consistent, the method returns the string representation of the solution itself; otherwise, it returns a message indicating that the knowledge base is inconsistent.

        :return: Returns the string representation of the solution if the knowledge base is consistent, or 'Inconsistent KB' otherwise.

        :rtype: str
        """

        if self.consistent:
            return str(self.sol)
        return "Inconsistent KB"
