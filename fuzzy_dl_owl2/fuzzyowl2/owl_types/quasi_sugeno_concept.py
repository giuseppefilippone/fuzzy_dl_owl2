from fuzzy_dl_owl2.fuzzyowl2.owl_types.concept_definition import ConceptDefinition
from fuzzy_dl_owl2.fuzzyowl2.util.constants import ConceptType


class QsugenoConcept(ConceptDefinition):
    """
    Represents a specific type of fuzzy logic operator known as a quasi-Sugeno integral within the FuzzyOWL2 ontology framework. It extends the base concept definition to encapsulate a weighted aggregation of multiple fuzzy concepts, requiring a list of numerical weights and a corresponding list of concept identifiers upon initialization. The structure provides access to these components via getter methods and formats the data into a specific parenthetical string representation for serialization or logical processing.

    :param _weights: The coefficients weighting the fuzzy concepts in the quasi-Sugeno aggregation.
    :type _weights: list[float]
    :param _concepts: The fuzzy concepts that are aggregated within this quasi-Sugeno concept.
    :type _concepts: list[str]
    """


    def __init__(self, weights: list[float], concepts: list[str]) -> None:
        """
        Initializes a Quasi-Sugeno concept instance by registering the specific concept type with the parent class and storing the provided aggregation parameters. This method assigns the list of floating-point weights and the list of concept identifiers to internal attributes, which are likely used for subsequent fuzzy logic operations. While the constructor does not perform explicit validation on the input lists in the provided snippet, it establishes the core state of the object by invoking the superclass initialization with the QUASI_SUGENO type.

        :param weights: A list of numerical values representing the importance or influence associated with each concept.
        :type weights: list[float]
        :param concepts: A list of labels or names identifying the criteria or attributes corresponding to the provided weights.
        :type concepts: list[str]
        """

        super().__init__(ConceptType.QUASI_SUGENO)
        self._weights: list[float] = weights
        self._concepts: list[str] = concepts

    def get_weights(self) -> list[float]:
        """
        Retrieves the list of weights associated with the Sugeno concept. This method acts as a getter for the internal `_weights` attribute, returning the floating-point values that define the importance or density of the criteria. The operation is read-only and does not alter the state of the object.

        :return: A list of floating-point numbers representing the weights.

        :rtype: list[float]
        """

        return self._weights

    def get_concepts(self) -> list[str]:
        """
        Returns the list of concepts stored in the `QsugenoConcept` instance. This method provides direct access to the internal `_concepts` attribute, which contains the collection of string-based concepts. As the method returns a reference to the underlying list rather than a copy, any modifications made to the returned list will directly alter the object's internal state.

        :return: A list of strings representing the concepts associated with this instance.

        :rtype: list[str]
        """

        return self._concepts

    def __str__(self) -> str:
        """
        Returns a formatted string representation of the Q-sugeno concept, structured as a parenthetical expression. The output string begins with the 'q-sugeno' identifier, followed by a space-separated sequence of the internal weights converted to strings. It concludes with a space-separated list of the underlying concepts. This method is primarily intended for generating a human-readable or serialized view of the object's state without modifying the underlying data.

        :return: A string representation of the object in the format '(q-sugeno (weights...) (concepts...))'.

        :rtype: str
        """

        return f"(q-sugeno ({' '.join(map(str, self._weights))}) ({' '.join(self._concepts)}))"
