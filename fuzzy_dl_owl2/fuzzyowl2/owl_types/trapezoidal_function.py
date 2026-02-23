from fuzzy_dl_owl2.fuzzyowl2.owl_types.fuzzy_datatype import FuzzyDatatype


class TrapezoidalFunction(FuzzyDatatype):
    """
    This class models a trapezoidal membership function, a fundamental construct in fuzzy logic used to define a set with a flat top region where membership is complete. It is characterized by four floating-point parameters: the left endpoint `a`, the left peak `b`, the right peak `c`, and the right endpoint `d`. The function increases linearly from `a` to `b`, maintains a maximum membership value between `b` and `c`, and decreases linearly from `c` to `d`. To utilize this class, instantiate it with the four coordinates that define the specific trapezoidal shape required for the fuzzy set. As a subclass of `FuzzyDatatype`, it integrates into the FuzzyOWL2 framework to represent fuzzy data types with specific geometric boundaries.

    :param _a: The left endpoint of the trapezoidal membership function.
    :type _a: float
    :param _b: The left peak point of the trapezoidal membership function.
    :type _b: float
    :param _c: The right peak point of the trapezoidal membership function.
    :type _c: float
    :param _d: The right endpoint of the trapezoidal membership function.
    :type _d: float
    """


    def __init__(self, a: float, b: float, c: float, d: float) -> None:
        """
        Initializes a new instance of the trapezoidal function by defining the four key parameters that determine its shape. The arguments `a`, `b`, `c`, and `d` correspond to the x-coordinates of the trapezoid's vertices, typically representing the start of the rise, the start of the plateau, the end of the plateau, and the end of the fall. This constructor stores these values as internal attributes to configure the function's behavior, assuming the caller provides values that adhere to the logical ordering $a \le b \le c \le d$ to form a valid trapezoid.

        :param a: The first numerical value used to initialize the object's state.
        :type a: float
        :param b: The second float value used to initialize the object.
        :type b: float
        :param c: The third floating-point value used to initialize the instance.
        :type c: float
        :param d: The value assigned to the internal `_d` attribute during object initialization.
        :type d: float
        """

        super().__init__()
        self._a: float = a
        self._b: float = b
        self._c: float = c
        self._d: float = d

    def get_a(self) -> float:
        """
        Returns the value of the internal attribute `_a`, which represents the first parameter defining the trapezoidal function's geometry. This parameter typically corresponds to the leftmost x-coordinate of the function's support or the point where the function begins to rise. The method performs a direct retrieval without modifying the object's state and returns the value as a float.

        :return: The current value of the attribute 'a'.

        :rtype: float
        """

        return self._a

    def get_b(self) -> float:
        """
        Returns the value of the internal attribute `_b`, which represents the left boundary of the trapezoid's upper plateau. This method serves as a read-only accessor to retrieve the x-coordinate where the function stops increasing and reaches its maximum value. It does not modify the object's state or perform any calculations beyond returning the stored float.

        :return: The value of the attribute `_b`.

        :rtype: float
        """

        return self._b

    def get_c(self) -> float:
        """
        Returns the value of the internal parameter `_c`, which represents the right endpoint of the trapezoid's top plateau. This value marks the transition point where the function's output stops being maximal and begins to decrease. As a getter method, it provides read-only access to this specific coordinate without altering the function's state.

        :return: The value of the attribute c.

        :rtype: float
        """

        return self._c

    def get_d(self) -> float:
        """
        Returns the value of the parameter $d$, which defines the upper bound of the trapezoidal function's support. This value corresponds to the x-coordinate where the function's membership value returns to zero after the plateau. The method acts as a simple accessor for the internal `_d` attribute and does not modify the state of the object.

        :return: The current value of the _d attribute.

        :rtype: float
        """

        return self._d

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the trapezoidal function, formatted to resemble a constructor call. The string includes the function name followed by the six internal attributes—k1, k2, a, b, c, and d—that define the specific geometry of the trapezoid. This representation is useful for debugging and logging, providing a concise summary of the object's state without modifying the underlying data.

        :return: A string representation of the object, formatted as a function call containing the current parameter values.

        :rtype: str
        """

        return f"trapezoidal({self._k1}, {self._k2}, {self._a}, {self._b}, {self._c}, {self._d})"
