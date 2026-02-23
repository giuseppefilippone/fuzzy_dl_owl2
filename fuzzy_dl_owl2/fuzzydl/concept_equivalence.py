from __future__ import annotations

import typing

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept


class ConceptEquivalence:
    """
    This class encapsulates the axiom of equivalence between two distinct concepts, serving as a structural representation that asserts their equality within a specific context. It functions as a container for a pair of `Concept` objects, allowing users to define and manipulate relationships where two entities are treated as interchangeable. To utilize this class, instantiate it with the two concepts you wish to equate; you can then access these concepts directly or via getter methods, and generate independent copies of the equivalence statement using the clone functionality.

    :param c1: The first concept participating in the equivalence relationship.
    :type c1: Concept
    :param c2: The second concept participating in the equivalence relation.
    :type c2: Concept
    """


    def __init__(self, c1: Concept, c2: Concept) -> None:
        # First concept
        """
        Initializes a new instance representing an equivalence relationship between two concepts. The method accepts two `Concept` objects, `c1` and `c2`, and assigns them to the corresponding instance attributes `self.c1` and `self.c2` to establish the object's internal state. This constructor performs no validation or modification of the input concepts, relying on the caller to provide valid instances.

        :param c1: The first concept to be stored in the instance.
        :type c1: Concept
        :param c2: The second concept to store.
        :type c2: Concept
        """

        self.c1: Concept = c1
        # Second concept
        self.c2: Concept = c2

    def clone(self) -> typing.Self:
        """
        Creates and returns a new instance of `ConceptEquivalence` that replicates the state of the current object. The new object is constructed using the same `c1` and `c2` attributes found in the original instance. This method performs a shallow copy of the attributes, meaning that if `c1` or `c2` are mutable objects, the clone will reference the same underlying objects as the source. The original instance remains unmodified by this operation.

        :return: A new instance of the class initialized with the same concepts as the current object.

        :rtype: typing.Self
        """

        return ConceptEquivalence(self.c1, self.c2)

    def get_c1(self) -> Concept:
        """
        Returns the first concept associated with this equivalence instance. This accessor method retrieves the value of the internal attribute `c1`, representing one of the two concepts involved in the equivalence relationship. The operation is read-only and does not modify the state of the object or the returned concept.

        :return: The Concept instance stored in the c1 attribute.

        :rtype: Concept
        """

        return self.c1

    def get_c2(self) -> Concept:
        """
        Returns the second concept associated with this equivalence instance. This method acts as an accessor for the `c2` attribute, retrieving the `Concept` object that forms one side of the equivalence relationship. It performs no modifications to the object state and simply returns the stored value.

        :return: The `Concept` object stored in the `c2` attribute.

        :rtype: Concept
        """

        return self.c2
