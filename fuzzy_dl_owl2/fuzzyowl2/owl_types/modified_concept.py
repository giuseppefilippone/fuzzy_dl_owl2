from fuzzy_dl_owl2.fuzzyowl2.owl_types.concept_definition import ConceptDefinition
from fuzzy_dl_owl2.fuzzyowl2.util.constants import ConceptType


class ModifiedConcept(ConceptDefinition):

    def __init__(self, mod: str, c: str) -> None:
        super().__init__(ConceptType.MODIFIED_CONCEPT)
        self._mod: str = mod
        self._c: str = c

    def get_fuzzy_modifier(self) -> str:
        return self._mod

    def get_fuzzy_concept(self) -> str:
        return self._c

    def __str__(self) -> str:
        return f"({self._mod}, {self._c})"
