from __future__ import annotations

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.individual.created_individual import CreatedIndividual
from fuzzy_dl_owl2.fuzzydl.individual.individual import Individual
from fuzzy_dl_owl2.fuzzydl.knowledge_base import KnowledgeBase
from fuzzy_dl_owl2.fuzzydl.milp.solution import Solution
from fuzzy_dl_owl2.fuzzydl.query.min.min_instance_query import MinInstanceQuery
from fuzzy_dl_owl2.fuzzydl.query.query import Query
from fuzzy_dl_owl2.fuzzydl.util.util import Util


class AllInstancesQuery(Query):
    def __init__(self, concept: Concept) -> None:
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

        for i in self.individuals:
            if isinstance(i, CreatedIndividual):
                continue
            q: MinInstanceQuery = MinInstanceQuery(self.conc, i)
            sol: Solution = q.solve(kb)
            if sol.is_consistent_kb():
                self.degrees.append(float(sol.get_solution()))
                self.name += f"{q}{sol.get_solution()}"
                continue
            self.name = f"Instances of {self.conc}? Inconsistent KB"
            break
        return sol

    def get_individuals(self) -> list[Individual]:
        return self.individuals

    def get_degrees(self) -> list[float]:
        return self.degrees

    def __str__(self) -> str:
        return self.name
