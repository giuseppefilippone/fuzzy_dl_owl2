from fuzzy_dl_owl2.fuzzyowl2.owl_types.fuzzy_modifier import FuzzyModifier


class LinearModifier(FuzzyModifier):
    """
    Represents a specific type of fuzzy logic modifier that applies a linear transformation, typically used to scale or adjust membership degrees within the FuzzyOWL2 framework. To utilize this entity, instantiate it with a floating-point value that serves as the coefficient for the linear operation. Once instantiated, the coefficient can be retrieved using the provided accessor method, and the object provides a string representation indicating its type and value.

    :param _c: The numeric coefficient defining the linear transformation applied by the modifier.
    :type _c: float
    """


    def __init__(self, c: float) -> None:
        """
        Initializes a new instance of the LinearModifier class, configuring it with a specific coefficient for linear transformations. The method accepts a float value, `c`, which is stored internally as a private attribute `_c` to define the scaling factor or constant offset applied by this modifier. It also ensures the parent class is properly initialized by calling its constructor. While the type hint expects a float, passing non-numeric types may result in runtime errors when the modifier is applied to data.

        :param c: The floating-point value used to initialize the instance.
        :type c: float
        """

        super().__init__()
        self._c: float = c

    def get_c(self) -> float:
        """
        Retrieves the constant term 'c' currently stored in the linear modifier. This method returns the value of the private attribute `_c` as a floating-point number. It is a read-only operation that does not modify the object's state or have any side effects.

        :return: The value of the internal attribute `_c`.

        :rtype: float
        """

        return self._c

    def __str__(self) -> str:
        """
        Returns the informal string representation of the `LinearModifier` instance, which is intended to be readable and concise. The output is formatted as "linear-modifier({c})", where {c} represents the string conversion of the internal coefficient stored in `_c`. This method does not alter the state of the object and is implicitly called by the built-in `str()` function and print operations.

        :return: A string representation of the linear modifier, formatted as 'linear-modifier(c)' where c is the coefficient.

        :rtype: str
        """

        return f"linear-modifier({self._c})"
