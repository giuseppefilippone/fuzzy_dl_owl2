from __future__ import annotations

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.individual.individual import Individual
from fuzzy_dl_owl2.fuzzydl.milp.expression import Expression
from fuzzy_dl_owl2.fuzzydl.milp.term import Term
from fuzzy_dl_owl2.fuzzydl.milp.variable import Variable
from fuzzy_dl_owl2.fuzzydl.query.defuzzify.defuzzify_query import DefuzzifyQuery


class SomDefuzzifyQuery(DefuzzifyQuery):
    """This class implements the Smallest of Maxima (SOM) defuzzification strategy, a method used to convert fuzzy logic values into crisp, numerical outputs. It operates by identifying the domain values that correspond to the highest degree of membership for a specific individual within a given concept and selecting the smallest among those maxima. The query is constructed using a target concept, an individual instance, and a feature name, which define the scope of the fuzzy evaluation. As a subclass of `DefuzzifyQuery`, it provides a specific implementation for resolving feature values based on the SOM algorithm within a larger fuzzy logic framework."""


    def __init__(self, c: Concept, ind: Individual, f_name: str) -> None:
        """
        Initializes a new instance of the SomDefuzzifyQuery class, designed to represent a query involving defuzzification logic, likely within a Self-Organizing Map context. The constructor accepts a Concept object, an Individual object, and a string representing a feature name, delegating the core initialization logic to the parent class by passing these arguments directly to the superclass constructor. This setup ensures that the query is properly configured with the necessary entities and identifiers, relying on the parent class to handle the storage and any immediate side effects associated with these parameters.

        :param c: The concept associated with the instance.
        :type c: Concept
        :param ind: The individual entity or instance that this object represents.
        :type ind: Individual
        :param f_name: The name of the file.
        :type f_name: str
        """

        super().__init__(c, ind, f_name)

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the defuzzification query, specifically formatted to describe a "Smallest of the maxima" operation. The string dynamically includes the feature name and instance identifier stored in the object, providing context for the specific calculation being represented. This method is primarily used for logging or display purposes, outputting a descriptive label that concludes with an equals sign.

        :return: A string representation describing the smallest of the maxima defuzzification for the specific feature and instance.

        :rtype: str
        """

        return f"Smallest of the maxima defuzzification of feature {self.f_name} for instance {self.a} = "

    def get_obj_expression(self, q: Variable) -> Expression:
        """
        Constructs a linear expression representing the provided variable with a coefficient of 1.0. The method encapsulates the variable within a Term object assigned a unit weight and wraps it in an Expression structure, effectively creating a mathematical representation of the variable itself. This function is stateless and produces no side effects on the instance or the input variable, though it assumes the input is a valid Variable object to prevent errors during Term instantiation.

        :param q: The variable used to construct the objective expression.
        :type q: Variable

        :return: An Expression object representing the variable `q` with a coefficient of 1.0.

        :rtype: Expression
        """

        return Expression(Term(1.0, q))
