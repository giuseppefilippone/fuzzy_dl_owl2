import typing

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.concept.interface.has_concepts_interface import (
    HasConceptsInterface,
)
from fuzzy_dl_owl2.fuzzydl.concept.operator_concept import (
    And,
    GoedelAnd,
    GoedelOr,
    LukasiewiczOr,
    Not,
    OperatorConcept,
    Or,
)
from fuzzy_dl_owl2.fuzzydl.concept.truth_concept import TruthConcept
from fuzzy_dl_owl2.fuzzydl.util import constants
from fuzzy_dl_owl2.fuzzydl.util.constants import ConceptType, FuzzyLogic
from fuzzy_dl_owl2.fuzzydl.util.util import Util


class ImpliesConcept(Concept, HasConceptsInterface):

    def __init__(self, c_type: ConceptType, concepts: list[Concept]) -> None:
        Concept.__init__(self, c_type)
        HasConceptsInterface.__init__(self, concepts)

        assert c_type in (
            ConceptType.ZADEH_IMPLIES,
            ConceptType.GOEDEL_IMPLIES,
        )

        self.name: str = self.compute_name()

    def clone(self) -> typing.Self:
        return ImpliesConcept(self.type, [c for c in self.concepts])

    @staticmethod
    def lukasiewicz_implies(c1: Concept, c2: Concept) -> Concept:
        if c1.type == ConceptType.TOP:
            return c2
        if c2.type == ConceptType.TOP or c1.type == ConceptType.BOTTOM:
            return TruthConcept.get_top()
        if c2.type == ConceptType.BOTTOM:
            return -c1
        if constants.KNOWLEDGE_BASE_SEMANTICS == FuzzyLogic.CLASSICAL:
            return Or(-c1, c2)
        return LukasiewiczOr(-c1, c2)

    @staticmethod
    def kleene_dienes_implies(c1: Concept, c2: Concept) -> Concept:
        if c1.type == ConceptType.TOP:
            return c2
        if c2.type == ConceptType.TOP or c1.type == ConceptType.BOTTOM:
            return TruthConcept.get_top()
        if constants.KNOWLEDGE_BASE_SEMANTICS == FuzzyLogic.CLASSICAL:
            return Or(-c1, c2)
        return GoedelOr(-c1, c2)

    @staticmethod
    def goedel_implies(c1: Concept, c2: Concept) -> Concept:
        if c1.type == ConceptType.TOP:
            return c2
        if c2.type == ConceptType.TOP or c1.type == ConceptType.BOTTOM:
            return TruthConcept.get_top()
        if constants.KNOWLEDGE_BASE_SEMANTICS == FuzzyLogic.CLASSICAL:
            return Or(-c1, c2)
        if c1.type == ConceptType.GOEDEL_OR:
            return GoedelAnd(
                [GoedelOr(ci, c2) for ci in typing.cast(OperatorConcept, c1).concepts]
            )
        return ImpliesConcept(ConceptType.GOEDEL_IMPLIES, [c1, c2])

    @staticmethod
    def zadeh_implies(c1: Concept, c2: Concept) -> Concept:
        if constants.KNOWLEDGE_BASE_SEMANTICS == FuzzyLogic.CLASSICAL:
            return Or(-c1, c2)
        return ImpliesConcept(ConceptType.ZADEH_IMPLIES, [c1, c2])

    def replace(self, a: Concept, c: Concept) -> Concept:
        c_type: ConceptType = c.type
        if c_type == ConceptType.GOEDEL_IMPLIES:
            return ImpliesConcept.goedel_implies(
                self.concepts[0].replace(a, c), self.concepts[1].replace(a, c)
            )
        elif c_type == ConceptType.NOT_GOEDEL_IMPLIES:
            return Not(
                ImpliesConcept.goedel_implies(
                    self.concepts[0].replace(a, c), self.concepts[1].replace(a, c)
                )
            )
        Util.error(f"Error replacing in concept {self}")

    def compute_name(self) -> typing.Optional[str]:
        if self.type == ConceptType.GOEDEL_IMPLIES:
            return f"(g-implies {self.concepts[0]} {self.concepts[1]})"
        elif self.type == ConceptType.ZADEH_IMPLIES:
            return f"(z-implies {self.concepts[0]} {self.concepts[1]})"

    def compute_atomic_concepts(self) -> set[Concept]:
        result: set[Concept] = set()
        result.update(self.concepts[0].compute_atomic_concepts())
        result.update(self.concepts[1].compute_atomic_concepts())
        return result

    def get_roles(self) -> set[str]:
        return self.concepts[0].get_roles() | self.concepts[1].get_roles()

    def __neg__(self) -> Concept:
        return Not(self)

    def __and__(self, value: typing.Self) -> typing.Self:
        return And(self, value)

    def __or__(self, value: typing.Self) -> typing.Self:
        return Or(self, value)

    def __hash__(self) -> int:
        return hash(str(self))

    def __eq__(self, value: typing.Self) -> bool:
        return isinstance(value, ImpliesConcept) and str(self) == str(value)


# class ZadehImplies(ImpliesConcept):
#     def implies(self, c: Concept) -> typing.Self:
#         return ImpliesConcept.zadeh_implies(self, c)


# class GoedelImplies(ImpliesConcept):
#     def implies(self, c: Concept) -> typing.Self:
#         return ImpliesConcept.goedel_implies(self, c)


# class LukasiewiczImplies(ImpliesConcept):
#     def implies(self, c: Concept) -> typing.Self:
#         return ImpliesConcept.lukasiewicz_implies(self, c)


# class KleeneDienesImplies(ImpliesConcept):
#     def implies(self, c: Concept) -> typing.Self:
#         return ImpliesConcept.kleene_dienes_implies(self, c)

ZadehImplies = ImpliesConcept.zadeh_implies
GoedelImplies = ImpliesConcept.goedel_implies
LukasiewiczImplies = ImpliesConcept.lukasiewicz_implies
KleeneDienesImplies = ImpliesConcept.kleene_dienes_implies
