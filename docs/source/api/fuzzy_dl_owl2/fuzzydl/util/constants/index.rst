fuzzy_dl_owl2.fuzzydl.util.constants
====================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.util.constants



.. ── LLM-GENERATED DESCRIPTION START ──

A central configuration repository for a fuzzy description logic reasoning system that defines enumerations for logic operators, concept types, solver backends, and parsing keywords.


Description
-----------


Standardizing the vocabulary and configuration options used throughout the application, the code defines a comprehensive set of enumerations to manage the complexity of fuzzy reasoning. It categorizes distinct logic constructs, such as t-norms, t-conorms, implication rules, and aggregation operators like OWA and Sugeno integrals, into specific types to ensure type safety and consistency during inference. To support the interpretation of domain-specific syntax, the definitions map reserved language keywords directly to ``pyparsing`` objects, facilitating the automated parsing of FuzzyDL commands. Furthermore, the configuration specifies computational backend settings, including supported Mixed-Integer Linear Programming solvers and variable domains, while also managing global constants for file paths and numerical limits.

.. ── LLM-GENERATED DESCRIPTION END ──

Attributes
----------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.util.constants.KNOWLEDGE_BASE_SEMANTICS
   fuzzy_dl_owl2.fuzzydl.util.constants.MAXVAL
   fuzzy_dl_owl2.fuzzydl.util.constants.MAXVAL2
   fuzzy_dl_owl2.fuzzydl.util.constants.NUMBER
   fuzzy_dl_owl2.fuzzydl.util.constants.RESULTS_PATH
   fuzzy_dl_owl2.fuzzydl.util.constants.SEPARATOR
   fuzzy_dl_owl2.fuzzydl.util.constants.STAR_SEPARATOR


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.util.constants.BlockingDynamicType
   fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType
   fuzzy_dl_owl2.fuzzydl.util.constants.ConcreteFeatureType
   fuzzy_dl_owl2.fuzzydl.util.constants.CreatedIndividualBlockingType
   fuzzy_dl_owl2.fuzzydl.util.constants.FeatureFunctionType
   fuzzy_dl_owl2.fuzzydl.util.constants.FuzzyDLKeyword
   fuzzy_dl_owl2.fuzzydl.util.constants.FuzzyLogic
   fuzzy_dl_owl2.fuzzydl.util.constants.InequalityType
   fuzzy_dl_owl2.fuzzydl.util.constants.KnowledgeBaseRules
   fuzzy_dl_owl2.fuzzydl.util.constants.LogicOperatorType
   fuzzy_dl_owl2.fuzzydl.util.constants.MILPProvider
   fuzzy_dl_owl2.fuzzydl.util.constants.RepresentativeIndividualType
   fuzzy_dl_owl2.fuzzydl.util.constants.RestrictionType
   fuzzy_dl_owl2.fuzzydl.util.constants.VariableType


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_util_constants_BlockingDynamicType.png
       :alt: UML Class Diagram for BlockingDynamicType
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **BlockingDynamicType**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_util_constants_BlockingDynamicType.pdf
       :alt: UML Class Diagram for BlockingDynamicType
       :align: center
       :width: 5.3cm
       :class: uml-diagram

       UML Class Diagram for **BlockingDynamicType**

.. py:class:: BlockingDynamicType(*args, **kwds)

   Bases: :py:obj:`enum.Enum`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.util.constants.BlockingDynamicType
      :parts: 1
      :private-bases:


   This enumeration defines the specific strategies available for controlling the expansion of individuals within a reasoning process, specifically to ensure termination by preventing infinite model generation. It provides a range of options from disabling blocking entirely to applying various logical constraints—such as subset, set, or double blocking—that determine when a new individual is considered redundant or "blocked" by an existing one. These strategies are crucial for optimizing performance and correctness in automated reasoning tasks involving dynamic creation of entities.

   :param NO_BLOCKING: Indicates that no blocking strategy is applied.
   :type NO_BLOCKING: typing.Any
   :param SUBSET_BLOCKING: A blocking strategy where a new individual is blocked if its set of predecessors is a subset of the predecessors of an existing blocked individual.
   :type SUBSET_BLOCKING: typing.Any
   :param SET_BLOCKING: A blocking strategy based on set comparisons.
   :type SET_BLOCKING: typing.Any
   :param DOUBLE_BLOCKING: A blocking strategy where a node is blocked if it is blocked by an ancestor or if it is blocked by a node that is already blocked.
   :type DOUBLE_BLOCKING: typing.Any
   :param ANYWHERE_SUBSET_BLOCKING: A dynamic blocking strategy where an individual is blocked if its concept set is a subset of the concept set of any existing individual, regardless of the individual's position in the model tree.
   :type ANYWHERE_SUBSET_BLOCKING: typing.Any
   :param ANYWHERE_SET_BLOCKING: A blocking strategy that applies set blocking conditions to any ancestor node, not just the immediate predecessor.
   :type ANYWHERE_SET_BLOCKING: typing.Any
   :param ANYWHERE_DOUBLE_BLOCKING: A blocking strategy where a node is blocked if there exists any ancestor node that satisfies the double blocking condition.
   :type ANYWHERE_DOUBLE_BLOCKING: typing.Any


   .. py:method:: __repr__() -> str

      Returns the string representation of the `BlockingDynamicType` instance. This method provides a concise identifier for the object by returning the value of its `name` attribute directly. As a result, when the instance is printed or inspected in a REPL, it displays the assigned name rather than a standard memory address or constructor representation.

      :return: The string representation of the object, specifically its name.

      :rtype: str



   .. py:method:: __str__() -> str

      Returns a human-readable string representation of the object by returning the value of the `name` attribute. This method is implicitly invoked by the `str()` built-in function, the `print()` function, and formatted string literals. Since the implementation simply accesses the attribute, it will raise an `AttributeError` if `self.name` has not been defined, and it relies on Python's default string conversion if the attribute is not already a string. The operation is read-only and does not modify the state of the instance.

      :return: The string representation of the object, which is the value of the `name` attribute.

      :rtype: str



   .. py:attribute:: ANYWHERE_DOUBLE_BLOCKING
      :value: 6



   .. py:attribute:: ANYWHERE_SET_BLOCKING
      :value: 5



   .. py:attribute:: ANYWHERE_SUBSET_BLOCKING
      :value: 4



   .. py:attribute:: DOUBLE_BLOCKING
      :value: 3



   .. py:attribute:: NO_BLOCKING
      :value: 0



   .. py:attribute:: SET_BLOCKING
      :value: 2



   .. py:attribute:: SUBSET_BLOCKING
      :value: 1



.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_util_constants_ConceptType.png
       :alt: UML Class Diagram for ConceptType
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **ConceptType**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_util_constants_ConceptType.pdf
       :alt: UML Class Diagram for ConceptType
       :align: center
       :width: 3.7cm
       :class: uml-diagram

       UML Class Diagram for **ConceptType**

