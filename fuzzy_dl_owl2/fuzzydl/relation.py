from __future__ import annotations

import typing

if typing.TYPE_CHECKING:
    from fuzzy_dl_owl2.fuzzydl.degree.degree import Degree
    from fuzzy_dl_owl2.fuzzydl.individual.individual import Individual


class Relation:
    """
    This class models a role assertion connecting a subject individual to an object individual via a specific role, constrained by a lower bound degree. It serves as a container for the relationship's properties, storing the role name, the two involved individuals, and the minimum degree required for the assertion to hold. Users can instantiate this object to define such relationships, modify the subject or object individuals after creation, and retrieve string representations that include or exclude the degree constraint. Additionally, the class supports cloning to create independent copies of the assertion.

    :param role_name: The name identifying the specific role or relationship type asserted between the subject and object individuals.
    :type role_name: str
    :param ind_a: The subject individual of the role assertion.
    :type ind_a: Individual
    :param ind_b: The object individual of the role assertion.
    :type ind_b: Individual
    :param degree: The lower bound value for the role assertion.
    :type degree: Degree
    """


    def __init__(
        self, role_name: str, ind1: Individual, ind2: Individual, degree: Degree
    ):
        """
        Initializes a new instance representing a connection between two entities, defined by a specific role and a degree of intensity. The method accepts a string describing the relationship, two `Individual` objects representing the parties involved, and a `Degree` value to classify the bond. It assigns the first individual to the `ind_a` attribute and the second to `ind_b`, strictly preserving the order of the arguments provided. This constructor sets the internal state of the object but does not perform validation on the inputs or modify the `Individual` instances themselves.

        :param role_name: The name or label of the role.
        :type role_name: str
        :param ind1: The first individual involved in the relationship.
        :type ind1: Individual
        :param ind2: The second individual involved in the relationship.
        :type ind2: Individual
        :param degree: The degree of the relationship between the two individuals.
        :type degree: Degree
        """

        self.role_name: str = role_name
        self.ind_a: Individual = ind1
        self.ind_b: Individual = ind2
        self.degree: Degree = degree

    def clone(self) -> typing.Self:
        """
        Creates and returns a distinct copy of the current Relation instance. This method instantiates a new Relation object using the current values of role_name, ind_a, ind_b, and degree, ensuring that the original object remains unmodified. The returned object is a separate entity, though it shares the same attribute values as the source at the moment of cloning.

        :return: A new instance of the class with identical attributes to the current object.

        :rtype: typing.Self
        """

        return Relation(self.role_name, self.ind_a, self.ind_b, self.degree)

    def get_subject_individual(self) -> Individual:
        """
        Retrieves the individual entity that serves as the subject of this relation. This method returns the internal attribute `ind_a`, representing the source node or the first participant in the relationship. Since it returns a direct reference to the stored object, any modifications made to the returned instance will be reflected within the relation, and the method may raise an AttributeError if the relation has not been properly initialized.

        :return: The Individual object representing the subject.

        :rtype: Individual
        """

        return self.ind_a

    def get_object_individual(self) -> Individual:
        """
        Returns the `Individual` instance that serves as the object of this relation. This method retrieves the target entity involved in the binary link, corresponding to the internal attribute `ind_b`. The operation is read-only and does not modify the state of the relation or the returned individual.

        :return: The Individual instance stored in the object.

        :rtype: Individual
        """

        return self.ind_b

    def set_object_individual(self, ind: Individual) -> None:
        """
        Updates the object of the relation by assigning the provided Individual instance to the internal attribute `ind_b`. This operation mutates the state of the Relation object, replacing any existing object individual with the new value. The method returns None and does not enforce type constraints at runtime, assuming the provided argument adheres to the Individual type hint.

        :param ind: 
        :type ind: Individual
        """

        self.ind_b = ind

    def set_subject_individual(self, ind: Individual) -> None:
        """
        Assigns the provided `Individual` instance as the subject of the relation by updating the internal attribute `ind_a`. This method modifies the state of the object in place, overwriting any existing subject reference without performing additional validation or side effects on the input object. The operation returns `None`.

        :param ind: The individual to be assigned as the subject.
        :type ind: Individual
        """

        self.ind_a = ind

    def get_role_name(self) -> str:
        """
        Retrieves the name of the role associated with this relation instance. This method provides read access to the internal `role_name` attribute, which typically identifies the specific function or label of the entity within the relationship. It performs no modification of the object's state and will return the exact string value stored, or raise an `AttributeError` if the attribute has not been initialized.

        :return: The name of the role.

        :rtype: str
        """

        return self.role_name

    def get_degree(self) -> Degree:
        """
        Retrieves the degree associated with this relation instance. This method serves as an accessor for the internal `degree` attribute, returning the stored `Degree` object. It performs no modifications to the object's state and has no side effects.

        :return: The degree associated with the instance.

        :rtype: Degree
        """

        return self.degree

    def get_name_without_degree(self) -> str:
        """
        Generates a human-readable string representation of the relation that omits any degree or lower bound information. The returned string is formatted as '(individual_a, individual_b): role_name', incorporating the identifiers of the two entities involved and the name of the role connecting them. This method performs no modifications to the object's state and relies on the existence of the `ind_a`, `ind_b`, and `role_name` attributes.

        :return: A string representation of the role assertion formatted as "(individual_a, individual_b): role_name", excluding the lower bound.

        :rtype: str
        """

        return f"({self.ind_a}, {self.ind_b}): {self.role_name}"

    def __repr__(self) -> str:
        """
        Returns the official string representation of the instance by delegating to the object's informal string conversion method. This ensures that the output displayed in interactive sessions or logs is identical to the result of calling `str()` on the object. Since it relies on the underlying string conversion logic, any exceptions raised during that process will propagate through this method.

        :return: The string representation of the object.

        :rtype: str
        """

        return str(self)

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the relation, formatted as 'name >= degree'. The name component is retrieved by calling `get_name_without_degree`, while the degree component is taken directly from the object's degree attribute. This method is automatically invoked by the `str()` built-in function and the `print` statement to provide a concise summary of the relation's constraint.

        :return: A string representation of the object in the format "name >= degree".

        :rtype: str
        """

        return f"{self.get_name_without_degree()} >= {self.degree}"
