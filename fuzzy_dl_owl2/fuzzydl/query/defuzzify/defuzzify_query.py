from __future__ import annotations

import typing
from abc import abstractmethod

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.degree.degree_numeric import DegreeNumeric
from fuzzy_dl_owl2.fuzzydl.exception.inconsistent_ontology_exception import (
    InconsistentOntologyException,
)
from fuzzy_dl_owl2.fuzzydl.individual.created_individual import CreatedIndividual
from fuzzy_dl_owl2.fuzzydl.individual.individual import Individual
from fuzzy_dl_owl2.fuzzydl.knowledge_base import KnowledgeBase
from fuzzy_dl_owl2.fuzzydl.milp.expression import Expression
from fuzzy_dl_owl2.fuzzydl.milp.milp_helper import MILPHelper
from fuzzy_dl_owl2.fuzzydl.milp.solution import Solution
from fuzzy_dl_owl2.fuzzydl.milp.variable import Variable
from fuzzy_dl_owl2.fuzzydl.query.max.max_satisfiable_query import MaxSatisfiableQuery
from fuzzy_dl_owl2.fuzzydl.query.query import Query
from fuzzy_dl_owl2.fuzzydl.relation import Relation
from fuzzy_dl_owl2.fuzzydl.util.util import Util


class DefuzzifyQuery(Query):
    """
    This abstract class defines the structure for performing defuzzification, which involves converting a fuzzy membership degree into a crisp value for a specific individual and feature within a knowledge base. During execution, it first determines the maximum degree of membership for the individual to the given concept and asserts this value into a cloned version of the knowledge base. It then identifies the variable associated with the specified feature and optimizes an objective expression derived from that variable to produce the final result. Subclasses are required to implement the abstract method for generating the objective expression, allowing for different defuzzification strategies to be applied. The process relies on Mixed-Integer Linear Programming (MILP) and handles potential inconsistencies in the ontology gracefully.

    :param conc: The concept for which the defuzzification operation is performed.
    :type conc: Concept
    :param a: The individual entity for which the defuzzification query is being executed.
    :type a: Individual
    :param f_name: The name of the feature for which to perform defuzzification.
    :type f_name: str
    :param obj_expr: The objective expression used to optimize the solution, representing the degree of membership of the individual to the concept.
    :type obj_expr: Expression
    """


    def __init__(self, c: Concept, ind: Individual, feature_name: str) -> None:
        """
        Initializes a new instance of the query object by associating a specific concept and individual with a named feature. The constructor stores these parameters as instance attributes to define the context of the defuzzification operation. It also configures the underlying Mixed-Integer Linear Programming (MILP) environment by disabling verbose output for variables and labels, and initializes the placeholder for the objective expression.

        :param c: The concept object to be associated with this instance.
        :type c: Concept
        :param ind: The specific individual instance or entity involved in the feature definition.
        :type ind: Individual
        :param feature_name: The name of the feature associated with this instance.
        :type feature_name: str
        """

        super().__init__()
        self.conc: Concept = c
        self.a: Individual = ind
        self.f_name: str = feature_name
        self.obj_expr: Expression = None
        MILPHelper.PRINT_VARIABLES = False
        MILPHelper.PRINT_LABELS = False

    def preprocess(self, kb: KnowledgeBase) -> None:
        """
        Prepares the defuzzification query by solving a maximum satisfiability problem to determine the optimal degree for the conclusion associated with the current individual. If a consistent solution is found, the method updates the internal reference to the individual, asserts the calculated numeric degree back into the knowledge base, and resolves these assertions. Furthermore, it inspects the individual's role relations to identify a specific target individual, retrieving the corresponding MILP variable to construct and store an objective expression for later use.

        :param kb: The knowledge base instance used to solve queries, retrieve individuals, and manage assertions and MILP variables. This object is modified during the preprocessing step.
        :type kb: KnowledgeBase
        """

        kb.set_dynamic_blocking()
        s: Solution = MaxSatisfiableQuery(self.conc, self.a).solve(kb)

        if s is not None and s.is_consistent_kb():
            self.a = kb.individuals[str(self.a)]
            kb.set_dynamic_blocking()
            kb.add_assertion(
                self.a, self.conc, DegreeNumeric.get_degree(s.get_solution())
            )
            kb.solve_assertions()

            if self.f_name in self.a.role_relations:
                rel_set: list[Relation] = self.a.role_relations[self.f_name]
                b: CreatedIndividual = typing.cast(
                    CreatedIndividual, rel_set[0].get_object_individual()
                )
                q: Variable = kb.milp.get_variable(b)
                self.obj_expr = self.get_obj_expression(q)

    def solve(self, kb: KnowledgeBase) -> typing.Optional[Solution]:
        """
        Attempts to solve the defuzzification problem by first resolving the ABox of the provided Knowledge Base and then operating on a cloned instance to preserve the original state. The method applies preprocessing to the clone and, if an objective expression is defined, performs an optimization to find a solution. If the resulting solution value is negative, it is converted to its absolute value before being returned. If no objective expression is available, the method issues a warning and returns None. Furthermore, it handles inconsistent ontologies by catching the specific exception and returning a Solution object marked as inconsistent.

        :param kb: The knowledge base containing the ontology and ABox to be solved and optimized.
        :type kb: KnowledgeBase

        :return: A Solution object representing the optimization result, or None if the objective expression is missing or a defuzzification problem occurs. Returns a specific Solution indicating inconsistency if the ontology is inconsistent.

        :rtype: typing.Optional[Solution]
        """

        try:
            kb.solve_abox()
            cloned: KnowledgeBase = kb.clone()
            self.preprocess(cloned)

            if self.obj_expr is not None:
                MILPHelper.PRINT_LABELS = True
                MILPHelper.PRINT_VARIABLES = True

                sol: Solution = cloned.optimize(self.obj_expr)
                if sol.get_solution() < 0.0:
                    return Solution(-sol.get_solution())
                return sol

            Util.warning("Warning: Problem in defuzzification. Answer is 0.")
            return None
        except InconsistentOntologyException:
            return Solution(Solution.INCONSISTENT_KB)

    @abstractmethod
    def get_obj_expression(self, variable: Variable) -> Expression:
        """
        Retrieves the objective expression associated with the specified variable for the defuzzification process. This abstract method requires subclasses to implement the logic for constructing the expression, which typically represents the target function or calculation needed to resolve the fuzzy variable into a crisp value. The implementation determines how the variable's properties are translated into a formal expression used by the query engine.

        :param variable: The variable instance for which the corresponding object expression is to be retrieved.
        :type variable: Variable

        :return: The expression representing the object associated with the provided variable.

        :rtype: Expression
        """

        pass
