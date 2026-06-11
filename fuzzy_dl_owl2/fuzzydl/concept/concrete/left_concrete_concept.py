from __future__ import annotations

import typing

from fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_concrete_concept import (
    FuzzyConcreteConcept,
)
from fuzzy_dl_owl2.fuzzydl.concept.operator_concept import OperatorConcept
from fuzzy_dl_owl2.fuzzydl.util.util import Util


class LeftConcreteConcept(FuzzyConcreteConcept):
    """
    This class models a left shoulder fuzzy set, representing a concept where membership is maximized at lower values and decreases linearly towards zero. It is defined by a domain of validity `[k1, k2]` and a satisfaction interval `[a, b]`, where membership is 1 for inputs less than or equal to `a`, 0 for inputs greater than or equal to `b`, and linearly interpolated for values in between. To use this class, instantiate it with a name and the four float parameters, ensuring that `k1` is less than or equal to `a` and `k2` is greater than or equal to `b` to satisfy validation constraints. Once instantiated, the membership degree of a specific value can be retrieved, and the object supports logical operations like negation, conjunction, and disjunction through standard Python operators.

    :param k1: The lower bound of the domain interval [k1, k2] over which the concept is defined.
    :type k1: float
    :param k2: The upper bound of the interval [k1, k2] defining the domain of the concept.
    :type k2: float
    :param _a: The lower bound of the transition interval, defining the point at which the membership degree begins to decrease from 1.0.
    :type _a: float
    :param _b: The upper bound of the satisfaction interval, representing the point at which the membership degree becomes zero.
    :type _b: float
    """

    def __init__(self, name: str, k1: float, k2: float, a: float, b: float) -> None:
        """
        Initializes the instance with a specific name and four numerical parameters that define the shape of the concept. It enforces strict ordering constraints to ensure the parameters form a valid "Left" function: specifically, `a` must be less than or equal to `b`, `k1` must be less than or equal to `a`, and `k2` must be greater than or equal to `b`. If any of these conditions are violated, the method triggers an error. Upon successful validation, the parameters are converted to floats and stored as instance attributes for later use.

        :param name: The identifier or label for the function instance.
        :type name: str
        :param k1: The first boundary parameter defining the left function, constrained to be less than or equal to 'a'.
        :type k1: float
        :param k2: Upper boundary value defining the function's shape, constrained to be greater than or equal to b.
        :type k2: float
        :param a: The lower bound of the interval, constrained such that k1 <= a <= b.
        :type a: float
        :param b: The upper bound of the transition interval where the function reaches its maximum value. Must be greater than or equal to `a` and less than or equal to `k2`.
        :type b: float
        """

        super().__init__(name)
        if a > b:
            Util.error(f"Error: Left functions require {a} <= {b}")
        if k1 > a:
            Util.error(f"Error: Left functions require {k1} <= {a}")
        if k2 < b:
            Util.error(f"Error: Left functions require {k2} >= {b}")

        self.k1: float = float(k1)
        self.k2: float = float(k2)
        self._a: float = float(a)
        self._b: float = float(b)

    @property
    def a(self) -> float:
        """
        Returns the left breakpoint of this left-shoulder membership function, i.e. the point up to which the degree is ``1`` and beyond which it starts decreasing linearly toward zero. The value is held internally as a float and is read without modifying the instance.

        :return: The breakpoint ``a`` where the degree begins to fall from ``1``.

        :rtype: float
        """

        return self._a

    @a.setter
    def a(self, value: float) -> None:
        """
        Sets the left breakpoint ``a`` of this left-shoulder membership function (the point up to which the degree is ``1``). The provided value is cast to a float and stored in the private ``_a`` attribute; a non-convertible value raises a ``ValueError`` or ``TypeError``.

        :param value: The new breakpoint, converted to a float.
        :type value: float
        """

        self._a = float(value)

    @property
    def b(self) -> float:
        """
        Returns the right breakpoint of this left-shoulder membership function, i.e. the point at which the degree reaches zero. The value is held internally as a float and is read without modifying the instance.

        :return: The breakpoint ``b`` where the degree reaches ``0``.

        :rtype: float
        """

        return self._b

    @b.setter
    def b(self, value: float) -> None:
        """
        Sets the right breakpoint ``b`` of this left-shoulder membership function (the point where the degree reaches zero). The provided value is cast to a float and stored in the private ``_b`` attribute; a non-convertible value raises a ``ValueError`` or ``TypeError``.

        :param value: The new breakpoint, converted to a float.
        :type value: float
        """

        self._b = float(value)

    def clone(self) -> typing.Self:
        """
        Creates and returns a new instance that is a copy of the current object. The clone is instantiated with the same values for `name`, `k1`, `k2`, `a`, and `b` as the original. This method does not modify the existing instance, though the resulting clone may share references to mutable objects if the constructor does not perform deep copying.

        :return: A new instance of the class with the same attributes as the current object.

        :rtype: typing.Self
        """

        return LeftConcreteConcept(self.name, self.k1, self.k2, self.a, self.b)

    def get_membership_degree(self, value: float) -> float:
        """
        Computes the degree of membership for a given numerical value within a left-shoulder fuzzy set defined by the parameters `a` and `b`. The function returns 1.0 for values less than or equal to `a`, indicating full membership, and returns 0.0 for values greater than or equal to `b`, indicating no membership. For values falling strictly between `a` and `b`, the method performs a linear interpolation to determine a partial membership value between 0.0 and 1.0. This implementation assumes that `a` is strictly less than `b` to avoid division by zero errors during the interpolation step.

        :param value: The numeric input value for which to calculate the membership degree.
        :type value: float

        :return: The degree of membership of the input value, ranging from 0.0 to 1.0. Returns 1.0 for values at or below the lower bound, 0.0 for values at or above the upper bound, and a linearly interpolated value for those in between.

        :rtype: float
        """

        if value <= self.a:
            return 1.0
        if value >= self.b:
            return 0.0
        return (self.b - value) / (self.b - self.a)

    def compute_name(self) -> str:
        """
        Generates a canonical string representation of the concept by formatting the instance's defining parameters into a specific pattern. The returned string follows the format "left-shoulder(k1, k2, a, b)", utilizing the values of the attributes `k1`, `k2`, `a`, and `b`. This method is read-only and does not modify the state of the object.

        :return: A string representation of the left-shoulder function name, including its parameters.

        :rtype: str
        """

        return f"left-shoulder({self.k1}, {self.k2}, {self.a}, {self.b})"

    def __neg__(self) -> FuzzyConcreteConcept:
        """
        Implements the unary negation operator, allowing the concept to be inverted using the minus sign. This method computes the logical negation of the current instance by delegating to the `OperatorConcept.not_` static method. The operation returns a new `FuzzyConcreteConcept` representing the complement of the original concept, leaving the source instance unmodified.

        :return: A new concept representing the logical negation of the current concept.

        :rtype: FuzzyConcreteConcept
        """

        return OperatorConcept.not_(self)

    def __and__(self, value: typing.Self) -> typing.Self:
        """
        Implements the bitwise AND operation (`&`) for the concept, calculating the intersection between the current instance and another instance of the same type. This method delegates the actual computation to `OperatorConcept.and_` and returns a new instance representing the result, ensuring that the original operands remain unmodified. It enables the combination of concepts to identify shared properties or elements.

        :param value: The other operand to perform the AND operation with.
        :type value: typing.Self

        :return: The result of the bitwise AND operation between the instance and the provided value.

        :rtype: typing.Self
        """

        return OperatorConcept.and_(self, value)

    def __or__(self, value: typing.Self) -> typing.Self:
        """
        Implements the bitwise OR operation for the concept, enabling the use of the pipe operator (`|`) to combine the current instance with another value of the same type. This method delegates the underlying logic to the `OperatorConcept.or_` static method, which calculates the result. The operation returns a new instance of `LeftConcreteConcept` representing the union or disjunction of the operands, ensuring that the original objects remain unmodified.

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
        # return id(self)
        return hash(
            (self.name, self.k1, self.k2, self.a, self.b, hash(self.type))
        )

    # def __str__(self) -> str:
    #     return self.name
