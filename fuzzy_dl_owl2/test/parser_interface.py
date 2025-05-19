from fuzzy_dl_owl2.fuzzydl.milp.solution import Solution
from fuzzy_dl_owl2.fuzzydl.milp.variable import Variable
from fuzzy_dl_owl2.fuzzydl.parser.dl_parser import DLParser
from fuzzy_dl_owl2.fuzzydl.query.all_instances_query import AllInstancesQuery
from fuzzy_dl_owl2.fuzzydl.util.util import Util


class ParserInterface:

    def __init__(self, filename: str) -> None:
        self.filename: str = filename

    def solve(self) -> float:
        Variable.VARIABLE_NUMBER = 0

        kb, queries = DLParser.get_kb(self.filename)
        kb.solve_kb()
        for query in queries:
            if (
                isinstance(query, AllInstancesQuery)
                and not kb.get_individuals().values()
            ):
                return -1.0
            else:
                result: Solution = query.solve(kb)
                if result.is_consistent_kb():
                    Util.info(f"{query}{result}")
                    return result.get_solution()
        return -1.0
