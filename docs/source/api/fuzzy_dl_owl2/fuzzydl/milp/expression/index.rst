fuzzy_dl_owl2.fuzzydl.milp.expression
=====================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.milp.expression



.. ── LLM-GENERATED DESCRIPTION START ──

A Python class representing linear mathematical expressions used within fuzzy description logic constraints to model degrees of satisfaction.


Description
-----------


The software models linear mathematical expressions of the form :math:`c + c_1x_1 + \dots + c_nx_n`, which are typically employed to represent the degree of satisfaction for concepts in fuzzy description logic ontologies. Construction of these expressions is highly flexible, supporting initialization from numeric constants, sequences of terms, existing expression instances, or collections of variables, thereby allowing for seamless integration into larger constraint systems. Arithmetic manipulation is achieved through comprehensive operator overloading, enabling addition, subtraction, multiplication, and division with scalars, terms, or other expressions while automatically managing the consolidation of terms to merge coefficients for identical variables. Beyond basic arithmetic, the implementation includes utility functions for cloning, negation, and retrieving specific coefficients, ensuring that the mathematical objects can be easily queried, copied, and formatted as strings for debugging or output generation.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.milp.expression.Expression


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_milp_expression_Expression.png
       :alt: UML Class Diagram for Expression
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **Expression**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_milp_expression_Expression.pdf
       :alt: UML Class Diagram for Expression
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **Expression**

