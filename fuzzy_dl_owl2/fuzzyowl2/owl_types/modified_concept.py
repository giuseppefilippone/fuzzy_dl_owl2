from fuzzy_dl_owl2.fuzzyowl2.owl_types.concept_definition import ConceptDefinition
from fuzzy_dl_owl2.fuzzyowl2.util.constants import ConceptType


class ModifiedConcept(ConceptDefinition):
    """
    This entity encapsulates a concept within the FuzzyOWL2 framework that has been altered by a specific fuzzy modifier, such as a linguistic hedge. It acts as a specialized definition that combines a base concept name with a modifier to represent nuanced or graded logical expressions. To use this class, instantiate it by providing the modifier string and the concept string as arguments. Once created, the object allows retrieval of the modifier and the underlying concept through dedicated accessor methods, and it provides a string representation formatted as `(modifier concept)`.

    :param _mod: The fuzzy modifier (linguistic hedge) applied to the concept.
    :type _mod: str
    :param _c: The name of the concept to which the fuzzy modifier is applied.
    :type _c: str
    """


    def __init__(self, mod: str, c: str) -> None:
        """
        Initializes a new instance representing a modified concept by accepting a modifier and a base concept as strings. This method stores these values in private attributes `_mod` and `_c` respectively, and invokes the parent class constructor to establish the entity's type as `MODIFIED_CONCEPT`.

        :param mod: The string representing the modification or modifier applied to the concept.
        :type mod: str
        :param c: 
        :type c: str
        """

        super().__init__(ConceptType.MODIFIED_CONCEPT)
        self._mod: str = mod
        self._c: str = c

    def get_fuzzy_modifier(self) -> str:
        """
        Retrieves the fuzzy modifier string associated with the current concept instance. This value represents the specific nuance or qualification applied to the concept, distinguishing it from a standard definition. The method performs a direct lookup of the internal attribute and does not modify the state of the object.

        :return: The string representing the fuzzy modifier.

        :rtype: str
        """

        return self._mod

    def get_fuzzy_concept(self) -> str:
        """
        Retrieves the underlying string representation of the fuzzy concept stored within the instance. This method acts as a getter for the internal attribute `_c`, providing direct access to the core data without altering the object's state. It is the primary mechanism for obtaining the textual value associated with the modified concept.

        :return: The fuzzy concept associated with the object.

        :rtype: str
        """

        return self._c

    def __str__(self) -> str:
        """
        Generates a human-readable string representation of the instance, formatted as a parenthesized pair containing the modifier and the underlying concept separated by a space. This method is implicitly called by the `str()` built-in and print functions, relying on the internal `_mod` and `_c` attributes to be convertible to strings. The operation is read-only and does not alter the state of the object.

        :return: A string representation of the object formatted as "(_mod _c)".

        :rtype: str
        """

        return f"({self._mod} {self._c})"
