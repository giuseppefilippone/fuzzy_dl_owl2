import typing

from fuzzy_dl_owl2.fuzzydl.concept.all_some_concept import AllSomeConcept
from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.concept.interface.has_role_concept_interface import (
    HasRoleConceptInterface,
)
from fuzzy_dl_owl2.fuzzydl.concept.operator_concept import OperatorConcept
from fuzzy_dl_owl2.fuzzydl.util.constants import ConceptType


class ApproximationConcept(Concept, HasRoleConceptInterface):

    INVERSE_APPROXIMATION: dict[ConceptType, ConceptType] = {
        k: v
        for k, v in zip(
            [
                ConceptType.LOWER_APPROX,
                ConceptType.TIGHT_LOWER_APPROX,
                ConceptType.LOOSE_LOWER_APPROX,
                ConceptType.UPPER_APPROX,
                ConceptType.TIGHT_UPPER_APPROX,
                ConceptType.LOOSE_UPPER_APPROX,
            ],
            [
                ConceptType.UPPER_APPROX,
                ConceptType.TIGHT_UPPER_APPROX,
                ConceptType.LOOSE_UPPER_APPROX,
                ConceptType.LOWER_APPROX,
                ConceptType.TIGHT_LOWER_APPROX,
                ConceptType.LOOSE_LOWER_APPROX,
            ],
        )
    }

    def __init__(self, c_type: ConceptType, role: str, c: Concept) -> None:
        Concept.__init__(self, c_type)
        HasRoleConceptInterface.__init__(self, role, c)

        assert c_type in (
            ConceptType.LOWER_APPROX,
            ConceptType.TIGHT_LOWER_APPROX,
            ConceptType.LOOSE_LOWER_APPROX,
            ConceptType.UPPER_APPROX,
            ConceptType.TIGHT_UPPER_APPROX,
            ConceptType.LOOSE_UPPER_APPROX,
        )

        self.name = self.compute_name()

    @staticmethod
    def lower_approx(role: str, c: Concept) -> typing.Self:
        return ApproximationConcept(ConceptType.LOWER_APPROX, role, c)

    @staticmethod
    def loose_lower_approx(role: str, c: Concept) -> typing.Self:
        return ApproximationConcept(ConceptType.LOOSE_LOWER_APPROX, role, c)

    @staticmethod
    def tight_lower_approx(role: str, c: Concept) -> typing.Self:
        return ApproximationConcept(ConceptType.TIGHT_LOWER_APPROX, role, c)

    @staticmethod
    def upper_approx(role: str, c: Concept) -> typing.Self:
        return ApproximationConcept(ConceptType.UPPER_APPROX, role, c)

    @staticmethod
    def loose_upper_approx(role: str, c: Concept) -> typing.Self:
        return ApproximationConcept(ConceptType.LOOSE_UPPER_APPROX, role, c)

    @staticmethod
    def tight_upper_approx(role: str, c: Concept) -> typing.Self:
        return ApproximationConcept(ConceptType.TIGHT_UPPER_APPROX, role, c)

    def to_all_some_concept(self) -> AllSomeConcept:
        if self.type == ConceptType.LOWER_APPROX:
            return AllSomeConcept.all(self.role, self.curr_concept)
        if self.type == ConceptType.TIGHT_LOWER_APPROX:
            return AllSomeConcept.all(
                self.role, AllSomeConcept.all(self.role, self.curr_concept)
            )
        if self.type == ConceptType.LOOSE_LOWER_APPROX:
            return AllSomeConcept.some(
                self.role, AllSomeConcept.all(self.role, self.curr_concept)
            )
        if self.type == ConceptType.UPPER_APPROX:
            return AllSomeConcept.some(self.role, self.curr_concept)
        if self.type == ConceptType.TIGHT_UPPER_APPROX:
            return AllSomeConcept.all(
                self.role, AllSomeConcept.some(self.role, self.curr_concept)
            )
        if self.type == ConceptType.LOOSE_UPPER_APPROX:
            return AllSomeConcept.some(
                self.role, AllSomeConcept.some(self.role, self.curr_concept)
            )
        raise ValueError

    def clone(self) -> typing.Self:
        return ApproximationConcept(self.type, self.role, self.curr_concept)

    def replace(self, a: Concept, c: Concept) -> Concept:
        if isinstance(c, ApproximationConcept):
            c_type: ConceptType = c.type
            if c_type == ConceptType.LOWER_APPROX:
                return ApproximationConcept.lower_approx(
                    self.role, self.curr_concept.replace(a, c)
                )
            elif c_type == ConceptType.LOOSE_LOWER_APPROX:
                return ApproximationConcept.loose_lower_approx(
                    self.role, self.curr_concept.replace(a, c)
                )
            elif c_type == ConceptType.TIGHT_LOWER_APPROX:
                return ApproximationConcept.tight_lower_approx(
                    self.role, self.curr_concept.replace(a, c)
                )
            elif c_type == ConceptType.UPPER_APPROX:
                return ApproximationConcept.upper_approx(
                    self.role, self.curr_concept.replace(a, c)
                )
            elif c_type == ConceptType.LOOSE_UPPER_APPROX:
                return ApproximationConcept.loose_upper_approx(
                    self.role, self.curr_concept.replace(a, c)
                )
            elif c_type == ConceptType.TIGHT_UPPER_APPROX:
                return ApproximationConcept.tight_upper_approx(
                    self.role, self.curr_concept.replace(a, c)
                )

    def compute_name(self) -> typing.Optional[str]:
        if self.type == ConceptType.LOWER_APPROX:
            return f"(la {self.role} {self.curr_concept})"
        elif self.type == ConceptType.LOOSE_UPPER_APPROX:
            return f"(lua {self.role} {self.curr_concept})"
        elif self.type == ConceptType.LOOSE_LOWER_APPROX:
            return f"(lla {self.role} {self.curr_concept})"
        elif self.type == ConceptType.UPPER_APPROX:
            return f"(ua {self.role} {self.curr_concept})"
        elif self.type == ConceptType.TIGHT_UPPER_APPROX:
            return f"(tua {self.role} {self.curr_concept})"
        elif self.type == ConceptType.TIGHT_LOWER_APPROX:
            return f"(tla {self.role} {self.curr_concept})"
        raise ValueError

    def compute_atomic_concepts(self) -> set[Concept]:
        return self.curr_concept.compute_atomic_concepts()

    def get_roles(self) -> set[str]:
        return set([self.role]) | self.curr_concept.get_roles()

    def __neg__(self) -> Concept:
        return ApproximationConcept(
            ApproximationConcept.INVERSE_APPROXIMATION[self.type],
            self.role,
            -self.curr_concept,
        )

    def __and__(self, value: typing.Self) -> typing.Self:
        return OperatorConcept.and_(self, value)

    def __or__(self, value: typing.Self) -> typing.Self:
        return OperatorConcept.or_(self, value)

    def __hash__(self) -> int:
        return hash(str(self))


LowerApprox = ApproximationConcept.lower_approx
LooseLowerApprox = ApproximationConcept.loose_lower_approx
TightLowerApprox = ApproximationConcept.tight_lower_approx
UpperApprox = ApproximationConcept.upper_approx
LooseUpperApprox = ApproximationConcept.loose_upper_approx
TightUpperApprox = ApproximationConcept.tight_upper_approx
