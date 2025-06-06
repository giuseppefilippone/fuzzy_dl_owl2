import typing

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_concrete_concept import (
    FuzzyConcreteConcept,
)
from fuzzy_dl_owl2.fuzzydl.concept.operator_concept import OperatorConcept
from fuzzy_dl_owl2.fuzzydl.individual.individual import Individual
from fuzzy_dl_owl2.fuzzydl.util.constants import ConceptType


class SigmaConcept(Concept):
    """Sigma-count concept."""

    def __init__(
        self,
        concept: Concept,
        role: str,
        individuals: list[Individual],
        concrete_concept: FuzzyConcreteConcept,
    ) -> None:
        super().__init__(ConceptType.SIGMA_CONCEPT, "")
        self.concept: Concept = concept
        self.role: str = role
        self.individuals: list[Individual] = individuals
        self.concrete_concept: FuzzyConcreteConcept = concrete_concept
        self.name: str = self.compute_name()

    def get_individuals(self) -> list[Individual]:
        return self.individuals

    def get_concept(self) -> Concept:
        return self.concept

    def get_role(self) -> str:
        return self.role

    def get_fuzzy_concept(self) -> FuzzyConcreteConcept:
        return self.concrete_concept

    def clone(self) -> typing.Self:
        return SigmaConcept(
            self.concept.clone(),
            self.role,
            [i.clone() for i in self.individuals],
            self.concrete_concept.clone(),
        )

    def compute_atomic_concepts(self) -> set[Concept]:
        return set()

    def get_roles(self) -> set[str]:
        return set()

    def replace(self, a: Concept, c: Concept) -> Concept:
        return self

    def compute_name(self) -> str | None:
        return f"(sigma-count {self.role} {self.concept} {{{' '.join(map(str, self.individuals))}}} {self.concrete_concept})"

    def __neg__(self) -> Concept:
        return OperatorConcept.not_(self)

    def __and__(self, value: typing.Self) -> typing.Self:
        return OperatorConcept.and_(self, value)

    def __or__(self, value: typing.Self) -> typing.Self:
        return OperatorConcept.or_(self, value)

    def __hash__(self) -> int:
        return hash(str(self))
