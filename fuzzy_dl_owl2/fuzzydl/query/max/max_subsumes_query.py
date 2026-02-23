from __future__ import annotations

import typing

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.concept.implies_concept import ImpliesConcept
from fuzzy_dl_owl2.fuzzydl.concept.operator_concept import OperatorConcept
from fuzzy_dl_owl2.fuzzydl.degree.degree_variable import DegreeVariable
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
from fuzzy_dl_owl2.fuzzydl.query.subsumption_query import SubsumptionQuery
from fuzzy_dl_owl2.fuzzydl.util.config_reader import ConfigReader
from fuzzy_dl_owl2.fuzzydl.util.constants import LogicOperatorType


class MaxSubsumesQuery(SubsumptionQuery):
    """Represents a query to determine the maximum degree to which one fuzzy concept is subsumed by another within a knowledge base. It supports various fuzzy logic operators, including Łukasiewicz, Gödel, Kleene-Dienes, and Zadeh, to define the semantics of the subsumption relationship. The query is resolved by transforming the subsumption check into an optimization problem, specifically minimizing the degree of an implication assertion derived from the input concepts. This process involves cloning the knowledge base, preprocessing the concepts into a solvable form, and optimizing an objective expression to retrieve the solution."""


    def __init__(self, c1: Concept, c2: Concept, type_: LogicOperatorType) -> None:
        """
        Initializes a new instance of the MaxSubsumesQuery, configuring it with two specific concepts and a logical operator type. This method accepts `c1` and `c2` as the concepts to be compared or processed, and `type_` to specify the logic operator governing the query. The initialization logic is delegated to the superclass, ensuring that the base attributes are set up according to the parent class's implementation.

        :param c1: The first concept operand for the logic operation.
        :type c1: Concept
        :param c2: The second Concept operand involved in the logic operation.
        :type c2: Concept
        :param type_: The specific logic operator type to apply between the concepts.
        :type type_: LogicOperatorType
        """

        super().__init__(c1, c2, type_)

    def preprocess(self, kb: KnowledgeBase) -> None:
        """
        Prepares the query for execution by constructing a logical implication concept within the provided Knowledge Base. It creates a new individual and determines the specific implication structure based on the configured logic operator type (Lukasiewicz, Goedel, Kleene-Dienes, or Zadeh). The method retrieves the corresponding MILP variable for this individual and concept, sets the query's objective expression to minimize this variable, and adds an assertion linking them. As a side effect, it increments the Knowledge Base's counter for legacy binary variables and triggers the immediate solving of current assertions.

        :param kb: The KnowledgeBase instance on which to perform preprocessing operations. It is used to generate new individuals, access MILP variables, add assertions, and trigger the solving process.
        :type kb: KnowledgeBase
        """

        ind: CreatedIndividual = kb.get_new_individual()
        if self.type == LogicOperatorType.LUKASIEWICZ:
            conc: Concept = OperatorConcept.lukasiewicz_or(-self.c2, self.c1)
        elif self.type == LogicOperatorType.GOEDEL:
            conc: Concept = ImpliesConcept.goedel_implies(self.c2, self.c1)
        elif self.type == LogicOperatorType.KLEENE_DIENES:
            conc: Concept = ImpliesConcept.zadeh_implies(self.c2, self.c1)
        else:  # LogicOperatorType.ZADEH
            conc: Concept = OperatorConcept.goedel_or(-self.c2, self.c1)

        q: Variable = kb.milp.get_variable(typing.cast(Individual, ind), conc)
        kb.old_01_variables += 1
        self.obj_expr = Expression(Term(-1.0, q))

        kb.add_assertion(ind, conc, DegreeVariable.get_degree(q))
        kb.solve_assertions()

    def solve(self, kb: KnowledgeBase) -> Solution:
        """
        Executes the optimization query on the provided knowledge base to generate a solution. The method begins by initializing performance timers and conditionally cloning the knowledge base; if optimizations are disabled or nominals are present in the TBox, the ABox is solved within the clone, otherwise, the clone is created without the ABox. Following preprocessing, the method invokes the optimization routine on the cloned instance using the internal objective expression. If the ontology is found to be inconsistent during this process, the method catches the exception and returns a solution object indicating inconsistency. The original knowledge base remains unmodified, while internal timing metrics are updated.

        :param kb: The knowledge base containing the ontology to be solved or optimized.
        :type kb: KnowledgeBase

        :return: The Solution object resulting from optimizing the knowledge base, or a solution indicating inconsistency if the ontology is invalid.

        :rtype: Solution
        """

        try:
            self.set_initial_time()
            if ConfigReader.OPTIMIZATIONS == 0 or kb.has_nominals_in_tbox():
                cloned: KnowledgeBase = kb.clone()
                cloned.solve_abox()
            else:
                cloned: KnowledgeBase = kb.clone_without_abox()

            self.preprocess(cloned)
            sol: Solution = cloned.optimize(self.obj_expr)
            self.set_total_time()
            return sol
        except InconsistentOntologyException:
            return Solution(Solution.INCONSISTENT_KB)

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the subsumption query, formatted as a question asking whether the first concept subsumes the second. The representation interpolates the two concepts stored in the instance into a specific syntax that includes the phrase "subsumes" and the suffix "? <= ". This method is primarily intended for logging, debugging, or displaying the query to the user, and it does not modify the state of the object.

        :return: A string representing the subsumption query between `self.c1` and `self.c2`.

        :rtype: str
        """

        return f"{self.c1} subsumes {self.c2} ? <= "
