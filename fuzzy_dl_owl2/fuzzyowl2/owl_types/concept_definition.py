import abc

from fuzzy_dl_owl2.fuzzyowl2.util.constants import ConceptType


class ConceptDefinition(abc.ABC):
    def __init__(self, type: ConceptType) -> None:
        self._type: ConceptType = type

    def get_type(self) -> ConceptType:
        return self._type

    def __repr__(self) -> str:
        return str(self)
