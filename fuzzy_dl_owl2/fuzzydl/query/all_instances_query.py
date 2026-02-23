from __future__ import annotations

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.degree.degree_expression import DegreeExpression
from fuzzy_dl_owl2.fuzzydl.exception.inconsistent_ontology_exception import (
    InconsistentOntologyException,
)
from fuzzy_dl_owl2.fuzzydl.individual.created_individual import CreatedIndividual
from fuzzy_dl_owl2.fuzzydl.individual.individual import Individual
from fuzzy_dl_owl2.fuzzydl.knowledge_base import KnowledgeBase
from fuzzy_dl_owl2.fuzzydl.milp.expression import Expression
from fuzzy_dl_owl2.fuzzydl.milp.milp_helper import MILPHelper
from fuzzy_dl_owl2.fuzzydl.milp.solution import Solution
from fuzzy_dl_owl2.fuzzydl.milp.term import Term
from fuzzy_dl_owl2.fuzzydl.milp.variable import Variable
from fuzzy_dl_owl2.fuzzydl.query.min.min_instance_query import MinInstanceQuery
from fuzzy_dl_owl2.fuzzydl.query.query import Query
from fuzzy_dl_owl2.fuzzydl.util.constants import VariableType
from fuzzy_dl_owl2.fuzzydl.util.util import Util


