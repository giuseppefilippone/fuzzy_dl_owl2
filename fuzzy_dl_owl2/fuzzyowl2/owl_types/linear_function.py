from fuzzy_dl_owl2.fuzzyowl2.owl_types.fuzzy_datatype import FuzzyDatatype


class LinearFunction(FuzzyDatatype):
    """
    This class models a linear membership function within the FuzzyOWL2 framework, serving as a specific implementation of a fuzzy datatype. It is defined by two primary parameters, `a` and `b`, which represent the left and right endpoints of the linear shape, respectively. These endpoints determine the slope and interval of the function, allowing it to calculate degrees of membership for values within a fuzzy set. While the constructor initializes the geometric endpoints, the class also utilizes lower and upper bounds (`k1` and `k2`) to fully define the domain of the linear function.

    :param _a: The left endpoint of the linear membership function.
    :type _a: float
    :param _b: The right endpoint of the linear membership function.
    :type _b: float
    """


    def __init__(self, a: float, b: float) -> None:
        """
        Initializes a new instance of the LinearFunction class, representing a mathematical linear relationship defined as f(x) = ax + b. The method accepts two floating-point parameters, a and b, which serve as the slope and y-intercept of the line, respectively. These values are stored as private instance attributes _a and _b for use in subsequent calculations. As a side effect, the constructor also invokes the initializer of the superclass to ensure proper object initialization within the inheritance hierarchy.

        :param a: The first floating-point value used to initialize the instance.
        :type a: float
        :param b: The second numeric value used to initialize the object.
        :type b: float
        """

        super().__init__()
        self._a: float = a
        self._b: float = b

    def get_a(self) -> float:
        """
        Returns the floating-point value representing the coefficient 'a' (slope) of the linear function. This accessor method retrieves the internal `_a` attribute without modifying the object's state. It assumes the object has been properly initialized with a valid numerical value for the coefficient.

        :return: The current value of the internal attribute `_a`.

        :rtype: float
        """

        return self._a

    def get_b(self) -> float:
        """
        Returns the y-intercept of the linear function, corresponding to the constant term in the equation $y = mx + b$. This method provides read-only access to the internal `_b` attribute, ensuring that the value is retrieved without altering the object's state. The returned value is a float representing the point where the function crosses the y-axis.

        :return: The value of the attribute _b.

        :rtype: float
        """

        return self._b

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the linear function instance, formatted as a function call containing the object's internal parameters. The output string displays the values of the attributes `_k1`, `_k2`, `_a`, and `_b` in sequence within the syntax `linear(...)`. This method is intended for display and debugging purposes and does not alter the state of the object.

        :return: A human-readable string representation of the object, formatted as 'linear(k1, k2, a, b)'.

        :rtype: str
        """

        return f"linear({self._k1}, {self._k2}, {self._a}, {self._b})"
