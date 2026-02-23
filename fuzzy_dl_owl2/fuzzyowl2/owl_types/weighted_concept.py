from fuzzy_dl_owl2.fuzzyowl2.owl_types.concept_definition import ConceptDefinition
from fuzzy_dl_owl2.fuzzyowl2.util.constants import ConceptType


class WeightedConcept(ConceptDefinition):
    """
    This class models a weighted concept as defined in the FuzzyOWL2 ontology language, serving as a concrete implementation of `ConceptDefinition`. It encapsulates a relationship between a numerical weight and a named fuzzy concept, allowing for the representation of degrees of membership or importance associated with that concept. To utilize this class, instantiate it with a float for the weight and a string for the concept name; the stored values can then be accessed via the `get_number` and `get_fuzzy_concept` methods. The class also provides a string representation that displays the weight and concept name in a parenthesized format.

    :param _n: The numerical weight associated with the fuzzy concept.
    :type _n: float
    :param _c: The name or identifier of the fuzzy concept associated with the weight.
    :type _c: str
    """


    def __init__(self, n: float, c: str) -> None:
        """
        Initializes a weighted concept entity by associating a numerical value with a string identifier. This constructor accepts a float, representing a weight or magnitude, and a string, representing the concept's content or label. Upon instantiation, it invokes the superclass initializer to explicitly register the object as a WEIGHTED_CONCEPT type within the broader system hierarchy. The provided arguments are encapsulated as private attributes, ensuring that the numerical and textual data are stored securely within the instance.

        :param n: The numerical weight of the concept.
        :type n: float
        :param c: The string value representing the concept's identifier or code.
        :type c: str
        """

        super().__init__(ConceptType.WEIGHTED_CONCEPT)
        self._n: float = n
        self._c: str = c

    def get_number(self) -> float:
        """
        Returns the underlying numeric value of the weighted concept by accessing the internal `_n` attribute. The value is returned as a float, representing the current weight or count associated with the instance. This is a read-only operation that does not modify the object's state or any external data.

        :return: The numeric value stored in the instance.

        :rtype: float
        """

        return self._n

    def get_fuzzy_concept(self) -> str:
        """
        Retrieves the string representation of the fuzzy concept associated with this instance. This method acts as a simple accessor for the internal attribute `_c`, returning the specific concept label or identifier without modifying the object's state. As this is a read-only operation, it has no side effects and simply exposes the value stored during the object's initialization.

        :return: The fuzzy concept associated with the instance.

        :rtype: str
        """

        return self._c

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the weighted concept, formatted as a parenthesized pair containing the numeric weight and the concept identifier. This method is automatically invoked by the built-in `str()` function and print operations, ensuring the object is displayed clearly as "(weight concept)" without modifying the object's internal state.

        :return: A string representation of the object in the format '(_n _c)'.

        :rtype: str
        """

        return f"({self._n} {self._c})"
