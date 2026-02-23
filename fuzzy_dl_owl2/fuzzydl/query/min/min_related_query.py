from __future__ import annotations

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.concept.has_value_concept import HasValueConcept
from fuzzy_dl_owl2.fuzzydl.degree.degree_expression import DegreeExpression
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


class MinRelatedQuery(RelatedQuery):
    """
    Represents a query that retrieves the minimum degree to which two individuals are related through a specific role within a knowledge base. To use this class, instantiate it with the two individuals and the role name, then invoke the solve method with a KnowledgeBase instance. Internally, the query clones the knowledge base to avoid side effects, constructs a corresponding concept expression, and utilizes mixed-integer linear programming to optimize and determine the minimum membership degree of the role assertion. The result is encapsulated in a Solution object, which accounts for potential inconsistencies in the ontology.

    :param ind1: The first individual involved in the role assertion, representing the subject of the relationship.
    :type ind1: Individual
    :param ind2: The target individual in the role assertion, corresponding to 'b' in the query (min-related? a b R).
    :type ind2: Individual
    :param role: The name of the role or relationship type connecting the two individuals.
    :type role: str
    """


    def __init__(self, a: Individual, b: Individual, role_name: str) -> None:
        """
        Initializes a new instance of the `MinRelatedQuery` class, designed to encapsulate a query regarding the relationship between two specific individuals. The constructor accepts two `Individual` objects and a string representing the role name, assigning them to the instance attributes `ind1`, `ind2`, and `role` respectively. This method performs no validation or side effects beyond storing the provided references for use in subsequent operations.

        :param a: The first individual involved in the relationship.
        :type a: Individual
        :param b: The second Individual participating in the relationship.
        :type b: Individual
        :param role_name: The label or title defining the specific role or relationship type between the two individuals.
        :type role_name: str
        """

        self.ind1: Individual = a
        self.ind2: Individual = b
        self.role: str = role_name

    def preprocess(self, kb: KnowledgeBase) -> None:
        """
        Prepares the query for execution by constructing a `HasValueConcept` based on the query's role and secondary individual, and integrating it into the provided `KnowledgeBase`. It retrieves a MILP variable representing the degree of membership of the primary individual in this concept and sets the query's objective expression to target this variable. The method adds assertions to the knowledge base to link the individual to both the concept and its negation, enforcing a constraint where the degree of the negation is derived from the degree of the concept. As a side effect, it increments the knowledge base's counter for legacy variables and enables dynamic blocking if the concept involves existential restrictions. Finally, it triggers the solving of all added assertions to update the solver's state.

        :param kb: The knowledge base instance containing the MILP model, used to retrieve variables, add assertions, and trigger solving.
        :type kb: KnowledgeBase
        """

        conc: Concept = HasValueConcept(self.role, self.ind2)
        q: Variable = kb.milp.get_variable(self.ind1, conc)
        kb.add_assertion(self.ind1, conc, DegreeVariable.get_degree(q))
        kb.old_01_variables += 1
        self.obj_expr: Expression = Expression(Term(1.0, q))

        if "(some " in str(conc) or "(b-some " in str(conc):
            kb.set_dynamic_blocking()

        # a: not c >= 1-q
        kb.add_assertion(
            self.ind1,
            -conc,
            DegreeExpression.get_degree(Expression(1.0, Term(-1.0, q))),
        )
        kb.solve_assertions()

    def solve(self, kb: KnowledgeBase) -> Solution:
        """
        Executes the optimization process for the query using the provided Knowledge Base. The method initiates timing, modifies the input Knowledge Base by incrementing its binary variable counter, and resolves the ABox. A clone of the Knowledge Base is then preprocessed and optimized according to the query's objective expression to generate a solution. If the ontology is found to be inconsistent during this process, the method catches the exception and returns a solution indicating inconsistency rather than raising an error.

        :param kb: The knowledge base containing the ontology and constraints to be solved and optimized.
        :type kb: KnowledgeBase

        :return: The Solution object resulting from the optimization of the knowledge base, or a specific status indicating the ontology is inconsistent.

        :rtype: Solution
        """

        try:
            self.set_initial_time()
            kb.old_binary_variables += 1
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
        Returns a human-readable string representation of the query object. The output is formatted as a question asking whether the first individual is related to the second individual through a specific role, followed by a ' >= ' operator. This method is primarily used for debugging or displaying the current state of the query parameters.

        :return: A string representation of the object, formatted as a question asking if `ind1` is related to `ind2` through `role`.

        :rtype: str
        """

        return f"Is {self.ind1} related to {self.ind2} through {self.role} ? >= "
