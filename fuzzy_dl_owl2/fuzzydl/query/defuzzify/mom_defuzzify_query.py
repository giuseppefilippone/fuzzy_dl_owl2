from __future__ import annotations

import traceback
import typing

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.degree.degree_numeric import DegreeNumeric
from fuzzy_dl_owl2.fuzzydl.exception.fuzzy_ontology_exception import (
    FuzzyOntologyException,
)
from fuzzy_dl_owl2.fuzzydl.exception.inconsistent_ontology_exception import (
    InconsistentOntologyException,
)
from fuzzy_dl_owl2.fuzzydl.individual.created_individual import CreatedIndividual
from fuzzy_dl_owl2.fuzzydl.individual.individual import Individual
from fuzzy_dl_owl2.fuzzydl.knowledge_base import KnowledgeBase
from fuzzy_dl_owl2.fuzzydl.milp.expression import Expression
from fuzzy_dl_owl2.fuzzydl.milp.solution import Solution
from fuzzy_dl_owl2.fuzzydl.milp.term import Term
from fuzzy_dl_owl2.fuzzydl.milp.variable import Variable
from fuzzy_dl_owl2.fuzzydl.query.defuzzify.defuzzify_query import DefuzzifyQuery
from fuzzy_dl_owl2.fuzzydl.query.max.max_satisfiable_query import MaxSatisfiableQuery
from fuzzy_dl_owl2.fuzzydl.relation import Relation
from fuzzy_dl_owl2.fuzzydl.util.util import Util


