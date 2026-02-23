import typing

import trycast

from fuzzy_dl_owl2.fuzzydl.milp.term import Term
from fuzzy_dl_owl2.fuzzydl.milp.variable import Variable
from fuzzy_dl_owl2.fuzzydl.util import constants


class Expression:
    """
    This class models a linear mathematical expression of the form $c + c_1x_1 + \dots + c_nx_n$, typically used to represent the degree of satisfaction of a concept within a fuzzy description logic ontology. It offers flexible initialization options, allowing construction from a numeric constant, a sequence of `Term` objects, another `Expression` instance, or a collection of `Variable` objects. The class supports comprehensive arithmetic manipulation through operator overloading, enabling addition, subtraction, multiplication, and division with scalars, terms, or other expressions. Furthermore, it automatically manages term consolidation; if a term is added involving a variable that already exists, the coefficients are merged rather than creating a duplicate entry.

    :raises ValueError: 
    """


    @typing.overload
    def __init__(self, constant: constants.NUMBER) -> None: ...

    @typing.overload
    def __init__(self, constant: constants.NUMBER, *terms: Term) -> None: ...

    @typing.overload
    def __init__(self, *terms: Term) -> None: ...

    @typing.overload
    def __init__(self, expr: typing.Self) -> None: ...

    @typing.overload
    def __init__(self, v: typing.Union[list[Variable], set[Variable]]) -> None: ...

    def __init__(self, *args) -> None:
        """
        Initializes an Expression object by delegating to internal initialization methods based on the type and count of the provided arguments. This constructor supports flexible creation of expressions, allowing for a default zero value, a numeric constant, a copy of an existing Expression, a collection of Variables, or a single Term. When multiple arguments are supplied, they can represent a numeric coefficient followed by one or more Terms, or a sequence of Terms to be aggregated. If the provided arguments do not match any of the supported type signatures or combinations, a ValueError is raised to indicate invalid input.

        :param args: Variable arguments defining the initial value, which can be a number, an existing Expression, a collection of Variables, a Term, or multiple Terms optionally preceded by a numeric coefficient.
        :type args: typing.Any

        :raises ValueError: Raised when the provided arguments do not match any supported signature or type combination for initialization.
        """

        if len(args) == 0:
            self.__expression_init_1(0)
        elif len(args) == 1:
            if isinstance(args[0], constants.NUMBER):
                self.__expression_init_1(*args)
            elif isinstance(args[0], Expression):
                self.__expression_init_4(*args)
            elif trycast.trycast(typing.Union[list[Variable], set[Variable]], args[0]):
                self.__expression_init_5(*args)
            elif isinstance(args[0], Term):
                self.__expression_init_3(*args)
            else:
                raise ValueError
        else:
            if isinstance(args[0], constants.NUMBER) and all(
                isinstance(a, Term) for a in args[1:]
            ):
                self.__expression_init_2(*args)
            elif all(isinstance(a, Term) for a in args):
                self.__expression_init_3(*args)
            else:
                raise ValueError

    def __expression_init_1(self, constant: constants.NUMBER) -> None:
        """
        This internal initialization method configures the `Expression` instance to represent a standalone constant value. It validates that the provided `constant` argument is an instance of `constants.NUMBER` and assigns it to the corresponding instance attribute. Additionally, it initializes the `terms` list as empty, establishing that the expression currently consists solely of the constant term without any variable components.

        :param constant: The constant term or offset value for the expression.
        :type constant: constants.NUMBER
        """

        assert isinstance(constant, constants.NUMBER)
        # oefficient c
        self.constant: constants.NUMBER = constant
        # Terms c1 * x1 + c2 * x2 + ...
        self.terms: list[Term] = []

    def __expression_init_2(self, constant: constants.NUMBER, *terms: Term) -> None:
        """
        Initializes the expression with a specific numeric constant and a variable number of term objects. This method requires that at least one term be provided; otherwise, an assertion error is raised. It delegates the initialization of the constant component to `__expression_init_1` and stores the provided terms in the instance's internal list.

        :param constant: The constant additive term of the expression.
        :type constant: constants.NUMBER
        :param terms: 
        :type terms: Term
        """

        assert len(terms) > 0
        self.__expression_init_1(constant)
        # Terms c1 * x1 + c2 * x2 + ...
        self.terms: list[Term] = [t for t in terms]

    def __expression_init_3(self, *terms: Term) -> None:
        """
        Initializes the object by delegating to the secondary initialization method with a default scalar value of 0.0. It accepts a variable number of `Term` arguments, which are forwarded along with the zero value to configure the expression's state. This effectively creates an expression composed solely of the provided terms without an initial constant offset.

        :param terms: Variable number of Term objects comprising the expression.
        :type terms: Term
        """

        self.__expression_init_2(0.0, *terms)

    def __expression_init_4(self, expr: typing.Self) -> None:
        """
        This internal helper method initializes the current expression instance by copying the components of another expression object. It retrieves the constant value and the list of terms from the provided expression and passes them to the `__expression_init_2` method to complete the setup. This process effectively creates a new representation of the same mathematical expression, modifying the state of `self` in place.

        :param expr: An existing expression instance to copy the constant and terms from.
        :type expr: typing.Self
        """

        self.__expression_init_2(expr.constant, *expr.terms)

    def __expression_init_5(
        self, v: typing.Union[list[Variable], set[Variable]]
    ) -> None:
        """
        Initializes the expression as the sum of the provided variables. It accepts a list or set of Variable objects, converting each into a Term with a coefficient of 1.0 and aggregating them with a constant term of 0.0. If the input collection is empty, the expression represents a constant value of zero.

        :param v: A collection of variables to be summed with a coefficient of 1.0.
        :type v: typing.Union[list[Variable], set[Variable]]
        """

        self.__expression_init_2(0.0, *[Term(1.0, var) for var in v])

    def get_terms(self) -> list[Term]:
        """
        Returns the list of Term objects that make up this Expression. This method provides direct access to the internal list of terms; therefore, modifying the returned list will alter the state of the Expression instance.

        :return: The list of Term objects associated with this instance.

        :rtype: list[Term]
        """

        return self.terms

    def get_constant(self) -> constants.NUMBER:
        """
        Retrieves the constant value associated with this expression instance. The method returns the value of the internal `constant` attribute, which is expected to be of type `constants.NUMBER`. This is a read-only operation that does not modify the object's state or produce any side effects.

        :return: The numeric constant value stored in the instance.

        :rtype: constants.NUMBER
        """

        return self.constant

    def set_constant(self, constant: constants.NUMBER) -> None:
        """
        Updates the internal state of the Expression instance by assigning the provided numeric value to the `constant` attribute. This operation directly mutates the object, overwriting any previously stored value associated with this attribute. The method does not return a value and relies on the caller to ensure the input conforms to the expected numeric type.

        :param constant: The numeric value to assign to the constant.
        :type constant: constants.NUMBER
        """

        self.constant = constant

    def clone(self) -> typing.Self:
        """
        Creates and returns a new instance of the Expression that is a logical copy of the current object. The new instance is constructed using the same constant value and terms as the original, ensuring that the two objects are independent. This method has no side effects on the original Expression, though if the terms contain mutable objects, the clone will reference the same underlying objects as the source.

        :return: A new instance of the class with the same constant and terms as the current object.

        :rtype: typing.Self
        """

        return Expression(self.constant, *self.terms)

    @staticmethod
    def negate_expression(expr: typing.Self) -> typing.Self:
        """
        Returns a new expression that represents the mathematical negation of the provided input expression. This operation effectively flips the sign of the expression by utilizing the unary minus operator defined for the class. Since this is a static method, it acts as a utility function that processes the input instance without modifying it in place, assuming the underlying implementation of negation returns a new object. The specific behavior and potential exceptions depend entirely on the implementation of the `__neg__` magic method within the class hierarchy.

        :param expr: The expression to be negated.
        :type expr: typing.Self

        :return: The arithmetic negation of the expression.

        :rtype: typing.Self
        """

        return -expr

    @staticmethod
    def add_constant(expr: typing.Self, constant: constants.NUMBER) -> typing.Self:
        """
        Constructs a new expression representing the arithmetic sum of the provided expression and a numeric constant. This static method performs the addition by combining the constant with the expression, utilizing the expression's underlying logic to handle the operation. The process is non-destructive and side-effect-free, returning a new expression instance without modifying the original input expression or the constant value.

        :param expr: The expression to which the constant is added.
        :type expr: typing.Self
        :param constant: The numeric value to add to the expression.
        :type constant: constants.NUMBER

        :return: The expression resulting from adding the constant to the input expression.

        :rtype: typing.Self
        """

        return constant + expr

    def increment_constant(self) -> None:
        """Increments the value of the `constant` attribute stored in the instance by one. This method mutates the object's state directly, updating the existing attribute rather than creating a new one, and returns `None`. It relies on the `constant` attribute being defined and compatible with the addition assignment operator."""

        self.constant += 1

    def add_term(self, term: Term) -> None:
        """
        Adds the specified term to the expression, combining it with any existing term that shares the same variable. If a term with a matching variable is already present in the expression, the method updates that term by summing its value with the new term. If no matching variable is found, the new term is appended to the expression's internal list. This method modifies the expression in place and ensures the list of terms remains non-empty after the operation.

        :param term: The term to add to the expression. If a term with the same variable already exists, the terms are combined; otherwise, the term is appended.
        :type term: Term
        """

        for idx, t in enumerate(self.terms):
            if t.get_var() == term.get_var():
                self.terms[idx] = t + term
                return
        self.terms.append(term)
        assert len(self.terms) > 0

    @staticmethod
    def add_term_(exp: typing.Self, term: Term) -> typing.Self:
        """
        Creates a new expression by appending a specific term to a provided expression instance. This static method ensures the original expression remains unmodified by first constructing a copy of the input. It then invokes the instance-level addition logic on this copy and returns the updated expression.

        :param exp: The expression to which the term will be added.
        :type exp: typing.Self
        :param term: The term to be added to the expression.
        :type term: Term

        :return: The resulting expression after adding the specified term.

        :rtype: typing.Self
        """

        curr_expr: Expression = Expression(exp)
        curr_expr.add_term(term)
        return curr_expr

    @staticmethod
    def add_expressions(expr1: typing.Self, expr2: typing.Self) -> typing.Self:
        """
        Combines two expression instances by performing an addition operation and returning the resulting expression. This static method delegates to the underlying `__add__` implementation of the class, effectively calculating the sum of the two provided arguments. It returns a new instance representing the combined value, and typically does not modify the original input expressions, though specific behavior depends on the class's implementation of the addition operator.

        :param expr1: The first expression to add.
        :type expr1: typing.Self
        :param expr2: The second expression to be added to the first.
        :type expr2: typing.Self

        :return: A new instance representing the sum of the two expressions.

        :rtype: typing.Self
        """

        return expr1 + expr2

    @staticmethod
    def subtract_expressions(expr1: typing.Self, expr2: typing.Self) -> typing.Self:
        """
        Calculates the difference between two expression instances by subtracting the second argument from the first. This static method serves as a functional interface to the subtraction operator, returning a new object that represents the result without modifying the original inputs. The specific behavior and potential errors, such as type incompatibilities or domain-specific constraints, depend entirely on the implementation of the subtraction logic defined within the expression class.

        :param expr1: The expression from which the second expression is subtracted.
        :type expr1: typing.Self
        :param expr2: The expression to be subtracted from the first expression.
        :type expr2: typing.Self

        :return: The result of subtracting the second expression from the first.

        :rtype: typing.Self
        """

        return expr1 - expr2

    @staticmethod
    def multiply_constant(expr: typing.Self, constant: constants.NUMBER) -> typing.Self:
        """
        Performs scalar multiplication by combining a specific expression instance with a numeric constant. This static method returns a new expression representing the product, ensuring that the original expression remains unmodified. The operation effectively delegates to the multiplication operator defined for the expression class, allowing for consistent behavior across different numeric types.

        :param expr: The expression to be multiplied by the constant.
        :type expr: typing.Self
        :param constant: The numeric constant to multiply the expression by.
        :type constant: constants.NUMBER

        :return: An instance representing the product of the expression and the constant.

        :rtype: typing.Self
        """

        return expr * constant

    def get_constant_term(self, var: Variable) -> constants.NUMBER:
        """
        Retrieves the coefficient associated with a specific variable within the expression. The method iterates through the internal list of terms to locate the target variable; if a match is found, the corresponding coefficient is returned. If the variable is not present in the expression, the method returns 0.0.

        :param var: The variable whose coefficient is to be retrieved from the expression.
        :type var: Variable

        :return: The coefficient of the specified variable in the expression, or 0.0 if the variable is not present.

        :rtype: constants.NUMBER
        """

        for term in self.terms:
            if term.get_var() == var:
                return term.get_coeff()
        return 0.0

    def __neg__(self) -> typing.Self:
        """
        Returns a new Expression representing the arithmetic negation of the current instance. This is achieved by creating a new object with the constant value negated and every term in the expression multiplied by -1. The operation is non-destructive, leaving the original expression unchanged.

        :return: A new instance representing the negation of the current expression.

        :rtype: typing.Self
        """

        return Expression(-self.get_constant(), *[-t for t in self.get_terms()])

    def __add__(
        self, value: typing.Union[int, float, typing.Self, Term]
    ) -> typing.Self:
        """
        Overloads the addition operator to combine the current expression with a numeric value, a `Term`, or another `Expression`. If the provided value is a number, the method returns a new `Expression` instance with the value added to the constant term, leaving the original expression unchanged. Conversely, if the value is a `Term` or an `Expression`, the method modifies the current instance in place by incorporating the terms and constant from the provided value, and returns the updated instance.

        :param value: The right-hand operand to add, supporting numeric constants, Terms, or other instances of the class.
        :type value: typing.Union[int, float, typing.Self, Term]

        :return: An instance representing the arithmetic sum of the current object and the specified value.

        :rtype: typing.Self
        """

        if isinstance(value, constants.NUMBER):
            return Expression(self.get_constant() + value, *self.get_terms())
        elif isinstance(value, Term):
            result: Expression = self
            result.add_term(value)
            return result
        result: Expression = self
        for term in value.get_terms():
            result.add_term(term)
        result.constant += value.get_constant()
        return result

    def __radd__(self, scalar: constants.NUMBER) -> typing.Self:
        """
        Implements the reflected addition operation to support adding a numeric scalar to the expression when the expression is on the right-hand side of the operator. This method accepts a number and returns a new instance of the same class by delegating to the standard `__add__` method, effectively enabling commutative addition with scalars.

        :param scalar: A numeric value to add to the instance.
        :type scalar: constants.NUMBER

        :return: The sum of the instance and the provided scalar.

        :rtype: typing.Self
        """

        return self + scalar

    def __sub__(self, expr: typing.Union[int, float, typing.Self, Term]) -> typing.Self:
        """
        Performs subtraction by returning the result of adding the negation of the provided operand to the current instance. The operand can be a numeric scalar, a Term, or another Expression, and the operation relies on the class's implementation of addition and unary negation. This method does not modify the original object in place; instead, it returns a new Expression representing the difference.

        :param expr: The value or expression to subtract from the current instance.
        :type expr: typing.Union[int, float, typing.Self, Term]

        :return: A new instance representing the difference between the current object and the given expression.

        :rtype: typing.Self
        """

        return self + (-expr)

    def __rsub__(self, scalar: constants.NUMBER) -> typing.Self:
        """
        Handles the right-hand side subtraction operation, allowing a numeric scalar to be subtracted by this expression. When the subtraction operator is used with a number on the left and this expression on the right, this method is called to compute the result. It returns a new expression instance representing the arithmetic difference, effectively calculating the negation of the current expression added to the provided scalar value.

        :param scalar: The numeric value from which the instance is subtracted.
        :type scalar: constants.NUMBER

        :return: A new instance representing the result of subtracting the current object from the scalar value.

        :rtype: typing.Self
        """

        return -self + scalar

    def __mul__(self, scalar: constants.NUMBER) -> typing.Self:
        """
        Implements the multiplication operator to scale the expression by a numeric scalar. It constructs and returns a new Expression object by multiplying the existing constant value and every term within the expression by the provided scalar. This method does not modify the current instance in place, ensuring that the original expression remains unchanged.

        :param scalar: The numeric factor to multiply the expression by.
        :type scalar: constants.NUMBER

        :return: A new Expression instance representing the product of the current expression and the specified scalar.

        :rtype: typing.Self
        """

        return Expression(
            self.get_constant() * scalar,
            *[t * scalar for t in self.get_terms()],
        )

    def __rmul__(self, scalar: constants.NUMBER) -> typing.Self:
        """
        Handles the reflected multiplication operation, enabling the expression to be multiplied by a numeric scalar when the scalar is positioned on the left-hand side of the operator. This implementation delegates the calculation to the standard multiplication method (`__mul__`), ensuring that the operation behaves consistently regardless of the operand order. It returns a new instance of the expression representing the product, leaving the original expression unchanged.

        :param scalar: The numeric value to multiply the instance by.
        :type scalar: constants.NUMBER

        :return: The product of the scalar and the instance.

        :rtype: typing.Self
        """

        return self * scalar

    def __truediv__(self, scalar: constants.NUMBER) -> typing.Self:
        """
        Performs true division of the expression by a specified scalar value. This operation is implemented by multiplying the expression by the reciprocal of the scalar, effectively delegating the core logic to the multiplication operator. The method returns a new instance of the expression, leaving the original object unmodified. A `ZeroDivisionError` will be raised if the provided scalar is zero.

        :param scalar: The numeric scalar used as the divisor.
        :type scalar: constants.NUMBER

        :return: Returns the result of dividing this instance by the specified scalar.

        :rtype: typing.Self
        """

        return self * (1 / scalar)

    def __hash__(self) -> int:
        """
        Calculates the hash code for the expression based on its string representation, enabling the object to be used in hash-based collections such as dictionaries and sets. The implementation relies on the `__str__` method to generate a canonical string representation, ensuring that two expressions with identical string representations yield the same hash value. This behavior implies that the hashability of the object is intrinsically linked to the stability and uniqueness of its string output.

        :return: An integer hash value derived from the string representation of the object.

        :rtype: int
        """

        return hash(str(self))

    def __eq__(self, value: typing.Self) -> bool:
        """
        Determines whether the current expression is equivalent to another object by comparing their internal terms. The method returns False if the provided value is not an instance of the Expression class. For valid Expression instances, equality is established by verifying that both expressions contain the same number of terms and that every term present in the current expression also exists within the other expression, effectively treating the collection of terms as an unordered set.

        :param value: The expression to compare with the current instance.
        :type value: typing.Self

        :return: True if the provided value is an Expression instance with an identical set of terms, False otherwise.

        :rtype: bool
        """

        if not isinstance(value, Expression):
            return False
        return len(self.terms) == len(value.terms) and all(
            term in value.terms for term in self.terms
        )

    def __ne__(self, value: typing.Self) -> bool:
        """
        Determines whether the current instance is not equal to the specified value by negating the result of the equality comparison. This implementation delegates the core logic to the `__eq__` method, ensuring that inequality remains consistent with the defined equality semantics. Consequently, the behavior, including handling of type mismatches or specific comparison logic, is entirely dependent on the implementation of the equality operator.

        :param value: The object to compare against the current instance.
        :type value: typing.Self

        :return: True if the instance is not equal to the provided value, otherwise False.

        :rtype: bool
        """

        return not (self == value)

    def __repr__(self) -> str:
        """
        Returns a string representation of the Expression instance, typically used for debugging and logging. This implementation delegates directly to the `__str__` method, resulting in an output that is identical to the informal string representation rather than a distinct, unambiguous representation suitable for `eval()`. Consequently, the specific format and content of the returned string are determined entirely by the class's string conversion logic.

        :return: A string representation of the object, as returned by the `__str__` method.

        :rtype: str
        """

        return str(self)

    def __str__(self) -> str:
        """
        Generates a human-readable string representation of the mathematical expression by combining the constant value and the variable terms. The method formats each term with an explicit sign, omitting the coefficient value if it is 1 or -1 to improve readability. If the constant component is zero, it is excluded from the output entirely.

        :return: A string representation of the expression, combining the constant and terms with formatted coefficients and signs.

        :rtype: str
        """

        parts: list[str] = []
        if self.constant != 0.0:
            parts.append(str(self.constant))

        for term in self.terms:
            n: float = float(term.get_coeff())
            if n == 1.0:
                parts.append(f"+ {term.get_var()}")
            elif n == -1.0:
                parts.append(f"- {term.get_var()}")
            else:
                parts.append(f"{'+ ' if n >= 0 else '- '}{abs(n)} {term.get_var()}")
        return " ".join(parts)
