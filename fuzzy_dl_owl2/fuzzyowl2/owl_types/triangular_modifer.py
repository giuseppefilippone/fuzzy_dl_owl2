from fuzzy_dl_owl2.fuzzyowl2.owl_types.fuzzy_modifier import FuzzyModifier


class TriangularModifier(FuzzyModifier):
    """
    This class implements a triangular membership function used to define fuzzy modifiers within the FuzzyOWL2 framework. It models the degree of membership using a geometric shape defined by three specific parameters: a left endpoint representing the start of the support, a peak point indicating maximum membership, and a right endpoint marking the end of the support. Instances of this class are created by providing these three float values, which collectively determine the specific characteristics of the fuzzy modification applied to a concept.

    :param _a: The left endpoint of the triangular membership function.
    :type _a: float
    :param _b: The peak point of the triangular membership function.
    :type _b: float
    :param _c: The right endpoint of the triangular membership function.
    :type _c: float
    """


    def __init__(self, a: float, b: float, c: float) -> None:
        """
        Initializes the TriangularModifier instance with three floating-point values that define the shape of the triangle. The parameters `a`, `b`, and `c` are stored as private attributes and generally represent the minimum, mode, and maximum values, respectively. This method invokes the superclass constructor to ensure proper inheritance chain setup, but it does not enforce any specific ordering or validation constraints on the input values during initialization.

        :param a: 
        :type a: float
        :param b: The second float value used to initialize the object's state.
        :type b: float
        :param c: The third numerical value used to initialize the object's state.
        :type c: float
        """

        super().__init__()
        self._a: float = a
        self._b: float = b
        self._c: float = c

    def get_a(self) -> float:
        """
        Returns the value of the internal attribute `_a`, which likely represents a specific parameter of the triangular modification, such as a boundary or coordinate. This method serves as a simple accessor and does not modify the state of the object. It assumes the instance has been properly initialized; otherwise, accessing the underlying attribute may raise an `AttributeError`.

        :return: The value of the internal attribute 'a'.

        :rtype: float
        """

        return self._a

    def get_b(self) -> float:
        """
        Retrieves the value of the internal attribute `_b`, which typically represents the mode or upper limit parameter of the triangular distribution. This method serves as a simple accessor, returning the stored floating-point value without performing any calculations or modifying the object's state. It assumes the instance has been properly initialized, as it directly exposes the underlying private attribute.

        :return: The value of the attribute b.

        :rtype: float
        """

        return self._b

    def get_c(self) -> float:
        """
        Returns the value of the internal parameter 'c' for the triangular modifier. This accessor method retrieves the floating-point number stored in the private attribute `_c` without causing any side effects or altering the object's state.

        :return: The value of the 'c' attribute.

        :rtype: float
        """

        return self._c

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the current instance, formatted to display the internal parameters of the triangular modification. The output string follows the pattern "triangular-modifier(a, b, c)", incorporating the values of the private attributes `_a`, `_b`, and `_c`. This representation is useful for logging, debugging, or displaying the object's state in a user-friendly format without altering the object itself.

        :return: A human-readable string representation of the object, formatted as "triangular-modifier(a, b, c)".

        :rtype: str
        """

        return f"triangular-modifier({self._a}, {self._b}, {self._c})"
