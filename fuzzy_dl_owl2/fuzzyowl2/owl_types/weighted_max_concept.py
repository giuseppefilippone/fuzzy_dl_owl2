from fuzzy_dl_owl2.fuzzyowl2.owl_types.concept_definition import ConceptDefinition
from fuzzy_dl_owl2.fuzzyowl2.util.constants import ConceptType


class WeightedMaxConcept(ConceptDefinition):
    """
    This class models a specific fuzzy logic operator used within the FuzzyOWL2 ontology framework, designed to represent a weighted maximum aggregation over a set of concepts. It functions by accepting a list of `ConceptDefinition` objects during initialization, which serve as the operands for the aggregation logic. As a subclass of `ConceptDefinition`, it integrates seamlessly into the type system by registering itself as a `WEIGHTED_MAX` entity, allowing the system to distinguish it from other logical constructs. The stored concepts can be accessed via the `get_weighted_concepts` method, enabling further processing or evaluation of the fuzzy membership degrees associated with the weighted maximum operation.

    :param _wc: The list of concept definitions that are combined using the weighted maximum operator.
    :type _wc: list[ConceptDefinition]
    """


    def __init__(self, wc: list[ConceptDefinition]) -> None:
        """
        Initializes a new instance of the WeightedMaxConcept class, designed to represent a concept that calculates a weighted maximum. The constructor accepts a list of ConceptDefinition objects, which serve as the basis for the calculation, and stores them in a private instance variable. It also invokes the superclass initialization to explicitly set the concept type to WEIGHTED_MAX. This method does not perform validation on the input list, assuming it is correctly formatted prior to instantiation.

        :param wc: A list of concept definitions representing the weighted components.
        :type wc: list[ConceptDefinition]
        """

        super().__init__(ConceptType.WEIGHTED_MAX)
        self._wc: list[ConceptDefinition] = wc

    def get_weighted_concepts(self) -> list[ConceptDefinition]:
        """
        Returns the internal collection of weighted concepts stored within the instance. This method provides direct access to the list of `ConceptDefinition` objects, allowing the caller to inspect the current set of concepts. Because a reference to the internal list is returned rather than a copy, any modifications made to the list by the caller will directly affect the state of the object.

        :return: A list of ConceptDefinition objects representing the weighted concepts.

        :rtype: list[ConceptDefinition]
        """

        return self._wc

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the weighted maximum concept, formatted as a parenthesized list prefixed with 'w-max'. The internal components stored in the `_wc` attribute are converted to strings and joined by spaces to populate the content within the parentheses. This representation is useful for logging, debugging, or displaying the object's current state without modifying it.

        :return: A string representation of the object formatted as "(w-max ...)" with space-separated internal components.

        :rtype: str
        """

        return f"(w-max {' '.join(map(str, self._wc))})"
