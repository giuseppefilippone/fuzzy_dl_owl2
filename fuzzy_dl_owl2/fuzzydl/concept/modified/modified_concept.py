from __future__ import annotations

import typing
from abc import ABC

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.concept.interface.has_concept_interface import (
    HasConceptInterface,
)
from fuzzy_dl_owl2.fuzzydl.concept.operator_concept import OperatorConcept
from fuzzy_dl_owl2.fuzzydl.modifier.modifier import Modifier
from fuzzy_dl_owl2.fuzzydl.util.constants import ConceptType


class ModifiedConcept(Concept, HasConceptInterface, ABC):

    def __init__(self, c: Concept, mod: Modifier) -> None:
        Concept.__init__(self, ConceptType.MODIFIED)
        HasConceptInterface.__init__(self, c)

        self._modifier: Modifier = mod

    @property
    def modifier(self) -> Modifier:
        return self._modifier

    @modifier.setter
    def modifier(self, value: Modifier) -> None:
        self._modifier = value

    def compute_name(self) -> str | None:
        return f"({self.modifier} {self.curr_concept})"

    def compute_atomic_concepts(self) -> set[typing.Self]:
        return self.curr_concept.compute_atomic_concepts()

    def get_roles(self) -> set[str]:
        return self.curr_concept.get_roles()

    def is_concrete(self) -> bool:
        return self.curr_concept.is_concrete()

    def replace(self, concept1: Concept, concept2: Concept) -> Concept:
        return self

    def __neg__(self) -> typing.Self:
        return OperatorConcept.not_(self)

    def __and__(self) -> typing.Self:
        return OperatorConcept.and_(self)

    def __or__(self) -> typing.Self:
        return OperatorConcept.or_(self)

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return self.compute_name()
