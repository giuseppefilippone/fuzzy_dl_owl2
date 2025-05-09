import abc


class HasRoleInterface(abc.ABC):

    def __init__(self, role: str) -> None:
        self._role: str = role

    @property
    def role(self) -> str:
        return self._role

    @role.setter
    def role(self, value: str) -> None:
        self._role = value
