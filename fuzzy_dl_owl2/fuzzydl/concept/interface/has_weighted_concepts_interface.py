import abc
import typing

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.concept.interface.has_concepts_interface import (
    HasConceptsInterface,
)


class HasWeightedConceptsInterface(HasConceptsInterface, abc.ABC):

    def __init__(
        self,
        weights: typing.Optional[typing.Iterable[float]],
        concepts: typing.Iterable[Concept],
    ) -> None:
        super().__init__(concepts)

        self._weights: typing.Optional[list[float]] = (
            list(weights) if weights is not None else None
        )

    @property
    def weights(self) -> typing.Optional[list[float]]:
        return self._weights

    @weights.setter
    def weights(self, value: typing.Optional[typing.Iterable[float]]) -> None:
        self._weights = list(value) if value is not None else None
