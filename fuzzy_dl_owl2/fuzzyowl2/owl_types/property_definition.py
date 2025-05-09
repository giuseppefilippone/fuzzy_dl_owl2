class PropertyDefinition:
    def __init__(self, mod: str, prop: str) -> None:
        self._mod: str = mod
        self._prop: str = prop

    def get_fuzzy_modifier(self) -> str:
        return self._mod

    def get_property(self) -> str:
        return self._prop