.. py:class:: ConceptType(*args, **kwds)

   Bases: :py:obj:`enum.Enum`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType
      :parts: 1
      :private-bases:


   This enumeration categorizes the diverse structural forms that concepts can take within a fuzzy description logic reasoner. It encompasses standard logical constructs such as conjunctions, disjunctions, and existential or universal restrictions, alongside specialized fuzzy logic operators like Goedel and Lukasiewicz t-norms and t-conorms. Furthermore, it defines identifiers for rough set approximations (including tight and loose variants), aggregation methods like OWA and Sugeno integrals, and various weighted or thresholded concepts. By assigning a specific type to a concept, the reasoner can determine the appropriate semantic interpretation and computational algorithm to apply.

   :param AND: Represents a logical conjunction concept.
   :type AND: typing.Any
   :param GOEDEL_AND: Represents a conjunction operation using the Goedel t-norm (minimum).
   :type GOEDEL_AND: typing.Any
   :param LUKASIEWICZ_AND: Represents a conjunction operation based on the Lukasiewicz t-norm.
   :type LUKASIEWICZ_AND: typing.Any
   :param OR: Represents a standard logical disjunction concept.
   :type OR: typing.Any
   :param GOEDEL_OR: Represents the Goedel disjunction concept, a specific type of logical disjunction used by the reasoner.
   :type GOEDEL_OR: typing.Any
   :param LUKASIEWICZ_OR: Represents a Lukasiewicz disjunction concept.
   :type LUKASIEWICZ_OR: typing.Any
   :param SOME: Represents an existential restriction, indicating the existence of at least one relationship to a specific concept.
   :type SOME: typing.Any
   :param ALL: Represents a universal restriction concept type.
   :type ALL: typing.Any
   :param UPPER_APPROX: Represents an upper approximation concept in fuzzy rough set theory, capturing elements that possibly belong to the target set.
   :type UPPER_APPROX: typing.Any
   :param LOWER_APPROX: Represents a lower fuzzy rough concept.
   :type LOWER_APPROX: typing.Any
   :param FUZZY_NUMBER_COMPLEMENT: Represents a negated fuzzy number concept.
   :type FUZZY_NUMBER_COMPLEMENT: typing.Any
   :param TIGHT_UPPER_APPROX: Tight upper fuzzy rough concept.
   :type TIGHT_UPPER_APPROX: typing.Any
   :param TIGHT_LOWER_APPROX: Represents a tight lower approximation concept in fuzzy rough set theory, used to define elements that strictly belong to the set based on specific implication operators.
   :type TIGHT_LOWER_APPROX: typing.Any
   :param LOOSE_UPPER_APPROX: Represents a loose upper approximation of a fuzzy rough concept.
   :type LOOSE_UPPER_APPROX: typing.Any
   :param LOOSE_LOWER_APPROX: Represents a loose lower fuzzy rough concept.
   :type LOOSE_LOWER_APPROX: typing.Any
   :param GOEDEL_IMPLIES: Represents a concept based on the Goedel implication operator.
   :type GOEDEL_IMPLIES: typing.Any
   :param NOT_GOEDEL_IMPLIES: Represents the negation of a Gödel implication concept.
   :type NOT_GOEDEL_IMPLIES: typing.Any
   :param ATOMIC: Represents a basic, indivisible concept that serves as a fundamental building block for constructing more complex expressions within the reasoner.
   :type ATOMIC: typing.Any
   :param COMPLEMENT: Represents the logical complement of a concept.
   :type COMPLEMENT: typing.Any
   :param TOP: Represents the universal concept, encompassing all individuals within the domain of discourse.
   :type TOP: typing.Any
   :param BOTTOM: Represents the bottom concept, which denotes the empty set or a logical contradiction.
   :type BOTTOM: typing.Any
   :param AT_MOST_VALUE: Represents a datatype restriction where the value must be less than or equal to a specified limit.
   :type AT_MOST_VALUE: typing.Any
   :param AT_LEAST_VALUE: Represents a datatype restriction requiring a value to be at least a specified threshold.
   :type AT_LEAST_VALUE: typing.Any
   :param EXACT_VALUE: Represents an exact datatype restriction, requiring a data property to have a specific value.
   :type EXACT_VALUE: typing.Any
   :param NOT_AT_MOST_VALUE: Negation of an 'at most' datatype restriction.
   :type NOT_AT_MOST_VALUE: typing.Any
   :param NOT_AT_LEAST_VALUE: Negated 'at least' datatype restriction.
   :type NOT_AT_LEAST_VALUE: typing.Any
   :param NOT_EXACT_VALUE: Represents the negation of an exact value restriction, indicating that a property does not equal a specific value.
   :type NOT_EXACT_VALUE: typing.Any
   :param WEIGHTED: Represents a weighted concept, where weights are applied to sub-concepts to determine their relative importance or contribution.
   :type WEIGHTED: typing.Any
   :param NOT_WEIGHTED: Represents the negation of a weighted concept.
   :type NOT_WEIGHTED: typing.Any
   :param W_SUM: Represents a weighted sum concept, used to aggregate degrees of membership by summing the products of weights and component values.
   :type W_SUM: typing.Any
   :param NOT_W_SUM: Negated weighted sum concept.
   :type NOT_W_SUM: typing.Any
   :param POS_THRESHOLD: Represents a positive threshold concept.
   :type POS_THRESHOLD: typing.Any
   :param NOT_POS_THRESHOLD: Negated positive threshold concept.
   :type NOT_POS_THRESHOLD: typing.Any
   :param NEG_THRESHOLD: Represents a negative threshold concept used by the reasoner.
   :type NEG_THRESHOLD: typing.Any
   :param NOT_NEG_THRESHOLD: Represents the negated version of a negative threshold concept.
   :type NOT_NEG_THRESHOLD: typing.Any
   :param EXT_POS_THRESHOLD: Represents an extended positive threshold concept.
   :type EXT_POS_THRESHOLD: typing.Any
   :param NOT_EXT_POS_THRESHOLD: Negated extended positive threshold concept.
   :type NOT_EXT_POS_THRESHOLD: typing.Any
   :param EXT_NEG_THRESHOLD: Represents an extended negative threshold concept.
   :type EXT_NEG_THRESHOLD: typing.Any
   :param NOT_EXT_NEG_THRESHOLD: Represents the logical negation of the extended negative threshold concept.
   :type NOT_EXT_NEG_THRESHOLD: typing.Any
   :param CONCRETE: Represents a concept defined over a concrete domain, such as integers or strings, rather than abstract individuals.
   :type CONCRETE: typing.Any
   :param CONCRETE_COMPLEMENT: Represents a negated concrete concept.
   :type CONCRETE_COMPLEMENT: typing.Any
   :param MODIFIED: Represents a concept to which a modifier has been applied.
   :type MODIFIED: typing.Any
   :param MODIFIED_COMPLEMENT: Represents the negation of a modified concept.
   :type MODIFIED_COMPLEMENT: typing.Any
   :param SELF: Represents a self-reflexivity concept.
   :type SELF: typing.Any
   :param FUZZY_NUMBER: Represents a fuzzy number concept.
   :type FUZZY_NUMBER: typing.Any
   :param OWA: Represents a concept defined using the Ordered Weighted Averaging (OWA) aggregation operator.
   :type OWA: typing.Any
   :param QUANTIFIED_OWA: Represents a concept defined by a quantified-guided Ordered Weighted Averaging (OWA) aggregation.
   :type QUANTIFIED_OWA: typing.Any
   :param NOT_OWA: Represents a negated OWA concept.
   :type NOT_OWA: typing.Any
   :param NOT_QUANTIFIED_OWA: Represents the negation of a quantified-guided Ordered Weighted Averaging (OWA) concept.
   :type NOT_QUANTIFIED_OWA: typing.Any
   :param CHOQUET_INTEGRAL: Represents a concept defined by the Choquet integral aggregation operator.
   :type CHOQUET_INTEGRAL: typing.Any
   :param SUGENO_INTEGRAL: Represents a concept defined by the Sugeno integral.
   :type SUGENO_INTEGRAL: typing.Any
   :param QUASI_SUGENO_INTEGRAL: Represents a concept based on the Quasi-Sugeno integral, a fuzzy aggregation operator that generalizes the standard Sugeno integral.
   :type QUASI_SUGENO_INTEGRAL: typing.Any
   :param NOT_CHOQUET_INTEGRAL: Represents the negation of a Choquet integral concept.
   :type NOT_CHOQUET_INTEGRAL: typing.Any
   :param NOT_SUGENO_INTEGRAL: Represents the negation of a Sugeno integral concept.
   :type NOT_SUGENO_INTEGRAL: typing.Any
   :param NOT_QUASI_SUGENO_INTEGRAL: Negated Quasi-Sugeno integral concept.
   :type NOT_QUASI_SUGENO_INTEGRAL: typing.Any
   :param W_MAX: Represents a weighted maximum concept.
   :type W_MAX: typing.Any
   :param NOT_W_MAX: Represents the logical negation of a weighted maximum concept.
   :type NOT_W_MAX: typing.Any
   :param W_MIN: Weighted minimum concept.
   :type W_MIN: typing.Any
   :param NOT_W_MIN: Negated weighted minimum concept.
   :type NOT_W_MIN: typing.Any
   :param W_SUM_ZERO: Represents a weighted sum-zero concept.
   :type W_SUM_ZERO: typing.Any
   :param NOT_W_SUM_ZERO: Negated weighted sum-zero concept.
   :type NOT_W_SUM_ZERO: typing.Any
   :param NOT_SELF: Represents the negation of the self-reflexive concept.
   :type NOT_SELF: typing.Any
   :param HAS_VALUE: Represents a has-value restriction concept, indicating that a property must relate to a specific individual or value.
   :type HAS_VALUE: typing.Any
   :param NOT_HAS_VALUE: Negated has value restriction concept.
   :type NOT_HAS_VALUE: typing.Any
   :param ZADEH_IMPLIES: Represents Zadeh's set inclusion implication, specifically utilized for min-subs queries.
   :type ZADEH_IMPLIES: typing.Any
   :param NOT_ZADEH_IMPLIES: Negated Zadeh's set inclusion implication.
   :type NOT_ZADEH_IMPLIES: typing.Any
   :param SIGMA_CONCEPT: Represents a concept defined by the sigma-count (cardinality) of a fuzzy set.
   :type SIGMA_CONCEPT: typing.Any
   :param NOT_SIGMA_CONCEPT: Represents the negation of a sigma-count concept.
   :type NOT_SIGMA_CONCEPT: typing.Any


   .. py:method:: __repr__() -> str

      Returns the official string representation of the instance by delegating directly to the `name` attribute. This implementation provides a concise and human-readable identifier for the object, which is particularly useful for debugging and logging, instead of the default Python object representation. The method assumes that the `name` attribute is a string and does not modify the object's state.

      :return: Returns the string representation of the object, which is its name.

      :rtype: str



   .. py:method:: __str__() -> str

      Returns a human-readable string representation of the `ConceptType` instance, typically used for display or logging purposes. This method is implicitly called by the built-in `str()` function and `print()` statements, returning the value of the instance's `name` attribute. The operation has no side effects, though it will raise an `AttributeError` if the `name` attribute is not defined on the object.

      :return: The string representation of the object, which is its name.

      :rtype: str



   .. py:attribute:: ALL
      :value: 7



   .. py:attribute:: AND
      :value: 0



   .. py:attribute:: ATOMIC
      :value: 17



   .. py:attribute:: AT_LEAST_VALUE
      :value: 22



   .. py:attribute:: AT_MOST_VALUE
      :value: 21



   .. py:attribute:: BOTTOM
      :value: 20



   .. py:attribute:: CHOQUET_INTEGRAL
      :value: 49



   .. py:attribute:: COMPLEMENT
      :value: 18



   .. py:attribute:: CONCRETE
      :value: 39



   .. py:attribute:: CONCRETE_COMPLEMENT
      :value: 40



   .. py:attribute:: EXACT_VALUE
      :value: 23



   .. py:attribute:: EXT_NEG_THRESHOLD
      :value: 37



   .. py:attribute:: EXT_POS_THRESHOLD
      :value: 35



   .. py:attribute:: FUZZY_NUMBER
      :value: 44



   .. py:attribute:: FUZZY_NUMBER_COMPLEMENT
      :value: 10



   .. py:attribute:: GOEDEL_AND
      :value: 1



   .. py:attribute:: GOEDEL_IMPLIES
      :value: 15



   .. py:attribute:: GOEDEL_OR
      :value: 4



   .. py:attribute:: HAS_VALUE
      :value: 62



   .. py:attribute:: LOOSE_LOWER_APPROX
      :value: 14



   .. py:attribute:: LOOSE_UPPER_APPROX
      :value: 13



   .. py:attribute:: LOWER_APPROX
      :value: 9



   .. py:attribute:: LUKASIEWICZ_AND
      :value: 2



   .. py:attribute:: LUKASIEWICZ_OR
      :value: 5



   .. py:attribute:: MODIFIED
      :value: 41



   .. py:attribute:: MODIFIED_COMPLEMENT
      :value: 42



   .. py:attribute:: NEG_THRESHOLD
      :value: 33



   .. py:attribute:: NOT_AT_LEAST_VALUE
      :value: 25



   .. py:attribute:: NOT_AT_MOST_VALUE
      :value: 24



   .. py:attribute:: NOT_CHOQUET_INTEGRAL
      :value: 52



   .. py:attribute:: NOT_EXACT_VALUE
      :value: 26



   .. py:attribute:: NOT_EXT_NEG_THRESHOLD
      :value: 38



   .. py:attribute:: NOT_EXT_POS_THRESHOLD
      :value: 36



   .. py:attribute:: NOT_GOEDEL_IMPLIES
      :value: 16



   .. py:attribute:: NOT_HAS_VALUE
      :value: 63



   .. py:attribute:: NOT_NEG_THRESHOLD
      :value: 34



   .. py:attribute:: NOT_OWA
      :value: 47



   .. py:attribute:: NOT_POS_THRESHOLD
      :value: 32



   .. py:attribute:: NOT_QUANTIFIED_OWA
      :value: 48



   .. py:attribute:: NOT_QUASI_SUGENO_INTEGRAL
      :value: 54



   .. py:attribute:: NOT_SELF
      :value: 61



   .. py:attribute:: NOT_SIGMA_CONCEPT
      :value: 67



   .. py:attribute:: NOT_SUGENO_INTEGRAL
      :value: 53



   .. py:attribute:: NOT_WEIGHTED
      :value: 28



   .. py:attribute:: NOT_W_MAX
      :value: 56



   .. py:attribute:: NOT_W_MIN
      :value: 58



   .. py:attribute:: NOT_W_SUM
      :value: 30



   .. py:attribute:: NOT_W_SUM_ZERO
      :value: 60



   .. py:attribute:: NOT_ZADEH_IMPLIES
      :value: 65



   .. py:attribute:: OR
      :value: 3



   .. py:attribute:: OWA
      :value: 45



   .. py:attribute:: POS_THRESHOLD
      :value: 31



   .. py:attribute:: QUANTIFIED_OWA
      :value: 46



   .. py:attribute:: QUASI_SUGENO_INTEGRAL
      :value: 51



   .. py:attribute:: SELF
      :value: 43



   .. py:attribute:: SIGMA_CONCEPT
      :value: 66



   .. py:attribute:: SOME
      :value: 6



   .. py:attribute:: SUGENO_INTEGRAL
      :value: 50



   .. py:attribute:: TIGHT_LOWER_APPROX
      :value: 12



   .. py:attribute:: TIGHT_UPPER_APPROX
      :value: 11



   .. py:attribute:: TOP
      :value: 19



   .. py:attribute:: UPPER_APPROX
      :value: 8



   .. py:attribute:: WEIGHTED
      :value: 27



   .. py:attribute:: W_MAX
      :value: 55



   .. py:attribute:: W_MIN
      :value: 57



   .. py:attribute:: W_SUM
      :value: 29



   .. py:attribute:: W_SUM_ZERO
      :value: 59



   .. py:attribute:: ZADEH_IMPLIES
      :value: 64



