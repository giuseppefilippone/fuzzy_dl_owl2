from __future__ import annotations

import copy
import typing

from fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_concrete_concept import (
    FuzzyConcreteConcept,
)
from fuzzy_dl_owl2.fuzzydl.milp.variable import Variable


class ShowVariablesHelper:
    def __init__(self) -> None:
        self.abstract_fillers: dict[str, set[str]] = dict()
        self.concepts: set[str] = set()
        self.concrete_fillers: dict[str, set[str]] = dict()
        self.global_abstract_fillers: set[str] = set()
        self.global_concrete_fillers: set[str] = set()
        self.individuals: set[str] = set()
        self.labels_for_fillers: dict[str, list[FuzzyConcreteConcept]] = dict()
        self.variables: dict[Variable, str] = dict()

    def clone(self) -> typing.Self:
        s = ShowVariablesHelper()
        s.abstract_fillers = copy.deepcopy(self.abstract_fillers)
        s.concepts = copy.deepcopy(self.concepts)
        s.concrete_fillers = copy.deepcopy(self.concrete_fillers)
        s.global_abstract_fillers = copy.deepcopy(self.global_abstract_fillers)
        s.global_concrete_fillers = copy.deepcopy(self.global_concrete_fillers)
        s.individuals = copy.deepcopy(self.individuals)
        s.labels_for_fillers = {
            k: [c for c in v] for k, v in self.labels_for_fillers.items()
        }
        s.variables = {k: v for k, v in self.variables.items()}
        return s

    def get_name(self, var: Variable) -> str:
        return self.variables.get(var)

    def show_variable(self, var: Variable) -> bool:
        return var in self.variables

    def add_individual_to_show(self, ind_name: str) -> None:
        self.individuals.add(ind_name)

    def show_individuals(self, ind_name: str) -> bool:
        return ind_name in self.individuals

    @typing.overload
    def add_concrete_filler_to_show(self, f_name: str) -> None: ...

    @typing.overload
    def add_concrete_filler_to_show(self, f_name: str, ind_name: str) -> None: ...

    @typing.overload
    def add_concrete_filler_to_show(
        self, f_name: str, ind_name: str, ar: list[FuzzyConcreteConcept]
    ) -> None: ...

    def add_concrete_filler_to_show(self, *args) -> None:
        assert len(args) in [1, 2, 3]
        assert isinstance(args[0], str)
        if len(args) == 1:
            self.__add_concrete_filler_to_show_1(*args)
        elif len(args) == 2:
            assert isinstance(args[1], str)
            self.__add_concrete_filler_to_show_2(*args)
        else:
            assert isinstance(args[1], str)
            assert isinstance(args[2], list) and all(
                isinstance(a, FuzzyConcreteConcept) for a in args[2]
            )
            self.__add_concrete_filler_to_show_3(*args)

    def __add_concrete_filler_to_show_1(self, f_name: str) -> None:
        self.global_concrete_fillers.add(f_name)
        if f_name in self.concrete_fillers:
            del self.concrete_fillers[f_name]

    def __add_concrete_filler_to_show_2(self, f_name: str, ind_name: str) -> None:
        if f_name in self.global_concrete_fillers:
            return
        self.concrete_fillers[f_name] = self.concrete_fillers.get(f_name, set()) | set(
            [ind_name]
        )

    def __add_concrete_filler_to_show_3(
        self, f_name: str, ind_name: str, ar: list[FuzzyConcreteConcept]
    ) -> None:
        self.add_concrete_filler_to_show(f_name, ind_name)
        name: str = f"{f_name}({ind_name})"
        aux: list[FuzzyConcreteConcept] = self.get_labels(name)
        if len(aux) > 0:
            aux.extend(ar)
            self.labels_for_fillers[name] = aux
        else:
            self.labels_for_fillers[name] = ar

    def get_labels(self, var_name: str) -> list[FuzzyConcreteConcept]:
        return self.labels_for_fillers.get(var_name, [])

    @typing.overload
    def add_abstract_filler_to_show(self, role_name: str) -> None: ...

    @typing.overload
    def add_abstract_filler_to_show(self, role_name: str, ind_name: str) -> None: ...

    def add_abstract_filler_to_show(self, *args) -> None:
        assert len(args) in [1, 2]
        assert isinstance(args[0], str)
        if len(args) == 1:
            self.__add_abstract_filler_to_show_1(*args)
        else:
            assert isinstance(args[1], str)
            self.__add_abstract_filler_to_show_2(*args)

    def __add_abstract_filler_to_show_1(self, role_name: str) -> None:
        self.global_abstract_fillers.add(role_name)
        if role_name in self.abstract_fillers:
            del self.abstract_fillers[role_name]

    def __add_abstract_filler_to_show_2(self, role_name: str, ind_name: str) -> None:
        if role_name in self.global_abstract_fillers:
            return
        self.abstract_fillers[role_name] = self.abstract_fillers.get(
            role_name, set()
        ) | set([ind_name])

    def show_concrete_fillers(self, f_name: str, ind_name: str) -> bool:
        if f_name not in self.global_concrete_fillers:
            hs = self.concrete_fillers.get(f_name)
            return hs is not None and ind_name in hs
        return True

    def show_abstract_role_fillers(self, role_name: str, ind_name: str) -> bool:
        if role_name not in self.global_abstract_fillers:
            hs = self.abstract_fillers.get(role_name)
            return hs is not None and ind_name in hs
        return True

    def add_concept_to_show(self, conc_name: str) -> None:
        self.concepts.add(conc_name)

    def show_concepts(self, concept_name: str) -> bool:
        return concept_name in self.concepts

    def add_variable(self, var: Variable, name_to_show: str) -> None:
        self.variables[var] = name_to_show

    def get_variables(self) -> list[Variable]:
        return list(self.variables.keys())
