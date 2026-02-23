import typing

from fuzzy_dl_owl2.fuzzydl.milp.variable import Variable
from fuzzy_dl_owl2.fuzzydl.util import constants


class Term:
    """
    This class represents a fundamental component of a linear expression, defined as the product of a numerical coefficient and a variable. It is primarily utilized to construct mathematical representations of concept satisfaction degrees within fuzzy description logic ontologies. Instances can be initialized by providing both a coefficient and a variable, or by providing a variable alone, which automatically sets the coefficient to 1.0. The class supports standard arithmetic operations, including negation, addition, subtraction, and scalar multiplication or division; however, addition and subtraction operations are strictly constrained to terms that share the same variable, raising an error otherwise.

    :raises ValueError: Raised when attempting to add two terms with different variables.
    """


    @typing.overload
    def __init__(self, coeff: float, var: Variable) -> None: ...

    @typing.overload
    def __init__(self, var: Variable) -> None: ...

    def __init__(self, *args) -> None:
        """
        Initializes a new Term instance, which represents an algebraic component consisting of a coefficient and a variable. The constructor accepts either one or two arguments to define the term's structure. If a single argument is provided, it must be a Variable instance, representing a term with an implied coefficient. If two arguments are provided, the first must be a numeric constant representing the coefficient, and the second must be a Variable instance. The method strictly validates the argument count and types, raising an AssertionError if the inputs do not match the expected patterns.

        :param args: Arguments defining the term, accepted as either a single Variable or a numeric coefficient followed by a Variable.
        :type args: typing.Any
        """

        assert len(args) in [1, 2]
        if len(args) == 1:
            assert isinstance(args[0], Variable)
            self.__term_init_2(*args)
        else:
            assert isinstance(args[0], constants.NUMBER)
            assert isinstance(args[1], Variable)
            self.__term_init_1(*args)

    def __term_init_1(self, coeff: typing.Union[int, float], var: Variable) -> None:
        """
        Initializes the Term instance by assigning a specific coefficient and variable to the object's internal state. The method accepts a numeric coefficient, which may be an integer or a float, and a Variable object, storing them in the `coeff` and `var` attributes respectively. This operation directly modifies the instance, effectively defining the term's value and associated variable without performing additional validation or calculation.

        :param coeff: The numeric coefficient multiplying the variable.
        :type coeff: typing.Union[int, float]
        :param var: The variable component of the term.
        :type var: Variable
        """

        self.var: Variable = var
        self.coeff: float = coeff

    def __term_init_2(self, var: Variable) -> None:
        """
        Initializes the Term object by setting its coefficient to 1.0 and associating it with the provided Variable. This helper method delegates the core assignment logic to `__term_init_1`, effectively constructing a term that represents the variable itself without an explicit multiplicative factor. As this method modifies the instance's internal state, it relies on `__term_init_1` to handle any validation or type checking for the variable argument.

        :param var: The Variable instance representing the variable part of the term.
        :type var: Variable
        """

        self.__term_init_1(1.0, var)

    def clone(self) -> typing.Self:
        """
        Creates and returns a distinct copy of the current `Term` instance. The new object is constructed using the same coefficient and variable values as the original, ensuring that subsequent modifications to the clone do not affect the source object. This method provides a way to duplicate the term's state for independent operations.

        :return: A new instance of the class with the same coefficient and variable as the current instance.

        :rtype: typing.Self
        """

        return Term(self.coeff, self.var)

    def get_var(self) -> Variable:
        """
        Retrieves the `Variable` instance associated with this `Term`. This method serves as a simple accessor, returning the value of the internal `var` attribute without modifying the state of the object. It provides direct access to the variable component that defines or is linked to the current term.

        :return: Returns the `Variable` instance stored in the `var` attribute.

        :rtype: Variable
        """

        return self.var

    def get_coeff(self) -> float:
        """
        Retrieves the numerical coefficient associated with the term. This method serves as a simple accessor that returns the value stored in the internal `coeff` attribute without modifying the object's state. The returned value represents the scalar multiplier of the term and is expected to be a floating-point number.

        :return: The value of the coefficient.

        :rtype: float
        """

        return self.coeff

    def clone(self) -> typing.Self:
        return Term(self.coeff, self.var)

    def __neg__(self) -> typing.Self:
        """
        Implements the unary negation operator for the Term instance. This method returns a new Term object with the same variable component as the original but with its coefficient multiplied by -1. The operation is non-destructive, leaving the original Term unmodified.

        :return: A new Term instance representing the arithmetic negation of the current term.

        :rtype: typing.Self
        """

        return Term(-self.coeff, self.var)

    def __add__(self, term: typing.Self) -> typing.Self:
        """
        Combines the current instance with another `Term` instance by summing their coefficients, provided that both terms share the same variable. If the variables differ, a `ValueError` is raised to indicate that unlike terms cannot be combined. The operation returns a new `Term` object without modifying the original operands.

        :param term: The term to add to the current instance. It must have the same variable as the current instance.
        :type term: typing.Self

        :raises ValueError: Raised when attempting to add terms with different variables.

        :return: A new Term instance with the variable unchanged and the coefficient equal to the sum of the operands' coefficients.

        :rtype: typing.Self
        """

        if self.var != term.var:
            raise ValueError("Cannot add terms with different variables")
        return Term(self.coeff + term.coeff, self.var)

    def __sub__(self, term: typing.Self) -> typing.Self:
        """
        Returns a new Term instance representing the arithmetic difference between the current instance and the provided Term. The operation is performed by adding the negation of the specified term to the current instance, effectively delegating the logic to the `__add__` and `__neg__` methods. This method does not modify the original objects in place.

        :param term: The value to subtract from the current instance.
        :type term: typing.Self

        :return: The result of subtracting the provided term from the current instance.

        :rtype: typing.Self
        """

        return self + (-term)

    def __mul__(self, scalar: float) -> typing.Self:
        """
        Performs scalar multiplication on the term, returning a new instance with the scaled coefficient. The method multiplies the term's coefficient by the provided float value while leaving the variable component unchanged. This operation creates a distinct object, ensuring that the original term remains unmodified and no side effects occur on the existing state.

        :param scalar: The numeric factor by which to multiply the term's coefficient.
        :type scalar: float

        :return: A new Term instance with the coefficient scaled by the scalar.

        :rtype: typing.Self
        """

        return Term(self.coeff * scalar, self.var)

    def __rmul__(self, scalar: float) -> typing.Self:
        """
        Implements the reflected multiplication operation, enabling scalar multiplication when the scalar value appears on the left-hand side of the operator. This method delegates the actual computation to the standard multiplication logic, ensuring that the operation is commutative and consistent with left-hand multiplication. It returns a new instance of the Term representing the product, leaving the original object unmodified.

        :param scalar: The numeric value to multiply the instance by.
        :type scalar: float

        :return: The product of the scalar and this object.

        :rtype: typing.Self
        """

        return self * scalar

    def __truediv__(self, scalar: float) -> typing.Self:
        """
        Performs scalar division on the term using the forward slash operator. This operation is implemented by multiplying the term by the reciprocal of the provided scalar value, delegating the actual construction of the result to the multiplication logic. It returns a new instance of the `Term` class, ensuring the original object remains unmodified. A `ZeroDivisionError` will be raised if the input scalar is zero.

        :param scalar: The value to divide the instance by.
        :type scalar: float

        :return: A new instance of the same class representing the result of dividing the object by the specified scalar.

        :rtype: typing.Self
        """

        return self * (1 / scalar)

    def __eq__(self, term: typing.Self) -> bool:
        """
        Determines whether the current instance is equal to another object by first verifying that the provided argument is an instance of the `Term` class. If the argument is not a `Term`, the method returns False. When comparing against another `Term`, the method evaluates equality based on the `var` and `coeff` attributes, returning True only if both corresponding values are identical. This ensures that comparisons with incompatible types are handled gracefully without raising errors.

        :param term: The other instance to compare against for equality.
        :type term: typing.Self

        :return: True if the provided object is a Term instance with matching variable and coefficient, False otherwise.

        :rtype: bool
        """

        if not isinstance(term, Term):
            return False
        return self.var == term.var and self.coeff == term.coeff

    def __ne__(self, term: typing.Self) -> bool:
        """
        Determines whether the current term is not equal to the specified term. This method returns the logical negation of the equality comparison (`self == term`), meaning it returns `True` if the terms are different and `False` if they are the same. The specific logic for determining equality is delegated to the `__eq__` method, so any type checking or value comparison rules defined there apply here as well. This operation has no side effects on the object's state.

        :param term: The object to compare with the current instance.
        :type term: typing.Self

        :return: True if the current instance is not equal to the provided term, False otherwise.

        :rtype: bool
        """

        return not (self == term)

    def __hash__(self) -> int:
        """
        Computes the hash value for the `Term` instance, enabling its use as a key in dictionaries or as an element in sets. The implementation derives the hash from the string representation of the object, ensuring that two terms with identical string representations produce the same hash code. Because the hash is based on the result of `str(self)`, the object should be treated as immutable; if the object's state changes in a way that alters its string representation, the hash value will also change, which violates the contract required for hashable objects and can lead to errors when the object is used in hash-based collections.

        :return: An integer hash value computed from the string representation of the object.

        :rtype: int
        """

        return hash(str(self))

    def __repr__(self) -> str:
        """
        Returns a string representation of the Term instance. This implementation delegates directly to the `__str__` method, meaning the official representation is identical to the informal string representation. As a result, the output is primarily intended for readability and display rather than providing a machine-parseable expression to reconstruct the object.

        :return: A string representation of the object.

        :rtype: str
        """

        return str(self)

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the term, formatted as the coefficient multiplied by the variable. This method is automatically invoked by the `str()` built-in function and during string formatting operations. The output strictly follows the pattern "{coeff} * {var}" without performing algebraic simplification, meaning a coefficient of 1 will still be displayed explicitly. The method has no side effects and relies on the string representations of the underlying coefficient and variable attributes.

        :return: A string representation of the object formatted as "coeff * var".

        :rtype: str
        """

        return f"{self.coeff} * {self.var}"
