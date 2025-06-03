from __future__ import annotations

import copy
import os
import traceback
import typing

from fuzzy_dl_owl2.fuzzydl.assertion.assertion import Assertion
from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.concept.interface.has_value_interface import (
    HasValueInterface,
)
from fuzzy_dl_owl2.fuzzydl.degree.degree import Degree
from fuzzy_dl_owl2.fuzzydl.degree.degree_numeric import DegreeNumeric
from fuzzy_dl_owl2.fuzzydl.degree.degree_variable import DegreeVariable
from fuzzy_dl_owl2.fuzzydl.individual.created_individual import CreatedIndividual
from fuzzy_dl_owl2.fuzzydl.individual.individual import Individual
from fuzzy_dl_owl2.fuzzydl.milp.expression import Expression
from fuzzy_dl_owl2.fuzzydl.milp.inequation import Inequation
from fuzzy_dl_owl2.fuzzydl.milp.show_variables_helper import ShowVariablesHelper
from fuzzy_dl_owl2.fuzzydl.milp.solution import Solution
from fuzzy_dl_owl2.fuzzydl.milp.term import Term
from fuzzy_dl_owl2.fuzzydl.milp.variable import Variable
from fuzzy_dl_owl2.fuzzydl.relation import Relation
from fuzzy_dl_owl2.fuzzydl.restriction.restriction import Restriction
from fuzzy_dl_owl2.fuzzydl.util import constants
from fuzzy_dl_owl2.fuzzydl.util.config_reader import ConfigReader, MILPProvider
from fuzzy_dl_owl2.fuzzydl.util.constants import (
    ConceptType,
    InequalityType,
    VariableType,
)
from fuzzy_dl_owl2.fuzzydl.util.util import Util