.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_util_constants_ConcreteFeatureType.png
       :alt: UML Class Diagram for ConcreteFeatureType
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **ConcreteFeatureType**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_util_constants_ConcreteFeatureType.pdf
       :alt: UML Class Diagram for ConcreteFeatureType
       :align: center
       :width: 5.2cm
       :class: uml-diagram

       UML Class Diagram for **ConcreteFeatureType**

.. py:class:: ConcreteFeatureType(*args, **kwds)

   Bases: :py:obj:`enum.Enum`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.util.constants.ConcreteFeatureType
      :parts: 1
      :private-bases:


   This enumeration defines the set of primitive data types applicable to concrete features within the reasoning system. It categorizes features into distinct categories such as text, whole numbers, floating-point values, and binary states, enabling the reasoner to apply logic specific to each data format. Instances of this class provide a standardized way to represent feature types, and their string representation is simplified to the uppercase name of the specific type.

   :param STRING: Represents a textual feature type, indicating that the feature data is a string.
   :type STRING: typing.Any
   :param INTEGER: Represents a concrete feature type for integer values.
   :type INTEGER: typing.Any
   :param REAL: Indicates a feature with a floating-point or continuous numerical value.
   :type REAL: typing.Any
   :param BOOLEAN: Represents a concrete feature of boolean type.
   :type BOOLEAN: typing.Any


   .. py:method:: __repr__() -> str

      Returns the canonical string representation of the `ConcreteFeatureType` instance. This method is invoked by the `repr()` built-in function and is primarily used for debugging and logging. Instead of returning a detailed constructor-style representation, the implementation simply returns the value of the instance's `name` attribute, providing a direct and concise identifier for the feature type.

      :return: The string representation of the object, corresponding to its name.

      :rtype: str



   .. py:method:: __str__() -> str

      Returns a human-readable string representation of the `ConcreteFeatureType` instance by returning the value of its `name` attribute. This method is invoked implicitly by the `str()` built-in function and during string formatting operations, providing a concise identifier for the feature type. It has no side effects, though it will raise an `AttributeError` if the `name` attribute has not been set on the instance.

      :return: The object's name.

      :rtype: str



   .. py:attribute:: BOOLEAN
      :value: 3



   .. py:attribute:: INTEGER
      :value: 1



   .. py:attribute:: REAL
      :value: 2



   .. py:attribute:: STRING
      :value: 0



.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_util_constants_CreatedIndividualBlockingType.png
       :alt: UML Class Diagram for CreatedIndividualBlockingType
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **CreatedIndividualBlockingType**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_util_constants_CreatedIndividualBlockingType.pdf
       :alt: UML Class Diagram for CreatedIndividualBlockingType
       :align: center
       :width: 7.0cm
       :class: uml-diagram

       UML Class Diagram for **CreatedIndividualBlockingType**

.. py:class:: CreatedIndividualBlockingType(*args, **kwds)

   Bases: :py:obj:`enum.Enum`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.util.constants.CreatedIndividualBlockingType
      :parts: 1
      :private-bases:


   This enumeration defines the specific blocking states applicable to individuals generated during the reasoning process. It categorizes individuals into three distinct statuses: explicitly blocked, permitted for processing, or pending evaluation. When represented as a string, the members return their symbolic names, facilitating clear logging and debugging within the reasoning module.

   :param BLOCKED: Indicates that the created individual is blocked.
   :type BLOCKED: typing.Any
   :param NOT_BLOCKED: Indicates that the created individual is not blocked.
   :type NOT_BLOCKED: typing.Any
   :param UNCHECKED: Indicates that the blocking status for the created individual has not been checked.
   :type UNCHECKED: typing.Any


   .. py:method:: __repr__() -> str

      Returns the string representation of the instance, which is defined as the value of the object's name attribute. This method is primarily used for debugging and logging, providing a concise and readable identifier for the blocking type. It performs a direct attribute lookup without modifying the object's state or causing side effects.

      :return: The name of the object.

      :rtype: str



   .. py:method:: __str__() -> str

      Returns the informal string representation of the object, which is invoked by the `str()` built-in function and print operations. This implementation simply returns the value of the instance's `name` attribute, providing a human-readable identifier for the object. The method performs no modification of state and has no side effects, although it will raise an `AttributeError` if the `name` attribute is missing from the instance.

      :return: The string representation of the object, which is the value of its name attribute.

      :rtype: str



   .. py:attribute:: BLOCKED
      :value: 0



   .. py:attribute:: NOT_BLOCKED
      :value: 1



   .. py:attribute:: UNCHECKED
      :value: 2



.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_util_constants_FeatureFunctionType.png
       :alt: UML Class Diagram for FeatureFunctionType
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **FeatureFunctionType**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_util_constants_FeatureFunctionType.pdf
       :alt: UML Class Diagram for FeatureFunctionType
       :align: center
       :width: 5.1cm
       :class: uml-diagram

       UML Class Diagram for **FeatureFunctionType**

.. py:class:: FeatureFunctionType(*args, **kwds)

   Bases: :py:obj:`enum.Enum`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.util.constants.FeatureFunctionType
      :parts: 1
      :private-bases:


   Defines the specific categories of feature functions utilized by the reasoning engine, distinguishing between base values and arithmetic transformations. The available types include atomic and numeric values, alongside composite operations such as sum, subtraction, and product. This classification allows the system to apply specific logic or constraints depending on the nature of the feature calculation. When converted to a string, the members return their uppercase name rather than their integer value.

   :param ATOMIC: Represents a fundamental, indivisible feature that is not derived from other features or operations.
   :type ATOMIC: typing.Any
   :param NUMBER: Represents a feature that is a numeric value.
   :type NUMBER: typing.Any
   :param SUM: Represents a feature function that performs a summation operation.
   :type SUM: typing.Any
   :param SUBTRACTION: Represents a feature function that performs subtraction.
   :type SUBTRACTION: typing.Any
   :param PRODUCT: Represents the product of a number and a feature.
   :type PRODUCT: typing.Any


   .. py:method:: __repr__() -> str

      Returns the official string representation of the instance by directly accessing its name attribute. This method is intended to provide a concise and readable identifier for the object, typically used during debugging or logging, instead of the default memory address representation.

      :return: The name of the object.

      :rtype: str



   .. py:method:: __str__() -> str

      Returns the informal string representation of the feature function type instance. This method is invoked by the built-in `str()` function and `print()` statements to provide a human-readable identifier. It simply returns the value of the instance's `name` attribute, ensuring that the textual output corresponds directly to the specific type's defined name. The operation has no side effects and relies on the `name` attribute being properly initialized.

      :return: The name of the object.

      :rtype: str



   .. py:attribute:: ATOMIC
      :value: 0



   .. py:attribute:: NUMBER
      :value: 1



   .. py:attribute:: PRODUCT
      :value: 5



   .. py:attribute:: SUBTRACTION
      :value: 3



   .. py:attribute:: SUM
      :value: 2



.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_util_constants_FuzzyDLKeyword.png
       :alt: UML Class Diagram for FuzzyDLKeyword
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **FuzzyDLKeyword**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_util_constants_FuzzyDLKeyword.pdf
       :alt: UML Class Diagram for FuzzyDLKeyword
       :align: center
       :width: 12.0cm
       :class: uml-diagram

       UML Class Diagram for **FuzzyDLKeyword**

