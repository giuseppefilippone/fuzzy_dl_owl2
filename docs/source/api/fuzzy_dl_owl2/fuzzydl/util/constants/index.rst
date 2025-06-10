fuzzy_dl_owl2.fuzzydl.util.constants
====================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.util.constants


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

.. py:class:: BlockingDynamicType(*args, **kwds)

   Bases: :py:obj:`enum.Enum`


   Create a collection of name/value pairs.

   Example enumeration:

   >>> class Color(Enum):
   ...     RED = 1
   ...     BLUE = 2
   ...     GREEN = 3

   Access them by:

   - attribute access::

   >>> Color.RED
   <Color.RED: 1>

   - value lookup:

   >>> Color(1)
   <Color.RED: 1>

   - name lookup:

   >>> Color['RED']
   <Color.RED: 1>

   Enumerations can be iterated over, and know how many members they have:

   >>> len(Color)
   3

   >>> list(Color)
   [<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]

   Methods can be added to enumerations, and members can have their own
   attributes -- see the documentation for details.


   .. py:method:: __repr__() -> str


   .. py:method:: __str__() -> str


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



.. py:class:: ConceptType(*args, **kwds)

   Bases: :py:obj:`enum.Enum`


   Create a collection of name/value pairs.

   Example enumeration:

   >>> class Color(Enum):
   ...     RED = 1
   ...     BLUE = 2
   ...     GREEN = 3

   Access them by:

   - attribute access::

   >>> Color.RED
   <Color.RED: 1>

   - value lookup:

   >>> Color(1)
   <Color.RED: 1>

   - name lookup:

   >>> Color['RED']
   <Color.RED: 1>

   Enumerations can be iterated over, and know how many members they have:

   >>> len(Color)
   3

   >>> list(Color)
   [<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]

   Methods can be added to enumerations, and members can have their own
   attributes -- see the documentation for details.


   .. py:method:: __repr__() -> str


   .. py:method:: __str__() -> str


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



.. py:class:: ConcreteFeatureType(*args, **kwds)

   Bases: :py:obj:`enum.Enum`


   Create a collection of name/value pairs.

   Example enumeration:

   >>> class Color(Enum):
   ...     RED = 1
   ...     BLUE = 2
   ...     GREEN = 3

   Access them by:

   - attribute access::

   >>> Color.RED
   <Color.RED: 1>

   - value lookup:

   >>> Color(1)
   <Color.RED: 1>

   - name lookup:

   >>> Color['RED']
   <Color.RED: 1>

   Enumerations can be iterated over, and know how many members they have:

   >>> len(Color)
   3

   >>> list(Color)
   [<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]

   Methods can be added to enumerations, and members can have their own
   attributes -- see the documentation for details.


   .. py:method:: __repr__() -> str


   .. py:method:: __str__() -> str


   .. py:attribute:: BOOLEAN
      :value: 3



   .. py:attribute:: INTEGER
      :value: 1



   .. py:attribute:: REAL
      :value: 2



   .. py:attribute:: STRING
      :value: 0



.. py:class:: CreatedIndividualBlockingType(*args, **kwds)

   Bases: :py:obj:`enum.Enum`


   Create a collection of name/value pairs.

   Example enumeration:

   >>> class Color(Enum):
   ...     RED = 1
   ...     BLUE = 2
   ...     GREEN = 3

   Access them by:

   - attribute access::

   >>> Color.RED
   <Color.RED: 1>

   - value lookup:

   >>> Color(1)
   <Color.RED: 1>

   - name lookup:

   >>> Color['RED']
   <Color.RED: 1>

   Enumerations can be iterated over, and know how many members they have:

   >>> len(Color)
   3

   >>> list(Color)
   [<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]

   Methods can be added to enumerations, and members can have their own
   attributes -- see the documentation for details.


   .. py:method:: __repr__() -> str


   .. py:method:: __str__() -> str


   .. py:attribute:: BLOCKED
      :value: 0



   .. py:attribute:: NOT_BLOCKED
      :value: 1



   .. py:attribute:: UNCHECKED
      :value: 2



