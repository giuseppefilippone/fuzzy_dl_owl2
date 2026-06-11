from __future__ import annotations

import typing

from fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_concrete_concept import (
    FuzzyConcreteConcept,
)
from fuzzy_dl_owl2.fuzzydl.concept.operator_concept import OperatorConcept
from fuzzy_dl_owl2.fuzzydl.util.util import Util


class RightConcreteConcept(FuzzyConcreteConcept):
    """
    This class models a specific type of fuzzy logic concept characterized by a "right shoulder" membership function, where the degree of truth increases linearly from zero to one over a specified interval. It is typically used to represent concepts that become increasingly true as a variable grows larger, such as "high temperature" or "large size." To use this class, instantiate it with a name, the domain boundaries (`k1`, `k2`) defining the valid range of the variable, and the transition boundaries (`a`, `b`) defining the interval over which the membership ramps up. The class ensures structural integrity by validating that the domain fully encompasses the transition interval and that the transition boundaries are ordered correctly. Once instantiated, the membership degree for any value can be calculated using the `get_membership_degree` method, and the concept supports standard fuzzy logic operations like negation, conjunction, and disjunction.

    :param k1: The lower bound of the domain interval over which the concept is defined.
    :type k1: float
    :param k2: The upper bound of the interval [k1, k2] defining the domain of the concept.
    :type k2: float
    :param _a: The lower bound of the interval for which the concept is satisfied, representing the threshold where the membership degree begins to increase from zero.
    :type _a: float
    :param _b: The upper bound of the satisfaction interval, representing the threshold where the membership degree becomes 1.
    :type _b: float
    """

    def __init__(self, name: str, k1: float, k2: float, a: float, b: float) -> None:
        """
        Initializes the RightConcreteConcept instance by assigning a name and defining the geometric parameters k1, k2, a, and b. This constructor enforces specific ordering constraints necessary for the validity of the underlying "Right" function: a must not exceed b, k1 must not exceed a, and k2 must be at least b. If these constraints are not met, the method triggers an error. Finally, it stores the parameters as instance attributes, ensuring a and b are stored as floating-point numbers.

        :param name: The name of the function instance.
        :type name: str
        :param k1: The lower bound of the support interval, which must be less than or equal to the start of the core.
        :type k1: float
        :param k2: Upper bound parameter that must be greater than or equal to b.
        :type k2: float
        :param a: The lower boundary of the interval, satisfying the condition k1 <= a <= b.
        :type a: float
        :param b: The upper bound of the interval, which must be greater than or equal to a and less than or equal to k2.
        :type b: float
        """

        super().__init__(name)
        if a > b:
            Util.error(f"Error: Right functions require {a} <= {b}")
        if k1 > a:
            Util.error(f"Error: Right functions require {k1} <= {a}")
        if k2 < b:
            Util.error(f"Error: Right functions require {k2} >= {b}")

        self.k1: float = k1
        self.k2: float = k2
        self._a: float = float(a)
        self._b: float = float(b)

    @property
    def a(self) -> float:
        """
        Returns the left breakpoint of this right-shoulder membership function, i.e. the point up to which the degree is ``0`` and beyond which it starts increasing linearly toward one. The value is held internally as a float and is read without modifying the instance.

        :return: The breakpoint ``a`` where the degree begins to rise from ``0``.

        :rtype: float
        """

        return self._a

    @a.setter
    def a(self, value: float) -> None:
        """
        Sets the left breakpoint ``a`` of this right-shoulder membership function (the point up to which the degree is ``0``). The provided value is cast to a float and stored in the private ``_a`` attribute; a non-convertible value raises a ``ValueError`` or ``TypeError``.

        :param value: The new breakpoint, converted to a float.
        :type value: float
        """

        self._a = float(value)

    @property
    def b(self) -> float:
        """
        Returns the right breakpoint of this right-shoulder membership function, i.e. the point at which the degree reaches its maximum value of ``1``. The value is held internally as a float and is read without modifying the instance.

        :return: The breakpoint ``b`` where the degree reaches ``1``.

        :rtype: float
        """

        return self._b

    @b.setter
    def b(self, value: float) -> None:
        """
        Sets the right breakpoint ``b`` of this right-shoulder membership function (the point where the degree reaches ``1``). The provided value is cast to a float and stored in the private ``_b`` attribute; a non-convertible value raises a ``ValueError`` or ``TypeError``.

        :param value: The new breakpoint, converted to a float.
        :type value: float
        """

        self._b = float(value)

    def clone(self) -> typing.Self:
        """
        Creates and returns a distinct copy of the current instance by instantiating a new `RightConcreteConcept` object. The new object is initialized with the exact same values for the `name`, `k1`, `k2`, `a`, and `b` attributes as the original. This method ensures that the original object remains unmodified while providing a separate entity with identical state.

        :return: A new instance of the class initialized with the same attribute values as the current object.

        :rtype: typing.Self
        """

        return RightConcreteConcept(self.name, self.k1, self.k2, self.a, self.b)

    def get_membership_degree(self, x: float) -> float:
        """
        Calculates the membership degree of a given value `x` within a right-shoulder fuzzy set defined by the parameters `a` and `b`. The function returns 0.0 if `x` is less than or equal to `a`, and 1.0 if `x` is greater than or equal to `b`. For values falling strictly between `a` and `b`, the method computes a linear interpolation, returning a value between 0.0 and 1.0 that represents the proportional distance of `x` from the lower bound `a`. This calculation is stateless and does not modify the object's attributes.

        :param x: The input value to evaluate for membership.
        :type x: float

        :return: The degree of membership of x in the interval [a, b], ranging from 0.0 to 1.0 based on linear interpolation.

        :rtype: float
        """

        if x <= self.a:
            return 0.0
        if x >= self.b:
            return 1.0
        return (x - self.a) / (self.b - self.a)

    def compute_name(self) -> str:
        """
        Generates a standardized string representation of the right-shoulder concept instance by interpolating the object's defining parameters into a specific format. The returned string follows the pattern "right-shoulder(k1, k2, a, b)", utilizing the values of the corresponding attributes. This operation is read-only and does not alter the state of the object, though it requires that the necessary attributes exist on the instance.

        :return: A string representing the name of the right-shoulder function, formatted with the current parameters k1, k2, a, and b.

        :rtype: str
        """

        return f"right-shoulder({self.k1}, {self.k2}, {self.a}, {self.b})"

    def __neg__(self) -> FuzzyConcreteConcept:
        """
        Implements the unary negation operator, allowing the concept to be inverted using the minus sign. This method returns a new FuzzyConcreteConcept representing the logical negation of the current instance, effectively computing the complement of the concept. The operation is performed by delegating to OperatorConcept.not_ and does not modify the original object in place.

        :return: A `FuzzyConcreteConcept` representing the logical negation of the current concept.

        :rtype: FuzzyConcreteConcept
        """

        return OperatorConcept.not_(self)

    def __and__(self, value: typing.Self) -> typing.Self:
        """
        Performs a logical or bitwise conjunction between the current instance and another instance of the same type, typically invoked via the `&` operator. This method delegates the core logic to the `and_` static method of the `OperatorConcept` class, ensuring that the operation is handled consistently within the broader module architecture. It returns a new instance of the class representing the result of the conjunction, leaving the original operands unchanged unless the underlying `OperatorConcept` implementation specifies otherwise.

        :param value: The operand to perform the AND operation with.
        :type value: typing.Self

        :return: A new instance representing the logical conjunction of this object and the provided value.

        :rtype: typing.Self
        """

        return OperatorConcept.and_(self, value)

    def __or__(self, value: typing.Self) -> typing.Self:
        """
        Implements the bitwise OR operation using the `|` operator, allowing the instance to be combined with another value of the same type. The method delegates the specific logic of the operation to `OperatorConcept.or_`, passing both the current instance and the provided value as arguments. It returns the resulting instance, which maintains the type of the operands, though any side effects depend on the implementation of the delegated `or_` method.

        :param value: The right-hand operand to combine with the current instance using the OR operation.
        :type value: typing.Self

        :return: The result of the OR operation between this instance and the provided value.

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
            (self.k1, self.k2, hash(self.a), hash(self.b))
        )

    # def __str__(self) -> str:
    #     return self.get_name()
