import typing

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.exception.fuzzy_ontology_exception import (
    FuzzyOntologyException,
)
from fuzzy_dl_owl2.fuzzydl.util.constants import ConceptType


class StringConcept(Concept):

    def __init__(self, name: str) -> None:
        super().__init__(ConceptType.ATOMIC)
        self._name: str = name

    def clone(self) -> typing.Self:
        return StringConcept(self.name)

    def compute_name(self) -> str | None:
        return f'"{self.name}"'

    def get_roles(self) -> set[str]:
        return set()

    def compute_atomic_concepts(self) -> set[typing.Self]:
        return set()

    def replace(self, a: typing.Self, c: typing.Self) -> typing.Self | None:
        return self

    def __neg__(self) -> typing.Self:
        raise FuzzyOntologyException("Strings cannot be complemented")

    def __hash__(self) -> int:
        return hash(str(self))