.. py:class:: FuzzyDLKeyword(*args, **kwds)

   Bases: :py:obj:`enum.Enum`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.util.constants.FuzzyDLKeyword
      :parts: 1
      :private-bases:


   This enumeration defines the comprehensive vocabulary of the FuzzyDL language, mapping specific reserved words and symbols to their corresponding parsing constructs. It encompasses a wide variety of language elements, including query commands (such as satisfiability and instance retrieval), concept and role definitions, logical operators (including specific fuzzy logic norms like Gödel and Łukasiewicz), and data type identifiers. Each member stores a `pyparsing` object—typically a `CaselessKeyword` or `Literal`—enabling direct integration into a grammar definition for parsing FuzzyDL syntax. The class supports flexible usage by providing methods to extract the underlying string name or parser token, and it implements custom equality logic to allow comparison against raw strings, parser objects, or other enum instances.

   :param MAX_INSTANCE_QUERY: Keyword representing the maximum instance query, used to find the instance with the highest degree of membership.
   :type MAX_INSTANCE_QUERY: typing.Any
   :param MIN_INSTANCE_QUERY: Keyword used to query for the instance with the minimum degree of membership.
   :type MIN_INSTANCE_QUERY: typing.Any
   :param ALL_INSTANCES_QUERY: Keyword representing a query to retrieve all instances of a concept.
   :type ALL_INSTANCES_QUERY: typing.Any
   :param MAX_RELATED_QUERY: Keyword for the query that retrieves the individual with the maximum degree of relatedness to a specified individual.
   :type MAX_RELATED_QUERY: typing.Any
   :param MIN_RELATED_QUERY: Keyword for the 'min-related?' query, used to retrieve the minimum degree of relatedness.
   :type MIN_RELATED_QUERY: typing.Any
   :param MAX_SUBS_QUERY: Case-insensitive keyword token for the 'max-subs?' query operation.
   :type MAX_SUBS_QUERY: typing.Any
   :param MAX_G_SUBS_QUERY: Keyword for querying the maximum degree of subsumption using Gödel logic.
   :type MAX_G_SUBS_QUERY: typing.Any
   :param MAX_L_SUBS_QUERY: Keyword representing the query for the maximum degree of subsumption using Łukasiewicz logic.
   :type MAX_L_SUBS_QUERY: typing.Any
   :param MAX_KD_SUBS_QUERY: Represents the keyword for the maximum subsumption query using Kleene-Dienes implication logic.
   :type MAX_KD_SUBS_QUERY: typing.Any
   :param MIN_SUBS_QUERY: Parser keyword for the minimum subsumption query, used to determine the minimum degree of subsumption between concepts.
   :type MIN_SUBS_QUERY: typing.Any
   :param MIN_G_SUBS_QUERY: Represents the query keyword for finding the minimum subsumption degree using Gödel logic.
   :type MIN_G_SUBS_QUERY: typing.Any
   :param MIN_L_SUBS_QUERY: Represents the keyword used to query the minimum degree of subsumption under Lukasiewicz logic.
   :type MIN_L_SUBS_QUERY: typing.Any
   :param MIN_KD_SUBS_QUERY: Represents the keyword for the minimum subsumption query using Kleene-Dienes logic.
   :type MIN_KD_SUBS_QUERY: typing.Any
   :param MAX_SAT_QUERY: Keyword used to query the maximum degree of satisfiability for a concept.
   :type MAX_SAT_QUERY: typing.Any
   :param MIN_SAT_QUERY: Represents the 'min-sat?' keyword used to query for the minimum satisfiability degree.
   :type MIN_SAT_QUERY: typing.Any
   :param MAX_VAR_QUERY: Represents the "max-var?" keyword used to query for the maximum variable value.
   :type MAX_VAR_QUERY: typing.Any
   :param MIN_VAR_QUERY: Keyword representing the query for the minimum value of a variable.
   :type MIN_VAR_QUERY: typing.Any
   :param SAT_QUERY: Keyword representing the satisfiability query, used to determine if a concept is consistent.
   :type SAT_QUERY: typing.Any
   :param DEFUZZIFY_LOM_QUERY: Keyword for the defuzzification query using the Largest of Maximum (LOM) method.
   :type DEFUZZIFY_LOM_QUERY: typing.Any
   :param DEFUZZIFY_SOM_QUERY: Keyword for the defuzzification query that uses the Smallest of Maximums (SOM) method.
   :type DEFUZZIFY_SOM_QUERY: typing.Any
   :param DEFUZZIFY_MOM_QUERY: Represents the 'defuzzify-mom?' keyword, used to execute a defuzzification query based on the Mean of Maxima method.
   :type DEFUZZIFY_MOM_QUERY: typing.Any
   :param BNP_QUERY: Represents the 'bnp?' keyword used to perform a best necessary property query.
   :type BNP_QUERY: typing.Any
   :param INSTANCE: Keyword used to assert that an individual is an instance of a concept.
   :type INSTANCE: typing.Any
   :param DEFINE_TRUTH_CONSTANT: Keyword used to define a truth constant in the Fuzzy DL language.
   :type DEFINE_TRUTH_CONSTANT: typing.Any
   :param DEFINE_CONCEPT: Keyword used to define a named concept in the Fuzzy DL language.
   :type DEFINE_CONCEPT: typing.Any
   :param DEFINE_PRIMITIVE_CONCEPT: Keyword used to define a primitive concept in the Fuzzy DL language.
   :type DEFINE_PRIMITIVE_CONCEPT: typing.Any
   :param EQUIVALENT_CONCEPTS: Keyword used to declare that two concepts are equivalent in the FuzzyDL language.
   :type EQUIVALENT_CONCEPTS: typing.Any
   :param DEFINE_FUZZY_CONCEPT: Keyword used to define a fuzzy concept in the Fuzzy DL language.
   :type DEFINE_FUZZY_CONCEPT: typing.Any
   :param DEFINE_FUZZY_NUMBER: Keyword used to define a fuzzy number in the Fuzzy DL language.
   :type DEFINE_FUZZY_NUMBER: typing.Any
   :param DEFINE_FUZZY_NUMBER_RANGE: Keyword used to define a range of fuzzy numbers.
   :type DEFINE_FUZZY_NUMBER_RANGE: typing.Any
   :param DEFINE_FUZZY_SIMILARITY: Keyword for defining a fuzzy similarity relation in the Fuzzy DL language.
   :type DEFINE_FUZZY_SIMILARITY: typing.Any
   :param DEFINE_FUZZY_EQUIVALENCE: Keyword used to define a fuzzy equivalence relation in the Fuzzy DL language.
   :type DEFINE_FUZZY_EQUIVALENCE: typing.Any
   :param RELATED: Keyword used to assert that two individuals are related by a specific role.
   :type RELATED: typing.Any
   :param DEFINE_MODIFIER: Keyword used to define a fuzzy modifier.
   :type DEFINE_MODIFIER: typing.Any
   :param FUNCTIONAL: Keyword used to define a functional role, indicating that an individual is associated with at most one other individual via this role.
   :type FUNCTIONAL: typing.Any
   :param TRANSITIVE: Keyword used to specify that a role is transitive.
   :type TRANSITIVE: typing.Any
   :param REFLEXIVE: Keyword used to declare a role as reflexive, meaning every individual is related to itself.
   :type REFLEXIVE: typing.Any
   :param SYMMETRIC: Keyword representing the symmetric property for a role in the Fuzzy DL language.
   :type SYMMETRIC: typing.Any
   :param IMPLIES_ROLE: Keyword representing the implication or inclusion relationship between roles.
   :type IMPLIES_ROLE: typing.Any
   :param INVERSE: Keyword used to define or specify the inverse of a role in the Fuzzy DL language.
   :type INVERSE: typing.Any
   :param INVERSE_FUNCTIONAL: Keyword used to declare a role as inverse-functional, meaning that the inverse of the role relates to at most one individual.
   :type INVERSE_FUNCTIONAL: typing.Any
   :param DISJOINT: Keyword used to specify that two concepts are disjoint, meaning they share no common instances.
   :type DISJOINT: typing.Any
   :param DISJOINT_UNION: Keyword used to define a disjoint union of concepts.
   :type DISJOINT_UNION: typing.Any
   :param RANGE: Keyword used to specify the range restriction for a role, defining the valid types of objects or values it can relate to.
   :type RANGE: typing.Any
   :param DOMAIN: Keyword used to specify the domain restriction of a role in the FuzzyDL language.
   :type DOMAIN: typing.Any
   :param CONSTRAINTS: Represents the 'constraints' keyword in the Fuzzy DL language syntax.
   :type CONSTRAINTS: typing.Any
   :param DEFINE_FUZZY_LOGIC: Keyword used to define the specific fuzzy logic system (e.g., Zadeh, Lukasiewicz) used for reasoning.
   :type DEFINE_FUZZY_LOGIC: typing.Any
   :param CRISP_CONCEPT: Represents the 'crisp-concept' keyword, used to denote concepts with binary membership values rather than fuzzy degrees.
   :type CRISP_CONCEPT: typing.Any
   :param CRISP_ROLE: Keyword representing a crisp (non-fuzzy) role in the Fuzzy DL language.
   :type CRISP_ROLE: typing.Any
   :param AND: Keyword representing the logical conjunction (intersection) of concepts or roles.
   :type AND: typing.Any
   :param GOEDEL_AND: Keyword representing the Gödel t-norm logical conjunction operator.
   :type GOEDEL_AND: typing.Any
   :param LUKASIEWICZ_AND: Represents the Lukasiewicz conjunction operator keyword used in fuzzy logic expressions.
   :type LUKASIEWICZ_AND: typing.Any
   :param IMPLIES: Represents the logical implication operator keyword used in Fuzzy DL expressions.
   :type IMPLIES: typing.Any
   :param GOEDEL_IMPLIES: Keyword representing the Gödel implication operator in fuzzy logic.
   :type GOEDEL_IMPLIES: typing.Any
   :param KLEENE_DIENES_IMPLIES: Represents the Kleene-Dienes fuzzy implication operator keyword.
   :type KLEENE_DIENES_IMPLIES: typing.Any
   :param LUKASIEWICZ_IMPLIES: Represents the Lukasiewicz implication operator used in fuzzy logic expressions.
   :type LUKASIEWICZ_IMPLIES: typing.Any
   :param ZADEH_IMPLIES: Represents the Zadeh implication operator used in fuzzy logic expressions.
   :type ZADEH_IMPLIES: typing.Any
   :param OR: Represents the logical disjunction operator 'or' used for combining concepts or axioms.
   :type OR: typing.Any
   :param GOEDEL_OR: Represents the logical OR operation based on Gödel fuzzy logic.
   :type GOEDEL_OR: typing.Any
   :param LUKASIEWICZ_OR: Keyword representing the Lukasiewicz OR (disjunction) operator in fuzzy logic expressions.
   :type LUKASIEWICZ_OR: typing.Any
   :param NOT: Represents the logical negation operator used in Fuzzy DL expressions.
   :type NOT: typing.Any
   :param SOME: Represents the existential quantification keyword used to define concept restrictions where at least one filler of a role belongs to a specific concept.
   :type SOME: typing.Any
   :param HAS_VALUE: Represents the "b-some" keyword, used to express existential restrictions or value assertions where a role is associated with a specific individual or value.
   :type HAS_VALUE: typing.Any
   :param ALL: Keyword representing the universal quantifier used to define restrictions on roles.
   :type ALL: typing.Any
   :param TOP: Represents the universal concept (Top) in the Fuzzy DL language, denoting the set of all individuals.
   :type TOP: typing.Any
   :param BOTTOM: Represents the bottom concept (the empty concept or logical false) in the Fuzzy DL language.
   :type BOTTOM: typing.Any
   :param W_SUM: Represents the weighted sum operator in the FuzzyDL language.
   :type W_SUM: typing.Any
   :param W_SUM_ZERO: Represents the weighted sum zero operator.
   :type W_SUM_ZERO: typing.Any
   :param W_MAX: Represents the weighted maximum operator keyword used in FuzzyDL expressions.
   :type W_MAX: typing.Any
   :param W_MIN: Represents the weighted minimum keyword in the FuzzyDL language.
   :type W_MIN: typing.Any
   :param SELF: Represents the 'self' keyword used to denote self-reference in concept expressions.
   :type SELF: typing.Any
   :param UPPER_APPROXIMATION: Keyword representing the 'ua' operator used to define the upper approximation of a concept.
   :type UPPER_APPROXIMATION: typing.Any
   :param LOWER_APPROXIMATION: Represents the lower approximation operator in the Fuzzy DL language, corresponding to the keyword 'la'.
   :type LOWER_APPROXIMATION: typing.Any
   :param OWA: Represents the Ordered Weighted Averaging (OWA) aggregation operator.
   :type OWA: typing.Any
   :param Q_OWA: Keyword representing the Quasi Ordered Weighted Averaging (Q-OWA) operator.
   :type Q_OWA: typing.Any
   :param CHOQUET: Keyword representing the Choquet integral aggregation operator.
   :type CHOQUET: typing.Any
   :param SUGENO: Represents the Sugeno integral aggregation operator keyword used in fuzzy logic expressions.
   :type SUGENO: typing.Any
   :param QUASI_SUGENO: Represents the Quasi-Sugeno operator keyword used for fuzzy aggregation or integration.
   :type QUASI_SUGENO: typing.Any
   :param TIGHT_UPPER_APPROXIMATION: Represents the "tua" keyword for the tight upper approximation operator in the Fuzzy DL language.
   :type TIGHT_UPPER_APPROXIMATION: typing.Any
   :param TIGHT_LOWER_APPROXIMATION: Keyword representing the tight lower approximation operator in the Fuzzy DL language.
   :type TIGHT_LOWER_APPROXIMATION: typing.Any
   :param LOOSE_UPPER_APPROXIMATION: Keyword representing the loose upper approximation operator.
   :type LOOSE_UPPER_APPROXIMATION: typing.Any
   :param LOOSE_LOWER_APPROXIMATION: Represents the loose lower approximation operator, denoted by 'lla', used for defining relaxed lower bounds in fuzzy concepts.
   :type LOOSE_LOWER_APPROXIMATION: typing.Any
   :param FEATURE_SUM: Represents the feature sum operator in the FuzzyDL language.
   :type FEATURE_SUM: typing.Any
   :param FEATURE_SUB: Represents the subtraction operator for feature terms in the FuzzyDL language.
   :type FEATURE_SUB: typing.Any
   :param FEATURE_MUL: Represents the feature multiplication operator ('f*') used in Fuzzy DL expressions.
   :type FEATURE_MUL: typing.Any
   :param FEATURE_DIV: Represents the FuzzyDL keyword for the division operation on features.
   :type FEATURE_DIV: typing.Any
   :param SIGMA_COUNT: Represents the 'sigma-count' keyword used to calculate the cardinality of a fuzzy set.
   :type SIGMA_COUNT: typing.Any
   :param CRISP: Represents the "crisp" keyword used to define a crisp (non-fuzzy) type or shape for numbers or concepts in the FuzzyDL language.
   :type CRISP: typing.Any
   :param LEFT_SHOULDER: Represents a left-shoulder membership function shape used in fuzzy logic definitions.
   :type LEFT_SHOULDER: typing.Any
   :param RIGHT_SHOULDER: Represents a right-shoulder membership function shape used in fuzzy logic definitions.
   :type RIGHT_SHOULDER: typing.Any
   :param TRIANGULAR: Represents the keyword for a triangular membership function or fuzzy number shape.
   :type TRIANGULAR: typing.Any
   :param TRAPEZOIDAL: Keyword used to specify a trapezoidal shape for fuzzy numbers or membership functions.
   :type TRAPEZOIDAL: typing.Any
   :param LINEAR: Represents the "linear" keyword used to define linear membership functions or shapes.
   :type LINEAR: typing.Any
   :param MODIFIED: Represents the "modified" keyword in the FuzzyDL language, used for defining modified fuzzy concepts or modifiers.
   :type MODIFIED: typing.Any
   :param LINEAR_MODIFIER: Represents the 'linear-modifier' keyword in the FuzzyDL language, used to specify a linear modification operation on fuzzy concepts.
   :type LINEAR_MODIFIER: typing.Any
   :param TRIANGULAR_MODIFIER: Keyword used to specify a triangular shape for a modifier definition.
   :type TRIANGULAR_MODIFIER: typing.Any
   :param SHOW_VARIABLES: Keyword used to display the variables defined in the current context.
   :type SHOW_VARIABLES: typing.Any
   :param SHOW_ABSTRACT_FILLERS: Represents the keyword used to display abstract fillers.
   :type SHOW_ABSTRACT_FILLERS: typing.Any
   :param SHOW_ABSTRACT_FILLERS_FOR: Represents the command to display abstract fillers for a specific individual or entity.
   :type SHOW_ABSTRACT_FILLERS_FOR: typing.Any
   :param SHOW_CONCRETE_FILLERS: Keyword representing the command to display concrete fillers (data values) associated with a role or instance.
   :type SHOW_CONCRETE_FILLERS: typing.Any
   :param SHOW_CONCRETE_FILLERS_FOR: Keyword used to display concrete fillers for a specific entity.
   :type SHOW_CONCRETE_FILLERS_FOR: typing.Any
   :param SHOW_CONCRETE_INSTANCE_FOR: Keyword used to display a concrete instance for a specific concept or identifier.
   :type SHOW_CONCRETE_INSTANCE_FOR: typing.Any
   :param SHOW_INSTANCES: Keyword used to display the instances defined in the Fuzzy DL knowledge base.
   :type SHOW_INSTANCES: typing.Any
   :param SHOW_CONCEPTS: Represents the keyword used to display the defined concepts.
   :type SHOW_CONCEPTS: typing.Any
   :param SHOW_LANGUAGE: Keyword representing the command to display the language syntax or configuration.
   :type SHOW_LANGUAGE: typing.Any
   :param FREE: Keyword representing the free logic type.
   :type FREE: typing.Any
   :param BINARY: Represents the "binary" keyword in the FuzzyDL language.
   :type BINARY: typing.Any
   :param LUKASIEWICZ: Keyword representing the Lukasiewicz fuzzy logic type.
   :type LUKASIEWICZ: typing.Any
   :param ZADEH: Keyword representing the Zadeh fuzzy logic type.
   :type ZADEH: typing.Any
   :param CLASSICAL: Represents the "classical" keyword, used to specify standard Boolean logic or crisp operations within the Fuzzy DL language.
   :type CLASSICAL: typing.Any
   :param SUM: Represents the addition operator symbol "+" in the Fuzzy DL language.
   :type SUM: typing.Any
   :param SUB: Represents the subtraction operator ("-") in the Fuzzy DL language.
   :type SUB: typing.Any
   :param MUL: Represents the arithmetic multiplication operator.
   :type MUL: typing.Any
   :param LESS_THAN_OR_EQUAL_TO: Represents the "less than or equal to" comparison operator used in Fuzzy DL expressions.
   :type LESS_THAN_OR_EQUAL_TO: typing.Any
   :param GREATER_THAN_OR_EQUAL_TO: Represents the "greater than or equal to" comparison operator (">=").
   :type GREATER_THAN_OR_EQUAL_TO: typing.Any
   :param EQUALS: Represents the equality operator used for comparisons within the Fuzzy DL language.
   :type EQUALS: typing.Any
   :param STRING: Keyword representing the string data type in the Fuzzy DL language.
   :type STRING: typing.Any
   :param BOOLEAN: Case-insensitive keyword representing the boolean data type in the Fuzzy DL language.
   :type BOOLEAN: typing.Any
   :param INTEGER: Keyword representing the integer data type within the Fuzzy DL language.
   :type INTEGER: typing.Any
   :param REAL: Represents the primitive data type for real numbers within the FuzzyDL language syntax.
   :type REAL: typing.Any

   :raises NotImplementedError: Raised when comparing the keyword to an object of an unsupported type. Equality is only implemented for strings, pyparsing elements, and other FuzzyDLKeyword instances.


   .. py:method:: __eq__(value: object) -> bool

      Determines equality by comparing the keyword's name against the provided value, supporting strings, pyparsing objects, and other FuzzyDLKeyword instances. The comparison is case-insensitive when the input is a string, a pyparsing CaselessKeyword, or a pyparsing Literal. If the input is another FuzzyDLKeyword instance, the method compares the results of their respective get_name methods. If the provided value is not one of these supported types, the method raises a NotImplementedError.

      :param value: The object to compare against. Supported types include strings (case-insensitive), `pp.CaselessKeyword`, `pp.Literal`, and `FuzzyDLKeyword`.
      :type value: object

      :raises NotImplementedError: Raised when the provided value is not a supported type for comparison (str, CaselessKeyword, Literal, or FuzzyDLKeyword).

      :return: True if the object's name matches the name of the provided value (string, CaselessKeyword, Literal, or FuzzyDLKeyword) in a case-insensitive manner; otherwise, False.

      :rtype: bool



   .. py:method:: __repr__() -> str

      Returns the string representation of the FuzzyDLKeyword instance. This implementation returns the value of the `name` attribute directly, providing a concise and readable identifier rather than a full constructor representation. Consequently, when the object is inspected or printed, it displays its underlying name.

      :return: The string representation of the object, which is the value of its `name` attribute.

      :rtype: str



   .. py:method:: __str__() -> str

      Returns the string representation of the `FuzzyDLKeyword` instance, which is derived directly from its `name` attribute. This method is invoked implicitly by Python whenever the object is converted to a string, for example, when using the `print()` function or string formatting. The operation has no side effects on the object's state, though it will raise an `AttributeError` if the `name` attribute is missing.

      :return: The string representation of the object, specifically the value of its `name` attribute.

      :rtype: str



   .. py:method:: get_name() -> str

      Retrieves and normalizes the name associated with the underlying value object. The method converts the name to lowercase and strips all occurrences of single and double quotes using a regular expression substitution. This processing ensures a consistent string representation suitable for comparison or fuzzy matching, and it does not modify the state of the object itself. Note that this method assumes `self.value` and `self.value.name` are accessible and valid strings; if these attributes are missing or lack the expected methods, an `AttributeError` will be raised.

      :return: The lowercased name with all single and double quotes removed.

      :rtype: str



   .. py:method:: get_value() -> Union[pyparsing.CaselessKeyword, pyparsing.Literal]

      Returns the underlying pyparsing element stored within the instance. This method provides access to the specific parsing token, which can be either a CaselessKeyword for case-insensitive matching or a Literal for exact string matching. It serves as a simple getter with no side effects, allowing the retrieval of the configured parser component.

      :return: Returns the internal value, which is either a CaselessKeyword or a Literal.

      :rtype: typing.Union[pp.CaselessKeyword, pp.Literal]



   .. py:attribute:: ALL


   .. py:attribute:: ALL_INSTANCES_QUERY


   .. py:attribute:: AND


   .. py:attribute:: BINARY


   .. py:attribute:: BNP_QUERY


   .. py:attribute:: BOOLEAN


   .. py:attribute:: BOTTOM


   .. py:attribute:: CHOQUET


   .. py:attribute:: CLASSICAL


   .. py:attribute:: CONSTRAINTS


   .. py:attribute:: CRISP


   .. py:attribute:: CRISP_CONCEPT


   .. py:attribute:: CRISP_ROLE


   .. py:attribute:: DEFINE_CONCEPT


   .. py:attribute:: DEFINE_FUZZY_CONCEPT


   .. py:attribute:: DEFINE_FUZZY_EQUIVALENCE


   .. py:attribute:: DEFINE_FUZZY_LOGIC


   .. py:attribute:: DEFINE_FUZZY_NUMBER


   .. py:attribute:: DEFINE_FUZZY_NUMBER_RANGE


   .. py:attribute:: DEFINE_FUZZY_SIMILARITY


   .. py:attribute:: DEFINE_MODIFIER


   .. py:attribute:: DEFINE_PRIMITIVE_CONCEPT


   .. py:attribute:: DEFINE_TRUTH_CONSTANT


   .. py:attribute:: DEFUZZIFY_LOM_QUERY


   .. py:attribute:: DEFUZZIFY_MOM_QUERY


   .. py:attribute:: DEFUZZIFY_SOM_QUERY


   .. py:attribute:: DISJOINT


   .. py:attribute:: DISJOINT_UNION


   .. py:attribute:: DOMAIN


   .. py:attribute:: EQUALS


   .. py:attribute:: EQUIVALENT_CONCEPTS


   .. py:attribute:: FEATURE_DIV


   .. py:attribute:: FEATURE_MUL


   .. py:attribute:: FEATURE_SUB


   .. py:attribute:: FEATURE_SUM


   .. py:attribute:: FREE


   .. py:attribute:: FUNCTIONAL


   .. py:attribute:: GOEDEL_AND


   .. py:attribute:: GOEDEL_IMPLIES


   .. py:attribute:: GOEDEL_OR


   .. py:attribute:: GREATER_THAN_OR_EQUAL_TO


   .. py:attribute:: HAS_VALUE


   .. py:attribute:: IMPLIES


   .. py:attribute:: IMPLIES_ROLE


   .. py:attribute:: INSTANCE


   .. py:attribute:: INTEGER


   .. py:attribute:: INVERSE


   .. py:attribute:: INVERSE_FUNCTIONAL


   .. py:attribute:: KLEENE_DIENES_IMPLIES


   .. py:attribute:: LEFT_SHOULDER


   .. py:attribute:: LESS_THAN_OR_EQUAL_TO


   .. py:attribute:: LINEAR


   .. py:attribute:: LINEAR_MODIFIER


   .. py:attribute:: LOOSE_LOWER_APPROXIMATION


   .. py:attribute:: LOOSE_UPPER_APPROXIMATION


   .. py:attribute:: LOWER_APPROXIMATION


   .. py:attribute:: LUKASIEWICZ


   .. py:attribute:: LUKASIEWICZ_AND


   .. py:attribute:: LUKASIEWICZ_IMPLIES


   .. py:attribute:: LUKASIEWICZ_OR


   .. py:attribute:: MAX_G_SUBS_QUERY


   .. py:attribute:: MAX_INSTANCE_QUERY


   .. py:attribute:: MAX_KD_SUBS_QUERY


   .. py:attribute:: MAX_L_SUBS_QUERY


   .. py:attribute:: MAX_RELATED_QUERY


   .. py:attribute:: MAX_SAT_QUERY


   .. py:attribute:: MAX_SUBS_QUERY


   .. py:attribute:: MAX_VAR_QUERY


   .. py:attribute:: MIN_G_SUBS_QUERY


   .. py:attribute:: MIN_INSTANCE_QUERY


   .. py:attribute:: MIN_KD_SUBS_QUERY


   .. py:attribute:: MIN_L_SUBS_QUERY


   .. py:attribute:: MIN_RELATED_QUERY


   .. py:attribute:: MIN_SAT_QUERY


   .. py:attribute:: MIN_SUBS_QUERY


   .. py:attribute:: MIN_VAR_QUERY


   .. py:attribute:: MODIFIED


   .. py:attribute:: MUL


   .. py:attribute:: NOT


   .. py:attribute:: OR


   .. py:attribute:: OWA


   .. py:attribute:: QUASI_SUGENO


   .. py:attribute:: Q_OWA


   .. py:attribute:: RANGE


   .. py:attribute:: REAL


   .. py:attribute:: REFLEXIVE


   .. py:attribute:: RELATED


   .. py:attribute:: RIGHT_SHOULDER


   .. py:attribute:: SAT_QUERY


   .. py:attribute:: SELF


   .. py:attribute:: SHOW_ABSTRACT_FILLERS


   .. py:attribute:: SHOW_ABSTRACT_FILLERS_FOR


   .. py:attribute:: SHOW_CONCEPTS


   .. py:attribute:: SHOW_CONCRETE_FILLERS


   .. py:attribute:: SHOW_CONCRETE_FILLERS_FOR


   .. py:attribute:: SHOW_CONCRETE_INSTANCE_FOR


   .. py:attribute:: SHOW_INSTANCES


   .. py:attribute:: SHOW_LANGUAGE


   .. py:attribute:: SHOW_VARIABLES


   .. py:attribute:: SIGMA_COUNT


   .. py:attribute:: SOME


   .. py:attribute:: STRING


   .. py:attribute:: SUB


   .. py:attribute:: SUGENO


   .. py:attribute:: SUM


   .. py:attribute:: SYMMETRIC


   .. py:attribute:: TIGHT_LOWER_APPROXIMATION


   .. py:attribute:: TIGHT_UPPER_APPROXIMATION


   .. py:attribute:: TOP


   .. py:attribute:: TRANSITIVE


   .. py:attribute:: TRAPEZOIDAL


   .. py:attribute:: TRIANGULAR


   .. py:attribute:: TRIANGULAR_MODIFIER


   .. py:attribute:: UPPER_APPROXIMATION


   .. py:attribute:: W_MAX


   .. py:attribute:: W_MIN


   .. py:attribute:: W_SUM


   .. py:attribute:: W_SUM_ZERO


   .. py:attribute:: ZADEH


   .. py:attribute:: ZADEH_IMPLIES


