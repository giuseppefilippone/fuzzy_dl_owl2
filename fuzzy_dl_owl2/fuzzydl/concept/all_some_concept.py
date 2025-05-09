import typing

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.concept.interface.has_role_concept_interface import (
    HasRoleConceptInterface,
)
from fuzzy_dl_owl2.fuzzydl.concept.truth_concept import TruthConcept
from fuzzy_dl_owl2.fuzzydl.util.config_reader import ConfigReader
from fuzzy_dl_owl2.fuzzydl.util.constants import ConceptType


class AllSomeConcept(Concept, HasRoleConceptInterface):

    def __init__(self, role: str, c: Concept, c_type: ConceptType) -> None:
        Concept.__init__(self, c_type)
        HasRoleConceptInterface.__init__(self, role, c)

        assert c_type in (ConceptType.ALL, ConceptType.SOME)
        self._name: str = self.compute_name()

    @staticmethod
    def new(c_type: ConceptType, role: str, concept: Concept) -> typing.Self:
        if c_type == ConceptType.SOME:
            if ConfigReader.OPTIMIZATIONS != 0 and concept.type == ConceptType.BOTTOM:
                return TruthConcept.get_bottom()
        else:
            if ConfigReader.OPTIMIZATIONS != 0 and concept.type == ConceptType.TOP:
                return TruthConcept.get_top()
        return AllSomeConcept(role, concept, c_type)

    @staticmethod
    def all(role: str, concept: Concept) -> typing.Self:
        return AllSomeConcept.new(ConceptType.ALL, role, concept)

    @staticmethod
    def some(role: str, concept: Concept) -> typing.Self:
        return AllSomeConcept.new(ConceptType.SOME, role, concept)

    def clone(self) -> typing.Self:
        return AllSomeConcept.new(self.type, self.role, self.curr_concept)

    def replace(self, a: Concept, c: Concept) -> Concept:
        return AllSomeConcept.new(self.type, self.role, self.curr_concept.replace(a, c))

    def get_atoms(self) -> list[typing.Self]:
        return self.curr_concept.get_atoms()

    def is_complemented_atomic(self) -> bool:
        return False

    def compute_name(self) -> str:
        if self.type == ConceptType.ALL:
            return f"(all {self.role} {self.curr_concept})"
        else:
            return f"(some {self.role} {self.curr_concept})"

    def compute_atomic_concepts(self) -> set[Concept]:
        return self.curr_concept.compute_atomic_concepts()

    def get_roles(self) -> set[str]:
        return set([self.role]) | self.curr_concept.get_roles()

    def __neg__(self) -> Concept:
        return AllSomeConcept.new(
            ConceptType.ALL if self.type == ConceptType.SOME else ConceptType.SOME,
            self.role,
            -self.curr_concept,
        )

    def __hash__(self) -> int:
        return hash(str(self))


# class AllConcept(AllSomeConcept):
#     def __call__(self, *args) -> typing.Self:
#         return AllSomeConcept.all(args)


# class SomeConcept(AllSomeConcept):
#     def __call__(self, *args) -> typing.Self:
#         return AllSomeConcept.some(args)


All = AllSomeConcept.all
Some = AllSomeConcept.some
