import typing

from fuzzy_dl_owl2.fuzzydl.degree.degree import Degree
from fuzzy_dl_owl2.fuzzydl.milp.expression import Expression
from fuzzy_dl_owl2.fuzzydl.milp.inequation import Inequation
from fuzzy_dl_owl2.fuzzydl.util.constants import InequalityType


class DegreeNumeric(Degree):
    """
    This concrete implementation of a degree encapsulates a specific numeric value, typically used to quantify the satisfaction level of a concept within a mathematical or logical model. Unlike abstract or symbolic degrees, this class stores a floating-point number that can be directly manipulated in arithmetic operations involving expressions and inequalities. Users can instantiate it directly with a float or utilize static factory methods such as `get_one` to retrieve standard values. The class provides utility methods to integrate the numeric value into larger expressions, perform comparisons, and generate inequality constraints based on the stored value.

    :param value: The underlying floating-point number representing the magnitude of the degree.
    :type value: float
    """


    def __init__(self, numeric: float) -> None:
        """
        Initializes the instance by converting the provided input to a floating-point number and assigning it to the `value` attribute. The constructor accepts any argument compatible with the standard Python `float` constructor, such as integers, floats, or numeric strings, ensuring the internal state is always stored as a float. If the input cannot be successfully converted, a `TypeError` or `ValueError` will be raised. This method modifies the instance state by setting the `value` attribute but does not produce any external side effects.

        :param numeric: The numeric value to initialize the instance with.
        :type numeric: float
        """

        self.value: float = float(numeric)

    @staticmethod
    def get_one() -> typing.Self:
        """
        Returns a new instance of `DegreeNumeric` representing the value 1.0. This static method acts as a factory to provide a consistent unit value without requiring an existing object instance. The operation has no side effects and simply constructs and returns the object.

        :return: Returns a new instance of the class representing the value one.

        :rtype: typing.Self
        """

        return DegreeNumeric(1.0)

    @staticmethod
    def get_degree(value: float) -> typing.Self:
        """
        Instantiates a new `DegreeNumeric` object using the provided float value. This static method serves as a factory function, allowing for the explicit conversion of a raw numeric value into the class's specific degree representation. The method delegates directly to the class constructor, meaning any validation or error handling is determined by the initialization logic of `DegreeNumeric`, and it produces no side effects other than the allocation of the new instance.

        :param value: The numeric value representing the angle in degrees.
        :type value: float

        :return: A new DegreeNumeric instance initialized with the provided value.

        :rtype: typing.Self
        """

        return DegreeNumeric(value)

    def clone(self) -> typing.Self:
        """
        Creates and returns a new instance of the class that replicates the current object's state. This is accomplished by extracting the internal numeric value and passing it to the class's factory method, `get_degree`. The method does not modify the original instance, ensuring that the returned object is a distinct copy, though the exact behavior relies on the implementation of the underlying factory method.

        :return: A new instance of the class with the same value as the current instance.

        :rtype: typing.Self
        """

        return DegreeNumeric.get_degree(self.value)

    def get_numerical_value(self) -> float:
        """
        Returns the underlying numeric value of the degree instance as a float. This method provides direct access to the internal `value` attribute without performing any calculations or modifications to the object state. It is a pure accessor function with no side effects.

        :return: The numerical value stored in the object.

        :rtype: float
        """

        return self.value

    def create_inequality_with_degree_rhs(
        self, expr: Expression, inequation_type: InequalityType
    ) -> Inequation:
        """
        Constructs an inequality object that compares the provided expression against the numeric degree value stored in the current instance. The method generates the inequality by subtracting the instance's value from the input expression, effectively positioning the degree value as the right-hand side of the comparison. The specific relational operator, such as less-than or greater-than, is determined by the `inequation_type` argument.

        :param expr: The algebraic expression representing the left-hand side of the inequality.
        :type expr: Expression
        :param inequation_type: Specifies the relational operator or type of the inequality relation (e.g., less than, greater than).
        :type inequation_type: InequalityType

        :return: An Inequation object representing the comparison between the provided expression and the degree value, using the specified inequality type.

        :rtype: Inequation
        """

        return Inequation(expr - 1.0 * self.value, inequation_type)

    def is_numeric(self) -> bool:
        """
        Returns a boolean value indicating that the current instance represents a numeric degree. This method serves as a type flag, allowing calling code to distinguish between numeric and non-numeric degree representations within a potentially polymorphic class hierarchy. Since this class specifically defines a numeric type, the method unconditionally returns True. The operation has no side effects.

        :return: True, indicating that the object is numeric.

        :rtype: bool
        """

        return True

    def add_to_expression(self, expr: Expression) -> Expression:
        """
        Adds the numeric value stored in the current instance to the provided expression. This operation combines the input expression with the instance's internal value using the addition operator, returning a new expression object that represents the result. The method does not modify the original expression or the instance itself, though it relies on the underlying compatibility between the expression type and the numeric value.

        :param expr: The expression to which the instance's value is added.
        :type expr: Expression

        :return: The Expression resulting from adding the instance's value to the input expression.

        :rtype: Expression
        """

        return expr + self.value

    def subtract_from_expression(self, expr: Expression) -> Expression:
        """
        Subtracts the numeric value stored in this instance from the given expression. This operation returns a new Expression object representing the result of the subtraction, ensuring that neither the input expression nor the current instance is mutated.

        :param expr: The expression from which the value is subtracted.
        :type expr: Expression

        :return: The resulting Expression after subtracting the current value from the provided expression.

        :rtype: Expression
        """

        return expr - self.value

    def multiply_constant(self, constant: float) -> Expression:
        """
        Multiplies the underlying numeric value of the instance by the specified floating-point constant and returns the result encapsulated in a new Expression object. This operation performs standard scalar multiplication without modifying the original instance, relying on the behavior of Python's floating-point arithmetic for the calculation.

        :param constant: The numeric value to multiply the expression's underlying value by.
        :type constant: float

        :return: A new Expression object representing the product of the current value and the provided constant.

        :rtype: Expression
        """

        return Expression(self.value * constant)

    def is_number_not_one(self) -> bool:
        """
        Determines whether the underlying numeric value of the instance is different from exactly 1.0. This method returns True if the value is not equal to 1.0 and False if it matches. It performs a direct comparison without modifying the object's state, meaning floating-point values that are close to but not exactly 1.0 will be considered different.

        :return: True if the value is not equal to 1.0, False otherwise.

        :rtype: bool
        """

        return self.value != 1.0

    def is_number_zero(self) -> bool:
        """
        Determines whether the underlying numeric value of the instance is exactly zero. This is achieved by performing a strict equality comparison between the instance's value attribute and the floating-point literal 0.0. Consequently, values that are extremely close to zero but not exactly equal to it will result in a return value of False. The method does not modify the state of the object.

        :return: True if the value is zero, False otherwise.

        :rtype: bool
        """

        return self.value == 0.0

    def __eq__(self, d: Degree) -> bool:
        """
        Checks for equality between the current instance and another object. The method returns True only if the provided argument is an instance of DegreeNumeric and its underlying numerical value matches the internal value of this instance. If the argument is of a different type or the numerical values do not align, the method returns False. This operation does not modify the state of either object.

        :param d: The `Degree` instance to compare with the current instance.
        :type d: Degree

        :return: True if the provided Degree object is a DegreeNumeric instance with the same numerical value as this instance, otherwise False.

        :rtype: bool
        """

        if isinstance(d, DegreeNumeric):
            return self.value == d.get_numerical_value()
        return False

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the `DegreeNumeric` instance, formatted to display the underlying numeric value. The output follows the pattern "Degree({value})", where {value} corresponds to the instance's `value` attribute. This method is implicitly invoked by the `str()` built-in and print functions, and it does not modify the object's state, though it requires the `value` attribute to be present.

        :return: A human-readable string representation of the object, formatted as "Degree(value)".

        :rtype: str
        """

        return f"Degree({self.value})"
