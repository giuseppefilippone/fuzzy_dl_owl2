import typing

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.individual.individual import Individual
from fuzzy_dl_owl2.fuzzydl.milp.variable import Variable


class SigmaCount:
    """
    This class represents a sigma-count concept within fuzzy description logic, serving as a structural representation for evaluating constraints based on the quantity of role fillers. It defines a condition where a target individual is considered satisfied if the number of related entities—connected via a specific role and conforming to a particular concept—falls within a fuzzy set determined by a collection of reference individuals. To use this class, instantiate it with a variable for the count, the target individual, the list of reference individuals, the role name, and the concept to be evaluated. The object provides methods to access these internal components and a cloning utility to create deep copies of the instance.

    :param variable: The variable associated with the sigma-count concept, used for counting the number of role fillers that satisfy the concept C.
    :type variable: Variable
    :param individual: The individual for which the sigma-count concept is being evaluated.
    :type individual: Individual
    :param individuals: The set of individuals $\{a_1, a_2, \dots, a_n\}$ considered in the fuzzy concrete concept $D$ for the sigma-count evaluation.
    :type individuals: list[Individual]
    :param role: The relationship identifier 'r' used in the sigma-count expression to connect the individual to the fillers being counted.
    :type role: str
    :param concept: The concept C that role fillers must satisfy to be included in the sigma-count.
    :type concept: Concept
    """


    def __init__(
        self,
        var: Variable,
        ind: Individual,
        inds: list[Individual],
        role: str,
        concept: Concept,
    ) -> None:
        """
        Initializes a new instance of the SigmaCount class, capturing the necessary components for a counting operation within a logical context. The constructor accepts a variable, a primary individual, a list of individuals, a role identifier, and a concept object, assigning each to its respective instance attribute. This setup stores the provided data directly without performing validation, allowing the object to maintain the specific state required for subsequent processing or calculations involving these entities.

        :param var: The variable entity to be associated with this instance.
        :type var: Variable
        :param ind: The specific individual object associated with the instance, distinct from the list of individuals.
        :type ind: Individual
        :param inds: A list of Individual objects to be associated with the instance.
        :type inds: list[Individual]
        :param role: The semantic role or relationship type defining the individual's function within the context.
        :type role: str
        :param concept: The concept to be associated with the instance.
        :type concept: Concept
        """

        self.variable: Variable = var
        self.individual: Individual = ind
        self.individuals: list[Individual] = inds
        self.role: str = role
        self.concept: Concept = concept

    def clone(self) -> typing.Self:
        """
        Creates and returns a deep copy of the current `SigmaCount` instance. The method recursively clones the `variable`, `individual`, and `concept` attributes, and generates a new list containing clones of all elements within the `individuals` collection. The `role` attribute is passed by reference rather than being cloned. This operation has no side effects on the original object, ensuring that the returned instance is independent with respect to its deep-copied components.

        :return: A new instance of `SigmaCount` that is a deep copy of the current object.

        :rtype: typing.Self
        """

        return SigmaCount(
            self.variable.clone(),
            self.individual.clone(),
            [i.clone() for i in self.individuals],
            self.role,
            self.concept.clone(),
        )

    def get_variable(self) -> Variable:
        """
        Retrieves the `Variable` instance associated with this `SigmaCount` object. This method acts as a simple accessor, returning the reference to the internal variable attribute without modifying the state of the object. It allows external code to inspect which variable is being tracked or aggregated by the counter.

        :return: The `Variable` instance stored in the `variable` attribute.

        :rtype: Variable
        """

        return self.variable

    def get_individual(self) -> Individual:
        """
        Retrieves the `Individual` entity associated with the current `SigmaCount` instance. This accessor method returns the reference to the stored object without causing any side effects or modifying the internal state.

        :return: The Individual instance associated with this object.

        :rtype: Individual
        """

        return self.individual

    def get_individuals(self) -> list[Individual]:
        """
        Retrieves the collection of `Individual` objects managed by the `SigmaCount` instance. Since this method returns a direct reference to the internal list, any in-place modifications to the returned list will alter the state of the object.

        :return: A list of the individuals associated with this instance.

        :rtype: list[Individual]
        """

        return self.individuals

    def get_role(self) -> str:
        """
        Retrieves the string value assigned to the `role` attribute of the current instance. This accessor method provides read-only access to the specific role or category associated with the `SigmaCount` object without modifying its internal state. It assumes the attribute has been properly initialized; accessing this method on an instance where the attribute is missing will result in an `AttributeError`.

        :return: The role associated with the instance.

        :rtype: str
        """

        return self.role

    def get_concept(self) -> Concept:
        """
        Returns the `Concept` object associated with the current `SigmaCount` instance. This method acts as a simple accessor, retrieving the value of the `concept` attribute without modifying the object's internal state. If the attribute has not been set, this method will raise an `AttributeError`.

        :return: The Concept object associated with this instance.

        :rtype: Concept
        """

        return self.concept

    def __hash__(self) -> int:
        """
        Computes the hash value for the instance by hashing its string representation. This allows the object to be used as a dictionary key or stored in a set. The hash is derived directly from the output of the `__str__` method, ensuring that the hash value remains consistent as long as the string representation does not change.

        :return: An integer hash value calculated from the object's string representation.

        :rtype: int
        """

        return hash(str(self))

    def __repr__(self) -> str:
        """
        Returns the official string representation of the instance by delegating directly to the informal string conversion logic. This approach ensures that the output displayed in interactive sessions or logs is identical to the user-facing string format. The method performs no state modifications and depends entirely on the behavior of the `__str__` method to generate the resulting string.

        :return: The string representation of the object, identical to the output of `str()`.

        :rtype: str
        """

        return str(self)

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the SigmaCount instance formatted as a functional expression. The output string follows the pattern 'sigma-count(...)', incorporating the object's variable, individual, individuals, role, and concept attributes as comma-separated arguments. This method is intended for display purposes and does not modify the object's state.

        :return: A string representation of the object, formatted as a sigma-count function call containing the variable, individual, individuals, role, and concept attributes.

        :rtype: str
        """

        return f"sigma-count({self.variable}, {self.individual}, {self.individuals}, {self.role}, {self.concept})"