.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_util_constants_FuzzyLogic.png
       :alt: UML Class Diagram for FuzzyLogic
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **FuzzyLogic**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_util_constants_FuzzyLogic.pdf
       :alt: UML Class Diagram for FuzzyLogic
       :align: center
       :width: 3.7cm
       :class: uml-diagram

       UML Class Diagram for **FuzzyLogic**

.. py:class:: FuzzyLogic

   Bases: :py:obj:`enum.StrEnum`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.util.constants.FuzzyLogic
      :parts: 1
      :private-bases:


   This enumeration defines the specific mathematical frameworks or strategies for fuzzy logic operations supported by the reasoner. It provides options such as Classical, Zadeh, and Lukasiewicz logic, which dictate how truth values are combined and manipulated during inference. By inheriting from `StrEnum`, instances behave as strings in value while maintaining the type safety and distinct identity of an enumeration, allowing for easy serialization and comparison.

   :param CLASSICAL: Selects the classical fuzzy logic inference method for the reasoner.
   :type CLASSICAL: typing.Any
   :param ZADEH: Indicates the use of standard Zadeh operators for fuzzy logic operations.
   :type ZADEH: typing.Any
   :param LUKASIEWICZ: Specifies the Łukasiewicz variant of fuzzy logic for reasoning operations.
   :type LUKASIEWICZ: typing.Any


   .. py:method:: __repr__() -> str

      Returns the official string representation of the `FuzzyLogic` instance. Instead of providing a detailed constructor-style representation, this method returns the value of the instance's `name` attribute directly. This behavior allows the object to be identified succinctly by its name when displayed in the interactive console or during debugging sessions.

      :return: The string representation of the object, which is the value of the `name` attribute.

      :rtype: str



   .. py:method:: __str__() -> str

      Returns the informal string representation of the FuzzyLogic instance, which is invoked by the built-in `str()` function and `print()` calls. The implementation simply returns the object's internal `value` attribute, delegating the actual formatting logic to whatever type that attribute holds. Consequently, the output depends entirely on the string conversion behavior of the underlying value, and the method itself does not modify the object's state or produce side effects.

      :return: The string representation of the object, corresponding to the `value` attribute.

      :rtype: str



   .. py:attribute:: CLASSICAL
      :value: 'classical'



   .. py:attribute:: LUKASIEWICZ
      :value: 'lukasiewicz'



   .. py:attribute:: ZADEH
      :value: 'zadeh'



