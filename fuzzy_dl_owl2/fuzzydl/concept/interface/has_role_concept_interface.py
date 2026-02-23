import abc

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.concept.interface.has_concept_interface import (
    HasConceptInterface,
)
from fuzzy_dl_owl2.fuzzydl.concept.interface.has_role_interface import HasRoleInterface


class HasRoleConceptInterface(HasRoleInterface, HasConceptInterface, abc.ABC):

    """This abstract base class defines a contract for objects that must manage both a functional role and a specific concept. It combines the behaviors of role and concept handling, requiring implementations to provide properties for getting and setting a string-based role and a `Concept` object. This design allows for dynamic modification of the operational context and the associated domain entity, ensuring that the class can flexibly adapt to changes in the role it performs or the concept it represents."""


    def __init__(self, role: str, concept: Concept) -> None:
        """
        Initializes the instance by delegating to the parent interfaces for role and concept assignment. It accepts a string defining the role and a Concept object representing the concept, invoking the initialization logic of `HasRoleInterface` and `HasConceptInterface` respectively. This method ensures that the instance is configured with both attributes, relying on the parent classes to handle the specific storage and validation of the provided values.

        :param role: The specific role or capacity assigned to this instance.
        :type role: str
        :param concept: The concept entity to be associated with the object.
        :type concept: Concept
        """

        HasRoleInterface.__init__(self, role)
        HasConceptInterface.__init__(self, concept)
