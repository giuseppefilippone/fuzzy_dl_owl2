from fuzzy_dl_owl2.fuzzyowl2.owl_types.concept_definition import ConceptDefinition
from fuzzy_dl_owl2.fuzzyowl2.util.constants import ConceptType


class OwaConcept(ConceptDefinition):
    """
    This class models an Ordered Weighted Averaging (OWA) operation within the FuzzyOWL2 framework, serving as a specialized definition for fuzzy logic concepts. It encapsulates the parameters necessary to perform the aggregation, specifically a sequence of floating-point weights and a list of associated fuzzy concept identifiers. By inheriting from the base definition type, it integrates into the broader ontology structure while providing specific accessors to retrieve the weights and concepts, as well as a string representation formatted for the specific syntax of the system.

    :param _weights: Coefficients used to calculate the ordered weighted average of the fuzzy concepts.
    :type _weights: list[float]
    :param _concepts: The fuzzy concepts to be aggregated by the OWA operator.
    :type _concepts: list[str]
    """


    def __init__(self, weights: list[float], concepts: list[str]) -> None:
        """
        Initializes a new instance representing an Ordered Weighted Averaging (OWA) concept by accepting a list of numerical weights and a list of concept identifiers. The method invokes the superclass constructor to register the entity type as OWA and stores the provided arguments directly as internal attributes. Note that this implementation assigns the lists by reference rather than creating copies, meaning subsequent modifications to the original input lists will affect the object's state, and it does not enforce constraints such as the weights summing to one.

        :param weights: A list of numerical coefficients representing the weighting vector for the OWA operator.
        :type weights: list[float]
        :param concepts: A list of strings representing the concepts or labels associated with the weights.
        :type concepts: list[str]
        """

        super().__init__(ConceptType.OWA)
        self._weights: list[float] = weights
        self._concepts: list[str] = concepts

    def get_weights(self) -> list[float]:
        """
        Retrieves the list of floating-point weights used by the OWA operator to calculate the aggregated value. This method returns a direct reference to the internal `_weights` attribute, meaning that any modifications made to the returned list will alter the state of the object itself. It is typically used to inspect or externally manipulate the weighting criteria without invoking specific setter logic.

        :return: A list of float values representing the weights.

        :rtype: list[float]
        """

        return self._weights

    def get_concepts(self) -> list[str]:
        """
        Retrieves the list of concepts associated with the OwaConcept instance. This method returns the value of the internal `_concepts` attribute, which is a list of strings. It serves as a simple accessor to expose the stored concept data without altering the object's state.

        :return: A list of strings representing the concepts associated with this object.

        :rtype: list[str]
        """

        return self._concepts

    def __str__(self) -> str:
        """
        Returns a string representation of the OWA concept formatted as a parenthesized expression. The output follows the structure "(owa (weights) (concepts))", where the internal weights are converted to strings and joined by spaces, and the concept labels are similarly concatenated. This representation is intended to provide a human-readable summary of the aggregation operator's configuration and associated terms.

        :return: A string representation of the object in the format `(owa (weights) (concepts))`.

        :rtype: str
        """

        return (
            f"(owa ({' '.join(map(str, self._weights))}) ({' '.join(self._concepts)}))"
        )
