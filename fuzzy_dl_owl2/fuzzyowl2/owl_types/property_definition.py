class PropertyDefinition:
    """
    Encapsulates a property name alongside its corresponding fuzzy modifier, serving as a fundamental building block for defining fuzzy logic constraints within the FuzzyOWL2 ontology framework. By storing these two elements together, it allows for the precise application of linguistic hedges or truth values to specific object or data properties. Users should instantiate this object by providing the modifier and property strings, and subsequently access the stored values via the dedicated getter methods to construct complex fuzzy axioms.

    :param _mod: The fuzzy modifier associated with the property definition.
    :type _mod: str
    :param _prop: The name of the property being defined.
    :type _prop: str
    """


    def __init__(self, mod: str, prop: str) -> None:
        """
        Initializes a new instance representing a specific property definition within a module. The constructor accepts two string arguments, `mod` and `prop`, which are assigned to internal attributes to define the module and property identifiers respectively. This method performs no validation or side effects beyond storing the provided values.

        :param mod: The name of the module.
        :type mod: str
        :param prop: The name of the property.
        :type prop: str
        """

        self._mod: str = mod
        self._prop: str = prop

    def get_fuzzy_modifier(self) -> str:
        """
        Retrieves the specific string modifier used to define the fuzzy matching behavior for this property. This value is stored internally and determines how lenient or strict comparisons involving this property should be interpreted.

        :return: The string representing the fuzzy modifier.

        :rtype: str
        """

        return self._mod

    def get_property(self) -> str:
        """
        Returns the string value associated with this property definition. This method provides access to the internal `_prop` attribute, allowing the retrieval of the property's identifier or value without modifying the object's state. Since it directly accesses an internal attribute, it assumes the attribute has been properly initialized during object creation.

        :return: The value of the property.

        :rtype: str
        """

        return self._prop
