import typing

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.concept.interface.has_concept_interface import (
    HasConceptInterface,
)
from fuzzy_dl_owl2.fuzzydl.concept.operator_concept import OperatorConcept
from fuzzy_dl_owl2.fuzzydl.util.constants import ConceptType


class WeightedConcept(Concept, HasConceptInterface):

    def __init__(self, weight: float, c: Concept) -> None:
        Concept.__init__(self, ConceptType.WEIGHTED)
        HasConceptInterface.__init__(self, c)

        self._weight: float = weight
        self.name = self.compute_name()

    @property
    def weight(self) -> float:
        return self._weight

    @weight.setter
    def weight(self, value: float) -> None:
        self._weight = value

    def clone(self) -> typing.Self:
        return WeightedConcept(self.weight, self.curr_concept)

    def replace(self, a: Concept, c: Concept) -> Concept:
        c_type: ConceptType = c.type
        if c_type == ConceptType.WEIGHTED:
            return WeightedConcept(self.weight, self.curr_concept.replace(a, c))

    def compute_name(self) -> typing.Optional[str]:
        return f"({self.weight} {self.curr_concept})"

    def compute_atomic_concepts(self) -> set[Concept]:
        return self.curr_concept.compute_atomic_concepts()

    def get_roles(self) -> set[str]:
        return self.curr_concept.get_roles()

    def __neg__(self) -> Concept:
        return OperatorConcept.not_(self)

    def __and__(self, value: typing.Self) -> typing.Self:
        return OperatorConcept.and_(self, value)

    def __or__(self, value: typing.Self) -> typing.Self:
        return OperatorConcept.or_(self, value)

    def __hash__(self) -> int:
        return hash(str(self))
