fuzzy_dl_owl2.fuzzydl.degree.degree_variable
============================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.degree.degree_variable



.. ── LLM-GENERATED DESCRIPTION START ──

Encapsulates a symbolic variable to represent a dynamic degree of satisfaction for use in algebraic expressions and constraints.


Description
-----------


The software provides a mechanism to treat degrees of satisfaction as symbolic algebraic variables rather than fixed numeric constants, enabling dynamic constraint solving within a fuzzy logic framework. By wrapping a ``Variable`` instance, the implementation allows these symbolic degrees to participate in the construction of linear expressions and inequalities, effectively bridging the gap between abstract fuzzy logic concepts and Mixed-Integer Linear Programming (MILP) formulations. Design choices ensure that the entity is explicitly identified as non-numeric, preventing it from being confused with concrete values during type checking or evaluation phases. Furthermore, the logic supports standard algebraic operations such as addition, subtraction, and scalar multiplication, which are essential for building complex constraints where the satisfaction level must be determined by a solver rather than hardcoded.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.degree.degree_variable.DegreeVariable


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_degree_degree_variable_DegreeVariable.png
       :alt: UML Class Diagram for DegreeVariable
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **DegreeVariable**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_degree_degree_variable_DegreeVariable.pdf
       :alt: UML Class Diagram for DegreeVariable
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **DegreeVariable**

