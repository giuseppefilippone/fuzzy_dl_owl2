import copy
import typing

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.concept.interface.has_value_interface import (
    HasValueInterface,
)
from fuzzy_dl_owl2.fuzzydl.concept.operator_concept import OperatorConcept
from fuzzy_dl_owl2.fuzzydl.util.constants import ConceptType
from fuzzy_dl_owl2.fuzzydl.util.util import Util


class HasValueConcept(Concept, HasValueInterface):

    def __init__(self, role: str, value: typing.Any) -> None:
        Concept.__init__(self, ConceptType.HAS_VALUE)
        HasValueInterface.__init__(self, role, value)

        self.name: str = self.compute_name()

    @staticmethod
    def has_value(role: str, i: typing.Any) -> typing.Self:
        return HasValueConcept(role, i)

    def clone(self) -> typing.Self:
        return HasValueConcept(self.role, copy.deepcopy(self.value))

    def replace(self, a: Concept, c: Concept) -> Concept:
        Util.error(f"Error replacing in concept {self}")
        return None

    def compute_name(self) -> typing.Optional[str]:
        return f"(b-some {self.role} {self.value})"

    def compute_atomic_concepts(self) -> set[Concept]:
        return set()

    def get_roles(self) -> set[str]:
        return set()

    def __neg__(self) -> Concept:
        return OperatorConcept.not_(self)

    def __and__(self, value: typing.Self) -> typing.Self:
        return OperatorConcept.and_(self, value)

    def __or__(self, value: typing.Self) -> typing.Self:
        return OperatorConcept.or_(self, value)

    def __hash__(self) -> int:
        return hash(str(self))
