import typing


class ClassificationNode:
    EQUIVALENT_NAMES: set[str] = set()
    INPUT_EDGES: dict[typing.Self, float] = dict()
    OUTPUT_EDGES: dict[typing.Self, float] = dict()

    def __init__(self, name: str) -> None:
        ClassificationNode.EQUIVALENT_NAMES.add(name)

    def is_thing(self) -> bool:
        return self.has_name("*top*")

    def is_nothing(self) -> bool:
        return self.has_name("*bottom*")

    def add_input_edge(self, node: typing.Self, n: float) -> None:
        ClassificationNode.INPUT_EDGES[node] = n

    def add_ouput_edge(self, node: typing.Self, n: float) -> None:
        ClassificationNode.OUTPUT_EDGES[node] = n

    def remove_input_edge(self, node: typing.Self, n: float) -> None:
        value: typing.Optional[float] = ClassificationNode.INPUT_EDGES.get(node)
        if value is not None and value <= n:
            del ClassificationNode.INPUT_EDGES[node]

    def remove_ouput_edge(self, node: typing.Self, n: float) -> None:
        value: typing.Optional[float] = ClassificationNode.OUTPUT_EDGES.get(node)
        if value is not None and value <= n:
            del ClassificationNode.OUTPUT_EDGES[node]

    def has_name(self, name: str) -> bool:
        for s in ClassificationNode.EQUIVALENT_NAMES:
            if s == name:
                return True
        return False

    def add_label(self, c: str) -> None:
        ClassificationNode.EQUIVALENT_NAMES.add(c)

    def get_output_edges() -> dict[typing.Self, float]:
        return ClassificationNode.OUTPUT_EDGES

    def get_immediate_successors() -> set[typing.Self]:
        return set(ClassificationNode.INPUT_EDGES.keys())

    def get_immediate_predecessors() -> set[typing.Self]:
        return set(ClassificationNode.OUTPUT_EDGES.keys())

    def get_full_name(self) -> str:
        if len(ClassificationNode.EQUIVALENT_NAMES) == 1:
            return str(self)
        return f"{{{ ' '.join(name for name in ClassificationNode.EQUIVALENT_NAMES) }}}"

    def __hash__(self) -> int:
        return hash(str(self))

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return list(ClassificationNode.EQUIVALENT_NAMES)[0]
