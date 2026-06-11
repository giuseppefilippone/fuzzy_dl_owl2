fuzzy_dl_owl2.fuzzydl.milp.inequation
=====================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.milp.inequation



.. ── LLM-GENERATED DESCRIPTION START ──

Encapsulates linear constraints of the form :math:`E \bowtie 0` within a mixed-integer linear programming framework, normalizing the right-hand side to zero while supporting equality, less-than, and greater-than relations.


Description
-----------


The software defines a structure for representing mathematical linear constraints where the right-hand side is always normalized to zero, simplifying the handling of inequalities within a solver or optimization engine. By encapsulating an algebraic expression alongside a relational operator, it allows for the precise definition of constraints such as less-than, greater-than, or equal-to relationships. Static factory methods are provided to streamline the instantiation of specific inequality types, acting as convenient aliases for the constructor. Furthermore, the implementation includes standard object comparison and hashing mechanisms, enabling these constraints to be used effectively within hash-based collections like sets and dictionaries while ensuring that string representations remain human-readable for debugging purposes.

.. ── LLM-GENERATED DESCRIPTION END ──

Attributes
----------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.milp.inequation.EqualTo
   fuzzy_dl_owl2.fuzzydl.milp.inequation.GreaterThan
   fuzzy_dl_owl2.fuzzydl.milp.inequation.LessThan


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.milp.inequation.Inequation


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_milp_inequation_Inequation.png
       :alt: UML Class Diagram for Inequation
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **Inequation**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_milp_inequation_Inequation.pdf
       :alt: UML Class Diagram for Inequation
       :align: center
       :width: 11.4cm
       :class: uml-diagram

       UML Class Diagram for **Inequation**

