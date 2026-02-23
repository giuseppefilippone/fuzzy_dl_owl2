from __future__ import annotations

import typing

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.concept.modified.modified_concept import ModifiedConcept
from fuzzy_dl_owl2.fuzzydl.concept.operator_concept import OperatorConcept
from fuzzy_dl_owl2.fuzzydl.modifier.modifier import Modifier


class LinearlyModifiedConcept(ModifiedConcept):
    """This class models a concept whose degree of satisfaction is adjusted by a linear modifier, representing a structure of the form (modifier C). It is instantiated by providing a base concept and a specific linear modifier that scales or shifts the concept's truth value in a linear fashion. The class supports standard logical operations, including negation, conjunction, and disjunction, enabling the integration of modified concepts into complex logical expressions. Furthermore, it provides utility methods for cloning the instance and replacing sub-concepts within the underlying structure, allowing for dynamic manipulation of the concept hierarchy."""


    def __init__(self, c: Concept, mod: Modifier) -> None:
        """
        Initializes a new instance representing a concept that has been modified, presumably in a linear fashion based on the class name. The constructor requires a base `Concept` object and a `Modifier` object as arguments, which are passed directly to the superclass constructor to handle the core initialization logic. This method relies on the parent class to validate the inputs and set up the internal state, meaning any side effects or validation errors are determined by the implementation of the superclass.

        :param c: The Concept instance to initialize the object with.
        :type c: Concept
        :param mod: The modifier applied to the concept.
        :type mod: Modifier
        """

        super().__init__(c, mod)

    def clone(self) -> typing.Self:
        """
        Creates and returns a new instance of `LinearlyModifiedConcept` that duplicates the state of the current object. The clone is initialized with the same `curr_concept` and `modifier` attributes as the original, ensuring that subsequent modifications to the new instance do not affect the source. This method provides a mechanism for obtaining an independent copy of the object without altering the original's internal state.

        :return: A new instance of the class that is a copy of the current object, initialized with the same concept and modifier.

        :rtype: typing.Self
        """

        return LinearlyModifiedConcept(self.curr_concept, self.modifier)

    def replace(self, a: Concept, c: Concept) -> typing.Self:
        """
        Returns a new instance of the class where the underlying concept has been updated by replacing occurrences of concept `a` with concept `c`. The replacement operation is delegated to the underlying concept, and the modifier associated with the current instance is preserved in the result. This method does not mutate the original instance but instead returns a modified copy.

        :param a: The concept to find and replace.
        :type a: Concept
        :param c: The concept to substitute in place of `a`.
        :type c: Concept

        :return: A new instance of the class where the underlying concept has `a` replaced by `c`, retaining the current modifier.

        :rtype: typing.Self
        """

        return -LinearlyModifiedConcept(self.curr_concept.replace(a, c), self.modifier)

    def __neg__(self) -> Concept:
        """
        Returns the logical negation of the current concept, effectively representing the 'not' operation. This method is invoked when the unary minus operator (`-`) is applied to an instance of the class. It delegates the construction of the resulting concept to `OperatorConcept.not_`, returning a new `Concept` object without modifying the original instance.

        :return: A new Concept representing the logical negation of the current concept.

        :rtype: Concept
        """

        return OperatorConcept.not_(self)

    def __and__(self, value: typing.Self) -> typing.Self:
        """
        Implements the bitwise AND operation for the concept, allowing the use of the `&` operator to combine it with another instance of the same type. This method delegates the actual computation to `OperatorConcept.and_`, ensuring that the logic for conjunction is handled centrally within the module. The operation returns a new instance representing the result of the combination, without modifying the original objects.

        :param value: The right-hand operand for the AND operation.
        :type value: typing.Self

        :return: The result of the AND operation between this instance and the provided value.

        :rtype: typing.Self
        """

        return OperatorConcept.and_(self, value)

    def __or__(self, value: typing.Self) -> typing.Self:
        """
        Performs a logical OR or union operation between the current instance and another instance of the same type, enabling the use of the pipe operator (`|`). This method delegates the underlying logic to `OperatorConcept.or_`, which handles the specific combination rules. It returns a new instance representing the combined concept without modifying the original operands. The operation expects the provided value to be a compatible instance of the same class.

        :param value: The other operand to perform the OR operation with.
        :type value: typing.Self

        :return: An instance representing the result of the OR operation between this instance and the provided value.

        :rtype: typing.Self
        """

        return OperatorConcept.or_(self, value)

    def __hash__(self) -> int:
        """
        Computes the hash value for the instance by delegating to the hash of the object's string representation. This behavior allows instances of `LinearlyModifiedConcept` to be used as dictionary keys or stored in sets, provided that the string representation remains consistent for equal objects and does not change over the object's lifetime. The implementation relies on the `__str__` method to generate the input for the hash function.

        :return: An integer hash value derived from the object's string representation.

        :rtype: int
        """

        return hash(str(self))
