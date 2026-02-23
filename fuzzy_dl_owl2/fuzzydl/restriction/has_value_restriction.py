from __future__ import annotations

from fuzzy_dl_owl2.fuzzydl.degree.degree import Degree
from fuzzy_dl_owl2.fuzzydl.restriction.restriction import Restriction


class HasValueRestriction(Restriction):
    """
    This class models a universal restriction that links a specific role to a particular individual, constrained by a lower bound degree. It is designed to represent logical constraints where a role must be associated with a specific entity, often within the context of fuzzy description logics. To use this class, instantiate it with a string representing the role name, a string for the individual name, and a `Degree` object that defines the lower bound. The class allows retrieval of the individual name via the `get_individual` method and offers a string representation of the restriction's logical structure—specifically a negated existential quantification—through the `get_name_without_degree` method.

    :param ind_name: The name of the individual involved in the restriction.
    :type ind_name: str
    """


    def __init__(self, role_name: str, individual: str, degree: Degree) -> None:
        """
        Initializes a restriction object that enforces a specific value for a given role. It accepts the name of the role to be restricted, the identifier of the individual that serves as the value, and a `Degree` object that qualifies the restriction. During initialization, the method calls the parent class constructor, passing `None` in place of a concept filler, and assigns the provided individual identifier to the `ind_name` attribute.

        :param role_name: The name or title of the role.
        :type role_name: str
        :param individual: The name of the individual associated with this role.
        :type individual: str
        :param degree: The degree or level associated with the role.
        :type degree: Degree
        """

        super().__init__(role_name, None, degree)
        self.ind_name: str = individual

    def get_individual(self) -> str:
        """
        Returns the specific individual name associated with the restriction instance. This method acts as a getter for the internal `ind_name` attribute, providing access to the identifier of the entity being restricted. Since it simply returns the stored value, it does not modify the object's state or have side effects, though the returned value depends entirely on how the instance was initialized or modified prior to this call.

        :return: The name of the individual.

        :rtype: str
        """

        return self.ind_name

    def get_name_without_degree(self) -> str:
        """
        Generates a string representation of the restriction formatted as a negated existential assertion. It constructs this string using the instance's role name and individual name to produce a logical expression equivalent to stating that the specified role does not have the specified individual as a value. The returned string follows the specific syntax '(not (b-some ...))', which is used to define the constraint in the underlying system.

        :return: Returns a string formatted as a negated 'b-some' expression involving the role and individual.

        :rtype: str
        """

        return f"(not (b-some {self.role_name} {self.ind_name}))"
