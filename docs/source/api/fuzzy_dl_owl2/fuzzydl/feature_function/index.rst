fuzzy_dl_owl2.fuzzydl.feature_function
======================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.feature_function



.. ── LLM-GENERATED DESCRIPTION START ──

A class representing mathematical expressions over features that supports arithmetic operations and conversion into linear programming constraints.


Description
-----------


Software components defined here provide a mechanism to construct and manipulate mathematical expressions involving atomic features, constants, and arithmetic operations such as summation, subtraction, and scalar multiplication. The design utilizes a polymorphic initialization strategy where the specific structure of the expression—whether it is a simple variable, a numeric constant, or a complex composite operation—is determined dynamically based on the types and quantities of arguments provided during instantiation. This intermediate representation allows for recursive traversal to extract dependencies, such as collecting all unique feature names referenced within the expression tree. Furthermore, the logic includes functionality to translate these abstract definitions into concrete linear programming expressions by resolving atomic features to solver variables using the relational context of a specific individual and a helper utility for mixed-integer linear programming (MILP) models.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.feature_function.FeatureFunction


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_feature_function_FeatureFunction.png
       :alt: UML Class Diagram for FeatureFunction
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **FeatureFunction**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_feature_function_FeatureFunction.pdf
       :alt: UML Class Diagram for FeatureFunction
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **FeatureFunction**

