import typing

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.concept.interface.has_concept_interface import (
    HasConceptInterface,
)
from fuzzy_dl_owl2.fuzzydl.concept.operator_concept import OperatorConcept
from fuzzy_dl_owl2.fuzzydl.util.constants import ConceptType


class ThresholdConcept(Concept, HasConceptInterface):

    def __init__(self, c_type: ConceptType, c: Concept, weight: float) -> None:
        Concept.__init__(self, c_type)
        HasConceptInterface.__init__(self, c)

        assert c_type in (
            ConceptType.POS_THRESHOLD,
            ConceptType.NEG_THRESHOLD,
        )

        self._weight: float = weight
        self.name = self.compute_name()

    @property
    def weight(self) -> float:
        return self._weight

    @weight.setter
    def weight(self, value: float) -> None:
        self._weight = value

    @staticmethod
    def pos_threshold(w: float, c: typing.Self) -> typing.Self:
        return ThresholdConcept(ConceptType.POS_THRESHOLD, c, w)

    @staticmethod
    def neg_threshold(w: float, c: typing.Self) -> typing.Self:
        return ThresholdConcept(ConceptType.NEG_THRESHOLD, c, w)

    def clone(self) -> typing.Self:
        return ThresholdConcept(self.type, self.curr_concept, self.weight)

    def replace(self, a: Concept, c: Concept) -> Concept:
        c_type: ConceptType = c.type
        if c_type == ConceptType.POS_THRESHOLD:
            return ThresholdConcept.pos_threshold(
                self.weight, self.curr_concept.replace(a, c)
            )
        elif c_type == ConceptType.NEG_THRESHOLD:
            return ThresholdConcept.neg_threshold(
                self.weight, self.curr_concept.replace(a, c)
            )

    def compute_name(self) -> typing.Optional[str]:
        if self.type == ConceptType.POS_THRESHOLD:
            return f"([>= {self.weight}] {self.curr_concept})"
        elif self.type == ConceptType.NEG_THRESHOLD:
            return f"([<= {self.weight}] {self.curr_concept})"

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


PosThreshold = ThresholdConcept.pos_threshold
NegThreshold = ThresholdConcept.neg_threshold
