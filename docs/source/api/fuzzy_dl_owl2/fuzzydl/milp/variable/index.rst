fuzzy_dl_owl2.fuzzydl.milp.variable
===================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.milp.variable



.. ── LLM-GENERATED DESCRIPTION START ──

A symbolic variable class designed for linear expressions within mixed-integer linear programming contexts, specifically to represent degrees of satisfaction in fuzzy description logic ontologies.


Description
-----------


The implementation encapsulates essential properties such as a unique identifier, a specific domain type, and numeric bounds that are automatically configured based on the variable's classification. Design decisions include the use of static factory methods to simplify the instantiation of specific variable types like binary or continuous, while a class-level counter ensures the generation of unique sequential names when explicit identifiers are not provided. Logic for boundary management is tightly coupled with the variable type, where setting a variable to binary or semi-continuous automatically constrains the domain between zero and one, whereas continuous or integer types default to infinite bounds. Equality and hashing behaviors rely entirely on the variable's string representation, allowing instances to be used effectively within hash-based collections, and the class further supports cloning to create independent copies of existing variables.

.. ── LLM-GENERATED DESCRIPTION END ──

Attributes
----------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.milp.variable.BinaryVar
   fuzzy_dl_owl2.fuzzydl.milp.variable.FreeVar
   fuzzy_dl_owl2.fuzzydl.milp.variable.IntegerVar
   fuzzy_dl_owl2.fuzzydl.milp.variable.UpVar


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.milp.variable.Variable


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_milp_variable_Variable.png
       :alt: UML Class Diagram for Variable
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **Variable**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_milp_variable_Variable.pdf
       :alt: UML Class Diagram for Variable
       :align: center
       :width: 11.0cm
       :class: uml-diagram

       UML Class Diagram for **Variable**

