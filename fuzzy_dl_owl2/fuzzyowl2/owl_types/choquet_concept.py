from fuzzy_dl_owl2.fuzzyowl2.owl_types.concept_definition import ConceptDefinition
from fuzzy_dl_owl2.fuzzyowl2.util.constants import ConceptType


class ChoquetConcept(ConceptDefinition):

    """
    This entity models a fuzzy concept defined via the Choquet integral within the FuzzyOWL2 framework, serving as a specialized implementation of a concept definition. It encapsulates the logic for aggregating multiple underlying concepts using a specific set of weights that represent the importance of various subsets of those concepts. To utilize this structure, instantiate it with a list of floating-point values representing the fuzzy measure weights and a corresponding list of strings identifying the concepts to be aggregated. Once initialized, the object provides methods to retrieve the weights and concept identifiers, and it formats its internal state into a specific string syntax for serialization or display.

    :param _weights: Numerical values determining the contribution of the associated concepts in the Choquet integral.
    :type _weights: list[float]
    :param _concepts: The list of concept identifiers that are aggregated to form the Choquet concept.
    :type _concepts: list[str]
    """


    def __init__(self, weights: list[float], concepts: list[str]) -> None:
        """
        Initializes a ChoquetConcept instance by invoking the parent class constructor with the `ConceptType.CHOQUET` identifier to establish its type. The method assigns the provided list of floating-point weights and the list of string concept identifiers to private instance attributes, preserving them for internal logic. This constructor does not perform validation on the length or values of the input lists, leaving the integrity of the data to the caller.

        :param weights: List of numerical weights corresponding to the concepts.
        :type weights: list[float]
        :param concepts: A list of concept names or identifiers associated with the provided weights.
        :type concepts: list[str]
        """

        super().__init__(ConceptType.CHOQUET)
        self._weights: list[float] = weights
        self._concepts: list[str] = concepts

    def get_weights(self) -> list[float]:
        """
        Returns the list of floating-point weights currently stored within the Choquet concept instance. These weights typically represent the fuzzy measure or capacity values used for aggregation. The method provides direct access to the internal `_weights` attribute; therefore, modifying the returned list in-place will alter the internal state of the object.

        :return: A list of floating-point numbers representing the weights.

        :rtype: list[float]
        """

        return self._weights

    def get_concepts(self) -> list[str]:
        """
        Retrieves the list of concepts associated with the current instance. This method acts as a simple accessor, returning the internal `_concepts` attribute directly. Because it returns a reference to the underlying list rather than a copy, any modifications made to the returned list will affect the internal state of the object.

        :return: A list of strings representing the concepts associated with this object.

        :rtype: list[str]
        """

        return self._concepts

    def __str__(self) -> str:
        """
        Returns a formatted string representation of the instance, encapsulating the internal weights and concepts within a parenthesized syntax starting with the 'choquet' identifier. The weights are explicitly converted to strings and joined by spaces, while the concepts are joined directly, implying that the internal concept list must consist of string objects to avoid a TypeError. This method is intended for display or logging purposes and has no side effects on the object's state.

        :return: A string representation of the object formatted as (choquet weights concepts).

        :rtype: str
        """

        return f"(choquet ({' '.join(map(str, self._weights))}) ({' '.join(self._concepts)}))"