.. py:class:: Inequation(exp: fuzzy_dl_owl2.fuzzydl.milp.expression.Expression, i_type: fuzzy_dl_owl2.fuzzydl.util.constants.InequalityType)

   Encodes a linear constraint  $E \bowtie 0$  with  $\bowtie \in \{=, \le, \ge\}$.
   The right-hand side is always normalised to zero; ``MILPHelper.add_new_constraint``
   shifts the expression by a ``Degree`` when the target bound is not zero.

   Factory aliases: ``GreaterThan``, ``LessThan``, ``EqualTo``.

   :param type: Specifies the relational operator of the inequality, determining if the expression is greater than, less than, or equal to zero.
   :type type: InequalityType
   :param expr: Mathematical expression representing the left-hand side of the inequality, which is compared to zero.
   :type expr: Expression


   .. py:method:: __eq__(value: Self) -> bool

      Determines whether the current instance is equal to another `Inequation` object by comparing their internal attributes. The method returns `True` only if both the underlying expression (`expr`) and the inequality type (`type`) of the two objects match exactly; otherwise, it returns `False`. This strict comparison ensures that two inequalities are considered equivalent only when they represent the same mathematical relationship involving the same expression.

      :param value: The object to compare for equality.
      :type value: typing.Self

      :return: True if the expression and type of the current instance match those of the provided value, otherwise False.

      :rtype: bool



   .. py:method:: __hash__() -> int

      Calculates the hash value for the instance by hashing its string representation, enabling the object to be used as a key in dictionaries or as an element in sets. This implementation relies on the `__str__` method to determine the object's identity for hashing purposes. It is important to note that if the object is mutable and its string representation changes after it has been added to a hash-based collection, the hash value will change, potentially causing the object to become lost or inaccessible within that collection.

      :return: An integer hash value derived from the string representation of the object.

      :rtype: int



   .. py:method:: __ne__(value: Self) -> bool

      Defines the behavior of the inequality operator for instances of this class. The method determines if the current object differs from the provided value by evaluating the equality comparison and negating the result. Consequently, the logic and any potential side effects are entirely dependent on the implementation of the equality operator (`__eq__`). It returns a boolean value indicating whether the two instances are distinct.

      :param value: The object to compare against for inequality.
      :type value: typing.Self

      :return: True if the current instance is not equal to the specified value, False otherwise.

      :rtype: bool



   .. py:method:: __repr__() -> str

      Returns the official string representation of the mathematical inequality, intended primarily for debugging and logging. This implementation delegates directly to the standard string conversion logic, ensuring that the formal representation matches the user-friendly display format. Consequently, invoking the representation function on an instance yields the same output as converting it to a string.

      :return: A string representation of the object.

      :rtype: str



   .. py:method:: __str__() -> str

      Returns a human-readable string representation of the inequality, formatted as 'expression operator 0'. The method constructs this string by combining the string representation of the expression attribute, the specific inequality operator returned by `get_string_type`, and the constant zero. This representation is primarily used for display purposes and debugging.

      :return: Returns a string representation of the object formatted as '{expression} {type} 0'.

      :rtype: str



   .. py:method:: clone() -> Self

      Returns a shallow copy  $(E, \bowtie)$.

      :return: A new instance of the class initialized with the same expression and type as the current object.
      :rtype: typing.Self



   .. py:method:: equal_to(exp: fuzzy_dl_owl2.fuzzydl.milp.expression.Expression) -> Self
      :staticmethod:


      Factory for  $E = 0$.

      :param exp: The expression to compare against for equality.
      :type exp: Expression

      :return: An `Inequation` representing that the current expression is equal to the provided expression.
      :rtype: typing.Self



   .. py:method:: get_constant() -> float

      Returns the right-hand side constant $-c_0$ (since the stored form is
      $E \bowtie 0$).

      :return: The negative of the constant value associated with the expression.
      :rtype: float



   .. py:method:: get_string_type() -> str

      Returns a string representation of the inequality operator defined by the instance. It translates the internal `InequalityType` enumeration into a specific mathematical symbol, mapping equality to its standard value and mapping less-than or greater-than types to the inclusive operators "<=" and ">=" respectively. The method relies on the internal type being one of the defined enumeration values and will raise an assertion error if an unexpected type is encountered.

      :return: The string representation of the inequality operator (e.g., '<=', '>=', or '=').

      :rtype: str



   .. py:method:: get_terms() -> list[fuzzy_dl_owl2.fuzzydl.milp.term.Term]

      Returns the terms of the underlying expression $E$.

      :return: A list of Term objects representing the constituent terms of the expression.
      :rtype: list[Term]



   .. py:method:: get_type() -> fuzzy_dl_owl2.fuzzydl.util.constants.InequalityType

      Retrieves the specific classification of the inequality represented by the current instance. This method acts as an accessor for the internal `type` attribute, returning the `InequalityType` value that defines the relational operator (such as less-than or greater-than) governing the equation. As this is a read-only operation, it has no side effects and simply exposes the state of the object for use by solvers, formatters, or other dependent logic.

      :return: The specific type of inequality represented by this instance.

      :rtype: InequalityType



   .. py:method:: greater_then(exp: fuzzy_dl_owl2.fuzzydl.milp.expression.Expression) -> Self
      :staticmethod:


      Creates and returns a new `Inequation` instance representing a "greater than" relationship involving the provided expression. This static method acts as a factory, wrapping the given `Expression` object within an `Inequation` structure and explicitly setting the inequality type to `GREATER_THAN`. It does not modify the input expression and relies on the `Inequation` constructor to handle the specific initialization logic.

      :param exp: The expression operand to be used in the greater-than inequality.
      :type exp: Expression

      :return: Returns a new Inequation instance representing a greater-than inequality with the provided expression.

      :rtype: typing.Self



   .. py:method:: is_zero() -> bool

      Determines whether the underlying expression of the inequation evaluates to zero. It returns True only if all coefficients of the terms in the expression are zero and the constant term is also zero, indicating that the expression is identically zero regardless of variable values.

      :return: True if the expression is zero (i.e., all coefficients and the constant term are zero), otherwise False.

      :rtype: bool



   .. py:method:: less_than(exp: fuzzy_dl_owl2.fuzzydl.milp.expression.Expression) -> Self
      :staticmethod:


      Factory for  $E \le 0$.

      :param exp: The expression representing the left-hand side of the inequality.
      :type exp: Expression

      :return: Returns a new instance representing a "less than" inequality involving the provided expression.
      :rtype: typing.Self



   .. py:attribute:: expr
      :type:  fuzzy_dl_owl2.fuzzydl.milp.expression.Expression


   .. py:attribute:: type
      :type:  fuzzy_dl_owl2.fuzzydl.util.constants.InequalityType


.. py:data:: EqualTo

.. py:data:: GreaterThan

.. py:data:: LessThan
