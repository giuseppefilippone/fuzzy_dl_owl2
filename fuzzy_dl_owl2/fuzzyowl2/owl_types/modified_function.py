from fuzzy_dl_owl2.fuzzyowl2.owl_types.fuzzy_datatype import FuzzyDatatype


class ModifiedFunction(FuzzyDatatype):
    def __init__(self, mod: str, d: str) -> None:
        super().__init__()
        self._mod: str = mod
        self._d: str = d

    def get_mod(self) -> str:
        return self._mod

    def get_d(self) -> str:
        return self._d

    def __str__(self) -> str:
        return f"({self._mod}, {self._d})"