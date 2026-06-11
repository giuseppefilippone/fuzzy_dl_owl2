from __future__ import annotations

import typing

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.concept.modified.triangularly_modified_concept import (
    TriangularlyModifiedConcept,
)
from fuzzy_dl_owl2.fuzzydl.concept.operator_concept import OperatorConcept
from fuzzy_dl_owl2.fuzzydl.modifier.modifier import Modifier
from fuzzy_dl_owl2.fuzzydl.util.util import Util


class TriangularModifier(Modifier):
    r"""
    This class implements a fuzzy logic modifier that applies a triangular membership function to concepts, defining how strongly a specific value belongs to a modified concept. The function is characterized by three parameters: the left boundary `a`, the peak `b`, and the right boundary `c`, which must satisfy the ordering $a \le b \le c$. Membership degrees increase linearly from 0 at `a` to 1 at `b`, and then decrease linearly back to 0 at `c`. To utilize this modifier, instantiate it with a name and the three boundary values, and then apply it to a `Concept` instance via the `modify` method, which produces a `TriangularlyModifiedConcept`. The class also provides a `get_membership_degree` method for calculating the specific membership value of a given input.

    :param _a: The left endpoint of the triangular membership function, marking the lower bound where the membership degree begins to increase from zero.
    :type _a: typing.Any
    :param _b: The x-coordinate of the peak of the triangular membership function, representing the point of maximum membership degree.
    :type _b: typing.Any
    :param _c: The right endpoint of the triangular membership function, defining the upper bound where the membership degree reaches zero.
    :type _c: typing.Any
    """

    def __init__(self, name: str, a: float, b: float, c: float) -> None:
        """
        Initializes the triangular modifier with a specific identifier and three parameters defining its shape. The parameters `a`, `b`, and `c` represent the start, peak, and end points of the triangle, respectively, and must satisfy the condition `a <= b <= c`. If this ordering constraint is violated, the method raises an error via the utility module. Upon successful validation, the method stores these values as private attributes and invokes the superclass constructor to handle the initialization of the base component.

        :param name: Identifier or label for the triangular function instance.
        :type name: str
        :param a: The lower bound of the triangular function, representing the minimum value. Must be less than or equal to `b`.
        :type a: float
        :param b: The value representing the peak or mode of the triangular function, which must be greater than or equal to the lower limit and less than or equal to the upper limit.
        :type b: float
        :param c: The upper bound or maximum value of the triangular function, which must be greater than or equal to `b`.
        :type c: float
        """

        super().__init__(name)
        if not (a <= b <= c):
            Util.error(f"Error: Triangular functions require {a} <= {b} <= {c}")
        self._a = a
        self._b = b
        self._c = c

    @property
    def a(self) -> float:
        """
        Returns the left endpoint of this triangular modifier's membership function, i.e. the lower bound where the membership degree begins rising from zero toward the peak. The value is read from the private ``_a`` attribute without modifying the instance.

        :return: The left endpoint ``a`` of the triangle.

        :rtype: float
        """

        return self._a

    @a.setter
    def a(self, value: float) -> None:
        """
        Sets the left endpoint ``a`` of this triangular modifier's membership function. The provided value is stored directly in the private ``_a`` attribute; the ``a <= b <= c`` ordering is not re-validated here.

        :param value: The new left endpoint ``a``.
        :type value: float
        """

        self._a = value

    @property
    def b(self) -> float:
        """
        Returns the peak of this triangular modifier's membership function, i.e. the point where the membership degree reaches its maximum value of ``1``. The value is read from the private ``_b`` attribute without modifying the instance.

        :return: The peak ``b`` of the triangle.

        :rtype: float
        """

        return self._b

    @b.setter
    def b(self, value: float) -> None:
        """
        Sets the peak ``b`` of this triangular modifier's membership function. The provided value is stored directly in the private ``_b`` attribute; the ``a <= b <= c`` ordering is not re-validated here.

        :param value: The new peak ``b``.
        :type value: float
        """

        self._b = value

    @property
    def c(self) -> float:
        """
        Returns the right endpoint of this triangular modifier's membership function, i.e. the upper bound where the membership degree falls back to zero. The value is read from the private ``_c`` attribute without modifying the instance.

        :return: The right endpoint ``c`` of the triangle.

        :rtype: float
        """

        return self._c

    @c.setter
    def c(self, value: float) -> None:
        """
        Sets the right endpoint ``c`` of this triangular modifier's membership function. The provided value is stored directly in the private ``_c`` attribute; the ``a <= b <= c`` ordering is not re-validated here.

        :param value: The new right endpoint ``c``.
        :type value: float
        """

        self._c = value

    def clone(self) -> typing.Self:
        """
        Creates and returns a new instance of the class that is a copy of the current object. This method instantiates a new object using the current values of the `name`, `a`, `b`, and `c` attributes, ensuring that the returned modifier has the same configuration as the original. The operation has no side effects on the existing instance.

        :return: A new instance of the class with identical attributes to the current instance.

        :rtype: typing.Self
        """

        return TriangularModifier(self.name, self.a, self.b, self.c)

    def compute_name(self) -> str:
        """
        Generates a standardized string representation for the triangular modifier instance based on its defining parameters. The returned value follows the format 'triangular-modifier(a, b, c)', incorporating the current values of the instance's attributes a, b, and c. This method does not modify the object's state and is primarily useful for logging, debugging, or identifying specific modifier configurations.

        :return: A string representing the name of the triangular modifier, formatted with the values of a, b, and c.

        :rtype: str
        """

        return f"triangular-modifier({self.a}, {self.b}, {self.c})"

    def get_membership_degree(self, x: float) -> float:
        """
        Calculates the degree of membership for a given input value x within a triangular fuzzy set defined by the parameters a, b, and c. The function returns 0.0 if the input lies outside the interval [a, c]. For values between a and the peak b, the membership increases linearly, while values between b and c result in a linear decrease. This method performs a pure calculation without modifying internal state or causing side effects.

        :param x: The input value for which to calculate the membership degree.
        :type x: float

        :return: The degree of membership of the input value x to the fuzzy set, ranging from 0.0 (no membership) to 1.0 (full membership).

        :rtype: float
        """

        if x <= self.a or x >= self.c:
            return 0.0
        if x <= self.b:
            return (x - self.a) / (self.b - self.a)
        return (self.c - x) / (self.c - self.b)

    def modify(self, concept: Concept) -> Concept:
        """
        Applies the triangular modification logic encapsulated by this instance to the provided concept. This method does not mutate the original concept directly; instead, it creates and returns a new `TriangularlyModifiedConcept` wrapper that combines the original concept with the current modifier. This allows the modified concept to be evaluated or processed with the specific triangular characteristics defined by the modifier.

        :param concept: The concept to be modified.
        :type concept: Concept

        :return: A new Concept instance that wraps the provided concept and applies a triangular modification using the current object.

        :rtype: Concept
        """

        return TriangularlyModifiedConcept(concept, self)

    def __neg__(self) -> Concept:
        """
        Implements the unary negation operator, enabling the use of the minus sign to invert the logic of the triangular modifier. This method returns a new `Concept` instance representing the logical complement of the current modifier by delegating to `OperatorConcept.not_`. The operation is non-destructive, leaving the original modifier unchanged while generating a distinct conceptual entity that encapsulates the negation.

        :return: A Concept representing the logical negation of the current instance.

        :rtype: Concept
        """

        return OperatorConcept.not_(self)

    def __and__(self, value: typing.Self) -> typing.Self:
        """
        Implements the bitwise AND operation (`&`) for the `TriangularModifier` class, enabling logical conjunction between the current instance and another of the same type. This method delegates the underlying logic to `OperatorConcept.and_` and returns a new `TriangularModifier` instance representing the combined result, ensuring that the operation does not modify the original operands in place.

        :param value: The right-hand operand for the AND operation, which must be an instance of the same class.
        :type value: typing.Self

        :return: The result of the AND operation between the current instance and the provided value.

        :rtype: typing.Self
        """

        return OperatorConcept.and_(self, value)

    def __or__(self, value: typing.Self) -> typing.Self:
        """
        Implements the bitwise OR operation using the pipe operator (`|`) to combine the current instance with another `TriangularModifier`. This method delegates the logic to `OperatorConcept.or_`, which calculates the union of the two modifiers based on the underlying concept definitions. It returns a new instance of `TriangularModifier` representing the combined result, ensuring that the original operands remain unmodified.

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
        return hash((self.name, self.a, self.b, self.c))

    # def __str__(self) -> str:
    #     return self.get_name()
