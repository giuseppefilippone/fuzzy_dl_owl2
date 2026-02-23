from fuzzy_dl_owl2.fuzzyowl2.owl_types.concept_definition import ConceptDefinition
from fuzzy_dl_owl2.fuzzyowl2.util.constants import ConceptType


class WeightedMinConcept(ConceptDefinition):
    """
    This class models a weighted minimum aggregation operator within the FuzzyOWL2 framework, designed to construct complex fuzzy concepts by combining a collection of sub-concepts. To use it, instantiate the object with a list of `ConceptDefinition` instances that represent the components to be aggregated. The class provides access to these components through a getter method and generates a string representation that visually denotes the weighted minimum operation.

    :param _wc: Collection of concept definitions that constitute the operands of the weighted minimum operation.
    :type _wc: list[ConceptDefinition]
    """


    def __init__(self, wc: list[ConceptDefinition]) -> None:
        """
        Constructs a WeightedMinConcept instance by accepting a list of ConceptDefinition objects that define the components for the weighted minimum operation. The method stores this list internally and invokes the superclass initializer to set the concept type to WEIGHTED_MIN. No explicit validation is performed on the input list within this constructor, so the caller is responsible for ensuring the definitions are correctly formatted.

        :param wc: A list of concept definitions representing the weighted components.
        :type wc: list[ConceptDefinition]
        """

        super().__init__(ConceptType.WEIGHTED_MIN)
        self._wc: list[ConceptDefinition] = wc

    def get_weighted_concepts(self) -> list[ConceptDefinition]:
        """
        Retrieves the internal collection of concept definitions that have been weighted and processed by this instance. The method returns a list of `ConceptDefinition` objects representing the current state of the weighted concepts. Since this method returns a direct reference to the internal list, any modifications made to the list by the caller will immediately affect the internal state of the object.

        :return: A list of weighted concept definitions associated with the object.

        :rtype: list[ConceptDefinition]
        """

        return self._wc

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the weighted minimum concept, formatted as a parenthetical expression starting with the prefix "w-min". The method joins the string representations of the elements stored in the internal `_wc` attribute with spaces to form the content of the expression. This operation does not modify the object's state and depends on the string conversion behavior of the individual elements within the internal collection.

        :return: Returns a readable string representation of the object, formatted as "(w-min ...)" with the internal components space-separated.

        :rtype: str
        """

        return f"(w-min {' '.join(map(str, self._wc))})"
