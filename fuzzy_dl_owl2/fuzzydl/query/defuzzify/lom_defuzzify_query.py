from __future__ import annotations

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.individual.individual import Individual
from fuzzy_dl_owl2.fuzzydl.milp.expression import Expression
from fuzzy_dl_owl2.fuzzydl.milp.term import Term
from fuzzy_dl_owl2.fuzzydl.milp.variable import Variable
from fuzzy_dl_owl2.fuzzydl.query.defuzzify.defuzzify_query import DefuzzifyQuery


class LomDefuzzifyQuery(DefuzzifyQuery):
    """Represents a query that performs defuzzification using the Largest of Maxima (LOM) method to convert a fuzzy membership value into a crisp number. This approach is specifically designed to select the highest numerical value within the plateau where the degree of membership is maximized for a given feature. To use this class, instantiate it with a `Concept` providing the context, an `Individual` representing the entity being analyzed, and a string specifying the `feature_name` to be defuzzified. It functions within a broader fuzzy logic framework by generating objective expressions that facilitate the calculation of the desired crisp value."""


    def __init__(self, c: Concept, ind: Individual, feature_name: str) -> None:
        """
        Initializes a new instance of the LOM defuzzification query, configuring it to evaluate a specific feature of an individual against a given concept. The constructor accepts a Concept object representing the fuzzy definition, an Individual object representing the target entity, and a string specifying the name of the feature to be defuzzified. By calling the superclass initializer, this method ensures that the query state is established according to the inherited logic, potentially triggering any validation or setup routines defined in the parent class.

        :param c: The Concept object that this instance is associated with.
        :type c: Concept
        :param ind: The specific individual entity or instance to which the feature applies.
        :type ind: Individual
        :param feature_name: The name of the feature associated with the concept and individual.
        :type feature_name: str
        """

        super().__init__(c, ind, feature_name)

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the defuzzification query, formatted to describe the specific operation being performed. The output identifies the method as "Largest of the maxima defuzzification" and incorporates the name of the feature and the instance identifier stored within the object. The resulting string is constructed as a prefix ending with an equals sign, suitable for logging or displaying the query context before the final result.

        :return: A string describing the largest of the maxima defuzzification for the specific feature and instance.

        :rtype: str
        """

        return f"Largest of the maxima defuzzification of feature {self.f_name} for instance {self.a} = "

    def get_obj_expression(self, variable: Variable) -> Expression:
        """
        Constructs an objective expression representing the negative of the specified variable by creating a Term with a coefficient of -1.0 associated with that variable and wrapping it within an Expression object. This is typically utilized within optimization contexts to formulate a minimization objective for the given variable. The method is stateless and does not modify the input variable or the instance's internal state.

        :param variable: The variable for which to generate the objective expression.
        :type variable: Variable

        :return: An Expression representing the negative of the specified variable.

        :rtype: Expression
        """

        return Expression(Term(-1.0, variable))
