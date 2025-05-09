import typing

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.util.constants import ConceptType


class TruthConcept(Concept):
    def __init__(self, c_type: ConceptType) -> None:
        assert c_type in (ConceptType.TOP, ConceptType.BOTTOM)
        if c_type == ConceptType.TOP:
            super().__init__(ConceptType.TOP)
        else:
            super().__init__(ConceptType.BOTTOM)
        self.name = self.compute_name()

    @staticmethod
    def get_top():
        return TruthConcept(ConceptType.TOP)

    @staticmethod
    def get_bottom():
        return TruthConcept(ConceptType.BOTTOM)

    def is_atomic(self) -> bool:
        return True

    def is_complemented_atomic(self) -> bool:
        return False

    def clone(self) -> typing.Self:
        return TruthConcept(self.type)

    def replace(self, a: Concept, c: Concept) -> Concept:
        return self

    def compute_name(self) -> typing.Optional[str]:
        if self.type == ConceptType.TOP:
            return "*top*"
        elif self.type == ConceptType.BOTTOM:
            return "*bottom*"

    def compute_atomic_concepts(self) -> set[Concept]:
        return set()

    def get_atomic_concepts(self) -> set[typing.Self]:
        return set([self])

    def get_atoms(self) -> list[typing.Self]:
        return [self]

    def get_roles(self) -> set[str]:
        return set()

    def __and__(self, value: typing.Self) -> typing.Self:
        return value if self.type == ConceptType.TOP else TruthConcept.get_bottom()

    def __or__(self, value: typing.Self) -> typing.Self:
        return TruthConcept.get_top() if self.type == ConceptType.TOP else value

    def __rshift__(self, value: Concept) -> Concept:
        if self.type == ConceptType.TOP:
            return value
        else:
            return TruthConcept.get_top()

    def __neg__(self) -> typing.Self:
        if self.type == ConceptType.TOP:
            return TruthConcept(ConceptType.BOTTOM)
        else:
            return TruthConcept(ConceptType.TOP)

    def __hash__(self) -> int:
        return hash(self.name)

    def __eq__(self, value: typing.Self) -> bool:
        return isinstance(value, TruthConcept) and str(self) == str(value)

    def __ne__(self, value: typing.Self) -> bool:
        return not (self == value)


TOP: Concept = TruthConcept.get_top()
BOTTOM: Concept = TruthConcept.get_bottom()
