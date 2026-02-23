fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_number.triangular_fuzzy_number
===========================================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_number.triangular_fuzzy_number



.. ── LLM-GENERATED DESCRIPTION START ──

A Python class that models triangular fuzzy numbers, providing arithmetic and logical operations alongside utilities for defuzzification and range management.


Description
-----------


The software models uncertain numerical values using a triangular membership function defined by three distinct parameters representing the lower bound, the peak, and the upper bound. It supports flexible initialization, allowing instances to be created either with or without an explicit string identifier, while enforcing strict validation on the input types and argument counts. Arithmetic operations such as addition, subtraction, multiplication, and division are implemented to produce new instances based on interval arithmetic principles, ensuring that the original operands remain unmodified. Furthermore, the logic integrates with a broader framework by delegating fuzzy logical operations like conjunction and disjunction to an external operator handler, while also providing utilities for defuzzification through the calculation of the Best Non-Fuzzy Performance. Class-level configuration allows for the definition of a global range or universe of discourse, which influences how these fuzzy numbers are identified and managed within the system.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_number.triangular_fuzzy_number.TriangularFuzzyNumber


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_concrete_fuzzy_number_triangular_fuzzy_number_TriangularFuzzyNumber.png
       :alt: UML Class Diagram for TriangularFuzzyNumber
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **TriangularFuzzyNumber**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_concrete_fuzzy_number_triangular_fuzzy_number_TriangularFuzzyNumber.pdf
       :alt: UML Class Diagram for TriangularFuzzyNumber
       :align: center
       :width: 11.1cm
       :class: uml-diagram

       UML Class Diagram for **TriangularFuzzyNumber**

