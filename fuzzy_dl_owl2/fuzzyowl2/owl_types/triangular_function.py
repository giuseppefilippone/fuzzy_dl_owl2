from fuzzy_dl_owl2.fuzzyowl2.owl_types.fuzzy_datatype import FuzzyDatatype


class TriangularFunction(FuzzyDatatype):
    """
    This class models a triangular membership function, which is commonly used in fuzzy logic systems to define vague or imprecise concepts. It is characterized by three specific points: the left endpoint where the membership degree begins to increase, the peak point where the membership degree reaches its maximum, and the right endpoint where the membership degree returns to zero. Inheriting from FuzzyDatatype, it serves as a concrete implementation within the FuzzyOWL2 framework, enabling the representation of fuzzy sets and constraints in ontological reasoning. To utilize this class, instantiate it with three floating-point numbers corresponding to these geometric parameters to define the shape and support of the fuzzy region.

    :param _a: The left endpoint of the triangular membership function.
    :type _a: float
    :param _b: The peak point of the triangular membership function.
    :type _b: float
    :param _c: The right endpoint of the triangular membership function.
    :type _c: float
    """


    def __init__(self, a: float, b: float, c: float) -> None:
        """
        Initializes a new instance of the TriangularFunction class by accepting three floating-point values that define the shape of the function. The parameters `a`, `b`, and `c` are stored as private attributes `_a`, `_b`, and `_c` respectively, serving as the defining characteristics for the triangle. Additionally, this method calls the superclass initializer to ensure proper inheritance chain setup.

        :param a: The first floating-point value used to initialize the object's state.
        :type a: float
        :param b: The second of three values used to initialize the instance.
        :type b: float
        :param c: The third value or coefficient initializing the instance.
        :type c: float
        """

        super().__init__()
        self._a: float = a
        self._b: float = b
        self._c: float = c

    def get_a(self) -> float:
        """
        Retrieves the value of the internal attribute `_a`, which typically represents the lower bound or the first vertex defining the shape of the triangular function. This method provides read-only access to the parameter without modifying the object's state. It assumes that `_a` has been properly initialized as a float during the object's construction.

        :return: The value of the internal attribute `_a`.

        :rtype: float
        """

        return self._a

    def get_b(self) -> float:
        """
        Retrieves the value of the internal parameter `_b`, which typically represents the peak or center point of the triangular function. This method serves as a simple accessor and returns the value as a float without modifying the object's state. The validity of the returned value depends on the initialization of the `TriangularFunction` instance.

        :return: The value of the `_b` attribute.

        :rtype: float
        """

        return self._b

    def get_c(self) -> float:
        """
        Returns the value of the internal attribute `_c`, which serves as a key parameter defining the shape or range of the triangular function. As a standard accessor method, it provides read-only access to this configuration value without inducing any side effects or altering the object's state. The method guarantees that the parameter is returned as a float, ensuring compatibility with numerical operations performed by the class.

        :return: The value of the internal attribute `_c`.

        :rtype: float
        """

        return self._c

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the triangular function instance, formatted to resemble a constructor call. The output string explicitly lists the values of the internal parameters `_k1`, `_k2`, `_a`, `_b`, and `_c`, providing a concise summary of the object's configuration. This method has no side effects and relies on the string conversion of the internal attributes; it is primarily used for debugging, logging, or displaying the object to the user.

        :return: A string representation of the object, formatted as a constructor call displaying the current values of the parameters.

        :rtype: str
        """

        return f"triangular({self._k1}, {self._k2}, {self._a}, {self._b}, {self._c})"
