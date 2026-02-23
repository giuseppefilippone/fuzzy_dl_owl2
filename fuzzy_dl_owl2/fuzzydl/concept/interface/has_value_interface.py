import abc
import copy
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
        Updates the internal state of the instance by assigning a deep copy of the provided argument to the `_value` attribute. This setter accepts any Python object and ensures that subsequent modifications to the original input object do not affect the stored value. Because it relies on `copy.deepcopy`, the operation may be computationally expensive for complex objects and will raise an error if the input cannot be deep-copied.

        :param value: The value to set. A deep copy of this object is stored internally to prevent external mutations from affecting the internal state.
        :type value: typing.Any
        """

        return self._value

    @value.setter
    def value(self, value: typing.Any) -> None:
        self._value = copy.deepcopy(value)
