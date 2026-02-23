from __future__ import annotations

import typing

from fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_concrete_concept import (
    FuzzyConcreteConcept,
)
from fuzzy_dl_owl2.fuzzydl.concept.operator_concept import OperatorConcept
from fuzzy_dl_owl2.fuzzydl.exception.fuzzy_ontology_exception import (
    FuzzyOntologyException,
)


class TriangularConcreteConcept(FuzzyConcreteConcept):
    """
    This class implements a fuzzy logic concept characterized by a triangular membership function, defining how strongly a specific value belongs to the concept. It operates within a defined domain interval `[k1, k2]` and establishes a core satisfaction interval `[a, c]`, where the membership degree rises linearly from the lower bound `a` to a peak of 1.0 at `b`, then decreases linearly to the upper bound `c`. Users can instantiate this class with specific boundary parameters to model linguistic variables or fuzzy sets, and subsequently evaluate the membership degree of any given numeric value using the `get_membership_degree` method. The class enforces strict validation to ensure the parameters form a valid triangle and that the definition interval encompasses the satisfaction interval, raising an exception if these constraints are violated.

    :param k1: The lower bound of the domain interval [k1, k2] over which the concept is defined.
    :type k1: float
    :param k2: The upper bound of the domain interval [k1, k2] for which the concept is defined.
    :type k2: float
    :param _a: The lower bound of the support interval for the triangular membership function, representing the point where the membership degree begins to increase from zero.
    :type _a: float
    :param _b: The peak value of the triangular membership function where the concept is fully satisfied, corresponding to a membership degree of 1.
    :type _b: float
    :param _c: The upper bound of the interval for which the concept is satisfied, representing the point where the membership degree drops to zero. It must be greater than or equal to the peak value b.
    :type _c: float

    :raises FuzzyOntologyException: Raised if the provided parameters do not satisfy the constraints for a valid triangular function, specifically if the satisfaction interval bounds are not ordered ($a \le b \le c$) or if the definition interval $[k_1, k_2]$ does not fully encompass the satisfaction interval $[a, c]$ (i.e., $k_1 > a$ or $k_2 < c$).
    """


    def __init__(
        self, name: str, k1: float, k2: float, a: float, b: float, c: float
    ) -> None:
        """
        Initializes a new instance representing a triangular fuzzy concept with the specified name and parameters. The method validates the geometric constraints of the triangle, ensuring that the defining points satisfy $a \le b \le c$. Additionally, it enforces that the lower boundary $k1$ is less than or equal to $a$ and the upper boundary $k2$ is greater than or equal to $c$. If any of these conditions are violated, a `FuzzyOntologyException` is raised. Upon successful validation, the method stores these values as instance attributes, converting the triangle vertices to floats, and invokes the parent class initializer to set the concept's name.

        :param name: Identifier for the triangular fuzzy set instance.
        :type name: str
        :param k1: Lower bound of the domain, which must be less than or equal to the start of the triangular support (a).
        :type k1: float
        :param k2: Upper bound of the domain, defining the maximum valid value for the function, which must be greater than or equal to the upper support bound `c`.
        :type k2: float
        :param a: The lower bound of the triangular function, representing the x-coordinate where the membership value begins to rise. It must satisfy $k1 \le a \le b$.
        :type a: float
        :param b: The peak value of the triangular membership function.
        :type b: float
        :param c: The upper bound of the triangular support, representing the rightmost point where the membership value returns to zero.
        :type c: float

        :raises FuzzyOntologyException: Raised if the provided parameters violate the constraints required for a triangular function, specifically if the vertices are not ordered ($a \le b \le c$), the lower bound $k1$ exceeds $a$, or the upper bound $k2$ is less than $c$.
        """

        super().__init__(name)
        if not (a <= b <= c):
            raise FuzzyOntologyException(
                f"Error: Triangular functions require {a} <= {b} <= {c}"
            )
        if k1 > a:
            raise FuzzyOntologyException(
                f"Error: Triangular functions require {k1} <= {a}"
            )
        if k2 < c:
            raise FuzzyOntologyException(
                f"Error: Triangular functions require {k2} >= {c}"
            )

        self.k1: float = k1
        self.k2: float = k2
        self._a: float = float(a)
        self._b: float = float(b)
        self._c: float = float(c)

    @property
    def a(self) -> float:
        """
        Sets the value of the property 'a' for the TriangularConcreteConcept instance. The provided value is converted to a float and stored in the private attribute `_a`, ensuring that the internal representation is always a floating-point number. This method will raise an exception if the input cannot be cast to a float.

        :param value: The new value to assign to the attribute, converted to a float.
        :type value: float
        """

        return self._a

    @a.setter
    def a(self, value: float) -> None:
        self._a = float(value)

    @property
    def b(self) -> float:
        """
        Updates the internal state of the instance by setting the value of the property 'b'. The method accepts a single argument, which is explicitly converted to a float before being assigned to the private attribute '_b'. This conversion ensures type consistency, though it may raise a ValueError or TypeError if the provided input cannot be parsed as a float.

        :param value: The new value to be stored, converted to a float.
        :type value: float
        """

        return self._b

    @b.setter
    def b(self, value: float) -> None:
        self._b = float(value)

    @property
    def c(self) -> float:
        """
        Sets the value of the property 'c' for the triangular concept instance. This method accepts a numeric input, coerces it to a float, and assigns it to the internal `_c` attribute. It modifies the object's state and may raise an exception if the input cannot be successfully converted to a floating-point number.

        :param value: The new value for the attribute, converted to a float.
        :type value: float
        """

        return self._c

    @c.setter
    def c(self, value: float) -> None:
        self._c = float(value)

    def clone(self) -> typing.Self:
        """
        Creates and returns a distinct copy of the current `TriangularConcreteConcept` instance. The new object is instantiated with the exact same values for the `name`, `k1`, `k2`, `a`, `b`, and `c` attributes as the original. This operation does not modify the state of the existing object, ensuring that the original and the clone are independent entities.

        :return: A new instance of the class initialized with the same attributes as the current object.

        :rtype: typing.Self
        """

        return TriangularConcreteConcept(
            self.name, self.k1, self.k2, self.a, self.b, self.c
        )

    def get_membership_degree(self, x: float) -> float:
        """
        Calculates the membership degree of a specific value `x` within the triangular fuzzy set represented by this concept. The membership is determined by the relative position of `x` between the three defining parameters `a` (start), `b` (peak), and `c` (end). If `x` lies outside the interval $[a, c]$, the method returns 0.0. For values in the rising interval between `a` and `b`, the result is a linear interpolation from 0.0 to 1.0, while values in the falling interval between `b` and `c` yield a linear interpolation from 1.0 back to 0.0. This method performs a pure calculation without modifying the object's state.

        :param x: The input value for which the membership degree is calculated.
        :type x: float

        :return: The degree of membership of `x` in the triangular fuzzy set, ranging from 0.0 (no membership) to 1.0 (full membership).

        :rtype: float
        """

        if x <= self.a or x >= self.c:
            return 0.0
        if x <= self.b:
            return (x - self.a) / (self.b - self.a)
        return (self.c - x) / (self.c - self.b)

    def compute_name(self) -> str:
        """
        Generates a standardized string identifier for the triangular concept based on its current configuration. This method formats the instance attributes `k1`, `k2`, `a`, `b`, and `c` into a string that mimics a function invocation syntax. The operation is read-only and produces a unique textual representation of the object's parameters without causing any side effects.

        :return: A string representing the name of the triangular distribution, formatted with its parameters.

        :rtype: str
        """

        return f"triangular({self.k1}, {self.k2}, {self.a}, {self.b}, {self.c})"

    def __neg__(self) -> FuzzyConcreteConcept:
        """
        Implements the unary negation operator to compute the logical complement of the current triangular concept. This method delegates the operation to `OperatorConcept.not_`, effectively inverting the membership function associated with the instance. It returns a new `FuzzyConcreteConcept` representing the negated value without modifying the original object.

        :return: The logical negation of the concept.

        :rtype: FuzzyConcreteConcept
        """

        return OperatorConcept.not_(self)

    def __and__(self, value: typing.Self) -> typing.Self:
        """
        Implements the bitwise or logical AND operation for the class, allowing instances to be combined using the `&` operator. This method accepts another instance of the same type and delegates the calculation to the `OperatorConcept.and_` method to determine the result. The operation returns a new instance of the same type, representing the conjunction of the current instance and the provided value.

        :param value: The right-hand operand to perform the AND operation with.
        :type value: typing.Self

        :return: The result of the AND operation between this instance and the provided value.

        :rtype: typing.Self
        """

        return OperatorConcept.and_(self, value)

    def __or__(self, value: typing.Self) -> typing.Self:
        """
        Implements the bitwise OR operator (`|`) to perform a logical disjunction between the current instance and another `TriangularConcreteConcept`. This method accepts a value of the same type and delegates the computation to the `or_` method of `OperatorConcept`. It returns a new instance of `TriangularConcreteConcept` representing the result of the operation, without modifying the original operands.

        :param value: The right-hand operand for the OR operation, which must be an instance of the same class.
        :type value: typing.Self

        :return: The result of the OR operation between this instance and the provided value.

        :rtype: typing.Self
        """

        return OperatorConcept.or_(self, value)

    def __hash__(self) -> int:
        """
        Calculates a unique integer identifier for the instance based on its string representation. By delegating to the hash of the string form, this method ensures that objects with identical string outputs produce the same hash, thereby enabling the instance to be used as a dictionary key or stored within a set. It is important to note that the stability of the hash value is contingent upon the implementation of the `__str__` method; if the string representation changes, the hash will change as well.

        :return: An integer representing the hash of the object's string representation.

        :rtype: int
        """

        return hash(str(self))

    # def __str__(self) -> str:
    #     return self.get_name()
