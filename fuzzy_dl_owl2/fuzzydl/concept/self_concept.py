import typing

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.concept.interface.has_role_interface import HasRoleInterface
from fuzzy_dl_owl2.fuzzydl.concept.operator_concept import OperatorConcept
from fuzzy_dl_owl2.fuzzydl.util.constants import ConceptType


class SelfConcept(Concept, HasRoleInterface):

    def __init__(self, role: str) -> None:
        Concept.__init__(self, ConceptType.SELF)
        HasRoleInterface.__init__(self, role)
        self.name = self.compute_name()

    @staticmethod
    def self(role: str) -> typing.Self:
        return SelfConcept(role)

    def clone(self):
        return SelfConcept(self.role)

    def replace(self, a: Concept, c: Concept) -> Concept:
        return self

    def compute_name(self) -> typing.Optional[str]:
        return f"(self {self.role})"

    def compute_atomic_concepts(self) -> set[Concept]:
        return set([self])

    def get_roles(self) -> set[str]:
        return set([self.role])

    def __neg__(self) -> Concept:
        return OperatorConcept.not_(self)

    def __and__(self, value: typing.Self) -> typing.Self:
        return OperatorConcept.and_(self, value)

    def __or__(self, value: typing.Self) -> typing.Self:
        return OperatorConcept.or_(self, value)

    def __hash__(self) -> int:
        return hash(str(self))
