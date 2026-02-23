fuzzy_dl_owl2.fuzzydl.degree.degree_expression
==============================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.degree.degree_expression



.. ── LLM-GENERATED DESCRIPTION START ──

A symbolic representation of a degree that wraps an algebraic expression to support dynamic, non-numeric calculations within a fuzzy logic framework.


Description
-----------


Extending the base ``Degree`` abstraction, this implementation provides a mechanism to handle satisfaction measures that are not fixed numeric values but are instead defined by symbolic algebraic expressions. By encapsulating an ``Expression`` object, the logic enables dynamic manipulation of degrees through standard arithmetic operations such as addition, subtraction, and scalar multiplication, which are essential for formulating complex constraints in optimization problems. The design explicitly treats these entities as non-numeric, ensuring that they are processed symbolically during the construction of mathematical models, specifically when generating inequalities that compare external expressions against the internal state. Functionality includes cloning capabilities and equality checks based on the underlying expression, ensuring that the symbolic nature of the degree is preserved throughout algebraic transformations and comparisons.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.degree.degree_expression.DegreeExpression


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_degree_degree_expression_DegreeExpression.png
       :alt: UML Class Diagram for DegreeExpression
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **DegreeExpression**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_degree_degree_expression_DegreeExpression.pdf
       :alt: UML Class Diagram for DegreeExpression
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **DegreeExpression**