.. py:class:: Expression(constant: fuzzy_dl_owl2.fuzzydl.util.constants.NUMBER)
              Expression(constant: fuzzy_dl_owl2.fuzzydl.util.constants.NUMBER, *terms: fuzzy_dl_owl2.fuzzydl.milp.term.Term)
              Expression(*terms: fuzzy_dl_owl2.fuzzydl.milp.term.Term)
              Expression(expr: Self)
              Expression(v: Union[list[fuzzy_dl_owl2.fuzzydl.milp.variable.Variable], set[fuzzy_dl_owl2.fuzzydl.milp.variable.Variable]])

   This class models a linear mathematical expression of the form $c + c_1x_1 + \dots + c_nx_n$, typically used to represent the degree of satisfaction of a concept within a fuzzy description logic ontology. It offers flexible initialization options, allowing construction from a numeric constant, a sequence of `Term` objects, another `Expression` instance, or a collection of `Variable` objects. The class supports comprehensive arithmetic manipulation through operator overloading, enabling addition, subtraction, multiplication, and division with scalars, terms, or other expressions. Furthermore, it automatically manages term consolidation; if a term is added involving a variable that already exists, the coefficients are merged rather than creating a duplicate entry.

   :raises ValueError:


   .. py:method:: __add__(value: Union[int, float, Self, fuzzy_dl_owl2.fuzzydl.milp.term.Term]) -> Self

      Overloads the addition operator to combine the current expression with a numeric value, a `Term`, or another `Expression`. If the provided value is a number, the method returns a new `Expression` instance with the value added to the constant term, leaving the original expression unchanged. Conversely, if the value is a `Term` or an `Expression`, the method modifies the current instance in place by incorporating the terms and constant from the provided value, and returns the updated instance.

      :param value: The right-hand operand to add, supporting numeric constants, Terms, or other instances of the class.
      :type value: typing.Union[int, float, typing.Self, Term]

      :return: An instance representing the arithmetic sum of the current object and the specified value.

      :rtype: typing.Self



   .. py:method:: __eq__(value: Self) -> bool

      Determines whether the current expression is equivalent to another object by comparing their internal terms. The method returns False if the provided value is not an instance of the Expression class. For valid Expression instances, equality is established by verifying that both expressions contain the same number of terms and that every term present in the current expression also exists within the other expression, effectively treating the collection of terms as an unordered set.

      :param value: The expression to compare with the current instance.
      :type value: typing.Self

      :return: True if the provided value is an Expression instance with an identical set of terms, False otherwise.

      :rtype: bool



   .. py:method:: __expression_init_1(constant: fuzzy_dl_owl2.fuzzydl.util.constants.NUMBER) -> None

      This internal initialization method configures the `Expression` instance to represent a standalone constant value. It validates that the provided `constant` argument is an instance of `constants.NUMBER` and assigns it to the corresponding instance attribute. Additionally, it initializes the `terms` list as empty, establishing that the expression currently consists solely of the constant term without any variable components.

      :param constant: The constant term or offset value for the expression.
      :type constant: constants.NUMBER



   .. py:method:: __expression_init_2(constant: fuzzy_dl_owl2.fuzzydl.util.constants.NUMBER, *terms: fuzzy_dl_owl2.fuzzydl.milp.term.Term) -> None

      Initializes the expression with a specific numeric constant and a variable number of term objects. This method requires that at least one term be provided; otherwise, an assertion error is raised. It delegates the initialization of the constant component to `__expression_init_1` and stores the provided terms in the instance's internal list.

      :param constant: The constant additive term of the expression.
      :type constant: constants.NUMBER
      :param terms:
      :type terms: Term



   .. py:method:: __expression_init_3(*terms: fuzzy_dl_owl2.fuzzydl.milp.term.Term) -> None

      Initializes the object by delegating to the secondary initialization method with a default scalar value of 0.0. It accepts a variable number of `Term` arguments, which are forwarded along with the zero value to configure the expression's state. This effectively creates an expression composed solely of the provided terms without an initial constant offset.

      :param terms: Variable number of Term objects comprising the expression.
      :type terms: Term



   .. py:method:: __expression_init_4(expr: Self) -> None

      This internal helper method initializes the current expression instance by copying the components of another expression object. It retrieves the constant value and the list of terms from the provided expression and passes them to the `__expression_init_2` method to complete the setup. This process effectively creates a new representation of the same mathematical expression, modifying the state of `self` in place.

      :param expr: An existing expression instance to copy the constant and terms from.
      :type expr: typing.Self



   .. py:method:: __expression_init_5(v: Union[list[fuzzy_dl_owl2.fuzzydl.milp.variable.Variable], set[fuzzy_dl_owl2.fuzzydl.milp.variable.Variable]]) -> None

      Initializes the expression as the sum of the provided variables. It accepts a list or set of Variable objects, converting each into a Term with a coefficient of 1.0 and aggregating them with a constant term of 0.0. If the input collection is empty, the expression represents a constant value of zero.

      :param v: A collection of variables to be summed with a coefficient of 1.0.
      :type v: typing.Union[list[Variable], set[Variable]]



   .. py:method:: __hash__() -> int

      Calculates the hash code for the expression based on its string representation, enabling the object to be used in hash-based collections such as dictionaries and sets. The implementation relies on the `__str__` method to generate a canonical string representation, ensuring that two expressions with identical string representations yield the same hash value. This behavior implies that the hashability of the object is intrinsically linked to the stability and uniqueness of its string output.

      :return: An integer hash value derived from the string representation of the object.

      :rtype: int



   .. py:method:: __mul__(scalar: fuzzy_dl_owl2.fuzzydl.util.constants.NUMBER) -> Self

      Implements the multiplication operator to scale the expression by a numeric scalar. It constructs and returns a new Expression object by multiplying the existing constant value and every term within the expression by the provided scalar. This method does not modify the current instance in place, ensuring that the original expression remains unchanged.

      :param scalar: The numeric factor to multiply the expression by.
      :type scalar: constants.NUMBER

      :return: A new Expression instance representing the product of the current expression and the specified scalar.

      :rtype: typing.Self



   .. py:method:: __ne__(value: Self) -> bool

      Determines whether the current instance is not equal to the specified value by negating the result of the equality comparison. This implementation delegates the core logic to the `__eq__` method, ensuring that inequality remains consistent with the defined equality semantics. Consequently, the behavior, including handling of type mismatches or specific comparison logic, is entirely dependent on the implementation of the equality operator.

      :param value: The object to compare against the current instance.
      :type value: typing.Self

      :return: True if the instance is not equal to the provided value, otherwise False.

      :rtype: bool



   .. py:method:: __neg__() -> Self

      Returns a new Expression representing the arithmetic negation of the current instance. This is achieved by creating a new object with the constant value negated and every term in the expression multiplied by -1. The operation is non-destructive, leaving the original expression unchanged.

      :return: A new instance representing the negation of the current expression.

      :rtype: typing.Self



   .. py:method:: __radd__(scalar: fuzzy_dl_owl2.fuzzydl.util.constants.NUMBER) -> Self

      Implements the reflected addition operation to support adding a numeric scalar to the expression when the expression is on the right-hand side of the operator. This method accepts a number and returns a new instance of the same class by delegating to the standard `__add__` method, effectively enabling commutative addition with scalars.

      :param scalar: A numeric value to add to the instance.
      :type scalar: constants.NUMBER

      :return: The sum of the instance and the provided scalar.

      :rtype: typing.Self



   .. py:method:: __repr__() -> str

      Returns a string representation of the Expression instance, typically used for debugging and logging. This implementation delegates directly to the `__str__` method, resulting in an output that is identical to the informal string representation rather than a distinct, unambiguous representation suitable for `eval()`. Consequently, the specific format and content of the returned string are determined entirely by the class's string conversion logic.

      :return: A string representation of the object, as returned by the `__str__` method.

      :rtype: str



   .. py:method:: __rmul__(scalar: fuzzy_dl_owl2.fuzzydl.util.constants.NUMBER) -> Self

      Handles the reflected multiplication operation, enabling the expression to be multiplied by a numeric scalar when the scalar is positioned on the left-hand side of the operator. This implementation delegates the calculation to the standard multiplication method (`__mul__`), ensuring that the operation behaves consistently regardless of the operand order. It returns a new instance of the expression representing the product, leaving the original expression unchanged.

      :param scalar: The numeric value to multiply the instance by.
      :type scalar: constants.NUMBER

      :return: The product of the scalar and the instance.

      :rtype: typing.Self



   .. py:method:: __rsub__(scalar: fuzzy_dl_owl2.fuzzydl.util.constants.NUMBER) -> Self

      Handles the right-hand side subtraction operation, allowing a numeric scalar to be subtracted by this expression. When the subtraction operator is used with a number on the left and this expression on the right, this method is called to compute the result. It returns a new expression instance representing the arithmetic difference, effectively calculating the negation of the current expression added to the provided scalar value.

      :param scalar: The numeric value from which the instance is subtracted.
      :type scalar: constants.NUMBER

      :return: A new instance representing the result of subtracting the current object from the scalar value.

      :rtype: typing.Self



   .. py:method:: __str__() -> str

      Generates a human-readable string representation of the mathematical expression by combining the constant value and the variable terms. The method formats each term with an explicit sign, omitting the coefficient value if it is 1 or -1 to improve readability. If the constant component is zero, it is excluded from the output entirely.

      :return: A string representation of the expression, combining the constant and terms with formatted coefficients and signs.

      :rtype: str



   .. py:method:: __sub__(expr: Union[int, float, Self, fuzzy_dl_owl2.fuzzydl.milp.term.Term]) -> Self

      Performs subtraction by returning the result of adding the negation of the provided operand to the current instance. The operand can be a numeric scalar, a Term, or another Expression, and the operation relies on the class's implementation of addition and unary negation. This method does not modify the original object in place; instead, it returns a new Expression representing the difference.

      :param expr: The value or expression to subtract from the current instance.
      :type expr: typing.Union[int, float, typing.Self, Term]

      :return: A new instance representing the difference between the current object and the given expression.

      :rtype: typing.Self



   .. py:method:: __truediv__(scalar: fuzzy_dl_owl2.fuzzydl.util.constants.NUMBER) -> Self

      Performs true division of the expression by a specified scalar value. This operation is implemented by multiplying the expression by the reciprocal of the scalar, effectively delegating the core logic to the multiplication operator. The method returns a new instance of the expression, leaving the original object unmodified. A `ZeroDivisionError` will be raised if the provided scalar is zero.

      :param scalar: The numeric scalar used as the divisor.
      :type scalar: constants.NUMBER

      :return: Returns the result of dividing this instance by the specified scalar.

      :rtype: typing.Self



   .. py:method:: add_constant(expr: Self, constant: fuzzy_dl_owl2.fuzzydl.util.constants.NUMBER) -> Self
      :staticmethod:


      Constructs a new expression representing the arithmetic sum of the provided expression and a numeric constant. This static method performs the addition by combining the constant with the expression, utilizing the expression's underlying logic to handle the operation. The process is non-destructive and side-effect-free, returning a new expression instance without modifying the original input expression or the constant value.

      :param expr: The expression to which the constant is added.
      :type expr: typing.Self
      :param constant: The numeric value to add to the expression.
      :type constant: constants.NUMBER

      :return: The expression resulting from adding the constant to the input expression.

      :rtype: typing.Self



   .. py:method:: add_expressions(expr1: Self, expr2: Self) -> Self
      :staticmethod:


      Combines two expression instances by performing an addition operation and returning the resulting expression. This static method delegates to the underlying `__add__` implementation of the class, effectively calculating the sum of the two provided arguments. It returns a new instance representing the combined value, and typically does not modify the original input expressions, though specific behavior depends on the class's implementation of the addition operator.

      :param expr1: The first expression to add.
      :type expr1: typing.Self
      :param expr2: The second expression to be added to the first.
      :type expr2: typing.Self

      :return: A new instance representing the sum of the two expressions.

      :rtype: typing.Self



   .. py:method:: add_term(term: fuzzy_dl_owl2.fuzzydl.milp.term.Term) -> None

      Adds the specified term to the expression, combining it with any existing term that shares the same variable. If a term with a matching variable is already present in the expression, the method updates that term by summing its value with the new term. If no matching variable is found, the new term is appended to the expression's internal list. This method modifies the expression in place and ensures the list of terms remains non-empty after the operation.

      :param term: The term to add to the expression. If a term with the same variable already exists, the terms are combined; otherwise, the term is appended.
      :type term: Term



   .. py:method:: add_term_(exp: Self, term: fuzzy_dl_owl2.fuzzydl.milp.term.Term) -> Self
      :staticmethod:


      Creates a new expression by appending a specific term to a provided expression instance. This static method ensures the original expression remains unmodified by first constructing a copy of the input. It then invokes the instance-level addition logic on this copy and returns the updated expression.

      :param exp: The expression to which the term will be added.
      :type exp: typing.Self
      :param term: The term to be added to the expression.
      :type term: Term

      :return: The resulting expression after adding the specified term.

      :rtype: typing.Self



   .. py:method:: clone() -> Self

      Creates and returns a new instance of the Expression that is a logical copy of the current object. The new instance is constructed using the same constant value and terms as the original, ensuring that the two objects are independent. This method has no side effects on the original Expression, though if the terms contain mutable objects, the clone will reference the same underlying objects as the source.

      :return: A new instance of the class with the same constant and terms as the current object.

      :rtype: typing.Self



   .. py:method:: get_constant() -> fuzzy_dl_owl2.fuzzydl.util.constants.NUMBER

      Retrieves the constant value associated with this expression instance. The method returns the value of the internal `constant` attribute, which is expected to be of type `constants.NUMBER`. This is a read-only operation that does not modify the object's state or produce any side effects.

      :return: The numeric constant value stored in the instance.

      :rtype: constants.NUMBER



   .. py:method:: get_constant_term(var: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable) -> fuzzy_dl_owl2.fuzzydl.util.constants.NUMBER

      Retrieves the coefficient associated with a specific variable within the expression. The method iterates through the internal list of terms to locate the target variable; if a match is found, the corresponding coefficient is returned. If the variable is not present in the expression, the method returns 0.0.

      :param var: The variable whose coefficient is to be retrieved from the expression.
      :type var: Variable

      :return: The coefficient of the specified variable in the expression, or 0.0 if the variable is not present.

      :rtype: constants.NUMBER



   .. py:method:: get_terms() -> list[fuzzy_dl_owl2.fuzzydl.milp.term.Term]

      Returns the list of Term objects that make up this Expression. This method provides direct access to the internal list of terms; therefore, modifying the returned list will alter the state of the Expression instance.

      :return: The list of Term objects associated with this instance.

      :rtype: list[Term]



   .. py:method:: increment_constant() -> None

      Increments the value of the `constant` attribute stored in the instance by one. This method mutates the object's state directly, updating the existing attribute rather than creating a new one, and returns `None`. It relies on the `constant` attribute being defined and compatible with the addition assignment operator.



   .. py:method:: multiply_constant(expr: Self, constant: fuzzy_dl_owl2.fuzzydl.util.constants.NUMBER) -> Self
      :staticmethod:


      Performs scalar multiplication by combining a specific expression instance with a numeric constant. This static method returns a new expression representing the product, ensuring that the original expression remains unmodified. The operation effectively delegates to the multiplication operator defined for the expression class, allowing for consistent behavior across different numeric types.

      :param expr: The expression to be multiplied by the constant.
      :type expr: typing.Self
      :param constant: The numeric constant to multiply the expression by.
      :type constant: constants.NUMBER

      :return: An instance representing the product of the expression and the constant.

      :rtype: typing.Self



   .. py:method:: negate_expression(expr: Self) -> Self
      :staticmethod:


      Returns a new expression that represents the mathematical negation of the provided input expression. This operation effectively flips the sign of the expression by utilizing the unary minus operator defined for the class. Since this is a static method, it acts as a utility function that processes the input instance without modifying it in place, assuming the underlying implementation of negation returns a new object. The specific behavior and potential exceptions depend entirely on the implementation of the `__neg__` magic method within the class hierarchy.

      :param expr: The expression to be negated.
      :type expr: typing.Self

      :return: The arithmetic negation of the expression.

      :rtype: typing.Self



   .. py:method:: set_constant(constant: fuzzy_dl_owl2.fuzzydl.util.constants.NUMBER) -> None

      Updates the internal state of the Expression instance by assigning the provided numeric value to the `constant` attribute. This operation directly mutates the object, overwriting any previously stored value associated with this attribute. The method does not return a value and relies on the caller to ensure the input conforms to the expected numeric type.

      :param constant: The numeric value to assign to the constant.
      :type constant: constants.NUMBER



   .. py:method:: subtract_expressions(expr1: Self, expr2: Self) -> Self
      :staticmethod:


      Calculates the difference between two expression instances by subtracting the second argument from the first. This static method serves as a functional interface to the subtraction operator, returning a new object that represents the result without modifying the original inputs. The specific behavior and potential errors, such as type incompatibilities or domain-specific constraints, depend entirely on the implementation of the subtraction logic defined within the expression class.

      :param expr1: The expression from which the second expression is subtracted.
      :type expr1: typing.Self
      :param expr2: The expression to be subtracted from the first expression.
      :type expr2: typing.Self

      :return: The result of subtracting the second expression from the first.

      :rtype: typing.Self