# @utils.singleton
class MILPHelper:
    PRINT_LABELS: bool = True
    PRINT_VARIABLES: bool = True

    def __init__(self) -> None:
        self.constraints: list[Inequation] = list()
        self.crisp_concepts: set[str] = set()
        self.crisp_roles: set[str] = set()
        self.number_of_variables: dict[str, int] = dict()
        self.show_vars: ShowVariablesHelper = ShowVariablesHelper()
        self.string_features: set[str] = set()
        self.string_values: dict[int, str] = dict()
        self.variables: list[Variable] = []

    def clone(self) -> typing.Self:
        milp: MILPHelper = MILPHelper()
        milp.constraints = [c.clone() for c in self.constraints]
        milp.crisp_concepts = copy.deepcopy(self.crisp_concepts)
        milp.crisp_roles = copy.deepcopy(self.crisp_roles)
        milp.number_of_variables = copy.deepcopy(self.number_of_variables)
        milp.show_vars = self.show_vars.clone()
        milp.string_features = copy.deepcopy(self.string_features)
        milp.string_values = copy.deepcopy(self.string_values)
        milp.variables = [v.clone() for v in self.variables]
        return milp

    def optimize(self, objective: Expression) -> typing.Optional[Solution]:
        Util.debug(f"Running MILP solver: {ConfigReader.MILP_PROVIDER.name}")
        if ConfigReader.MILP_PROVIDER == MILPProvider.GUROBI:
            return self.solve_gurobi(objective)
        elif ConfigReader.MILP_PROVIDER == MILPProvider.MIP:
            return self.solve_mip(objective)
        elif ConfigReader.MILP_PROVIDER in [
            MILPProvider.PULP,
            MILPProvider.PULP_GLPK,
            MILPProvider.PULP_HIGHS,
            MILPProvider.PULP_CPLEX,
        ]:
            return self.solve_pulp(objective)
        # elif ConfigReader.MILP_PROVIDER == MILPProvider.SCIPY:
        #     return self.solve_scipy(objective)
        else:
            raise ValueError(
                f"Unsupported MILP provider: {ConfigReader.MILP_PROVIDER.name}"
            )

    @typing.overload
    def print_instance_of_labels(
        self, f_name: str, ind_name: str, value: float
    ) -> None: ...

    @typing.overload
    def print_instance_of_labels(self, name: str, value: float) -> None: ...

    def print_instance_of_labels(self, *args) -> None:
        assert len(args) in [2, 3]
        assert isinstance(args[0], str)
        if len(args) == 2:
            assert isinstance(args[1], constants.NUMBER)
            self.__print_instance_of_labels_2(*args)
        else:
            assert isinstance(args[1], str)
            assert isinstance(args[2], constants.NUMBER)
            self.__print_instance_of_labels_1(*args)

    def __print_instance_of_labels_1(
        self, f_name: str, ind_name: str, value: float
    ) -> None:
        name = f"{f_name}({ind_name})"
        labels = self.show_vars.get_labels(name)
        for f in labels:
            Util.info(
                f"{name} is {f.compute_name()} = {f.get_membership_degree(value)}"
            )

    def __print_instance_of_labels_2(self, name: str, value: float) -> None:
        labels = self.show_vars.get_labels(name)
        for f in labels:
            Util.info(
                f"{name} is {f.compute_name()} = {f.get_membership_degree(value)}"
            )

    def get_new_variable(self, v_type: VariableType) -> Variable:
        while True:
            new_var: Variable = Variable.get_new_variable(v_type)
            var_name = str(new_var)
            if var_name not in self.number_of_variables:
                break

        self.variables.append(new_var)
        self.number_of_variables[var_name] = len(self.variables)
        return new_var

    @typing.overload
    def get_variable(self, var_name: str) -> Variable: ...

    @typing.overload
    def get_variable(self, var_name: str, v_type: VariableType) -> Variable: ...

    @typing.overload
    def get_variable(self, ass: Assertion) -> Variable: ...

    @typing.overload
    def get_variable(self, rel: Relation) -> Variable: ...

    @typing.overload
    def get_variable(self, ind: Individual, restrict: Restriction) -> Variable: ...

    @typing.overload
    def get_variable(self, ind: Individual, c: Concept) -> Variable: ...

    @typing.overload
    def get_variable(self, ind: Individual, concept_name: str) -> Variable: ...

    @typing.overload
    def get_variable(self, a: Individual, b: Individual, role: str) -> Variable: ...

    @typing.overload
    def get_variable(
        self, a: Individual, b: Individual, role: str, v_type: VariableType
    ) -> Variable: ...

    @typing.overload
    def get_variable(
        self, a: str, b: str, role: str, v_type: VariableType
    ) -> Variable: ...

    @typing.overload
    def get_variable(self, ind: CreatedIndividual) -> Variable: ...

    @typing.overload
    def get_variable(self, ind: CreatedIndividual, v_type: VariableType) -> None: ...

    def get_variable(self, *args) -> Variable:
        assert len(args) in [1, 2, 3, 4]
        if len(args) == 1:
            if isinstance(args[0], str):
                return self.__get_variable_1(*args)
            elif isinstance(args[0], Assertion):
                return self.__get_variable_3(*args)
            elif isinstance(args[0], Relation):
                return self.__get_variable_4(*args)
            elif isinstance(args[0], CreatedIndividual):
                return self.__get_variable_11(*args)
            else:
                raise ValueError
        elif len(args) == 2:
            if isinstance(args[0], str) and isinstance(args[1], VariableType):
                return self.__get_variable_2(*args)
            elif isinstance(args[0], Individual) and isinstance(args[1], Restriction):
                return self.__get_variable_5(*args)
            elif isinstance(args[0], Individual) and isinstance(args[1], Concept):
                return self.__get_variable_6(*args)
            elif isinstance(args[0], CreatedIndividual) and isinstance(
                args[1], VariableType
            ):
                return self.__get_variable_12(*args)
            elif isinstance(args[0], Individual) and isinstance(args[1], str):
                return self.__get_variable_7(*args)
            else:
                raise ValueError
        elif len(args) == 3:
            if (
                isinstance(args[0], Individual)
                and isinstance(args[1], Individual)
                and isinstance(args[2], str)
            ):
                return self.__get_variable_8(*args)
            else:
                raise ValueError
        elif len(args) == 4:
            if (
                isinstance(args[0], Individual)
                and isinstance(args[1], Individual)
                and isinstance(args[2], str)
                and isinstance(args[3], VariableType)
            ):
                return self.__get_variable_9(*args)
            elif (
                isinstance(args[0], str)
                and isinstance(args[1], str)
                and isinstance(args[2], str)
                and isinstance(args[3], VariableType)
            ):
                return self.__get_variable_10(*args)
            else:
                raise ValueError
        else:
            raise ValueError

    def __get_variable_1(self, var_name: str) -> Variable:
        if var_name in self.number_of_variables:
            for variable in self.variables:
                if str(variable) == var_name:
                    return variable
        var: Variable = Variable(var_name, VariableType.SEMI_CONTINUOUS)
        self.variables.append(var)
        self.number_of_variables[str(var)] = len(self.variables)
        return var

    def __get_variable_2(self, var_name: str, v_type: VariableType) -> Variable:
        var: Variable = self.get_variable(var_name)
        var.set_type(v_type)
        return var

    def __get_variable_3(self, ass: Assertion) -> Variable:
        return self.get_variable(ass.get_individual(), ass.get_concept())

    def __get_variable_4(self, rel: Relation) -> Variable:
        a: Individual = rel.get_subject_individual()
        b: Individual = rel.get_object_individual()
        role: str = rel.get_role_name()
        return self.get_variable(a, b, role)

    def __get_variable_5(self, ind: Individual, restrict: Restriction) -> Variable:
        var: Variable = self.get_variable(f"{ind}:{restrict.get_name_without_degree()}")
        if self.show_vars.show_individuals(str(ind)):
            self.show_vars.add_variable(var, str(var))
        return var

    def __get_variable_6(self, ind: Individual, c: Concept) -> Variable:
        if c.type == ConceptType.HAS_VALUE:
            assert isinstance(c, HasValueInterface)

            r: str = c.role
            b: str = str(c.value)
            return self.get_variable(str(ind), b, r, VariableType.SEMI_CONTINUOUS)
        return self.get_variable(ind, str(c))

    def __get_variable_7(self, ind: Individual, concept_name: str) -> Variable:
        var: Variable = self.get_variable(f"{ind}:{concept_name}")
        if concept_name in self.crisp_concepts:
            var.set_binary_variable()
        if self.show_vars.show_individuals(str(ind)) or self.show_vars.show_concepts(
            concept_name
        ):
            self.show_vars.add_variable(var, str(var))
        return var

    def __get_variable_8(self, a: Individual, b: Individual, role: str) -> Variable:
        return self.get_variable(a, b, role, VariableType.SEMI_CONTINUOUS)

    def __get_variable_9(
        self, a: Individual, b: Individual, role: str, v_type: VariableType
    ) -> Variable:
        return self.get_variable(str(a), str(b), role, v_type)

    def __get_variable_10(
        self, a: str, b: str, role: str, v_type: VariableType
    ) -> Variable:
        var_name: str = f"({a},{b}):{role}"
        var: Variable = self.get_variable(var_name)
        if role in self.crisp_roles:
            var.set_binary_variable()
        if self.show_vars.show_abstract_role_fillers(
            role, a
        ) or self.show_vars.show_concrete_fillers(role, a):
            self.show_vars.add_variable(var, var_name)
        var.set_type(v_type)
        return var

    def __get_variable_11(self, ind: CreatedIndividual) -> Variable:
        return self.get_variable(ind, VariableType.CONTINUOUS)

    def __get_variable_12(self, ind: CreatedIndividual, v_type: VariableType) -> None:
        if ind.get_parent() is None:
            parent_name: str = "unknown_parent"
        else:
            parent_name: str = str(ind.get_parent())
        feture_name: str = ind.get_role_name()
        if feture_name is None:
            feture_name = "unknown_feature"
        name: str = f"{feture_name}({parent_name})"
        if name == "unknown_feature(unknown_parent)":
            name = str(ind)

        if name in self.number_of_variables:
            x_c: Variable = self.get_variable(name)
        else:
            x_c: Variable = self.get_variable(name)
            if self.show_vars.show_concrete_fillers(feture_name, parent_name):
                self.show_vars.add_variable(x_c, name)
            x_c.set_type(v_type)
        return x_c

    @typing.overload
    def has_variable(self, name: str) -> bool: ...

    @typing.overload
    def has_variable(self, ass: Assertion) -> bool: ...

    def has_variable(self, *args) -> bool:
        assert len(args) == 1
        if isinstance(args[0], str):
            return self.__has_variable_1(*args)
        elif isinstance(args[0], Assertion):
            return self.__has_variable_2(*args)
        else:
            raise ValueError

    def __has_variable_1(self, name: str) -> bool:
        return name in self.number_of_variables

    def __has_variable_2(self, ass: Assertion) -> bool:
        return self.has_variable(ass.get_name_without_degree())

    @typing.overload
    def get_nominal_variable(self, i1: str) -> Variable: ...

    @typing.overload
    def get_nominal_variable(self, i1: str, i2: str) -> Variable: ...

    def get_nominal_variable(self, *args) -> Variable:
        assert len(args) in [1, 2]
        assert isinstance(args[0], str)
        if len(args) == 1:
            return self.__get_nominal_variable_1(*args)
        else:
            assert isinstance(args[1], str)
            return self.__get_nominal_variable_2(*args)

    def __get_nominal_variable_1(self, i1: str) -> Variable:
        return self.get_nominal_variable(i1, i1)

    def __get_nominal_variable_2(self, i1: str, i2: str) -> Variable:
        var_name = f"{i1}:{{ {i2} }}"
        v: Variable = self.get_variable(var_name)
        v.set_type(VariableType.BINARY)
        return v

    def exists_nominal_variable(self, i: str) -> bool:
        var_name: str = f"{i}:{{ {i} }}"
        return var_name in list(map(str, self.variables))

    def get_negated_nominal_variable(self, i1: str, i2: str) -> Variable:
        var_name: str = f"{i1}: not {{ {i2} }}"
        flag: bool = var_name in list(map(str, self.variables))
        v: Variable = self.get_variable(var_name)
        if not flag:
            v.set_type(VariableType.BINARY)
            not_v: Variable = self.get_nominal_variable(i1, i2)
            self.add_new_constraint(
                Expression(1.0, Term(-1.0, v), Term(-1.0, not_v)), InequalityType.EQUAL
            )
        return v

    @typing.overload
    def add_new_constraint(
        self, expr: Expression, constraint_type: InequalityType
    ) -> None: ...

    @typing.overload
    def add_new_constraint(self, x: Variable, n: float) -> None: ...

    @typing.overload
    def add_new_constraint(self, ass: Assertion, n: float) -> None: ...

    @typing.overload
    def add_new_constraint(self, x: Variable, d: Degree) -> None: ...

    @typing.overload
    def add_new_constraint(self, ass: Assertion) -> None: ...

    @typing.overload
    def add_new_constraint(
        self, expr: Expression, constraint_type: InequalityType, degree: Degree
    ) -> None: ...

    @typing.overload
    def add_new_constraint(
        self, expr: Expression, constraint_type: InequalityType, n: float
    ) -> None: ...

    def add_new_constraint(self, *args) -> None:
        assert len(args) in [1, 2, 3]
        if len(args) == 1:
            assert isinstance(args[0], Assertion)
            self.__add_new_constraint_5(*args)
        elif len(args) == 2:
            if isinstance(args[0], Expression) and isinstance(args[1], InequalityType):
                self.__add_new_constraint_1(*args)
            elif isinstance(args[0], Variable) and isinstance(
                args[1], constants.NUMBER
            ):
                self.__add_new_constraint_2(*args)
            elif isinstance(args[0], Assertion) and isinstance(
                args[1], constants.NUMBER
            ):
                self.__add_new_constraint_3(*args)
            elif isinstance(args[0], Variable) and isinstance(args[1], Degree):
                self.__add_new_constraint_4(*args)
            else:
                raise ValueError
        elif len(args) == 3:
            if (
                isinstance(args[0], Expression)
                and isinstance(args[1], InequalityType)
                and isinstance(args[2], Degree)
            ):
                self.__add_new_constraint_6(*args)
            elif (
                isinstance(args[0], Expression)
                and isinstance(args[1], InequalityType)
                and isinstance(args[2], constants.NUMBER)
            ):
                self.__add_new_constraint_7(*args)
            else:
                raise ValueError
        else:
            raise ValueError

    def __add_new_constraint_1(
        self, expr: Expression, constraint_type: InequalityType
    ) -> None:
        self.constraints.append(Inequation(expr, constraint_type))

    def __add_new_constraint_2(self, x: Variable, n: float) -> None:
        self.add_new_constraint(
            Expression(Term(1.0, x)),
            InequalityType.GREATER_THAN,
            DegreeNumeric.get_degree(n),
        )

    def __add_new_constraint_3(self, ass: Assertion, n: float) -> None:
        self.add_new_constraint(self.get_variable(ass), n)

    def __add_new_constraint_4(self, x: Variable, d: Degree) -> None:
        self.add_new_constraint(
            Expression(Term(1.0, x)), InequalityType.GREATER_THAN, d
        )

    def __add_new_constraint_5(self, ass: Assertion) -> None:
        x_ass: Variable = self.get_variable(ass)
        ass_name: str = str(x_ass)
        deg: Degree = ass.get_lower_limit()
        if isinstance(deg, DegreeVariable):
            deg_name: str = str(typing.cast(DegreeVariable, deg).get_variable())
            if ass_name == deg_name:
                return
        self.add_new_constraint(x_ass, deg)

    def __add_new_constraint_6(
        self, expr: Expression, constraint_type: InequalityType, degree: Degree
    ) -> None:
        self.constraints.append(
            degree.create_inequality_with_degree_rhs(expr, constraint_type)
        )

    def __add_new_constraint_7(
        self, expr: Expression, constraint_type: InequalityType, n: float
    ) -> None:
        self.add_new_constraint(expr, constraint_type, DegreeNumeric.get_degree(n))

    def add_equality(self, var1: Variable, var2: Variable) -> None:
        self.add_new_constraint(
            Expression(Term(1.0, var1), Term(-1.0, var2)), InequalityType.EQUAL
        )

    def add_string_feature(self, role: str) -> None:
        self.string_features.add(role)

    def add_string_value(self, value: str, int_value: int) -> None:
        self.string_values[int_value] = value

    def change_variable_names(
        self, old_name: str, new_name: str, old_is_created_individual: bool
    ) -> None:
        old_values: list[str] = [f"{old_name},", f",{old_name}", f"{old_name}:"]
        new_values: list[str] = [f"{new_name},", f",{new_name}", f"{new_name}:"]
        to_process: list[Variable] = copy.deepcopy(self.variables)
        for v1 in to_process:
            name: str = str(v1)
            for old_value, new_value in zip(old_values, new_values):
                if old_value not in name:
                    continue
                name2: str = name.replace(old_value, new_value, 1)
                v2: Variable = self.get_variable(name2)
                if self.check_if_replacement_is_needed(v1, old_value, v2, new_value):
                    if old_is_created_individual:
                        self.add_equality(v1, v2)
                    else:
                        a_is_b: Variable = self.get_nominal_variable(new_name, old_name)
                        self.add_new_constraint(
                            Expression(
                                1.0, Term(-1.0, a_is_b), Term(1.0, v1), Term(-1.0, v2)
                            ),
                            InequalityType.GREATER_THAN,
                        )

    def check_if_replacement_is_needed(
        self, v1: Variable, s1: str, v2: Variable, s2: str
    ) -> bool:
        name1: str = str(v1)
        begin1: int = name1.index(s1)
        name2: str = str(v2)
        begin2: int = name2.index(s2)
        if begin1 != begin2:
            return False
        return (
            name1[:begin1] == name2[:begin2]
            and name1[begin1 + len(s1) :] == name2[begin2 + len(s2) :]
        )

    @typing.overload
    def get_ordered_permutation(self, x: list[Variable]) -> list[Variable]: ...

    @typing.overload
    def get_ordered_permutation(
        self, x: list[Variable], z: list[list[Variable]]
    ) -> list[Variable]: ...

    def get_ordered_permutation(self, *args) -> list[Variable]:
        assert len(args) in [1, 2]
        assert isinstance(args[0], list) and all(
            isinstance(a, Variable) for a in args[0]
        )
        if len(args) == 1:
            return self.__get_ordered_permutation_1(*args)
        elif len(args) == 2:
            assert isinstance(args[1], list) and all(
                isinstance(a, list) and all(isinstance(ai, Variable) for ai in a)
                for a in args[1]
            )
            return self.__get_ordered_permutation_2(*args)
        else:
            raise ValueError

    def __get_ordered_permutation_1(self, x: list[Variable]) -> list[Variable]:
        n: int = len(x)
        z: list[list[Variable]] = [
            [self.get_new_variable(VariableType.BINARY) for _ in range(n)]
            for _ in range(n)
        ]
        return self.get_ordered_permutation(x, z)

    def __get_ordered_permutation_2(
        self, x: list[Variable], z: list[list[Variable]]
    ) -> list[Variable]:
        n: int = len(x)
        y: list[Variable] = [
            self.get_new_variable(VariableType.SEMI_CONTINUOUS) for _ in range(n)
        ]
        for i in range(n - 1):
            self.add_new_constraint(
                Expression(Term(1.0, y[i]), Term(-1.0, y[i + 1])),
                InequalityType.GREATER_THAN,
            )
        for i in range(n):
            for j in range(n):
                self.add_new_constraint(
                    Expression(Term(1.0, x[j]), Term(-1.0, y[i]), Term(1.0, z[i][j])),
                    InequalityType.GREATER_THAN,
                )
        for i in range(n):
            for j in range(n):
                self.add_new_constraint(
                    Expression(Term(1.0, x[j]), Term(-1.0, y[i]), Term(-1.0, z[i][j])),
                    InequalityType.LESS_THAN,
                )
        for i in range(n):
            exp: Expression = Expression(1.0 - n)
            for j in range(n):
                exp.add_term(Term(1.0, z[i][j]))
            self.add_new_constraint(exp, InequalityType.EQUAL)

        for i in range(n):
            exp: Expression = Expression(1.0 - n)
            for j in range(n):
                exp.add_term(Term(1.0, z[j][i]))
            self.add_new_constraint(exp, InequalityType.EQUAL)
        return y

    def solve_gurobi(self, objective: Expression) -> typing.Optional[Solution]:
        import gurobipy as gp
        from gurobipy import GRB

        try:
            Util.debug(f"Objective function -> {objective}")

            num_binary_vars: int = 0
            num_free_vars: int = 0
            num_integer_vars: int = 0
            num_up_vars: int = 0
            size: int = len(self.variables)
            objective_value: list[float] = [0.0] * size

            if objective is not None:
                for term in objective.get_terms():
                    index = self.variables.index(term.get_var())
                    objective_value[index] += term.get_coeff()

            env = gp.Env(empty=True)
            if not ConfigReader.DEBUG_PRINT:
                env.setParam("OutputFlag", 0)
            env.setParam("IntFeasTol", 1e-9)
            env.setParam("BarConvTol", 0)
            env.start()

            model = gp.Model("model", env=env)
            vars_gurobi: dict[str, gp.Var] = dict()
            show_variable: list[bool] = [False] * size

            my_vars: list[Variable] = self.show_vars.get_variables()

            var_types: dict[VariableType, str] = {
                VariableType.BINARY: GRB.BINARY,
                VariableType.INTEGER: GRB.INTEGER,
                VariableType.CONTINUOUS: GRB.CONTINUOUS,
                VariableType.SEMI_CONTINUOUS: GRB.SEMICONT,
            }
            var_name_map: dict[str, str] = {
                str(v): f"x{i}" for i, v in enumerate(self.variables)
            }
            inv_var_name_map: dict[str, str] = {v: k for k, v in var_name_map.items()}

            for i, curr_variable in enumerate(self.variables):
                v_type: VariableType = curr_variable.get_type()
                ov: float = objective_value[i]

                Util.debug(
                    (
                        f"Variable -- "
                        f"[{curr_variable.get_lower_bound()}, {curr_variable.get_upper_bound()}] - "
                        f"Obj value = {ov} - "
                        f"Var type = {v_type.name} -- "
                        f"Var = {curr_variable}"
                    )
                )

                vars_gurobi[var_name_map[str(curr_variable)]] = model.addVar(
                    lb=curr_variable.get_lower_bound(),
                    ub=curr_variable.get_upper_bound(),
                    obj=ov,
                    vtype=var_types[v_type],
                    name=var_name_map[str(curr_variable)],
                )

                if curr_variable in my_vars:
                    show_variable[i] = True

                if v_type == VariableType.BINARY:
                    num_binary_vars += 1
                elif v_type == VariableType.CONTINUOUS:
                    num_free_vars += 1
                elif v_type == VariableType.INTEGER:
                    num_integer_vars += 1
                elif v_type == VariableType.SEMI_CONTINUOUS:
                    num_up_vars += 1

            model.update()

            Util.debug(f"# constraints -> {len(self.constraints)}")
            constraint_name: str = "constraint"
            for i, constraint in enumerate(self.constraints):
                if constraint in self.constraints[:i]:
                    continue
                if constraint.is_zero():
                    continue

                curr_name: str = f"{constraint_name}_{i + 1}"
                expr: gp.LinExpr = gp.LinExpr()
                for term in constraint.get_terms():
                    v: gp.Var = vars_gurobi[var_name_map[str(term.get_var())]]
                    c: float = term.get_coeff()
                    if c == 0:
                        continue
                    expr.add(v, c)

                if expr.size() == 0:
                    continue

                if constraint.get_type() == InequalityType.EQUAL:
                    gp_constraint: gp.Constr = expr == constraint.get_constant()
                elif constraint.get_type() == InequalityType.LESS_THAN:
                    gp_constraint: gp.Constr = expr <= constraint.get_constant()
                elif constraint.get_type() == InequalityType.GREATER_THAN:
                    gp_constraint: gp.Constr = expr >= constraint.get_constant()

                model.addConstr(gp_constraint, curr_name)
                Util.debug(f"{curr_name}: {constraint}")

            model.update()
            model.optimize()

            model.write(os.path.join(constants.RESULTS_PATH, "gurobi_model.lp"))
            model.write(os.path.join(constants.RESULTS_PATH, "gurobi_solution.json"))

            Util.debug(f"Model:")
            sol: Solution = None
            # if model.Status == GRB.INFEASIBLE and ConfigReader.RELAX_MILP:
            #     self.__gurobi_handle_model_infeasibility(model)

            if model.Status == GRB.INFEASIBLE:
                sol = Solution(False)
            else:
                for i in range(size):
                    if ConfigReader.DEBUG_PRINT or show_variable[i]:
                        name: str = self.variables[i].name
                        value: float = round(vars_gurobi[var_name_map[name]].X, 6)
                        if self.PRINT_VARIABLES:
                            Util.debug(f"{name} = {value}")
                        if self.PRINT_LABELS:
                            self.print_instance_of_labels(name, value)
                result: float = Util.round(abs(model.ObjVal))
                sol = Solution(result)

            model.printQuality()
            model.printStats()

            Util.debug(
                f"{constants.STAR_SEPARATOR}Statistics{constants.STAR_SEPARATOR}"
            )
            Util.debug("MILP problem:")
            Util.debug(f"\t\tSemi continuous variables: {num_up_vars}")
            Util.debug(f"\t\tBinary variables: {num_binary_vars}")
            Util.debug(f"\t\tContinuous variables: {num_free_vars}")
            Util.debug(f"\t\tInteger variables: {num_integer_vars}")
            Util.debug(f"\t\tTotal variables: {len(self.variables)}")
            Util.debug(f"\t\tConstraints: {len(self.constraints)}")
            return sol
        except gp.GurobiError as e:
            Util.error(f"Error code: {e.errno}. {e.message}")
            return None

    # def __gurobi_handle_model_infeasibility(self, model: typing.Any) -> None:
    #     import gurobipy as gp

    #     model: gp.Model = typing.cast(gp.Model, model)
    #     model.computeIIS()
    #     # Print out the IIS constraints and variables
    #     Util.debug("The following constraints and variables are in the IIS:")
    #     Util.debug("Constraints:")
    #     for c in model.getConstrs():
    #         assert isinstance(c, gp.Constr)
    #         if c.IISConstr:
    #             Util.debug(f"\t\t{c.ConstrName}: {model.getRow(c)} {c.Sense} {c.RHS}")

    #     Util.debug("Variables:")
    #     for v in model.getVars():
    #         if v.IISLB:
    #             Util.debug(f"\t\t{v.VarName} ≥ {v.LB}")
    #         if v.IISUB:
    #             Util.debug(f"\t\t{v.VarName} ≤ {v.UB}")

    #     Util.debug("Relaxing the variable bounds:")
    #     # relaxing only variable bounds
    #     model.feasRelaxS(0, False, True, False)
    #     # for relaxing variable bounds and constraint bounds use
    #     # model.feasRelaxS(0, False, True, True)
    #     model.optimize()

    def solve_mip(self, objective: Expression) -> typing.Optional[Solution]:
        import mip

        try:
            Util.debug(f"Objective function -> {objective}")

            num_binary_vars: int = 0
            num_free_vars: int = 0
            num_integer_vars: int = 0
            num_up_vars: int = 0
            size: int = len(self.variables)
            objective_value: list[float] = [0.0] * size

            if objective is not None:
                for term in objective.get_terms():
                    index = self.variables.index(term.get_var())
                    objective_value[index] += term.get_coeff()

            model: mip.Model = mip.Model(
                name="FuzzyDL", sense=mip.MINIMIZE, solver_name=mip.CBC
            )
            model.verbose = 0
            model.infeas_tol = 1e-9
            model.integer_tol = 1e-9
            model.max_mip_gap = ConfigReader.EPSILON
            model.emphasis = mip.SearchEmphasis.OPTIMALITY
            model.opt_tol = 0
            model.preprocess = 1

            if ConfigReader.DEBUG_PRINT:
                model.verbose = 1

            vars_mip: dict[str, mip.Var] = dict()
            show_variable: list[bool] = [False] * size

            my_vars: list[Variable] = self.show_vars.get_variables()
            var_types: dict[VariableType, str] = {
                VariableType.BINARY: mip.BINARY,
                VariableType.INTEGER: mip.INTEGER,
                VariableType.CONTINUOUS: mip.CONTINUOUS,
                VariableType.SEMI_CONTINUOUS: mip.CONTINUOUS,
            }
            var_name_map: dict[str, str] = {
                str(v): f"x{i}" for i, v in enumerate(self.variables)
            }
            inv_var_name_map: dict[str, str] = {v: k for k, v in var_name_map.items()}

            for i, curr_variable in enumerate(self.variables):
                v_type: VariableType = curr_variable.get_type()
                ov: float = objective_value[i]

                Util.debug(
                    (
                        f"Variable -- "
                        f"[{curr_variable.get_lower_bound()}, {curr_variable.get_upper_bound()}] - "
                        f"Obj value = {ov} - "
                        f"Var type = {v_type.name} -- "
                        f"Var = {curr_variable}"
                    )
                )

                vars_mip[var_name_map[str(curr_variable)]] = model.add_var(
                    name=var_name_map[str(curr_variable)],
                    var_type=var_types[v_type],
                    lb=curr_variable.get_lower_bound(),
                    ub=curr_variable.get_upper_bound(),
                    obj=ov,
                )

                if curr_variable in my_vars:
                    show_variable[i] = True

                if v_type == VariableType.BINARY:
                    num_binary_vars += 1
                elif v_type == VariableType.CONTINUOUS:
                    num_free_vars += 1
                elif v_type == VariableType.INTEGER:
                    num_integer_vars += 1
                elif v_type == VariableType.SEMI_CONTINUOUS:
                    num_up_vars += 1

            Util.debug(f"# constraints -> {len(self.constraints)}")
            constraint_name: str = "constraint"
            for i, constraint in enumerate(self.constraints):
                if constraint in self.constraints[:i]:
                    continue
                if constraint.is_zero():
                    continue
                curr_name: str = f"{constraint_name}_{i + 1}"
                expr: mip.LinExpr = mip.xsum(
                    term.get_coeff() * vars_mip[var_name_map[str(term.get_var())]]
                    for term in constraint.get_terms()
                )

                if constraint.get_type() == InequalityType.EQUAL:
                    gp_constraint: mip.Constr = expr == constraint.get_constant()
                elif constraint.get_type() == InequalityType.LESS_THAN:
                    gp_constraint: mip.Constr = expr <= constraint.get_constant()
                elif constraint.get_type() == InequalityType.GREATER_THAN:
                    gp_constraint: mip.Constr = expr >= constraint.get_constant()

                model.add_constr(gp_constraint, curr_name)
                Util.debug(f"{curr_name}: {constraint}")

            model.objective = mip.xsum(
                ov * vars_mip[var_name_map[str(self.variables[i])]]
                for i, ov in enumerate(objective_value)
                if ov != 0
            )

            # model.optimize(relax=ConfigReader.RELAX_MILP)
            model.optimize()

            model.write(os.path.join(constants.RESULTS_PATH, "mip_model.lp"))

            Util.debug(f"Model:")
            sol: Solution = None
            if model.status == mip.OptimizationStatus.INFEASIBLE:
                sol = Solution(False)
            else:
                model.write(os.path.join(constants.RESULTS_PATH, "mip_solution.sol"))
                for i in range(size):
                    if ConfigReader.DEBUG_PRINT or show_variable[i]:
                        name: str = self.variables[i].name
                        value: float = round(vars_mip[var_name_map[name]].x, 6)
                        if self.PRINT_VARIABLES:
                            Util.debug(f"{name} = {value}")
                        if self.PRINT_LABELS:
                            self.print_instance_of_labels(name, value)
                result: float = Util.round(abs(model.objective_value))
                sol = Solution(result)

            Util.debug(
                f"{constants.STAR_SEPARATOR}Statistics{constants.STAR_SEPARATOR}"
            )
            Util.debug("MILP problem:")
            Util.debug(f"\t\tSemi continuous variables: {num_up_vars}")
            Util.debug(f"\t\tBinary variables: {num_binary_vars}")
            Util.debug(f"\t\tContinuous variables: {num_free_vars}")
            Util.debug(f"\t\tInteger variables: {num_integer_vars}")
            Util.debug(f"\t\tTotal variables: {len(self.variables)}")
            Util.debug(f"\t\tConstraints: {len(self.constraints)}")
            return sol
        except Exception as e:
            Util.error(f"Error: {e} {traceback.format_exc()}")
            return None

    def solve_pulp(self, objective: Expression) -> typing.Optional[Solution]:
        import pulp

        try:
            Util.debug(f"Objective function -> {objective}")

            num_binary_vars: int = 0
            num_free_vars: int = 0
            num_integer_vars: int = 0
            num_up_vars: int = 0
            size: int = len(self.variables)
            objective_value: list[float] = [0.0] * size
            show_variable: list[bool] = [False] * size
            my_vars: list[Variable] = self.show_vars.get_variables()

            if objective is not None:
                for term in objective.get_terms():
                    objective_value[
                        self.variables.index(term.get_var())
                    ] += term.get_coeff()

            model = pulp.LpProblem(
                f"FuzzyDL-{ConfigReader.MILP_PROVIDER.upper()}", pulp.LpMinimize
            )

            var_types: dict[VariableType, str] = {
                VariableType.BINARY: pulp.LpBinary,
                VariableType.INTEGER: pulp.LpInteger,
                VariableType.CONTINUOUS: pulp.LpContinuous,
                VariableType.SEMI_CONTINUOUS: pulp.LpContinuous,
            }

            vars_pulp: dict[str, pulp.LpVariable] = dict()
            var_name_map: dict[str, str] = {
                str(v): f"x{i}" for i, v in enumerate(self.variables)
            }
            semicontinuous_var_counter: int = 1
            semicontinuous_var_name: str = "semic_z"
            for i, curr_variable in enumerate(self.variables):
                v_type: VariableType = curr_variable.get_type()
                Util.debug(
                    (
                        f"Variable -- "
                        f"[{curr_variable.get_lower_bound()}, {curr_variable.get_upper_bound()}] - "
                        f"Obj value = {objective_value[i]} - "
                        f"Var type = {v_type.name} -- "
                        f"Var = {curr_variable}"
                    )
                )

                vars_pulp[var_name_map[str(curr_variable)]] = pulp.LpVariable(
                    name=var_name_map[str(curr_variable)],
                    lowBound=(
                        curr_variable.get_lower_bound()
                        if curr_variable.get_lower_bound() != float("-inf")
                        else None
                    ),
                    upBound=(
                        curr_variable.get_upper_bound()
                        if curr_variable.get_upper_bound() != float("inf")
                        else None
                    ),
                    cat=var_types[v_type],
                )

                if curr_variable in my_vars:
                    show_variable[i] = True

                if (
                    v_type == VariableType.SEMI_CONTINUOUS
                    and ConfigReader.MILP_PROVIDER
                    in [
                        MILPProvider.PULP_GLPK,
                        MILPProvider.PULP_CPLEX,
                    ]
                ):
                    # Semi Continuous variables are not handled by GLPK and HiGHS
                    # if x in [L, U] u {0} is semi continuous, then add the following constraints
                    # L * y <= x <= U * y, where y in {0, 1} is a binary variable
                    bin_var = pulp.LpVariable(
                        name=f"{semicontinuous_var_name}{semicontinuous_var_counter}",
                        cat=pulp.LpBinary,
                    )
                    constraint_1 = (
                        vars_pulp[var_name_map[str(curr_variable)]]
                        >= bin_var * curr_variable.get_lower_bound()
                    )
                    constraint_2 = (
                        vars_pulp[var_name_map[str(curr_variable)]]
                        <= bin_var * curr_variable.get_upper_bound()
                    )
                    if constraint_1 not in model.constraints.values():
                        model.addConstraint(
                            constraint_1, name=f"constraint_{bin_var.name}_1"
                        )
                    if constraint_2 not in model.constraints.values():
                        model.addConstraint(
                            constraint_2, name=f"constraint_{bin_var.name}_2"
                        )
                    semicontinuous_var_counter += 1
                    Util.debug(
                        (
                            f"New Variable -- "
                            f"[{bin_var.lowBound}, {bin_var.upBound}] - "
                            f"Var type = {bin_var.cat} -- "
                            f"Var = {bin_var.name}"
                        )
                    )
                    Util.debug(f"New Constraint 1 -- {constraint_1}")
                    Util.debug(f"New Constraint 2 -- {constraint_2}")

                if v_type == VariableType.BINARY:
                    num_binary_vars += 1
                elif v_type == VariableType.CONTINUOUS:
                    num_free_vars += 1
                elif v_type == VariableType.INTEGER:
                    num_integer_vars += 1
                elif v_type == VariableType.SEMI_CONTINUOUS:
                    num_up_vars += 1

            Util.debug(f"# constraints -> {len(self.constraints)}")
            constraint_name: str = "constraint"
            pulp_sense: dict[InequalityType, int] = {
                InequalityType.EQUAL: pulp.LpConstraintEQ,
                InequalityType.LESS_THAN: pulp.LpConstraintLE,
                InequalityType.GREATER_THAN: pulp.LpConstraintGE,
            }
            for i, constraint in enumerate(self.constraints):
                if constraint in self.constraints[:i]:
                    continue
                # ignore zero constraints
                if constraint.is_zero():
                    continue

                curr_name: str = f"{constraint_name}_{i + 1}"
                pulp_expr: pulp.LpAffineExpression = pulp.lpSum(
                    term.get_coeff() * vars_pulp[var_name_map[str(term.get_var())]]
                    for term in constraint.get_terms()
                )
                pulp_constraint: pulp.LpConstraint = pulp.LpConstraint(
                    e=pulp_expr,
                    sense=pulp_sense[constraint.get_type()],
                    rhs=constraint.get_constant(),
                )

                # ignore zero constraints of type a * x - a * x
                if (
                    len(pulp_constraint) == 1
                    and list(pulp_constraint.values())[0] == 0
                    and pulp_constraint.constant == 0
                ):
                    continue

                model.addConstraint(pulp_constraint, name=curr_name)
                Util.debug(f"{curr_name}: {constraint}")

            if ConfigReader.MILP_PROVIDER == MILPProvider.PULP:
                solver = pulp.PULP_CBC_CMD(
                    mip=True,
                    msg=ConfigReader.DEBUG_PRINT,
                    gapRel=1e-9,
                    presolve=True,
                    keepFiles=False,  # ConfigReader.DEBUG_PRINT,
                    logPath=(
                        os.path.join(".", "logs", f"pulp_{pulp.PULP_CBC_CMD.name}.log")
                        if ConfigReader.DEBUG_PRINT
                        else None
                    ),
                    options=[
                        "--primalTolerance",  # feasibility tolerance
                        "1e-9",
                        "--integerTolerance",  # integer feasibility tolerance
                        "1e-9",
                        "--ratioGap",  # relative mip gap
                        str(ConfigReader.EPSILON),
                        "--allowableGap",  # optimality gap tolerance
                        "0",
                        "--preprocess",  # enable preprocessing
                        "on",
                    ],
                )
            elif ConfigReader.MILP_PROVIDER == MILPProvider.PULP_GLPK:
                solver = pulp.GLPK_CMD(
                    mip=True,
                    msg=ConfigReader.DEBUG_PRINT,
                    keepFiles=False,  # ConfigReader.DEBUG_PRINT,
                    options=[
                        "--presol",  # use presolver (default; assumes --scale and --adv)
                        "--exact",  # use simplex method based on exact arithmetic
                        "--xcheck",  # check final basis using exact arithmetic
                        "--intopt",  # enforce MIP (Mixed Integer Programming)
                        "--mipgap",
                        str(
                            ConfigReader.EPSILON
                        ),  # no relative gap between primal & best bound
                    ]
                    + (
                        [
                            "--log",
                            os.path.join(".", "logs", f"pulp_{pulp.GLPK_CMD.name}.log"),
                        ]
                        if ConfigReader.DEBUG_PRINT
                        else []
                    ),
                )
            elif ConfigReader.MILP_PROVIDER == MILPProvider.PULP_HIGHS:
                solver = pulp.HiGHS(
                    mip=True,
                    msg=ConfigReader.DEBUG_PRINT,
                    gapRel=1e-6,
                    log_file=(
                        os.path.join(".", "logs", f"pulp_{pulp.HiGHS.name}.log")
                        if ConfigReader.DEBUG_PRINT
                        else None
                    ),
                    primal_feasibility_tolerance=1e-9,
                    dual_feasibility_tolerance=1e-9,
                    mip_feasibility_tolerance=1e-9,
                    presolve="on",
                    parallel="on",
                    write_solution_to_file=True,
                    write_solution_style=1,
                    solution_file=os.path.join(
                        constants.RESULTS_PATH, "highs_solution.sol"
                    ),
                    write_model_file=os.path.join(
                        constants.RESULTS_PATH, "highs_model.lp"
                    ),
                )
            elif ConfigReader.MILP_PROVIDER == MILPProvider.PULP_CPLEX:
                solver = pulp.CPLEX_CMD(
                    # path="/Applications/CPLEX_Studio2211/cplex/bin/arm64_osx/cplex",
                    mip=True,
                    msg=ConfigReader.DEBUG_PRINT,
                    gapRel=1e-9,
                    keepFiles=False,  # ConfigReader.DEBUG_PRINT,
                    logPath=(
                        os.path.join(".", "logs", f"pulp_{pulp.CPLEX_CMD.name}.log")
                        if ConfigReader.DEBUG_PRINT
                        else None
                    ),
                )

            model.objective = pulp.lpSum(
                ov * vars_pulp[var_name_map[str(self.variables[i])]]
                for i, ov in enumerate(objective_value)
                if ov != 0
            )
            result = model.solve(solver=solver)
            if ConfigReader.MILP_PROVIDER == MILPProvider.PULP_CPLEX:
                for file in os.listdir("./"):
                    if "clone" in file:
                        os.remove(file)

            Util.debug(f"Model:")
            sol: Solution = None
            if result != pulp.LpStatusOptimal:
                sol = Solution(False)
            else:
                var_dict: dict[str, pulp.LpVariable] = model.variablesDict()
                for i in range(size):
                    if ConfigReader.DEBUG_PRINT or show_variable[i]:
                        name: str = self.variables[i].name
                        value: float = (
                            round(var_dict[var_name_map[name]].value(), 6)
                            if var_name_map[name] in var_dict
                            else 0.0
                        )
                        if self.PRINT_VARIABLES:
                            Util.debug(f"{name} = {value}")
                        if self.PRINT_LABELS:
                            self.print_instance_of_labels(name, value)
                result: float = Util.round(abs(model.objective.value()))
                sol = Solution(result)

            Util.debug(
                f"{constants.STAR_SEPARATOR}Statistics{constants.STAR_SEPARATOR}"
            )
            Util.debug("MILP problem:")
            Util.debug(f"\t\tSemi continuous variables: {num_up_vars}")
            Util.debug(f"\t\tBinary variables: {num_binary_vars}")
            Util.debug(f"\t\tContinuous variables: {num_free_vars}")
            Util.debug(f"\t\tInteger variables: {num_integer_vars}")
            Util.debug(f"\t\tTotal variables: {len(self.variables)}")
            Util.debug(f"\t\tConstraints: {len(self.constraints)}")
            return sol
        except Exception as e:
            Util.error(f"Error: {e} {traceback.format_exc()}")
            return None

    # def solve_scipy(self, objective: Expression) -> typing.Optional[Solution]:
    #     import numpy as np
    #     from scipy.optimize import milp, OptimizeResult, LinearConstraint, Bounds, linprog, linprog_verbose_callback, show_options

    #     num_binary_vars: int = 0
    #     num_free_vars: int = 0
    #     num_integer_vars: int = 0
    #     num_up_vars: int = 0
    #     size: int = len(self.variables)
    #     objective_value: list[float] = [0.0] * size
    #     show_variable: list[bool] = [False] * size
    #     my_vars: list[Variable] = self.show_vars.get_variables()

    #     if objective is not None:
    #         for term in objective.get_terms():
    #             index = self.variables.index(term.get_var())
    #             objective_value[index] += term.get_coeff()

    #     var_types: dict[VariableType, str] = {
    #         VariableType.BINARY: 1,
    #         VariableType.CONTINUOUS: 0,
    #         VariableType.INTEGER: 1,
    #         VariableType.SEMI_CONTINUOUS: 2,
    #     }

    #     for i, curr_variable in enumerate(self.variables):
    #         v_type: VariableType = curr_variable.get_type()

    #         Util.debug(
    #             (
    #                 f"Variable -- "
    #                 f"[{curr_variable.get_lower_bound()}, {curr_variable.get_upper_bound()}] - "
    #                 f"Obj value = {objective_value[i]} - "
    #                 f"Var type = {v_type.name} -- "
    #                 f"Var = {curr_variable}"
    #             )
    #         )

    #         if curr_variable in my_vars:
    #             show_variable[i] = True

    #         if v_type == VariableType.BINARY:
    #             num_binary_vars += 1
    #         elif v_type == VariableType.CONTINUOUS:
    #             num_free_vars += 1
    #         elif v_type == VariableType.INTEGER:
    #             num_integer_vars += 1
    #         elif v_type == VariableType.SEMI_CONTINUOUS:
    #             num_up_vars += 1

    #     Util.debug(f"# constraints -> {len(self.constraints)}")
    #     constraint_name: str = "constraint"
    #     matrix_A = np.zeros((len(self.constraints), len(self.variables)))
    #     inequality_A = np.zeros((len(self.constraints), len(self.variables)))
    #     equality_A = np.zeros((len(self.constraints), len(self.variables)))
    #     lb = np.zeros(len(self.constraints))
    #     ub = np.zeros(len(self.constraints))
    #     in_ub = np.zeros(len(self.constraints))
    #     eq_ub = np.zeros(len(self.constraints))
    #     for i, constraint in enumerate(self.constraints):
    #         curr_name: str = f"{constraint_name}_{i + 1}"
    #         row = np.zeros(len(self.variables))
    #         for term in constraint.get_terms():
    #             row[self.variables.index(term.get_var())] = term.get_coeff()
    #         if np.allclose(row, 0):
    #             continue
    #         Util.debug(f"{curr_name}: {constraint}")
    #         matrix_A[i, :] = row
    #         if constraint.type == InequalityType.EQUAL:
    #             equality_A[i, :] = row
    #             eq_ub[i] = constraint.get_constant()

    #             lb[i] = constraint.get_constant()
    #             ub[i] = constraint.get_constant()
    #         elif constraint.type == InequalityType.LESS_THAN:
    #             inequality_A[i, :] = row
    #             in_ub[i] = constraint.get_constant()

    #             lb[i] = -np.inf
    #             ub[i] = constraint.get_constant()
    #         elif constraint.type == InequalityType.GREATER_THAN:
    #             inequality_A[i, :] = -row
    #             in_ub[i] = -constraint.get_constant()

    #             lb[i] = constraint.get_constant()
    #             ub[i] = np.inf

    #     indices = np.all(matrix_A == 0, axis=1)
    #     matrix_A = np.delete(matrix_A, indices, axis=0)
    #     lb = np.delete(lb, indices, axis=0)
    #     ub = np.delete(ub, indices, axis=0)

    #     indices = np.all(inequality_A == 0, axis=1)
    #     inequality_A = np.delete(inequality_A, indices, axis=0)
    #     in_ub = np.delete(in_ub, indices, axis=0)

    #     indices = np.all(equality_A == 0, axis=1)
    #     equality_A = np.delete(equality_A, indices, axis=0)
    #     eq_ub = np.delete(eq_ub, indices, axis=0)

    #     bounds = Bounds(
    #         [var.get_lower_bound() for var in self.variables],
    #         [var.get_upper_bound() for var in self.variables],
    #         keep_feasible=True,
    #     )
    #     integrality = np.array([var_types[var.get_type()] for var in self.variables])
    #     constraint = LinearConstraint(
    #         matrix_A, lb, ub, keep_feasible=True
    #     )

    #     result: OptimizeResult = milp(
    #         c=np.array(objective_value),
    #         integrality=integrality,
    #         constraints=constraint,
    #         bounds=bounds,
    #         options={
    #             "disp": ConfigReader.DEBUG_PRINT,
    #             "presolve": True,
    #             "mip_rel_gap": 1e-6,
    #         },
    #     )

    #     result: OptimizeResult = linprog(
    #         c=np.array(objective_value),
    #         A_ub=inequality_A,
    #         b_ub=in_ub,
    #         A_eq=equality_A,
    #         b_eq=eq_ub,
    #         method="highs-ipm",
    #         integrality=integrality,
    #         bounds=[(var.get_lower_bound(), var.get_upper_bound()) for var in self.variables],
    #         options={
    #             "disp": ConfigReader.DEBUG_PRINT,
    #             "presolve": False,
    #             "mip_rel_gap": 1e-3,
    #             "ipm_optimality_tolerance": 1e-5,
    #         },
    #         # callback=linprog_verbose_callback if ConfigReader.DEBUG_PRINT else None
    #     )

    #     Util.debug(f"Model:\n{result}")

    #     sol: Solution = None
    #     if not result.success:
    #         sol = Solution(False)
    #     else:
    #         for i in range(size):
    #             if ConfigReader.DEBUG_PRINT or show_variable[i]:
    #                 name: str = self.variables[i].name
    #                 value: float = (
    #                     round(result.x[i], 6)
    #                 )
    #                 if self.PRINT_VARIABLES:
    #                     Util.debug(f"{name} = {value}")
    #                 if self.PRINT_LABELS:
    #                     self.print_instance_of_labels(name, value)
    #         result: float = Util.round(abs(result.fun))
    #         sol = Solution(result)

    #     Util.debug(
    #         f"{constants.STAR_SEPARATOR}Statistics{constants.STAR_SEPARATOR}"
    #     )
    #     Util.debug("MILP problem:")
    #     Util.debug(f"\t\tSemi continuous variables: {num_up_vars}")
    #     Util.debug(f"\t\tBinary variables: {num_binary_vars}")
    #     Util.debug(f"\t\tContinuous variables: {num_free_vars}")
    #     Util.debug(f"\t\tInteger variables: {num_integer_vars}")
    #     Util.debug(f"\t\tTotal variables: {len(self.variables)}")
    #     Util.debug(f"\t\tConstraints: {len(self.constraints)}")
    #     return sol

    def add_crisp_concept(self, concept_name: str) -> None:
        self.crisp_concepts.add(concept_name)

    def add_crisp_role(self, role_name: str) -> None:
        self.crisp_roles.add(role_name)

    def is_crisp_concept(self, concept_name: str) -> bool:
        return concept_name in self.crisp_concepts

    def is_crisp_role(self, role_name: str) -> bool:
        return role_name in self.crisp_roles

    def set_binary_variables(self) -> None:
        for v in self.variables:
            if v.get_datatype_filler_type() or v.get_type() in (
                VariableType.CONTINUOUS,
                VariableType.INTEGER,
            ):
                continue
            v.set_binary_variable()

    def get_name_for_integer(self, i: int) -> typing.Optional[str]:
        for name, i2 in self.number_of_variables.items():
            if i == i2:
                return name
        return None

    def get_number_for_assertion(self, ass: Assertion) -> int:
        return self.number_of_variables.get(str(self.get_variable(ass)))

    def add_contradiction(self) -> None:
        self.constraints.clear()
        self.add_new_constraint(Expression(1.0), InequalityType.EQUAL)
