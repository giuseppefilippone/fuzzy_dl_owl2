from __future__ import annotations

import typing

from fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_concrete_concept import (
    FuzzyConcreteConcept,
)
from fuzzy_dl_owl2.fuzzydl.concept.operator_concept import OperatorConcept
from fuzzy_dl_owl2.fuzzydl.util.util import Util


class TrapezoidalConcreteConcept(FuzzyConcreteConcept):
    """
    This class represents a trapezoidal concrete concept within a fuzzy logic framework, defining a membership function that follows a trapezoidal shape. It is defined by a universe of discourse interval [k1, k2] and four shape parameters a, b, c, and d, which establish the support [a, d] and the core [b, c] of the concept. The membership degree is 0 for values less than or equal to a or greater than or equal to d, equals 1 for values between b and c, and transitions linearly for values in the intervals (a, b) and (c, d). To use this class, instantiate it with a descriptive name and the required float parameters, ensuring that the shape parameters adhere to the strict ordering a <= b <= c <= d and that the definition interval fully encompasses the support interval (k1 <= a and k2 >= d). The class provides functionality to calculate membership degrees, clone instances, and supports logical operations such as AND, OR, and NOT via operator overloading.

    :param name: Identifier for the concept, used for identification and debugging purposes.
    :type name: str
    :param k1: The lower bound of the interval [k1, k2] defining the domain over which the concept is defined.
    :type k1: float
    :param k2: The upper bound of the interval for which the concept is defined.
    :type k2: float
    :param _a: The lower bound of the support interval, marking the point where the membership degree begins to increase from zero.
    :type _a: float
    :param _b: The lower bound of the plateau region where the membership degree is 1.
    :type _b: float
    :param _c: The upper bound of the plateau where the membership degree is 1.
    :type _c: float
    :param _d: The upper bound of the interval for which the concept is satisfied, representing the point where the membership degree drops to zero.
    :type _d: float
    """


    def __init__(
        self, name: str, k1: float, k2: float, a: float, b: float, c: float, d: float
    ) -> None:
        """
        Initializes the trapezoidal concept with a specific name and geometric parameters defining its shape and domain. The method enforces strict ordering constraints on the trapezoid vertices, requiring $a \le b \le c \le d$, and ensures the domain limits $k1$ and $k2$ fully contain the trapezoid by mandating $k1 \le a$ and $k2 \ge d$. If these validation checks fail, an error is triggered. Upon successful validation, the parameters are stored as instance attributes, with the vertex coordinates explicitly cast to floating-point numbers, and the parent class constructor is invoked.

        :param name: Identifier for the trapezoidal function instance.
        :type name: str
        :param k1: Lower bound of the domain, required to be less than or equal to the start of the trapezoid (a).
        :type k1: float
        :param k2: Upper bound of the domain, which must be greater than or equal to the rightmost point of the trapezoid.
        :type k2: float
        :param a: The left-most x-coordinate defining the start of the trapezoidal shape, satisfying `k1 <= a <= b`.
        :type a: float
        :param b: The second point of the trapezoidal shape, marking the start of the plateau where the function reaches its maximum value. Must satisfy a <= b <= c.
        :type b: float
        :param c: The third point defining the trapezoidal shape, marking the end of the plateau where the function value begins to decrease.
        :type c: float
        :param d: The rightmost x-coordinate of the trapezoid, representing the point where the function returns to zero. Must be greater than or equal to c and less than or equal to k2.
        :type d: float
        """

        super().__init__(name)
        if not (a <= b <= c <= d):
            Util.error(f"Error: Trapezoidal functions require {a} <= {b} <= {c} <= {d}")
        if k1 > a:
            Util.error(f"Error: Trapezoidal functions require {k1} <= {a}")
        if k2 < d:
            Util.error(f"Error: Trapezoidal functions require {k2} >= {d}")

        self.name: str = name
        self.k1: float = k1
        self.k2: float = k2
        self._a: float = float(a)
        self._b: float = float(b)
        self._c: float = float(c)
        self._d: float = float(d)

    @property
    def a(self) -> float:
        """
        Sets the value of the property 'a', representing a specific geometric dimension of the trapezoidal concrete concept. The method accepts a numeric input, casts it to a float, and stores the result in the private attribute `_a`. This type conversion ensures that the internal state maintains floating-point precision for subsequent calculations, even if an integer or compatible numeric type is provided.

        :param value: The value to assign to the attribute, converted to a float.
        :type value: float
        """

        return self._a

    @a.setter
    def a(self, value: float) -> None:
        self._a = float(value)

    @property
    def b(self) -> float:
        """
        Sets the dimension represented by 'b' for the trapezoidal concrete concept, typically corresponding to a width or base length. The method accepts a value, explicitly converts it to a float, and assigns it to the internal attribute `_b`. This ensures the underlying data type remains consistent, though providing a value that cannot be converted to a float will raise an error.

        :param value: The new value to assign to the b attribute.
        :type value: float
        """

        return self._b

    @b.setter
    def b(self, value: float) -> None:
        self._b = float(value)

    @property
    def c(self) -> float:
        """
        Assigns the specified value to the property 'c', which corresponds to a geometric dimension of the trapezoidal concrete concept. The input is explicitly cast to a float to maintain numerical precision and stored in the private attribute `_c`. This setter modifies the object's state and may raise a TypeError or ValueError if the provided value cannot be converted to a float.

        :param value: The new value to assign to the property, converted to a float.
        :type value: float
        """

        return self._c

    @c.setter
    def c(self, value: float) -> None:
        self._c = float(value)

    @property
    def d(self) -> float:
        """
        Sets the depth dimension of the trapezoidal concrete concept. This method serves as the setter for the `d` property, converting the provided value to a float and storing it in the private `_d` attribute. While this ensures the internal state is always a float, passing a non-numeric value will result in a `ValueError` or `TypeError` during the conversion process.

        :param value: The numeric value to assign to the attribute, converted to a float.
        :type value: float
        """

        return self._d

    @d.setter
    def d(self, value: float) -> None:
        self._d = float(value)

    def clone(self) -> typing.Self:
        """
        Creates and returns a new instance that is an independent copy of the current object. The method instantiates a new object using the current values of the `name`, `k1`, `k2`, `a`, `b`, `c`, and `d` attributes. This operation has no side effects on the original instance, ensuring that modifications to the returned copy do not affect the source data.

        :return: A new instance of the class initialized with the same attribute values as the current object.

        :rtype: typing.Self
        """

        return TrapezoidalConcreteConcept(
            self.name, self.k1, self.k2, self.a, self.b, self.c, self.d
        )

    def get_membership_degree(self, x: float) -> float:
        """
        Computes the degree of membership for a given input value within a trapezoidal fuzzy set defined by the instance's boundary parameters. The function returns 0.0 if the input lies outside the range defined by the lower and upper bounds, and returns 1.0 if the input falls within the central plateau. For values located on the rising or falling edges of the trapezoid, the method performs linear interpolation to return a fractional membership value between 0.0 and 1.0. This calculation is stateless and does not modify the object's attributes.

        :param x: The input value to evaluate against the membership function.
        :type x: float

        :return: The degree of membership of the input value x, ranging from 0.0 to 1.0.

        :rtype: float
        """

        if x <= self.a or x >= self.d:
            return 0.0
        if self.b <= x <= self.c:
            return 1.0
        if x >= self.a:
            return (x - self.a) / (self.b - self.a)
        return (self.d - x) / (self.d - self.c)

    def compute_name(self) -> str:
        """
        Constructs a human-readable string identifier that encapsulates the specific parameters of the trapezoidal concept. The output is formatted as a function-like string containing the values of the six defining attributes—k1, k2, a, b, c, and d—enclosed in parentheses. This method relies on the existence of these instance attributes and will raise an error if any are undefined.

        :return: A string representation of the trapezoidal configuration with the current parameter values.

        :rtype: str
        """

        return (
            f"trapezoidal({self.k1}, {self.k2}, {self.a}, {self.b}, {self.c}, {self.d})"
        )

    def __neg__(self) -> FuzzyConcreteConcept:
        """
        Implements the unary negation operator for the trapezoidal fuzzy concept, returning a new concept that represents the logical complement of the current instance. This operation delegates the calculation to the `not_` method of the `OperatorConcept` class, effectively inverting the membership function. The method does not modify the original object but instead produces a new `FuzzyConcreteConcept` instance reflecting the negated state.

        :return: Returns the logical negation of the current concept.

        :rtype: FuzzyConcreteConcept
        """

        return OperatorConcept.not_(self)

    def __and__(self, value: typing.Self) -> typing.Self:
        """
        Performs a logical conjunction (AND) operation between the current instance and another instance of the same type, typically invoked via the `&` operator. The method delegates the core logic to the `OperatorConcept.and_` function, returning a new instance that represents the result while leaving the original operands unchanged.

        :param value: The right-hand operand to perform the AND operation with.
        :type value: typing.Self

        :return: The result of the AND operation between this instance and the provided value.

        :rtype: typing.Self
        """

        return OperatorConcept.and_(self, value)

    def __or__(self, value: typing.Self) -> typing.Self:
        """
        Implements the bitwise OR operation for the concept, allowing the use of the pipe operator (`|`) to combine two instances. This method delegates the logic to the `OperatorConcept.or_` method, which computes the logical disjunction between the current object and the provided value. It returns a new instance of the same type representing the result of the operation, leaving the original operands unchanged.

        :param value: The right-hand operand to combine with the current instance using the OR operator.
        :type value: typing.Self

        :return: The result of the OR operation between the current instance and the provided value.

        :rtype: typing.Self
        """

        return OperatorConcept.or_(self, value)

    def __hash__(self) -> int:
        """
        Computes the integer hash value for the instance, enabling its use as a key in dictionary lookups or membership in sets. The implementation derives the hash from the string representation of the object, meaning that two instances with identical string outputs will produce the same hash code. Because the hash is based on the string representation, the efficiency of this method is directly tied to the performance of the `__str__` method, and any mutation that alters the string output will result in a different hash value.

        :return: An integer hash value derived from the string representation of the object.

        :rtype: int
        """

        return hash(str(self))

    # def __str__(self) -> str:
    #     return self.get_name()
