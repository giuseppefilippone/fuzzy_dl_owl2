from __future__ import annotations

import typing
from abc import ABC, abstractmethod

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept


class Modifier(ABC):
    """
    Fuzzy modifier.
    """

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
        """
        Modifies a fuzzy concept.

        Args:
            concept (Concept): A fuzzy concept

        Returns:
            Concept: Fuzzy concept resulting from the application of the modifier to c.
        """
        pass

    @abstractmethod
    def get_membership_degree(self, value: float) -> float:
        """
        Gets the image in [0,1] of a real number to the modifier.

        Args:
            value (float): A real number in the range of values of the modifier function.

        Returns:
            float: Image in [0,1] of x to the explicit modifier function.
        """
        pass

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        if self.name is None:
            self.name = self.compute_name()
        return self.name
