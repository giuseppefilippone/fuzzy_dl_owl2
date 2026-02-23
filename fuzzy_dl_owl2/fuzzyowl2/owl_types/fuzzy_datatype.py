import abc

class FuzzyDatatype(abc.ABC):

    """
    This abstract base class serves as a foundational component for representing fuzzy datatypes within the FuzzyOWL2 framework, specifically defining a range characterized by a lower and an upper bound. It manages two primary attributes, `k1` and `k2`, which correspond to the minimum and maximum values of the fuzzy interval, respectively. Intended to be subclassed, it provides getter and setter methods to manipulate these boundaries, allowing concrete implementations to define specific fuzzy logic behaviors based on these parameters. By default, the bounds are initialized to zero, providing a neutral starting state for derived classes.

    :param _k1: The lower bound of the fuzzy datatype.
    :type _k1: float
    :param _k2: The upper bound of the fuzzy datatype.
    :type _k2: float
    """


    def __init__(self) -> None:
        """Initializes a new instance of the FuzzyDatatype class by setting the internal state to default values. Specifically, it assigns a value of 0.0 to the private attributes _k1 and _k2, ensuring the object is ready for subsequent configuration or use in fuzzy logic operations."""

        self._k1: float = 0.0
        self._k2: float = 0.0

    def get_min_value(self) -> float:
        """
        Retrieves the minimum value defining the support of the fuzzy number, corresponding to the internal attribute `_k1`. This value represents the lower bound of the range where the membership function is non-zero. The method performs a direct retrieval without modifying the object's state and returns the value as a float.

        :return: The minimum value associated with the instance.

        :rtype: float
        """

        return self._k1

    def get_max_value(self) -> float:
        """
        Returns the upper bound or maximum value defining the range of this fuzzy datatype. This method accesses the internal `_k2` attribute, which typically represents the rightmost point of the support or core in fuzzy logic representations. The operation is a simple accessor and does not modify the state of the object.

        :return: 

        :rtype: float
        """

        return self._k2

    def set_min_value(self, min: float) -> None:
        """
        Assigns the specified floating-point value to the internal attribute `_k1`, effectively defining the lower bound or starting parameter for the fuzzy data type. This method directly mutates the instance's state without performing validation on the input type or logical consistency with other parameters. It returns `None`, indicating that the operation is performed solely for its side effect of updating the object's configuration.

        :param min: The new minimum value to be assigned.
        :type min: float
        """

        self._k1 = min

    def set_max_value(self, max: float) -> None:
        """
        Updates the upper bound parameter of the fuzzy datatype by assigning the provided float value to the internal `_k2` attribute. This method mutates the object's state in place, altering the definition of the fuzzy set's range or shape. It does not perform validation to ensure the new maximum is greater than the minimum value, so users must ensure logical consistency to avoid invalid configurations.

        :param max: The maximum value to set.
        :type max: float
        """

        self._k2 = max

    def __repr__(self) -> str:
        """
        Returns the official string representation of the `FuzzyDatatype` instance by delegating to the `__str__` method. This implementation ensures that the output used for debugging and logging is identical to the informal string representation, prioritizing human readability over a strictly unambiguous or executable Python expression.

        :return: A string representation of the object.

        :rtype: str
        """

        return str(self)
