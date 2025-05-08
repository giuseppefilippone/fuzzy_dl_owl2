class RoleParentWithDegree:
    def __init__(self, parent: str, degree: float) -> None:
        self.degree: float = degree
        self.parent: str = parent

    def get_degree(self) -> float:
        return self.degree

    def get_parent(self) -> str:
        return self.parent
