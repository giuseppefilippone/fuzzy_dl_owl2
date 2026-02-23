from fuzzy_dl_owl2.fuzzyowl2.owl_types.fuzzy_datatype import FuzzyDatatype


class CrispFunction(FuzzyDatatype):
    """
    This class represents a crisp function within the FuzzyOWL2 framework, acting as a specialized fuzzy datatype to model precise mathematical intervals or linear transformations. It is characterized by two primary coefficients, `a` and `b`, which are supplied during instantiation, and it is conceptually bounded by lower and upper limits, `k1` and `k2`. Users can employ this class to define crisp constraints in fuzzy ontologies by initializing it with the required parameters, and the object exposes these values through getter methods while providing a string representation that includes the bounds. It serves as a fundamental building block for integrating non-fuzzy, exact logic into a broader fuzzy system.

    :param _a: The first parameter of the crisp function.
    :type _a: float
    :param _b: The second parameter defining the crisp function.
    :type _b: float
    """


    def __init__(self, a: float, b: float) -> None:
        """
        Initializes a new instance of the CrispFunction class, configuring it with the provided numerical parameters. This constructor accepts two floating-point values, `a` and `b`, which are assigned to private attributes to define the specific characteristics of the function. The method also ensures proper initialization of the inheritance hierarchy by invoking the superclass constructor before setting the instance state.

        :param a: The first numerical value used to initialize the object's state.
        :type a: float
        :param b: A floating-point value used to initialize the instance.
        :type b: float
        """

        super().__init__()
        self._a: float = a
        self._b: float = b

    def get_a(self) -> float:
        """
        Retrieves the value of the internal attribute `_a`, which represents a specific parameter or coefficient of the crisp function. The method returns this value as a float and does not modify the state of the object. If the internal attribute has not been initialized, the method will raise an AttributeError.

        :return: Returns the value of the attribute `a`.

        :rtype: float
        """

        return self._a

    def get_b(self) -> float:
        """
        Retrieves the value of the internal attribute `_b` associated with the function instance. This method serves as a getter to expose the specific parameter, likely representing a coefficient or offset, without modifying the object's state. The returned value is a floating-point number, assuming the attribute has been initialized during the object's construction.

        :return: The value of the _b attribute.

        :rtype: float
        """

        return self._b

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the `CrispFunction` instance, formatted to resemble a function invocation. The string includes the values of the internal parameters `_k1`, `_k2`, `_a`, and `_b` enclosed in parentheses and prefixed by 'crisp'. This method is intended for display and debugging purposes; it does not modify the object's state and relies on the string representations of the underlying attributes.

        :return: Returns a string representation of the object, displaying the current parameter values.

        :rtype: str
        """

        return f"crisp({self._k1}, {self._k2}, {self._a}, {self._b})"
