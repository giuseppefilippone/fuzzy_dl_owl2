from __future__ import annotations

import time
from abc import ABC, abstractmethod

from fuzzy_dl_owl2.fuzzydl.knowledge_base import KnowledgeBase
from fuzzy_dl_owl2.fuzzydl.milp.solution import Solution


class Query(ABC):
    def __init__(self) -> None:
        self.initial_time: int = 0
        self.total_time: int = 0

    def set_initial_time(self) -> None:
        self.initial_time = time.perf_counter_ns()

    def set_total_time(self) -> None:
        end_time: int = time.perf_counter_ns()
        self.total_time = end_time - self.initial_time

    def get_total_time(self) -> float:
        return self.total_time / 1e9

    @abstractmethod
    def preprocess(self, knowledge_base: KnowledgeBase) -> None:
        """Preprocess the query with given knowledge base"""
        pass

    @abstractmethod
    def solve(self, knowledge_base: KnowledgeBase) -> Solution:
        """Solve the query using given knowledge base"""
        pass

    @abstractmethod
    def __str__(self) -> str:
        """String representation of the query"""
        pass
