from __future__ import annotations

import typing

from fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_concrete_concept import (
    FuzzyConcreteConcept,
)
from fuzzy_dl_owl2.fuzzydl.concept.operator_concept import OperatorConcept
from fuzzy_dl_owl2.fuzzydl.util.util import Util


class LinearConcreteConcept(FuzzyConcreteConcept):
    """
    This class models a fuzzy concept characterized by a piecewise linear membership function operating on a normalized domain from 0 to 1. The function is defined by a specific "knee" point determined by parameters `a` and `b`, creating a linear ramp from (0, 0) to (a, b) and a second linear ramp from (a, b) to (1, 1). While the constructor accepts parameters `k1` and `k2` to denote the definition interval, the membership calculation logic strictly relies on the normalized input value and the `a` and `b` parameters. To use this class, instantiate it with a name and the required float parameters, ensuring that `k1` is less than or equal to `a` and `b` does not exceed 1.0 to avoid validation errors. Once instantiated, the membership degree of a specific value can be retrieved using the `get_membership_degree` method, and the object supports standard fuzzy logic operations such as negation, conjunction, and disjunction.

    :param k1: Lower bound of the interval for which the concept is defined.
    :type k1: float
    :param k2: The upper bound of the interval for which the concept is defined.
    :type k2: float
    :param _a: The lower bound of the interval for which the concept is satisfied, acting as a threshold in the piecewise linear membership function.
    :type _a: float
    :param _b: The membership degree at the threshold `a`, defining the slope of the linear membership function. Must be less than or equal to 1.0.
    :type _b: float
    """


    def __init__(self, name: str, k1: float, k2: float, a: float, b: float) -> None:
        """
        Initializes the instance by setting up the defining parameters for a linear concrete concept. This constructor accepts a string identifier and four numerical coefficients (k1, k2, a, b) that govern the linear behavior. It enforces specific constraints to ensure mathematical validity: the value of k1 must not exceed a, and the value of b must be less than or equal to 1.0. If these constraints are violated, the method triggers an error via the utility module. Upon successful validation, the parameters are converted to floats and stored as instance attributes, and the parent class is initialized with the provided name.

        :param name: Identifier for the instance.
        :type name: str
        :param k1: The first coefficient or constant value for the linear function, which must be less than or equal to 'a'.
        :type k1: float
        :param k2: The second coefficient or slope parameter for the linear function.
        :type k2: float
        :param a: Upper bound for the parameter k1.
        :type a: float
        :param b: A coefficient used in the linear function definition, constrained to be less than or equal to 1.0.
        :type b: float
        """

        super().__init__(name)
        if k1 > a:
            Util.error(f"Error: Linear functions require {k1} <= {a}")
        if b > 1.0:
            Util.error(f"Error: Linear functions require {b} <= 1.0")

        self.k1: float = float(k1)
        self.k2: float = float(k2)
        self._a: float = float(a)
        self._b: float = float(b)

    @property
    def a(self) -> float:
        """
        Sets the value of the coefficient 'a' for the linear concept. This method accepts a value, converts it to a float, and assigns it to the internal attribute `_a`. It ensures type consistency by forcing the storage format to be a float, which may raise a `ValueError` or `TypeError` if the input is not a valid number. Modifying this property updates the internal state of the object, which may influence subsequent calculations or behaviors relying on this coefficient.

        :param value: The new value to assign to the internal attribute, converted to a float.
        :type value: float
        """

        return self._a

    @a.setter
    def a(self, value: float) -> None:
        self._a = float(value)

    @property
    def b(self) -> float:
        """
        Updates the internal state of the instance by assigning a new value to the underlying attribute. The input is coerced to a floating-point number before storage to ensure type consistency, regardless of whether the original input was an integer or a numeric string. This setter modifies the private attribute `_b` and will propagate standard exceptions if the provided value cannot be converted to a float.

        :param value: The new value for the 'b' attribute, converted to a float.
        :type value: float
        """

        return self._b

    @b.setter
    def b(self, value: float) -> None:
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
        Calculates the degree of membership for a given input value based on a piecewise linear function defined by the concept's parameters. The input is treated as a normalized value, where any input less than or equal to zero results in a membership of 0.0, and any input greater than or equal to one results in a membership of 1.0. Between zero and the internal threshold `self.a`, the membership increases linearly from 0.0 to `self.b`. For values between `self.a` and 1.0, the membership increases linearly from `self.b` to 1.0. This method does not modify the state of the object.

        :param value: The input value to evaluate against the membership function. Values less than or equal to 0 return 0, and values greater than or equal to 1 return 1.
        :type value: float

        :return: The calculated degree of membership for the input value, bounded between 0.0 and 1.0.

        :rtype: float
        """

        if value <= 0:
            return 0.0
        if value >= 1.0:
            return 1.0
        if value <= self.a:
            return self.b / self.a * value
        return (value * (1.0 - self.b) + (self.b - self.a)) / (1.0 - self.a)

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
        Computes the hash value for the instance based on its string representation, enabling the object to be used as a key in dictionaries or as a member of sets. The implementation delegates to the built-in hash function applied to the result of `str(self)`, meaning the hash value is intrinsically linked to the object's string output. Consequently, if the object is mutable and its string representation changes during its lifetime, the hash value will also change, which violates the standard contract for hashable objects and can lead to errors if the instance is used as a dictionary key after modification. Furthermore, the efficiency of this operation depends on the computational cost of generating the string representation.

        :return: An integer hash value computed from the string representation of the object.

        :rtype: int
        """

        return hash(str(self))

    # def __str__(self) -> str:
    #     return self.get_name()
