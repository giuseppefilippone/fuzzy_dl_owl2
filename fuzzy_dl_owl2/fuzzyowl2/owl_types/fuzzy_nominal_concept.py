from fuzzy_dl_owl2.fuzzyowl2.owl_types.concept_definition import ConceptDefinition
from fuzzy_dl_owl2.fuzzyowl2.util.constants import ConceptType


class FuzzyNominalConcept(ConceptDefinition):
    """
    This class models a specific type of fuzzy concept within the FuzzyOWL2 framework, representing the assertion that a named individual belongs to a concept with a defined degree of membership. To use this entity, instantiate it with a floating-point value indicating the truth value or membership degree and a string representing the identifier of the individual. The object provides methods to retrieve both the degree of membership and the individual's name, allowing for the precise representation of fuzzy assertions about specific entities in an ontology.

    :param _n: The degree of membership of the individual in the fuzzy nominal concept.
    :type _n: float
    :param _i: The name or identifier of the individual entity.
    :type _i: str
    """


    def __init__(self, n: float, i: str) -> None:
        """
        Initializes a new instance representing a fuzzy nominal concept, setting up the necessary internal state and type classification. The constructor accepts a floating-point value and a string identifier, storing them as private attributes to represent the concept's numerical and categorical components respectively. It also invokes the superclass initialization to explicitly register the object's type as FUZZY_NOMINAL within the broader concept system.

        :param n: The floating-point value representing the numeric component of the concept.
        :type n: float
        :param i: The identifier or label associated with the concept.
        :type i: str
        """

        super().__init__(ConceptType.FUZZY_NOMINAL)
        self._n: float = n
        self._i: str = i

    def get_degree(self) -> float:
        """
        Retrieves the numeric degree value representing the membership or truth level of this fuzzy nominal concept. This accessor returns the internal state variable `_n` as a floating-point number. The method performs no computation and has no side effects, simply providing direct read access to the concept's current degree.

        :return: The degree value.

        :rtype: float
        """

        return self._n

    def get_individual(self) -> str:
        """
        Returns the individual identifier associated with this fuzzy nominal concept. This method provides access to the internal `_i` attribute, which stores the string representation of the individual. It is a side-effect-free operation that simply retrieves the stored value without altering the object's state.

        :return: The individual string associated with this instance.

        :rtype: str
        """

        return self._i

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the fuzzy nominal concept, formatted as a parenthesized pair containing the degree and the individual. This method retrieves the degree and individual values by calling the `get_degree` and `get_individual` methods, respectively, and formats them into a string suitable for display or logging. It does not modify the internal state of the object, though any exceptions raised by the getter methods will propagate through this call.

        :return: A string representation of the object, formatted as "(degree individual)".

        :rtype: str
        """

        return f"({self.get_degree()} {self.get_individual()})"
