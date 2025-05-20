from fuzzy_dl_owl2.fuzzyowl2.owl_types.fuzzy_property import FuzzyProperty


class ModifiedProperty(FuzzyProperty):

    def __init__(self, mod: str, prop: str) -> None:
        super().__init__()
        self._mod: str = mod
        self._prop: str = prop

    def get_fuzzy_modifier(self) -> str:
        return self._mod

    def get_property(self) -> str:
        return self._prop

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return f"({self.get_fuzzy_modifier()}, {self.get_property()})"
