from fuzzy_dl_owl2.fuzzyowl2.owl_types.fuzzy_datatype import FuzzyDatatype


class ModifiedFunction(FuzzyDatatype):
    """
    This class models a modified function within the FuzzyOWL2 framework, representing a fuzzy datatype that has been transformed by a specific linguistic modifier. It extends the base fuzzy datatype functionality by associating a standard datatype with a modifier string, allowing for the representation of nuanced fuzzy concepts where a base property is altered by terms such as "very" or "somewhat." To utilize this class, instantiate it with the desired modifier and the name of the target datatype; the resulting object provides access to these components through getter methods and generates a string representation formatted as a parenthesized pair.

    :param _mod: The fuzzy modifier or linguistic hedge applied to the underlying datatype.
    :type _mod: str
    :param _d: The name of the datatype to which the fuzzy modifier is applied.
    :type _d: str
    """


    def __init__(self, mod: str, d: str) -> None:
        """
        Initializes a new instance of the ModifiedFunction class by accepting two string parameters, `mod` and `d`. This method ensures that the parent class is properly initialized via a call to `super().__init__()` before storing the provided arguments in private instance attributes named `_mod` and `_d`. While the type hints suggest strings, the method will store any object passed to it, making these values available for subsequent operations within the instance.

        :param mod: The name of the module.
        :type mod: str
        :param d: The value to be stored as the instance's internal `_d` attribute.
        :type d: str
        """

        super().__init__()
        self._mod: str = mod
        self._d: str = d

    def get_mod(self) -> str:
        """
        Retrieves the value of the internal `_mod` attribute, which represents the modification context or module name associated with the function instance. This method serves as a simple accessor, returning the stored string without modifying the object's state. If the underlying attribute has not been initialized, an `AttributeError` will be raised.

        :return: The current value of the `_mod` attribute.

        :rtype: str
        """

        return self._mod

    def get_d(self) -> str:
        """
        Retrieves the value of the internal attribute `_d` stored within the instance. This method serves as an accessor to expose the encapsulated data without modifying the object's state. It returns the value as a string, though an `AttributeError` will be raised if the attribute has not been initialized.

        :return: The value of the _d attribute.

        :rtype: str
        """

        return self._d

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the object, formatted as a parenthesized tuple containing the internal modifier and data attributes separated by a space. This method is invoked implicitly by the `str()` built-in function and the `print` statement, providing a concise summary of the object's state without modifying it. The output depends entirely on the string conversion of the underlying `_mod` and `_d` attributes, meaning any exceptions raised during their stringification will propagate to this call.

        :return: A string representation of the object, formatted as '(_mod _d)'.

        :rtype: str
        """

        return f"({self._mod} {self._d})"