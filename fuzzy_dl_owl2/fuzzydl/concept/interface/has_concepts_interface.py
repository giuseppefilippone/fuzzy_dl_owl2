import abc
import typing

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept


class HasConceptsInterface(abc.ABC):

    """
    This abstract base class serves as a foundational component for objects that manage a collection of concepts, providing a concrete implementation for storage and access. It initializes with an iterable of concepts and exposes a property that allows for both retrieval and dynamic modification of the underlying list. By handling the conversion of input iterables to a list, it ensures a consistent internal state for subclasses that need to track or represent multiple conceptual entities.

    :param _concepts: Internal storage for the concepts currently represented or manipulated by the class.
    :type _concepts: list[Concept]
    """


    def __init__(self, concepts: typing.Iterable[Concept]) -> None:
        """
        Initializes the instance with a collection of Concept objects, accepting any iterable of such items. The provided iterable is immediately converted into a list and assigned to the internal `_concepts` attribute, ensuring that the data is stored in a mutable sequence format. This operation consumes the input iterable, which means generators will be exhausted upon initialization, and creates a shallow copy to decouple the instance's state from the original collection.

        :param concepts: An iterable of Concept objects to initialize the instance with.
        :type concepts: typing.Iterable[Concept]
        """

        self._concepts: list[Concept] = list(concepts)

    @property
    def concepts(self) -> list[Concept]:
        """
        Replaces the internal collection of concepts with the provided iterable of Concept objects. The method converts the input iterable into a list before assignment, ensuring that the underlying `_concepts` attribute stores a concrete, mutable sequence. This operation overwrites any previously stored concepts rather than appending to them.

        :param value: An iterable of Concept objects to assign to the internal concepts list.
        :type value: typing.Iterable[Concept]
        """

        return self._concepts

    @concepts.setter
    def concepts(self, value: typing.Iterable[Concept]) -> None:
        self._concepts = list(value)