.. py:class:: FeatureFunctionType(*args, **kwds)

   Bases: :py:obj:`enum.Enum`


   Create a collection of name/value pairs.

   Example enumeration:

   >>> class Color(Enum):
   ...     RED = 1
   ...     BLUE = 2
   ...     GREEN = 3

   Access them by:

   - attribute access::

   >>> Color.RED
   <Color.RED: 1>

   - value lookup:

   >>> Color(1)
   <Color.RED: 1>

   - name lookup:

   >>> Color['RED']
   <Color.RED: 1>

   Enumerations can be iterated over, and know how many members they have:

   >>> len(Color)
   3

   >>> list(Color)
   [<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]

   Methods can be added to enumerations, and members can have their own
   attributes -- see the documentation for details.


   .. py:method:: __repr__() -> str


   .. py:method:: __str__() -> str


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



.. py:class:: FuzzyDLKeyword(*args, **kwds)

   Bases: :py:obj:`enum.Enum`


   Create a collection of name/value pairs.

   Example enumeration:

   >>> class Color(Enum):
   ...     RED = 1
   ...     BLUE = 2
   ...     GREEN = 3

   Access them by:

   - attribute access::

   >>> Color.RED
   <Color.RED: 1>

   - value lookup:

   >>> Color(1)
   <Color.RED: 1>

   - name lookup:

   >>> Color['RED']
   <Color.RED: 1>

   Enumerations can be iterated over, and know how many members they have:

   >>> len(Color)
   3

   >>> list(Color)
   [<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]

   Methods can be added to enumerations, and members can have their own
   attributes -- see the documentation for details.


   .. py:method:: __eq__(value: object) -> bool


   .. py:method:: __repr__() -> str


   .. py:method:: __str__() -> str


   .. py:method:: get_name() -> str


   .. py:method:: get_value() -> Union[pyparsing.CaselessKeyword, pyparsing.Literal]


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


.. py:class:: FuzzyLogic

   Bases: :py:obj:`enum.StrEnum`


   Enum where members are also (and must be) strings


   .. py:method:: __repr__() -> str

      Return repr(self).



   .. py:method:: __str__() -> str

      Return str(self).



   .. py:attribute:: CLASSICAL
      :value: 'classical'



   .. py:attribute:: LUKASIEWICZ
      :value: 'lukasiewicz'



   .. py:attribute:: ZADEH
      :value: 'zadeh'



.. py:class:: InequalityType

   Bases: :py:obj:`enum.StrEnum`


   Enum where members are also (and must be) strings


   .. py:method:: __repr__() -> str

      Return repr(self).



   .. py:method:: __str__() -> str

      Return str(self).



   .. py:attribute:: EQUAL
      :value: '='



   .. py:attribute:: GREATER_THAN
      :value: '>'



   .. py:attribute:: LESS_THAN
      :value: '<'



.. py:class:: KnowledgeBaseRules(*args, **kwds)

   Bases: :py:obj:`enum.Enum`


   Create a collection of name/value pairs.

   Example enumeration:

   >>> class Color(Enum):
   ...     RED = 1
   ...     BLUE = 2
   ...     GREEN = 3

   Access them by:

   - attribute access::

   >>> Color.RED
   <Color.RED: 1>

   - value lookup:

   >>> Color(1)
   <Color.RED: 1>

   - name lookup:

   >>> Color['RED']
   <Color.RED: 1>

   Enumerations can be iterated over, and know how many members they have:

   >>> len(Color)
   3

   >>> list(Color)
   [<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]

   Methods can be added to enumerations, and members can have their own
   attributes -- see the documentation for details.


   .. py:method:: __repr__() -> str


   .. py:method:: __str__() -> str


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