.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_util_constants_InequalityType.png
       :alt: UML Class Diagram for InequalityType
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **InequalityType**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_util_constants_InequalityType.pdf
       :alt: UML Class Diagram for InequalityType
       :align: center
       :width: 3.8cm
       :class: uml-diagram

       UML Class Diagram for **InequalityType**

.. py:class:: InequalityType

   Bases: :py:obj:`enum.StrEnum`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.util.constants.InequalityType
      :parts: 1
      :private-bases:


   This enumeration defines the standard comparison operators used to express logical relationships or constraints between values. It inherits from `StrEnum`, allowing its members to function as strings (such as ">") while providing the safety and structure of an enumeration. The class supports three primary operations: greater than, less than, and equal, making it suitable for defining conditions in rule engines, query builders, or mathematical contexts. When converted to a string, the enum yields its symbolic representation, whereas its representation provides the constant name.

   :param GREATER_THAN: Represents the greater-than inequality operator.
   :type GREATER_THAN: typing.Any
   :param LESS_THAN: Represents the "less than" comparison operator.
   :type LESS_THAN: typing.Any
   :param EQUAL: Represents an equality relationship.
   :type EQUAL: typing.Any


   .. py:method:: __repr__() -> str

      Returns the official string representation of the instance, designed to be unambiguous and useful for debugging. The implementation delegates directly to the `name` attribute of the object, returning its value as the representation string. This method is invoked by the built-in `repr()` function and has no side effects, though it assumes that the `name` attribute is defined on the instance.

      :return: The string representation of the object, which is the value of its `name` attribute.

      :rtype: str



   .. py:method:: __str__() -> str

      Returns the string representation of the inequality type instance. This method is invoked when the object is converted to a string, such as during string formatting or printing operations. It simply returns the underlying value associated with the instance, ensuring that the textual output corresponds directly to the specific inequality type defined.

      :return: The string representation of the object, which is the `value` attribute.

      :rtype: str



   .. py:attribute:: EQUAL
      :value: '='



   .. py:attribute:: GREATER_THAN
      :value: '>'



   .. py:attribute:: LESS_THAN
      :value: '<'



.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_util_constants_KnowledgeBaseRules.png
       :alt: UML Class Diagram for KnowledgeBaseRules
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **KnowledgeBaseRules**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_util_constants_KnowledgeBaseRules.pdf
       :alt: UML Class Diagram for KnowledgeBaseRules
       :align: center
       :width: 5.3cm
       :class: uml-diagram

       UML Class Diagram for **KnowledgeBaseRules**