.. py:class:: DegreeVariable(variable: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.degree.degree.Degree`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.degree.degree_variable.DegreeVariable
      :parts: 1
      :private-bases:


   This class encapsulates a symbolic representation of a degree of satisfaction, where the magnitude is not a fixed numeric value but is instead defined by a variable. It serves as a bridge between the abstract concept of a "degree" and the algebraic manipulation of variables, allowing the degree to participate in mathematical expressions and constraints. By wrapping a `Variable` instance, it enables operations such as addition, subtraction, and scalar multiplication within expressions, as well as the creation of inequalities where the variable acts as the right-hand side. Unlike numeric degrees, this entity is identified as non-numeric, making it suitable for contexts where the satisfaction level is dynamic or unknown and must be solved for rather than hardcoded.

   :param variable: Symbolic variable representing the degree, used to construct algebraic expressions and inequalities.
   :type variable: Variable


   .. py:method:: __eq__(degree: fuzzy_dl_owl2.fuzzydl.degree.degree.Degree) -> bool

      Determines whether the current `DegreeVariable` instance is equal to another object. Equality is established only if the provided argument is also an instance of `DegreeVariable` and the underlying variable, accessed via `get_variable()`, is identical to that of the current instance. If the argument is of a different type or the underlying variables do not match, the method returns `False`.

      :param degree: The degree object to compare against for equality.
      :type degree: Degree

      :return: True if the provided object is a DegreeVariable representing the same underlying variable, otherwise False.

      :rtype: bool



   .. py:method:: __str__() -> str

      Returns a human-readable string representation of the `DegreeVariable` instance, formatted as "Degree(variable)" where "variable" is the value of the instance's variable attribute. This method is implicitly invoked by the built-in `str()` function and print operations. It performs no side effects on the object's state, though it relies on the string conversion of the underlying variable attribute.

      :return: Returns a string representation of the object in the format 'Degree(variable)'.

      :rtype: str



   .. py:method:: add_to_expression(expr: fuzzy_dl_owl2.fuzzydl.milp.expression.Expression) -> fuzzy_dl_owl2.fuzzydl.milp.expression.Expression

      Incorporates the variable represented by this `DegreeVariable` into a given expression by adding it as a term with a coefficient of 1.0. The method returns a new `Expression` object representing the sum of the input and the variable, ensuring that the original expression is not modified. This function is primarily used for incrementally constructing expressions where the specific degree variable needs to be included, relying on the underlying `Expression` class to handle the addition logic.

      :param expr: The expression to which the term is added.
      :type expr: Expression

      :return: The resulting Expression after adding a term with a coefficient of 1.0 and the instance's variable to the input expression.

      :rtype: Expression



   .. py:method:: clone() -> Self

      Creates and returns a new instance of `DegreeVariable` that corresponds to the same underlying variable as the current instance. This method achieves this by calling the `get_degree` factory method, passing the internal variable reference to generate the copy. The operation is side-effect-free with respect to the original object, meaning the state of the current instance remains unchanged.

      :return: A new instance of the class representing the same underlying variable.

      :rtype: typing.Self



   .. py:method:: create_inequality_with_degree_rhs(expr: fuzzy_dl_owl2.fuzzydl.milp.expression.Expression, inequality_type: fuzzy_dl_owl2.fuzzydl.util.constants.InequalityType) -> fuzzy_dl_owl2.fuzzydl.milp.inequation.Inequation

      Creates an inequality constraint where the degree variable serves as the right-hand side operand relative to the provided expression. The method constructs a new `Inequation` instance by subtracting the degree variable from the input expression using a coefficient of -1.0. This results in a constraint that effectively compares the expression to the degree variable according to the specified `inequality_type` (e.g., less than or equal to). The operation does not modify the input expression or the variable itself.

      :param expr: The expression representing the left-hand side of the inequality.
      :type expr: Expression
      :param inequality_type: The relational operator (e.g., less than, greater than) defining the inequality.
      :type inequality_type: InequalityType

      :return: Returns an Inequation representing the inequality `expr` [inequality_type] `self.variable`.

      :rtype: Inequation



   .. py:method:: get_degree(value: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable) -> Self
      :staticmethod:


      Constructs a `DegreeVariable` instance using the provided `Variable` object as its underlying value. This static method serves as a factory function to explicitly wrap or cast a generic variable into a degree-specific representation. It does not modify the input variable but rather creates a new instance, delegating the actual initialization logic to the `DegreeVariable` constructor.

      :param value: The variable to be converted into a DegreeVariable.
      :type value: Variable

      :return: A DegreeVariable instance initialized with the provided variable.

      :rtype: typing.Self



   .. py:method:: get_variable() -> fuzzy_dl_owl2.fuzzydl.milp.variable.Variable

      Retrieves the underlying `Variable` instance stored within the `DegreeVariable` object. This method serves as a getter for the internal `variable` attribute, providing access to the symbolic variable associated with the specific degree. It is a read-only operation that does not alter the state of the instance.

      :return: The `Variable` instance associated with this object.

      :rtype: Variable



   .. py:method:: is_number_not_one() -> bool

      Determines whether the instance represents a numeric value that is not equal to one. For the `DegreeVariable` class, this method unconditionally returns False, indicating that the entity does not satisfy the condition of being a number distinct from one. This behavior suggests that within the module's type hierarchy, a `DegreeVariable` is either treated as a non-numeric entity or is implicitly associated with the value one.

      :return: Always returns False.

      :rtype: bool



   .. py:method:: is_number_zero() -> bool

      Checks if the instance represents the numerical value zero. This method always returns `False`, reflecting that a `DegreeVariable` is a symbolic entity and not a constant. It is primarily used to distinguish variables from numeric constants during expression evaluation or simplification.

      :return: True if the number is zero, False otherwise.

      :rtype: bool



   .. py:method:: is_numeric() -> bool

      Indicates that this variable does not represent a numeric constant. Unlike concrete numbers or evaluated expressions, a DegreeVariable is a symbolic entity, so this method always returns False to signal that it cannot be treated as a raw numeric value during computations or type checking.

      :return: True if the object is numeric, False otherwise.

      :rtype: bool



   .. py:method:: multiply_constant(constant: float) -> fuzzy_dl_owl2.fuzzydl.milp.expression.Expression

      Multiplies the variable represented by this instance by a specified scalar constant to generate a new linear expression. The method constructs a `Term` object using the provided constant as the coefficient and the current variable, then wraps this term within an `Expression` object. This operation does not modify the original `DegreeVariable` instance; instead, it returns a distinct `Expression` representing the product of the constant and the variable.

      :param constant: The numeric coefficient for the variable in the resulting term.
      :type constant: float

      :return: A new Expression representing the product of the provided constant and the variable.

      :rtype: Expression



   .. py:method:: subtract_from_expression(expr: fuzzy_dl_owl2.fuzzydl.milp.expression.Expression) -> fuzzy_dl_owl2.fuzzydl.milp.expression.Expression

      Subtracts the variable represented by this `DegreeVariable` instance from a given expression. It performs this operation by adding a term with a coefficient of -1.0 and the instance's variable to the input expression. The method returns a new `Expression` object containing the result, ensuring that the original input expression remains unmodified.

      :param expr: The expression from which the current term is subtracted.
      :type expr: Expression

      :return: A new Expression representing the result of subtracting the variable from the provided expression.

      :rtype: Expression



   .. py:attribute:: variable
      :type:  fuzzy_dl_owl2.fuzzydl.milp.variable.Variable

