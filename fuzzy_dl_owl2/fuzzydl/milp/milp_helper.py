from __future__ import annotations

import copy
import os
import typing

import gurobipy as gp
from gurobipy import GRB

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
from fuzzy_dl_owl2.fuzzydl.util.config_reader import ConfigReader
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

    def optimize(self, objective: Expression) -> Solution:
        return self.solve_gurobi(objective)

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
        try:
            Util.debug("Running MILP solver: Gurobi")
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
            vars_gurobi: list[gp.Var] = []
            show_variable: list[bool] = [False] * size

            my_vars: list[Variable] = self.show_vars.get_variables()

            for i in range(size):
                v: Variable = self.variables[i]
                v_type: VariableType = v.get_type()
                ov: float = objective_value[i]

                Util.debug(
                    (
                        f"Variable -- "
                        f"[{v.get_lower_bound()}, {v.get_upper_bound()}] - "
                        f"Obj value = {ov} - "
                        f"Var type = {v_type.name} -- "
                        f"Var = {v}"
                    )
                )

                vars_gurobi.append(
                    model.addVar(
                        lb=v.get_lower_bound(),
                        ub=v.get_upper_bound(),
                        obj=ov,
                        vtype=v_type.name,
                        name=str(v),
                    )
                )

                if v in my_vars:
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
                curr_name: str = f"{constraint_name}_{i + 1}"
                expr: gp.LinExpr = gp.LinExpr()
                for term in constraint.get_terms():
                    index: int = self.variables.index(term.get_var())
                    v: gp.Var = vars_gurobi[index]
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
                Util.debug(f"{curr_name}: {gp_constraint}")

            model.update()
            model.optimize()

            model.write(os.path.join(constants.RESULTS_PATH, "model.lp"))
            model.write(os.path.join(constants.RESULTS_PATH, "solution.json"))

            Util.debug(f"Model:")
            sol: Solution = None
            if model.Status == GRB.INFEASIBLE and ConfigReader.RELAX_MILP:
                self.__handle_model_infeasibility(model)

            if model.Status == GRB.INFEASIBLE:
                sol = Solution(False)
            else:
                for i in range(size):
                    if ConfigReader.DEBUG_PRINT or show_variable[i]:
                        name: str = vars_gurobi[i].VarName
                        value: float = round(vars_gurobi[i].X, 6)
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

    def __handle_model_infeasibility(self, model: gp.Model) -> None:
        model.computeIIS()
        # Print out the IIS constraints and variables
        Util.debug("The following constraints and variables are in the IIS:")
        Util.debug("Constraints:")
        for c in model.getConstrs():
            assert isinstance(c, gp.Constr)
            if c.IISConstr:
                Util.debug(f"\t\t{c.ConstrName}: {model.getRow(c)} {c.Sense} {c.RHS}")

        Util.debug("Variables:")
        for v in model.getVars():
            if v.IISLB:
                Util.debug(f"\t\t{v.VarName} ≥ {v.LB}")
            if v.IISUB:
                Util.debug(f"\t\t{v.VarName} ≤ {v.UB}")

        Util.debug("Relaxing the variable bounds:")
        # relaxing only variable bounds
        model.feasRelaxS(0, False, True, False)
        # for relaxing variable bounds and constraint bounds use
        # model.feasRelaxS(0, False, True, True)
        model.optimize()

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
