import abc
import typing

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.concept.interface.has_concepts_interface import (
    HasConceptsInterface,
)


class HasWeightedConceptsInterface(HasConceptsInterface, abc.ABC):
    """
    This abstract base class defines a contract for objects that manage a collection of concepts alongside associated numerical weights, extending the functionality of the basic concept interface. It provides properties to retrieve and update the list of weights, ensuring that these values are stored as mutable lists of floats or explicitly set to null to indicate the absence of weighting. By handling the initialization and modification of these weights, the class enables dynamic representation of concepts where each element carries a specific magnitude or significance.

    :param _weights: Internal list of weights associated with the current concepts, or None if no weights are assigned.
    :type _weights: typing.Optional[list[float]]
    """

    def __init__(
        self,
        weights: typing.Optional[typing.Iterable[float]],
        concepts: typing.Iterable[Concept],
    ) -> None:
        """
        Initializes the instance with a collection of concepts and an optional iterable of weights. The concepts are passed to the parent class constructor for initialization. If weights are provided, they are converted to a list and stored internally; otherwise, the internal weight attribute is set to None.

        :param weights: Optional iterable of numerical weights. If provided, the values are stored as a list; otherwise, the weights are set to None.
        :type weights: typing.Optional[typing.Iterable[float]]
        :param concepts: An iterable of Concept objects used to initialize the instance.
        :type concepts: typing.Iterable[Concept]
        """

        super().__init__(concepts)

        self._weights: typing.Optional[list[float]] = (
            list(weights) if weights is not None else None
        )

    @property
    def weights(self) -> typing.Optional[list[float]]:
        """
        Returns the per-concept weights applied in the weighted aggregation, or ``None`` when no weights are set. The value is read from the private ``_weights`` attribute without modifying the instance.

        :return: The list of weights, or ``None`` if unset.

        :rtype: typing.Optional[list[float]]
        """

        return self._weights

    @weights.setter
    def weights(self, value: typing.Optional[typing.Iterable[float]]) -> None:
        """
        Sets the per-concept weights of the weighted aggregation, replacing any existing values. A provided iterable is materialized into a list and stored in the private ``_weights`` attribute; passing ``None`` clears the weights.

        :param value: The new weights, or ``None`` to clear them.
        :type value: typing.Optional[typing.Iterable[float]]
        """

        self._weights = list(value) if value is not None else None
