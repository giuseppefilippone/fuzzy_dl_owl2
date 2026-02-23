from __future__ import annotations

from abc import ABC

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.individual.individual import Individual
from fuzzy_dl_owl2.fuzzydl.milp.expression import Expression
from fuzzy_dl_owl2.fuzzydl.query.query import Query
from fuzzy_dl_owl2.fuzzydl.util.util import Util


class InstanceQuery(Query, ABC):
    """
    This abstract base class defines a framework for querying specific instances of a concept relative to a particular individual, typically used to identify instances with minimum or maximum membership degrees. Upon initialization, it accepts a concept and an individual, validating that the concept is abstract and raising an error if a concrete concept is provided. It maintains an expression attribute to represent the degree of membership, which is intended to be populated by subclasses to facilitate the specific query logic.

    :param conc: The concept for which to retrieve the instance.
    :type conc: Concept
    :param ind: The individual for which to retrieve the instance.
    :type ind: Individual
    :param obj_expr: Expression representing the degree of membership of the individual to the concept.
    :type obj_expr: Expression
    """


    def __init__(self, concept: Concept, individual: Individual) -> None:
        """
        Initializes a query object designed to check if a specific individual is an instance of a given concept. The constructor performs a validation check to ensure the provided concept is not concrete; if the concept is determined to be concrete, an error is raised. Upon successful validation, the concept and individual are stored as instance attributes, and the object expression attribute is initialized to None.

        :param concept: The abstract concept to associate with the individual. Must not be a concrete concept.
        :type concept: Concept
        :param individual: The individual instance to be associated with the concept.
        :type individual: Individual
        """

        super().__init__()
        if concept.is_concrete():
            Util.error(f"Error: {concept} cannot be a concrete concept.")

        self.conc: Concept = concept
        self.ind: Individual = individual
        self.obj_expr: Expression = None
