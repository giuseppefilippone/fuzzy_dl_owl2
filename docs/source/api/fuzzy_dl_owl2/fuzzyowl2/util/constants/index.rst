fuzzy_dl_owl2.fuzzyowl2.util.constants
======================================

.. py:module:: fuzzy_dl_owl2.fuzzyowl2.util.constants



.. ── LLM-GENERATED DESCRIPTION START ──

Centralizes the definition of fuzzy concept types and parsing keywords required for processing the FuzzyOWL2 ontology language.


Description
-----------


The ``ConceptType`` enumeration categorizes various fuzzy logic constructs, such as aggregation operators and weighted operations, serving as a type discriminator to ensure correct semantic application during ontology manipulation. Complementing this, the ``FuzzyOWL2Keyword`` enumeration maps the specific vocabulary of the FuzzyOWL2 syntax—including logic operators, comparison symbols, and structural tags—to their corresponding ``pyparsing`` objects. By encapsulating parser definitions within an enumeration, the codebase avoids scattered string literals and provides a robust mechanism for token identification. Custom equality overrides further enhance usability by allowing comparisons against raw strings or parser objects directly, ensuring that the parsing logic remains both readable and maintainable.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzyowl2.util.constants.ConceptType
   fuzzy_dl_owl2.fuzzyowl2.util.constants.FuzzyOWL2Keyword


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzyowl2_util_constants_ConceptType.png
       :alt: UML Class Diagram for ConceptType
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **ConceptType**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzyowl2_util_constants_ConceptType.pdf
       :alt: UML Class Diagram for ConceptType
       :align: center
       :width: 3.7cm
       :class: uml-diagram

       UML Class Diagram for **ConceptType**

.. py:class:: ConceptType

   Bases: :py:obj:`enum.StrEnum`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzyowl2.util.constants.ConceptType
      :parts: 1
      :private-bases:


   This enumeration categorizes the various types of fuzzy concepts utilized within the FuzzyOWL2 framework. Extending `StrEnum`, it provides a set of string-based identifiers that distinguish between different fuzzy logic constructs, such as aggregation operators (e.g., Sugeno, Choquet, OWA), weighted operations (e.g., Weighted Sum, Weighted Min), and structural modifications (e.g., Modified Concept, Fuzzy Nominal). It serves as a type discriminator for concept definitions, ensuring that specific fuzzy semantics are correctly applied during ontology processing.

   :param CHOQUET: Represents a concept defined using the Choquet integral aggregation operator.
   :type CHOQUET: typing.Any
   :param FUZZY_NOMINAL: Represents a concept defined by a fuzzy nominal, typically involving specific individuals or enumerated values with fuzzy membership degrees.
   :type FUZZY_NOMINAL: typing.Any
   :param MODIFIED_CONCEPT: Represents a concept that has been modified by a specific function or hedge.
   :type MODIFIED_CONCEPT: typing.Any
   :param OWA: Represents a concept defined using the Ordered Weighted Averaging (OWA) aggregation operator.
   :type OWA: typing.Any
   :param QUANTIFIED_OWA: Represents a concept type that employs Quantified Ordered Weighted Averaging (OWA) aggregation.
   :type QUANTIFIED_OWA: typing.Any
   :param QUASI_SUGENO: Represents a concept defined using the Quasi-Sugeno fuzzy integral.
   :type QUASI_SUGENO: typing.Any
   :param SUGENO: Represents a concept defined using the Sugeno integral.
   :type SUGENO: typing.Any
   :param WEIGHTED_CONCEPT: Represents a concept that is associated with a specific weight, serving as a fundamental element for weighted aggregation operations.
   :type WEIGHTED_CONCEPT: typing.Any
   :param WEIGHTED_MAX: Represents a fuzzy concept defined using the weighted maximum aggregation operator.
   :type WEIGHTED_MAX: typing.Any
   :param WEIGHTED_MIN: Represents a fuzzy concept defined using the weighted minimum aggregation operator.
   :type WEIGHTED_MIN: typing.Any
   :param WEIGHTED_SUM: Represents a concept defined by the weighted sum aggregation operator.
   :type WEIGHTED_SUM: typing.Any
   :param WEIGHTED_SUM_ZERO: Represents a concept type defined by a weighted sum aggregation with a zero-sum constraint.
   :type WEIGHTED_SUM_ZERO: typing.Any


   .. py:method:: __repr__() -> str

      Returns the official string representation of the ConceptType instance. This implementation returns the value of the object's 'name' attribute directly, providing a concise and human-readable identifier for the concept. The method has no side effects and relies solely on the current state of the 'name' attribute.

      :return: A string representation of the object, corresponding to its name.

      :rtype: str



   .. py:method:: __str__() -> str

      Returns a human-readable string representation of the instance, which is primarily used for display purposes or when the object is converted to a string. This implementation specifically returns the value of the `name` attribute associated with the `ConceptType` instance, providing a concise identifier rather than a detailed structural representation.

      :return: The name of the object.

      :rtype: str



   .. py:attribute:: CHOQUET


   .. py:attribute:: FUZZY_NOMINAL


   .. py:attribute:: MODIFIED_CONCEPT


   .. py:attribute:: OWA


   .. py:attribute:: QUANTIFIED_OWA


   .. py:attribute:: QUASI_SUGENO


   .. py:attribute:: SUGENO


   .. py:attribute:: WEIGHTED_CONCEPT


   .. py:attribute:: WEIGHTED_MAX


   .. py:attribute:: WEIGHTED_MIN


   .. py:attribute:: WEIGHTED_SUM


   .. py:attribute:: WEIGHTED_SUM_ZERO


