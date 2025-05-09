from __future__ import annotations

import copy
import typing
from abc import abstractmethod

from fuzzy_dl_owl2.fuzzydl.assertion.assertion import Assertion
from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_number.triangular_fuzzy_number import (
    TriangularFuzzyNumber,
)
from fuzzy_dl_owl2.fuzzydl.exception.inconsistent_ontology_exception import (
    InconsistentOntologyException,
)
from fuzzy_dl_owl2.fuzzydl.relation import Relation
from fuzzy_dl_owl2.fuzzydl.restriction.restriction import Restriction
from fuzzy_dl_owl2.fuzzydl.util.constants import RepresentativeIndividualType


class Individual:
    DEFAULT_NAME: str = "i"

    def __init__(self, name: str) -> None:
        self.name: str = name
        self.concrete_role_restrictions: dict[str, list[Assertion]] = dict()
        self.fillers_to_show: dict[str, set[str]] = dict()
        self.list_of_concepts: set[Concept] = set()
        self.nominal_list: set[str] = set()
        self.not_self_roles: set[str] = list()
        self.role_relations: dict[str, list[Relation]] = dict()
        self.role_restrictions: dict[str, list[Restriction]] = dict()

    def clone(self) -> typing.Self:
        ind = Individual(self.name)
        self.clone_attributes(ind)
        return ind

    def clone_attributes(self, ind: typing.Self) -> None:
        ind.concrete_role_restrictions = {
            k: [a for a in v] for k, v in self.concrete_role_restrictions.items()
        }
        ind.fillers_to_show = copy.deepcopy(self.fillers_to_show)
        ind.list_of_concepts = set([c for c in self.list_of_concepts])
        ind.nominal_list = copy.deepcopy(self.nominal_list)
        ind.not_self_roles = copy.deepcopy(self.not_self_roles)
        # ind.representatives = copy.deepcopy(self.representatives)
        ind.role_restrictions = {
            k: [r.clone() for r in v] for k, v in self.role_restrictions.items()
        }
        ind.role_relations = {
            k: [r.clone() for r in v] for k, v in self.role_relations.items()
        }

    def set_name(self, name: str) -> None:
        self.name = name

    def add_concrete_restriction(self, f_name: str, ass: Assertion) -> None:
        self.concrete_role_restrictions[f_name] = self.concrete_role_restrictions.get(
            f_name, []
        ) + [ass]

    @abstractmethod
    def get_representative_if_exists(
        self,
        type: RepresentativeIndividualType,
        f_name: str,
        f: TriangularFuzzyNumber,
    ):
        pass

    def add_concept(self, c: Concept) -> None:
        self.list_of_concepts.add(c)

    def get_concepts(self) -> set[Concept]:
        return self.list_of_concepts

    def add_to_nominal_list(self, ind_name: str) -> None:
        self.nominal_list.add(ind_name)

    def get_nominal_list(self) -> set[str]:
        return self.nominal_list

    def is_blockable(self) -> bool:
        return False

    def set_label(self, ind_name: str) -> None:
        raise InconsistentOntologyException(
            f"Individuals cannot have names {self.name} and {ind_name}"
        )

    def prune(self) -> None:
        to_prune: list[Individual] = []
        for role in self.role_relations:
            rels: list[Relation] = self.role_relations.get(role, [])
            for r in rels:
                obj: Individual = r.get_object_individual()
                if obj.is_blockable():
                    to_prune.append(obj)
        self.role_relations = dict()
        for i in to_prune:
            i.prune()

    def __eq__(self, value: typing.Self) -> bool:
        return self.name == value.name

    def __ne__(self, value: typing.Self) -> bool:
        return not (self == value)

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return self.name
