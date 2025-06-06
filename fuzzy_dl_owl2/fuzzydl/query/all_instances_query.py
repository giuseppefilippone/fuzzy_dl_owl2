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
    Min instance query for every individual of a knowledge base.
    """

    def __init__(self, concept: Concept) -> None:
        super().__init__()
        if concept.is_concrete():
            Util.error(f"Error: {concept} cannot be a concrete concept.")
        self.conc = concept
        self.degrees: list[float] = []
        self.individuals: list[Individual] = []
        self.name = f"Instances of {self.conc}?"

    def preprocess(self, kb: KnowledgeBase) -> None:
        pass

    def solve(self, kb: KnowledgeBase) -> Solution:
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
        Specific algorithm to solve the instance retrieval.
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
        return self.individuals

    def get_degrees(self) -> list[float]:
        return self.degrees

    def __str__(self) -> str:
        return self.name
