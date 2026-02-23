from fuzzy_dl_owl2.fuzzyowl2.owl_types.concept_definition import ConceptDefinition
from fuzzy_dl_owl2.fuzzyowl2.util.constants import ConceptType


class QowaConcept(ConceptDefinition):
    """
    This class encapsulates the definition of a Quantified Ordered Weighted Averaging (OWA) concept as defined in the FuzzyOWL2 ontology language. It serves as a specialized implementation of `ConceptDefinition`, designed to model fuzzy logic operations where a set of concepts is aggregated based on a linguistic quantifier. Users can instantiate this class by supplying a string representing the quantifier and a list of strings corresponding to the underlying fuzzy concepts, allowing for the representation of complex, weighted aggregations within the system.

    :param _q: The quantifier defining the aggregation weights for the OWA concept.
    :type _q: str
    :param _concepts: The list of fuzzy concepts that are aggregated by the quantified OWA operator.
    :type _concepts: list[str]
    """


    def __init__(self, q: str, concepts: list[str]) -> None:
        """
        Initializes a new instance of a Quantified OWA concept, configuring it with a specific quantifier and a collection of related concepts. This method invokes the superclass constructor to establish the entity's type as QUANTIFIED_OWA before storing the provided quantifier string and list of concept strings into private instance attributes. While no input validation is performed on the arguments, the operation ensures the object is fully initialized and ready for use within the broader logic framework.

        :param q: The quantifier string representing the linguistic term or expression defining the aggregation degree.
        :type q: str
        :param concepts: A list of concept identifiers or names involved in the quantified OWA.
        :type concepts: list[str]
        """

        super().__init__(ConceptType.QUANTIFIED_OWA)
        self._q: str = q
        self._concepts: list[str] = concepts

    def get_quantifier(self) -> str:
        """
        Retrieves the quantifier associated with the current concept instance. This method returns the value of the internal `_q` attribute, representing the specific quantification logic or scope defined for the object. It is a read-only operation that exposes the stored string value without modifying the instance's state.

        :return: The quantifier string.

        :rtype: str
        """

        return self._q

    def get_concepts(self) -> list[str]:
        """
        Retrieves the list of concepts currently stored within the instance. This method provides direct access to the internal `_concepts` attribute, returning a list of strings. Since the reference to the internal list is returned rather than a copy, any modifications made to the returned list will directly alter the state of the object.

        :return: A list of strings representing the concepts associated with the object.

        :rtype: list[str]
        """

        return self._concepts

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the QowaConcept instance, formatted as a parenthetical expression beginning with the 'q-owa' identifier. The representation concatenates the string value of the internal quantifier `_q` and the sequence of concepts, which are joined by spaces. This method has no side effects and is intended for displaying the object's current state or for serialization into a specific logical syntax.

        :return: A string representation of the object in the format "(q-owa <q> <concepts>)".

        :rtype: str
        """

        return f"(q-owa {self._q} {' '.join(self._concepts)})"
