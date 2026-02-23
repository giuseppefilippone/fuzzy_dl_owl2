from fuzzy_dl_owl2.fuzzyowl2.owl_types.fuzzy_property import FuzzyProperty


class ModifiedProperty(FuzzyProperty):
    """
    This class models a property within the FuzzyOWL2 framework that has been subjected to a fuzzy modification, effectively combining a standard property with a linguistic hedge or modifier. It extends the base `FuzzyProperty` to allow for the representation of nuanced relationships where the property's truth value is altered by a specific factor, such as "very" or "somewhat." To use this class, instantiate it by providing the fuzzy modifier as a string and the name of the property to be modified. The resulting object stores these values and offers methods to retrieve the specific modifier and the underlying property, while its string representation formats the pair as a parenthesized tuple.

    :param _mod: The fuzzy modifier applied to the property.
    :type _mod: str
    :param _prop: The name of the underlying property to which the fuzzy modifier is applied.
    :type _prop: str
    """


    def __init__(self, mod: str, prop: str) -> None:
        """
        Initializes a new instance of the ModifiedProperty class by accepting a module name and a property name as string arguments. This constructor invokes the parent class's initialization method to ensure proper setup of the inheritance hierarchy before storing the provided arguments. The `mod` and `prop` values are assigned to the private instance attributes `_mod` and `_prop` respectively, making them available for subsequent operations. No validation or transformation is applied to the input strings during this process.

        :param mod: The name of the module.
        :type mod: str
        :param prop: The name of the property.
        :type prop: str
        """

        super().__init__()
        self._mod: str = mod
        self._prop: str = prop

    def get_fuzzy_modifier(self) -> str:
        """
        Retrieves the fuzzy modifier string associated with this property instance. This method serves as a getter for the internal `_mod` attribute, returning the value that defines the specific modification or matching rule applied to the property. As a read-only operation, it has no side effects on the object's state, though it may raise an `AttributeError` if the underlying attribute has not been initialized.

        :return: The string representing the fuzzy modifier.

        :rtype: str
        """

        return self._mod

    def get_property(self) -> str:
        """
        Retrieves the value stored in the internal `_prop` attribute. This method acts as a simple accessor to expose the underlying property data without modifying the state of the instance. It assumes the internal attribute has been initialized; otherwise, an `AttributeError` will be raised.

        :return: The value of the internal property.

        :rtype: str
        """

        return self._prop

    def __repr__(self) -> str:
        """
        Returns the official string representation of the object by delegating to the informal string conversion method. This implementation invokes `str(self)`, ensuring that the output matches the result of the `__str__` method rather than providing a distinct, machine-parseable representation. Consequently, the returned value is primarily intended for display purposes and may not be sufficient to reconstruct the object instance.

        :return: The string representation of the object.

        :rtype: str
        """

        return str(self)

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the object, formatted as a parenthesized pair containing the fuzzy modifier followed by the property. This method is invoked automatically by the print function and string conversion operations, relying on the current state of the instance without modifying any internal data. The specific values displayed are determined by calling the respective getter methods for the fuzzy modifier and the property.

        :return: A string representation of the object in the format "(fuzzy_modifier property)".

        :rtype: str
        """

        return f"({self.get_fuzzy_modifier()} {self.get_property()})"
