from __future__ import annotations

import typing

from fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_concrete_concept import (
    FuzzyConcreteConcept,
)
from fuzzy_dl_owl2.fuzzydl.concept.operator_concept import OperatorConcept
from fuzzy_dl_owl2.fuzzydl.util.util import Util


class LinearConcreteConcept(FuzzyConcreteConcept):
    """
    This class models a fuzzy concept characterized by a piecewise linear membership function on the feature domain `[k1, k2]`. The function is defined by a "knee" point `(a, b)`, with `a` in the units of the feature and `b` the membership degree reached at `a`: a linear ramp from `(k1, 0)` to `(a, b)` and a second linear ramp from `(a, b)` to `(k2, 1)`. This is the same shape the MILP encoding of the concept enforces. Instantiate it with a name and the four float parameters, with `k1 < a < k2` and `0 <= b <= 1`; the membership degree of a value can then be retrieved with `get_membership_degree`, and the object supports the usual fuzzy operations (negation, conjunction, disjunction).

    :param k1: Lower bound of the feature domain; the membership degree is 0 at and below `k1`.
    :type k1: float
    :param k2: Upper bound of the feature domain; the membership degree is 1 at and above `k2`.
    :type k2: float
    :param _a: Abscissa of the knee, in feature units, strictly between `k1` and `k2`.
    :type _a: float
    :param _b: The membership degree at the knee `a`, in `[0, 1]`.
    :type _b: float
    """

    def __init__(self, name: str, k1: float, k2: float, a: float, b: float) -> None:
        """
        Initializes the instance with the feature domain `[k1, k2]` and the knee `(a, b)` of the piecewise linear membership function. The parameters are validated so that the two ramps are well defined: `k1 < k2`, `k1 < a < k2` (the degenerate knees `a == k1` and `a == k2` would make one ramp vertical and its slope undefined) and `0 <= b <= 1`. Violations are reported through the utility module. The values are stored as floats and the parent class is initialized with the provided name.

        :param name: Identifier for the instance.
        :type name: str
        :param k1: Lower bound of the feature domain, strictly less than `a`.
        :type k1: float
        :param k2: Upper bound of the feature domain, strictly greater than `a`.
        :type k2: float
        :param a: Abscissa of the knee, in feature units.
        :type a: float
        :param b: Membership degree at the knee, in `[0, 1]`.
        :type b: float
        """

        super().__init__(name)
        # Deliberate divergence from the Java oracle, which only checks k1 <= a and
        # b <= 1 and accepts the degenerate knees a == k1 / a == k2 (vertical ramp).
        # if k1 > a:
        #     Util.error(f"Error: Linear functions require {k1} <= {a}")
        # if b > 1.0:
        #     Util.error(f"Error: Linear functions require {b} <= 1.0")
        if k1 >= k2:
            Util.error(f"Error: Linear functions require {k1} < {k2}")
        if not (k1 < a < k2):
            Util.error(f"Error: Linear functions require {k1} < {a} < {k2}")
        if not (0.0 <= b <= 1.0):
            Util.error(f"Error: Linear functions require 0 <= {b} <= 1")

        self.k1: float = float(k1)
        self.k2: float = float(k2)
        self._a: float = float(a)
        self._b: float = float(b)

    @property
    def a(self) -> float:
        """
        Returns the x-coordinate of the knee of this piecewise-linear membership function, i.e. the threshold on the normalized domain at which the slope of the ramp changes. The value is held internally as a float and is read without modifying the instance.

        :return: The knee position ``a`` of the linear function.

        :rtype: float
        """

        return self._a

    @a.setter
    def a(self, value: float) -> None:
        """
        Sets the x-coordinate of the knee ``a`` of this piecewise-linear membership function. The provided value is cast to a float and stored in the private ``_a`` attribute; a non-convertible value raises a ``ValueError`` or ``TypeError``.

        :param value: The new knee position, converted to a float.
        :type value: float
        """

        self._a = float(value)

    @property
    def b(self) -> float:
        """
        Returns the membership degree reached at the knee ``a`` of this piecewise-linear function, i.e. the y-coordinate of the breakpoint that fixes the slope of the two linear segments. The value is held internally as a float and is read without modifying the instance.

        :return: The membership degree ``b`` at the knee.

        :rtype: float
        """

        return self._b

    @b.setter
    def b(self, value: float) -> None:
        """
        Sets the membership degree ``b`` reached at the knee of this piecewise-linear function. The provided value is cast to a float and stored in the private ``_b`` attribute; a non-convertible value raises a ``ValueError`` or ``TypeError``.

        :param value: The new degree at the knee, converted to a float.
        :type value: float
        """

        self._b = float(value)

    def clone(self) -> typing.Self:
        """
        Creates and returns a new instance of the class that is a distinct copy of the current object. This method initializes the new instance using the values of the `name`, `k1`, `k2`, `a`, and `b` attributes from the original object. The operation does not modify the state of the existing instance, ensuring that the original and the clone are independent objects with identical initial data.

        :return: A new instance of the class initialized with the same attribute values as the current object.

        :rtype: typing.Self
        """

        return LinearConcreteConcept(self.name, self.k1, self.k2, self.a, self.b)

    def get_membership_degree(self, value: float) -> float:
        """
        Calculates the degree of membership of a feature value: 0.0 at and below `k1`, a linear ramp from `(k1, 0)` to the knee `(a, b)`, a second linear ramp from `(a, b)` to `(k2, 1)`, and 1.0 at and above `k2`. This is exactly the function the MILP encoding of the concept enforces, expressed in the units of the feature. This method does not modify the state of the object.

        :param value: The feature value to evaluate, in the units of the feature domain `[k1, k2]`.
        :type value: float

        :return: The calculated degree of membership for the input value, bounded between 0.0 and 1.0.

        :rtype: float
        """

        # Deliberate divergence from the Java oracle (which shares this defect):
        # the original compared the value with 0 and 1, i.e. treated it as already
        # normalised, while using `a` in feature units. The result was right only
        # for k1 = 0, k2 = 1. The MILP rows (see KnowledgeBase, linear concrete
        # concept equations) work in feature units: y=0 -> x_ass = b (x - k1)/(a - k1),
        # y=1 -> x_ass = b + (1 - b)(x - a)/(k2 - a); this is the same function.
        # if value <= 0:
        #     return 0.0
        # if value >= 1.0:
        #     return 1.0
        # if value <= self.a:
        #     return self.b / self.a * value
        # return (value * (1.0 - self.b) + (self.b - self.a)) / (1.0 - self.a)
        if value <= self.k1:
            return 0.0
        if value >= self.k2:
            return 1.0
        if value <= self.a:
            return self.b * (value - self.k1) / (self.a - self.k1)
        return self.b + (1.0 - self.b) * (value - self.a) / (self.k2 - self.a)

    def compute_name(self) -> str:
        """
        Constructs a descriptive name for the linear concept instance by interpolating its key parameters into a standardized string format. The method retrieves the values of `k1`, `k2`, `a`, and `b` from the instance state and returns them formatted as "linear(k1, k2, a, b)". This function is purely deterministic and has no side effects, relying solely on the current state of the object's attributes.

        :return: A string representation of the linear function formatted with the current parameters.

        :rtype: str
        """

        return f"linear({self.k1}, {self.k2}, {self.a}, {self.b})"

    def __neg__(self) -> FuzzyConcreteConcept:
        """
        Implements the unary negation operator, allowing the concept to be inverted using the `-` prefix. This method delegates the logic to `OperatorConcept.not_` to compute the logical complement of the current instance. The operation returns a new `FuzzyConcreteConcept` representing the negation, rather than modifying the original object.

        :return: A new FuzzyConcreteConcept representing the logical negation of the current concept.

        :rtype: FuzzyConcreteConcept
        """

        return OperatorConcept.not_(self)

    def __and__(self, value: typing.Self) -> typing.Self:
        """
        Computes the logical conjunction or intersection of the current concept with another instance of the same type. This method enables the use of the bitwise AND operator (`&`) to combine concepts, delegating the specific logic to the `OperatorConcept.and_` method. The operation returns a new instance representing the result, leaving the original operands unchanged.

        :param value: The right-hand operand for the AND operation, which must be an instance of the same type.
        :type value: typing.Self

        :return: The result of the AND operation between this instance and the provided value.

        :rtype: typing.Self
        """

        return OperatorConcept.and_(self, value)

    def __or__(self, value: typing.Self) -> typing.Self:
        """
        Performs a logical OR operation between the current concept and another concept of the same type. This method enables the use of the pipe operator (`|`) to combine concepts, delegating the underlying logic to the `OperatorConcept.or_` method. It returns a new instance representing the result of the operation, leaving the original operands unchanged.

        :param value: The right-hand operand to combine with the current instance using the OR operation.
        :type value: typing.Self

        :return: Returns a new instance representing the logical OR of this object and the provided value.

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
    #     return self.get_name()
