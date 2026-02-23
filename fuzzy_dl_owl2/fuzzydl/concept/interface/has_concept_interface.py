import abc

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept


class HasConceptInterface(abc.ABC):
    """
    This class serves as an abstract base class that provides a standard interface for managing a mutable conceptual entity, ensuring that implementing objects can track and modify a specific concept. It encapsulates the logic for storing and updating the current concept through the `curr_concept` property, which allows for dynamic changes to the underlying representation at runtime. Subclasses can leverage this functionality to maintain a consistent state regarding the concept they are operating on, initializing with a specific concept instance and replacing it as needed through the provided property setter.

    :param _curr_concept: Internal storage for the active concept that the instance is currently representing or manipulating.
    :type _curr_concept: Concept
    """


    def __init__(self, concept: Concept) -> None:
        """
        Constructs a new instance and associates it with the provided Concept object. The method stores the argument in the private attribute `_curr_concept`, establishing the initial state of the instance. Because the assignment is by reference, any subsequent modifications to the original Concept object will be reflected in the instance's internal state, and the method does not perform explicit validation or deep copying of the input.

        :param concept: The Concept instance to be stored as the current concept.
        :type concept: Concept
        """

        self._curr_concept: Concept = concept

    @property
    def curr_concept(self) -> Concept:
        """
        Sets the current concept for the object, replacing any previously stored value. This method accepts a `Concept` instance and assigns it to the internal `_curr_concept` attribute, effectively updating the object's state to reflect the new active concept.

        :param value: The Concept object to set as the current concept.
        :type value: Concept
        """

        return self._curr_concept

    @curr_concept.setter
    def curr_concept(self, value: Concept) -> None:
        self._curr_concept = value
