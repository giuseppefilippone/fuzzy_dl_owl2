from fuzzy_dl_owl2.fuzzyowl2.owl_types.concept_definition import ConceptDefinition
from fuzzy_dl_owl2.fuzzyowl2.util.constants import ConceptType


class WeightedSumConcept(ConceptDefinition):
    """
    This class represents a weighted sum concept within the FuzzyOWL2 framework, serving as a specialized definition that aggregates multiple underlying concepts. It is utilized to construct complex fuzzy concepts by combining a list of existing `ConceptDefinition` objects, which act as the components of the summation. Upon instantiation, the class initializes itself with the specific concept type `WEIGHTED_SUM` and stores the provided list of concepts, allowing them to be retrieved later via the `get_weighted_concepts` method for further processing or serialization.

    :param _wc: Collection of concept definitions that comprise the weighted sum.
    :type _wc: list[ConceptDefinition]
    """


    def __init__(self, wc: list[ConceptDefinition]) -> None:
        """
        Initializes a new instance representing a concept defined as a weighted sum of other concepts. The constructor accepts a list of `ConceptDefinition` objects that serve as the components for the calculation. It invokes the superclass initialization to set the concept type to `WEIGHTED_SUM` and assigns the provided list to an internal attribute. Note that the list is stored by reference, meaning subsequent modifications to the original list will affect the instance's state.

        :param wc: A list of concept definitions representing the components to be included in the weighted sum.
        :type wc: list[ConceptDefinition]
        """

        super().__init__(ConceptType.WEIGHTED_SUM)
        self._wc: list[ConceptDefinition] = wc

    def get_weighted_concepts(self) -> list[ConceptDefinition]:
        """
        Retrieves the list of concept definitions that are used to calculate the weighted sum for this instance. The method returns the internal list of concepts directly, providing access to the underlying data structure. Because a reference to the internal list is returned, any modifications made to the list or its elements will be reflected in the state of the object.

        :return: A list of weighted concept definitions.

        :rtype: list[ConceptDefinition]
        """

        return self._wc

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the concept, formatted as a parenthesized expression prefixed with 'w-sum'. The internal components are converted to strings and joined by spaces within the parentheses. This method does not modify the object's state and handles empty component lists by returning the prefix with an empty body.

        :return: A string representation of the object, formatted as '(w-sum ...)' containing the space-separated elements of the internal collection.

        :rtype: str
        """

        return f"(w-sum {' '.join(map(str, self._wc))})"
