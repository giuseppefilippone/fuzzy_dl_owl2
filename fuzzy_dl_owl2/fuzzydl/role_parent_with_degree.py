class RoleParentWithDegree:
    """
    Pair of elements (role, degree in [0,1]).
    Given a role, represents a role parent and the inclusion degree.
    """

    def __init__(self, parent: str, degree: float) -> None:
        self.parent: str = parent
        self.degree: float = degree

    def get_degree(self) -> float:
        return self.degree

    def get_parent(self) -> str:
        return self.parent