.. py:class:: Variable(name: str, v_type: fuzzy_dl_owl2.fuzzydl.util.constants.VariableType)

   This class models a symbolic variable used within linear expressions, typically to represent degrees of satisfaction in fuzzy description logic ontologies. It encapsulates properties such as a unique name, a specific type (e.g., binary, integer, or continuous), and corresponding lower and upper bounds that are automatically adjusted based on the variable type. Users can instantiate variables directly or utilize static factory methods to create specific variable types, while a class-level counter facilitates the automatic generation of unique sequential names. Additionally, the class provides functionality to flag variables as datatype fillers and supports cloning for creating independent copies.

   :param VARIABLE_NAME: Default prefix used for generating names of new variables.
   :type VARIABLE_NAME: str
   :param VARIABLE_NUMBER: Counter used to generate unique identifiers for automatically created variables.
   :type VARIABLE_NUMBER: int
   :param lower_bound: The minimum value the variable can assume.
   :type lower_bound: float
   :param upper_bound: The upper limit of the variable's domain, representing the maximum value it can assume.
   :type upper_bound: float
   :param name: Unique identifier for the variable instance, determining its string representation and equality.
   :type name: str
   :param type: An enumeration specifying the variable's domain (e.g., binary, continuous, integer), which determines its valid value range and implicitly sets its lower and upper bounds.
   :type type: VariableType
   :param datatype_filler: Flag indicating whether the variable is a filler value for a datatype restriction.
   :type datatype_filler: bool


   .. py:method:: __eq__(value: Self) -> bool

      Determines equality between the current instance and another object by comparing their string representations. The method converts both `self` and the provided `value` to strings and returns `True` if these representations are identical, otherwise `False`. This implies that two distinct objects are considered equal if they produce the same string output, and the comparison does not depend on object identity or specific attribute values beyond what is captured by the `__str__` method. Note that this implementation does not perform strict type checking on the input value, meaning it will attempt to compare against any object that supports string conversion.

      :param value: The instance to compare against the current object, where equality is determined by comparing their string representations.
      :type value: typing.Self

      :return: True if the string representation of the current instance is equal to the string representation of the provided value, otherwise False.

      :rtype: bool



   .. py:method:: __hash__() -> int

      Returns the hash value for the `Variable` instance, enabling its use in hash-based collections like dictionaries and sets. The hash is calculated by converting the object to its string representation and hashing that string. Consequently, the hash value is directly tied to the output of the object's `__str__` method, meaning that any change to the object's state which alters its string representation will result in a different hash.

      :return: An integer hash value derived from the object's string representation.

      :rtype: int



   .. py:method:: __ne__(value: object) -> bool

      Determines whether the current `Variable` instance is not equal to the specified value. This method implements the behavior of the inequality operator (`!=`) by returning the logical negation of the equality comparison. Consequently, its behavior regarding type compatibility and comparison logic is entirely dependent on the implementation of the `__eq__` method; if `__eq__` returns `NotImplemented` or raises an error for a given type, this method will propagate that behavior. There are no side effects associated with this operation.

      :param value: The object to compare with the current instance.
      :type value: object

      :return: True if the object is not equal to the specified value, otherwise False.

      :rtype: bool



   .. py:method:: __repr__() -> str

      Returns a string representation of the Variable instance, intended for debugging and interactive use. This method delegates directly to the `__str__` implementation, ensuring that the output is identical to the user-facing string representation. Consequently, any formatting logic or exceptions raised during string conversion will be reflected in the result of this method.

      :return: A string representation of the object, equivalent to the result of str(self).

      :rtype: str



   .. py:method:: __str__() -> str

      Returns the string representation of the Variable instance, which is defined as the value of its `name` attribute. This method is automatically invoked by built-in functions like `str()` and `print()` to provide a human-readable identifier for the object. The operation has no side effects and relies on the `name` attribute being present on the instance.

      :return: Returns the name of the object.

      :rtype: str



   .. py:method:: clone() -> Self

      Creates and returns a new `Variable` instance that is a copy of the current object. The new instance is initialized with the same `name` and `type` attributes as the original, ensuring that the two objects are distinct but share the same initial data. This method does not modify the original `Variable` instance; however, if the `name` or `type` attributes are mutable objects, the clone will reference the same underlying objects rather than creating deep copies of them.

      :return: A new instance of the class that is a copy of the current object.

      :rtype: typing.Self



   .. py:method:: get_binary_variable(name: str) -> Self
      :staticmethod:


      Creates and returns a new variable instance constrained to binary values, typically representing a boolean state or a yes/no decision. This factory method accepts a string identifier for the variable and initializes it with the specific type attribute required for binary constraints within the optimization model. As a static method, it serves as a convenient constructor for generating binary variables without requiring an existing instance of the class.

      :param name: The identifier or label for the binary variable.
      :type name: str

      :return: A new binary variable instance with the specified name.

      :rtype: typing.Self



   .. py:method:: get_continuous_variable(name: str) -> Self
      :staticmethod:


      Creates a new instance of the Variable class specifically configured to represent a continuous variable. This static method accepts a single string argument representing the variable's name and initializes the object with the type set to CONTINUOUS. The operation has no side effects on existing state, as it simply constructs and returns a new object, though the behavior depends on the underlying Variable constructor's handling of the provided name argument.

      :param name: The identifier or label for the continuous variable.
      :type name: str

      :return: A new continuous variable instance initialized with the specified name.

      :rtype: typing.Self



   .. py:method:: get_datatype_filler_type() -> bool

      Returns the boolean value of the `datatype_filler` attribute associated with this variable. This method serves as a getter to determine if the variable is flagged as a datatype filler. It does not modify the object's state and has no side effects, though it will raise an AttributeError if the underlying attribute has not been initialized.

      :return: Returns the boolean value of the `datatype_filler` attribute.

      :rtype: bool



   .. py:method:: get_integer_variable(name: str) -> Self
      :staticmethod:


      This static method acts as a factory for creating a `Variable` instance specifically configured to represent an integer type. It accepts a string argument representing the variable's name and returns a new `Variable` object initialized with that name and the type set to `VariableType.INTEGER`. The method does not modify any existing state and relies on the underlying `Variable` constructor for handling the provided name.

      :param name: The identifier or label for the integer variable.
      :type name: str

      :return: A new instance representing an integer variable with the specified name.

      :rtype: typing.Self



   .. py:method:: get_lower_bound() -> float

      Retrieves the lower bound value currently assigned to this variable instance. This method acts as a simple accessor for the `lower_bound` attribute, returning the numerical constraint that defines the minimum limit for the variable. It performs no computation and does not alter the state of the object, though the specific meaning of the returned value—such as whether it represents a hard constraint or a default initialization—depends on the broader logic of the `Variable` class.

      :return: The lower bound value.

      :rtype: float



   .. py:method:: get_new_variable(v_type: fuzzy_dl_owl2.fuzzydl.util.constants.VariableType) -> Self
      :staticmethod:


      Generates a new `Variable` instance with a unique, auto-generated name based on the specified variable type. The method increments an internal class-level counter to ensure that each subsequent call produces a distinct identifier, combining a static name prefix with the current counter value. This process modifies the class state by updating the counter, meaning the generated names are sequential and dependent on the history of calls to this method.

      :param v_type: The type of the new variable instance to be created.
      :type v_type: VariableType

      :return: A new Variable instance with a unique, auto-generated name and the specified type.

      :rtype: typing.Self



   .. py:method:: get_semi_continuous_variable(name: str) -> Self
      :staticmethod:


      This static method serves as a factory for creating a Variable instance with its type explicitly set to semi-continuous. It accepts a string representing the variable's name and returns a new Variable object configured accordingly. By using this method, the caller ensures the variable is initialized with the correct classification for optimization contexts where the variable must be either zero or within a specific continuous range.

      :param name: The identifier or label for the variable instance.
      :type name: str

      :return: A Variable instance representing a semi-continuous variable with the specified name.

      :rtype: typing.Self



   .. py:method:: get_type() -> fuzzy_dl_owl2.fuzzydl.util.constants.VariableType

      Retrieves the type classification associated with the variable instance. This method returns the value stored in the internal `type` attribute, which defines the specific data type or category of the variable. It is a read-only operation that does not modify the object's state, and it simply returns whatever value is currently assigned to the type attribute.

      :return: The type of the variable represented by this instance.

      :rtype: VariableType



   .. py:method:: get_upper_bound() -> float

      Retrieves the upper bound limit defined for this variable. This method returns the floating-point value stored in the `upper_bound` attribute, representing the maximum permissible value the variable can assume within its specific context. As a simple accessor, it performs no state modifications or calculations, directly exposing the internal constraint value to the caller.

      :return: The upper bound value.

      :rtype: float



   .. py:method:: set_binary_variable() -> None

      Marks the current variable instance as a binary variable, effectively restricting its domain to discrete values of 0 and 1. This method updates the variable's internal type attribute by delegating to the `set_type` method with the appropriate enumeration value. As this operation modifies the object's state in place, any previous type assignment associated with the variable will be overwritten.



   .. py:method:: set_datatype_filler_variable() -> None

      Marks the variable instance as a datatype filler by setting the `datatype_filler` attribute to `True`. This operation is typically used to designate the variable as a placeholder or default value intended to satisfy a specific data type requirement within a schema or data processing pipeline. The method modifies the object's state in place and does not return any value.



   .. py:method:: set_name(name: str) -> None

      Assigns the provided string identifier to the instance, overwriting any existing value stored in the name attribute. This method directly mutates the object's state to reflect the new label. While the signature expects a string, the implementation performs no type validation, meaning any object passed as the name will be stored.

      :param name: The new name to assign to the instance.
      :type name: str



   .. py:method:: set_type(v_type: fuzzy_dl_owl2.fuzzydl.util.constants.VariableType) -> None

      Updates the variable's type to the specified value and automatically adjusts the variable's bounds to match standard defaults for that type. When the type is set to BINARY or SEMI_CONTINUOUS, the lower and upper bounds are reset to 0.0 and 1.0, respectively. For CONTINUOUS or INTEGER types, the bounds are set to negative and positive infinity. This method modifies the variable's state in place and asserts that the provided type is valid.

      :param v_type: The type of the variable (e.g., continuous, integer, binary, or semi-continuous). Setting this type automatically updates the variable's default bounds to standard values appropriate for the selection.
      :type v_type: VariableType



   .. py:attribute:: VARIABLE_NAME
      :type:  str
      :value: 'y'



   .. py:attribute:: VARIABLE_NUMBER
      :type:  int
      :value: 0



   .. py:attribute:: datatype_filler
      :type:  bool
      :value: False



   .. py:attribute:: lower_bound
      :type:  float
      :value: 0.0



   .. py:attribute:: name
      :type:  str


   .. py:attribute:: type
      :type:  fuzzy_dl_owl2.fuzzydl.util.constants.VariableType
      :value: None



   .. py:attribute:: upper_bound
      :type:  float
      :value: 0.0



.. py:data:: BinaryVar

.. py:data:: FreeVar

.. py:data:: IntegerVar

.. py:data:: UpVar
