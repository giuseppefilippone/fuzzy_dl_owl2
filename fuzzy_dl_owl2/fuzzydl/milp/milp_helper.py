from __future__ import annotations

import copy
import os
import re
import time
import traceback
import typing

import networkx as nx

from fuzzy_dl_owl2.fuzzydl.assertion.assertion import Assertion
from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.concept.interface.has_value_interface import (
    HasValueInterface,
)
from fuzzy_dl_owl2.fuzzydl.concept.sigma_count import SigmaCount
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
    MILPProvider,
    VariableType,
)
from fuzzy_dl_owl2.fuzzydl.util.util import Util


# @utils.singleton
class MILPHelper:
    """MILP problem manager, storing the problem and calling an external solver."""

    PARTITION: bool = False
    # Indicates whether we want to show the membership degrees to linguistic labels or not.
    PRINT_LABELS: bool = True
    # Indicates whether we want to show the value of the variables or not.
    PRINT_VARIABLES: bool = True

    def __init__(self) -> None:
        self.nominal_variables: bool = False
        self.cardinalities: list[SigmaCount] = list()
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
        milp.nominal_variables = self.nominal_variables
        milp.cardinalities = [c.clone() for c in self.cardinalities]
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
        """
        It optimizes an expression using a solvers from MILPProvider.

        Args:
            objective (Expression): Expression to be optimized.

        Raises:
            ValueError: If MILPProvider is not known.

        Returns:
            typing.Optional[Solution]: An optimal solution of the expression
        """
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
        """Shows the membership degrees to some linguistic labels."""
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
        """
        Shows the membership degrees to some linguistic labels.

        Args:
            f_name (str): Name of the feature.
            ind_name (str): Name of the individual.
            value (float): Value of the feature for the given individual.
        """
        name: str = f"{f_name}({ind_name})"
        labels = self.show_vars.get_labels(name)
        for f in labels:
            Util.info(
                f"{name} is {f.compute_name()} = {f.get_membership_degree(value)}"
            )

    def __print_instance_of_labels_2(self, name: str, value: float) -> None:
        """
        Shows the membership degrees to some linguistic labels.

        Args:
            name (str): Name of the feature (individual).
            value (float): Value of the feature for the given individual.
        """
        labels = self.show_vars.get_labels(name)
        for f in labels:
            Util.info(
                f"{name} is {f.compute_name()} = {f.get_membership_degree(value)}"
            )

    def get_new_variable(self, v_type: VariableType) -> Variable:
        """Gets a new variable with the indicated type."""
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
        """
        Gets a variable with the given name, creating a new one of type SEMI_CONTINUOUS in [0, 1] if it does not exist.
        """
        if var_name in self.number_of_variables:
            for variable in self.variables:
                if str(variable) == var_name:
                    return variable
        var: Variable = Variable(var_name, VariableType.SEMI_CONTINUOUS)
        self.variables.append(var)
        self.number_of_variables[str(var)] = len(self.variables)
        return var

    def __get_variable_2(self, var_name: str, v_type: VariableType) -> Variable:
        """
        Gets a variable with the indicated name and bound.

        Only used by DatatypeReasoner.
        """
        var: Variable = self.get_variable(var_name)
        var.set_type(v_type)
        return var

    def __get_variable_3(self, ass: Assertion) -> Variable:
        """
        Gets a variable taking the value of a concept assertion, creating a new one of type SEMI_CONTINUOUS in [0, 1] if it does not exist.

        Args:
            ass (Assertion): A fuzzy concept assertion.

        Returns:
            Variable: A variable taking the value of the assertion.
        """
        return self.get_variable(ass.get_individual(), ass.get_concept())

    def __get_variable_4(self, rel: Relation) -> Variable:
        """
        Gets a variable taking the value of a role assertion, creating a new one of type SEMI_CONTINUOUS in [0, 1] if it does not exist.

        Args:
            ass (Assertion): A fuzzy role assertion.

        Returns:
            Variable: A variable taking the value of the assertion.
        """
        a: Individual = rel.get_subject_individual()
        b: Individual = rel.get_object_individual()
        role: str = rel.get_role_name()
        return self.get_variable(a, b, role)

    def __get_variable_5(self, ind: Individual, restrict: Restriction) -> Variable:
        """
        Gets a variable taking the value of a universal restriction, creating a new one of type SEMI_CONTINUOUS in [0, 1] if it does not exist.

        Args:
            ind (Individual): Subject individual of the restrictions.
            restrict (Restriction): A fuzzy role assertion.

        Returns:
            Variable: A variable taking the value of the assertion.
        """
        var: Variable = self.get_variable(f"{ind}:{restrict.get_name_without_degree()}")
        if self.show_vars.show_individuals(str(ind)):
            self.show_vars.add_variable(var, str(var))
        return var

    def __get_variable_6(self, ind: Individual, c: Concept) -> Variable:
        """
        Gets a variable taking the value of a concept assertion, creating a new one of type SEMI_CONTINUOUS in [0, 1] if it does not exist.

        Args:
            ind (Individual): An individual.
            c (Concept): A fuzzy concept.

        Returns:
            Variable: A variable taking the value of the assertion.
        """
        if c.type == ConceptType.HAS_VALUE:
            assert isinstance(c, HasValueInterface)

            r: str = c.role
            b: str = str(c.value)
            return self.get_variable(str(ind), b, r, VariableType.SEMI_CONTINUOUS)
        return self.get_variable(ind, str(c))

    def __get_variable_7(self, ind: Individual, concept_name: str) -> Variable:
        """
        Gets a variable taking the value of a concept assertion, creating a new one of type SEMI_CONTINUOUS in [0, 1] if it does not exist.

        Args:
            ind (Individual): An individual.
            concept_name (str): A fuzzy concept name.

        Returns:
            Variable: A variable taking the value of the assertion.
        """
        var: Variable = self.get_variable(f"{ind}:{concept_name}")
        if concept_name in self.crisp_concepts:
            var.set_binary_variable()
        if self.show_vars.show_individuals(str(ind)) or self.show_vars.show_concepts(
            concept_name
        ):
            self.show_vars.add_variable(var, str(var))
        return var

    def __get_variable_8(self, a: Individual, b: Individual, role: str) -> Variable:
        """
        Gets a variable taking the value of a role assertion, creating a new one of type SEMI_CONTINUOUS in [0, 1] if it does not exist.

        Args:
            a (Individual): Object individual.
            b (Individual): Subject individual.
            role (str): A role name.

        Returns:
            Variable: A variable taking the value of the assertion.
        """
        return self.get_variable(a, b, role, VariableType.SEMI_CONTINUOUS)

    def __get_variable_9(
        self, a: Individual, b: Individual, role: str, v_type: VariableType
    ) -> Variable:
        """
        Gets a variable taking the value of a role assertion, creating a new one of type SEMI_CONTINUOUS in [0, 1] if it does not exist.

        Args:
            a (Individual): Object individual.
            b (Individual): Subject individual.
            role (str): A role name.
            v_type (VariableType): Type of the variable.

        Returns:
            Variable: A variable taking the value of the assertion.
        """
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
        """
        Gets a variable taking the value of a concrete individual.

        Args:
            ind (CreatedIndividual): A concrete individual.

        Returns:
            Variable: A variable taking the value of the assertion.
        """
        return self.get_variable(ind, VariableType.CONTINUOUS)

    def __get_variable_12(self, ind: CreatedIndividual, v_type: VariableType) -> None:
        """
        Gets a variable taking the value of a concrete individual.

        Args:
            ind (CreatedIndividual): A concrete individual.
            v_type (VariableType): Type of the variable.

        Returns:
            Variable: A variable taking the value of the assertion.
        """
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

    def exists_variable(self, a: Individual, b: Individual, role: str) -> bool:
        """
        Checks if a variable taking the value of a role assertion exists.

        Args:
            a (Individual): Object individual.
            b (Individual): Subject individual.
            role (str): A role name.
        """
        var_name: str = f"({a},{b}):{role}"
        return var_name in self.number_of_variables

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
        """Cheks if there is a variable with the given name."""
        return name in self.number_of_variables

    def __has_variable_2(self, ass: Assertion) -> bool:
        """Cheks if there is a variable for a concept assertion."""
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
        """
        Gets a variable taking the value of an individual i1 belonging to the nominal concept {i1}.

        Args:
            i1 (str): An individual.

        Returns:
            Variable: A variable taking the value of the assertion i1:{i1}.
        """
        return self.get_nominal_variable(i1, i1)

    def __get_nominal_variable_2(self, i1: str, i2: str) -> Variable:
        """
        Gets a variable taking the value of an individual i1 belonging to the nominal concept {i2}.

        Args:
            i1 (str): An individual that is subject of the assertion.
            i2 (str): An individual representing the nominal concept.

        Returns:
            Variable: A variable taking the value of the assertion i1:{i2}.
        """
        var_name = f"{i1}:{{ {i2} }}"
        v: Variable = self.get_variable(var_name)
        v.set_type(VariableType.BINARY)
        return v

    def is_nominal_variable(self, i: str) -> bool:
        """Checks if a variable 'i' is a nominal variable."""
        # s: list[str] = i.split(":{")
        # if len(s) != 2:
        #     return False
        # return s[1] == f"{s[0]}" + "}"
        pattern = re.compile(r"([^:]+):\{\1\}")
        return len(pattern.findall(i)) > 0

    def has_nominal_variable(self, terms: list[Term]) -> bool:
        """Checks if a collection of terms has a nominal variable."""
        for term in terms:
            if self.is_nominal_variable(str(term.get_var())):
                return True
        return False

    def exists_nominal_variable(self, i: str) -> bool:
        """Checks if there exists a variable taking the value of an individual i belonging to the nominal concept {i}."""
        var_name: str = f"{i}:{{ {i} }}"
        return var_name in list(map(str, self.variables))

    def get_negated_nominal_variable(self, i1: str, i2: str) -> Variable:
        """
        Gets a variable taking the value of an individual i1 not belonging to the nominal concept {i2}.

        Args:
            i1 (str): An individual that is subject of the assertion.
            i2 (str): An individual representing the nominal concept.

        Returns:
            Variable: A variable taking the value of the assertion i1: not {i2}.
        """
        var_name: str = f"{i1}: not {{ {i2} }}"
        flag: bool = var_name in list(map(str, self.variables))
        v: Variable = self.get_variable(var_name)
        # First time the variable is created, x_{a:{o} } = 1 - x_{a: not {o} }
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
        """
        Adds a new inequality of the form:  expr constraint_type 0.

        Args:
            expr (Expression): An expression in the left side of the inequality.
            constraint_type (InequalityType): Type of the constraint (EQ, GR, LE).
        """
        self.constraints.append(Inequation(expr, constraint_type))

    def __add_new_constraint_2(self, x: Variable, n: float) -> None:
        """
        Adds a new inequality of the form: x >= n.

        Args:
            x (Variable): A variable.
            n (float): A real number.
        """
        self.add_new_constraint(
            Expression(Term(1.0, x)),
            InequalityType.GREATER_THAN,
            DegreeNumeric.get_degree(n),
        )

    def __add_new_constraint_3(self, ass: Assertion, n: float) -> None:
        """
        Given a fuzzy assertion a:C >= L and a number n, adds an inequality of the form: xAss >= n.

        Args:
            ass (Assertion): A fuzzy assertion.
            n (float): A real number.
        """
        self.add_new_constraint(self.get_variable(ass), n)

    def __add_new_constraint_4(self, x: Variable, d: Degree) -> None:
        """
        Add an inequality of the form: x >= d.

        Args:
            x (Variable): A variable.
            d (Degree): A degree.
        """
        self.add_new_constraint(
            Expression(Term(1.0, x)), InequalityType.GREATER_THAN, d
        )

    def __add_new_constraint_5(self, ass: Assertion) -> None:
        """
        Adds a new inequality encoded in a fuzzy assertion.

        Args:
            ass (Assertion): A fuzzy assertion.
        """
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
        """
        Adds a new inequality of the form: expr constraint_type degree.

        Args:
            expr (Expression): An expression in the left side of the inequality.
            constraint_type (InequalityType): Type of the constraint (EQ, GR, LE).
            degree (Degree): A degree in the right side of the inequality.
        """
        self.constraints.append(
            degree.create_inequality_with_degree_rhs(expr, constraint_type)
        )

    def __add_new_constraint_7(
        self, expr: Expression, constraint_type: InequalityType, n: float
    ) -> None:
        """
        Adds a new inequality of the form: expr constraint_type n.

        Args:
            expr (Expression): An expression in the left side of the inequality.
            constraint_type (InequalityType): Type of the constraint (EQ, GR, LE).
            n (float): A real number expression in the right side of the inequality.
        """
        self.add_new_constraint(expr, constraint_type, DegreeNumeric.get_degree(n))

    def add_equality(self, var1: Variable, var2: Variable) -> None:
        """
        Add an equality of the form: var1 = var2.
        """
        self.add_new_constraint(
            Expression(Term(1.0, var1), Term(-1.0, var2)), InequalityType.EQUAL
        )

    def add_string_feature(self, role: str) -> None:
        """Adds a string feature."""
        self.string_features.add(role)

    def add_string_value(self, value: str, int_value: int) -> None:
        """
        Relates the value of a string feature with an integer value.

        Args:
            value (str): Value of a string feature.
            int_value (int): Corresponding integer value.
        """
        self.string_values[int_value] = value

    def change_variable_names(
        self, old_name: str, new_name: str, old_is_created_individual: bool
    ) -> None:
        """
        Replaces the name of the variables including an individual name with the name of another individual name.

        Args:
            old_name (str): Old individual name.
            new_name (str): New individual name.
            old_is_created_individual (bool): Indicates whether the old individual is a created individual or not.
        """

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
                        # a:{b} => x_{a:C}) \geq  x_{b:C}
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
        # They are not similar because the parts before s1 and s2 have different lengths.
        if begin1 != begin2:
            return False
        # If the parts before and after s1/s2 coincide, they are similar.
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
        """
        Gets an ordered permutation of the variables.

        Args:
            x (list[Variable]): A vector of input variables.
            z (list[list[Variable]]): A matrix of intermediate variables.

        Returns:
            list[Variable]: A permutation of the input variables such that y[0] >= y[1] >= ... >= y[n-1]
        """
        n: int = len(x)
        # New n [0,1] variables yi
        y: list[Variable] = [
            self.get_new_variable(VariableType.SEMI_CONTINUOUS) for _ in range(n)
        ]
        # y1 >= y2 >= ... >= yn
        for i in range(n - 1):
            self.add_new_constraint(
                Expression(Term(1.0, y[i]), Term(-1.0, y[i + 1])),
                InequalityType.GREATER_THAN,
            )
        # for each i,j : yi - kz_{ij} <= xj
        for i in range(n):
            for j in range(n):
                self.add_new_constraint(
                    Expression(Term(1.0, x[j]), Term(-1.0, y[i]), Term(1.0, z[i][j])),
                    InequalityType.GREATER_THAN,
                )
        # for each i,j : xj <= yi + kz_{ij}
        for i in range(n):
            for j in range(n):
                self.add_new_constraint(
                    Expression(Term(1.0, x[j]), Term(-1.0, y[i]), Term(-1.0, z[i][j])),
                    InequalityType.LESS_THAN,
                )
        # for each i : \sum_{j} z_{ij} = n - 1
        for i in range(n):
            exp: Expression = Expression(1.0 - n)
            for j in range(n):
                exp.add_term(Term(1.0, z[i][j]))
            self.add_new_constraint(exp, InequalityType.EQUAL)
        # for each j : \sum_{i} z_{ij} = n - 1
        for i in range(n):
            exp: Expression = Expression(1.0 - n)
            for j in range(n):
                exp.add_term(Term(1.0, z[j][i]))
            self.add_new_constraint(exp, InequalityType.EQUAL)
        return y

    def __bfs(self, graph: nx.Graph, solution: dict[int, int]) -> int:
        # Number of nodes
        n: int = graph.number_of_nodes()

        # Solution is a mapping: variable -> partition
        # Initial partition value is 0
        for i in range(n):
            solution[i] = 0

        # Number of partition
        p: int = 1

        # Iterate over not processed nodes
        queue: list[int] = list()
        for i in range(n - 1):
            # Skip node if processed
            if solution[i] != 0:
                continue
            queue = [i]
            solution[i] = p
            self.__compute_partition(queue, solution, p, graph)

            # Next partition
            p += 1
        return p - 1

    def __compute_partition(
        self, queue: list[int], solution: dict[int, int], p: int, graph: nx.Graph
    ) -> None:

        while len(queue) > 0:
            current: int = queue.pop()
            neighbors: list[int] = list(graph.neighbors(current))
            if len(neighbors) == 0:
                continue
            for j in neighbors:
                if solution[j] != 0:
                    continue
                solution[j] = p
                queue.append(j)

    def set_nominal_variables(self, value: bool) -> None:
        self.nominal_variables = value

    def __remove_nominal_variables(self) -> None:
        constraints_to_remove: list[int] = []
        variable_to_remove: list[int] = []
        for i, constraint in enumerate(self.constraints):
            terms: list[Term] = constraint.get_terms()
            if self.has_nominal_variable(terms):
                constraints_to_remove.append(i)
        for i, variable in enumerate(self.variables):
            if self.is_nominal_variable(str(variable)):
                variable_to_remove.append(i)

        self.constraints = [
            constraint
            for i, constraint in enumerate(self.constraints)
            if i not in constraints_to_remove
        ]
        self.variables = [
            variable
            for i, variable in enumerate(self.variables)
            if i not in variable_to_remove
        ]

    def __get_graph(self) -> nx.Graph:
        g: nx.Graph = nx.Graph()

        # Create nodes
        n: int = len(self.variables)
        for i in range(n):
            g.add_node(i)

        # Create edges
        edge: int = 0
        for constraint in self.constraints:
            terms: list[Term] = constraint.get_terms()
            if len(terms) == 0:
                continue
            first_var: int = self.variables.index(terms[0].get_var())
            for term in terms[1:]:
                other_var: int = self.variables.index(term.get_var())
                # Edges between first and other
                edge += 1
                g.add_edge(first_var, other_var, number=edge)

        return g

    def __common_partition_part(
        self, objective: Expression
    ) -> tuple[list[Variable], dict[int, int], int, list[int], int, int]:

        objectives: list[Variable] = list()

        # Partition time
        init_time: int = time.perf_counter_ns()

        # Graph
        solution: dict[int, int] = dict()
        num_partitions: int = self.__bfs(self.__get_graph(), solution)

        # Mapping partition -> number of objective variables in partition
        num_variables_in_partition: list[int] = [0] * num_partitions

        # Compute objective coefficients
        for term in objective.get_terms():
            v: Variable = term.get_var()
            objectives.append(v)
            index: int = self.variables.index(v)
            num_partition: int = solution.get(index) - 1
            num_variables_in_partition[num_partition] += 1

        # Compute two or more partitions
        two_or_more: int = 0
        count: int = 0
        for i in range(num_partitions):
            if num_variables_in_partition[i] > 1:
                two_or_more += 1
                count += num_variables_in_partition[i]

        end_time: int = time.perf_counter_ns()
        total_time: float = (end_time - init_time) * 1e-9
        Util.debug(f"Partition time: {total_time} s")
        return (
            objectives,
            solution,
            num_partitions,
            num_variables_in_partition,
            two_or_more,
            count,
        )

    def __solve_gurobi_using_partitions(
        self, objective: Expression
    ) -> typing.Optional[Solution]:
        import gurobipy as gp
        from gurobipy import GRB

        (
            objectives,
            solution,
            num_partitions,
            num_variables_in_partition,
            two_or_more,
            count,
        ) = self.__common_partition_part(objective)

        if two_or_more == 0:
            MILPHelper.PARTITION = False
            return self.solve_gurobi(objective)

        # Specific algorithm starts here
        try:
            Util.debug(
                f"There are {two_or_more} partitions with {count} dependent objective variables"
            )

            # PROBLEMS with 1 or less
            env = gp.Env(empty=True)
            if not ConfigReader.DEBUG_PRINT:
                env.setParam("OutputFlag", 0)
            env.setParam("IntFeasTol", 1e-9)
            env.setParam("BarConvTol", 0)
            env.start()

            model: gp.Model = gp.Model("partition-model-1-or-less", env=env)

            # Create variables
            vars_gurobi: dict[str, gp.Var] = dict()

            var_types: dict[VariableType, str] = {
                VariableType.BINARY: GRB.BINARY,
                VariableType.INTEGER: GRB.INTEGER,
                VariableType.CONTINUOUS: GRB.CONTINUOUS,
                VariableType.SEMI_CONTINUOUS: GRB.SEMICONT,
            }
            var_name_map: dict[str, str] = {
                str(v): f"x{i}" for i, v in enumerate(self.variables)
            }
            for i, curr_variable in enumerate(self.variables):
                num_partition: int = solution.get(i) - 1
                if num_variables_in_partition[num_partition] > 1:
                    continue  # Next variable
                v_type: VariableType = curr_variable.get_type()

                Util.debug(
                    (
                        f"Variable -- "
                        f"[{curr_variable.get_lower_bound()}, {curr_variable.get_upper_bound()}] - "
                        f"Obj value = 0 - "
                        f"Var type = {v_type.name} -- "
                        f"Var = {curr_variable}"
                    )
                )

                vars_gurobi[var_name_map[str(v)]] = model.addVar(
                    lb=curr_variable.get_lower_bound(),
                    ub=curr_variable.get_upper_bound(),
                    obj=0,
                    vtype=var_types[v_type],
                    name=var_name_map[str(curr_variable)],
                )

            # Integrate new variables
            model.update()

            constraint_name: str = "constraint"
            # Add constraints
            for i, constraint in enumerate(self.constraints):
                if constraint in self.constraints[:i]:
                    continue
                if constraint.is_zero():
                    continue

                curr_name: str = f"{constraint_name}_{i + 1}"
                expr: gp.LinExpr = gp.LinExpr()
                for term in constraint.get_terms():
                    index: int = self.variables.index(term.get_var())
                    num_partition: int = solution.get(index) - 1
                    if num_variables_in_partition[num_partition] > 1:
                        break  # Exit for term loop
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

            # Integrate new constraints
            model.update()

            # Optimize model
            model.optimize()
            Util.debug(f"Model:")

            # Return solution
            if model.Status == GRB.INFEASIBLE:
                return Solution(Solution.INCONSISTENT_KB)

            # One for each partition with two or more variables, plus one for the rest (all partitions with 0 and 1)
            sol: Solution = Solution(1.0)

            # PROBLEMS with 2 or more
            for obj_var in objectives:
                env = gp.Env(empty=True)
                if not ConfigReader.DEBUG_PRINT:
                    env.setParam("OutputFlag", 0)
                env.setParam("IntFeasTol", 1e-9)
                env.setParam("BarConvTol", 0)
                env.start()

                model: gp.Model = gp.Model("partition-model-2-or-more", env=env)

                index: int = self.variables.index(obj_var)
                problem: int = solution.get(index) - 1

                vars_gurobi: dict[str, gp.Var] = dict()

                # Create variables
                for i, curr_variable in enumerate(self.variables):
                    num_partition: int = solution.get(i) - 1
                    if num_partition != problem:
                        continue

                    v_type: VariableType = curr_variable.get_type()
                    ov: float = 1.0 if i == self.variables.index(obj_var) else 0.0

                Util.debug(
                    (
                        f"Variable -- "
                        f"[{curr_variable.get_lower_bound()}, {curr_variable.get_upper_bound()}] - "
                        f"Obj value = {ov} - "
                        f"Var type = {v_type.name} -- "
                        f"Var = {curr_variable}"
                    )
                )

                vars_gurobi[var_name_map[str(v)]] = model.addVar(
                    lb=curr_variable.get_lower_bound(),
                    ub=curr_variable.get_upper_bound(),
                    obj=ov,
                    vtype=var_types[v_type],
                    name=var_name_map[str(curr_variable)],
                )

                # Integrate new variables
                model.update()

                constraint_name: str = "constraint"
                # Add constraints
                for i, constraint in enumerate(self.constraints):
                    if constraint in self.constraints[:i]:
                        continue
                    if constraint.is_zero():
                        continue

                    curr_name: str = f"{constraint_name}_{i + 1}"
                    expr: gp.LinExpr = gp.LinExpr()
                    for term in constraint.get_terms():
                        index: int = self.variables.index(term.get_var())
                        num_partition: int = solution.get(index) - 1
                        if num_partition != problem:
                            break  # Exit for term loop
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

                # Integrate new constraints
                model.update()

                # Optimize model
                model.optimize()

                # Return solution
                if model.Status == GRB.INFEASIBLE:
                    return Solution(Solution.INCONSISTENT_KB)
                else:
                    result: float = Util.round(abs(model.ObjVal))
                    sol = Solution(result)
                    name: str = str(obj_var)
                    sol.add_showed_variable(name, result)

                model.printQuality()
                model.printStats()

            return sol
        except gp.GurobiError as e:
            Util.error(f"Error code: {e.errno}. {e.message}")
            return None

    def solve_gurobi(self, objective: Expression) -> typing.Optional[Solution]:
        """
        Solves a MILP problem using Gurobi.
        """

        import gurobipy as gp
        from gurobipy import GRB

        if not self.nominal_variables:
            self.__remove_nominal_variables()

        if MILPHelper.PARTITION:
            return self.__solve_gurobi_using_partitions(objective)

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
                    # Compute objective coefficients
                    index = self.variables.index(term.get_var())
                    objective_value[index] += term.get_coeff()

            env = gp.Env(empty=True)
            if not ConfigReader.DEBUG_PRINT:
                env.setParam("OutputFlag", 0)
            env.setParam("IntFeasTol", 1e-9)
            env.setParam("BarConvTol", 0)
            env.start()

            model: gp.Model = gp.Model("model", env=env)
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

            # Create variables
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

            # Integrate new variables
            model.update()

            Util.debug(f"# constraints -> {len(self.constraints)}")
            constraint_name: str = "constraint"
            # Add constraints
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

            # Integrate new constraints
            model.update()

            # Optimize model
            model.optimize()

            model.write(os.path.join(constants.RESULTS_PATH, "gurobi_model.lp"))
            model.write(os.path.join(constants.RESULTS_PATH, "gurobi_solution.json"))

            Util.debug(f"Model:")
            sol: Solution = None
            # if model.Status == GRB.INFEASIBLE and ConfigReader.RELAX_MILP:
            #     self.__gurobi_handle_model_infeasibility(model)

            # Return solution
            if model.Status == GRB.INFEASIBLE:
                sol = Solution(Solution.INCONSISTENT_KB)
            else:
                result: float = Util.round(abs(model.ObjVal))
                sol = Solution(result)
                for i in range(size):
                    if ConfigReader.DEBUG_PRINT or show_variable[i]:
                        name: str = self.variables[i].name
                        value: float = round(vars_gurobi[var_name_map[name]].X, 6)
                        if show_variable[i]:
                            sol.add_showed_variable(name, value)
                        # if self.PRINT_VARIABLES:
                        Util.debug(f"{name} = {value}")
                        if self.PRINT_LABELS:
                            self.print_instance_of_labels(name, value)

            model.printQuality()
            model.printStats()

            Util.debug(
                f"{constants.STAR_SEPARATOR}Statistics{constants.STAR_SEPARATOR}"
            )
            Util.debug("MILP problem:")
            # Show number of variables
            Util.debug(f"\t\tSemi continuous variables: {num_up_vars}")
            Util.debug(f"\t\tBinary variables: {num_binary_vars}")
            Util.debug(f"\t\tContinuous variables: {num_free_vars}")
            Util.debug(f"\t\tInteger variables: {num_integer_vars}")
            Util.debug(f"\t\tTotal variables: {len(self.variables)}")
            # Show number of constraints
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
                sol = Solution(Solution.INCONSISTENT_KB)
            else:
                model.write(os.path.join(constants.RESULTS_PATH, "mip_solution.sol"))
                result: float = Util.round(abs(model.objective_value))
                sol = Solution(result)
                for i in range(size):
                    if ConfigReader.DEBUG_PRINT or show_variable[i]:
                        name: str = self.variables[i].name
                        value: float = round(vars_mip[var_name_map[name]].x, 6)
                        if show_variable[i]:
                            sol.add_showed_variable(name, value)
                        # if self.PRINT_VARIABLES:
                        Util.debug(f"{name} = {value}")
                        if self.PRINT_LABELS:
                            self.print_instance_of_labels(name, value)

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
                sol = Solution(Solution.INCONSISTENT_KB)
            else:
                result: float = Util.round(abs(model.objective.value()))
                sol = Solution(result)
                var_dict: dict[str, pulp.LpVariable] = model.variablesDict()
                for i in range(size):
                    if ConfigReader.DEBUG_PRINT or show_variable[i]:
                        name: str = self.variables[i].name
                        value: float = (
                            round(var_dict[var_name_map[name]].value(), 6)
                            if var_name_map[name] in var_dict
                            else 0.0
                        )
                        if show_variable[i]:
                            sol.add_showed_variable(name, value)
                        # if self.PRINT_VARIABLES:
                        Util.debug(f"{name} = {value}")
                        if self.PRINT_LABELS:
                            self.print_instance_of_labels(name, value)

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
    #         sol = Solution(Solution.INCONSISTENT_KB)
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
        """Defines a concept to be crisp."""
        self.crisp_concepts.add(concept_name)

    def add_crisp_role(self, role_name: str) -> None:
        """Defines a role to be crisp."""
        self.crisp_roles.add(role_name)

    def is_crisp_concept(self, concept_name: str) -> bool:
        """Checks if a concept is crisp or not."""
        return concept_name in self.crisp_concepts

    def is_crisp_role(self, role_name: str) -> bool:
        """Checks if a role is crisp or not."""
        return role_name in self.crisp_roles

    def set_binary_variables(self) -> None:
        """Transforms every [0,1]-variable into a {0,1} variable."""
        # set all variables binary, except
        #   - those that hold the value of a datatype filler
        #   - free variables in constraints
        for v in self.variables:
            if v.get_datatype_filler_type() or v.get_type() in (
                VariableType.CONTINUOUS,
                VariableType.INTEGER,
            ):
                continue
            v.set_binary_variable()

    def get_name_for_integer(self, i: int) -> typing.Optional[str]:
        """Gets the name of the i-th variable."""
        for name, i2 in self.number_of_variables.items():
            if i == i2:
                return name
        return None

    def get_number_for_assertion(self, ass: Assertion) -> int:
        """Gets an integer codification of an assertion."""
        return self.number_of_variables.get(str(self.get_variable(ass)))

    def add_contradiction(self) -> None:
        """Add a contradiction to make the fuzzy KB unsatisfiable"""
        self.constraints.clear()
        self.add_new_constraint(Expression(1.0), InequalityType.EQUAL)

    def add_cardinality_list(self, sc: SigmaCount) -> None:
        """
        SigmaCount(r,C,O,d)^I(w) = d^I(xSigma)

        Args:
            sc (SigmaCount):
                xSigma: Free variable taking the value  \sigma_{i2 \in O} r(i1, i2) \otimes C(i2)
                i1: Name of an individual, subject of the relation.
                O: Set of individuals candidates to be the object of the relation.
                r: Role.
                C: Concept.
        """
        self.cardinalities.append(sc)
