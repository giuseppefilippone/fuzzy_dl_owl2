import typing

from fuzzy_dl_owl2.fuzzydl.util import constants
from fuzzy_dl_owl2.fuzzydl.util.constants import ConcreteFeatureType


class ConcreteFeature:
    """
    This class models a specific attribute of an individual, characterized by a name and a data type such as string, boolean, integer, or real. The type is automatically determined during initialization based on the provided arguments: supplying only a name defaults to a string type, passing a boolean flag explicitly sets the type to boolean, and providing numeric bounds (`k1` and `k2`) defines an integer or real range. It supports accessing and modifying the feature's type and numeric boundaries, as well as cloning the instance to create an independent copy.

    :raises ValueError: Raised when the arguments provided during initialization are invalid, such as having an incorrect number of arguments or types that do not match the expected signature for a boolean or numeric feature.
    """


    @typing.overload
    def __init__(self, name: str) -> None: ...

    @typing.overload
    def __init__(self, name: str, is_boolean: bool) -> None: ...

    @typing.overload
    def __init__(self, name: str, k1: int, k2: int) -> None: ...

    @typing.overload
    def __init__(self, name: str, k1: float, k2: float) -> None: ...

    def __init__(self, *args) -> None:
        """
        Initializes the ConcreteFeature instance by delegating to specific internal initialization logic based on the number and types of arguments provided. The first argument must always be a string, serving as the feature's identifier. The constructor supports three distinct signatures: a single string; a string followed by a boolean flag; or a string followed by two numeric values, which must be either integers or specific number constants defined in the module. If the number of arguments is not between one and three, or if the types of the arguments do not conform to these specific patterns, the method raises an assertion error or a ValueError.

        :param args: Variable-length arguments allowing initialization with a string, a string and a boolean, or a string and two numeric values (integers or constants.NUMBER).
        :type args: typing.Any

        :raises ValueError: Raised if the number of arguments is not 1, 2, or 3, or if three arguments are provided but the second and third arguments are not both integers or both of type `constants.NUMBER`.
        """

        assert len(args) in [1, 2, 3]

        assert isinstance(args[0], str)
        if len(args) == 1:
            self.__concrete_feature_init_1(*args)
        elif len(args) == 2:
            assert isinstance(args[1], bool)
            self.__concrete_feature_init_2(*args)
        elif len(args) == 3:
            if isinstance(args[1], int) and isinstance(args[2], int):
                self.__concrete_feature_init_3(*args)
            elif isinstance(args[1], constants.NUMBER) and isinstance(
                args[2], constants.NUMBER
            ):
                self.__concrete_feature_init_4(*args)
            else:
                raise ValueError
        else:
            raise ValueError

    def __concrete_feature_init_1(self, name: str) -> None:
        """
        Initializes the `ConcreteFeature` instance with a specific name and default configuration for range constraints and data type. This method assigns the provided string to the `name` attribute, sets the lower and upper bounds (`k1` and `k2`) to `None`, and explicitly sets the feature type to `ConcreteFeatureType.STRING`. It directly mutates the instance's state, effectively resetting any pre-existing values for the bounds and type, and is intended for use when creating features that do not initially require numeric range definitions.

        :param name: The name of the concrete feature.
        :type name: str
        """

        self.name: str = name
        # Lower bound for the range
        self.k1: typing.Optional[typing.Union[float, int]] = None
        # Upper bound for the range
        self.k2: typing.Optional[typing.Union[float, int]] = None
        self.type: ConcreteFeatureType = ConcreteFeatureType.STRING

    def __concrete_feature_init_2(self, name: str, is_boolean: bool) -> None:
        """
        Initializes the feature instance by delegating the assignment of the feature's name to the primary initialization method, `__concrete_feature_init_1`. This method accepts a string for the name and a boolean flag to determine the feature's data type. If the `is_boolean` flag is set to True, the instance's type attribute is explicitly set to `ConcreteFeatureType.BOOLEAN`; if the flag is False, the type attribute remains in whatever state it was left by the preceding initialization call. This process mutates the instance's state in-place.

        :param name: The name or identifier of the feature.
        :type name: str
        :param is_boolean: Flag indicating whether the feature type should be set to BOOLEAN.
        :type is_boolean: bool
        """

        self.__concrete_feature_init_1(name)
        if is_boolean:
            self.type: ConcreteFeatureType = ConcreteFeatureType.BOOLEAN

    def __concrete_feature_init_3(self, name: str, k1: int, k2: int) -> None:
        """
        Initializes the feature as an integer type defined by a specific range between two bounds. It delegates the assignment of the feature's name to the `__concrete_feature_init_1` method, then sets the `k1` attribute as the lower bound and the `k2` attribute as the upper bound. This method modifies the instance's state by setting the `type` attribute to `ConcreteFeatureType.INTEGER`, though it does not perform validation to ensure that the lower bound is less than the upper bound.

        :param name: The identifier or label for the feature.
        :type name: str
        :param k1: The lower bound for the range.
        :type k1: int
        :param k2: Upper bound for the range.
        :type k2: int
        """

        self.__concrete_feature_init_1(name)
        # Lower bound for the range
        self.k1: typing.Optional[typing.Union[float, int]] = k1
        # Upper bound for the range
        self.k2: typing.Optional[typing.Union[float, int]] = k2
        self.type: ConcreteFeatureType = ConcreteFeatureType.INTEGER

    def __concrete_feature_init_4(self, name: str, k1: float, k2: float) -> None:
        """
        Initializes a concrete feature instance representing a real-valued variable with a specified name and numerical range. The `k1` and `k2` parameters define the lower and upper bounds of the feature's domain, respectively. This method explicitly sets the feature type to `REAL` and delegates the initialization of the name attribute to a separate internal routine.

        :param name: Identifier for the feature.
        :type name: str
        :param k1: The lower bound for the feature's value range.
        :type k1: float
        :param k2: The upper bound for the range.
        :type k2: float
        """

        self.__concrete_feature_init_1(name)
        # Lower bound for the range
        self.k1: typing.Optional[typing.Union[float, int]] = k1
        # Upper bound for the range
        self.k2: typing.Optional[typing.Union[float, int]] = k2
        self.type: ConcreteFeatureType = ConcreteFeatureType.REAL

    def clone(self) -> typing.Self:
        """
        Creates and returns a new instance that duplicates the current object's configuration, ensuring the returned copy is independent of the original. The initialization logic adapts based on the feature's underlying type: boolean features are reconstructed with a specific flag, string features are initialized solely by name, and other types are instantiated using the name along with primary and secondary key values. This method does not modify the state of the existing instance.

        :return: A new instance of the class that is a copy of the current object, preserving its name and type-specific attributes.

        :rtype: typing.Self
        """

        if self.type == ConcreteFeatureType.BOOLEAN:
            return ConcreteFeature(self.name, is_boolean=True)
        elif self.type == ConcreteFeatureType.STRING:
            return ConcreteFeature(self.name)

        return ConcreteFeature(self.name, self.k1, self.k2)

    def get_type(self) -> ConcreteFeatureType:
        """
        Returns the specific type classification associated with the feature instance. This method acts as a simple accessor for the internal `type` attribute, providing the `ConcreteFeatureType` that defines the nature of the object. It does not modify the instance state and has no side effects.

        :return: The concrete feature type associated with the instance.

        :rtype: ConcreteFeatureType
        """

        return self.type

    def set_type(self, new_type: ConcreteFeatureType) -> None:
        """
        Updates the type definition of the feature instance to the specified value, replacing the existing type attribute. This method mutates the object's state by directly assigning the provided `ConcreteFeatureType` to the internal `type` property. It does not return a value and assumes the input is a valid type definition compatible with the feature's schema.

        :param new_type: The concrete feature type to assign to the instance.
        :type new_type: ConcreteFeatureType
        """

        self.type = new_type

    def get_k1(self) -> typing.Optional[typing.Union[float, int]]:
        """
        Returns the current value of the `k1` attribute stored within the instance. The method provides access to a numeric parameter that may be represented as either an integer or a float, or it may return None if the value is undefined or null. Since this is a getter method, it performs no side effects or modifications to the object's internal state.

        :return: The value of the k1 attribute.

        :rtype: typing.Optional[typing.Union[float, int]]
        """

        return self.k1

    def get_k2(self) -> typing.Optional[typing.Union[float, int]]:
        """
        Retrieves the current value of the `k2` attribute associated with the `ConcreteFeature` instance. The returned value can be a numeric type, specifically an integer or a float, depending on how the attribute was originally set. If the attribute is uninitialized or explicitly set to `None`, the method returns `None`. This is a read-only accessor function that does not alter the object's state or produce any side effects.

        :return: The value of the `k2` attribute, which may be an integer, a float, or None.

        :rtype: typing.Optional[typing.Union[float, int]]
        """

        return self.k2

    def set_range(
        self,
        k1: typing.Optional[typing.Union[float, int]],
        k2: typing.Optional[typing.Union[float, int]],
    ) -> None:
        """
        Updates the range boundaries for the feature by assigning the provided values to the instance attributes. The parameters `k1` and `k2` can be integers, floats, or None, allowing for partial or unset range definitions. This method directly mutates the object's state without performing validation on the relative order or magnitude of the inputs.

        :param k1: The starting value or lower bound of the range. Can be a number or None to indicate an unbounded start.
        :type k1: typing.Optional[typing.Union[float, int]]
        :param k2: The upper bound or end value of the range, or None to indicate no upper bound.
        :type k2: typing.Optional[typing.Union[float, int]]
        """

        self.k1 = k1
        self.k2 = k2

    def get_name(self) -> str:
        """
        Returns the name of the feature instance. This method provides direct access to the internal `name` attribute, which serves as the identifier for the feature. It is a read-only operation that does not modify the state of the object, though it will raise an `AttributeError` if the underlying attribute has not been initialized.

        :return: The name associated with the object instance.

        :rtype: str
        """

        return self.name

    def __repr__(self) -> str:
        """
        Returns the official string representation of the instance by delegating to the object's `__str__` method. This implementation ensures that the output of `repr()` is identical to the informal string representation provided by `str()`. Because it relies on `__str__`, the behavior and format of the output are determined by that method, and a failure to define `__str__` could lead to a recursion error.

        :return: A string representation of the object.

        :rtype: str
        """

        return str(self)

    def __str__(self) -> str:
        """
        Returns the informal string representation of the feature instance. This implementation delegates the formatting logic to the `get_name` method, effectively using the feature's name as its primary identifier when converted to a string. It is automatically invoked by the built-in `str()` function and print statements.

        :return: The name of the object.

        :rtype: str
        """

        return self.get_name()