class AllInstancesQuery(Query):
    """
    This class represents a query designed to retrieve all individuals from a knowledge base that are instances of a specified concept, along with their respective degrees of membership. It supports fuzzy logic by determining the minimum degree to which each individual satisfies the concept, rather than relying on binary classification. To use this class, instantiate it with a target `Concept` object—ensuring the concept is not concrete—and invoke the `solve` method with a `KnowledgeBase` to perform the retrieval. The results can be accessed via the `get_individuals` and `get_degrees` methods, which return the list of matching entities and their calculated membership values.

    :param conc: The concept defining the criteria for retrieving instances and calculating membership degrees.
    :type conc: typing.Any
    :param degrees: Stores the membership degrees corresponding to the retrieved individuals, indicating the extent to which each satisfies the concept.
    :type degrees: list[float]
    :param individuals: The list of individuals from the knowledge base that are evaluated for membership in the concept.
    :type individuals: list[Individual]
    :param name: A string representation of the query that stores the formatted results, including individuals and their degrees, or an error message upon execution.
    :type name: typing.Any
    """


    def __init__(self, concept: Concept) -> None:
        """
        Initializes the query object designed to find all instances associated with a specific concept. It accepts a `Concept` argument which must not be concrete; if a concrete concept is provided, the method triggers an error via `Util.error`. The constructor stores the concept, initializes empty lists to hold the resulting individuals and their degrees, and generates a descriptive name for the query. It also invokes the superclass initializer to ensure proper object setup.

        :param concept: The abstract concept for which instances are being queried. Must not be a concrete concept.
        :type concept: Concept
        """

        super().__init__()
        if concept.is_concrete():
            Util.error(f"Error: {concept} cannot be a concrete concept.")
        self.conc = concept
        self.degrees: list[float] = []
        self.individuals: list[Individual] = []
        self.name = f"Instances of {self.conc}?"

    def preprocess(self, kb: KnowledgeBase) -> None:
        """
        Prepares the query for execution by performing necessary setup operations using the provided `KnowledgeBase`. This method typically involves validating the query parameters, resolving internal references, or optimizing the retrieval strategy based on the schema or data available in the knowledge base. It modifies the internal state of the query object in place and does not return a value.

        :param kb: The knowledge base object to be preprocessed or prepared for subsequent operations.
        :type kb: KnowledgeBase
        """

        pass

    def solve(self, kb: KnowledgeBase) -> Solution:
        """
        Executes the query to identify all individuals within the Knowledge Base that are instances of the specified concept. It begins by validating the consistency of the ABox, returning a specific solution if the ontology is found to be inconsistent. The method iterates through the individuals in the knowledge base, ignoring any that are dynamically created, and performs a minimum instance query for each to determine the degree of membership. As consistent results are found, they are appended to the internal list of degrees and formatted into the query's name string. If an inconsistency arises during the iteration, the loop terminates immediately, and the inconsistent solution is returned.

        :param kb: The knowledge base containing the ontology and individuals to be queried and solved.
        :type kb: KnowledgeBase

        :return: A Solution object representing the result of the operation. If the Knowledge Base is inconsistent, the solution indicates this error state; otherwise, it contains the result of the minimum instance query for the last individual processed.

        :rtype: Solution
        """

        sol: Solution = None
        self.name: str = ""
        self.individuals: list[Individual] = list(kb.individuals.values())

        try:
            kb.solve_abox()
        except InconsistentOntologyException as e:
            return Solution(Solution.INCONSISTENT_KB)

        for i in self.individuals:
            if isinstance(i, CreatedIndividual):
                continue
            q: MinInstanceQuery = MinInstanceQuery(self.conc, i)
            sol: Solution = q.solve(kb)
            if sol.is_consistent_kb():
                self.degrees.append(float(sol.get_solution()))
                self.name += f"{q}{sol.get_solution()}\n"
                continue
            self.name = f"Instances of {self.conc}? Inconsistent KB"
            break
        return sol

    def solve_new(self, kb: KnowledgeBase) -> Solution:
        """
        Implements a specific algorithm to retrieve instances of the target concept by calculating the degree of membership for each individual in the provided knowledge base. The method operates on a clone of the input knowledge base to preserve the original state, first checking for consistency; if the ABox is inconsistent, it returns a solution indicating an inconsistent knowledge base. For each individual, excluding those that are dynamically created, it introduces a new semi-continuous variable into the MILP model and adds assertions that link the individual's relationship to the concept with this variable. It then constructs an objective function to maximize the sum of these variables and performs an optimization. As a side effect of this process, the method updates the instance's internal state by populating `self.degrees` with the calculated membership values and `self.name` with a descriptive string of the results, while temporarily toggling MILP helper flags for the optimization step.

        :param kb: The knowledge base containing the ontology and individuals to be analyzed. It is cloned internally to ensure the original object remains unmodified during the solving process.
        :type kb: KnowledgeBase

        :return: A Solution object containing the optimization results, including the degrees of membership for individuals regarding the target concept, or indicating an inconsistent knowledge base.

        :rtype: Solution
        """

        self.name: str = ""
        new_variables: list[Variable] = list()
        var_names: dict[str, str] = dict()
        self.individuals: list[Individual] = list(kb.individuals.values())
        cloned: KnowledgeBase = kb.clone()

        try:
            cloned.solve_abox()
        except InconsistentOntologyException as e:
            return Solution(Solution.INCONSISTENT_KB)

        for i in self.individuals:
            if isinstance(i, CreatedIndividual):
                continue
            q: Variable = cloned.milp.get_new_variable(VariableType.SEMI_CONTINUOUS)
            cloned.old_01_variables += 1
            s: str = f"Is {i} instance of {self.conc}? >= "
            var_names[str(q)] = s
            cloned.milp.show_vars.add_variable(q, s)
            new_variables.append(q)
            # a: not c >= 1-q
            cloned.add_assertion(
                i,
                -self.conc,
                DegreeExpression.get_degree(Expression(1.0, Term(-1.0, q))),
            )
        cloned.solve_assertions()
        obj_expr: Expression = Expression()
        for var in new_variables:
            obj_expr.add_term(Term(1.0, var))

        MILPHelper.PRINT_LABELS = False
        MILPHelper.PRINT_VARIABLES = False
        MILPHelper.PARTITION = True
        sol: Solution = cloned.optimize(obj_expr)
        MILPHelper.PARTITION = False
        MILPHelper.PRINT_LABELS = True
        MILPHelper.PRINT_VARIABLES = True

        if sol.is_consistent_kb():
            ht: dict[str, float] = sol.get_showed_variables()
            individuals_and_degrees: dict[str, float] = dict()
            for s in ht:
                var_name: str = var_names.get(s)
                value: float = ht.get(s)
                self.name += f"{var_name} {value}\n"
                individuals_and_degrees[var_name, value]

            for i in range(len(self.individuals)):
                var_name: str = f"Is {self.individuals[i]} instance of {self.conc} >= "
                value: float = individuals_and_degrees.get(var_name)
                self.degrees.append(value)
        else:
            self.name = f"Instances of {self.conc}? Inconsistent KB"
        return sol

    def get_individuals(self) -> list[Individual]:
        """
        Retrieves the list of `Individual` objects stored in the `individuals` attribute of the query instance. This method serves as a direct accessor and does not modify the object's state or perform any calculations. Because it returns a reference to the internal list, any in-place modifications made to the returned list will be reflected in the query object's internal state.

        :return: The list of individuals stored in the instance.

        :rtype: list[Individual]
        """

        return self.individuals

    def get_degrees(self) -> list[float]:
        """
        Retrieves the collection of degree values stored within the query instance. This accessor returns the reference to the internal `degrees` attribute, which is a list of floating-point numbers. Note that because the list object is returned directly, modifications to the returned list will affect the internal state of the query object.

        :return: A list of floating-point numbers representing the degree values.

        :rtype: list[float]
        """

        return self.degrees

    def __str__(self) -> str:
        """
        Returns the informal string representation of the query object, which is utilized by the built-in `str()` function and `print()` calls. This implementation simply delegates to the instance's `name` attribute, ensuring that the object is represented by its identifying name in user-facing contexts. Since it relies on the `name` attribute, it assumes that the attribute is defined and holds a value suitable for string representation.

        :return: The string representation of the object, which is its name.

        :rtype: str
        """

        return self.name
