import abc
import typing


class HasRoleInterface(abc.ABC):
    """
    This abstract base class provides a standard implementation for managing a role attribute, designed to be inherited by classes that need to track a specific context or function. It initializes with a string representing the role and exposes this value through getter and setter properties, enabling the role to be accessed or dynamically modified throughout the object's lifecycle. By integrating this component, classes gain a consistent mechanism for handling role-based state without needing to implement the logic themselves.

    :param _role: Internal storage for the current role that the class is working with or representing.
    :type _role: str
    """


    def __init__(self, role: str) -> None:
        """
        Initializes a new instance of the `HasRoleInterface` with the specified role string. The provided value is stored in a private attribute `_role`, establishing the object's state regarding its designated function or permission level. This constructor does not perform validation on the input type at runtime, meaning any object passed as `role` will be assigned to the internal variable regardless of the type hint.

        :param role: The role assigned to the instance.
        :type role: str
        """

        self._role: str = role

    @property
    def role(self) -> str:
        """
        Returns the name of the role (binary relation) associated with this concept, such as the role quantified over by an existential or universal restriction. The value is read from the private ``_role`` attribute without modifying the instance.

        :return: The associated role name.

        :rtype: str
        """

        return self._role

    @role.setter
    def role(self, value: str) -> None:
        """
        Sets the name of the role associated with this concept, replacing the previously stored value. The provided value is stored directly in the private ``_role`` attribute without validation.

        :param value: The new role name.
        :type value: str
        """

        self._role = value
