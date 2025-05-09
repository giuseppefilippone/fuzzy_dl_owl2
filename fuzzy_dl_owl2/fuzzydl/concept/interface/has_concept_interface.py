import abc

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept


class HasConceptInterface(abc.ABC):

    def __init__(self, concept: Concept) -> None:
        self._curr_concept: Concept = concept

    @property
    def curr_concept(self) -> Concept:
        return self._curr_concept

    @curr_concept.setter
    def curr_concept(self, value: Concept) -> None:
        self._curr_concept = value
