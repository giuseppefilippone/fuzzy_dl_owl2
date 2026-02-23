from __future__ import annotations

import typing

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.individual.individual import Individual
from fuzzy_dl_owl2.fuzzydl.milp.expression import Expression
from fuzzy_dl_owl2.fuzzydl.query.query import Query
from fuzzy_dl_owl2.fuzzydl.util.util import Util


class SatisfiableQuery(Query):
    """This abstract class serves as the foundational interface for min/max satisfiability queries within a fuzzy logic framework. It is designed to evaluate the degree to which a specific fuzzy concept is satisfied, optionally in the context of a particular individual. Upon initialization, the class requires a non-concrete concept and accepts an optional individual argument, storing these entities along with a placeholder for the resulting objective expression. By enforcing constraints on the input concept and providing a common structure for storing query parameters, it facilitates the implementation of specific satisfiability checks that determine the bounds or extent of concept fulfillment."""


    @typing.overload
    def __init__(self, c: Concept, a: Individual) -> None: ...

    @typing.overload
    def __init__(self, c: Concept) -> None: ...

    def __init__(self, *args) -> None:
        """
        Initializes a new instance of a satisfiability query, accepting either one or two arguments to define the query parameters. The first argument is mandatory and must be an instance of `Concept`. If a second argument is provided, it must be an instance of `Individual` or `None`. The method validates the input types and argument count, raising an `AssertionError` for invalid configurations, before delegating to internal initialization routines and invoking the superclass constructor.

        :param args: Variable length argument list containing either a single `Concept` or a `Concept` followed by an `Individual` (or `None`).
        :type args: typing.Any
        """

        super().__init__()
        assert len(args) in [1, 2]
        assert isinstance(args[0], Concept)
        if len(args) == 1:
            self.__satisfiable_query_init_2(*args)
        else:
            assert args[1] is None or isinstance(args[1], Individual)
            self.__satisfiable_query_init_1(*args)

    def __satisfiable_query_init_1(self, c: Concept, a: Individual) -> None:
        """
        Initializes a satisfiability query designed to evaluate whether a specific individual satisfies a given fuzzy concept. This method assigns the provided concept and individual to the instance attributes `self.conc` and `self.ind`, respectively, while setting the objective expression to None. It performs a validation step to ensure the concept is not concrete, raising an error if the input violates this constraint. This setup prepares the query object for subsequent satisfiability testing operations involving the specified individual.

        :param c: The fuzzy concept to be tested for satisfiability. Must not be a concrete concept.
        :type c: Concept
        :param a: The individual entity used during the satisfiability test.
        :type a: Individual
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
        Initializes the query object to test the general satisfiability of a given fuzzy concept. This method serves as an alternative constructor that delegates to the primary initialization routine, passing `None` as the secondary argument to indicate that the check is not bound to a specific individual or context. By invoking the main initialization logic with these parameters, it configures the internal state necessary to determine if the concept is logically consistent within the current knowledge base.

        :param c: The fuzzy concept to be checked for satisfiability.
        :type c: Concept
        """

        self.__init__(c, None)
