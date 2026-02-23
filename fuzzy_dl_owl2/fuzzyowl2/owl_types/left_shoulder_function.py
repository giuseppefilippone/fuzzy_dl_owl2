from fuzzy_dl_owl2.fuzzyowl2.owl_types.fuzzy_datatype import FuzzyDatatype


class LeftShoulderFunction(FuzzyDatatype):
    """
    Represents a left-shoulder membership function used in fuzzy logic systems, such as FuzzyOWL2, to model concepts where membership is high for low values and decreases as values increase. To use this class, instantiate it with two floating-point parameters, `a` and `b`, which define the start and end of the transition zone where the membership value drops from 1 to 0. The function relies on bounds `k1` and `k2`, inherited from the parent `FuzzyDatatype`, to define the overall domain of the fuzzy set.

    :param _a: The left endpoint of the left-shoulder membership function.
    :type _a: float
    :param _b: The right endpoint of the left-shoulder membership function.
    :type _b: float
    """


    def __init__(self, a: float, b: float) -> None:
        """
        Initializes the LeftShoulderFunction instance by defining its core parameters. This method accepts two floating-point numbers, `a` and `b`, which typically represent the boundaries or coefficients defining the function's shape, and assigns them to the internal attributes `_a` and `_b`. Additionally, it invokes the superclass's initialization routine to ensure proper inheritance chain setup.

        :param a: The initial value for the first component of the object's state.
        :type a: float
        :param b: The second numeric value used to initialize the instance.
        :type b: float
        """

        super().__init__()
        self._a: float = a
        self._b: float = b

    def get_a(self) -> float:
        """
        Retrieves the numeric value of the 'a' parameter, which defines a specific characteristic of the left shoulder function's shape. This method acts as a simple accessor for the private attribute `_a`, returning its current value without performing any calculations or validation. The operation is read-only and has no side effects on the object's state.

        :return: The current value of the attribute 'a'.

        :rtype: float
        """

        return self._a

    def get_b(self) -> float:
        """
        Returns the value of the internal parameter `_b`, which represents a specific boundary or configuration point for the left shoulder function. This method acts as a read-only accessor, retrieving the stored floating-point value without modifying the object's state or causing any side effects.

        :return: The value of the internal attribute _b.

        :rtype: float
        """

        return self._b

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the function instance, formatted to display its defining parameters. The output follows the pattern "left-shoulder(k1, k2, a, b)", where the values correspond to the internal attributes `_k1`, `_k2`, `_a`, and `_b`. This representation is primarily used for logging, debugging, and display purposes, and it does not modify the state of the object.

        :return: A string representation of the object, formatted as a function call with the current parameters.

        :rtype: str
        """

        return f"left-shoulder({self._k1}, {self._k2}, {self._a}, {self._b})"
