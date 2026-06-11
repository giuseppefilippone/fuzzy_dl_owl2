# import copy
import abc
import typing

from fuzzy_dl_owl2.fuzzydl.concept.interface.has_role_interface import HasRoleInterface


class HasValueInterface(HasRoleInterface, abc.ABC):
    """
    This abstract base class extends role management capabilities by introducing a mechanism to handle a generic value alongside a role. It provides concrete implementations for initializing and accessing the value, with the setter specifically utilizing a deep copy operation to ensure that the internal state remains isolated from external modifications. By combining role and value attributes, it offers a consistent interface for objects that need to represent or manipulate specific data within a defined context.

    :param _value: Internal storage for the value represented by the class, managed via the public property and stored as a deep copy to prevent external mutation.
    :type _value: typing.Any
    """

    def __init__(self, role: str, value: typing.Any) -> None:
        """
        Initializes the instance by associating a specific role with an arbitrary value. The method delegates the handling of the role to the parent class constructor via a super call, ensuring consistent initialization behavior across the inheritance hierarchy. It then stores the provided value in a private instance attribute, allowing the object to encapsulate data of any type alongside its designated role.

        :param role: The role of the instance, passed to the superclass for initialization.
        :type role: str
        :param value:
        :type value: typing.Any
        """

        super().__init__(role)

        self._value: typing.Any = value

    @property
    def value(self) -> typing.Any:
        """
        Retrieves the current value stored in the instance. This getter provides access to the internal `_value` attribute without creating a copy, meaning that modifications to the returned object will affect the internal state if the object is mutable.

        :return: The value currently stored in the instance.
        :rtype: typing.Any
        """

        return self._value

    @value.setter
    def value(self, value: typing.Any) -> None:
        """
        Sets the filler value carried by this concept (for example, the individual of a value restriction or the data value of a datatype filler). The provided value is stored directly in the private ``_value`` attribute by reference, without copying or validation.

        :param value: The new value to store.
        :type value: typing.Any
        """

        # self._value = copy.deepcopy(value)
        self._value = value
