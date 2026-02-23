import abc

from fuzzy_dl_owl2.fuzzyowl2.util.constants import ConceptType


class ConceptDefinition(abc.ABC):
    """
    This abstract base class serves as the foundational representation for concept definitions within the FuzzyOWL2 framework. It is designed to be subclassed rather than instantiated directly, providing a common interface for various types of fuzzy concept definitions. Upon initialization, a specific `ConceptType` must be provided to categorize the nature of the definition, which can subsequently be retrieved using the `get_type` method.

    :param _type: The specific classification or category of the fuzzy concept definition.
    :type _type: fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType
    """

    def __init__(self, type: ConceptType) -> None:
        """
        Initializes a new instance of the ConceptDefinition class, associating it with a specific concept type. The constructor requires a single argument, `type`, which is expected to be a valid instance of ConceptType. This value is directly assigned to the internal `_type` attribute, defining the fundamental nature of the concept definition for the lifetime of the object.

        :param type: Specifies the classification or category of the concept.
        :type type: fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType
        """

        self._type: ConceptType = type

    def get_type(self) -> ConceptType:
        """
        Returns the type classification associated with this concept definition. This method acts as an accessor for the internal `_type` attribute, providing the specific `ConceptType` that categorizes the concept. It does not modify the state of the object.

        :return: The type of the concept.

        :rtype: fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType
        """

        return self._type

    def __repr__(self) -> str:
        """
        Returns the official string representation of the `ConceptDefinition` instance. This method delegates directly to the `__str__` method, ensuring that the output used for debugging and logging is identical to the informal string representation provided by the object.

        :return: The string representation of the object.

        :rtype: str
        """

        return str(self)