class MomDefuzzifyQuery(DefuzzifyQuery):
    """This class implements a defuzzification strategy that calculates the crisp value of a specific feature for an individual based on the "middle of maxima" principle within a fuzzy ontology framework. To determine the result, it first establishes the maximum degree of membership the individual has to a given concept. It then performs optimization to find the smallest and largest feature values that satisfy this maximum membership degree, effectively identifying the boundaries of the membership plateau. The final output is the arithmetic mean of these two boundary values. Users should instantiate this class with a target concept, an individual, and a feature name, then invoke the solve method with a knowledge base to retrieve the calculated solution."""


    def __init__(self, c: Concept, ind: Individual, feature_name: str) -> None:
        """
        Initializes a new instance designed to perform Mean of Maxima (Mom) defuzzification on a specific feature of an individual relative to a concept. The method accepts a `Concept` object defining the fuzzy criteria, an `Individual` object representing the entity to be evaluated, and a string identifying the target feature. By invoking the superclass initializer, this constructor delegates the core state management to the parent class, ensuring the object is properly configured for subsequent execution of the defuzzification logic.

        :param c: The concept instance associated with the individual and feature.
        :type c: Concept
        :param ind: The individual entity to which the feature applies.
        :type ind: Individual
        :param feature_name: The name of the feature or attribute associated with the concept and individual.
        :type feature_name: str
        """

        super().__init__(c, ind, feature_name)

    def preprocess(self, kb: KnowledgeBase) -> None:
        """
        Prepares the internal state of the query object for the Mean of Maxima (MoM) defuzzification process by interacting with the provided KnowledgeBase. This method retrieves and validates the configuration of the target output variable, ensuring that the necessary fuzzy sets and universe of discourse are available for calculation. As a side effect, it updates the instance attributes to store intermediate results or references required for the subsequent defuzzification step, potentially raising an error if the specified variable cannot be found in the KnowledgeBase or is improperly configured.

        :param kb: The knowledge base object to be preprocessed.
        :type kb: KnowledgeBase
        """

        pass

    def solve(self, kb: KnowledgeBase) -> Solution:
        """
        Executes a Mean of Maxima (MOM) defuzzification strategy to derive a crisp numerical value from a fuzzy knowledge base. The method begins by solving the ABox of the input knowledge base and determining the maximum degree of membership for the target concept and individual via a max-satisfiability query. It then creates a modified clone of the knowledge base where the individual is asserted to possess the concept at this maximum degree, subsequently identifying the MILP variable associated with the specified role relation. The solution is calculated by optimizing this variable to find both the minimum and maximum values within the feasible region and returning their average. Edge cases include returning an inconsistent solution if the ontology cannot be solved or if optimization fails, and returning None with a warning if the required role relations or variables are absent. The method has side effects of solving the ABox of the input knowledge base and printing warnings or stack traces to standard output upon encountering errors.

        :param kb: The input knowledge base containing the ontology, individuals, and assertions used to perform the reasoning and optimization tasks.
        :type kb: KnowledgeBase

        :return: A Solution object containing the calculated numeric value (Mean of Maximums) derived from fuzzy logic optimization, or None if defuzzification fails. The Solution may also indicate an inconsistent knowledge base.

        :rtype: Solution
        """

        try:
            kb.solve_abox()
            cloned: KnowledgeBase = kb.clone()
            cloned.set_dynamic_blocking()
            s: Solution = MaxSatisfiableQuery(self.conc, self.a).solve(cloned)
            if not s.is_consistent_kb():
                return s
            d: float = s.get_solution()
            # LOM
            cloned: KnowledgeBase = kb.clone()
            ind: Individual = cloned.individuals.get(str(self.a))
            cloned.set_dynamic_blocking()
            cloned.add_assertion(self.a, self.conc, DegreeNumeric.get_degree(d))
            cloned.solve_assertions()
            if self.f_name not in ind.role_relations:
                Util.warning("Warning: Problem in defuzzification. Answer is 0.")
                return None
        except InconsistentOntologyException:
            return Solution(Solution.INCONSISTENT_KB)

        rel_set: list[Relation] = ind.role_relations.get(self.f_name)
        b: CreatedIndividual = typing.cast(
            CreatedIndividual, rel_set[0].get_object_individual()
        )
        q: Variable = cloned.milp.get_variable(b)
        if q is None:
            Util.warning("Warning: Problem in defuzzification. Answer is 0.")
            return None

        try:
            obj_expr: Expression = Expression(Term(-1.0, q))
            sol1: Solution = cloned.optimize(obj_expr)
            if sol1.get_solution() < 0.0:
                sol1 = Solution(sol1.get_solution())

            # SOM
            obj_expr: Expression = Expression(Term(1.0, q))
            sol2: Solution = cloned.optimize(obj_expr)
            if sol2.get_solution() < 0.0:
                sol2 = Solution(sol2.get_solution())

            # MOM
            if sol1.is_consistent_kb() and sol2.is_consistent_kb():
                value = (sol1.get_solution() + sol2.get_solution()) / 2.0
                kb.milp.print_instance_of_labels(self.f_name, str(self.a), value)
                return Solution(value)

            # Returns an inconsistent KB solution
            return sol1
        except FuzzyOntologyException as e:
            traceback.print_exc()
        except InconsistentOntologyException as e:
            traceback.print_exc()
        return Solution(Solution.INCONSISTENT_KB)

    def get_obj_expression(self, variable: Variable) -> Expression:
        # Put anything here, we do not use this method
        """
        Returns a placeholder objective expression for the provided variable. This method is currently not utilized within the defuzzification logic and serves as a stub implementation. It constructs and returns an Expression object containing a single Term with a coefficient of -1.0, regardless of the input variable's state.

        :param variable: The variable object to be used in constructing the expression.
        :type variable: Variable

        :return: An Expression object representing the negative of the provided variable.

        :rtype: Expression
        """

        return Expression(Term(-1.0, variable))

    def __str__(self) -> str:
        """
        Provides a human-readable string representation of the Middle of Maxima (MoM) defuzzification query object. The returned string formats a description that includes the specific feature name and instance identifier associated with the query, ending with an equals sign to facilitate the display of the resulting value. This method relies on the existence of the `f_name` and `a` attributes; accessing this string representation will raise an AttributeError if these attributes are not defined on the instance.

        :return: Returns a string describing the middle of the maxima defuzzification calculation for the specific feature and instance.

        :rtype: str
        """

        return f"Middle of the maxima defuzzification of feature {self.f_name} for instance {self.a} = "
