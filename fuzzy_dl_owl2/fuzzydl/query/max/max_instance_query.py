from __future__ import annotations

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
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
from fuzzy_dl_owl2.fuzzydl.query.instance_query import InstanceQuery


class MaxInstanceQuery(InstanceQuery):
    """This class implements a reasoning query designed to calculate the maximum degree of membership for a specific individual within a given concept. It functions by constructing an optimization problem that maximizes the variable associated with the individual's membership, effectively retrieving the highest truth value supported by the knowledge base. To ensure the integrity of the original state, the query operates on a cloned version of the knowledge base, where it preprocesses the problem by adding necessary assertions and enabling dynamic blocking strategies for complex logical constructs like universal quantification. The execution involves solving the ABox and optimizing the objective expression, returning a solution that reflects the maximum membership degree or indicates an inconsistent ontology if the constraints cannot be satisfied."""


    def __init__(self, concept: Concept, individual: Individual) -> None:
        """
        Initializes a query object to determine if a specific individual is the maximum instance of a given concept. The constructor requires a Concept object, representing the class or description to be checked, and an Individual object, representing the entity being tested. It delegates the storage of these parameters to the parent class's initialization method, ensuring the query state is correctly established.

        :param concept: The concept representing the class or category to which the individual belongs.
        :type concept: Concept
        :param individual: The specific individual instance or entity to be associated with the object.
        :type individual: Individual
        """

        super().__init__(concept, individual)

    def preprocess(self, kb: KnowledgeBase) -> None:
        """
        Prepares the knowledge base for a maximum instance query by initializing the necessary MILP variables and constraints. It retrieves the variable associated with the specific individual and concept, increments the counter for legacy binary variables, and constructs an objective expression to maximize the retrieved variable. If the concept expression involves universal restrictions or negated existential restrictions, the method enables dynamic blocking on the knowledge base to handle these specific logic constructs. Finally, it adds an assertion linking the individual, concept, and variable degree to the knowledge base and triggers the solver to process these assertions.

        :param kb: The KnowledgeBase instance managing the MILP context, variable storage, and assertion solving. It is updated with new constraints and internal counters during the preprocessing step.
        :type kb: KnowledgeBase
        """

        q: Variable = kb.milp.get_variable(self.ind, self.conc)
        kb.old_01_variables += 1
        self.obj_expr: Expression = Expression(Term(-1.0, q))

        if "(all " in str(self.conc) or "(not (b-some " in str(self.conc):
            kb.set_dynamic_blocking()

        # a: c >= q
        kb.add_assertion(self.ind, self.conc, DegreeVariable.get_degree(q))
        kb.solve_assertions()

    def solve(self, kb: KnowledgeBase) -> Solution:
        """
        Executes the solving workflow for the maximum instance query, starting a timer and invoking the ABox solver on the provided KnowledgeBase, potentially modifying it in place. The method then creates a clone of the KnowledgeBase to perform preprocessing and optimization based on the instance's objective expression, ensuring the optimization logic does not further alter the original input. After calculating the total execution time, the resulting Solution is returned. If the ontology is determined to be inconsistent during the ABox solving phase, the method handles the exception by returning a Solution indicating an inconsistent KnowledgeBase.

        :param kb: The knowledge base containing the ontology and constraints to be solved and optimized.
        :type kb: KnowledgeBase

        :return: The Solution object resulting from the optimization of the preprocessed knowledge base, or a solution indicating an inconsistent ontology.

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
        Returns a formatted string representation of the query, posing the question of whether the individual `self.ind` is an instance of the concept `self.conc`. The string is constructed using an f-string and concludes with the suffix "? <=", adhering to a specific syntax likely used for display or serialization within the module. This operation is read-only and does not alter the state of the object.

        :return: Returns a string representation of the object, formatted as a question asking if `self.ind` is an instance of `self.conc`.

        :rtype: str
        """

        return f"Is {self.ind} instance of {self.conc} ? <= "
