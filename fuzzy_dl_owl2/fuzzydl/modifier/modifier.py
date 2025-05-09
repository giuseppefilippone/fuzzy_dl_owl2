from __future__ import annotations

import typing
from abc import ABC, abstractmethod

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept


class Modifier(ABC):

    def __init__(self, name: str) -> None:
        self.name: str = name

    def set_name(self, name: str) -> None:
        self.name = name

    @abstractmethod
    def compute_name(self) -> str:
        pass

    @abstractmethod
    def clone(self) -> typing.Self:
        pass

    @abstractmethod
    def modify(self, concept: Concept) -> Concept:
        pass

    @abstractmethod
    def get_membership_degree(self, value: float) -> float:
        pass

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        if self.name is None:
            self.name = self.compute_name()
        return self.name