.. py:class:: DegreeExpression(expr: fuzzy_dl_owl2.fuzzydl.milp.expression.Expression)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.degree.degree.Degree`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.degree.degree_expression.DegreeExpression
      :parts: 1
      :private-bases:


   This class represents a non-numeric degree defined by a symbolic expression, serving as a dynamic measure of satisfaction or magnitude within a broader system of degrees. It extends the base `Degree` class to encapsulate an `Expression` object, enabling the degree to participate in algebraic manipulations such as addition, subtraction, and scalar multiplication. Unlike fixed numeric degrees, this class allows for context-dependent values and provides functionality to construct inequalities by comparing external expressions against the stored expression. Consequently, it identifies itself as non-numeric, distinguishing its behavior from concrete constant degrees.

   :param expr: The underlying expression that defines the value of the degree.
   :type expr: Expression


   .. py:method:: __eq__(d: fuzzy_dl_owl2.fuzzydl.degree.degree.Degree) -> bool

      Determines equality by comparing the current instance against another object. If the provided argument is an instance of `DegreeExpression`, the method returns the result of comparing that argument directly to the internal expression of the current instance. If the argument is not a `DegreeExpression`, the method returns False.

      :param d: The object to compare with this instance.
      :type d: Degree

      :return: True if the provided object is a DegreeExpression equal to the expression represented by this instance, otherwise False.

      :rtype: bool



   .. py:method:: __str__() -> str

      Returns a human-readable string representation of the `DegreeExpression` object, formatted as `Degree(expr)`, where `expr` is the string representation of the underlying expression stored in the instance. This method is invoked automatically by the `str()` built-in function and during string formatting operations, providing a clear and concise way to visualize the structure of the expression for debugging or display purposes.

      :return: A string representation of the object, formatted as 'Degree(expression)'.

      :rtype: str



   .. py:method:: add_to_expression(expr: fuzzy_dl_owl2.fuzzydl.milp.expression.Expression) -> fuzzy_dl_owl2.fuzzydl.milp.expression.Expression

      Calculates the sum of a given expression and the internal expression held by the current instance. The method accepts an `Expression` object as an argument and returns a new `Expression` representing the result of adding the argument to the instance's expression. This operation depends on the addition behavior defined for the `Expression` type and does not modify the state of the current instance or the input argument.

      :param expr: The expression to be added to the current instance's expression.
      :type expr: Expression

      :return: An Expression representing the sum of the provided expression and the instance's expression.

      :rtype: Expression



   .. py:method:: clone() -> Self

      Creates and returns a new instance of the `DegreeExpression` that is semantically equivalent to the current object. This method delegates to the `get_degree` class method, passing the underlying expression to construct a fresh copy, ensuring that modifications to the new instance do not affect the original.

      :return: A new instance of the class representing the same degree expression.

      :rtype: typing.Self



   .. py:method:: create_inequality_with_degree_rhs(expr: fuzzy_dl_owl2.fuzzydl.milp.expression.Expression, inequality_type: fuzzy_dl_owl2.fuzzydl.util.constants.InequalityType) -> fuzzy_dl_owl2.fuzzydl.milp.inequation.Inequation

      Constructs an `Inequation` object that compares the provided expression against the current `DegreeExpression` instance, placing the instance on the right-hand side of the relationship. The method creates this inequality by subtracting the instance's internal expression from the input `expr` and passing the result to the `Inequation` constructor along with the specified `inequality_type`. This process has no side effects on the input or the current object, but it relies on the underlying expressions being compatible for subtraction.

      :param expr: The expression to compare against the instance's expression.
      :type expr: Expression
      :param inequality_type: Specifies the relational operator (e.g., less than, greater than) for the constructed inequation.
      :type inequality_type: InequalityType

      :return: Returns an Inequation comparing the input expression to the degree, with the degree positioned on the right-hand side.

      :rtype: Inequation



   .. py:method:: get_degree(value: fuzzy_dl_owl2.fuzzydl.milp.expression.Expression) -> Self
      :staticmethod:


      Constructs a new `DegreeExpression` instance by wrapping the provided input expression. This static method serves as a factory function, taking a generic `Expression` object and encapsulating it within the specific `DegreeExpression` type. The operation delegates directly to the class constructor, meaning any validation or transformation of the input is handled during the instantiation process, and the original input remains unmodified.

      :param value: The expression representing the degree value.
      :type value: Expression

      :return: A DegreeExpression object that wraps the provided expression value.

      :rtype: typing.Self



   .. py:method:: get_expression() -> fuzzy_dl_owl2.fuzzydl.milp.expression.Expression

      Retrieves the underlying `Expression` object stored within the instance. This method serves as a simple accessor that returns the reference held by the internal `expr` attribute without performing any computations or modifications to the state. Because it returns a direct reference to the internal object, any changes made to the returned expression will be reflected in the state of the `DegreeExpression` instance.

      :return: Returns the Expression object stored in this instance.

      :rtype: Expression



   .. py:method:: is_number_not_one() -> bool

      Checks if the expression represents a numeric value that is not equal to one. This implementation always returns False, indicating that instances of this class are never considered to be numbers distinct from one, regardless of their internal state. The method performs no computation and has no side effects.

      :return: Always returns False.

      :rtype: bool



   .. py:method:: is_number_zero() -> bool

      Determines whether the current expression represents the numeric value zero. This method unconditionally returns False, indicating that an instance of DegreeExpression is never considered to be the number zero, regardless of its specific attributes or configuration. This behavior is consistent with the semantic role of a degree expression as a structural component rather than a numeric constant.

      :return: True if the number is zero, False otherwise.

      :rtype: bool



   .. py:method:: is_numeric() -> bool

      Determines whether the expression represents a numeric value. This method consistently returns False, indicating that a DegreeExpression is not treated as a numeric entity within the system, regardless of its specific content or state. This distinction implies that the expression is handled symbolically or structurally rather than as a concrete number.

      :return: Returns False, indicating that the object is not numeric.

      :rtype: bool



   .. py:method:: multiply_constant(constant: float) -> fuzzy_dl_owl2.fuzzydl.milp.expression.Expression

      Multiplies the underlying expression by a specified scalar constant. This method accepts a floating-point value and returns a new `Expression` object representing the product of the internal expression and the constant. The operation does not modify the current instance in place; instead, it delegates the multiplication to the internal `expr` attribute and returns the result.

      :param constant: The scalar value by which the expression is multiplied.
      :type constant: float

      :return: An Expression representing the product of the current expression and the provided constant.

      :rtype: Expression



   .. py:method:: subtract_from_expression(expr: fuzzy_dl_owl2.fuzzydl.milp.expression.Expression) -> fuzzy_dl_owl2.fuzzydl.milp.expression.Expression

      Subtracts the internal expression of the current instance from a given expression object. This method accepts an external expression as an argument and computes the difference by deducting the instance's stored expression value from it. The operation returns a new Expression object representing the result, effectively implementing the logic `argument - self.expr`.

      :param expr: The expression from which the current object's expression will be subtracted.
      :type expr: Expression

      :return: An Expression representing the result of subtracting the instance's expression from the provided expression.

      :rtype: Expression



   .. py:attribute:: expr
      :type:  fuzzy_dl_owl2.fuzzydl.milp.expression.Expression

