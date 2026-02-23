import typing

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.degree.degree import Degree
from fuzzy_dl_owl2.fuzzydl.degree.degree_numeric import DegreeNumeric


class Label:
    """
    Represents a weighted fuzzy concept used to annotate individuals, pairing a specific concept with a degree of satisfaction. To use this class, instantiate it with a `Concept` object and a `Degree` value between 0 and 1, where the degree indicates the extent to which the concept applies. The class provides logic for comparing instances, ensuring that two objects are equal only if their concepts are identical and their weights share the same type and numerical value.

    :param concept: The fuzzy concept instance defining the label's semantic category.
    :type concept: Concept
    :param weight: The degree to which the associated concept is satisfied for the individual, represented as a value between 0 and 1.
    :type weight: Degree
    """


    def __init__(self, concept: Concept, weight: Degree) -> None:
        """
        Initializes a new Label instance by associating a specific Concept with a quantitative weight. The weight parameter, representing the degree or strength of the label, is expected to be a value between 0 and 1. This method assigns the provided concept and weight to the instance's attributes, establishing the object's initial state without performing validation on the input range.

        :param concept: The underlying concept or entity represented by the instance.
        :type concept: Concept
        :param weight: The degree of the concept, normalized to the range [0, 1].
        :type weight: Degree
        """

        self.concept: Concept = concept
        # Weight in [0,1]
        self.weight: Degree = weight

    @staticmethod
    def weights_equal(w1: Degree, w2: Degree) -> bool:
        """
        Determines whether two `Degree` instances represent equivalent weights by first verifying that they are instances of the exact same class. If the classes differ, the method returns False immediately. For instances of the same class, non-numeric degrees are considered equal, while numeric degrees are compared based on their specific numerical values. This method performs a strict type check and does not modify the input objects.

        :param w1: The first Degree instance to compare.
        :type w1: Degree
        :param w2: The second degree to compare against the first argument.
        :type w2: Degree

        :return: True if the two Degree objects are of the same class and have equal numerical values (if numeric), otherwise False.

        :rtype: bool
        """

        if not w1.__class__ == w2.__class__:
            return False
        return (
            not w1.is_numeric()
            or typing.cast(DegreeNumeric, w1).get_numerical_value()
            == typing.cast(DegreeNumeric, w2).get_numerical_value()
        )

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the label instance by concatenating the `concept` and `weight` attributes with a single space. This method is implicitly invoked by the built-in `str()` function and print operations to provide a concise summary of the object's state. It has no side effects and relies on the string conversion of the underlying attributes, meaning that non-string values for `concept` or `weight` will be implicitly formatted as strings.

        :return: A human-readable string representation of the object, formatted as 'concept weight'.

        :rtype: str
        """

        return f"{self.concept} {self.weight}"

    def __eq__(self, cw: typing.Self) -> bool:
        """
        Determines if the current `Label` instance is equal to another instance by comparing their internal state. The method first performs a strict equality check on the `concept` attribute; if the concepts differ, it immediately returns `False`. If the concepts match, the method relies on the `weights_equal` helper function to evaluate the equality of the `weight` attributes, returning the result of that comparison. This operation does not modify the state of either object.

        :param cw: The other instance to compare for equality.
        :type cw: typing.Self

        :return: True if the concepts and weights of the two instances are equal, False otherwise.

        :rtype: bool
        """

        if self.concept != cw.concept:
            return False
        return self.weights_equal(self.weight, cw.weight)

    def __ne__(self, cw: typing.Self) -> bool:
        """
        Implements the inequality comparison for the `Label` object, determining whether the current instance differs from the specified `Label` instance (`cw`). It returns `True` if the two instances are not equal and `False` otherwise, effectively inverting the result of the equality check. This method has no side effects and relies entirely on the logic defined in the `__eq__` method to determine equality.

        :param cw: The object to compare against for inequality.
        :type cw: typing.Self

        :return: True if the current instance is not equal to the specified object, False otherwise.

        :rtype: bool
        """

        return not (self == cw)
