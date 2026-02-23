from __future__ import annotations

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.degree.degree import Degree


class AtomicAssertion:
    """
    This class models a fundamental logical constraint within a fuzzy logic framework, specifically asserting that a specific atomic concept must meet or exceed a defined threshold of membership. It encapsulates a relationship between a concept and a degree, representing the condition where the concept's membership is greater than or equal to the specified value. To utilize this class, instantiate it with a `Concept` object representing the subject and a `Degree` object representing the required lower bound. The object stores these components and provides methods to retrieve the concept's name and the specific degree value, as well as a string representation of the assertion.

    :param c: The atomic concept whose membership degree is evaluated against the assertion's lower bound.
    :type c: Concept
    :param degree: The lower bound degree threshold that the atomic concept's membership must meet or exceed for the assertion to be satisfied.
    :type degree: Degree
    """


    def __init__(self, c: Concept, degree: Degree) -> None:
        # Atomic concept
        """
        Initializes an instance representing an atomic assertion by associating a specific concept with a lower bound degree. This constructor stores the provided `Concept` and `Degree` objects as instance attributes, establishing the fundamental state of the assertion. The `degree` parameter serves as a constraint or minimum threshold, defining the extent to which the concept is asserted to hold true.

        :param c: The atomic concept to be stored.
        :type c: Concept
        :param degree: The lower bound degree associated with the concept.
        :type degree: Degree
        """

        self.c: Concept = c
        # Lower bound degree
        self.degree: Degree = degree

    def get_concept_name(self) -> str:
        """
        Retrieves the name of the concept associated with this atomic assertion by accessing the internal attribute `c` and converting it to a string. This method ensures that the concept identifier is returned as a string, regardless of the original type of the stored attribute. It is a read-only operation that does not modify the state of the object.

        :return: The concept name as a string.

        :rtype: str
        """

        return str(self.c)

    def get_degree(self) -> Degree:
        """
        Retrieves the degree value associated with this atomic assertion. This method acts as a simple accessor for the internal `degree` attribute, returning the stored instance of the `Degree` type. As it only reads an existing attribute, the operation has no side effects and does not alter the state of the object.

        :return: The degree associated with the object.

        :rtype: Degree
        """

        return self.degree

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the assertion, formatted with angle brackets that enclose the values of the 'c' and 'degree' attributes. This method is designed for display and logging purposes, providing a concise snapshot of the object's current state without causing any side effects.

        :return: A string representation of the object, displaying the values of `c` and `degree` enclosed in angle brackets.

        :rtype: str
        """

        return f"< {self.c} {self.degree} >"
