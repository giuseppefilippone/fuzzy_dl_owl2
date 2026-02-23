from __future__ import annotations

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.concept.has_value_concept import HasValueConcept
from fuzzy_dl_owl2.fuzzydl.degree.degree_variable import DegreeVariable
from fuzzy_dl_owl2.fuzzydl.exception.inconsistent_ontology_exception import (
    InconsistentOntologyException,
)
from fuzzy_dl_owl2.fuzzydl.individual.individual import Individual
from fuzzy_dl_owl2.fuzzydl.knowledge_base import KnowledgeBase
from fuzzy_dl_owl2.fuzzydl.milp.expression import Expression
from fuzzy_dl_owl2.fuzzydl.milp.solution import Solution
from fuzzy_dl_owl2.fuzzydl.milp.term import Term
from fuzzy_dl_owl2.fuzzydl.milp.variable import Variable
from fuzzy_dl_owl2.fuzzydl.query.related_query import RelatedQuery


class MaxRelatedQuery(RelatedQuery):
    """
    This class models a query designed to determine the maximum degree of truth for a specific relationship between two individuals within a fuzzy knowledge base. It operates by formulating an optimization problem where the goal is to maximize the membership degree of the assertion that the first individual is related to the second individual via a specified role. To use this class, instantiate it with the two individuals involved and the name of the role, then invoke the solve method with a knowledge base instance to retrieve the optimal solution. The implementation handles potential ontology inconsistencies gracefully by returning a specific solution state.

    :param ind1: The first individual in the role assertion, representing the subject of the relationship.
    :type ind1: Individual
    :param ind2: The second individual in the role assertion, representing the target of the relationship.
    :type ind2: Individual
    :param role: The name of the role through which the two individuals are related.
    :type role: str
    """


    def __init__(self, a: Individual, b: Individual, role_name: str) -> None:
        """
        Initializes a new instance of the query object by storing the provided entities and relationship context. The method accepts two `Individual` objects and a string representing the role name, assigning them to the instance attributes `ind1`, `ind2`, and `role` respectively. This constructor performs no validation or side effects other than populating the object's internal state with the given arguments.

        :param a: The first individual involved in the relationship.
        :type a: Individual
        :param b: The second Individual instance involved in the relationship.
        :type b: Individual
        :param role_name: The name or label defining the role associated with the relationship between the two individuals.
        :type role_name: str
        """

        self.ind1: Individual = a
        self.ind2: Individual = b
        self.role: str = role_name

    def preprocess(self, kb: KnowledgeBase) -> None:
        # glb(ind1 : b-some R ind2)
        """
        Prepares the query for execution by translating a specific relationship constraint into a Mixed-Integer Linear Programming (MILP) formulation within the provided Knowledge Base. It constructs a `HasValueConcept` representing the restriction that an individual must have a specific value for a given role, retrieves the corresponding MILP variable, and asserts this relationship with a degree derived from that variable. As a side effect, this method increments the knowledge base's counter for legacy variables, initializes the instance's objective expression to optimize the relationship's degree, and triggers the solving of all current assertions to update the system state.

        :param kb: The knowledge base context used to access the MILP model, add assertions, update variable counters, and trigger the solver.
        :type kb: KnowledgeBase
        """

        conc: Concept = HasValueConcept(self.role, self.ind2)
        q: Variable = kb.milp.get_variable(self.ind1, conc)
        kb.add_assertion(self.ind1, conc, DegreeVariable.get_degree(q))
        kb.old_01_variables += 1
        self.obj_expr: Expression = Expression(Term(-1.0, q))
        kb.solve_assertions()

    def solve(self, kb: KnowledgeBase) -> Solution:
        """
        Executes the optimization query by first resolving the ABox of the provided Knowledge Base to ensure consistency. Upon successful resolution, the method clones the Knowledge Base to preserve the original state, applies necessary preprocessing, and runs an optimization routine using the defined objective expression. The process includes tracking the total execution time. If the Knowledge Base is determined to be inconsistent during the initial resolution step, the method intercepts the exception and returns a Solution object specifically marked as inconsistent.

        :param kb: The knowledge base containing the ontology and data to be solved and optimized.
        :type kb: KnowledgeBase

        :return: The Solution object resulting from the optimization process, or a specific solution state indicating the knowledge base is inconsistent.

        :rtype: Solution
        """

        try:
            self.set_initial_time()
            kb.solve_abox()
            cloned: KnowledgeBase = kb.clone()
            self.preprocess(cloned)
            sol: Solution = cloned.optimize(self.obj_expr)
            self.set_total_time()
            return sol
        except InconsistentOntologyException:
            return Solution(Solution.INCONSISTENT_KB)

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the query object, formatted as a question regarding the relationship between two individuals. The method constructs the string by interpolating the first individual, the second individual, and the relationship role into a template that asks if the first is related to the second through the specified role. The output string concludes with a prompt indicator ('<= ') and relies on the standard string conversion of the object's attributes, ensuring that the method does not modify the object's state.

        :return: A string representation of the relationship query, formatted as a question asking if the first individual is related to the second through the specified role.

        :rtype: str
        """

        return f"Is {self.ind1} related to {self.ind2} through {self.role} ? <= "
