from fuzzy_dl_owl2.fuzzyowl2.owl_types.concept_definition import ConceptDefinition
from fuzzy_dl_owl2.fuzzyowl2.util.constants import ConceptType


class SugenoConcept(ConceptDefinition):
    """
    This class models a Sugeno fuzzy integral concept within the FuzzyOWL2 framework, acting as a specialized definition that aggregates multiple fuzzy concepts based on a corresponding set of weights. It extends the base `ConceptDefinition` and requires initialization with two parallel lists: a sequence of floating-point values representing the weights and a sequence of strings identifying the specific fuzzy concepts to be combined. Once instantiated, the object provides methods to retrieve the weights and concepts, and it defines a string representation that formats the data into a standard Sugeno operator expression for serialization or display.

    :param _weights: Coefficients representing the relative importance or contribution of the corresponding fuzzy concepts in the Sugeno model.
    :type _weights: list[float]
    :param _concepts: The fuzzy concepts that are aggregated within the Sugeno concept.
    :type _concepts: list[str]
    """


    def __init__(self, weights: list[float], concepts: list[str]) -> None:
        """
        Initializes a SugenoConcept instance by assigning the provided weights and concepts to internal attributes. The method accepts a list of floating-point values representing weights and a list of strings representing the associated concepts. Additionally, it invokes the superclass constructor to explicitly set the concept type to SUGENO, ensuring proper classification within the broader system.

        :param weights: Numerical values representing the importance or density associated with the corresponding concepts.
        :type weights: list[float]
        :param concepts: A list of string labels or identifiers representing the concepts associated with the provided weights.
        :type concepts: list[str]
        """

        super().__init__(ConceptType.SUGENO)
        self._weights: list[float] = weights
        self._concepts: list[str] = concepts

    def get_weights(self) -> list[float]:
        """
        Retrieves the list of weights associated with the Sugeno concept, which represent the importance values used in fuzzy integration calculations. This method returns a direct reference to the internal list of floating-point numbers, meaning modifications to the returned list will alter the object's internal state.

        :return: A list of floating-point numbers representing the weights.

        :rtype: list[float]
        """

        return self._weights

    def get_concepts(self) -> list[str]:
        """
        Retrieves the list of linguistic concepts or labels associated with this instance. This method provides direct access to the internal `_concepts` attribute, returning the list of strings that define the terms used in the Sugeno model. As the method returns a reference to the internal list, modifying the returned collection may inadvertently alter the state of the object.

        :return: A list of strings representing the concepts stored in the object.

        :rtype: list[str]
        """

        return self._concepts

    def __str__(self) -> str:
        """
        Returns a string representation of the object formatted as a parenthesized expression, resembling an S-expression. The output string begins with the 'sugeno' identifier, followed by a space-separated list of the internal weights converted to strings, and concludes with a space-separated list of the associated concepts. This representation is primarily intended for displaying the current state of the fuzzy measure and its components in a readable or parsable format.

        :return: A string representation of the object, formatted as a Sugeno expression containing the weights and concepts.

        :rtype: str
        """

        return (
            f"(sugeno ({' '.join(map(str, self._weights))}) ({' '.join(self._concepts)}))"
        )