.. py:class:: LogicOperatorType(*args, **kwds)

   Bases: :py:obj:`enum.Enum`


   Create a collection of name/value pairs.

   Example enumeration:

   >>> class Color(Enum):
   ...     RED = 1
   ...     BLUE = 2
   ...     GREEN = 3

   Access them by:

   - attribute access::

   >>> Color.RED
   <Color.RED: 1>

   - value lookup:

   >>> Color(1)
   <Color.RED: 1>

   - name lookup:

   >>> Color['RED']
   <Color.RED: 1>

   Enumerations can be iterated over, and know how many members they have:

   >>> len(Color)
   3

   >>> list(Color)
   [<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]

   Methods can be added to enumerations, and members can have their own
   attributes -- see the documentation for details.


   .. py:method:: __repr__() -> str


   .. py:method:: __str__() -> str


   .. py:attribute:: GOEDEL
      :value: 1



   .. py:attribute:: KLEENE_DIENES
      :value: 2



   .. py:attribute:: LUKASIEWICZ
      :value: 0



   .. py:attribute:: ZADEH
      :value: 3



.. py:class:: MILPProvider

   Bases: :py:obj:`enum.StrEnum`


   Enum where members are also (and must be) strings


   .. py:method:: from_str(value: str) -> Self
      :staticmethod:



   .. py:attribute:: GUROBI


   .. py:attribute:: MIP


   .. py:attribute:: PULP


   .. py:attribute:: PULP_CPLEX


   .. py:attribute:: PULP_GLPK


   .. py:attribute:: PULP_HIGHS


.. py:class:: RepresentativeIndividualType(*args, **kwds)

   Bases: :py:obj:`enum.Enum`


   Create a collection of name/value pairs.

   Example enumeration:

   >>> class Color(Enum):
   ...     RED = 1
   ...     BLUE = 2
   ...     GREEN = 3

   Access them by:

   - attribute access::

   >>> Color.RED
   <Color.RED: 1>

   - value lookup:

   >>> Color(1)
   <Color.RED: 1>

   - name lookup:

   >>> Color['RED']
   <Color.RED: 1>

   Enumerations can be iterated over, and know how many members they have:

   >>> len(Color)
   3

   >>> list(Color)
   [<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]

   Methods can be added to enumerations, and members can have their own
   attributes -- see the documentation for details.


   .. py:method:: __repr__() -> str


   .. py:method:: __str__() -> str


   .. py:attribute:: GREATER_EQUAL
      :value: 0



   .. py:attribute:: LESS_EQUAL
      :value: 1



.. py:class:: RestrictionType(*args, **kwds)

   Bases: :py:obj:`enum.Enum`


   Create a collection of name/value pairs.

   Example enumeration:

   >>> class Color(Enum):
   ...     RED = 1
   ...     BLUE = 2
   ...     GREEN = 3

   Access them by:

   - attribute access::

   >>> Color.RED
   <Color.RED: 1>

   - value lookup:

   >>> Color(1)
   <Color.RED: 1>

   - name lookup:

   >>> Color['RED']
   <Color.RED: 1>

   Enumerations can be iterated over, and know how many members they have:

   >>> len(Color)
   3

   >>> list(Color)
   [<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]

   Methods can be added to enumerations, and members can have their own
   attributes -- see the documentation for details.


   .. py:method:: __repr__() -> str


   .. py:method:: __str__() -> str


   .. py:attribute:: AT_LEAST_VALUE
      :value: 1



   .. py:attribute:: AT_MOST_VALUE
      :value: 0



   .. py:attribute:: EXACT_VALUE
      :value: 2



.. py:class:: VariableType

   Bases: :py:obj:`enum.StrEnum`


   Enum where members are also (and must be) strings


   .. py:method:: __repr__() -> str

      Return repr(self).



   .. py:method:: __str__() -> str

      Return str(self).



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


