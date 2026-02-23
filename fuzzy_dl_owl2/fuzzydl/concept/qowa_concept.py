import typing

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_concrete_concept import (
    FuzzyConcreteConcept,
)
from fuzzy_dl_owl2.fuzzydl.concept.operator_concept import OperatorConcept
from fuzzy_dl_owl2.fuzzydl.concept.owa_concept import OwaConcept
from fuzzy_dl_owl2.fuzzydl.util.constants import ConceptType


class QowaConcept(OwaConcept):
    """
    This class implements a quantified aggregation strategy that combines a collection of concepts using a fuzzy quantifier to dynamically determine the weighting scheme. Instead of requiring explicit weights, it calculates them by evaluating the membership degree of the provided quantifier across the range of input concepts. Users can instantiate this object by providing a fuzzy concrete concept as the quantifier and a list of concepts to be aggregated. During initialization, the system automatically computes the weights and generates a standardized string representation. It supports standard logical operations and ensures structural consistency through cloning and replacement methods.

    :param type: The classification identifier for the concept, indicating it is a quantified OWA.
    :type type: typing.Any
    :param _quantifier: Stores the fuzzy concrete concept representing the quantifier, which determines the aggregation weights for the OWA operation.
    :type _quantifier: FuzzyConcreteConcept
    :param name: String representation of the concept formatted as `(q-owa Q C1 ... Cn)`, automatically generated during initialization and updated when the quantifier changes.
    :type name: typing.Any
    """


    def __init__(
        self, quantifier: FuzzyConcreteConcept, concepts: list[Concept]
    ) -> None:
        """
        Initializes a Quantified Ordered Weighted Averaging (OWA) concept by associating a fuzzy quantifier with a list of underlying concepts. This constructor sets the entity type to QUANTIFIED_OWA and stores the provided quantifier, which is subsequently used to compute the specific weights for the aggregation based on the number of concepts in the list. Additionally, it automatically generates a display name for the instance and invokes the parent class initialization to handle the base concept collection.

        :param quantifier: The fuzzy concrete concept representing the linguistic quantifier used to define the weighting scheme for the OWA aggregation.
        :type quantifier: FuzzyConcreteConcept
        :param concepts: A list of concepts representing the criteria or arguments over which the quantifier is applied.
        :type concepts: list[Concept]
        """

        super().__init__(None, concepts)

        self.type = ConceptType.QUANTIFIED_OWA
        self._quantifier: FuzzyConcreteConcept = quantifier
        self.compute_weights(len(concepts))
        self.name = self.compute_name()

    @property
    def quantifier(self) -> FuzzyConcreteConcept:
        """
        Sets the quantifier for the concept to the provided `FuzzyConcreteConcept` value. This method updates the internal `_quantifier` attribute and automatically triggers a recalculation of the concept's name by calling `compute_name`, ensuring that the display name remains consistent with the new quantifier state.

        :param value: The fuzzy concrete concept to assign as the quantifier.
        :type value: FuzzyConcreteConcept
        """

        return self._quantifier

    @quantifier.setter
    def quantifier(self, value: FuzzyConcreteConcept) -> None:
        self._quantifier = value
        self.name = self.compute_name()

    def clone(self) -> typing.Self:
        """
        Creates and returns a new instance of `QowaConcept` that is a shallow copy of the current object. The new instance preserves the original quantifier and creates a new list containing references to the same underlying concept objects. This ensures that structural modifications to the clone's list of concepts do not affect the original instance, although changes to the individual concept objects themselves will be reflected in both.

        :return: A new instance of the class with the same quantifier and a copy of the concepts list.

        :rtype: typing.Self
        """

        return QowaConcept(self.quantifier, [c for c in self.concepts])

    def compute_weights(self, n: int) -> None:
        """
        Calculates and appends a sequence of weights to the instance's weight list based on the associated quantifier. The method iterates `n` times, calculating the normalized position `w` and determining the membership degree of the difference between the current and previous positions (which is constant at `1/n`). If the input `n` is less than or equal to zero, the method returns without making changes. This operation modifies the internal state by appending to the `weights` attribute, meaning repeated calls will extend the list rather than replace it.

        :param n: The number of weights to generate, used as the denominator for calculating the step size.
        :type n: int
        """

        if n <= 0:
            return
        if self.weights is None:
            self.weights = []
        previous: float = 0.0
        for i in range(1, n + 1):
            w: float = i / n
            self.weights.append(self.quantifier.get_membership_degree(w - previous))
            previous: float = w

    def replace(self, a: Concept, c: Concept) -> typing.Optional[Concept]:
        """
        Returns a new concept instance where all occurrences of the target concept `a` are substituted with the replacement concept `c`. This operation traverses the internal list of concepts recursively, applying the replacement to each sub-concept to ensure the substitution propagates through the entire structure. The method constructs a new `OwaConcept` using the original quantifier and the modified list of concepts, then returns the negation of that structure, leaving the original instance unmodified.

        :param a: The concept to be replaced.
        :type a: Concept
        :param c: The concept to substitute for `a` within the structure.
        :type c: Concept

        :return: A new Concept instance where all occurrences of concept `a` have been replaced by concept `c`.

        :rtype: typing.Optional[Concept]
        """

        return -OwaConcept(self.quantifier, [ci.replace(a, c) for ci in self.concepts])

    def compute_name(self) -> str:
        """
        Generates a standardized string representation of the QOWA concept by combining its quantifier and associated concepts into a specific parenthetical format. The returned string follows the pattern "(q-owa <quantifier> <concept1> <concept2> ...)", where the quantifier and the list of concepts are converted to strings and joined by spaces. This method does not modify the object's state and relies on the string conversion methods of the underlying quantifier and concept objects.

        :return: A string representation of the query name, formatted with the quantifier and concepts.

        :rtype: str
        """

        return f"(q-owa {self.quantifier} {' '.join(map(str, self.concepts))})"

    def __neg__(self) -> Concept:
        """
        Returns the logical negation of the current concept instance, corresponding to the unary minus operator. The method constructs an intermediate `OwaConcept` using the instance's weights and concepts, then applies a logical NOT operation via `OperatorConcept.not_`. This results in a new `Concept` object representing the complement of the original logic without modifying the original instance.

        :return: Returns a new Concept representing the logical negation of the current instance.

        :rtype: Concept
        """

        return OperatorConcept.not_(OwaConcept(self.weights, self.concepts))

    def __and__(self, value: typing.Self) -> typing.Self:
        """
        Implements the bitwise AND operation (`&`) for the `QowaConcept` instance, allowing it to be combined with another instance of the same type. This method delegates the actual computation to `OperatorConcept.and_`, passing the current object and the provided value as operands. The operation returns a new instance representing the result of the conjunction, leaving the original operands unchanged.

        :param value: The right-hand operand for the AND operation.
        :type value: typing.Self

        :return: A new instance representing the result of the AND operation between this object and the provided value.

        :rtype: typing.Self
        """

        return OperatorConcept.and_(self, value)

    def __or__(self, value: typing.Self) -> typing.Self:
        """
        Implements the bitwise OR operation for the concept, allowing it to be combined with another instance of the same type using the pipe operator (`|`). This method delegates the actual combination logic to `OperatorConcept.or_`, which produces a new concept representing the logical disjunction or union of the two operands. The operation is non-destructive, ensuring that the original instances remain unmodified while a new object is returned to represent the result.

        :param value: The right-hand operand for the OR operation.
        :type value: typing.Self

        :return: The result of the logical OR or union operation between this instance and the provided value.

        :rtype: typing.Self
        """

        return OperatorConcept.or_(self, value)

    def __hash__(self) -> int:
        """
        Computes the hash value for the instance by hashing its string representation, enabling the object to be used as a key in dictionaries or stored in sets. This implementation delegates the hashing logic to the result of the `__str__` method, ensuring that instances with identical string representations yield the same hash. Consequently, the efficiency of this operation is directly tied to the performance of the object's string conversion, and any exceptions raised during string formatting will propagate to the hash calculation.

        :return: An integer hash value derived from the string representation of the object.

        :rtype: int
        """

        return hash(str(self))
