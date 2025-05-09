import typing

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.concept.operator_concept import OperatorConcept
from fuzzy_dl_owl2.fuzzydl.exception.fuzzy_ontology_exception import (
    FuzzyOntologyException,
)
from fuzzy_dl_owl2.fuzzydl.util.constants import ConceptType


class NegatedNominal(Concept):

    def __init__(self, ind_name: str) -> None:
        super().__init__(ConceptType.ATOMIC)
        self._ind_name: str = ind_name
        self.name: str = f"(not {{ {ind_name} }} )"

    @property
    def ind_name(self) -> str:
        return self._ind_name

    @ind_name.setter
    def ind_name(self, value: str) -> None:
        self._ind_name = value

    def clone(self) -> typing.Self:
        return NegatedNominal(self.ind_name)

    def compute_name(self) -> str | None:
        return self.name

    def __neg__(self) -> typing.Self:
        raise FuzzyOntologyException("Negated nominals cannot be complemented")

    def __hash__(self) -> int:
        return hash(str(self))

    def __and__(self, value: typing.Self) -> typing.Self:
        return OperatorConcept.and_(self, value)

    def __or__(self, value: typing.Self) -> typing.Self:
        return OperatorConcept.or_(self, value)
