import typing
from abc import ABC, abstractmethod

from fuzzy_dl_owl2.fuzzydl.milp.expression import Expression
from fuzzy_dl_owl2.fuzzydl.milp.inequation import Inequation
from fuzzy_dl_owl2.fuzzydl.util.constants import InequalityType


class Degree(ABC):
    """
    This abstract base class defines the interface for a "degree," a metric used to quantify the extent to which a concept is satisfied by an individual. It provides a polymorphic mechanism to handle various underlying representations—such as raw numeric values, variables, or complex expressions—uniformly within a constraint or satisfaction system. Concrete implementations are typically instantiated via the static `get_degree` factory method, which determines the specific subclass based on the input type. The class exposes methods for arithmetic manipulation, such as adding to expressions or multiplying by constants, as well as utility functions to check for specific numeric states (like zero or one) and to generate inequalities where the degree serves as the right-hand side.

    :raises NotImplementedError: Raised when the `get_degree` method is called on the abstract base class `Degree`, as this method must be implemented by concrete subclasses to handle the creation of degree instances from input values.
    """


    @staticmethod
    @abstractmethod
    def get_degree(value) -> typing.Self:
        """
        Constructs an instance of the class from the provided value, acting as a factory method to convert raw input into a specific `Degree` object. As an abstract static method, it defines a required interface that subclasses must implement to handle the specific logic of value conversion, validation, or normalization. The method returns a new instance of the class type, and calling it directly on the base class will raise a `NotImplementedError`.

        :param value: The value used to calculate or determine the degree.
        :type value: typing.Any

        :raises NotImplementedError: Indicates that this method is abstract and must be overridden by a subclass, or that the functionality is not yet implemented.

        :return: The instance of the class.

        :rtype: typing.Self
        """

        raise NotImplementedError

    # @typing.overload
    # @staticmethod
    # def get_degree(value: float) -> typing.Self:
    #     return DegreeNumeric(value)

    # @typing.overload
    # @staticmethod
    # def get_degree(value: Variable) -> typing.Self:
    #     return DegreeVariable(value)

    # @typing.overload
    # @staticmethod
    # def get_degree(value: Expression) -> typing.Self:
    #     return DegreeExpression(value)

    @abstractmethod
    def clone(self) -> typing.Self:
        """
        Creates and returns a distinct copy of the current object, ensuring the returned instance is of the same concrete type as the original. As an abstract method, this function serves as a contract that requires subclasses to implement the specific logic for duplicating their internal state, typically resulting in a deep copy that is independent of the source. The operation should not modify the state of the original instance.

        :return: A new instance that is a copy of the current object.

        :rtype: typing.Self
        """

        pass

    @abstractmethod
    def is_numeric(self) -> bool:
        """
        Determines whether the degree instance represents a concrete numeric value rather than a symbolic expression or an undefined state. As an abstract method, it requires implementation by subclasses to define the specific criteria for what constitutes a numeric degree within the context of the derived type. The method returns True if the degree holds a specific number, and False if it is symbolic, variable-based, or otherwise non-numeric.

        :return: True if the object is numeric, False otherwise.

        :rtype: bool
        """

        pass

    @abstractmethod
    def create_inequality_with_degree_rhs(
        self,
        expression: Expression,
        inequation_type: InequalityType,
    ) -> Inequation:
        """
        Generates an inequality object where the provided expression forms the left-hand side and the degree represented by this instance forms the right-hand side. The specific comparison operator is determined by the supplied `InequalityType`, allowing for the creation of constraints such as 'expression < degree' or 'expression >= degree'. Since this is an abstract method, subclasses must provide the concrete implementation for how the degree is represented within the resulting `Inequation`.

        :param expression: The mathematical expression representing the right-hand side of the inequality.
        :type expression: Expression
        :param inequation_type: Specifies the type of inequality, defining the relational operator to be used between the expression and the right-hand side.
        :type inequation_type: InequalityType

        :return: Returns an Inequation object representing the specified inequality with the expression on the left and a degree value on the right.

        :rtype: Inequation
        """

        pass

    @abstractmethod
    def add_to_expression(self, expression: Expression) -> Expression:
        """
        Defines the contract for integrating the current degree instance into a symbolic expression. Subclasses must implement this method to specify the exact logic for how the degree value or unit is combined with the provided expression, ensuring type consistency and mathematical correctness. The method accepts an existing `Expression` and returns a modified or new `Expression` representing the outcome of the operation.

        :param expression: The expression to which the current object is added.
        :type expression: Expression

        :return: The Expression object representing the result of adding the current instance to the provided expression.

        :rtype: Expression
        """

        pass

    @abstractmethod
    def subtract_from_expression(self, expression: Expression) -> Expression:
        """
        Computes the result of subtracting the current degree instance from the provided expression. This abstract method serves as an interface for defining how a specific degree value or type acts as a subtrahend within a larger expression structure. Implementations are expected to return a new Expression object representing the calculated difference, ensuring that the original input expression remains unmodified.

        :param expression: The expression from which the current instance is subtracted.
        :type expression: Expression

        :return: An Expression representing the result of subtracting the current instance from the provided expression.

        :rtype: Expression
        """

        pass

    @abstractmethod
    def multiply_constant(self, double: float) -> Expression:
        """
        Multiplies the current mathematical entity by a scalar floating-point constant. This abstract method defines the interface for scaling operations, requiring subclasses to return a new `Expression` representing the product without modifying the original instance. Implementations should handle standard arithmetic edge cases, such as multiplication by zero resulting in a zero expression, ensuring the result remains consistent with the broader symbolic algebra system.

        :param double: The constant value to multiply the expression by.
        :type double: float

        :return: A new Expression representing the product of this expression and the provided constant.

        :rtype: Expression
        """

        pass

    @abstractmethod
    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the degree. As an abstract method, it serves as a contract that requires all concrete subclasses to define their own specific string formatting logic. This method is intended for display purposes and is invoked by the built-in `str()` function and print statements, ensuring that every degree type can be presented to the user in a consistent manner.

        :return: Return a string containing a nicely printable representation of the object.

        :rtype: str
        """

        pass

    @abstractmethod
    def __eq__(self, degree: typing.Self) -> bool:
        """
        Determines whether the current instance is semantically equivalent to another instance of the same type. As an abstract method, it requires subclasses to provide a concrete implementation that defines the specific criteria for equality, typically based on the internal value or state of the degree. The method should return True if the objects are considered equal and False otherwise, and it must handle comparisons with incompatible types by returning NotImplemented to ensure proper Python comparison protocol behavior. This operation is expected to be side-effect free, meaning it should not modify the state of either object involved in the comparison.

        :param degree: The other instance to compare for equality.
        :type degree: typing.Self

        :return: True if the two instances are equal, False otherwise.

        :rtype: bool
        """

        pass

    def __ne__(self, value: typing.Self) -> bool:
        """
        Determines whether the current `Degree` instance is not equal to the provided value. This method implements the behavior for the inequality operator (`!=`) by inverting the result of the equality comparison (`__eq__`). Consequently, its specific logic and handling of type mismatches depend entirely on the implementation of the `__eq__` method within the class.

        :param value: The object to compare against the current instance.
        :type value: typing.Self

        :return: True if the current instance is not equal to the provided value, otherwise False.

        :rtype: bool
        """

        return not (self == value)

    @abstractmethod
    def is_number_not_one(self) -> bool:
        """
        Checks whether the degree of the algebraic structure is not equal to one. As an abstract method, it requires implementation by subclasses to define the specific criteria for the degree. The method returns True if the degree differs from one, indicating a non-linear or specific non-unitary state, and False only when the degree is exactly one.

        :return: True if the number is not equal to 1, False otherwise.

        :rtype: bool
        """

        pass

    @abstractmethod
    def is_number_zero(self) -> bool:
        """
        Determines whether the numeric value associated with the degree instance is zero. As an abstract method, it mandates that subclasses provide the specific implementation for evaluating this condition, which may involve checking a specific attribute or handling floating-point precision. The method returns a boolean indicating the result of the zero-check without modifying the object's state.

        :return: True if the number is zero, False otherwise.

        :rtype: bool
        """

        pass

    def __repr__(self) -> str:
        """
        Returns a string representation of the `Degree` instance, intended for debugging and logging. This implementation delegates directly to the `__str__` method, ensuring that the output produced by the `repr()` function is identical to the standard string representation of the object.

        :return: A string representation of the object.

        :rtype: str
        """

        return str(self)
