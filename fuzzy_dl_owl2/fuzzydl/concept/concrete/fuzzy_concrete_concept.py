from __future__ import annotations

import typing
from abc import ABC, abstractmethod

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.exception.fuzzy_ontology_exception import (
    FuzzyOntologyException,
)
from fuzzy_dl_owl2.fuzzydl.util.constants import ConceptType
from fuzzy_dl_owl2.fuzzydl.util.util import Util


class FuzzyConcreteConcept(Concept, ABC):

    def __init__(self, name: str) -> None:
        super().__init__(ConceptType.CONCRETE, name)
        self.name: str = name
        self._k1: float = 0.0
        self._k2: float = 0.0

    @property
    def k1(self) -> float:
        return self._k1

    @k1.setter
    def k1(self, value: float) -> None:
        self._k1 = float(value)

    @property
    def k2(self) -> float:
        return self._k2

    @k2.setter
    def k2(self, value: float) -> None:
        self._k2 = float(value)

    def compute_name(self) -> str:
        return self.name

    def is_concrete(self) -> bool:
        return True

    def compute_atomic_concepts(self) -> set[typing.Self]:
        return set()

    def get_roles(self) -> set[str]:
        return set()

    def replace(self, concept1: Concept, concept2: Concept) -> Concept:
        try:
            Util.error(f"Error replacing in concept {self}")
        except FuzzyOntologyException:
            pass
        return None

    @abstractmethod
    def get_membership_degree(self, value: float) -> float:
        """Get membership degree for a value"""
        pass

    # def __str__(self) -> str:
    #     return self.get_name() or self.name
