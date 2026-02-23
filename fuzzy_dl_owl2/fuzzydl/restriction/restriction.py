from __future__ import annotations

import typing

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.degree.degree import Degree


class Restriction:
    """
    This class models a universal restriction within a logical framework, combining a specific role, a target concept, and a lower bound degree to define a constraint. It represents the condition that for all entities connected via the given role, they must belong to the specified concept with a certainty or membership level that meets or exceeds the provided degree. The structure supports cloning and provides string representations that reflect the logical syntax, including a format that explicitly includes the degree threshold.

    :param role_name: The name of the role for which the restriction is defined.
    :type role_name: str
    :param concept: The concept defining the target of the universal restriction.
    :type concept: Concept
    :param degree: The lower bound degree defining the threshold for the restriction.
    :type degree: Degree
    """


    def __init__(self, role_name: str, concept: Concept, degree: Degree) -> None:
        """
        Initializes a new instance representing a constraint or limitation applied to a specific role within a conceptual structure. The constructor stores the provided role name as a string, along with the associated `Concept` and `Degree` objects, directly into the instance attributes. This setup establishes the fundamental relationship between the role, the concept being restricted, and the degree of that restriction, serving as the basis for further semantic processing or validation operations within the module.

        :param role_name: The name or label identifying the specific role.
        :type role_name: str
        :param concept: The specific concept instance associated with the role.
        :type concept: Concept
        :param degree: The intensity or magnitude of the concept associated with the role.
        :type degree: Degree
        """

        self.role_name: str = role_name
        self.concept: Concept = concept
        self.degree: Degree = degree

    def clone(self) -> typing.Self:
        """
        Creates and returns a new instance of the `Restriction` class that duplicates the state of the current object. The new object is initialized with the same `role_name`, `concept`, and `degree` values as the original. This method does not modify the existing instance, providing a way to obtain an independent copy of the restriction for further use or modification.

        :return: A new instance of the class initialized with the same role name, concept, and degree as the current object.

        :rtype: typing.Self
        """

        return Restriction(self.role_name, self.concept, self.degree)

    def get_role_name(self) -> str:
        """
        Retrieves the name of the role associated with this restriction instance. This method acts as a getter for the internal `role_name` attribute, returning its current value without modifying the object's state. The returned value is expected to be a string representing the specific role identifier.

        :return: The name of the role.

        :rtype: str
        """

        return self.role_name

    def get_degree(self) -> Degree:
        """
        Returns the `Degree` object associated with this `Restriction` instance. This method provides access to the internal `degree` attribute, allowing the caller to inspect the specific degree defined by the restriction. As a getter, it performs a read-only operation and does not alter the state of the object.

        :return: The degree associated with the object.

        :rtype: Degree
        """

        return self.degree

    def get_concept(self) -> Concept:
        """
        Returns the `Concept` entity to which this restriction applies. This accessor method provides direct read-only access to the underlying concept attribute without modifying the state of the `Restriction` instance. The returned object represents the specific subject or entity being constrained by the current restriction logic.

        :return: The Concept object associated with this instance.

        :rtype: Concept
        """

        return self.concept

    def get_name_without_degree(self) -> str:
        """
        Constructs and returns a string representation of the restriction that excludes any specific degree or quantifier, defaulting to a universal scope. The output is formatted as a parenthetical statement combining the role name and concept with the prefix 'all', effectively describing the restriction as applying to all instances of the concept for that role.

        :return: A string representing the restriction name without the degree, formatted as '(all {role_name} {concept})'.

        :rtype: str
        """

        return f"(all {self.role_name} {self.concept})"

    def __repr__(self) -> str:
        """
        Returns the string representation of the restriction object by delegating to the `__str__` method. This implementation ensures that the official representation used by the interpreter is identical to the informal string representation, prioritizing human readability over a machine-parseable format. The method does not modify the object's state, though it will propagate any exceptions raised during the string conversion process.

        :return: Returns the string representation of the object.

        :rtype: str
        """

        return str(self)

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the restriction, formatted to display the constraint condition as "name >= degree". This method is primarily used for logging or displaying the object to a user, providing a clear indication of the minimum threshold enforced by the restriction. It relies on the `get_name_without_degree` method to retrieve the identifier and accesses the `degree` attribute directly, ensuring that the output reflects the current state of the object without causing any side effects.

        :return: A string representation of the object in the format 'name >= degree'.

        :rtype: str
        """

        return f"{self.get_name_without_degree()} >= {self.degree}"
