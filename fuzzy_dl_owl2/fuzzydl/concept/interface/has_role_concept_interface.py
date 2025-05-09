import abc

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.concept.interface.has_concept_interface import (
    HasConceptInterface,
)
from fuzzy_dl_owl2.fuzzydl.concept.interface.has_role_interface import HasRoleInterface


class HasRoleConceptInterface(HasRoleInterface, HasConceptInterface, abc.ABC):

    def __init__(self, role: str, concept: Concept) -> None:
        HasRoleInterface.__init__(self, role)
        HasConceptInterface.__init__(self, concept)
