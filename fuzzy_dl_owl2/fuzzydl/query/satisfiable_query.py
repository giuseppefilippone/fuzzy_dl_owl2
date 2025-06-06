from __future__ import annotations

import typing

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.individual.individual import Individual
from fuzzy_dl_owl2.fuzzydl.milp.expression import Expression
from fuzzy_dl_owl2.fuzzydl.query.query import Query
from fuzzy_dl_owl2.fuzzydl.util.util import Util


class SatisfiableQuery(Query):
    """Fuzzy concept satisfiability query."""

    @typing.overload
    def __init__(self, c: Concept, a: Individual) -> None: ...

    @typing.overload
    def __init__(self, c: Concept) -> None: ...

    def __init__(self, *args) -> None:
        super().__init__()
        assert len(args) in [1, 2]
        assert isinstance(args[0], Concept)
        if len(args) == 1:
            self.__satisfiable_query_init_2(*args)
        else:
            assert args[1] is None or isinstance(args[1], Individual)
            self.__satisfiable_query_init_1(*args)

    def __satisfiable_query_init_1(self, c: Concept, a: Individual) -> None:
        """Constructor for a satisfiability query involving a specific individual.

        Args:
            c (Concept): A fuzzy concept for which the satisfiability is to be tested.
            a (Individual): An individual used in the satisfiability test.
        """
        if c.is_concrete():
            Util.error(f"Error: {c} cannot be a concrete concept.")
        # Fuzzy concept
        self.conc: Concept = c
        # Optional individual used during the satisfiability test.
        self.ind: Individual = a
        # Objective expression
        self.obj_expr: Expression = None

    def __satisfiable_query_init_2(self, c: Concept) -> None:
        """
        Constructor for a general satisfiability query.

        Args:
            c (Concept): A fuzzy concept for which the satisfiability is to be tested.
        """
        self.__init__(c, None)
