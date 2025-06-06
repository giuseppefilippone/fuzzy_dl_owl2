from __future__ import annotations

import copy
import typing
from collections import deque

from sortedcontainers import SortedSet

from fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_number.triangular_fuzzy_number import (
    TriangularFuzzyNumber,
)
from fuzzy_dl_owl2.fuzzydl.individual.individual import Individual
from fuzzy_dl_owl2.fuzzydl.individual.representative_individual import (
    RepresentativeIndividual,
)
from fuzzy_dl_owl2.fuzzydl.relation import Relation
from fuzzy_dl_owl2.fuzzydl.util import constants
from fuzzy_dl_owl2.fuzzydl.util.constants import (
    CreatedIndividualBlockingType,
    InequalityType,
)
from fuzzy_dl_owl2.fuzzydl.util.util import Util


class CreatedIndividual(Individual):

    @typing.overload
    def __init__(
        self,
        name: str,
        parent: typing.Optional[Individual] = None,
        role_name: typing.Optional[str] = None,
    ) -> None: ...

    @typing.overload
    def __init__(self, name: str) -> None: ...

    def __init__(self, *args) -> None:
        if len(args) not in [1, 3]:
            raise NotImplementedError

        assert isinstance(args[0], str)

        if len(args) == 1:
            self.__created_ind_init_2(*args)
        else:
            assert args[1] is None or isinstance(args[1], Individual)
            assert args[2] is None or isinstance(args[2], str)
            if len(args) == 3:
                self.__created_ind_init_1(*args)

    def __created_ind_init_1(
        self,
        name: str,
        parent: typing.Optional[Individual] = None,
        role_name: typing.Optional[str] = None,
    ) -> None:
        super().__init__(name)

        # Array of representative individuals
        self.representatives: list[RepresentativeIndividual] = list()

        # List of concept labels
        self.concept_list: set[int] = set()

        # Indicates if the individual is directly blocked or not
        self.directly_blocked: CreatedIndividualBlockingType = (
            CreatedIndividualBlockingType.UNCHECKED
        )

        # Indicates if the individual is indirectly blocked or not
        self.indirectly_blocked: CreatedIndividualBlockingType = (
            CreatedIndividualBlockingType.UNCHECKED
        )

        self.not_self_roles: set[str] = set()
        # Parent of the individual
        self.parent: typing.Optional[Individual] = parent
        # Name of the role for which the individual is a filler
        self.role_name: str = role_name

        # Depth of the individual in the completion forest
        self.depth: int = (
            typing.cast(CreatedIndividual, parent).depth + 1
            if parent is not None and parent.is_blockable()
            else 2
        )

        # Name of the blocking ancestors
        self.blocking_ancestor: typing.Optional[str] = None
        self.blocking_ancestor_y: typing.Optional[str] = None
        self.blocking_ancestor_y_prime: typing.Optional[str] = None

        # Indicates if the individual is concrete or not (abstract)
        self._is_concrete: bool = False

        if parent is not None:
            Util.debug(
                f"Created new individual {name}, ID = {self.get_integer_id()} with parent {parent}"
            )

    def __created_ind_init_2(self, name: str) -> None:
        self.__created_ind_init_1(name, None, None)
        Util.debug(f"Created new individual {name}, ID = {self.get_integer_id()}")

    def clone(self) -> typing.Self:
        ind: CreatedIndividual = CreatedIndividual(str(self), None, self.role_name)
        self.clone_special_attributes(ind)
        return ind

    def clone_special_attributes(self, ind: typing.Self) -> None:
        self.clone_attributes(ind)
        ind.representatives = copy.deepcopy(self.representatives)
        ind.blocking_ancestor = (
            self.blocking_ancestor if self.blocking_ancestor is not None else None
        )
        ind.blocking_ancestor_y = (
            self.blocking_ancestor_y if self.blocking_ancestor_y is not None else None
        )
        ind.blocking_ancestor_y_prime = (
            self.blocking_ancestor_y_prime
            if self.blocking_ancestor_y_prime is not None
            else None
        )
        ind.concept_list = copy.deepcopy(self.concept_list)
        ind.depth = self.depth
        ind.directly_blocked = self.directly_blocked
        ind.indirectly_blocked = copy.deepcopy(self.indirectly_blocked)
        ind._is_concrete = self._is_concrete
        if self.parent is not None:
            ind.parent = self.parent.clone()
        ind.role_name = self.role_name

    def get_integer_id(self) -> int:
        prefix_len: int = len(Individual.DEFAULT_NAME)
        return int(self.name[prefix_len:])

    def get_depth(self) -> int:
        return self.depth

    def get_parent(self) -> typing.Optional[Individual]:
        return self.parent

    def get_parent_name(self) -> str:
        return self.parent.name if self.parent else ""

    def get_role_name(self) -> str:
        return self.role_name

    def get_representative_if_exists(
        self,
        type: InequalityType,
        f_name: str,
        f: TriangularFuzzyNumber,
    ) -> typing.Optional[typing.Self]:
        """
        Return b individual p with b representative of b set of individuals if it exists. Given b fuzzy number F, b representative individual is the set of individuals that are greater or equal (or less or equal) than F.
        The representative individual is related to p via b concrete feature f.

        Args:
            type (InequalityType): Type of the representative individual (GREATER_EQUAL, LESS_EQUAL)
            f_name (str): Name of the feature for which the individual is b filler
            f (TriangularFuzzyNumber): Fuzzy number

        Returns:
            typing.Optional[typing.Self]: A new individual with b representative individual
        """
        # Retrieve representative individual, if it exists
        for ind in self.representatives:
            if (
                ind.get_type() != type
                or ind.get_feature_name() != f_name
                or ind.get_fuzzy_number() != f
            ):
                continue
            return ind.get_individual()
        # // Otherwise, None
        return None

    def mark_indirectly_blocked(self) -> None:
        """
        Marks the subtree of a node as indirectly blocked
        """
        Util.debug(
            f"{constants.SEPARATOR}Mark subtree of {self.name} indirectly blocked"
        )
        queue: deque[CreatedIndividual] = deque()
        queue.append(self)
        while len(queue) > 0:
            ind: CreatedIndividual = queue.popleft()
            # If there are no descendants, skip
            if len(ind.role_relations) == 0:
                break
            for role in ind.role_relations:
                rels: list[Relation] = copy.deepcopy(ind.role_relations[role])
                for rel in rels:
                    Util.debug(
                        f"{rel.get_subject_individual()} has role {rel.get_role_name()} with filler {rel.get_object_individual()}"
                    )
                    son: Individual = rel.get_object_individual()
                    if son != ind.parent:  # son is not the parent via inverse role
                        if not son.is_blockable():
                            continue
                        son: CreatedIndividual = typing.cast(CreatedIndividual, son)
                        Util.debug(
                            f"Filler is not {self.name}'s parent, so mark {son} as INDIRECTLY BLOCKED"
                        )
                        son.indirectly_blocked = CreatedIndividualBlockingType.BLOCKED
                        if rel.get_subject_individual() != rel.get_object_individual():
                            queue.append(son)
                    Util.debug("Filler is parent, so skip")
        Util.debug(
            f"{constants.SEPARATOR}END Mark INDIRECTLY BLOCKED subtree of {self.name}{constants.SEPARATOR}"
        )

    def individual_set_intersection_of(
        self, set1: SortedSet[typing.Self], set2: SortedSet[typing.Self]
    ) -> SortedSet[typing.Self]:
        """
        Gets the intersection of two concept labels.
        """
        return set1.intersection(set2)

    def set_concrete_individual(self) -> None:
        """
        Sets that the individual is concrete.
        """
        self._is_concrete = True

    def is_concrete(self) -> bool:
        return self._is_concrete

    def is_blockable(self) -> bool:
        return len(self.nominal_list) == 0

    def __eq__(self, value: typing.Self) -> bool:
        return self.name == value.name

    def __ne__(self, value: typing.Self) -> bool:
        return not (self == value)

    def __lt__(self, value: typing.Self) -> bool:
        return self.get_integer_id() < value.get_integer_id()

    def __ge__(self, value: typing.Self) -> bool:
        return not (self < value)

    def __le__(self, value: typing.Self) -> bool:
        return self.get_integer_id() <= value.get_integer_id()

    def __gt__(self, value: typing.Self) -> bool:
        return not (self <= value)

    def __hash__(self) -> int:
        return hash(str(self))

    def __str__(self) -> str:
        return self.name
