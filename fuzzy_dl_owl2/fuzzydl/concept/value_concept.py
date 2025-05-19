import typing

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.concept.interface.has_value_interface import (
    HasValueInterface,
)
from fuzzy_dl_owl2.fuzzydl.concept.operator_concept import OperatorConcept
from fuzzy_dl_owl2.fuzzydl.util.constants import ConceptType


class ValueConcept(Concept, HasValueInterface):

    def __init__(self, c_type: ConceptType, role: str, value: typing.Any) -> None:
        Concept.__init__(self, c_type)
        HasValueInterface.__init__(self, role, value)

        assert c_type in (
            ConceptType.AT_MOST_VALUE,
            ConceptType.AT_LEAST_VALUE,
            ConceptType.EXACT_VALUE,
        )

        self.name = self.compute_name()

    @staticmethod
    def at_most_value(role: str, o: typing.Any) -> typing.Self:
        return ValueConcept(ConceptType.AT_MOST_VALUE, role, o)

    @staticmethod
    def at_least_value(role: str, o: typing.Any) -> typing.Self:
        return ValueConcept(ConceptType.AT_LEAST_VALUE, role, o)

    @staticmethod
    def exact_value(role: str, o: typing.Any) -> typing.Self:
        return ValueConcept(ConceptType.EXACT_VALUE, role, o)

    def clone(self) -> typing.Self:
        return ValueConcept(self.type, self.role, self.value)

    def replace(self, a: Concept, c: Concept) -> Concept:
        return self

    def compute_name(self) -> typing.Optional[str]:
        if self.type == ConceptType.AT_MOST_VALUE:
            return f"(<= {self.role} {self.value})"
        elif self.type == ConceptType.AT_LEAST_VALUE:
            return f"(>= {self.role} {self.value})"
        elif self.type == ConceptType.EXACT_VALUE:
            return f"(= {self.role} {self.value})"

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
