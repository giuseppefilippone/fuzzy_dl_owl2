from fuzzy_dl_owl2.fuzzyowl2.owl_types.fuzzy_datatype import FuzzyDatatype


class RightShoulderFunction(FuzzyDatatype):
    """
    This class models a fuzzy membership function characterized by a "right shoulder" shape, typically used to represent concepts where values greater than a certain threshold have full membership. It is designed for use within the FuzzyOWL2 framework and extends the base `FuzzyDatatype`. The function is defined by two parameters, `a` and `b`, which establish the interval where the degree of membership linearly increases from zero to one; values below `a` have zero membership, while values at or above `b` have full membership.

    :param _a: The left endpoint of the right shoulder membership function.
    :type _a: float
    :param _b: The right endpoint of the right shoulder membership function.
    :type _b: float
    """


    def __init__(self, a: float, b: float) -> None:
        """
        Initializes the function instance by storing the provided boundary parameters `a` and `b` as internal attributes. This constructor invokes the superclass initializer to ensure proper inheritance chain setup before assigning the float values to `_a` and `_b`, which typically define the inflection points or range of the right-shoulder shape. No validation is performed on the input values, allowing any floating-point numbers to be assigned.

        :param a: The first floating-point value to be stored in the instance.
        :type a: float
        :param b: The second float value used to initialize the object.
        :type b: float
        """

        super().__init__()
        self._a: float = a
        self._b: float = b

    def get_a(self) -> float:
        """
        Retrieves the value of the internal parameter 'a' for the RightShoulderFunction instance. This method acts as a getter for the private attribute `_a`, returning the float value that defines a specific characteristic of the function's shape or position.

        :return: The value of a.

        :rtype: float
        """

        return self._a

    def get_b(self) -> float:
        """
        Returns the value of the parameter 'b' for the right shoulder function. This method serves as an accessor for the internal attribute `_b`, which typically defines a specific boundary or slope point within the function's definition. The operation has no side effects and simply returns the stored floating-point value.

        :return: The value of the attribute b.

        :rtype: float
        """

        return self._b

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the right-shoulder function instance, formatted to display the specific parameters defining the function's shape. The output follows the pattern "right-shoulder(k1, k2, a, b)", where the placeholders are replaced by the actual values of the internal attributes. This representation is useful for logging, debugging, or displaying the object's configuration in a concise manner.

        :return: A string representation of the object in the format 'right-shoulder(k1, k2, a, b)'.

        :rtype: str
        """

        return f"right-shoulder({self._k1}, {self._k2}, {self._a}, {self._b})"