.. py:class:: KnowledgeBaseRules(*args, **kwds)

   Bases: :py:obj:`enum.Enum`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.util.constants.KnowledgeBaseRules
      :parts: 1
      :private-bases:


   This enumeration defines a comprehensive set of inference rules and logical operators applicable within a knowledge base system, specifically catering to fuzzy logic and many-valued reasoning. It encompasses various t-norms and t-conorms (such as Gödel and Łukasiewicz variants for conjunction, disjunction, and implication), quantifiers, and advanced aggregation operators like OWA, Choquet integrals, and Sugeno integrals. Additionally, it includes specific property checks and their negations (e.g., `CONCRETE`, `WEIGHTED`) to determine the characteristics of data or rules. Users can reference these members to configure reasoning behavior or validate rule properties, noting that the string representation of each member automatically strips the "RULE_" prefix for readability.

   :param RULE_ATOMIC: Represents a basic, indivisible fact or condition that serves as a fundamental building block within the knowledge base.
   :type RULE_ATOMIC: typing.Any
   :param RULE_COMPLEMENT: Represents the rule for applying the complement operation (logical negation).
   :type RULE_COMPLEMENT: typing.Any
   :param RULE_GOEDEL_AND: Specifies the Gödel t-norm (minimum) for the logical AND operation.
   :type RULE_GOEDEL_AND: typing.Any
   :param RULE_LUKASIEWICZ_AND: Represents the Łukasiewicz t-norm for the logical AND operation.
   :type RULE_LUKASIEWICZ_AND: typing.Any
   :param RULE_GOEDEL_OR: Represents the Gödel t-conorm (logical OR) rule, which calculates the maximum of the input values.
   :type RULE_GOEDEL_OR: typing.Any
   :param RULE_LUKASIEWICZ_OR: Represents the logical OR operation based on Łukasiewicz logic.
   :type RULE_LUKASIEWICZ_OR: typing.Any
   :param RULE_GOEDEL_SOME: Represents the existential quantifier rule ('some') based on Gödel logic.
   :type RULE_GOEDEL_SOME: typing.Any
   :param RULE_LUKASIEWICZ_SOME: Represents the existential quantifier rule based on Łukasiewicz logic.
   :type RULE_LUKASIEWICZ_SOME: typing.Any
   :param RULE_GOEDEL_ALL: Represents the Gödel logic rule for universal quantification, corresponding to the minimum of a set of values.
   :type RULE_GOEDEL_ALL: typing.Any
   :param RULE_LUKASIEWICZ_ALL: Represents the Łukasiewicz logic rule for the universal quantifier.
   :type RULE_LUKASIEWICZ_ALL: typing.Any
   :param RULE_TOP: Represents the top element (tautology) in the logic system, corresponding to the maximum truth value.
   :type RULE_TOP: typing.Any
   :param RULE_BOTTOM: Represents the logical bottom element (minimal truth value), typically corresponding to false or zero.
   :type RULE_BOTTOM: typing.Any
   :param RULE_GOEDEL_IMPLIES: Represents the Gödel implication rule, a specific fuzzy logic implication operator used for inference.
   :type RULE_GOEDEL_IMPLIES: typing.Any
   :param RULE_NOT_GOEDEL_IMPLIES: Represents the negation of the Gödel implication rule.
   :type RULE_NOT_GOEDEL_IMPLIES: typing.Any
   :param RULE_CONCRETE: Represents the rule for concrete elements or properties.
   :type RULE_CONCRETE: typing.Any
   :param RULE_NOT_CONCRETE: Represents a rule or condition that is not concrete, distinguishing abstract or fuzzy elements from specific instances.
   :type RULE_NOT_CONCRETE: typing.Any
   :param RULE_MODIFIED: Represents a rule or condition that checks for or indicates the modified state of an entity.
   :type RULE_MODIFIED: typing.Any
   :param RULE_NOT_MODIFIED: Indicates that the rule or element has not been modified.
   :type RULE_NOT_MODIFIED: typing.Any
   :param RULE_DATATYPE: Represents a rule that checks for or applies to data types.
   :type RULE_DATATYPE: typing.Any
   :param RULE_NOT_DATATYPE: Represents a rule indicating that the element is not a datatype.
   :type RULE_NOT_DATATYPE: typing.Any
   :param RULE_FUZZY_NUMBER: Indicates a rule or property related to fuzzy numbers.
   :type RULE_FUZZY_NUMBER: typing.Any
   :param RULE_NOT_FUZZY_NUMBER: Represents a rule condition indicating that the target element is not a fuzzy number.
   :type RULE_NOT_FUZZY_NUMBER: typing.Any
   :param RULE_WEIGHTED: Represents a rule that utilizes weighted aggregation or applies weights to its components.
   :type RULE_WEIGHTED: typing.Any
   :param RULE_NOT_WEIGHTED: Indicates that the rule or condition is not weighted.
   :type RULE_NOT_WEIGHTED: typing.Any
   :param RULE_THRESHOLD: Identifies a rule that applies a threshold condition.
   :type RULE_THRESHOLD: typing.Any
   :param RULE_NOT_THRESHOLD: Represents the negation of a threshold rule or condition.
   :type RULE_NOT_THRESHOLD: typing.Any
   :param RULE_OWA: Represents the Ordered Weighted Averaging (OWA) aggregation rule.
   :type RULE_OWA: typing.Any
   :param RULE_NOT_OWA: Represents the negation of the Ordered Weighted Averaging (OWA) aggregation rule.
   :type RULE_NOT_OWA: typing.Any
   :param RULE_W_SUM: Represents a rule that utilizes a weighted sum aggregation operator.
   :type RULE_W_SUM: typing.Any
   :param RULE_NOT_W_SUM: Indicates that the rule is not a weighted sum.
   :type RULE_NOT_W_SUM: typing.Any
   :param RULE_CHOQUET_INTEGRAL: Represents the Choquet integral rule, used for aggregating information while accounting for interactions between criteria.
   :type RULE_CHOQUET_INTEGRAL: typing.Any
   :param RULE_NOT_CHOQUET_INTEGRAL: Represents a rule or condition indicating that the element is not a Choquet integral.
   :type RULE_NOT_CHOQUET_INTEGRAL: typing.Any
   :param RULE_SUGENO_INTEGRAL: Represents the Sugeno integral rule.
   :type RULE_SUGENO_INTEGRAL: typing.Any
   :param RULE_NOT_SUGENO_INTEGRAL: Represents the negation of the Sugeno integral rule, identifying elements or conditions that are not Sugeno integrals.
   :type RULE_NOT_SUGENO_INTEGRAL: typing.Any
   :param RULE_QUASI_SUGENO_INTEGRAL: Represents a rule or aggregation method utilizing the Quasi-Sugeno integral.
   :type RULE_QUASI_SUGENO_INTEGRAL: typing.Any
   :param RULE_NOT_QUASI_SUGENO_INTEGRAL: Represents a rule that is not a Quasi-Sugeno Integral.
   :type RULE_NOT_QUASI_SUGENO_INTEGRAL: typing.Any
   :param RULE_SELF: Represents a rule that applies to the entity itself or is self-referential.
   :type RULE_SELF: typing.Any
   :param RULE_NOT_SELF: Represents the rule indicating that a relationship or property is not self-referential.
   :type RULE_NOT_SELF: typing.Any
   :param RULE_W_MIN: Represents the weighted minimum rule.
   :type RULE_W_MIN: typing.Any
   :param RULE_NOT_W_MIN: Represents the negation of the weighted minimum (W-Min) rule.
   :type RULE_NOT_W_MIN: typing.Any
   :param RULE_W_MAX: Represents the weighted maximum rule used for aggregating values or criteria.
   :type RULE_W_MAX: typing.Any
   :param RULE_NOT_W_MAX: Represents the negation of the Weighted Maximum rule.
   :type RULE_NOT_W_MAX: typing.Any
   :param RULE_W_SUM_ZERO: Represents a rule or property concerning a weighted sum that is zero.
   :type RULE_W_SUM_ZERO: typing.Any
   :param RULE_NOT_W_SUM_ZERO: Represents the rule where the weighted sum is not zero.
   :type RULE_NOT_W_SUM_ZERO: typing.Any
   :param RULE_HAS_VALUE: Represents a rule that verifies whether a specific attribute or entity possesses an assigned value.
   :type RULE_HAS_VALUE: typing.Any
   :param RULE_NOT_HAS_VALUE: Represents a rule condition checking that a specific element or property lacks an assigned value.
   :type RULE_NOT_HAS_VALUE: typing.Any
   :param RULE_ZADEH_IMPLIES: Represents the Zadeh implication rule, a specific fuzzy logic implication operator.
   :type RULE_ZADEH_IMPLIES: typing.Any
   :param RULE_NOT_ZADEH_IMPLIES: Represents the rule for the negation of Zadeh implication.
   :type RULE_NOT_ZADEH_IMPLIES: typing.Any
   :param RULE_SIGMA_COUNT: Represents a rule or condition involving the sigma count (fuzzy cardinality) operation.
   :type RULE_SIGMA_COUNT: typing.Any
   :param RULE_NOT_SIGMA_COUNT: Represents the negation of the sigma count rule.
   :type RULE_NOT_SIGMA_COUNT: typing.Any


   .. py:method:: __repr__() -> str

      Returns a string representation of the `KnowledgeBaseRules` instance by delegating to the `__str__` method. This ensures that the official representation used by the interpreter and debugging tools matches the informal string output. The method does not modify the object's state.

      :return: The string representation of the object, obtained by calling str() on the instance.

      :rtype: str



   .. py:method:: __str__() -> str

      Returns a human-readable string representation of the KnowledgeBaseRules instance by processing the object's `name` attribute. This method strips the 'RULE_' substring from the name to provide a simplified identifier, leaving the rest of the string intact if the prefix is not present. It is automatically invoked when the instance is converted to a string or printed.

      :return: The object's name with the 'RULE_' prefix removed.

      :rtype: str



   .. py:attribute:: RULE_ATOMIC
      :value: 0



   .. py:attribute:: RULE_BOTTOM
      :value: 11



   .. py:attribute:: RULE_CHOQUET_INTEGRAL
      :value: 30



   .. py:attribute:: RULE_COMPLEMENT
      :value: 1



   .. py:attribute:: RULE_CONCRETE
      :value: 14



   .. py:attribute:: RULE_DATATYPE
      :value: 18



   .. py:attribute:: RULE_FUZZY_NUMBER
      :value: 20



   .. py:attribute:: RULE_GOEDEL_ALL
      :value: 8



   .. py:attribute:: RULE_GOEDEL_AND
      :value: 2



   .. py:attribute:: RULE_GOEDEL_IMPLIES
      :value: 12



   .. py:attribute:: RULE_GOEDEL_OR
      :value: 4



   .. py:attribute:: RULE_GOEDEL_SOME
      :value: 6



   .. py:attribute:: RULE_HAS_VALUE
      :value: 44



   .. py:attribute:: RULE_LUKASIEWICZ_ALL
      :value: 9



   .. py:attribute:: RULE_LUKASIEWICZ_AND
      :value: 3



   .. py:attribute:: RULE_LUKASIEWICZ_OR
      :value: 5



   .. py:attribute:: RULE_LUKASIEWICZ_SOME
      :value: 7



   .. py:attribute:: RULE_MODIFIED
      :value: 16



   .. py:attribute:: RULE_NOT_CHOQUET_INTEGRAL
      :value: 31



   .. py:attribute:: RULE_NOT_CONCRETE
      :value: 15



   .. py:attribute:: RULE_NOT_DATATYPE
      :value: 19



   .. py:attribute:: RULE_NOT_FUZZY_NUMBER
      :value: 21



   .. py:attribute:: RULE_NOT_GOEDEL_IMPLIES
      :value: 13



   .. py:attribute:: RULE_NOT_HAS_VALUE
      :value: 45



   .. py:attribute:: RULE_NOT_MODIFIED
      :value: 17



   .. py:attribute:: RULE_NOT_OWA
      :value: 27



   .. py:attribute:: RULE_NOT_QUASI_SUGENO_INTEGRAL
      :value: 35



   .. py:attribute:: RULE_NOT_SELF
      :value: 37



   .. py:attribute:: RULE_NOT_SIGMA_COUNT
      :value: 49



   .. py:attribute:: RULE_NOT_SUGENO_INTEGRAL
      :value: 33



   .. py:attribute:: RULE_NOT_THRESHOLD
      :value: 25



   .. py:attribute:: RULE_NOT_WEIGHTED
      :value: 23



   .. py:attribute:: RULE_NOT_W_MAX
      :value: 41



   .. py:attribute:: RULE_NOT_W_MIN
      :value: 39



   .. py:attribute:: RULE_NOT_W_SUM
      :value: 29



   .. py:attribute:: RULE_NOT_W_SUM_ZERO
      :value: 43



   .. py:attribute:: RULE_NOT_ZADEH_IMPLIES
      :value: 47



   .. py:attribute:: RULE_OWA
      :value: 26



   .. py:attribute:: RULE_QUASI_SUGENO_INTEGRAL
      :value: 34



   .. py:attribute:: RULE_SELF
      :value: 36



   .. py:attribute:: RULE_SIGMA_COUNT
      :value: 48



   .. py:attribute:: RULE_SUGENO_INTEGRAL
      :value: 32



   .. py:attribute:: RULE_THRESHOLD
      :value: 24



   .. py:attribute:: RULE_TOP
      :value: 10



   .. py:attribute:: RULE_WEIGHTED
      :value: 22



   .. py:attribute:: RULE_W_MAX
      :value: 40



   .. py:attribute:: RULE_W_MIN
      :value: 38



   .. py:attribute:: RULE_W_SUM
      :value: 28



   .. py:attribute:: RULE_W_SUM_ZERO
      :value: 42



   .. py:attribute:: RULE_ZADEH_IMPLIES
      :value: 46



.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_util_constants_LogicOperatorType.png
       :alt: UML Class Diagram for LogicOperatorType
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **LogicOperatorType**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_util_constants_LogicOperatorType.pdf
       :alt: UML Class Diagram for LogicOperatorType
       :align: center
       :width: 4.7cm
       :class: uml-diagram

       UML Class Diagram for **LogicOperatorType**

