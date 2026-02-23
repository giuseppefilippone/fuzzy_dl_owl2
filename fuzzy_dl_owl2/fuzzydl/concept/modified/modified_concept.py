from __future__ import annotations

import typing
from abc import ABC

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.concept.interface.has_concept_interface import (
    HasConceptInterface,
)
from fuzzy_dl_owl2.fuzzydl.concept.operator_concept import OperatorConcept
from fuzzy_dl_owl2.fuzzydl.modifier.modifier import Modifier
from fuzzy_dl_owl2.fuzzydl.util.constants import ConceptType


class ModifiedConcept(Concept, HasConceptInterface, ABC):
    """
    This class represents a conceptual construct where a base concept is altered by a modifier, thereby changing the degree or manner in which an individual satisfies that concept. It functions as a wrapper around an existing concept, preserving the underlying structural properties—such as roles and atomicity—while applying the semantic shift defined by the associated modifier. Users can instantiate this entity by providing a target concept and a modifier, and it supports integration into logical expressions through standard operator overloading for negation, conjunction, and disjunction.

    :param _modifier: The modifier instance that adjusts the degree of satisfaction of the underlying concept.
    :type _modifier: Modifier
    """


    def __init__(self, c: Concept, mod: Modifier) -> None:
        """
        Initializes a new instance representing a concept that has been modified by a specific modifier. The constructor configures the object as a Concept of type MODIFIED and establishes the interface connection to the provided base concept. It also stores the modifier internally to define the nature of the modification applied to the underlying concept.

        :param c: The underlying concept to be modified.
        :type c: Concept
        :param mod: The modifier applied to the concept.
        :type mod: Modifier
        """

        Concept.__init__(self, ConceptType.MODIFIED)
        HasConceptInterface.__init__(self, c)

        self._modifier: Modifier = mod

    @property
    def modifier(self) -> Modifier:
        """
        Sets the modifier applied to the concept by updating the internal state. This setter accepts a `Modifier` instance and assigns it to the private `_modifier` attribute, effectively replacing any previously associated modifier. It enables dynamic modification of the concept's behavior or properties after the object has been instantiated.

        :param value: 
        :type value: Modifier
        """

        return self._modifier

    @modifier.setter
    def modifier(self, value: Modifier) -> None:
        self._modifier = value

    def compute_name(self) -> str | None:
        """
        Generates a formatted string representation of the entity by combining the instance's modifier and current concept attributes. The resulting string is constructed by placing the modifier and concept side-by-side within parentheses, providing a concise identifier for the modified state. This method performs a read-only operation and does not alter the object's state, though it will raise an error if the required attributes are missing.

        :return: A string representing the computed name, formatted as "({modifier} {curr_concept})".

        :rtype: str | None
        """

        return f"({self.modifier} {self.curr_concept})"

    def compute_atomic_concepts(self) -> set[typing.Self]:
        """
        Computes the set of atomic concepts representing the fundamental components of the current concept state. This method delegates the actual computation to the `curr_concept` attribute, invoking its corresponding method to retrieve the results. It returns a set of atomic concepts, effectively exposing the decomposed structure of the underlying concept without modifying the object's state.

        :return: A set of atomic concepts representing the fundamental components of the current concept.

        :rtype: set[typing.Self]
        """

        return self.curr_concept.compute_atomic_concepts()

    def get_roles(self) -> set[str]:
        """
        Retrieves the set of role identifiers associated with the underlying concept instance. This method delegates the call to the `curr_concept` attribute, returning the collection of roles defined by that object. The operation relies on the internal concept reference being properly initialized; otherwise, an AttributeError may occur.

        :return: A set of role names associated with the current concept.

        :rtype: set[str]
        """

        return self.curr_concept.get_roles()

    def is_concrete(self) -> bool:
        """
        Determines whether the underlying concept is concrete by delegating the check to the `curr_concept` attribute. It returns a boolean value that reflects the concreteness status of the wrapped concept. This method serves as a pass-through, relying entirely on the implementation of the `is_concrete` method within the `curr_concept` object.

        :return: True if the current concept is concrete, False otherwise.

        :rtype: bool
        """

        return self.curr_concept.is_concrete()

    def replace(self, concept1: Concept, concept2: Concept) -> Concept:
        """
        This method serves as a no-operation implementation for the replacement logic, returning the current instance unchanged regardless of the input concepts. Although the signature suggests substituting `concept1` with `concept2`, this specific implementation indicates that the `ModifiedConcept` does not support or require internal modifications of this nature. Consequently, invoking this method has no side effects on the object's state or the provided arguments.

        :param concept1: The concept to be replaced.
        :type concept1: Concept
        :param concept2: The concept to replace the first argument with.
        :type concept2: Concept

        :return: Returns the instance itself after replacing `concept1` with `concept2`.

        :rtype: Concept
        """

        return self

    def __neg__(self) -> typing.Self:
        """
        Implements the unary negation operator for the concept, effectively treating the minus sign as a logical NOT operation. When invoked, this method returns a new instance representing the logical negation of the current concept by delegating to `OperatorConcept.not_`. The original instance remains unmodified, and the returned value is of the same type as the input.

        :return: Returns a new instance representing the logical negation of the current concept.

        :rtype: typing.Self
        """

        return OperatorConcept.not_(self)

    def __and__(self) -> typing.Self:
        """
        This method implements the bitwise AND operation (`&`) for the concept by delegating the logic to the `OperatorConcept.and_` method. It passes the current instance to the helper method, which returns a new instance of the same class, effectively creating a new concept based on the AND operation. The method does not modify the original instance in place, and any errors raised during the delegation process will propagate to the caller.

        :return: The result of the AND operation, returned as an instance of the same class.

        :rtype: typing.Self
        """

        return OperatorConcept.and_(self)

    def __or__(self) -> typing.Self:
        """
        Implements the bitwise OR operation for the concept, enabling the use of the pipe (`|`) operator. The method delegates the execution logic to the `OperatorConcept.or_` static method, passing the current instance as the argument. It returns a new instance of the same type, representing the result of the operation.

        :return: A new instance representing the logical disjunction (OR) of this concept with another.

        :rtype: typing.Self
        """

        return OperatorConcept.or_(self)

    def __repr__(self) -> str:
        """
        Returns the official string representation of the object by delegating directly to the `__str__` method. This implementation ensures that the output produced by the built-in `repr()` function is identical to the informal string representation. Consequently, the method provides a consistent string format for debugging and logging purposes without implementing distinct logic for representation.

        :return: A string representation of the object.

        :rtype: str
        """

        return str(self)

    def __str__(self) -> str:
        """
        Returns the informal string representation of the ModifiedConcept instance. This method delegates the generation of the display name to the `compute_name` method, which calculates the name based on the object's current state. It is intended to provide a human-readable format and is automatically invoked by the `str()` built-in function and print operations.

        :return: The informal string representation of the object, specifically its computed name.

        :rtype: str
        """

        return self.compute_name()
