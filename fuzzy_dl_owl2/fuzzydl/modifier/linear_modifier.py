from __future__ import annotations

import typing

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.concept.modified.linearly_modified_concept import (
    LinearlyModifiedConcept,
)
from fuzzy_dl_owl2.fuzzydl.concept.operator_concept import OperatorConcept
from fuzzy_dl_owl2.fuzzydl.modifier.modifier import Modifier


class LinearModifier(Modifier):
    """
    This class implements a modifier that applies a piecewise linear transformation to the membership degrees of concepts, governed by a configurable parameter 'c'. The value of 'c' determines the inflection point of the linear function, allowing for precise control over the intensity of the modification. To use this class, instantiate it with a name and the desired 'c' value, then apply it to a `Concept` object using the `modify` method to produce a `LinearlyModifiedConcept`. The logic ensures that membership degrees are clamped between 0 and 1, and the class supports logical operations such as negation, conjunction, and disjunction.

    :param _c: The parameter determining the slope and intercept of the linear membership function.
    :type _c: float
    :param _a: The threshold value on the input domain that separates the two linear segments of the membership function.
    :type _a: float
    :param _b: The y-coordinate of the intermediate point $(a, b)$ in the piecewise linear membership function.
    :type _b: float
    """

    def __init__(self, name: str, c: float) -> None:
        """
        Initializes the modifier with a unique identifier and a coefficient that determines the weighting behavior. The coefficient `c` is stored directly, and two derived attributes, `_a` and `_b`, are calculated to represent normalized weights such that their sum equals 1. Specifically, `_a` is set to `c / (c + 1)` and `_b` to `1 / (c + 1)`. This setup ensures that the modifier can apply a linear transformation based on the relative strength of the coefficient. The method propagates the name to the parent class for initialization. A critical edge case to consider is that providing a coefficient value of `-1.0` will cause a `ZeroDivisionError` during the calculation of the internal weights.

        :param name: Identifier for the instance, passed to the parent class.
        :type name: str
        :param c: A coefficient used to determine the relative weights of internal components. It is used to derive two values that sum to 1.
        :type c: float
        """

        super().__init__(name)
        self._c: float = c
        self._a: float = c / (c + 1.0)
        self._b: float = 1.0 / (c + 1.0)

    @property
    def a(self) -> float:
        """
        Returns the first derived weight of the linear modifier, computed at construction as ``c / (c + 1)``. Together with ``b`` it forms the pair of weights (summing to ``1``) that define the piecewise-linear membership transformation. The value is read from the private ``_a`` attribute without modifying the instance.

        :return: The derived weight ``a`` of the modifier.

        :rtype: float
        """

        return self._a

    @a.setter
    def a(self, value: float) -> None:
        """
        Sets the first derived weight ``a`` of the linear modifier. The provided value is stored directly in the private ``_a`` attribute without coercion or re-deriving it from ``c``.

        :param value: The new derived weight ``a``.
        :type value: float
        """

        self._a = value

    @property
    def b(self) -> float:
        """
        Returns the second derived weight of the linear modifier, computed at construction as ``1 / (c + 1)``. Together with ``a`` it forms the pair of weights (summing to ``1``) that define the piecewise-linear membership transformation. The value is read from the private ``_b`` attribute without modifying the instance.

        :return: The derived weight ``b`` of the modifier.

        :rtype: float
        """

        return self._b

    @b.setter
    def b(self, value: float) -> None:
        """
        Sets the second derived weight ``b`` of the linear modifier. The provided value is stored directly in the private ``_b`` attribute without coercion or re-deriving it from ``c``.

        :param value: The new derived weight ``b``.
        :type value: float
        """

        self._b = value

    @property
    def c(self) -> float:
        """
        Returns the shape coefficient ``c`` of the linear modifier, the single parameter from which the derived weights ``a`` and ``b`` are computed and which controls the intensity of the modification. The value is read from the private ``_c`` attribute without modifying the instance.

        :return: The shape coefficient ``c`` of the modifier.

        :rtype: float
        """

        return self._c

    @c.setter
    def c(self, value: float) -> None:
        """
        Sets the shape coefficient ``c`` of the linear modifier. The provided value is stored directly in the private ``_c`` attribute; note that the derived weights ``a`` and ``b`` are not recomputed.

        :param value: The new shape coefficient ``c``.
        :type value: float
        """

        self._c = value

    def clone(self) -> typing.Self:
        """
        Creates and returns a new instance of `LinearModifier` that is a copy of the current object. The clone is initialized with the same `name` and `c` attributes as the original, resulting in an independent object that can be modified without affecting the source.

        :return: A new instance of the class that is a copy of the current object.

        :rtype: typing.Self
        """

        return LinearModifier(self.name, self.c)

    def modify(self, concept: Concept) -> LinearlyModifiedConcept:
        """
        Applies the linear modification logic encapsulated by this instance to a provided concept. This method constructs and returns a new `LinearlyModifiedConcept` object that wraps the original concept alongside the current modifier, effectively binding the two without mutating the original concept.

        :param concept: The Concept instance to be modified.
        :type concept: Concept

        :return: A `LinearlyModifiedConcept` representing the input `concept` modified by the current object.

        :rtype: LinearlyModifiedConcept
        """

        return LinearlyModifiedConcept(concept, self)

    def compute_name(self) -> str:
        """
        Generates a string identifier for the linear modifier based on its coefficient attribute. The returned string follows the specific format "linear-modifier(c)", where 'c' is replaced by the string representation of the instance's 'c' attribute. This method performs no state modification and assumes the 'c' attribute is defined and convertible to a string.

        :return: A string representing the name of the linear modifier, formatted as 'linear-modifier({c})'.

        :rtype: str
        """

        return f"linear-modifier({self.c})"

    def get_membership_degree(self, value: float) -> float:
        """
        Calculates the degree of membership for a given input value using a piecewise linear function defined by the instance attributes `a` and `b`. The function maps the input range [0, 1] to an output range [0, 1], clamping any values outside this interval to the nearest boundary. Specifically, for inputs between 0 and `a`, the result is linearly interpolated from 0 to `b`, whereas inputs between `a` and 1 are interpolated from `b` to 1. This method does not modify the state of the object.

        :param value: The crisp input value for which to calculate the membership degree. Values outside the range [0, 1] are clamped to the nearest boundary.
        :type value: float

        :return: A float representing the degree of membership for the input value, ranging from 0.0 to 1.0.

        :rtype: float
        """

        if value <= 0.0:
            return 0.0
        if value >= 1.0:
            return 1.0
        if value <= self.a:
            return self.b / self.a * value
        return (value * (1.0 - self.b) + self.b - self.a) / (1.0 - self.a)

    def __neg__(self) -> Concept:
        """
        Implements the unary negation operator for the `LinearModifier` instance, returning a new `Concept` that represents the logical negation of the current modifier. This operation delegates the creation of the negated concept to the `OperatorConcept.not_` factory method, ensuring that the resulting object encapsulates the inverse logic without modifying the original instance.

        :return: A Concept representing the logical negation of the current instance.

        :rtype: Concept
        """

        return OperatorConcept.not_(self)

    def __and__(self, value: typing.Self) -> typing.Self:
        """
        Implements the bitwise AND operation (`&`) for the `LinearModifier` class, enabling the combination of the current instance with another instance of the same type. This method delegates the specific logic for the conjunction to `OperatorConcept.and_`, which determines how the two modifiers interact. The operation returns a new `LinearModifier` instance representing the result, ensuring that the original operands are not modified.

        :param value: The right-hand operand for the AND operation.
        :type value: typing.Self

        :return: The result of the AND operation between this instance and the provided value.

        :rtype: typing.Self
        """

        return OperatorConcept.and_(self, value)

    def __or__(self, value: typing.Self) -> typing.Self:
        """
        Implements the bitwise OR operation for the `LinearModifier` class, allowing instances to be combined using the pipe operator (`|`). This method takes another `LinearModifier` instance and delegates the combination logic to `OperatorConcept.or_`, returning a new instance that represents the result of the operation. The original instances remain unmodified, ensuring that the operation is side-effect-free.

        :param value: The right-hand operand to combine with the current instance using the OR operation.
        :type value: typing.Self

        :return: The result of the OR operation between the current instance and the provided value.

        :rtype: typing.Self
        """

        return OperatorConcept.or_(self, value)

    def __hash__(self) -> int:
        """
        Return a hash value for this object, computed from its string representation. This approach ensures that the hash value reflects the structural identity of the object without relying on cached values or additional methods. The hash is derived from the output of the `__str__` method, which provides a consistent and unique representation of the concept's structure. This implementation does not utilize any internal caching mechanism and directly computes the hash each time it is called.

        :return: An integer hash value representing the structural identity of this object.

        :rtype: int
        """
        # return hash(str(self))
        return hash((self.name, self.c, self.a, self.b))

    # def __str__(self) -> str:
    #     return self.compute_name()
