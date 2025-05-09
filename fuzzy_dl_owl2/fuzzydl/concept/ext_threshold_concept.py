import typing

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.concept.interface.has_concept_interface import (
    HasConceptInterface,
)
from fuzzy_dl_owl2.fuzzydl.concept.operator_concept import OperatorConcept
from fuzzy_dl_owl2.fuzzydl.milp.variable import Variable
from fuzzy_dl_owl2.fuzzydl.util.constants import ConceptType


class ExtThresholdConcept(Concept, HasConceptInterface):

    def __init__(
        self, c_type: ConceptType, c: Concept, weight_variable: Variable
    ) -> None:
        Concept.__init__(self, c_type)
        HasConceptInterface.__init__(self, c)

        assert c_type in (
            ConceptType.EXT_POS_THRESHOLD,
            ConceptType.EXT_NEG_THRESHOLD,
        )
        self._weight_variable: Variable = weight_variable
        self.name: str = self.compute_name()

    @property
    def weight_variable(self) -> Variable:
        return self._weight_variable

    @weight_variable.setter
    def weight_variable(self, value: Variable) -> None:
        self._weight_variable = value

    @staticmethod
    def extended_pos_threshold(v: Variable, c: typing.Self) -> typing.Self:
        return ExtThresholdConcept(ConceptType.EXT_POS_THRESHOLD, c, v)

    @staticmethod
    def extended_neg_threshold(v: Variable, c: typing.Self) -> typing.Self:
        return ExtThresholdConcept(ConceptType.EXT_NEG_THRESHOLD, c, v)

    def clone(self):
        return ExtThresholdConcept(self.type, self.curr_concept, self.weight_variable)

    def replace(self, a: Concept, c: Concept) -> Concept:
        return ExtThresholdConcept(
            self.type, self.curr_concept.replace(a, c), self.weight_variable
        )

    def compute_name(self) -> typing.Optional[str]:
        if self.type == ConceptType.EXT_POS_THRESHOLD:
            return f"([>= {self.weight_variable}] {self.curr_concept})"
        else:
            return f"([<= {self.weight_variable}] {self.curr_concept})"

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


ExtendedPosThreshold = ExtThresholdConcept.extended_pos_threshold
ExtendedNegThreshold = ExtThresholdConcept.extended_neg_threshold
