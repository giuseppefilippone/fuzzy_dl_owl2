import traceback

from fuzzy_dl_owl2.fuzzydl.knowledge_base import KnowledgeBase
from fuzzy_dl_owl2.fuzzydl.milp.solution import Solution
from fuzzy_dl_owl2.fuzzydl.query.query import Query
from fuzzy_dl_owl2.fuzzydl.util.util import Util


class ClassificationQuery(Query):

    def __init__(self) -> None:
        super().__init__()

    def preprocess(self, kb: KnowledgeBase) -> None:
        pass

    def solve(self, kb: KnowledgeBase) -> Solution:
        try:
            kb.classify()
            return Solution(1.0)
        except Exception as ex:
            Util.debug(traceback.format_exc())
            return Solution(Solution.INCONSISTENT_KB)

    def __str__(self) -> str:
        return "Classify? <= "
