from __future__ import annotations

from fuzzy_dl_owl2.fuzzydl.individual.individual import Individual
from fuzzy_dl_owl2.fuzzydl.milp.expression import Expression
from fuzzy_dl_owl2.fuzzydl.query.query import Query


class RelatedQuery(Query):
    """
    This abstract class serves as a foundational interface for queries that evaluate the entailment of role assertions, specifically focusing on the relationships between individuals. It is designed to support operations that determine minimum or maximum degrees of membership, acting as a shared structure for more specific query implementations. The class encapsulates the parameters necessary for these evaluations, including the specific role being examined, the subject and object individuals involved in the relation, and an expression representing the desired degree of membership. By defining these attributes, it provides a standardized way to construct and process queries regarding the strength or validity of connections within a logical framework.

    :param role: The role or relation type for which related individuals are retrieved.
    :type role: str
    :param ind1: The individual acting as the subject of the relation.
    :type ind1: Individual
    :param ind2: The individual acting as the object of the role assertion relation.
    :type ind2: Individual
    :param obj_expr: The objective expression representing the degree of membership of the relation.
    :type obj_expr: Expression
    """


    def __init__(self) -> None:
        """Initializes a new instance of the RelatedQuery class by invoking the superclass constructor and setting up the internal state for a relationship query. This method prepares the object to store the components of a relation by initializing the `role` attribute for the abstract role, `ind1` and `ind2` for the subject and object individuals, and `obj_expr` for an objective expression. All of these attributes are initially set to None, requiring them to be populated explicitly to define a specific query."""

        super().__init__()
        # Abstract role
        self.role: str = None
        # Subject of the relation.
        self.ind1: Individual = None
        # Object of the relation.
        self.ind2: Individual = None
        # Objective expression
        self.obj_expr: Expression = None
