from __future__ import annotations

import typing

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.concept.modified.modified_concept import ModifiedConcept
from fuzzy_dl_owl2.fuzzydl.concept.operator_concept import OperatorConcept
from fuzzy_dl_owl2.fuzzydl.modifier.modifier import Modifier


class TriangularlyModifiedConcept(ModifiedConcept):
    """This class represents a conceptual entity where a base concept is adjusted by a triangular modifier, which transforms the degree of satisfaction or membership value of the concept in a specific, non-linear manner. To utilize this structure, one must instantiate it with the target concept and the desired triangular modifier. The resulting object supports standard logical operations, including negation, conjunction, and disjunction, allowing it to participate in complex logical expressions. Additionally, it offers methods for cloning the instance and recursively replacing sub-concepts within the underlying structure to facilitate dynamic manipulation of the conceptual hierarchy."""


    def __init__(self, c: Concept, mod: Modifier) -> None:
        """
        Initializes a new instance by associating a specific Concept with a Modifier. The constructor delegates the core initialization logic to the superclass, passing the provided concept and modifier arguments directly to the parent's `__init__` method. Consequently, the behavior and any potential side effects are determined by the implementation of the parent class.

        :param c: The underlying concept entity used to initialize the instance.
        :type c: Concept
        :param mod: The modifier to apply to the concept.
        :type mod: Modifier
        """

        super().__init__(c, mod)

    def clone(self) -> typing.Self:
        """
        Creates and returns a new instance of `TriangularlyModifiedConcept` that replicates the state of the current object. The clone is constructed using the existing `curr_concept` and `modifier` attributes, ensuring that the original object remains unmodified. Note that because the attributes are passed directly to the new instance, this operation performs a shallow copy; if the underlying concept or modifier objects are mutable, changes to them will be reflected in both the original and the clone.

        :return: A new instance of the class that is a copy of the current object.

        :rtype: typing.Self
        """

        return TriangularlyModifiedConcept(self.curr_concept, self.modifier)

    def replace(self, a: Concept, c: Concept) -> Concept:
        """
        Performs a substitution operation by replacing every instance of concept `a` with concept `c` within the underlying `curr_concept`. This method preserves the current `modifier` and constructs a new `TriangularlyModifiedConcept` instance containing the updated underlying concept. The final result is the logical negation of this newly constructed instance, ensuring that the original object remains unmodified.

        :param a: The concept to be replaced within the current concept structure.
        :type a: Concept
        :param c: The concept to substitute for the target concept `a`.
        :type c: Concept

        :return: A new Concept representing the result of replacing concept `a` with concept `c` within the current concept, preserving the existing modification context and applying a negation.

        :rtype: Concept
        """

        return -TriangularlyModifiedConcept(
            self.curr_concept.replace(a, c), self.modifier
        )

    def __neg__(self) -> Concept:
        """
        Implements the unary negation operator, enabling the use of the minus sign to represent the logical negation of the concept. This method returns a new `Concept` instance that wraps the current instance within a logical 'NOT' operation by delegating to `OperatorConcept.not_`. The operation does not modify the original object in place.

        :return: A new Concept representing the logical negation of this concept.

        :rtype: Concept
        """

        return OperatorConcept.not_(self)

    def __and__(self, value: typing.Self) -> typing.Self:
        """
        Implements the bitwise AND operation using the `&` operator for the current instance. This method delegates the actual computation to the `OperatorConcept.and_` static method, passing both the current instance and the provided value. It returns a new instance of the same type representing the result of the conjunction, without modifying the original operands.

        :param value: The other operand to perform the AND operation with.
        :type value: typing.Self

        :return: The result of the logical AND operation between this instance and the provided value.

        :rtype: typing.Self
        """

        return OperatorConcept.and_(self, value)

    def __or__(self, value: typing.Self) -> typing.Self:
        """
        Implements the bitwise OR operation for the concept, enabling the use of the pipe operator (`|`) to combine two instances. This method accepts another object of the same type and returns a new instance representing the logical disjunction or union of the two concepts. The operation is delegated to the `OperatorConcept` class to handle the specific calculation logic, ensuring that the original instances remain unmodified.

        :param value: Another instance to combine with the current instance using the OR operation.
        :type value: typing.Self

        :return: The result of the OR operation between the current instance and the provided value.

        :rtype: typing.Self
        """

        return OperatorConcept.or_(self, value)

    def __hash__(self) -> int:
        """
        Computes the integer hash value for the instance, allowing it to be used as a key in dictionaries or stored in sets. The implementation generates the hash by converting the object to its string representation and hashing that result, meaning the hash value is entirely dependent on the output of the `__str__` method. Consequently, the consistency of the hash relies on the stability of the string representation; if the object is mutable and its string form changes, the hash value will change, potentially violating the contract required for hashable objects.

        :return: An integer hash value derived from the string representation of the object.

        :rtype: int
        """

        return hash(str(self))