.. py:class:: LogicOperatorType(*args, **kwds)

   Bases: :py:obj:`enum.Enum`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.util.constants.LogicOperatorType
      :parts: 1
      :private-bases:


   This enumeration defines the specific logic operator strategies available to the reasoning engine, corresponding to standard fuzzy logic systems. It includes variants such as Lukasiewicz, Gödel, Kleene-Dienes, and Zadeh, which determine how logical operations like conjunction and disjunction are evaluated within the system. When converted to a string or represented, the value returns its identifier name rather than its underlying integer code.

   :param LUKASIEWICZ: Represents the Łukasiewicz logic operator, commonly used in many-valued logic reasoning.
   :type LUKASIEWICZ: typing.Any
   :param GOEDEL: Represents the Gödel logic operator type used by the reasoner.
   :type GOEDEL: typing.Any
   :param KLEENE_DIENES: Represents the Kleene-Dienes logic operator, a specific operator type used by the reasoner.
   :type KLEENE_DIENES: typing.Any
   :param ZADEH: Represents the standard fuzzy logic operators defined by Lotfi Zadeh, utilizing minimum for conjunction and maximum for disjunction.
   :type ZADEH: typing.Any


   .. py:method:: __repr__() -> str

      Returns the name of the logic operator type as its official string representation. This method overrides the default behavior to provide a concise and readable identifier, which is particularly useful for debugging and logging. It simply returns the value of the `name` attribute associated with the instance.

      :return: The name of the object.

      :rtype: str



   .. py:method:: __str__() -> str

      Returns the string representation of the logic operator type by accessing its internal name attribute. This method is invoked implicitly when the object is converted to a string, such as during printing or string formatting operations. It ensures that the textual output corresponds directly to the identifier defined for the specific operator.

      :return: Returns the string representation of the object, which is its name.

      :rtype: str



   .. py:attribute:: GOEDEL
      :value: 1



   .. py:attribute:: KLEENE_DIENES
      :value: 2



   .. py:attribute:: LUKASIEWICZ
      :value: 0



   .. py:attribute:: ZADEH
      :value: 3



.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_util_constants_MILPProvider.png
       :alt: UML Class Diagram for MILPProvider
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **MILPProvider**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_util_constants_MILPProvider.pdf
       :alt: UML Class Diagram for MILPProvider
       :align: center
       :width: 6.7cm
       :class: uml-diagram

       UML Class Diagram for **MILPProvider**

.. py:class:: MILPProvider

   Bases: :py:obj:`enum.StrEnum`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.util.constants.MILPProvider
      :parts: 1
      :private-bases:


   This enumeration defines the available Mixed-Integer Linear Programming (MILP) solver backends supported by the reasoning system. It provides specific members for distinct solvers such as GUROBI and MIP, as well as configurations for the PULP library using different underlying engines like GLPK, HiGHS, or CPLEX. As a string-based enum, it facilitates configuration by allowing direct string comparisons, and it includes a static `from_str` method to safely parse case-insensitive string inputs into the corresponding enum member, raising an error for invalid values.

   :param GUROBI: Selects the Gurobi solver for MILP optimization.
   :type GUROBI: typing.Any
   :param MIP: Selects the Python-MIP solver backend.
   :type MIP: typing.Any
   :param PULP: Represents the default solver backend provided by the PuLP library.
   :type PULP: typing.Any
   :param PULP_GLPK: Uses the GLPK solver via the PuLP interface.
   :type PULP_GLPK: typing.Any
   :param PULP_HIGHS: Specifies the HiGHS solver, accessed via the PuLP library.
   :type PULP_HIGHS: typing.Any
   :param PULP_CPLEX: Uses the CPLEX solver via the PuLP interface.
   :type PULP_CPLEX: typing.Any

   :raises ValueError: Raised when the string provided to `from_str` does not match any of the available MILP provider options.


   .. py:method:: from_str(value: str) -> Self
      :staticmethod:


      This static method parses a string representation of a provider name and returns the corresponding `MILPProvider` enumeration member. The matching process is case-insensitive, as the input string is converted to lowercase before lookup. If the provided value does not correspond to any defined provider, a `ValueError` is raised with a message listing the valid available options.

      :param value: The name of the MILP provider to convert.
      :type value: str

      :raises ValueError: If the provided string does not correspond to a valid `MILPProvider` member.

      :return: The `MILPProvider` enum member corresponding to the input string, matched case-insensitively.

      :rtype: typing.Self



   .. py:attribute:: GUROBI


   .. py:attribute:: MIP


   .. py:attribute:: PULP


   .. py:attribute:: PULP_CPLEX


   .. py:attribute:: PULP_GLPK


   .. py:attribute:: PULP_HIGHS


.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_util_constants_RepresentativeIndividualType.png
       :alt: UML Class Diagram for RepresentativeIndividualType
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **RepresentativeIndividualType**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_util_constants_RepresentativeIndividualType.pdf
       :alt: UML Class Diagram for RepresentativeIndividualType
       :align: center
       :width: 6.7cm
       :class: uml-diagram

       UML Class Diagram for **RepresentativeIndividualType**

.. py:class:: RepresentativeIndividualType(*args, **kwds)

   Bases: :py:obj:`enum.Enum`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.util.constants.RepresentativeIndividualType
      :parts: 1
      :private-bases:


   This enumeration categorizes the specific types of representative individuals employed by the reasoning engine to define logical bounds or constraints. It distinguishes between two distinct options: `GREATER_EQUAL`, which typically represents a lower bound or minimum cardinality, and `LESS_EQUAL`, which represents an upper bound or maximum cardinality. By selecting one of these values, the reasoner can determine the specific inequality or approximation strategy to apply when processing a concept.

   :param GREATER_EQUAL: Represents a representative individual satisfying a greater-than-or-equal-to condition.
   :type GREATER_EQUAL: typing.Any
   :param LESS_EQUAL: Indicates that the representative individual is used for less-than-or-equal-to comparisons.
   :type LESS_EQUAL: typing.Any


   .. py:method:: __repr__() -> str

      Returns the string representation of the object, which is defined as the value of the `name` attribute. This implementation provides a direct and concise identifier for the instance rather than a formal representation including the class name. It is primarily used for debugging and logging contexts where the specific name of the individual type is the most relevant information.

      :return: A string representation of the object, specifically the value of its `name` attribute.

      :rtype: str



   .. py:method:: __str__() -> str

      Returns a human-readable string representation of the `RepresentativeIndividualType` instance by delegating to the object's `name` attribute. This method is automatically invoked when the instance is converted to a string using the built-in `str()` function or formatted for output, such as in print statements. The implementation has no side effects, though it assumes that the `name` attribute is defined and contains a value that serves as a valid string representation.

      :return: The informal string representation of the object, which is its name.

      :rtype: str



   .. py:attribute:: GREATER_EQUAL
      :value: 0



   .. py:attribute:: LESS_EQUAL
      :value: 1



.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_util_constants_RestrictionType.png
       :alt: UML Class Diagram for RestrictionType
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **RestrictionType**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_util_constants_RestrictionType.pdf
       :alt: UML Class Diagram for RestrictionType
       :align: center
       :width: 4.0cm
       :class: uml-diagram

       UML Class Diagram for **RestrictionType**

.. py:class:: RestrictionType(*args, **kwds)

   Bases: :py:obj:`enum.Enum`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.util.constants.RestrictionType
      :parts: 1
      :private-bases:


   This enumeration defines the specific categories of constraints that can be applied by the reasoning engine. It distinguishes between three primary modes of restriction: an upper bound limit (`AT_MOST_VALUE`), a lower bound limit (`AT_LEAST_VALUE`), and a precise equality requirement (`EXACT_VALUE`). By utilizing these members, developers can explicitly declare the nature of a restriction, allowing the reasoner to correctly interpret and enforce the intended logic on the associated values.

   :param AT_MOST_VALUE: Specifies that the value must be less than or equal to a defined maximum.
   :type AT_MOST_VALUE: typing.Any
   :param AT_LEAST_VALUE: Represents a restriction requiring the value to be greater than or equal to a specified threshold.
   :type AT_LEAST_VALUE: typing.Any
   :param EXACT_VALUE: Indicates that the restricted property or quantity must match the specified value exactly.
   :type EXACT_VALUE: typing.Any


   .. py:method:: __repr__() -> str

      Returns the official string representation of the restriction type instance by returning the value of its `name` attribute. This method is intended to provide a concise and unambiguous identifier for the object, typically used for debugging and logging. It performs no side effects and assumes the `name` attribute is populated with a string value.

      :return: The name of the object.

      :rtype: str



   .. py:method:: __str__() -> str

      Returns a human-readable string representation of the restriction type instance. This method is invoked by the built-in `str()` function and string formatting operations, allowing the object to be displayed cleanly in logs or user interfaces. It simply returns the value of the `name` attribute, ensuring that the string output corresponds directly to the instance's identifier. The method has no side effects and assumes that the `name` attribute is defined on the instance.

      :return: The string representation of the object, which is its name.

      :rtype: str



   .. py:attribute:: AT_LEAST_VALUE
      :value: 1



   .. py:attribute:: AT_MOST_VALUE
      :value: 0



   .. py:attribute:: EXACT_VALUE
      :value: 2



.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_util_constants_VariableType.png
       :alt: UML Class Diagram for VariableType
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **VariableType**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_util_constants_VariableType.pdf
       :alt: UML Class Diagram for VariableType
       :align: center
       :width: 3.7cm
       :class: uml-diagram

       UML Class Diagram for **VariableType**

.. py:class:: VariableType

   Bases: :py:obj:`enum.StrEnum`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.util.constants.VariableType
      :parts: 1
      :private-bases:


   This enumeration defines the permissible domains for variables, typically within the context of mathematical optimization or modeling. It categorizes variables into distinct types such as binary, continuous, integer, and semi-continuous, each imposing specific constraints on the values the variable can assume. As a string-based enumeration, members can be used directly in string comparisons or serialization, and the class is configured to return the member's name when represented as a string.

   :param BINARY: Represents a variable restricted to two values, typically 0 and 1.
   :type BINARY: typing.Any
   :param CONTINUOUS: Represents a variable that can take any real value within its bounds.
   :type CONTINUOUS: typing.Any
   :param INTEGER: Represents a variable restricted to integer values.
   :type INTEGER: typing.Any
   :param SEMI_CONTINUOUS: Represents a variable that is either zero or takes a value within a specified continuous range.
   :type SEMI_CONTINUOUS: typing.Any


   .. py:method:: __repr__() -> str

      Returns the official string representation of the `VariableType` instance. The implementation delegates directly to the `name` attribute, returning its value as the representation. This method has no side effects and is primarily used for debugging and logging purposes.

      :return: Returns the string representation of the object, which is the value of its `name` attribute.

      :rtype: str



   .. py:method:: __str__() -> str

      Provides a human-readable string representation of the `VariableType` instance by returning the value of its `name` attribute. This method is automatically invoked by the built-in `str()` function and during string formatting operations, such as when using `print()` or f-strings. The operation has no side effects and relies on the `name` attribute being present on the instance.

      :return: The name of the object.

      :rtype: str



   .. py:attribute:: BINARY


   .. py:attribute:: CONTINUOUS


   .. py:attribute:: INTEGER


   .. py:attribute:: SEMI_CONTINUOUS


.. py:data:: KNOWLEDGE_BASE_SEMANTICS
   :type:  FuzzyLogic

.. py:data:: MAXVAL
   :type:  float
   :value: 2147483647000


.. py:data:: MAXVAL2
   :type:  float
   :value: 4294967294000


.. py:data:: NUMBER

.. py:data:: RESULTS_PATH
   :type:  str

.. py:data:: SEPARATOR
   :type:  str
   :value: '-------------------------'


.. py:data:: STAR_SEPARATOR
   :type:  str
   :value: '*************************'

