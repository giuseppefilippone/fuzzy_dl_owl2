import abc
import typing

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept


class HasConceptsInterface(abc.ABC):

    def __init__(self, concepts: typing.Iterable[Concept]) -> None:
        self._concepts: list[Concept] = list(concepts)

    @property
    def concepts(self) -> list[Concept]:
        return self._concepts

    @concepts.setter
    def concepts(self, value: typing.Iterable[Concept]) -> None:
        self._concepts = list(value)
