from __future__ import annotations

import typing

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.individual.individual import Individual
from fuzzy_dl_owl2.fuzzydl.milp.expression import Expression
from fuzzy_dl_owl2.fuzzydl.query.query import Query
from fuzzy_dl_owl2.fuzzydl.util.util import Util


class SatisfiableQuery(Query):

    @typing.overload
    def __init__(self, c: Concept, a: Individual) -> None: ...

    @typing.overload
    def __init__(self, c: Concept) -> None: ...

    def __init__(self, *args) -> None:
        assert len(args) in [1, 2]
        assert isinstance(args[0], Concept)
        if len(args) == 1:
            self.__satisfiable_query_init_2(*args)
        else:
            assert args[1] is None or isinstance(args[1], Individual)
            self.__satisfiable_query_init_1(*args)

    def __satisfiable_query_init_1(self, c: Concept, a: Individual) -> None:
        if c.is_concrete():
            Util.error(f"Error: {c} cannot be a concrete concept.")
        self.conc: Concept = c
        self.ind: Individual = a
        self.obj_expr: Expression = None

    def __satisfiable_query_init_2(self, c: Concept) -> None:
        self.__init__(c, None)