.. py:class:: FeatureFunction(feature: Self)
              FeatureFunction(feature: str)
              FeatureFunction(n: float)
              FeatureFunction(feature: list[Self])
              FeatureFunction(feature1: Self, feature2: Self)
              FeatureFunction(n: float, feature: Self)

   This class encapsulates a mathematical expression defined over features, supporting atomic variables, constants, and arithmetic operations such as summation, subtraction, and scalar multiplication. The specific type of function is determined polymorphically at initialization based on the provided arguments—for instance, passing a string defines an atomic feature, a float defines a constant, and a list of functions defines a sum. It serves as an intermediate representation that can be traversed to extract dependencies or converted into a concrete linear programming expression via the `to_expression` method, which resolves atomic features to variables based on an individual's relations.

   :raises ValueError: Raised if the arguments passed to the constructor do not match any of the valid signatures for defining a feature function, such as having an incorrect number of arguments or incompatible type combinations.


   .. py:method:: __feature_function_init_1(feature: str) -> None

      Initializes the object to represent an atomic feature function identified by the provided string. This configuration sets the instance's type to ATOMIC, prepares an empty list for potential child functions, assigns the specific feature name, and resets the internal counter to zero. The method directly mutates the instance's state to establish a base-level feature representation, assuming the input string is a valid identifier.

      :param feature: The name of the atomic feature.
      :type feature: str



   .. py:method:: __feature_function_init_2(n: float) -> None

      Initializes the feature function instance to represent a constant numeric value. It sets the type attribute to `NUMBER`, assigns the provided float argument to the `n` attribute, and explicitly clears the list of child functions and the feature name string to ensure a clean state.

      :param n: The numeric value associated with the feature function.
      :type n: float



   .. py:method:: __feature_function_init_3(feature: list[Self]) -> None

      Configures the instance to represent a summation operation over a provided list of subordinate feature functions. It sets the internal type to `SUM` and stores the input list within the instance for later aggregation. Additionally, this method resets the feature name identifier and the numeric coefficient to their default states of an empty string and 0.0, respectively, ensuring the composite function is initialized without residual values from other potential configurations.

      :param feature: A list of feature functions to be summed.
      :type feature: list[typing.Self]



   .. py:method:: __feature_function_init_4(feature1: Self, feature2: Self) -> None

      Initializes the instance to represent a subtraction operation between two feature functions. It configures the internal type to `SUBTRACTION` and stores the provided `feature1` and `feature2` as the operands for the calculation. As a side effect, this method explicitly clears the `feature` string attribute and resets the `n` numeric attribute to zero, ensuring the object state is consistent with a binary operation rather than a leaf node.

      :param feature1: The first operand in the subtraction operation, representing the value from which the second operand is subtracted.
      :type feature1: typing.Self
      :param feature2: The feature to subtract from the first feature.
      :type feature2: typing.Self



   .. py:method:: __feature_function_init_5(n: float, feature: Self) -> None

      Initializes the instance to represent a product feature function defined by a scalar coefficient and a nested feature. It sets the function type to PRODUCT, assigns the scalar value `n`, and stores the provided `feature` object in a list of sub-features. This operation overwrites existing attributes, specifically resetting the string-based feature identifier to an empty string.

      :param n: The numeric coefficient or scalar value associated with the feature function.
      :type n: float
      :param feature: The feature function instance to be used as a factor in the product operation.
      :type feature: typing.Self



   .. py:method:: __feature_function_init_6(feature: Self) -> None

      Copies the core attributes from an existing `FeatureFunction` instance to the current object. Specifically, it assigns the `type`, `f`, `feature`, and `n` attributes from the provided `feature` argument to `self`. This method performs a shallow copy, meaning mutable attributes like the list `f` will be shared between the two instances rather than deep-copied.

      :param feature: An existing instance of the same class from which to copy attributes to initialize the current instance.
      :type feature: typing.Self



   .. py:method:: __repr__() -> str

      Returns the official string representation of the object by delegating to the `__str__` method. This ensures that the output is identical to the informal string representation, providing a consistent textual format for debugging and logging. The specific content of the returned string depends entirely on the implementation of the string conversion logic within the class.

      :return: Returns the string representation of the object, identical to the output of `str()`.

      :rtype: str



   .. py:method:: __str__() -> str

      Returns a human-readable string representation of the feature function, formatted according to its specific type. For atomic features, it returns the feature name, while numeric types return the string value of the number. Composite operations are represented as mathematical expressions: products display a scalar multiplied by a sub-feature, subtractions show the difference between two sub-features, and sums join multiple sub-features with plus signs. If the feature function type does not match any known category, an empty string is returned.

      :return: A string representation of the feature function, formatted as a mathematical expression or feature name based on its type.

      :rtype: str



   .. py:method:: get_features() -> set[str]

      Recursively collects and returns a set of feature names that are utilized within the feature function's definition. The method handles different function types by traversing the internal structure: it returns the direct feature name for atomic types, aggregates features from all sub-functions for sums, combines features from the first two sub-functions for subtractions, and extracts features only from the first sub-function for products. This operation is read-only and does not alter the state of the object.

      :return: A set containing the unique names of all features involved in the function.

      :rtype: set[str]



   .. py:method:: get_number() -> float

      Retrieves the numeric value stored within the instance. This method acts as a getter for the internal attribute `n`, returning its current value as a float. The operation is read-only and does not modify the state of the object or any external entities.

      :return: The floating-point number associated with the instance.

      :rtype: float



   .. py:method:: get_type() -> fuzzy_dl_owl2.fuzzydl.util.constants.FeatureFunctionType

      Retrieves the type classification of the feature function instance. This method returns the value stored in the internal `type` attribute, which typically defines the category or operational nature of the feature function within the broader system. As a simple accessor, this method performs no modifications to the object's state and has no side effects.

      :return: The type of the feature function.

      :rtype: FeatureFunctionType



   .. py:method:: to_expression(a: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, milp: fuzzy_dl_owl2.fuzzydl.milp.milp_helper.MILPHelper) -> Optional[fuzzy_dl_owl2.fuzzydl.milp.expression.Expression]

      Converts the abstract definition of the feature function into a concrete mathematical expression suitable for a MILP solver, evaluated in the context of a specific individual `a`. Depending on the function's type, this involves retrieving the solver variable associated with a related individual for atomic features, generating constant terms for numbers, or recursively combining the expressions of child functions using arithmetic operations such as summation, subtraction, or scalar multiplication. The method relies on the provided `MILPHelper` to resolve individuals to variables and includes assertions to ensure the structural integrity of the function definition, such as the presence of required relations or a valid number of sub-functions. It returns the resulting `Expression` object, or `None` if the function type is unrecognized.

      :param a: The individual entity serving as the context for resolving feature relations and constructing the expression.
      :type a: Individual
      :param milp: Helper object used to look up variables associated with individuals in the MILP model.
      :type milp: MILPHelper

      :return: Returns an Expression object representing the mathematical formulation of the feature function for the given individual, or None if the function type is unsupported.

      :rtype: typing.Optional[Expression]