.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzyowl2_util_constants_FuzzyOWL2Keyword.png
       :alt: UML Class Diagram for FuzzyOWL2Keyword
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **FuzzyOWL2Keyword**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzyowl2_util_constants_FuzzyOWL2Keyword.pdf
       :alt: UML Class Diagram for FuzzyOWL2Keyword
       :align: center
       :width: 11.8cm
       :class: uml-diagram

       UML Class Diagram for **FuzzyOWL2Keyword**

.. py:class:: FuzzyOWL2Keyword(*args, **kwds)

   Bases: :py:obj:`enum.Enum`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzyowl2.util.constants.FuzzyOWL2Keyword
      :parts: 1
      :private-bases:


   This enumeration defines the specific vocabulary and structural tokens used in the FuzzyOWL2 language, mapping semantic concepts such as fuzzy logic operators, modifiers, and XML-like tags to their corresponding `pyparsing` definitions. It serves as a centralized registry for constructing grammars or validating syntax, where each member encapsulates a parser object that recognizes a specific keyword or symbol. The class provides utility methods to extract the string representation or the underlying parser object, and it overrides the equality comparison to allow flexible matching against raw strings, parser keywords, or other enum members based on the normalized token name.

   :param OPEN_TAG: Parser element representing the opening angle bracket delimiter used in FuzzyOWL2 syntax.
   :type OPEN_TAG: typing.Any
   :param CLOSE_TAG: Pyparsing element that matches the closing angle bracket character used to terminate tags.
   :type CLOSE_TAG: typing.Any
   :param SINGLE_CLOSE_TAG: Represents the self-closing tag delimiter '/>' used in FuzzyOWL2 syntax.
   :type SINGLE_CLOSE_TAG: typing.Any
   :param SLASH: Parser element representing the forward slash character used in FuzzyOWL2 syntax.
   :type SLASH: typing.Any
   :param ONTOLOGY: Parser element for the 'ontology' keyword.
   :type ONTOLOGY: typing.Any
   :param FUZZY_OWL_2: Keyword representing the 'fuzzyOwl2' identifier.
   :type FUZZY_OWL_2: typing.Any
   :param FUZZY_LABEL: Parser keyword for the 'fuzzyLabel' token used in FuzzyOWL2 syntax.
   :type FUZZY_LABEL: typing.Any
   :param FUZZY_TYPE: Parser token for the "fuzzyType" keyword used to specify the type of fuzzy logic or set.
   :type FUZZY_TYPE: typing.Any
   :param FUZZY_LOGIC: Keyword representing the "FuzzyLogic" token used to define or specify the fuzzy logic system within the ontology.
   :type FUZZY_LOGIC: typing.Any
   :param TYPE: Keyword representing the 'type' token in FuzzyOWL2 syntax.
   :type TYPE: typing.Any
   :param LOGIC: Keyword matching the 'logic' token used to define the fuzzy logic type.
   :type LOGIC: typing.Any
   :param DATATYPE: Parser element matching the 'datatype' keyword in FuzzyOWL2 syntax.
   :type DATATYPE: typing.Any
   :param CONCEPT: Parser element matching the 'concept' keyword in FuzzyOWL2 syntax.
   :type CONCEPT: typing.Any
   :param ROLE: Keyword identifying a role (object property) in FuzzyOWL2 syntax.
   :type ROLE: typing.Any
   :param AXIOM: Keyword representing the 'axiom' construct in FuzzyOWL2 syntax.
   :type AXIOM: typing.Any
   :param DEGREE_DEF: Keyword used to define the degree of truth or membership in fuzzy axioms.
   :type DEGREE_DEF: typing.Any
   :param DEGREE_VALUE: Keyword representing the specific value associated with a fuzzy degree definition.
   :type DEGREE_VALUE: typing.Any
   :param MODIFIED: Represents the 'modified' keyword used in the FuzzyOWL2 syntax.
   :type MODIFIED: typing.Any
   :param WEIGHTED: Keyword token representing the 'weighted' identifier in FuzzyOWL2 syntax.
   :type WEIGHTED: typing.Any
   :param NOMINAL: Keyword representing the 'nominal' construct in FuzzyOWL2 syntax.
   :type NOMINAL: typing.Any
   :param INDIVIDUAL: Keyword representing an individual in the FuzzyOWL2 syntax.
   :type INDIVIDUAL: typing.Any
   :param WEIGHTED_MAXIMUM: Keyword representing the weighted maximum aggregation operator in FuzzyOWL2 syntax.
   :type WEIGHTED_MAXIMUM: typing.Any
   :param WEIGHTED_MINIMUM: Keyword representing the weighted minimum operator in FuzzyOWL2 syntax.
   :type WEIGHTED_MINIMUM: typing.Any
   :param WEIGHTED_SUM: Keyword for the weighted sum operator in FuzzyOWL2.
   :type WEIGHTED_SUM: typing.Any
   :param WEIGHTED_SUMZERO: Keyword for the weighted sum zero aggregation operator.
   :type WEIGHTED_SUMZERO: typing.Any
   :param OWA: Keyword representing the Ordered Weighted Averaging (OWA) aggregation operator.
   :type OWA: typing.Any
   :param Q_OWA: Represents the 'qowa' keyword used for Quantified Ordered Weighted Averaging operations.
   :type Q_OWA: typing.Any
   :param CHOQUET: Keyword representing the Choquet integral aggregation operator.
   :type CHOQUET: typing.Any
   :param SUGENO: Keyword representing the Sugeno fuzzy integral or aggregation operator.
   :type SUGENO: typing.Any
   :param QUASI_SUGENO: Keyword representing the Quasi-Sugeno fuzzy integral or operator.
   :type QUASI_SUGENO: typing.Any
   :param MODIFIER: Keyword representing the 'modifier' construct in FuzzyOWL2 syntax.
   :type MODIFIER: typing.Any
   :param BASE: Keyword representing the 'base' component, used to specify the underlying concept or type in fuzzy definitions.
   :type BASE: typing.Any
   :param CONCEPT_NAMES: Keyword representing the 'names' identifier used to denote concept names within the FuzzyOWL2 syntax.
   :type CONCEPT_NAMES: typing.Any
   :param NAME: Keyword representing the literal string 'name' used in FuzzyOWL2 syntax.
   :type NAME: typing.Any
   :param WEIGHT: Keyword representing the 'weight' identifier used in weighted fuzzy logic constructs.
   :type WEIGHT: typing.Any
   :param WEIGHTS: Keyword for the 'weights' identifier used to specify a collection of weight values in FuzzyOWL2 syntax.
   :type WEIGHTS: typing.Any
   :param QUANTIFIER: Keyword representing the 'quantifier' token in FuzzyOWL2 syntax.
   :type QUANTIFIER: typing.Any
   :param CRISP: Keyword used to denote a crisp (non-fuzzy) element or logic type within the FuzzyOWL2 ontology.
   :type CRISP: typing.Any
   :param LEFT_SHOULDER: Keyword representing a left shoulder membership function shape.
   :type LEFT_SHOULDER: typing.Any
   :param RIGHT_SHOULDER: Keyword representing the 'rightshoulder' shape for a fuzzy membership function.
   :type RIGHT_SHOULDER: typing.Any
   :param TRIANGULAR: Keyword for the triangular membership function shape.
   :type TRIANGULAR: typing.Any
   :param TRAPEZOIDAL: Keyword representing the trapezoidal membership function type.
   :type TRAPEZOIDAL: typing.Any
   :param LINEAR: Represents the 'linear' keyword used to define linear membership functions or types.
   :type LINEAR: typing.Any
   :param A: Keyword representing the 'a' parameter used in defining fuzzy membership function shapes (e.g., triangular or trapezoidal).
   :type A: typing.Any
   :param B: Represents the keyword for the 'b' parameter, commonly used in defining fuzzy membership functions such as triangular or trapezoidal shapes.
   :type B: typing.Any
   :param C: Keyword representing the third parameter ('c') used to define the shape of fuzzy membership functions, such as triangular or trapezoidal shapes.
   :type C: typing.Any
   :param D: Keyword representing the 'd' parameter, typically used as the fourth coordinate defining the right endpoint of a trapezoidal fuzzy membership function.
   :type D: typing.Any
   :param LUKASIEWICZ: Keyword representing the Łukasiewicz fuzzy logic type.
   :type LUKASIEWICZ: typing.Any
   :param GOEDEL: Keyword representing the Gödel fuzzy logic type.
   :type GOEDEL: typing.Any
   :param ZADEH: Keyword representing the Zadeh fuzzy logic type, which uses standard min and max operators.
   :type ZADEH: typing.Any
   :param PRODUCT: Keyword representing the "product" t-norm logic operator used in FuzzyOWL2 expressions.
   :type PRODUCT: typing.Any
   :param EQUAL: The equals sign symbol used in FuzzyOWL2 syntax.
   :type EQUAL: typing.Any
   :param LES: Represents the 'les' keyword used for strict less-than comparisons.
   :type LES: typing.Any
   :param LEQ: Keyword representing the less-than-or-equal-to comparison operator.
   :type LEQ: typing.Any
   :param GEQ: Keyword representing the "greater than or equal to" comparison operator.
   :type GEQ: typing.Any
   :param GRE: Keyword representing the "greater than" comparison operator.
   :type GRE: typing.Any

   :raises NotImplementedError: Raised when attempting to compare the keyword with an object of an unsupported type (i.e., not a string, pyparsing Keyword, or another FuzzyOWL2Keyword).


   .. py:method:: __eq__(value: object) -> bool

      Determines equality between the current keyword instance and a provided value by comparing their underlying names. The method supports comparison against string literals, pyparsing Keyword objects, or other FuzzyOWL2Keyword instances, performing a case-insensitive check in all cases. If the provided value is not one of these supported types, a NotImplementedError is raised.

      :param value: The object to compare against, which can be a string (case-insensitive), a `pp.Keyword`, or another `FuzzyOWL2Keyword` instance.
      :type value: object

      :raises NotImplementedError: Raised when the provided value is not a string, pp.Keyword, or FuzzyOWL2Keyword instance.

      :return: True if the keyword name matches the provided value, False otherwise. Supports comparison against strings, pp.Keyword, and FuzzyOWL2Keyword objects.

      :rtype: bool



   .. py:method:: __repr__() -> str

      Returns the official string representation of the FuzzyOWL2Keyword instance by directly returning the value of its 'name' attribute. This implementation provides a concise and readable identifier for the object, which is particularly useful for debugging and logging purposes. The method assumes that the 'name' attribute is present and holds a string value; if the attribute is missing or of an incompatible type, the behavior may deviate from the standard expectation of returning a valid string representation.

      :return: The string representation of the object, corresponding to the value of its `name` attribute.

      :rtype: str



   .. py:method:: __str__() -> str

      Returns the informal string representation of the FuzzyOWL2Keyword instance, typically used for display or logging purposes. The method simply retrieves and returns the value stored in the instance's `name` attribute. This operation is read-only and does not modify the state of the object, though it relies on the `name` attribute being present.

      :return: Returns the string representation of the object, which is its name.

      :rtype: str



   .. py:method:: get_name() -> str

      Retrieves a normalized version of the keyword's name by converting it to lowercase and stripping all single and double quotation marks. This transformation ensures that variations in casing or quoting are standardized for comparison or processing. The method performs a read-only operation on the underlying value's name attribute and returns the cleaned string without modifying the original state.

      :return: The lowercase name with all single and double quotes removed.

      :rtype: str



   .. py:method:: get_str_value() -> str

      Converts the internal value to its string representation and removes all occurrences of both single and double quotes. This process ensures the returned string is sanitized of quote characters, which is useful for serialization or embedding the value in contexts where quotes might cause parsing errors. Note that this method strips quotes from anywhere within the string, not just the boundaries, and does not modify the original value attribute.

      :return: A string representation of the internal value with all single and double quotes removed.

      :rtype: str



   .. py:method:: get_tag_name() -> str

      Returns a capitalized string representation of the keyword, formatted for use as a tag name. This method retrieves the underlying string value via `get_str_value` and applies standard capitalization, converting the first character to uppercase and the remaining characters to lowercase. The operation is stateless and does not modify the object, relying entirely on the current output of the internal string value retrieval.

      :return: The tag name as a capitalized string.

      :rtype: str



   .. py:method:: get_value() -> Union[pyparsing.CaselessKeyword, pyparsing.Word]

      Retrieves the underlying parser element associated with this keyword instance. The returned value is a `pyparsing` object, specifically either a `CaselessKeyword` or a `Word`, which defines the matching pattern for the keyword in a grammar. This method acts as a simple accessor and does not modify the internal state of the object or perform any computation beyond returning the stored attribute.

      :return: Returns the pyparsing token (either a `CaselessKeyword` or a `Word`) associated with this instance.

      :rtype: typing.Union[pp.CaselessKeyword, pp.Word]



   .. py:attribute:: A


   .. py:attribute:: AXIOM


   .. py:attribute:: B


   .. py:attribute:: BASE


   .. py:attribute:: C


   .. py:attribute:: CHOQUET


   .. py:attribute:: CLOSE_TAG


   .. py:attribute:: CONCEPT


   .. py:attribute:: CONCEPT_NAMES


   .. py:attribute:: CRISP


   .. py:attribute:: D


   .. py:attribute:: DATATYPE


   .. py:attribute:: DEGREE_DEF


   .. py:attribute:: DEGREE_VALUE


   .. py:attribute:: EQUAL


   .. py:attribute:: FUZZY_LABEL


   .. py:attribute:: FUZZY_LOGIC


   .. py:attribute:: FUZZY_OWL_2


   .. py:attribute:: FUZZY_TYPE


   .. py:attribute:: GEQ


   .. py:attribute:: GOEDEL


   .. py:attribute:: GRE


   .. py:attribute:: INDIVIDUAL


   .. py:attribute:: LEFT_SHOULDER


   .. py:attribute:: LEQ


   .. py:attribute:: LES


   .. py:attribute:: LINEAR


   .. py:attribute:: LOGIC


   .. py:attribute:: LUKASIEWICZ


   .. py:attribute:: MODIFIED


   .. py:attribute:: MODIFIER


   .. py:attribute:: NAME


   .. py:attribute:: NOMINAL


   .. py:attribute:: ONTOLOGY


   .. py:attribute:: OPEN_TAG


   .. py:attribute:: OWA


   .. py:attribute:: PRODUCT


   .. py:attribute:: QUANTIFIER


   .. py:attribute:: QUASI_SUGENO


   .. py:attribute:: Q_OWA


   .. py:attribute:: RIGHT_SHOULDER


   .. py:attribute:: ROLE


   .. py:attribute:: SINGLE_CLOSE_TAG


   .. py:attribute:: SLASH


   .. py:attribute:: SUGENO


   .. py:attribute:: TRAPEZOIDAL


   .. py:attribute:: TRIANGULAR


   .. py:attribute:: TYPE


   .. py:attribute:: WEIGHT


   .. py:attribute:: WEIGHTED


   .. py:attribute:: WEIGHTED_MAXIMUM


   .. py:attribute:: WEIGHTED_MINIMUM


   .. py:attribute:: WEIGHTED_SUM


   .. py:attribute:: WEIGHTED_SUMZERO


   .. py:attribute:: WEIGHTS


   .. py:attribute:: ZADEH