.. py:class:: TriangularFuzzyNumber(name: str, a: float, b: float, c: float)
              TriangularFuzzyNumber(a: float, b: float, c: float)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.concept.concrete.triangular_concrete_concept.TriangularConcreteConcept`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_number.triangular_fuzzy_number.TriangularFuzzyNumber
      :parts: 1
      :private-bases:


   This class models a triangular fuzzy number defined by three parameters representing the lower bound, the peak (where membership is 1), and the upper bound. It allows for the representation of uncertain values where the degree of membership increases linearly from the lower bound to the peak and decreases linearly from the peak to the upper bound. Instances can be initialized using either three numerical values or a name string followed by the three values. The class supports standard arithmetic operations such as addition, subtraction, multiplication, and division, which return new instances representing the result. Additionally, it provides functionality for logical operations like negation, conjunction, and disjunction, as well as utilities to calculate the Best Non-Fuzzy Performance (BNP) for defuzzification and to check if the number is effectively a crisp value. Class-level methods are available to define a global range for the fuzzy numbers, affecting how they are identified or named.

   :param K1: The lower bound of the range defining the domain of the fuzzy numbers. This class variable defaults to negative infinity and can be configured using the `set_range` method.
   :type K1: float
   :param K2: The upper bound of the range of the fuzzy numbers, which is a class variable that can be set using the set_range method.
   :type K2: float


   .. py:method:: __add__(other: Self) -> Self

      Performs arithmetic addition between two triangular fuzzy numbers by summing their respective lower bounds, modal values, and upper bounds. This operation creates and returns a new `TriangularFuzzyNumber` instance representing the result, ensuring that the original operands remain unmodified. The method expects the `other` argument to be an instance of the same class and relies on the underlying numeric types of the parameters to support the addition operator.

      :param other: Another TriangularFuzzyNumber instance to add to the current instance.
      :type other: typing.Self

      :return: A new TriangularFuzzyNumber representing the sum of the current instance and the provided instance.

      :rtype: typing.Self



   .. py:method:: __and__(value: Self) -> Self

      Computes the logical intersection (AND) of this triangular fuzzy number with another provided value, effectively performing a fuzzy logic operation. This method overloads the bitwise AND operator (`&`) and delegates the specific calculation logic to the `OperatorConcept.and_` static method. The operation returns a new `TriangularFuzzyNumber` instance representing the result of the intersection without modifying the original operands; if the input numbers do not overlap, the resulting instance typically represents an empty or null set based on the underlying implementation.

      :param value: The other operand to perform the AND operation with.
      :type value: typing.Self

      :return: A new instance representing the conjunction of the current instance and the provided value.

      :rtype: typing.Self



   .. py:method:: __eq__(other: Self) -> bool

      Checks whether the current triangular fuzzy number is equivalent to another object by comparing their types and defining parameters. Equality is established only if both objects are instances of the exact same class and their respective attributes a, b, and c are identical. This strict type check ensures that instances of subclasses are not considered equal to instances of the parent class, even if their numerical values match. The operation has no side effects and returns a boolean value indicating the result of the comparison.

      :param other: The object to compare against. Equality is determined by identical types and matching attributes a, b, and c.
      :type other: typing.Self

      :return: True if the objects are of the same type and have equal attributes `a`, `b`, and `c`, otherwise False.

      :rtype: bool



   .. py:method:: __hash__() -> int

      Computes an integer hash value for the instance, allowing it to be used as a key in dictionaries and a member of sets. The implementation derives the hash from the object's string representation, meaning that two instances with identical string representations will yield the same hash. This method relies on the stability and uniqueness of the `__str__` implementation to maintain the invariant that equal objects must have equal hash values.

      :return: An integer hash value computed from the string representation of the object.

      :rtype: int



   .. py:method:: __mul__(other: Self) -> Self

      Performs component-wise multiplication between the current instance and another triangular fuzzy number, returning a new instance representing the product. The calculation multiplies the corresponding lower bound, peak, and upper bound values of the two operands directly. This operation assumes that the resulting values maintain the required ordering for a valid triangular fuzzy number, which may not hold if the operands contain negative values. The original objects remain unmodified as a new instance is created for the result.

      :param other: Another TriangularFuzzyNumber instance to multiply with the current instance.
      :type other: typing.Self

      :return: A new TriangularFuzzyNumber representing the product of the current instance and the provided operand.

      :rtype: typing.Self



   .. py:method:: __ne__(other: Self) -> bool

      Evaluates whether the current triangular fuzzy number is distinct from the specified other instance. This method implements the inequality operator by negating the result of the equality comparison, ensuring consistency between the two operations. If the provided object is not of the same type or is incompatible, the behavior depends on the underlying equality check, typically resulting in a return value of True. The operation does not modify the state of either object.

      :param other: The object to compare against the current instance.
      :type other: typing.Self

      :return: True if the instance is not equal to the other object, False otherwise.

      :rtype: bool



   .. py:method:: __neg__() -> TriangularFuzzyNumber

      Implements the unary negation operator for the triangular fuzzy number, allowing the instance to be prefixed with a minus sign (e.g., `-x`). The calculation is delegated to the `not_` method of the `OperatorConcept` class, which handles the specific logic for determining the negated value, often interpreted as the logical complement in fuzzy logic contexts. This method returns a new `TriangularFuzzyNumber` instance without modifying the original object.

      :return: A new TriangularFuzzyNumber representing the negation of the current instance.

      :rtype: TriangularFuzzyNumber



   .. py:method:: __or__(value: Self) -> Self

      Implements the bitwise OR operator (`|`) to perform a logical disjunction or union between the current triangular fuzzy number and another provided value. This operation typically calculates the maximum of the membership functions of the two operands, resulting in a new `TriangularFuzzyNumber` that represents the combined possibility distribution. The method does not modify the original instances in place but instead returns a new object containing the result of the fuzzy OR calculation.

      :param value: The right-hand operand for the logical OR operation.
      :type value: typing.Self

      :return: The result of the OR operation between the current instance and the provided value.

      :rtype: typing.Self



   .. py:method:: __sub__(other: Self) -> Self

      Computes the arithmetic difference between this triangular fuzzy number and another provided instance. The resulting fuzzy number is derived by applying interval arithmetic principles: the new lower bound is the difference between the current lower bound and the other's upper bound, the new modal value is the difference between the two modal values, and the new upper bound is the difference between the current upper bound and the other's lower bound. This operation returns a new `TriangularFuzzyNumber` object without modifying the original operands.

      :param other: The instance to subtract from the current one.
      :type other: typing.Self

      :return: A new TriangularFuzzyNumber representing the result of subtracting the other fuzzy number from this one.

      :rtype: typing.Self



   .. py:method:: __tringular_fn_init_1(name: str, a: float, b: float, c: float) -> None

      Initializes the triangular fuzzy number instance with a specific name and the three defining parameters (a, b, c) that represent the triangular distribution. This method delegates the core initialization to the parent class, passing the name, internal constants K1 and K2, and the coordinate values. It also explicitly sets the concept type to FUZZY_NUMBER and ensures the instance has a valid name, using the provided string or generating one automatically if the input is empty.

      :param name: The identifier or label for the fuzzy number. If a falsy value is provided, a default name is generated automatically.
      :type name: str
      :param a: The first vertex of the triangular membership function, representing the lower bound of the support.
      :type a: float
      :param b: The peak value of the triangular fuzzy number.
      :type b: float
      :param c: The right endpoint of the triangular fuzzy number's support interval.
      :type c: float



   .. py:method:: __tringular_fn_init_2(a: float, b: float, c: float) -> None

      This internal initialization helper sets up the instance using three numerical parameters that define the vertices of the triangular membership function. It accepts the lower bound, the peak, and the upper bound as floating-point values, constructs a default string label from these coordinates, and delegates the actual object initialization to the primary constructor. By doing so, it ensures the fuzzy number is configured with the specified shape parameters while automatically generating a descriptive identifier.

      :param a: The first of three numerical values used to initialize the object.
      :type a: float
      :param b: The second of three float values used to initialize the object.
      :type b: float
      :param c: The third float value used to initialize the object.
      :type c: float



   .. py:method:: __truediv__(other: Self) -> Self

      Performs division between the current triangular fuzzy number and another provided fuzzy number, returning a new instance representing the quotient. The calculation follows the extension principle for fuzzy arithmetic, where the resulting triplet is derived by dividing the dividend's lower bound by the divisor's upper bound, the modal values by each other, and the dividend's upper bound by the divisor's lower bound. This method includes a safeguard against division by zero; if any component of the divisor is zero, it triggers an error utility and returns None instead of performing the operation.

      :param other: The fuzzy number instance to divide by. Its components must not be zero to avoid division errors.
      :type other: typing.Self

      :return: A new TriangularFuzzyNumber representing the quotient of the division, or None if the divisor contains zero.

      :rtype: typing.Self



   .. py:method:: add(t1: Self, t2: Self) -> Self
      :staticmethod:


      Performs arithmetic addition on two triangular fuzzy numbers. This static method takes two instances of the class and returns a new instance representing their sum. The operation delegates to the class's addition operator, combining the parameters without modifying the original objects.

      :param t1: The first triangular fuzzy number to add.
      :type t1: typing.Self
      :param t2: The second triangular fuzzy number to be added.
      :type t2: typing.Self

      :return: A new triangular fuzzy number representing the sum of the two input numbers.

      :rtype: typing.Self



   .. py:method:: clone() -> Self

      Creates and returns a distinct copy of the current triangular fuzzy number by instantiating a new object with the same name and defining parameters (a, b, c). This method ensures that the returned instance is independent of the original, meaning modifications to one will not affect the other. Note that because the clone is generated via the class constructor, any attributes not passed as initialization arguments—such as derived properties or internal caches—will not be transferred to the new instance.

      :return: A new TriangularFuzzyNumber instance initialized with the same parameters as the current instance.

      :rtype: typing.Self



   .. py:method:: compute_name() -> str

      Generates a formatted string representation of the triangular fuzzy number by combining its defining parameters into a specific notation. The resulting string follows the pattern "(k1, k2; a, b, c)", incorporating the object's internal attributes `k1`, `k2`, `a`, `b`, and `c`. This operation is read-only and does not modify the state of the object, though it assumes that all required attributes are present; otherwise, an `AttributeError` will be raised.

      :return: A string representation of the object's attributes formatted as "(k1, k2; a, b, c)".

      :rtype: str



   .. py:method:: divided_by(t1: Self, t2: Self) -> Self
      :staticmethod:


      Calculates the quotient of two triangular fuzzy numbers and returns a new instance representing the result. This static method serves as a wrapper for the division operator, performing the necessary arithmetic to determine the fuzzy number resulting from the division of the first argument by the second. Care must be taken to ensure the denominator does not include zero within its support range, as this can lead to undefined behavior or exceptions. The operation is pure, meaning it does not modify the state of the input instances.

      :param t1: The triangular fuzzy number acting as the dividend.
      :type t1: typing.Self
      :param t2: The triangular fuzzy number to divide by.
      :type t2: typing.Self

      :return: A new triangular fuzzy number representing the quotient of the two input numbers.

      :rtype: typing.Self



   .. py:method:: get_best_non_fuzzy_performance() -> float

      Calculates the Best Non-fuzzy Performance (BNP), a defuzzified crisp value representing the triangular fuzzy number. This is achieved by computing the arithmetic mean of the three defining parameters of the triangle. The resulting value is rounded to a standard precision before being returned as a float.

      :return: The defuzzified crisp value representing the Best Non-Fuzzy Performance (BNP), calculated as the arithmetic mean of the fuzzy number's parameters.

      :rtype: float



   .. py:method:: has_defined_range() -> bool
      :staticmethod:


      This static method verifies whether the global range or universe of discourse for triangular fuzzy numbers has been established. It inspects the class-level attribute `K1`, which serves as the lower bound of the range, and returns `True` only if this value is not negative infinity. Consequently, the method indicates that the range is undefined if `K1` remains at its default negative infinity state, and it performs this check without modifying any object state.

      :return: True if the range of the fuzzy numbers has been defined, False otherwise.

      :rtype: bool



   .. py:method:: is_concrete() -> bool

      This method indicates whether the instance represents a concrete value, as opposed to an abstract or symbolic entity. For the `TriangularFuzzyNumber` class, the method unconditionally returns `True`, signifying that all instances are considered concrete. This property can be used to distinguish specific fuzzy numbers from other types in the system that may represent operations or undefined variables.

      :return: True, indicating that the object is concrete.

      :rtype: bool



   .. py:method:: is_number() -> bool

      Determines whether the fuzzy number represents a crisp value rather than an interval by verifying that the lower bound, modal value, and upper bound are identical. This condition implies that the triangular distribution has collapsed to a single point, effectively removing any fuzziness or uncertainty. The method returns True if all three defining components are equal, and False otherwise, without modifying the instance state.

      :return: True if the attributes a, b, and c are all equal; otherwise, False.

      :rtype: bool



   .. py:method:: minus(t1: Self, t2: Self) -> Self
      :staticmethod:


      Calculates the difference between two triangular fuzzy numbers by subtracting the second operand from the first. This static method returns a new triangular fuzzy number instance representing the result of the fuzzy arithmetic operation, leaving the original operands unmodified. The operation relies on the class's underlying subtraction logic to compute the resulting fuzzy set.

      :param t1: The triangular fuzzy number from which `t2` is subtracted.
      :type t1: typing.Self
      :param t2: The triangular fuzzy number to subtract.
      :type t2: typing.Self

      :return: A new triangular fuzzy number representing the difference between the two input numbers.

      :rtype: typing.Self



   .. py:method:: set_range(min_range: float, max_range: float) -> None
      :staticmethod:


      Updates the class-level range boundaries used by the `TriangularFuzzyNumber` class by assigning the provided `min_range` value to the class attribute `K1` and the `max_range` value to `K2`. As a static method, it modifies the global state of the class rather than an individual instance, affecting all subsequent operations that depend on these boundaries. While the method accepts any floating-point numbers, callers should ensure that `min_range` is less than `max_range` to maintain logical consistency, as no validation is performed to enforce this constraint.

      :param min_range: The lower bound of the range.
      :type min_range: float
      :param max_range: The upper bound of the range for the triangular fuzzy number.
      :type max_range: float



   .. py:method:: times(t1: Self, t2: Self) -> Self
      :staticmethod:


      This static method performs multiplication on two triangular fuzzy numbers. It accepts two instances of the class and returns a new instance representing the resulting fuzzy number. The actual arithmetic logic is handled by the class's multiplication operator, ensuring consistency with the defined fuzzy arithmetic rules. This operation is side-effect free, as it produces a new object rather than modifying the input arguments.

      :param t1: The first triangular fuzzy number to be multiplied.
      :type t1: typing.Self
      :param t2: The second triangular fuzzy number to multiply.
      :type t2: typing.Self

      :return: A new triangular fuzzy number representing the product of the two input numbers.

      :rtype: typing.Self



   .. py:attribute:: K1
      :type:  float


   .. py:attribute:: K2
      :type:  float

