from fuzzy_dl_owl2.fuzzyowl2.owl_types.concept_definition import ConceptDefinition
from fuzzy_dl_owl2.fuzzyowl2.util.constants import ConceptType


class WeightedSumZeroConcept(ConceptDefinition):

    """
    This class models a specific fuzzy logic constraint within the FuzzyOWL2 framework, representing a concept defined by a weighted sum that equates to zero. It serves as a specialized container that aggregates a collection of other concept definitions, which act as the components or operands involved in the calculation. To utilize this class, instantiate it with a list of `ConceptDefinition` objects representing the terms to be weighted. Once created, the object functions as a standard concept definition within the ontology, allowing the internal list of weighted concepts to be retrieved via the `get_weighted_concepts` method.

    :param _wc: Collection of concept definitions that constitute the operands of the weighted sum zero expression.
    :type _wc: list[ConceptDefinition]
    """


    def __init__(self, wc: list[ConceptDefinition]) -> None:
        """
        Initializes a `WeightedSumZeroConcept` instance by registering its specific type and storing the provided component definitions. This constructor accepts a list of `ConceptDefinition` objects that define the terms involved in the weighted sum calculation. It invokes the superclass initialization to set the concept type to `WEIGHTED_SUM_ZERO` and assigns the list to a private attribute for internal reference.

        :param wc: List of weighted concept definitions.
        :type wc: list[ConceptDefinition]
        """

        super().__init__(ConceptType.WEIGHTED_SUM_ZERO)
        self._wc: list[ConceptDefinition] = wc

    def get_weighted_concepts(self) -> list[ConceptDefinition]:
        """
        Returns the list of concept definitions associated with this weighted sum zero concept. This method provides access to the internal collection of concepts that are used to form the weighted sum. Note that the returned list is a direct reference to the internal state, so modifying it may alter the object's behavior.

        :return: A list of ConceptDefinition objects representing the weighted concepts.

        :rtype: list[ConceptDefinition]
        """

        return self._wc

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the weighted sum zero concept. The output is formatted as a parenthesized expression starting with the identifier 'w-sum-zero', followed by the string representations of the internal weights or coefficients. This method relies on the string conversion of the elements within the internal collection and does not alter the object's state.

        :return: A string representation of the object, formatted as "(w-sum-zero ...)" containing the internal weights joined by spaces.

        :rtype: str
        """

        return f"(w-sum-zero {' '.join(map(str, self._wc))})"
