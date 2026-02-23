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
    """
    This class serves as a comprehensive manager for Mixed-Integer Linear Programming (MILP) problems, functioning as an interface that translates high-level logical constructs—such as fuzzy concepts, roles, and individuals—into mathematical optimization models. It allows users to construct problems by retrieving or creating variables associated with specific domain entities, adding linear constraints or inequalities, and defining objective functions. The `optimize` method orchestrates the solving process by delegating to various external solver backends, including Gurobi, MIP, and PuLP, while also offering an optional partitioning strategy to handle complex problem structures. Beyond standard MILP operations, it provides specialized handling for "crisp" concepts and roles (enforcing binary variables), nominal variables, and string features, along with utilities to clone the problem state or output variable values and linguistic label memberships for analysis.

    :param PARTITION: Flag to enable a partitioning strategy that decomposes the MILP problem into smaller sub-problems based on variable connectivity.
    :type PARTITION: bool
    :param PRINT_LABELS: Determines whether to display the membership degrees of variables to linguistic labels.
    :type PRINT_LABELS: bool
    :param PRINT_VARIABLES: Controls whether the values of the variables are printed to the debug output.
    :type PRINT_VARIABLES: bool
    :param nominal_variables: Controls whether variables representing nominal concepts (e.g., `a:{a}`) are retained in the MILP problem. If False, these variables and their associated constraints are removed prior to optimization.
    :type nominal_variables: bool
    :param cardinalities: SigmaCount objects representing the cardinality constraints in the MILP problem.
    :type cardinalities: list[SigmaCount]
    :param constraints: A list of `Inequation` objects representing the linear constraints defining the feasible region of the MILP problem.
    :type constraints: list[Inequation]
    :param crisp_concepts: A set of concept names that are restricted to binary values (0 or 1), ensuring that any variables representing these concepts in the MILP problem are defined as binary variables.
    :type crisp_concepts: set[str]
    :param crisp_roles: A set of role names that are restricted to binary values (0 or 1), ensuring their corresponding variables in the MILP problem are binary.
    :type crisp_roles: set[str]
    :param number_of_variables: Maps variable names to their integer indices, ensuring uniqueness and enabling efficient variable lookup.
    :type number_of_variables: dict[str, int]
    :param show_vars: Helper instance that tracks variables designated for output and manages their association with linguistic labels for displaying membership degrees.
    :type show_vars: ShowVariablesHelper
    :param string_features: Stores the names of features that take string values, identifying variables in the MILP problem that require special handling distinct from numeric variables.
    :type string_features: set[str]
    :param string_values: Maps integer encodings to their corresponding string values, used to handle string features within the MILP problem.
    :type string_values: dict[int, str]
    :param variables: Stores the decision variables for the MILP problem in creation order, serving as the primary source for model construction and result mapping.
    :type variables: list[Variable]

    :raises ValueError: Raised if the configured MILP provider is unsupported or if methods are called with invalid arguments.
    """


    PARTITION: bool = False
    # Indicates whether we want to show the membership degrees to linguistic labels or not.
    PRINT_LABELS: bool = True
    # Indicates whether we want to show the value of the variables or not.
    PRINT_VARIABLES: bool = True

    def __init__(self) -> None:
        """Initializes the MILP helper instance by resetting all internal state attributes to their default values. This involves setting boolean flags to false and creating empty collections to hold model components such as variables, constraints, and cardinalities. It also prepares storage structures for specific features, including crisp concepts, crisp roles, and string-based attributes. Additionally, the constructor instantiates a `ShowVariablesHelper` object to manage the display and tracking of variables within the model."""

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
        """
        Creates and returns a deep copy of the current `MILPHelper` instance. The method constructs a new object and populates it by recursively cloning lists of complex objects such as `cardinalities`, `constraints`, and `variables`, while using `copy.deepcopy` for other mutable structures like `crisp_concepts` and `string_features`. This ensures that the returned instance is independent of the original for most attributes, though it is important to note that `nominal_variables` is assigned by reference rather than copied, meaning modifications to this specific attribute in the clone will affect the original object.

        :return: A deep copy of the current instance.

        :rtype: typing.Self
        """

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
        Optimizes the provided objective expression by dispatching the problem to a specific Mixed-Integer Linear Programming (MILP) solver defined in the global configuration. The method inspects the `MILP_PROVIDER` setting to select the appropriate backend, supporting options such as Gurobi, Python-MIP, and various PuLP interfaces. It delegates the actual solving process to the corresponding internal method and returns the resulting solution object. If the configured provider is not recognized or supported, a `ValueError` is raised.

        :param objective: The mathematical expression or model to be optimized using the configured MILP solver.
        :type objective: Expression

        :raises ValueError: Raised when the configured MILP provider is unsupported or unrecognized.

        :return: The optimal solution for the given objective expression, or None if no solution is found.

        :rtype: typing.Optional[Solution]
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
        """
        Outputs the membership degrees of a numerical value with respect to specific linguistic labels. This method acts as a dispatcher that supports two distinct calling signatures based on the number of arguments provided. If two arguments are supplied, it expects a string identifier and a numerical value; if three arguments are supplied, it expects two string identifiers followed by a numerical value. The method validates the input types and delegates the actual printing logic to private helper methods.

        :param args: The linguistic label and numeric value to evaluate, optionally preceded by a variable name.
        :type args: typing.Any
        """

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
        This method retrieves the linguistic labels associated with a specific feature and individual combination, identified by the constructed string `f_name(ind_name)`. It iterates through the retrieved labels, calculates the membership degree of the provided numerical value for each label, and prints the results to the console. If no labels are found for the given identifier, the method produces no output. The operation relies on the `show_vars` attribute to access the label definitions and uses a utility function to display the formatted information.

        :param f_name: Name of the feature for which membership degrees are displayed.
        :type f_name: str
        :param ind_name: Name of the individual entity to which the feature value belongs.
        :type ind_name: str
        :param value: Numerical value of the feature for the individual, used to compute and display membership degrees.
        :type value: float
        """

        name: str = f"{f_name}({ind_name})"
        labels = self.show_vars.get_labels(name)
        for f in labels:
            Util.info(
                f"{name} is {f.compute_name()} = {f.get_membership_degree(value)}"
            )

    def __print_instance_of_labels_2(self, name: str, value: float) -> None:
        """
        Retrieves the linguistic labels associated with the specified feature name and calculates the membership degree of the provided value for each label. For every label found, it formats and outputs a message containing the feature name, the label's computed name, and the calculated membership degree. This method acts as a diagnostic utility to visualize how a specific numerical value fits into the defined fuzzy categories, producing side effects in the form of log output without modifying the object's state.

        :param name: Name of the feature or individual used to retrieve the associated linguistic labels.
        :type name: str
        :param value: The numerical value of the feature for which membership degrees are calculated.
        :type value: float
        """

        labels = self.show_vars.get_labels(name)
        for f in labels:
            Util.info(
                f"{name} is {f.compute_name()} = {f.get_membership_degree(value)}"
            )

    def get_new_variable(self, v_type: VariableType) -> Variable:
        """
        Creates a new variable of the specified type and registers it within the MILP helper instance. The method guarantees a unique variable name by checking against the internal registry of existing variables; if a name collision is detected, it regenerates the variable until a unique identifier is found. As a side effect, the new variable is appended to the internal list of variables, and its name is recorded in the tracking dictionary with its corresponding index.

        :param v_type: The type of the variable to create.
        :type v_type: VariableType

        :return: A newly created Variable of the specified type, guaranteed to have a unique name and added to the internal variable list.

        :rtype: Variable
        """

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
        """
        Retrieves a `Variable` instance by acting as a polymorphic dispatcher that delegates to specific internal handlers based on the number and types of arguments provided. The method supports a wide variety of signatures involving strings, domain entities such as `Individual`, `Concept`, `Restriction`, and `CreatedIndividual`, as well as logical constructs like `Assertion` and `Relation`. Depending on the specific combination of inputs, the method may infer the variable type or accept an explicit `VariableType` argument. If the argument count is not between one and four, or if the provided types do not correspond to any defined overload, a `ValueError` is raised.

        :param args: Variable-length arguments specifying the criteria for retrieving the variable. The specific combination of argument types and count determines the lookup strategy, supporting inputs ranging from a simple name string to complex combinations of Individuals, Relations, and VariableTypes.
        :type args: typing.Any

        :raises ValueError: Raised if the provided arguments do not match any of the supported type signatures or argument counts.

        :return: The Variable object corresponding to the provided arguments.

        :rtype: Variable
        """

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
        Retrieves a variable instance corresponding to the specified name, creating it if necessary. If a variable with the provided name already exists in the internal registry, the existing object is returned. Otherwise, a new variable of type `SEMI_CONTINUOUS` is instantiated, appended to the internal list of variables, and registered in the variable count dictionary. This method modifies the internal state of the helper whenever a new variable is generated.

        :param var_name: Name of the variable to retrieve or create.
        :type var_name: str

        :return: The variable instance associated with the given name. If the variable does not exist, a new semi-continuous variable bounded in [0, 1] is created and returned.

        :rtype: Variable
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
        Retrieves a variable instance identified by the given name and explicitly sets its type to the specified value. This method first fetches the variable using the standard retrieval mechanism, mutates the variable's type attribute, and then returns the modified object. It is primarily utilized by the DatatypeReasoner to ensure variables are configured with the correct constraints during the reasoning process.

        :param var_name: The identifier for the variable to be retrieved.
        :type var_name: str
        :param v_type: The type or bound to assign to the variable.
        :type v_type: VariableType

        :return: The Variable object corresponding to `var_name`, configured with the specified type `v_type`.

        :rtype: Variable
        """

        var: Variable = self.get_variable(var_name)
        var.set_type(v_type)
        return var

    def __get_variable_3(self, ass: Assertion) -> Variable:
        """
        Retrieves the decision variable associated with a specific concept assertion, ensuring that the variable exists within the model. If the variable has not been previously defined, this method instantiates a new semi-continuous variable constrained to the interval [0, 1]. The returned variable represents the degree of truth or membership for the specified individual and concept pair.

        :param ass: The fuzzy concept assertion whose value is to be represented by a variable.
        :type ass: Assertion

        :return: The variable representing the truth value of the assertion.

        :rtype: Variable
        """

        return self.get_variable(ass.get_individual(), ass.get_concept())

    def __get_variable_4(self, rel: Relation) -> Variable:
        """
        Retrieves a variable representing the truth value of a specific fuzzy role assertion, creating it if necessary. The method extracts the subject individual, object individual, and role name from the provided `Relation` object and delegates to the underlying variable management system. If a variable for this specific assertion does not already exist, a new semi-continuous variable bounded between 0 and 1 is instantiated and added to the model. The function returns the variable associated with the assertion.

        :param rel: The fuzzy role assertion for which to retrieve or create the corresponding variable.
        :type rel: Relation

        :return: The variable representing the truth value of the role assertion, created as a semi-continuous variable in the range [0, 1] if it does not already exist.

        :rtype: Variable
        """

        a: Individual = rel.get_subject_individual()
        b: Individual = rel.get_object_individual()
        role: str = rel.get_role_name()
        return self.get_variable(a, b, role)

    def __get_variable_5(self, ind: Individual, restrict: Restriction) -> Variable:
        """
        Retrieves a decision variable representing a universal restriction applied to a specific individual, generating a unique key by combining the individual's identifier with the restriction's name. The method relies on the `get_variable` helper to fetch or instantiate the variable, ensuring it is available for the Mixed-Integer Linear Programming model. As a side effect, if the display configuration flags the individual for visibility, the variable is added to the display manager for tracking or logging.

        :param ind: The subject individual of the restriction, used to identify and retrieve the associated variable.
        :type ind: Individual
        :param restrict: A fuzzy role assertion representing the restriction associated with the individual.
        :type restrict: Restriction

        :return: The variable representing the value of the universal restriction for the given individual. If the variable does not already exist, a new semi-continuous variable bounded between 0 and 1 is created and returned.

        :rtype: Variable
        """

        var: Variable = self.get_variable(f"{ind}:{restrict.get_name_without_degree()}")
        if self.show_vars.show_individuals(str(ind)):
            self.show_vars.add_variable(var, str(var))
        return var

    def __get_variable_6(self, ind: Individual, c: Concept) -> Variable:
        """
        Retrieves or creates a variable representing the truth value of a concept assertion for a specific individual. If the concept is a `HAS_VALUE` restriction, the method extracts the role and value to define a semi-continuous variable bounded between 0 and 1. For other concept types, it generates the variable based on the individual and the string representation of the concept. The actual variable instantiation or lookup is delegated to the `get_variable` method, which handles the creation if the variable does not already exist.

        :param ind: The individual entity for which the concept assertion variable is being retrieved or created.
        :type ind: Individual
        :param c: The fuzzy concept representing the assertion. Used to identify the variable, extracting role and value details if the concept is of type HAS_VALUE.
        :type c: Concept

        :return: The variable representing the truth value of the assertion that the individual belongs to the concept. If the concept is a 'has-value' restriction, the variable is semi-continuous.

        :rtype: Variable
        """

        if c.type == ConceptType.HAS_VALUE:
            assert isinstance(c, HasValueInterface)

            r: str = c.role
            b: str = str(c.value)
            return self.get_variable(str(ind), b, r, VariableType.SEMI_CONTINUOUS)
        return self.get_variable(ind, str(c))

    def __get_variable_7(self, ind: Individual, concept_name: str) -> Variable:
        """
        Retrieves a variable representing the truth value of a concept assertion for a specific individual, identified by the combination of the individual and concept name. If the concept is defined as a crisp concept, the method ensures the variable is configured as a binary variable. Additionally, if the display settings are configured to show either the specific individual or the concept, the variable is added to the display tracker. The method returns the resulting variable object.

        :param ind: The individual entity for which the concept assertion variable is defined.
        :type ind: Individual
        :param concept_name: The name of the fuzzy concept associated with the individual.
        :type concept_name: str

        :return: The decision variable representing the truth value of the concept assertion for the given individual.

        :rtype: Variable
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
        Retrieves the decision variable representing the assertion of a specific role between a subject individual and an object individual. If a variable for this specific relationship does not already exist, the method creates a new one defined as a semi-continuous variable within the bounds of 0 and 1. This ensures that the Mixed-Integer Linear Programming model has a corresponding variable to track the state or validity of the role assertion.

        :param a: The object individual involved in the role assertion.
        :type a: Individual
        :param b: The subject individual of the role assertion.
        :type b: Individual
        :param role: The name of the role or relationship connecting the subject and object individuals.
        :type role: str

        :return: The variable representing the role assertion between the two individuals, configured as a semi-continuous variable in the range [0, 1].

        :rtype: Variable
        """

        return self.get_variable(a, b, role, VariableType.SEMI_CONTINUOUS)

    def __get_variable_9(
        self, a: Individual, b: Individual, role: str, v_type: VariableType
    ) -> Variable:
        """
        Retrieves or creates a variable representing a role assertion between two individuals within the mixed-integer linear programming model. This method serves as a wrapper that converts the subject and object individuals to their string representations before delegating to the underlying `get_variable` method, passing the role name and the specified variable type. If a variable for this specific role assertion does not already exist, the delegated call handles its instantiation, ensuring consistent access to variables modeling relationships between entities.

        :param a: The individual representing the object of the role assertion.
        :type a: Individual
        :param b: The individual acting as the subject in the role assertion.
        :type b: Individual
        :param role: The name of the role connecting the two individuals.
        :type role: str
        :param v_type: Specifies the classification or domain type of the variable representing the role assertion.
        :type v_type: VariableType

        :return: The variable representing the role assertion between the object individual and the subject individual, creating a new one if it does not already exist.

        :rtype: Variable
        """

        return self.get_variable(str(a), str(b), role, v_type)

    def __get_variable_10(
        self, a: str, b: str, role: str, v_type: VariableType
    ) -> Variable:
        """
        Retrieves or creates a decision variable representing a specific relationship between two entities, identified by the strings `a` and `b`, and characterized by the provided `role`. The method constructs a unique identifier for the variable by combining these inputs and fetches the corresponding object from an internal registry. If the role is designated as "crisp," the variable is constrained to be binary; otherwise, its mathematical type is set according to the `v_type` argument. Additionally, the method checks visibility conditions based on abstract or concrete fillers for the role and entity `a`, registering the variable with a display manager if these conditions are met. The fully configured variable object is then returned.

        :param a: The first component of the variable's identifier, used to construct the variable name and check visibility conditions.
        :type a: str
        :param b: The second component of the pair used to construct the variable's unique identifier.
        :type b: str
        :param role: The role or relationship defining the variable, used to construct its name, determine if it is binary, and check visibility settings for fillers.
        :type role: str
        :param v_type: The type classification to assign to the variable.
        :type v_type: VariableType

        :return: The `Variable` object corresponding to the specified role and arguments, configured with the provided type and binary status.

        :rtype: Variable
        """

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
        Retrieves or creates a continuous optimization variable associated with the provided concrete individual. This method acts as a specialized wrapper around the general variable retrieval logic, explicitly enforcing that the resulting variable is of the continuous type to accommodate real-valued constraints. It ensures that the MILP model correctly represents the individual's assertion using a non-discrete variable, potentially modifying the solver's internal state if the variable does not yet exist.

        :param ind: The concrete individual instance whose value is to be assigned to the variable.
        :type ind: CreatedIndividual

        :return: A continuous variable representing the value of the provided concrete individual.

        :rtype: Variable
        """

        return self.get_variable(ind, VariableType.CONTINUOUS)

    def __get_variable_12(self, ind: CreatedIndividual, v_type: VariableType) -> None:
        """
        Retrieves or creates a MILP variable associated with a specific concrete individual, deriving a unique identifier from the individual's role and parent context. The method constructs the variable name by combining the role name and parent string, substituting default placeholders or the individual's string representation if these attributes are missing. If the variable does not already exist in the internal registry, it is initialized, assigned the specified variable type, and conditionally added to the display tracking system based on visibility settings for concrete fillers.

        :param ind: The concrete individual instance used to generate the variable's name based on its role and parent.
        :type ind: CreatedIndividual
        :param v_type: The type classification to assign to the variable representing the individual's value.
        :type v_type: VariableType
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
        Determines whether a MILP variable representing a specific role assertion between two individuals has been registered within the helper. The method constructs a unique variable identifier by formatting the subject individual, object individual, and role name into a specific string pattern. It then checks for the existence of this key in the internal variable registry and returns a boolean result without modifying the state of the object.

        :param a: The object individual involved in the role assertion.
        :type a: Individual
        :param b: The individual acting as the subject in the role assertion.
        :type b: Individual
        :param role: The name of the role assertion defining the relationship between the subject and object individuals.
        :type role: str

        :return: True if a variable representing the role assertion between the object individual `a` and the subject individual `b` exists, False otherwise.

        :rtype: bool
        """

        var_name: str = f"({a},{b}):{role}"
        return var_name in self.number_of_variables

    @typing.overload
    def has_variable(self, name: str) -> bool: ...

    @typing.overload
    def has_variable(self, ass: Assertion) -> bool: ...

    def has_variable(self, *args) -> bool:
        """
        Checks for the existence of a variable based on the type of the provided argument. The method accepts a single argument, which must be either a string representing a variable name or an `Assertion` object. If the argument is a string, the method verifies if a variable with that name exists; if it is an `Assertion`, it checks the assertion's association with variables. The function returns a boolean value indicating the presence of the variable. Passing an argument of any other type raises a `ValueError`.

        :param args: The object to check, which must be either a string or an Assertion instance.
        :type args: typing.Any

        :raises ValueError: Raised if the provided argument is not a string or an Assertion instance.

        :return: True if the variable identified by the provided string or Assertion exists, False otherwise.

        :rtype: bool
        """

        assert len(args) == 1
        if isinstance(args[0], str):
            return self.__has_variable_1(*args)
        elif isinstance(args[0], Assertion):
            return self.__has_variable_2(*args)
        else:
            raise ValueError

    def __has_variable_1(self, name: str) -> bool:
        """
        Determines whether a variable with the specified name exists within the internal collection of variables managed by the helper. This method performs a membership check against the keys present in the `number_of_variables` attribute. It returns `True` if the variable name is found and `False` otherwise. The operation does not modify the state of the object or any of its attributes.

        :param name: The identifier of the variable to check for existence.
        :type name: str

        :return: True if a variable with the given name exists, False otherwise.

        :rtype: bool
        """

        return name in self.number_of_variables

    def __has_variable_2(self, ass: Assertion) -> bool:
        """
        Checks for the existence of a variable associated with a specific concept assertion by normalizing the assertion's identifier. The method strips degree information from the assertion's name before querying the internal variable registry. It returns a boolean indicating whether a variable corresponding to the normalized name is currently defined.

        :param ass: The concept assertion to check for an associated variable.
        :type ass: Assertion

        :return: True if a variable exists for the given assertion's name, otherwise False.

        :rtype: bool
        """

        return self.has_variable(ass.get_name_without_degree())

    @typing.overload
    def get_nominal_variable(self, i1: str) -> Variable: ...

    @typing.overload
    def get_nominal_variable(self, i1: str, i2: str) -> Variable: ...

    def get_nominal_variable(self, *args) -> Variable:
        """
        Retrieves a nominal variable instance associated with the provided string identifiers, supporting two distinct calling conventions based on the number of arguments. The method validates that the input consists of either one or two strings, raising an assertion error otherwise, and delegates the actual retrieval logic to private helper methods. It returns the corresponding Variable object, which serves as a fundamental component within the Mixed-Integer Linear Programming model managed by the helper.

        :param args: One or two string arguments used to identify the nominal variable.
        :type args: typing.Any

        :return: The nominal variable matching the specified identifier(s).

        :rtype: Variable
        """

        assert len(args) in [1, 2]
        assert isinstance(args[0], str)
        if len(args) == 1:
            return self.__get_nominal_variable_1(*args)
        else:
            assert isinstance(args[1], str)
            return self.__get_nominal_variable_2(*args)

    def __get_nominal_variable_1(self, i1: str) -> Variable:
        """
        Retrieves the decision variable representing the assertion that a specific individual belongs to its corresponding nominal concept. This method serves as a convenience wrapper that calls the general `get_nominal_variable` method, passing the same identifier for both the individual and the concept parameters. The resulting variable is used within the MILP formulation to encode the membership of the individual in the singleton set defined by itself.

        :param i1: The identifier of the individual representing the nominal concept.
        :type i1: str

        :return: A variable representing the assertion that the individual `i1` belongs to the nominal concept `{i1}`.

        :rtype: Variable
        """

        return self.get_nominal_variable(i1, i1)

    def __get_nominal_variable_2(self, i1: str, i2: str) -> Variable:
        """
        Retrieves or creates a binary decision variable representing the assertion that a specific individual belongs to a nominal concept. The method generates a unique variable name by combining the individual identifier and the nominal concept identifier, formatted as 'i1:{ i2 }'. It ensures the returned variable is configured as a binary type, delegating the actual variable lookup or instantiation to the underlying `get_variable` helper method.

        :param i1: The individual acting as the subject of the assertion.
        :type i1: str
        :param i2: An individual representing the nominal concept that the subject individual is asserted to belong to.
        :type i2: str

        :return: A binary Variable representing the assertion that individual i1 belongs to the nominal concept i2.

        :rtype: Variable
        """

        var_name = f"{i1}:{{ {i2} }}"
        v: Variable = self.get_variable(var_name)
        v.set_type(VariableType.BINARY)
        return v

    def is_nominal_variable(self, i: str) -> bool:
        """
        Determines whether the provided string `i` represents a nominal variable by checking if it conforms to the specific naming convention `name:{name}`. The method employs a regular expression to identify substrings where the text preceding a colon matches exactly the text enclosed within curly braces. It returns `True` if at least one such pattern is found within the input string, and `False` otherwise. This function performs a read-only operation and does not produce any side effects on the object's state or the input argument.

        :param i: The string representation of the variable to check.
        :type i: str

        :return: True if the input string matches the pattern 'name:{name}', indicating it is a nominal variable; otherwise, False.

        :rtype: bool
        """

        # s: list[str] = i.split(":{")
        # if len(s) != 2:
        #     return False
        # return s[1] == f"{s[0]}" + "}"
        pattern = re.compile(r"([^:]+):\{\1\}")
        return len(pattern.findall(i)) > 0

    def has_nominal_variable(self, terms: list[Term]) -> bool:
        """
        Determines whether the provided list of terms contains at least one variable that is classified as nominal. The method iterates through the collection, extracting the variable identifier from each term and verifying its status using the `is_nominal_variable` helper. It returns `True` immediately upon finding the first nominal variable and `False` if the list is empty or no such variable is found. This function performs a read-only check and does not modify the input terms.

        :param terms: A list of Term objects to inspect for nominal variables.
        :type terms: list[Term]

        :return: True if the provided list of terms contains at least one nominal variable, False otherwise.

        :rtype: bool
        """

        for term in terms:
            if self.is_nominal_variable(str(term.get_var())):
                return True
        return False

    def exists_nominal_variable(self, i: str) -> bool:
        """
        Determines whether a variable representing the nominal concept for a specific individual `i` is currently defined within the model. The method constructs the expected variable name based on the individual's identifier and checks for its presence in the internal collection of variables. This is a read-only operation that returns a boolean indicating whether the specific nominal variable has been instantiated.

        :param i: The identifier of the individual to check for the existence of a corresponding nominal variable.
        :type i: str

        :return: True if a variable representing the nominal concept for the individual `i` exists, False otherwise.

        :rtype: bool
        """

        var_name: str = f"{i}:{{ {i} }}"
        return var_name in list(map(str, self.variables))

    def get_negated_nominal_variable(self, i1: str, i2: str) -> Variable:
        """
        Retrieves or creates a binary decision variable representing the assertion that a specific individual does not belong to the nominal concept defined by another individual. The variable is identified by the string pattern "{i1}: not { {i2} }". If this variable is being created for the first time, the method sets its type to binary and adds a linear constraint to the model enforcing the relationship that the sum of this negated variable and its corresponding positive nominal variable equals one, ensuring they are mutually exclusive. If the variable already exists within the helper's variable set, it is returned directly without adding new constraints.

        :param i1: The individual representing the entity that is the subject of the negated assertion.
        :type i1: str
        :param i2: The individual representing the nominal concept that `i1` is asserted not to belong to.
        :type i2: str

        :return: A binary variable representing the assertion that individual `i1` does not belong to the nominal concept `{i2}`. If the variable is created for the first time, it is constrained to be the logical complement of the corresponding nominal variable.

        :rtype: Variable
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
        """
        Adds a new constraint to the MILP model, supporting multiple overloads based on the provided arguments to accommodate various ways of defining linear constraints. Depending on the number and types of arguments, the method dispatches to specific internal handlers for cases such as a single `Assertion`; a pair consisting of an `Expression` and `InequalityType`, a `Variable` and a numeric value, an `Assertion` and a numeric value, or a `Variable` and a `Degree`; or a triplet consisting of an `Expression`, an `InequalityType`, and either a `Degree` or a numeric value. If the number of arguments is not between 1 and 3, or if the specific type combination does not match a supported signature, a `ValueError` is raised. This operation modifies the internal state of the helper object by incorporating the new constraint into the underlying model.

        :param args: Variable-length arguments defining the constraint, accepting an Assertion or combinations of Expressions, Variables, InequalityTypes, Degrees, or numeric constants.
        :type args: typing.Any

        :raises ValueError: Raised when the provided arguments do not match any of the supported signatures or type combinations.
        """

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
        Constructs and appends a new inequality constraint to the internal collection of constraints, assuming the right-hand side is zero. The method accepts a mathematical expression and an inequality type (such as equality, greater than, or less than) to define the relationship between the expression and zero. This operation directly modifies the state of the MILP helper by adding the resulting `Inequation` object to the `constraints` list.

        :param expr: The left-hand side expression of the inequality.
        :type expr: Expression
        :param constraint_type: Specifies the relational operator for the inequality, such as equality, greater than, or less than.
        :type constraint_type: InequalityType
        """

        self.constraints.append(Inequation(expr, constraint_type))

    def __add_new_constraint_2(self, x: Variable, n: float) -> None:
        """
        Adds a linear inequality constraint to the model that enforces the variable `x` to be greater than or equal to the numeric value `n`. This method constructs a linear expression representing the variable and delegates to the main constraint addition routine using a greater-than inequality type. As a side effect, the internal state of the optimization model is modified to include this new restriction, which may alter the feasible region of the problem.

        :param x: The variable to be constrained in the inequality.
        :type x: Variable
        :param n: The numeric value representing the lower bound.
        :type n: float
        """

        self.add_new_constraint(
            Expression(Term(1.0, x)),
            InequalityType.GREATER_THAN,
            DegreeNumeric.get_degree(n),
        )

    def __add_new_constraint_3(self, ass: Assertion, n: float) -> None:
        """
        This method enforces a lower bound on the decision variable associated with a given fuzzy assertion by adding a new inequality constraint to the model. It retrieves the variable corresponding to the assertion and ensures that its value is greater than or equal to the specified numeric threshold. As a side effect, this modifies the internal state of the optimization problem by introducing a new constraint, but it does not return any value.

        :param ass: A fuzzy assertion representing the condition a:C >= L.
        :type ass: Assertion
        :param n: The lower bound value for the inequality constraint.
        :type n: float
        """

        self.add_new_constraint(self.get_variable(ass), n)

    def __add_new_constraint_4(self, x: Variable, d: Degree) -> None:
        """
        Adds a linear inequality constraint to the optimization model requiring the specified variable to be greater than or equal to the given degree. This helper method constructs a linear expression representing the variable and delegates to the core constraint addition logic, effectively enforcing a lower bound on the variable within the problem formulation. The operation modifies the internal state of the model by appending this new constraint to the set of defined conditions, assuming that the provided variable and degree are valid types compatible with the underlying solver.

        :param x: The variable on the left-hand side of the inequality.
        :type x: Variable
        :param d: The lower bound for the variable in the inequality.
        :type d: Degree
        """

        self.add_new_constraint(
            Expression(Term(1.0, x)), InequalityType.GREATER_THAN, d
        )

    def __add_new_constraint_5(self, ass: Assertion) -> None:
        """
        Adds a new inequality constraint to the model based on a provided fuzzy assertion. The method extracts the variable associated with the assertion and its lower limit degree. It specifically handles the edge case where the degree is a variable; if the assertion variable and the degree variable are identical, the method returns without adding a constraint to avoid redundancy. If the variables are distinct or the degree is a constant, the method delegates to the standard constraint addition routine to enforce the inequality.

        :param ass: The fuzzy assertion representing the inequality to be added, from which the variable and lower limit are extracted.
        :type ass: Assertion
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
        Constructs and appends a new inequality constraint to the internal list of constraints maintained by the helper. The constraint is defined by a relationship between a provided expression and a degree value, where the specific inequality type (equality, greater than, or less than) is determined by the `constraint_type` argument. The actual construction of the inequality object is delegated to the `degree` argument via its `create_inequality_with_degree_rhs` method, resulting in a direct modification of the object's state.

        :param expr: The expression representing the left-hand side of the inequality.
        :type expr: Expression
        :param constraint_type: Specifies the relational operator for the inequality (e.g., EQ, GR, or LE).
        :type constraint_type: InequalityType
        :param degree: The degree object representing the right-hand side of the inequality.
        :type degree: Degree
        """

        self.constraints.append(
            degree.create_inequality_with_degree_rhs(expr, constraint_type)
        )

    def __add_new_constraint_7(
        self, expr: Expression, constraint_type: InequalityType, n: float
    ) -> None:
        """
        This private method constructs and registers a new inequality constraint where the right-hand side is a scalar value. It accepts a linear expression, a constraint type (such as equality, greater than, or less than), and a floating-point number, converting the number into a `DegreeNumeric` object to match the solver's internal representation. The method then delegates the actual addition of the constraint to the main `add_new_constraint` routine, effectively updating the model's constraints to enforce the specified relationship.

        :param expr: The expression on the left-hand side of the inequality.
        :type expr: Expression
        :param constraint_type: Specifies the relational operator for the inequality, such as equality, greater than, or less than.
        :type constraint_type: InequalityType
        :param n: A real number representing the right-hand side of the inequality.
        :type n: float
        """

        self.add_new_constraint(expr, constraint_type, DegreeNumeric.get_degree(n))

    def add_equality(self, var1: Variable, var2: Variable) -> None:
        """
        Adds a linear constraint to the optimization model that enforces the equivalence of two specified variables. By creating an expression representing the difference between the first and second variable and setting it to zero, this method ensures that the solver assigns the same value to both variables. This action updates the internal model state, potentially affecting the feasibility or optimality of the solution depending on other existing constraints.

        :param var1: The first variable in the equality constraint.
        :type var1: Variable
        :param var2: The variable to equate to var1.
        :type var2: Variable
        """

        self.add_new_constraint(
            Expression(Term(1.0, var1), Term(-1.0, var2)), InequalityType.EQUAL
        )

    def add_string_feature(self, role: str) -> None:
        """
        Appends a specified string role to the internal collection of string features maintained by the helper. This operation modifies the object's state by adding the input to the `string_features` set. If the provided role is already present in the collection, the set ensures that no duplicate entry is created, making the operation idempotent.

        :param role: 
        :type role: str
        """

        self.string_features.add(role)

    def add_string_value(self, value: str, int_value: int) -> None:
        """
        Associates a human-readable string with a specific integer identifier, creating a mapping used to translate between solver indices and feature names. This method updates the internal dictionary responsible for storing these relationships, using the integer as the key and the string as the value. If the provided integer key already exists in the mapping, the previous string value will be overwritten with the new one.

        :param value: The string value to be associated with the integer identifier.
        :type value: str
        :param int_value: The integer key to associate with the string feature value.
        :type int_value: int
        """

        self.string_values[int_value] = value

    def change_variable_names(
        self, old_name: str, new_name: str, old_is_created_individual: bool
    ) -> None:
        """
        Updates the MILP model by renaming variables that include a specific individual identifier, replacing the old name with the new one within variable definitions. It iterates through existing variables to identify matches and establishes constraints linking the original variables to their renamed counterparts. The specific constraint logic depends on whether the old individual is a created individual: if true, an equality constraint is enforced to ensure the variables remain equivalent; otherwise, an inequality constraint is added involving a nominal variable to enforce that the value of the variable associated with the new name is greater than or equal to the value associated with the old name when the nominal condition is met.

        :param old_name: The existing individual name to be replaced within the variable definitions.
        :type old_name: str
        :param new_name: The target individual name used to replace the old name in variable definitions and construct new variable identifiers.
        :type new_name: str
        :param old_is_created_individual: Flag indicating if the old individual is a created individual; if True, an equality constraint is added between the old and new variables, otherwise an inequality constraint is added.
        :type old_is_created_individual: bool
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
        """
        Determines whether the string representations of two variables are structurally identical except for specific substrings located at the same position. The method compares the names of the variables by checking if the substrings `s1` and `s2` appear at the same starting index and if the characters preceding and following these substrings are exactly the same. This effectively verifies if the names follow a pattern of `prefix + s1 + suffix` and `prefix + s2 + suffix`. Note that the method will raise a `ValueError` if either `s1` is not found in the name of `v1` or `s2` is not found in the name of `v2`.

        :param v1: The first variable in the comparison, converted to a string to locate the substring s1 and compare its surrounding context with that of v2.
        :type v1: Variable
        :param s1: The substring to find within the first variable's name, acting as the anchor for comparing the surrounding context.
        :type s1: str
        :param v2: The variable to compare against `v1`, checking if its name matches `v1`'s name with `s2` replacing `s1`.
        :type v2: Variable
        :param s2: The substring within the second variable's name used to verify structural alignment with the first variable.
        :type s2: str

        :return: True if the string representations of v1 and v2 are identical except for the substrings s1 and s2, provided they occur at the same index.

        :rtype: bool
        """

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
        """
        Generates and returns a list of decision variables used to model an ordered permutation within a Mixed-Integer Linear Programming (MILP) context. The method acts as a dispatcher based on the number of arguments provided: it accepts either a single list of variables or a list of variables paired with a two-dimensional list of variables. Input validation is performed to ensure the first argument is a list of `Variable` objects and, if present, the second argument is a list of lists containing `Variable` objects. Depending on the argument count, the logic delegates to internal helper methods to construct the specific variable set required for the permutation constraints.

        :param args: A variable-length argument list accepting either a single list of Variables, or a list of Variables followed by a list of lists of Variables.
        :type args: typing.Any

        :raises ValueError: Raised if the number of provided arguments is not 1 or 2.

        :return: A list of Variable objects representing the ordered permutation derived from the input arguments.

        :rtype: list[Variable]
        """

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
        """
        Constructs an ordered permutation of the input variables by introducing an $n \times n$ matrix of auxiliary binary decision variables to model the sorting constraints. This method generates the necessary binary variables to represent the permutation mapping and delegates the actual constraint formulation and variable ordering to the `get_ordered_permutation` method. As a side effect of this operation, new binary variables are added to the underlying model.

        :param x: The list of variables to be permuted.
        :type x: list[Variable]

        :return: A list of variables representing the ordered permutation of the input list.

        :rtype: list[Variable]
        """

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
        Constructs a set of new variables representing the input variables sorted in non-increasing order. The method creates `n` semi-continuous variables `y` and adds constraints to enforce the sequence `y[0] >= y[1] >= ... >= y[n-1]`. It utilizes the provided matrix `z` to establish a system of linear constraints that ensures `y` is a permutation of the input list `x`, specifically by linking the values of `x` and `y` through `z` and enforcing that the sum of each row and column in `z` equals `n-1`. This process modifies the underlying model by adding these constraints and introducing the new variables.

        :param x: The list of variables to be sorted into a non-increasing order.
        :type x: list[Variable]
        :param z: A matrix of auxiliary variables used to formulate the constraints linking the input variables to the sorted output.
        :type z: list[list[Variable]]

        :return: A list of new variables representing the input variables sorted in non-increasing order.

        :rtype: list[Variable]
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
        """
        Identifies connected components within the graph using a Breadth-First Search (BFS) approach and assigns partition identifiers to nodes. The method initializes the provided solution dictionary, mapping all nodes to a default partition of 0, and then iterates through the nodes to find unvisited starting points. For each unvisited node, it invokes the `__compute_partition` helper method to traverse the graph and assign the current partition ID to all reachable nodes. The `solution` dictionary is modified in place to reflect these assignments, and the method returns the total count of partitions found.

        :param graph: The graph structure to be traversed and partitioned.
        :type graph: nx.Graph
        :param solution: Dictionary mapping node indices to their assigned partition IDs, modified in place to store the result.
        :type solution: dict[int, int]

        :return: The total number of partitions identified in the graph.

        :rtype: int
        """

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

        """
        Propagates a partition identifier through a graph starting from the nodes provided in the queue. The method iteratively processes nodes, assigning the specified partition ID `p` to all adjacent neighbors that have not yet been assigned a value in the solution dictionary. This traversal continues until the queue is exhausted, effectively marking a connected region of the graph. The `solution` dictionary is modified in-place to reflect these assignments, and the input `queue` is consumed during the operation.

        :param queue: List of node identifiers to be processed, used to traverse the graph and assign the partition ID to connected neighbors.
        :type queue: list[int]
        :param solution: Dictionary mapping node IDs to partition assignments, where a value of 0 indicates an unassigned node. Updated in place to assign the partition ID `p` to reachable nodes.
        :type solution: dict[int, int]
        :param p: The partition identifier or label to assign to nodes.
        :type p: int
        :param graph: The graph structure defining the connectivity between nodes, used to identify neighbors during the partition traversal.
        :type graph: nx.Graph
        """

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
        """
        Updates the configuration of the MILP helper instance by setting the flag that determines whether nominal variables are used. This method accepts a boolean value, which is assigned to the instance's internal state, thereby influencing the formulation of the optimization problem in subsequent operations. The operation modifies the object in-place and does not return a value.

        :param value: Flag indicating whether nominal variables are enabled.
        :type value: bool
        """

        self.nominal_variables = value

    def __remove_nominal_variables(self) -> None:
        """This method purges nominal variables and any constraints that depend on them from the object's internal state. It iterates through the existing constraints to identify those containing nominal terms and scans the variables to determine which are nominal. Once the indices of these elements are collected, the method reconstructs the `constraints` and `variables` lists, excluding the identified items. This process mutates the object's state by reassigning these attributes, effectively removing data that is incompatible with the solver's requirements. If no nominal variables or dependent constraints are present, the lists remain unchanged."""

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
        """
        Constructs a NetworkX graph representing the relationships between variables based on the defined constraints. Nodes are added for each variable in the internal list, indexed by their order. Edges are created by iterating through the constraints; for each constraint containing multiple terms, the method connects the first variable to every subsequent variable in that constraint, effectively creating a star topology for each constraint. Each edge is labeled with a unique sequential number. The method returns the newly created graph without modifying the state of the MILP helper instance, and it skips constraints that contain no terms.

        :return: A NetworkX graph where nodes represent variables and edges connect variables that appear together in a constraint. Each edge is assigned a unique sequential number.

        :rtype: nx.Graph
        """

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

        """
        Performs a graph-based partitioning of the variables involved in the provided objective expression to analyze their distribution across the problem structure. It utilizes a breadth-first search (BFS) algorithm on the internal graph to group variables into partitions, then maps the specific variables from the objective to these partitions. The method returns a tuple containing the list of objective variables, the mapping of variable indices to partition IDs, the total number of partitions, a breakdown of variable counts per partition, and statistics identifying partitions that contain multiple objective variables. This operation relies on the internal graph and variable list, logs the execution time for debugging, and assumes that all variables found in the objective are present within the graph structure.

        :param objective: The objective function expression used to extract variables for partition analysis.
        :type objective: Expression

        :return: A tuple containing the list of objective variables, a mapping of variable indices to partition IDs, the total number of partitions, a list of variable counts per partition, the number of partitions containing multiple variables, and the total count of variables within those partitions.

        :rtype: tuple[list[Variable], dict[int, int], int, list[int], int, int]
        """

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
        """
        This method solves a Mixed-Integer Linear Programming (MILP) problem by decomposing it into smaller sub-problems based on variable partitions, utilizing the Gurobi optimizer. It begins by determining the partition structure of the variables relative to the objective; if no partition contains more than one variable, it disables the partitioning strategy and delegates to the standard solver. The algorithm proceeds in two phases: first, it solves a model containing only variables from partitions with zero or one variable to check for immediate infeasibility. Second, for each variable in the objective that belongs to a partition with multiple variables, it constructs and optimizes a separate Gurobi model restricted to that partition, effectively optimizing for that specific variable within its local constraints. The results are aggregated into a Solution object, which is returned unless a sub-problem is infeasible (resulting in an inconsistent knowledge base indicator) or a Gurobi error occurs (resulting in None).

        :param objective: The mathematical expression representing the objective function to be optimized. It is analyzed to determine variable partitions and defines the optimization target for the sub-problems.
        :type objective: Expression

        :return: A Solution object representing the optimization result, or None if a Gurobi error occurs. If the model is infeasible, the Solution indicates an inconsistent knowledge base.

        :rtype: typing.Optional[Solution]
        """

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

                vars_gurobi[var_name_map[str(curr_variable)]] = model.addVar(
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

                vars_gurobi[var_name_map[str(curr_variable)]] = model.addVar(
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
        Constructs and optimizes a Mixed-Integer Linear Programming (MILP) model using the Gurobi solver based on the variables and constraints defined in the current instance. It translates the provided objective expression into Gurobi coefficients and handles various variable types, including binary, integer, continuous, and semi-continuous, while respecting their bounds. The method filters out duplicate or zero constraints before optimization and delegates to a partition-based solver if the `PARTITION` flag is enabled. Upon completion, it writes the model and solution files to the results directory and prints statistics or debug information if configured. If the model is infeasible, it returns a Solution object indicating inconsistency; if a Gurobi error occurs, it logs the exception and returns None.

        :param objective: The linear expression representing the objective function to be optimized.
        :type objective: Expression

        :return: A Solution object containing the optimal objective value and relevant variable assignments if the model is feasible, a Solution indicating inconsistency if the model is infeasible, or None if a Gurobi error occurs during solving.

        :rtype: typing.Optional[Solution]
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
        """
        Constructs and solves a Mixed-Integer Linear Programming (MIP) model using the CBC solver to minimize the provided objective expression. The method translates internal variable definitions and constraints into a `mip.Model`, handling binary, integer, continuous, and semi-continuous variable types while respecting their bounds. It returns a `Solution` object containing the optimal objective value and variable values, or a specific solution indicating an inconsistent knowledge base if the problem is infeasible. If an exception occurs during the process, the method returns `None`. Side effects include writing the generated model and solution files to the results directory and logging debug information regarding the model's structure and optimization statistics.

        :param objective: The linear expression defining the objective function to be minimized by the MIP solver.
        :type objective: Expression

        :return: A Solution object containing the optimization result, including the objective value and variable assignments if feasible, or a status indicating inconsistency if the model is infeasible. Returns None if an error occurs during the solving process.

        :rtype: typing.Optional[Solution]
        """

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
        """
        Solves the defined Mixed-Integer Linear Programming (MILP) problem using the PuLP library to minimize the provided objective expression. The method constructs a PuLP model by mapping internal variables to PuLP variables, supporting binary, integer, continuous, and semi-continuous types. Specifically, for semi-continuous variables when using GLPK or CPLEX, it introduces auxiliary binary variables and linear constraints to enforce the semi-continuous domain. It iterates through the helper's constraints to populate the model, skipping zero or duplicate entries. The solver is selected and configured dynamically based on the `MILP_PROVIDER` setting, with specific tolerances and logging options applied for CBC, GLPK, HiGHS, and CPLEX. Upon completion, it returns a `Solution` object containing the optimal objective value and variable assignments, or a specific solution indicating inconsistency if the problem is infeasible. If an exception occurs during the process, the method returns `None`. Side effects include generating debug logs, writing temporary log and model files to disk, and cleaning up specific temporary files created by CPLEX.

        :param objective: The linear expression defining the objective function to be minimized.
        :type objective: Expression

        :return: A Solution object containing the optimal objective value and variable assignments if the MILP problem is solved successfully. If the problem is infeasible or unbounded, returns a Solution indicating an inconsistent knowledge base. Returns None if an exception occurs during execution.

        :rtype: typing.Optional[Solution]
        """

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
        """
        Marks a specified concept as crisp by adding its identifier to the internal collection of crisp concepts. This method updates the state of the MILPHelper instance to indicate that the given concept should be treated with crisp logic during subsequent operations. Since the underlying storage is a set, adding a concept that has already been marked as crisp will have no additional effect.

        :param concept_name: The name of the concept to be defined as crisp.
        :type concept_name: str
        """

        self.crisp_concepts.add(concept_name)

    def add_crisp_role(self, role_name: str) -> None:
        """
        Registers the specified role name as a crisp role by adding it to the internal collection of crisp roles. This action modifies the object's state to indicate that the role should be treated as non-fuzzy or binary in subsequent operations. The operation is idempotent; if the role name is already present in the collection, the method has no effect.

        :param role_name: Name of the role to be defined as crisp.
        :type role_name: str
        """

        self.crisp_roles.add(role_name)

    def is_crisp_concept(self, concept_name: str) -> bool:
        """
        Determines whether the specified concept is classified as a crisp concept by checking its membership in the internal collection of crisp concepts. The method returns True if the concept name is present in the collection, indicating a crisp definition, and False otherwise. This operation is read-only and does not modify the state of the helper object.

        :param concept_name: The identifier of the concept to verify.
        :type concept_name: str

        :return: True if the specified concept name is present in the set of crisp concepts, otherwise False.

        :rtype: bool
        """

        return concept_name in self.crisp_concepts

    def is_crisp_role(self, role_name: str) -> bool:
        """
        Determines if the specified role is classified as a crisp role by checking for its presence in the internal collection of crisp roles. This method returns a boolean value indicating whether the role name is a member of that collection. It performs a read-only operation and does not modify the state of the object.

        :param role_name: The name of the role to check for crispness.
        :type role_name: str

        :return: True if the specified role is a crisp role, False otherwise.

        :rtype: bool
        """

        return role_name in self.crisp_roles

    def set_binary_variables(self) -> None:
        """Iterates over the collection of variables managed by the helper and converts them into binary variables, restricting their domain to the discrete set {0, 1}. This transformation specifically excludes variables that are already defined as continuous or integer, as well as those designated as datatype fillers. The method modifies the state of the variable objects in place, effectively preparing the model for a Mixed-Integer Linear Programming context by enforcing boolean constraints on the applicable variables."""

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
        """
        Retrieves the symbolic name associated with a specific integer index by performing a reverse lookup on the internal mapping of variable names to their integer identifiers. If the provided integer corresponds to a known variable index, the method returns the associated name string; otherwise, it returns None to indicate that no variable is currently mapped to that value. This is a read-only operation that does not modify the state of the object.

        :param i: The integer identifier of the variable to look up.
        :type i: int

        :return: The name of the variable associated with the given integer, or None if the integer is not found.

        :rtype: typing.Optional[str]
        """

        for name, i2 in self.number_of_variables.items():
            if i == i2:
                return name
        return None

    def get_number_for_assertion(self, ass: Assertion) -> int:
        """
        Retrieves the integer codification associated with a given assertion by first resolving the assertion to its variable representation and then looking up the corresponding integer value in the internal variable mapping. This method serves as a bridge between logical assertions and their numerical identifiers used in the MILP formulation, performing a read-only operation without modifying the underlying data structures. If the assertion has not been previously registered in the mapping, the method returns None.

        :param ass: The assertion to be converted into an integer codification.
        :type ass: Assertion

        :return: The integer identifier associated with the variable of the assertion.

        :rtype: int
        """

        return self.number_of_variables.get(str(self.get_variable(ass)))

    def add_contradiction(self) -> None:
        """Forces the fuzzy Knowledge Base (KB) into an unsatisfiable state by introducing a logical contradiction. This method first clears all existing constraints stored in the helper, effectively discarding any prior model state. It then adds a new constraint requiring a constant expression of 1.0 to equal zero, which is mathematically impossible, thereby ensuring that the MILP model becomes infeasible."""

        self.constraints.clear()
        self.add_new_constraint(Expression(1.0), InequalityType.EQUAL)

    def add_cardinality_list(self, sc: SigmaCount) -> None:
        """
        Appends a `SigmaCount` object to the internal collection of cardinality constraints maintained by the helper. This method registers a specific cardinality calculation, defined by a role, a concept, and a set of candidate individuals, for subsequent processing in the Mixed-Integer Linear Programming (MILP) model. The operation modifies the state of the instance by adding the element to the `cardinalities` list and returns `None`. It does not perform validation on the input object or check for duplicates within the list.

        :param sc: The cardinality constraint object to be appended to the list.
        :type sc: SigmaCount
        """

        self.cardinalities.append(sc)
