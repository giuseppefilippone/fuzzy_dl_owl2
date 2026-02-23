from __future__ import annotations

import typing

from fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_concrete_concept import (
    FuzzyConcreteConcept,
)
from fuzzy_dl_owl2.fuzzydl.concept.operator_concept import OperatorConcept


class CrispConcreteConcept(FuzzyConcreteConcept):
    """
    This class models a crisp concrete concept within a fuzzy logic framework, implementing a binary membership function that distinguishes strictly between satisfaction and non-satisfaction. It is defined by a validity interval [k1, k2] representing the domain of the concept, and a nested satisfaction interval [a, b] where the concept holds true. When evaluating a specific value, the class returns a membership degree of 1.0 if the value falls within the satisfaction interval [a, b] and 0.0 otherwise. The initialization process includes validation logic to ensure that the satisfaction interval is valid and fully contained within the validity interval, raising a ValueError if these constraints are violated. Furthermore, the class supports logical operations such as negation, conjunction, and disjunction, allowing for the composition of complex concepts.

    :param k1: Lower bound of the definition interval [k1, k2], representing the minimum value for which the concept is valid.
    :type k1: float
    :param k2: The upper bound of the interval defining the domain of the concept.
    :type k2: float
    :param _a: Stores the lower bound of the interval for which the concept is satisfied, defining the start of the range where the membership degree is 1.
    :type _a: float
    :param _b: The upper bound of the interval for which the concept is satisfied.
    :type _b: float

    :raises ValueError: Raised when the satisfaction interval [a, b] is invalid or not contained within the definition interval [k1, k2]. This happens if a > b, a < k1, or b > k2.
    """


    def __init__(self, name: str, k1: float, k2: float, a: float, b: float) -> None:
        """
        Initializes a new instance with a specific name and interval boundaries defined by the provided parameters. The parameters `k1` and `k2` represent the global domain limits, while `a` and `b` define the specific interval for this concept. The constructor validates that the interval is well-formed and contained within the domain, ensuring that `a` is less than or equal to `b`, `a` is greater than or equal to `k1`, and `b` is less than or equal to `k2`. If any of these constraints are violated, a `ValueError` is raised. Upon successful validation, the boundaries are stored as floating-point attributes on the instance.

        :param name: The identifier or label for the object instance.
        :type name: str
        :param k1: The absolute lower bound of the domain, defining the minimum value that the specific lower bound `a` can take.
        :type k1: float
        :param k2: The upper bound of the domain or support, which must be greater than or equal to the upper limit `b`.
        :type k2: float
        :param a: The lower bound of the interval, which must be greater than or equal to k1 and less than or equal to b.
        :type a: float
        :param b: The upper bound of the interval, constrained to be greater than or equal to `a` and less than or equal to `k2`.
        :type b: float

        :raises ValueError: Raised if the provided bounds `a` and `b` are invalid, specifically when `a` is greater than `b`, `a` is less than `k1`, or `b` is greater than `k2`.
        """

        super().__init__(name)

        if a > b:
            raise ValueError(
                f"The lower bound a = {a} must be less than or equal to the upper bound b = {b}."
            )
        if a < k1:
            raise ValueError(
                f"The lower bound a = {a} must be greater than or equal to the lower bound k1 = {k1}."
            )
        if b > k2:
            raise ValueError(
                f"The upper bound b = {b} must be less than or equal to the upper bound k2 = {k2}."
            )

        self.k1: float = float(k1)
        self.k2: float = float(k2)
        self._a: float = float(a)
        self._b: float = float(b)

    @property
    def a(self) -> float:
        """
        This setter method updates the value of the property 'a' for the instance. It assigns the provided floating-point value to the internal attribute `_a`, modifying the object's internal state. While the type hint suggests the input should be a float, the implementation performs no validation, meaning any type of value can be stored.

        :param value: The new floating-point value to assign to the internal attribute.
        :type value: float
        """

        return self._a

    @a.setter
    def a(self, value: float) -> None:
        self._a = value

    @property
    def b(self) -> float:
        """
        Updates the value of the attribute 'b' for the `CrispConcreteConcept` instance by assigning the provided floating-point number to the internal backing field `_b`. This method mutates the state of the object, potentially influencing any subsequent calculations or logic that relies on this specific property. While the signature indicates a float input, the implementation performs no explicit validation, meaning that passing incompatible types may lead to errors in later operations that expect a numeric value.

        :param value: The new value to assign to the b attribute.
        :type value: float
        """

        return self._b

    @b.setter
    def b(self, value: float) -> None:
        self._b = value

    def clone(self) -> typing.Self:
        """
        Creates and returns a distinct copy of the current `CrispConcreteConcept` instance. The new object is initialized with the same values for `name`, `k1`, `k2`, `a`, and `b` as the original. This operation has no side effects on the source object, ensuring that modifications to the clone do not affect the original instance.

        :return: A new instance of the class initialized with the same attribute values as the current instance.

        :rtype: typing.Self
        """

        return CrispConcreteConcept(self.name, self.k1, self.k2, self.a, self.b)

    def get_membership_degree(self, x: float) -> float:
        """
        Calculates the membership degree of a specific value within the context of this crisp concept. The membership is determined by checking if the input value falls within the closed interval defined by the concept's lower and upper bounds. If the value lies between these bounds (inclusive), the method returns 1.0 to signify full membership; otherwise, it returns 0.0. This method does not modify the state of the object.

        :param x: The input value to evaluate for membership.
        :type x: float

        :return: The degree of membership of the input value, returning 1.0 if it lies within the interval [a, b] and 0.0 otherwise.

        :rtype: float
        """

        if self.a <= x <= self.b:
            return 1.0
        return 0.0

    def compute_name(self) -> str:
        """
        Generates a standardized string identifier for the concept instance by interpolating its internal parameters into a specific format. The returned string follows the pattern "crisp(k1, k2, a, b)", where the placeholders are replaced by the string representations of the corresponding attributes `k1`, `k2`, `a`, and `b`. This method performs a read-only operation and does not modify the object's state, though the resulting string's content is dependent on the `__str__` implementation of the stored parameter values.

        :return: A string representation of the object's configuration in the format 'crisp(k1, k2, a, b)'.

        :rtype: str
        """

        return f"crisp({self.k1}, {self.k2}, {self.a}, {self.b})"

    def __neg__(self) -> FuzzyConcreteConcept:
        """
        Implements the unary negation operator to compute the logical complement of the concept. This operation delegates to `OperatorConcept.not_` to generate a new representation of the negated concept. The result is returned as a `FuzzyConcreteConcept`, indicating that the negation of a crisp concept is handled within the fuzzy logic framework, potentially promoting the type to accommodate degrees of truth or standardizing the output of logical operations. This method does not modify the current instance in place.

        :return: The logical negation of the current concept.

        :rtype: FuzzyConcreteConcept
        """

        return OperatorConcept.not_(self)

    def __and__(self, value: typing.Self) -> typing.Self:
        """
        Performs a logical conjunction or intersection between the current instance and another concept of the same type. This method enables the use of the bitwise AND operator (`&`) to combine concepts, delegating the underlying logic to the `OperatorConcept.and_` static method. It returns a new instance of the same class representing the result of the operation, leaving the original operands unchanged.

        :param value: The right-hand operand to perform the AND operation with.
        :type value: typing.Self

        :return: A new instance representing the logical conjunction of this concept and the provided value.

        :rtype: typing.Self
        """

        return OperatorConcept.and_(self, value)

    def __or__(self, value: typing.Self) -> typing.Self:
        """
        Performs a logical disjunction between the current concept and another value of the same type, enabling the use of the bitwise OR operator (`|`). This operation returns a new instance representing the union or combination of the two operands, with the specific calculation logic delegated to the `OperatorConcept.or_` method. The method expects the input value to be compatible with the current instance type to ensure the operation is valid.

        :param value: Another instance of the same type to combine with the current instance using the OR operation.
        :type value: typing.Self

        :return: The result of the OR operation between this instance and the provided value.

        :rtype: typing.Self
        """

        return OperatorConcept.or_(self, value)

    def __hash__(self) -> int:
        """
        Returns the hash value of the object by computing the hash of its string representation. This implementation delegates the hashing logic to the result of `str(self)`, ensuring that the hash is derived from the object's textual form. Consequently, the object is hashable and can be used in collections like dictionaries and sets, though care must be taken if the string representation is mutable, as changing it would alter the hash value.

        :return: An integer representing the hash of the object's string representation.

        :rtype: int
        """

        return hash(str(self))

    # def __str__(self) -> str:
    #     return self.get_name()
