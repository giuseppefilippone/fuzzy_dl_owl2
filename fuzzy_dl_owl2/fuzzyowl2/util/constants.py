import enum
import re
import typing

import pyparsing as pp


class ConceptType(enum.StrEnum):
    """
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
    """


    CHOQUET = enum.auto()
    FUZZY_NOMINAL = enum.auto()
    MODIFIED_CONCEPT = enum.auto()
    OWA = enum.auto()
    QUANTIFIED_OWA = enum.auto()
    QUASI_SUGENO = enum.auto()
    SUGENO = enum.auto()
    WEIGHTED_CONCEPT = enum.auto()
    WEIGHTED_MAX = enum.auto()
    WEIGHTED_MIN = enum.auto()
    WEIGHTED_SUM = enum.auto()
    WEIGHTED_SUM_ZERO = enum.auto()

    def __repr__(self) -> str:
        """
        Returns the official string representation of the ConceptType instance. This implementation returns the value of the object's 'name' attribute directly, providing a concise and human-readable identifier for the concept. The method has no side effects and relies solely on the current state of the 'name' attribute.

        :return: A string representation of the object, corresponding to its name.

        :rtype: str
        """

        return self.name

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the instance, which is primarily used for display purposes or when the object is converted to a string. This implementation specifically returns the value of the `name` attribute associated with the `ConceptType` instance, providing a concise identifier rather than a detailed structural representation.

        :return: The name of the object.

        :rtype: str
        """

        return self.name


# class FuzzyOWL2Keyword(enum.Enum):
#     OPEN_TAG = pp.Word("<")
#     CLOSE_TAG = pp.Word(">")
#     SINGLE_CLOSE_TAG = pp.Word("/>")
#     SLASH = pp.Word("/")
#     ONTOLOGY = pp.CaselessKeyword("ontology")
#     FUZZY_OWL_2 = pp.CaselessKeyword("fuzzyOwl2")
#     FUZZY_LABEL = pp.CaselessKeyword("fuzzyLabel")
#     FUZZY_TYPE = pp.CaselessKeyword("fuzzytype")
#     FUZZY_LOGIC = pp.CaselessKeyword("FuzzyLogic")
#     TYPE = pp.CaselessKeyword("type")
#     LOGIC = pp.CaselessKeyword("logic")
#     DATATYPE = pp.CaselessKeyword("datatype")
#     CONCEPT = pp.CaselessKeyword("concept")
#     ROLE = pp.CaselessKeyword("role")
#     AXIOM = pp.CaselessKeyword("axiom")
#     DEGREE_DEF = pp.CaselessKeyword("degree")
#     DEGREE_VALUE = pp.CaselessKeyword("value")
#     MODIFIED = pp.CaselessKeyword("modified")
#     WEIGHTED = pp.CaselessKeyword("weighted")
#     NOMINAL = pp.CaselessKeyword("nominal")
#     INDIVIDUAL = pp.CaselessKeyword("individual")
#     WEIGHTED_MAXIMUM = pp.CaselessKeyword("weightedMaximum")
#     WEIGHTED_MINIMUM = pp.CaselessKeyword("weightedMinimum")
#     WEIGHTED_SUM = pp.CaselessKeyword("weightedSum")
#     WEIGHTED_SUMZERO = pp.CaselessKeyword("weightedSumZero")
#     OWA = pp.CaselessKeyword("owa")
#     Q_OWA = pp.CaselessKeyword("qowa")
#     CHOQUET = pp.CaselessKeyword("choquet")
#     SUGENO = pp.CaselessKeyword("sugeno")
#     QUASI_SUGENO = pp.CaselessKeyword("quasisugeno")
#     MODIFIER = pp.CaselessKeyword("modifier")
#     BASE = pp.CaselessKeyword("base")
#     CONCEPT_NAMES = pp.CaselessKeyword("names")
#     NAME = pp.CaselessKeyword("name")
#     WEIGHT = pp.CaselessKeyword("weight")
#     WEIGHTS = pp.CaselessKeyword("weights")
#     QUANTIFIER = pp.CaselessKeyword("quantifier")
#     CRISP = pp.CaselessKeyword("crisp")
#     LEFT_SHOULDER = pp.CaselessKeyword("leftshoulder")
#     RIGHT_SHOULDER = pp.CaselessKeyword("rightshoulder")
#     TRIANGULAR = pp.CaselessKeyword("triangular")
#     TRAPEZOIDAL = pp.CaselessKeyword("trapezoidal")
#     LINEAR = pp.CaselessKeyword("linear")
#     A = pp.CaselessKeyword("a")
#     B = pp.CaselessKeyword("b")
#     C = pp.CaselessKeyword("c")
#     D = pp.CaselessKeyword("d")
#     LUKASIEWICZ = pp.CaselessKeyword("lukasiewicz")
#     GOEDEL = pp.CaselessKeyword("goedel")
#     ZADEH = pp.CaselessKeyword("zadeh")
#     PRODUCT = pp.CaselessKeyword("product")
#     EQUAL = pp.Word("=")
#     LES = pp.CaselessKeyword("les")
#     LEQ = pp.CaselessKeyword("leq")
#     GEQ = pp.CaselessKeyword("geq")
#     GRE = pp.CaselessKeyword("gre")

#     def get_name(self) -> str:
#         return re.sub(r"[\"\']+", "", self.value.name.lower())

#     def get_value(self) -> typing.Union[pp.CaselessKeyword, pp.Word]:
#         return self.value

#     def get_str_value(self) -> str:
#         return str(self.value).replace('"', "").replace("'", "")

#     def get_tag_name(self) -> str:
#         return self.get_str_value().capitalize()

#     def __eq__(self, value: object) -> bool:
#         if isinstance(value, str):
#             return self.get_name() == value.lower()
#         elif isinstance(value, pp.CaselessKeyword):
#             return self.get_name() == value.name.lower()
#         elif isinstance(value, FuzzyOWL2Keyword):
#             return self.get_name() == value.get_name()
#         raise NotImplementedError

#     def __repr__(self) -> str:
#         return self.name

#     def __str__(self) -> str:
#         return self.name


class FuzzyOWL2Keyword(enum.Enum):
    """
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
    """


    OPEN_TAG = pp.Word("<")
    CLOSE_TAG = pp.Word(">")
    SINGLE_CLOSE_TAG = pp.Word("/>")
    SLASH = pp.Word("/")
    ONTOLOGY = pp.Keyword("ontology")
    FUZZY_OWL_2 = pp.Keyword("fuzzyOwl2")
    FUZZY_LABEL = pp.Keyword("fuzzyLabel")
    FUZZY_TYPE = pp.Keyword("fuzzyType")
    FUZZY_LOGIC = pp.Keyword("FuzzyLogic")
    TYPE = pp.Keyword("type")
    LOGIC = pp.Keyword("logic")
    DATATYPE = pp.Keyword("datatype")
    CONCEPT = pp.Keyword("concept")
    ROLE = pp.Keyword("role")
    AXIOM = pp.Keyword("axiom")
    DEGREE_DEF = pp.Keyword("degree")
    DEGREE_VALUE = pp.Keyword("value")
    MODIFIED = pp.Keyword("modified")
    WEIGHTED = pp.Keyword("weighted")
    NOMINAL = pp.Keyword("nominal")
    INDIVIDUAL = pp.Keyword("individual")
    WEIGHTED_MAXIMUM = pp.Keyword("weightedMaximum")
    WEIGHTED_MINIMUM = pp.Keyword("weightedMinimum")
    WEIGHTED_SUM = pp.Keyword("weightedSum")
    WEIGHTED_SUMZERO = pp.Keyword("weightedSumZero")
    OWA = pp.Keyword("owa")
    Q_OWA = pp.Keyword("qowa")
    CHOQUET = pp.Keyword("choquet")
    SUGENO = pp.Keyword("sugeno")
    QUASI_SUGENO = pp.Keyword("quasisugeno")
    MODIFIER = pp.Keyword("modifier")
    BASE = pp.Keyword("base")
    CONCEPT_NAMES = pp.Keyword("names")
    NAME = pp.Keyword("name")
    WEIGHT = pp.Keyword("weight")
    WEIGHTS = pp.Keyword("weights")
    QUANTIFIER = pp.Keyword("quantifier")
    CRISP = pp.Keyword("crisp")
    LEFT_SHOULDER = pp.Keyword("leftshoulder")
    RIGHT_SHOULDER = pp.Keyword("rightshoulder")
    TRIANGULAR = pp.Keyword("triangular")
    TRAPEZOIDAL = pp.Keyword("trapezoidal")
    LINEAR = pp.Keyword("linear")
    A = pp.Keyword("a")
    B = pp.Keyword("b")
    C = pp.Keyword("c")
    D = pp.Keyword("d")
    LUKASIEWICZ = pp.Keyword("lukasiewicz")
    GOEDEL = pp.Keyword("goedel")
    ZADEH = pp.Keyword("zadeh")
    PRODUCT = pp.Keyword("product")
    EQUAL = pp.Word("=")
    LES = pp.Keyword("les")
    LEQ = pp.Keyword("leq")
    GEQ = pp.Keyword("geq")
    GRE = pp.Keyword("gre")

    def get_name(self) -> str:
        """
        Retrieves a normalized version of the keyword's name by converting it to lowercase and stripping all single and double quotation marks. This transformation ensures that variations in casing or quoting are standardized for comparison or processing. The method performs a read-only operation on the underlying value's name attribute and returns the cleaned string without modifying the original state.

        :return: The lowercase name with all single and double quotes removed.

        :rtype: str
        """

        return re.sub(r"[\"\']+", "", self.value.name.lower())

    def get_value(self) -> typing.Union[pp.CaselessKeyword, pp.Word]:
        """
        Retrieves the underlying parser element associated with this keyword instance. The returned value is a `pyparsing` object, specifically either a `CaselessKeyword` or a `Word`, which defines the matching pattern for the keyword in a grammar. This method acts as a simple accessor and does not modify the internal state of the object or perform any computation beyond returning the stored attribute.

        :return: Returns the pyparsing token (either a `CaselessKeyword` or a `Word`) associated with this instance.

        :rtype: typing.Union[pp.CaselessKeyword, pp.Word]
        """

        return self.value

    def get_str_value(self) -> str:
        """
        Converts the internal value to its string representation and removes all occurrences of both single and double quotes. This process ensures the returned string is sanitized of quote characters, which is useful for serialization or embedding the value in contexts where quotes might cause parsing errors. Note that this method strips quotes from anywhere within the string, not just the boundaries, and does not modify the original value attribute.

        :return: A string representation of the internal value with all single and double quotes removed.

        :rtype: str
        """

        return str(self.value).replace('"', "").replace("'", "")

    def get_tag_name(self) -> str:
        """
        Returns a capitalized string representation of the keyword, formatted for use as a tag name. This method retrieves the underlying string value via `get_str_value` and applies standard capitalization, converting the first character to uppercase and the remaining characters to lowercase. The operation is stateless and does not modify the object, relying entirely on the current output of the internal string value retrieval.

        :return: The tag name as a capitalized string.

        :rtype: str
        """

        return self.get_str_value().capitalize()

    def __eq__(self, value: object) -> bool:
        """
        Determines equality between the current keyword instance and a provided value by comparing their underlying names. The method supports comparison against string literals, pyparsing Keyword objects, or other FuzzyOWL2Keyword instances, performing a case-insensitive check in all cases. If the provided value is not one of these supported types, a NotImplementedError is raised.

        :param value: The object to compare against, which can be a string (case-insensitive), a `pp.Keyword`, or another `FuzzyOWL2Keyword` instance.
        :type value: object

        :raises NotImplementedError: Raised when the provided value is not a string, pp.Keyword, or FuzzyOWL2Keyword instance.

        :return: True if the keyword name matches the provided value, False otherwise. Supports comparison against strings, pp.Keyword, and FuzzyOWL2Keyword objects.

        :rtype: bool
        """

        if isinstance(value, str):
            return self.get_name() == value.lower()
        elif isinstance(value, pp.Keyword):
            return self.get_name() == value.name.lower()
        elif isinstance(value, FuzzyOWL2Keyword):
            return self.get_name() == value.get_name()
        raise NotImplementedError

    def __repr__(self) -> str:
        """
        Returns the official string representation of the FuzzyOWL2Keyword instance by directly returning the value of its 'name' attribute. This implementation provides a concise and readable identifier for the object, which is particularly useful for debugging and logging purposes. The method assumes that the 'name' attribute is present and holds a string value; if the attribute is missing or of an incompatible type, the behavior may deviate from the standard expectation of returning a valid string representation.

        :return: The string representation of the object, corresponding to the value of its `name` attribute.

        :rtype: str
        """

        return self.name

    def __str__(self) -> str:
        """
        Returns the informal string representation of the FuzzyOWL2Keyword instance, typically used for display or logging purposes. The method simply retrieves and returns the value stored in the instance's `name` attribute. This operation is read-only and does not modify the state of the object, though it relies on the `name` attribute being present.

        :return: Returns the string representation of the object, which is its name.

        :rtype: str
        """

        return self.name
