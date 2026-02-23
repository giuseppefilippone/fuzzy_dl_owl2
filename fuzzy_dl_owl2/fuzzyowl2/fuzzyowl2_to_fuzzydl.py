import os
import re
import string
import typing

from fuzzy_dl_owl2.fuzzydl.util.constants import FuzzyDLKeyword
from fuzzy_dl_owl2.fuzzydl.util.util import Util
from fuzzy_dl_owl2.fuzzyowl2.fuzzyowl2 import FuzzyOwl2
from fuzzy_dl_owl2.fuzzyowl2.owl_types.choquet_concept import ChoquetConcept
from fuzzy_dl_owl2.fuzzyowl2.owl_types.crisp_function import CrispFunction
from fuzzy_dl_owl2.fuzzyowl2.owl_types.fuzzy_nominal_concept import \
    FuzzyNominalConcept
from fuzzy_dl_owl2.fuzzyowl2.owl_types.left_shoulder_function import \
    LeftShoulderFunction
from fuzzy_dl_owl2.fuzzyowl2.owl_types.linear_function import LinearFunction
from fuzzy_dl_owl2.fuzzyowl2.owl_types.linear_modifier import LinearModifier
from fuzzy_dl_owl2.fuzzyowl2.owl_types.modified_concept import ModifiedConcept
from fuzzy_dl_owl2.fuzzyowl2.owl_types.modified_function import \
    ModifiedFunction
from fuzzy_dl_owl2.fuzzyowl2.owl_types.modified_property import \
    ModifiedProperty
from fuzzy_dl_owl2.fuzzyowl2.owl_types.owa_concept import OwaConcept
from fuzzy_dl_owl2.fuzzyowl2.owl_types.qowa_concept import QowaConcept
from fuzzy_dl_owl2.fuzzyowl2.owl_types.quasi_sugeno_concept import \
    QsugenoConcept
from fuzzy_dl_owl2.fuzzyowl2.owl_types.right_shoulder_function import \
    RightShoulderFunction
from fuzzy_dl_owl2.fuzzyowl2.owl_types.sugeno_concept import SugenoConcept
from fuzzy_dl_owl2.fuzzyowl2.owl_types.trapezoidal_function import \
    TrapezoidalFunction
from fuzzy_dl_owl2.fuzzyowl2.owl_types.triangular_function import \
    TriangularFunction
from fuzzy_dl_owl2.fuzzyowl2.owl_types.triangular_modifer import \
    TriangularModifier
from fuzzy_dl_owl2.fuzzyowl2.owl_types.weighted_concept import WeightedConcept
from fuzzy_dl_owl2.fuzzyowl2.owl_types.weighted_max_concept import \
    WeightedMaxConcept
from fuzzy_dl_owl2.fuzzyowl2.owl_types.weighted_min_concept import \
    WeightedMinConcept
from fuzzy_dl_owl2.fuzzyowl2.owl_types.weighted_sum_concept import \
    WeightedSumConcept
from fuzzy_dl_owl2.fuzzyowl2.owl_types.weighted_sum_zero_concept import \
    WeightedSumZeroConcept
from pyowl2.abstracts.class_expression import OWLClassExpression
from pyowl2.abstracts.data_property_expression import OWLDataPropertyExpression
from pyowl2.abstracts.data_range import OWLDataRange
from pyowl2.abstracts.entity import OWLEntity
from pyowl2.abstracts.individual import OWLIndividual
from pyowl2.abstracts.object_property_expression import \
    OWLObjectPropertyExpression
from pyowl2.base.datatype import OWLDatatype
from pyowl2.base.owl_class import OWLClass
from pyowl2.data_range.data_intersection_of import OWLDataIntersectionOf
from pyowl2.data_range.data_one_of import OWLDataOneOf
from pyowl2.data_range.datatype_restriction import (OWLDatatypeRestriction,
                                                    OWLFacet)
from pyowl2.expressions.data_property import OWLDataProperty
from pyowl2.expressions.object_property import OWLObjectProperty
from pyowl2.individual.anonymous_individual import OWLAnonymousIndividual
from pyowl2.literal.literal import OWLLiteral


# @utils.timer_decorator
class FuzzyOwl2ToFuzzyDL(FuzzyOwl2):
    """
    This class serves as a converter that transforms ontologies defined in the FuzzyOWL2 format into the specific syntax required by the FuzzyDL reasoner. Extending the base `FuzzyOwl2` class, it traverses the ontology structure and translates OWL entities—such as classes, object properties, data properties, and individuals—into their corresponding FuzzyDL constructs like concepts, roles, and instances. The converter handles a wide range of semantic elements, including class expressions (intersections, unions, complements), property characteristics (transitivity, symmetry, functionality), and complex fuzzy logic operators such as weighted sums, OWA, and Choquet integrals. It also manages the definition of datatypes, automatically setting appropriate ranges for numerical values and handling string or boolean types. During the conversion process, the class writes the resulting syntax to a specified output file while maintaining internal sets to track declared entities and prevent redundancy. Additionally, it includes error handling to identify and report unsupported constructs, such as cardinality restrictions or specific property axioms, ensuring the user is aware of translation limitations.

    :param EPSILON: A small constant used to adjust boundary values for exclusive data range restrictions, specifically for non-integer datatypes.
    :type EPSILON: float
    :param INTEGER_MAX_VALUE: The maximum value used to define the range of integer datatypes in the FuzzyDL representation.
    :type INTEGER_MAX_VALUE: int
    :param INTEGER_MIN_VALUE: The minimum value for integer datatypes, used as the lower bound for defining ranges and facets in the FuzzyDL representation.
    :type INTEGER_MIN_VALUE: int
    :param DOUBLE_MAX_VALUE: The upper bound for real number ranges used when defining data properties in the FuzzyDL output, specifically for double and float datatypes.
    :type DOUBLE_MAX_VALUE: float
    :param DOUBLE_MIN_VALUE: The minimum value for double (real) datatypes, used to define the lower bound of ranges for data properties in the FuzzyDL representation.
    :type DOUBLE_MIN_VALUE: float
    :param boolean_datatypes: Tracks data properties identified as having a boolean datatype to prevent duplicate range definitions in the FuzzyDL output.
    :type boolean_datatypes: set[str]
    :param numerical_datatypes: Tracks data properties identified as having numerical types (integer or real) to ensure their range definitions are written to the FuzzyDL output.
    :type numerical_datatypes: set[str]
    :param string_datatypes: A set of data property names identified as having a string, date, or URI range, used to track their declaration in the FuzzyDL output.
    :type string_datatypes: set[str]
    :param data_properties: Tracks the names of data properties encountered during the conversion process to disambiguate them from object properties with identical names.
    :type data_properties: set[str]
    :param object_properties: A set tracking the names of object properties encountered during the conversion process to distinguish them from data properties and ensure correct representation in the FuzzyDL output.
    :type object_properties: set[str]
    :param processed_functional_data_properties: A set of names for data properties that have already been declared as functional in the FuzzyDL output to prevent duplicate definitions.
    :type processed_functional_data_properties: set[str]
    :param processed_functional_object_properties: Tracks object properties that have already been written as functional to avoid duplicate definitions in the output.
    :type processed_functional_object_properties: set[str]
    """

    EPSILON: float = 0.001

    INTEGER_MAX_VALUE: int = 100000000  # 0x7FFFFFFF
    INTEGER_MIN_VALUE: int = -INTEGER_MAX_VALUE
    DOUBLE_MAX_VALUE: float = 1000 * float(INTEGER_MAX_VALUE)
    DOUBLE_MIN_VALUE: float = -DOUBLE_MAX_VALUE

    def __init__(
        self,
        input_file: str,
        output_file: str,
        base_iri: str = "http://www.semanticweb.org/ontologies/fuzzydl_ontology#",
    ) -> None:
        """
        Initializes the converter by setting up the input and output file paths and an optional base IRI, invoking the parent class constructor to handle core configuration. To ensure a clean conversion environment, the method removes any existing file at the specified output path. It also prepares internal data structures, specifically sets to track boolean, numerical, and string datatypes, as well as data and object properties, which will be populated during the translation from FuzzyOWL2 to FuzzyDL.

        :param input_file: Path to the input OWL file containing the FuzzyOWL2 ontology.
        :type input_file: str
        :param output_file: Path to the file where the FuzzyDL representation will be written. If the file already exists, it will be removed upon initialization.
        :type output_file: str
        :param base_iri: The base Internationalized Resource Identifier (IRI) used as the namespace for the ontology.
        :type base_iri: str
        """

        super().__init__(input_file, output_file, base_iri)

        if os.path.exists(self.output_dl):
            os.remove(self.output_dl)

        self.boolean_datatypes: set[str] = set()
        self.numerical_datatypes: set[str] = set()
        self.string_datatypes: set[str] = set()
        self.data_properties: set[str] = set()
        self.object_properties: set[str] = set()
        self.processed_functional_data_properties: set[str] = set()
        self.processed_functional_object_properties: set[str] = set()

    @staticmethod
    def is_reserved_word(s: str) -> bool:
        """
        This static method determines whether a given string is a reserved keyword or a numeric literal within the FuzzyDL language syntax. It returns True if the string matches specific FuzzyDL keywords, such as 'linear', 'triangular', or 'disjoint', or if the string can be successfully parsed as a floating-point number. This validation is used to prevent naming conflicts during the translation process, ensuring that identifiers do not clash with language primitives or numeric values.

        :param s: The string to check against FuzzyDL keywords and numeric values.
        :type s: str

        :return: True if the string is a FuzzyDL keyword or a numeric value, False otherwise.

        :rtype: bool
        """

        if s in (
            FuzzyDLKeyword.LINEAR,
            FuzzyDLKeyword.TRIANGULAR,
            FuzzyDLKeyword.CRISP,
            FuzzyDLKeyword.TRAPEZOIDAL,
            FuzzyDLKeyword.CLASSICAL,
            FuzzyDLKeyword.DISJOINT,
            FuzzyDLKeyword.DISJOINT,
            FuzzyDLKeyword.INSTANCE,
            FuzzyDLKeyword.RELATED,
            FuzzyDLKeyword.DOMAIN,
            FuzzyDLKeyword.RANGE,
        ):
            return True
        # avoid numbers
        try:
            _ = float(s)
            return True
        except:
            return False

    def __write(self, line: str) -> None:
        """
        This private helper method appends a specific line of text to the FuzzyDL output file associated with the current conversion process. It accepts a string argument, automatically appends a newline character, and writes the result to the file path specified by `self.output_dl` in append mode. This allows the converter to construct the output file incrementally while also logging the written content to the debug stream for traceability.

        :param line: The string content to be appended to the FuzzyDL output file.
        :type line: str
        """

        Util.debug(f"Writing line to FuzzyDL file: {line}")
        with open(self.output_dl, "a") as file:
            file.write(f"{line}\n")

    def get_short_name(self, s: typing.Union[OWLEntity, str]) -> str:
        """
        Extracts a simplified identifier from an OWL entity or a raw string, ensuring compatibility with the target syntax. If the input is an OWL entity, the method isolates the local name by splitting the entity's IRI on the hash symbol and taking the trailing segment. The resulting string is then sanitized by removing specific escaped parenthesis characters. To prevent syntax errors caused by language keywords, the method checks if the processed name is a reserved word and prefixes it with an underscore if necessary.

        :param s: The OWL entity or string to be converted into a short name.
        :type s: typing.Union[OWLEntity, str]

        :return: The short name of the input, extracted as the IRI fragment for OWL entities. The result has specific escape characters removed and is prefixed with an underscore if it is a reserved word.

        :rtype: str
        """

        if isinstance(s, OWLEntity):
            # s = str(self.pm.getShortForm(s))
            s = str(s.iri).split("#")[-1]
        s = s.replace(r"\\(", "")
        s = s.replace(r"\\)", "")
        if FuzzyOwl2ToFuzzyDL.is_reserved_word(s):
            return f"_{s}"
        else:
            return s

    def __get_facets(self, name: str) -> list[float]:
        """
        Retrieves the lower and upper bound constraints for a specified XML Schema datatype string, returning them as a list of two floating-point numbers. The method defaults to the maximum integer range defined by the class constants but adjusts these limits to match the semantic restrictions of specific subtypes, such as non-positive or positive integers. If the provided datatype name does not match one of the handled subtypes, the default integer range is returned.

        :param name: The qualified name of the XML Schema datatype (e.g., 'xsd:nonPositiveInteger').
        :type name: str

        :return: A list containing the minimum and maximum numeric bounds for the specified XML Schema datatype.

        :rtype: list[float]
        """

        facets: list[float] = [
            FuzzyOwl2ToFuzzyDL.INTEGER_MIN_VALUE,
            FuzzyOwl2ToFuzzyDL.INTEGER_MAX_VALUE,
        ]
        if name == "xsd:nonPositiveInteger":
            facets[1] = 0
        elif name == "xsd:NegativeInteger":
            facets[1] = -1
        elif name == "xsd:nonNegativeInteger":
            facets[0] = 0
        elif name == "xsd:positiveInteger":
            facets[0] = 1
        return facets

    def __is_real_datatype(self, d: typing.Union[OWLDatatype, OWLLiteral]) -> bool:
        """
        Determines whether the provided OWL datatype or literal corresponds to a real-valued numeric type. The method evaluates the input against a set of criteria, returning true if the type is identified as a double, float, real, rational, or decimal. This check is used internally to distinguish real numbers from other data types during the conversion process, and it does not modify the state of the input object.

        :param d: The OWL datatype or literal to verify if it represents a real number.
        :type d: typing.Union[OWLDatatype, OWLLiteral]

        :return: True if the input represents a real number datatype (including float, double, decimal, rational, or real), False otherwise.

        :rtype: bool
        """

        if d.is_double() or d.is_float():
            return True
        return d.is_real() or d.is_rational() or d.is_decimal()

    def __is_integer_datatype(self, d: typing.Union[OWLDatatype, OWLLiteral]) -> bool:
        """
        Determines whether the provided OWL datatype or literal represents an integer value. This method delegates the check to the `is_integer()` method of the input object, returning `True` if the object is an integer type and `False` otherwise. It is used internally to distinguish integer data types during the translation process from OWL2 to FuzzyDL, ensuring that specific formatting or mapping rules are applied to integer values. The method does not modify the input object and has no side effects.

        :param d: The OWL datatype or literal to check.
        :type d: typing.Union[OWLDatatype, OWLLiteral]

        :return: True if the provided datatype or literal is an integer type, False otherwise.

        :rtype: bool
        """

        return d.is_integer()

    def get_individual_name(self, i: OWLIndividual) -> str:
        """
        Retrieves a string representation of the identifier for a given OWL individual, handling both named and anonymous entities. If the individual is anonymous, the method returns the string value of its internal node ID. For named individuals, it delegates to the `get_short_name` method to obtain the appropriate identifier.

        :param i: The OWL individual for which to retrieve the name.
        :type i: OWLIndividual

        :return: A string representing the individual's name, specifically the node ID for anonymous individuals or the short name for named individuals.

        :rtype: str
        """

        if isinstance(i, OWLAnonymousIndividual):
            return str(i.node_id)
        else:
            return self.get_short_name(i)

    def get_top_concept_name(self) -> str:
        """
        Retrieves the specific string identifier used to represent the top concept (the universal concept) within the FuzzyDL syntax. This method returns a hardcoded string literal, "*top*", which serves as the symbol for the universal set during the translation process. It has no side effects and does not depend on the internal state of the object.

        :return: The string '*top*', representing the name of the top concept.

        :rtype: str
        """

        return "*top*"

    def get_bottom_concept_name(self) -> str:
        """
        Retrieves the specific string identifier used to represent the bottom concept (the logical equivalent of the empty set) in the target FuzzyDL syntax. This method returns a constant value, specifically '*bottom*', ensuring consistent representation when translating OWL constructs that denote inconsistency or the absence of instances. The function has no side effects and does not depend on the internal state of the converter instance.

        :return: The string name representing the bottom concept.

        :rtype: str
        """

        return "*bottom*"

    def get_atomic_concept_name(self, c: OWLClass) -> str:
        """
        Retrieves the specific string identifier used to represent an atomic concept within the FuzzyDL translation context. This method accepts an OWLClass object and delegates to the internal `get_short_name` utility to derive the appropriate name, ensuring that the identifier conforms to the naming conventions required by the target system. It serves as a bridge between the OWL ontology structure and the string-based representation needed for FuzzyDL processing.

        :param c: The atomic concept for which to retrieve the name.
        :type c: OWLClass

        :return: The short name of the specified OWL class.

        :rtype: str
        """

        return self.get_short_name(c)

    def get_object_intersection_of_name(self, operands: set[OWLClassExpression]) -> str:
        """
        Generates the string representation for an object intersection class expression compatible with FuzzyDL syntax. It accepts a set of OWL class expressions as operands and formats them into a conjunction string. If the input set contains exactly one operand, the method returns the name of that class directly without wrapping it in an intersection clause; otherwise, it joins the class names within an "(and ...)" structure. Note that in the single-operand case, the method modifies the input set by removing the element.

        :param operands: The set of OWL class expressions comprising the intersection.
        :type operands: set[OWLClassExpression]

        :return: The string representation of the object intersection, formatted as a logical conjunction "(and ...)" for multiple operands or the single class name if only one operand is provided.

        :rtype: str
        """

        if len(operands) == 1:
            return self.get_class_name(operands.pop())
        return f"(and {' '.join([self.get_class_name(c) for     c in operands])})"

    def get_object_union_of_name(self, operands: set[OWLClassExpression]) -> str:
        """
        Generates the FuzzyDL string representation for the logical union (disjunction) of the provided OWL class expressions. This method formats the operands according to FuzzyDL syntax, wrapping multiple operands in a parenthesized expression joined by the 'or' keyword. If the input set contains only a single operand, the method simplifies the output by returning the name of that class directly rather than wrapping it in a union expression.

        :param operands: The set of OWL class expressions comprising the object union.
        :type operands: set[OWLClassExpression]

        :return: The string representation of the object union. Returns the class name if there is a single operand, or a parenthesized logical disjunction of the operand names otherwise.

        :rtype: str
        """

        if len(operands) == 1:
            return self.get_class_name(operands.pop())
        return f"(or {' '.join([self.get_class_name(c) for     c in operands])})"

    def get_object_some_values_from_name(
        self, p: OWLObjectPropertyExpression, c: OWLClassExpression
    ) -> str:
        """
        Constructs a string representation of an existential restriction (ObjectSomeValuesFrom) formatted for the target FuzzyDL syntax. This method takes an object property expression and a class expression, converts them into their respective string names using internal helper methods, and combines them into a parenthesized expression following the pattern "(some P C)". It serves as a utility within the translation pipeline to ensure that complex class expressions are correctly serialized into the destination language format.

        :param p: The object property expression representing the relationship in the 'some values from' restriction.
        :type p: OWLObjectPropertyExpression
        :param c: The class expression serving as the filler for the restriction.
        :type c: OWLClassExpression

        :return: A string representing the ObjectSomeValuesFrom restriction, formatted as "(some <property_name> <class_name>)".

        :rtype: str
        """

        return f"(some {self.get_object_property_name(p)} {self.get_class_name(c)})"

    def get_object_all_values_from_name(
        self, p: OWLObjectPropertyExpression, c: OWLClassExpression
    ) -> str:
        """
        Generates the string representation for a universal object property restriction (ObjectAllValuesFrom) in the target syntax. It takes an object property expression and a class expression, retrieves their respective names using internal helper methods, and formats them into the structure `(all <property_name> <class_name>)`. This function is primarily used to translate OWL class restrictions into the specific format required by the FuzzyDL engine.

        :param p: The object property expression defining the relationship for the universal restriction.
        :type p: OWLObjectPropertyExpression
        :param c: The class expression defining the range of the universal restriction.
        :type c: OWLClassExpression

        :return: Returns the string representation of the ObjectAllValuesFrom restriction, formatted as '(all <property> <class>)'.

        :rtype: str
        """

        return f"(all {self.get_object_property_name(p)} {self.get_class_name(c)})"

    def get_data_some_values_from_name(
        self, p: OWLDataPropertyExpression, range: OWLDataRange
    ) -> str:
        """
        Generates the FuzzyDL syntax for an existential data restriction involving a specific property and range, adapting the translation strategy based on the type of the data range. For fuzzy datatypes, it constructs a standard existential restriction string. When handling numerical types (real or integer), the method ensures the property is registered as a numerical datatype, potentially writing a range definition to the output as a side effect if this is the first encounter with the property, and returns a lower-bound constraint. Boolean and enumerated ranges are translated into equality constraints. If the provided range type is not supported by the converter, an error is raised.

        :param p: The data property expression involved in the restriction.
        :type p: OWLDataPropertyExpression
        :param range: The data range (such as a datatype or an enumeration of literals) that the data property must take values from in the restriction.
        :type range: OWLDataRange

        :return: A string representation of the data restriction, formatted as a constraint expression (e.g., existential, inequality, or equality) based on the provided data property and range.

        :rtype: str
        """

        if isinstance(range, OWLDatatype):
            datatype_name: str = self.get_short_name(range)
            if datatype_name in self.fuzzy_datatypes:
                return f"(some {self.get_data_property_name(p)} {datatype_name})"
            else:
                d: OWLDatatype = range
                dp_name: str = self.get_data_property_name(p)
                if self.__is_real_datatype(d) or self.__is_integer_datatype(d):
                    if dp_name not in self.numerical_datatypes:
                        self.numerical_datatypes.add(dp_name)
                        if self.__is_real_datatype(d):
                            self.__write(
                                f"(range {dp_name} *real* {FuzzyOwl2ToFuzzyDL.DOUBLE_MIN_VALUE} {FuzzyOwl2ToFuzzyDL.DOUBLE_MAX_VALUE})"
                            )
                        else:
                            facets: list[float] = self.__get_facets(str(d))
                            self.__write(
                                f"(range {dp_name} *integer* {facets[0]} {facets[1]})"
                            )
                    if self.__is_real_datatype(d):
                        return f"(>= {dp_name} {FuzzyOwl2ToFuzzyDL.DOUBLE_MIN_VALUE})"
                    else:
                        return f"(>= {dp_name} {FuzzyOwl2ToFuzzyDL.INTEGER_MIN_VALUE})"
                elif d.is_boolean():
                    return f"(= {self.get_data_property_name(p)} {d})"
        elif isinstance(range, OWLDataOneOf):
            o: OWLDataOneOf = typing.cast(OWLDataOneOf, range)
            literat_set: list[OWLLiteral] = o.literals
            if len(literat_set) > 0:
                return f"(= {self.get_data_property_name(p)} {literat_set})"
        Util.error(
            f"Data some values restriction with range {range} and type {type(range)} not supported -- DataSomeValuesFrom({p} {range})"
        )
        return None

    def get_data_all_values_from_name(
        self, p: OWLDataPropertyExpression, range: OWLDataRange
    ) -> str:
        """
        Constructs the string representation for a universal data restriction (DataAllValuesFrom) in the FuzzyDL syntax, using the specified data property and data range. This method specifically supports restrictions where the range is a recognized fuzzy datatype; it retrieves the short name of the datatype and formats it alongside the property name. If the range is not a standard OWL datatype or is not included in the set of supported fuzzy datatypes, the method logs an error via the utility function and returns None.

        :param p: The data property expression whose values are restricted to the specified data range.
        :type p: OWLDataPropertyExpression
        :param range: The data range or datatype that the property values are restricted to.
        :type range: OWLDataRange

        :return: A string representation of the data all values from restriction in the format "(all <property> <datatype>)" if the range is a supported fuzzy datatype, otherwise None.

        :rtype: str
        """

        if isinstance(range, OWLDatatype):
            datatype_name: str = self.get_short_name(range)
            if datatype_name in self.fuzzy_datatypes:
                return f"(all {self.get_data_property_name(p)} {datatype_name})"
        Util.error(
            f"Data all values restriction with range {range} and type {type(range)} not supported -- DataAllValuesFrom({p} {range})"
        )
        return None

    def get_object_complement_of_name(self, c: OWLClassExpression) -> str:
        """
        This method constructs the string representation of an object complement (negation) for a given OWL class expression, formatted according to the target syntax of the conversion process. It retrieves the name of the input class expression by delegating to the `get_class_name` method and wraps the result in parentheses with the "not" keyword. The function does not modify the input object and relies entirely on the `get_class_name` method to correctly resolve the identifier for the provided class expression.

        :param c: The class expression to be complemented.
        :type c: OWLClassExpression

        :return: A string representing the object complement of the class expression, formatted as '(not [class_name])'.

        :rtype: str
        """

        return f"(not {self.get_class_name(c)})"

    def get_object_has_self_name(self, p: OWLObjectPropertyExpression) -> str:
        """
        Generates the FuzzyDL syntax representation for an object property "has self" restriction, translating an OWL object property expression into the target format. It constructs the string by wrapping the resolved property name within a `(self ...)` construct, which is the specific syntax used by FuzzyDL to denote that an individual is related to itself via the given property. The method delegates the extraction of the property's identifier to `get_object_property_name`, ensuring that complex property expressions are handled correctly before formatting.

        :param p: The object property expression used to define the self-restriction.
        :type p: OWLObjectPropertyExpression

        :return: A string representation of the ObjectHasSelf restriction for the given property, formatted as "(self <property_name>)".

        :rtype: str
        """

        return f"(self {self.get_object_property_name(p)})"

    def __get_set_name(self, curr_set: set) -> str:
        """
        Converts a Python set into a formatted string representation by removing delimiters and standardizing separators. This method takes a set, converts it to its string representation, and strips out bracket characters while replacing comma-space separators with single spaces. The resulting string is a space-delimited sequence of elements intended for use within the FuzzyDL translation logic.

        :param curr_set: The set to generate a name from.
        :type curr_set: set

        :return: A formatted string representing the set's contents, with escaped brackets removed and elements separated by spaces.

        :rtype: str
        """

        return str(curr_set).replace("\\[", "").replace("\\]", "").replace(", ", " ")

    def get_object_one_of_name(self, ind_set: set[OWLIndividual]) -> str:
        """
        This method is intended to retrieve or generate a name for an ObjectOneOf class expression based on a set of OWL individuals. However, the implementation explicitly indicates that ObjectOneOf concepts are not supported by the converter. As a result, the method triggers an error reporting utility with the details of the input set and returns None, effectively flagging the translation process for this specific construct as unsupported.

        :param ind_set: The set of individuals comprising the ObjectOneOf enumeration.
        :type ind_set: set[OWLIndividual]

        :return: None, indicating that the ObjectOneOf concept is not supported.

        :rtype: str
        """

        Util.error(
            f"OneOf concept not supported -- (OneOf {self.__get_set_name(ind_set)})"
        )
        return None

    def get_object_has_value_name(
        self, p: OWLObjectPropertyExpression, i: OWLIndividual
    ) -> str:
        """
        Generates the FuzzyDL string representation for an object property existential restriction involving a specific individual. It constructs the expression using the 'b-some' keyword, which denotes a bounded existential quantification, by combining the resolved names of the provided object property and individual. This method delegates the actual name resolution to internal helper methods and assumes that the inputs are valid OWL entities that can be successfully translated.

        :param p: The object property expression used to construct the object has value restriction name.
        :type p: OWLObjectPropertyExpression
        :param i: The individual that serves as the value for the object property expression.
        :type i: OWLIndividual

        :return: A string representing the ObjectHasValue restriction for the given property and individual, formatted as "(b-some property_name individual_name)".

        :rtype: str
        """

        return (
            f"(b-some {self.get_object_property_name(p)} {self.get_individual_name(i)})"
        )

    def get_data_has_value_name(
        self, p: OWLDataPropertyExpression, literal: OWLLiteral
    ) -> str:
        """
        Generates the string representation for a data property value restriction in the target syntax, formatted as an equality expression. This method manages the side effect of defining the property's datatype range and functionality within the output, ensuring these definitions are written only once per property by tracking them in internal sets. It supports integer, real, and boolean literals, deriving specific range constraints for numerical types based on facets or predefined bounds. If the provided literal type is not supported, the method logs an error and returns None.

        :param p: The data property expression involved in the restriction.
        :type p: OWLDataPropertyExpression
        :param literal: The specific literal value (integer, real, or boolean) that the data property is restricted to equal.
        :type literal: OWLLiteral

        :return: A string representation of the data has value restriction, formatted as an equality between the data property name and the literal value.

        :rtype: str
        """

        dp_name: str = self.get_data_property_name(p)
        if self.__is_integer_datatype(literal) or self.__is_real_datatype(literal):
            if dp_name not in self.numerical_datatypes:
                self.numerical_datatypes.add(dp_name)
                self.write_functional_data_property_axiom(p)
                if self.__is_real_datatype(literal):
                    self.__write(
                        f"(range {dp_name} *real* {FuzzyOwl2ToFuzzyDL.DOUBLE_MIN_VALUE} {FuzzyOwl2ToFuzzyDL.DOUBLE_MAX_VALUE})"
                    )
                else:
                    facets: list[float] = self.__get_facets(str(literal))
                    self.__write(f"(range {dp_name} *integer* {facets[0]} {facets[1]})")
            return f"(= {dp_name} {literal})"
        elif literal.is_boolean():
            if dp_name not in self.boolean_datatypes:
                self.boolean_datatypes.add(dp_name)
                self.write_functional_data_property_axiom(p)
                self.__write(f"(range {dp_name} *boolean*)")
            return f"(= {dp_name} {literal})"
        else:
            Util.error(
                f"Data hasValue restriction with literal {literal} not supported -- DataHasValue({p} {literal})"
            )
            return None

    def get_object_min_cardinality_restriction(
        self,
        cardinality: int,
        p: OWLObjectPropertyExpression,
        c: OWLClassExpression = None,
    ) -> str:
        """
        This method is intended to retrieve the string representation of an object minimum cardinality restriction for translation into FuzzyDL syntax, but the feature is currently unsupported by the implementation. Regardless of the provided cardinality, object property expression, or optional class expression filler, the method invokes an error utility to signal that this restriction type cannot be processed. Consequently, it always returns None and prevents the successful conversion of any ontology elements relying on object minimum cardinality constraints.

        :param cardinality: The minimum number of distinct individuals the object property expression must relate to.
        :type cardinality: int
        :param p: The object property expression to which the minimum cardinality restriction applies.
        :type p: OWLObjectPropertyExpression
        :param c: The class expression acting as the filler for the restriction.
        :type c: OWLClassExpression

        :return: Returns None, indicating that object min cardinality restrictions are not supported.

        :rtype: str
        """

        if c is not None:
            Util.error(
                (
                    f"Object min cardinality restriction not supported -- ObjectMaxCardinalityRestriction({cardinality} {p} {c})"
                )
            )
        else:
            Util.error(
                (
                    f"Object min cardinality restriction not supported -- ObjectMaxCardinalityRestriction({cardinality} {p})"
                )
            )
        return None

    def get_object_max_cardinality_restriction(
        self,
        cardinality: int,
        p: OWLObjectPropertyExpression,
        c: OWLClassExpression = None,
    ) -> str:
        """
        Generates the string representation for an object property maximum cardinality restriction defined by the specified cardinality and object property expression. However, this feature is currently unsupported by the implementation; the method always invokes an error reporting utility to signal the unsupported operation and returns `None`, regardless of whether an optional filler class expression is provided.

        :param cardinality: The maximum number of distinct individuals that can be related via the object property.
        :type cardinality: int
        :param p: The object property expression to which the maximum cardinality restriction applies.
        :type p: OWLObjectPropertyExpression
        :param c: The class expression serving as the filler for the restriction.
        :type c: OWLClassExpression

        :return: None, indicating that object max cardinality restrictions are not supported.

        :rtype: str
        """

        if c is not None:
            Util.error(
                (
                    f"Object max cardinality restriction not supported -- ObjectMaxCardinalityRestriction({cardinality} {p} {c})"
                )
            )
        else:
            Util.error(
                (
                    f"Object max cardinality restriction not supported -- ObjectMaxCardinalityRestriction({cardinality} {p})"
                )
            )
        return None

    def get_object_exact_cardinality_restriction(
        self,
        cardinality: int,
        p: OWLObjectPropertyExpression,
        c: OWLClassExpression = None,
    ) -> str:
        """
        This method is intended to generate the FuzzyDL syntax for an OWL object exact cardinality restriction, which specifies that an individual must be connected to exactly a certain number of other individuals via a specific object property, optionally restricted to a specific class. However, this functionality is currently unsupported by the translator; regardless of the provided cardinality, property, or class expression, the method triggers an error indicating the lack of support and returns None.

        :param cardinality: The exact number of distinct individuals that the object property expression must relate to.
        :type cardinality: int
        :param p: The object property expression defining the relationship for the exact cardinality restriction.
        :type p: OWLObjectPropertyExpression
        :param c: The class expression serving as the filler for the restriction.
        :type c: OWLClassExpression

        :return: None, indicating that object exact cardinality restrictions are not supported.

        :rtype: str
        """

        if c is not None:
            Util.error(
                (
                    f"Object exact cardinality restriction not supported -- ObjectExactCardinalityRestriction({cardinality} {p} {c})"
                )
            )
        else:
            Util.error(
                (
                    f"Object exact cardinality restriction not supported -- ObjectExactCardinalityRestriction({cardinality} {p})"
                )
            )
        return None

    def get_data_min_cardinality_restriction(
        self, cardinality: int, p: OWLDataPropertyExpression, range: OWLDataRange = None
    ) -> str:
        """
        This method attempts to handle the translation of a data minimum cardinality restriction, but the underlying system does not support this construct. Instead of returning a valid string representation, it always invokes an error reporting mechanism to signal the unsupported feature and returns `None`. The method accepts the cardinality, data property expression, and an optional data range, though these arguments are used solely to construct the error message rather than to perform a successful translation.

        :param cardinality: The minimum number of values the data property expression must have.
        :type cardinality: int
        :param p: The data property expression to which the minimum cardinality constraint applies.
        :type p: OWLDataPropertyExpression
        :param range: The data range restricting the values of the data property.
        :type range: OWLDataRange

        :return: None, as data min cardinality restrictions are not supported.

        :rtype: str
        """

        if range is not None:
            Util.error(
                (
                    f"Data min cardinality restriction not supported -- DataMinCardinalityRestriction({cardinality} {p} {range})"
                )
            )
        else:
            Util.error(
                (
                    f"Data min cardinality restriction not supported -- DataMinCardinalityRestriction({cardinality} {p})"
                )
            )
        return None

    def get_data_max_cardinality_restriction(
        self, cardinality: int, p: OWLDataPropertyExpression, range: OWLDataRange = None
    ) -> str:
        """
        This method attempts to retrieve the string representation of a data maximum cardinality restriction defined by a specific cardinality and data property. However, the implementation indicates that this restriction type is not supported by the target system. Consequently, the method always triggers an error reporting the unsupported feature and returns None, regardless of whether a specific data range is provided.

        :param cardinality: The maximum number of distinct data values allowed for the data property.
        :type cardinality: int
        :param p: The data property expression to which the maximum cardinality restriction applies.
        :type p: OWLDataPropertyExpression
        :param range: The data range that the data property values must belong to.
        :type range: OWLDataRange

        :return: None, indicating that data max cardinality restrictions are not supported.

        :rtype: str
        """

        if range is not None:
            Util.error(
                (
                    f"Data max cardinality restriction not supported -- DataMaxCardinalityRestriction({cardinality} {p} {range})"
                )
            )
        else:
            Util.error(
                (
                    f"Data max cardinality restriction not supported -- DataMaxCardinalityRestriction({cardinality} {p})"
                )
            )
        return None

    def get_data_exact_cardinality_restriction(
        self, cardinality: int, p: OWLDataPropertyExpression, range: OWLDataRange = None
    ) -> str:
        """
        This method is intended to retrieve the string representation for a data exact cardinality restriction during the translation from FuzzyOwl2 to FuzzyDL. However, the implementation indicates that this specific restriction type is not supported by the target system. Consequently, the method invokes an error reporting utility to log the unsupported operation and returns None, regardless of whether a specific data range is provided.

        :param cardinality: The exact number of data values an individual must have for the given data property.
        :type cardinality: int
        :param p: The data property expression to which the exact cardinality restriction applies.
        :type p: OWLDataPropertyExpression
        :param range: The data range or datatype that the values of the data property must belong to.
        :type range: OWLDataRange

        :return: None, indicating that data exact cardinality restrictions are not supported.

        :rtype: str
        """

        if range is not None:
            Util.error(
                (
                    f"Data exact cardinality restriction not supported -- DataExactCardinalityRestriction({cardinality} {p} {range})"
                )
            )
        else:
            Util.error(
                (
                    f"Data exact cardinality restriction not supported -- DataExactCardinalityRestriction({cardinality} {p})"
                )
            )
        return None

    def get_top_object_property_name(self) -> typing.Optional[str]:
        """
        This method attempts to retrieve the identifier for the top object property, but the underlying implementation explicitly does not support this feature. When invoked, it triggers an error logging utility to report the unsupported status and subsequently returns None.

        :return: None, indicating that the top object property feature is not supported.

        :rtype: typing.Optional[str]
        """

        Util.error("Top object property not supported")
        return None

    def get_bottom_object_property_name(self) -> typing.Optional[str]:
        """
        Retrieves the name of the bottom object property, which represents the property that relates no individuals. Because the target framework does not support this specific OWL construct, the method triggers an error logging mechanism and returns None. Callers must handle the absence of this feature rather than expecting a valid property identifier.

        :return: None, indicating that the bottom object property is not supported.

        :rtype: typing.Optional[str]
        """

        Util.error("Bottom object property not supported")
        return None

    def get_atomic_object_property_name(self, p: OWLObjectProperty) -> str:
        """
        Retrieves the normalized name for an atomic object property, ensuring it is unique within the target representation. The method first derives a short name from the provided property. If this name conflicts with an existing data property, it is prefixed with "_op@" to disambiguate it; otherwise, the name is registered in the internal set of object properties. This process ensures that the returned identifier is valid and distinct for the translation context.

        :param p: The object property for which to retrieve the atomic name.
        :type p: OWLObjectProperty

        :return: The short name of the object property, prefixed with '_op@' if it conflicts with an existing data property name.

        :rtype: str
        """

        name: str = self.get_short_name(p)
        if name in self.data_properties:
            name = f"_op@{name}"
        else:
            self.object_properties.add(name)
        return name

    def get_top_data_property_name(self) -> typing.Optional[str]:
        """
        Attempts to retrieve the identifier of the top data property within the ontology mapping context. Since the underlying conversion logic does not currently support top data properties, this method triggers an error reporting mechanism and returns None to indicate the absence of a valid name.

        :return: None, indicating that the top data property is not supported.

        :rtype: typing.Optional[str]
        """

        Util.error("Top data property not supported")
        return None

    def get_bottom_data_property_name(self) -> typing.Optional[str]:
        """
        This method attempts to retrieve the name of the bottom data property, but the underlying conversion logic does not support this feature. As a result, calling this method triggers an error reporting mechanism and returns None. It serves as a placeholder to indicate that bottom data properties cannot be mapped or processed in this context.

        :return: The name of the bottom data property, or None if not supported.

        :rtype: typing.Optional[str]
        """

        Util.error("Bottom data property not supported")
        return None

    def get_atomic_data_property_name(self, p: OWLDataProperty) -> str:
        """
        Retrieves the canonical identifier for an OWL data property within the translation context, ensuring it is distinct from object properties. It derives the name from the property's short form and checks for potential collisions with existing object properties. If a conflict is detected, the name is prefixed with '_dp@' to ensure uniqueness; otherwise, the name is added to the internal registry of data properties and returned. This process guarantees that the generated identifier is valid and unambiguous for the target system.

        :param p: The OWL data property for which to retrieve the atomic name.
        :type p: OWLDataProperty

        :return: The short name of the data property, prefixed with '_dp@' if it conflicts with an existing object property name.

        :rtype: str
        """

        name: str = self.get_short_name(p)
        if name in self.object_properties:
            name = f"_dp@{name}"
        else:
            self.data_properties.add(name)
        return name

    def write_fuzzy_logic(self, logic: str) -> None:
        """
        Writes the fuzzy logic declaration to the output file using the specific syntax required by FuzzyDL. This method accepts a string identifying the logic type and generates the corresponding `(define-fuzzy-logic ...)` command. It ensures that the superclass logic is executed first, potentially handling validation or setup, before appending the formatted declaration to the output stream. The operation directly modifies the underlying file or buffer associated with the writer.

        :param logic: The name of the fuzzy logic to declare.
        :type logic: str
        """

        super().write_fuzzy_logic(logic)
        self.__write(f"(define-fuzzy-logic {logic})")

    def write_concept_declaration(self, c: OWLClassExpression) -> None:
        """
        Outputs the FuzzyDL syntax required to declare a primitive concept corresponding to the given OWL class expression. This method first delegates to the superclass implementation to perform any preliminary processing, then writes a formatted definition string that associates the concept's name with the top concept. The resulting output follows the specific `define-primitive-concept` structure expected by the FuzzyDL reasoner.

        :param c: The OWL class expression to be declared as a primitive concept.
        :type c: OWLClassExpression
        """

        super().write_concept_declaration(c)
        self.__write(
            f"(define-primitive-concept {self.get_class_name(c)} {self.get_top_concept_name()})"
        )

    def write_data_property_declaration(self, dp: OWLDataPropertyExpression) -> None:
        """
        Writes the declaration for an OWL data property expression to the FuzzyDL output stream, incorporating specific constraints required by the target syntax. This method first delegates to the parent class to handle the standard declaration logic and then writes the functional axiom associated with the property. Crucially, it overrides the default range by explicitly setting the property's range to `*string*` in the output, ensuring compatibility with FuzzyDL's type system regardless of the original ontology definition.

        :param dp: The OWL data property expression to be declared and written to the output.
        :type dp: OWLDataPropertyExpression
        """

        super().write_data_property_declaration(dp)
        self.write_functional_data_property_axiom(dp)
        self.__write(f"(range {self.get_data_property_name(dp)} *string*)")

    def write_object_property_declaration(
        self, op: OWLObjectPropertyExpression
    ) -> None:
        """
        This method handles the generation of an object property declaration in the FuzzyDL output format. It accepts an OWL object property expression representing the relationship to be declared and delegates the actual writing process to the superclass implementation. By invoking this method, the converter ensures that the property is formally defined in the target file, allowing subsequent references to the property within the FuzzyDL syntax to be valid.

        :param op: The object property expression to be declared in the output file.
        :type op: OWLObjectPropertyExpression
        """

        super().write_object_property_declaration(op)

    def write_concept_assertion_axiom(
        self, i: OWLIndividual, c: OWLClassExpression, d: float
    ) -> None:
        """
        Serializes a fuzzy concept assertion axiom into the FuzzyDL syntax and writes it to the output stream. This method accepts an OWL individual, a class expression, and a floating-point degree of membership, formatting them into the specific pattern `(instance individual_name class_name degree)`. It invokes the superclass method prior to writing to ensure any inherited processing is handled, and relies on internal helper methods to resolve the string identifiers for the individual and class.

        :param i: The individual subject of the concept assertion.
        :type i: OWLIndividual
        :param c: The OWL class expression representing the concept being asserted for the individual.
        :type c: OWLClassExpression
        :param d: The degree of membership indicating the extent to which the individual belongs to the concept.
        :type d: float
        """

        super().write_concept_assertion_axiom(i, c, d)
        self.__write(
            f"(instance {self.get_individual_name(i)} {self.get_class_name(c)} {d})"
        )

    def write_object_property_assertion_axiom(
        self,
        i1: OWLIndividual,
        i2: OWLIndividual,
        p: OWLObjectPropertyExpression,
        d: float,
    ) -> None:
        """
        Serializes a fuzzy object property assertion into the specific syntax required by FuzzyDL and writes it to the output stream. The method accepts two individuals, an object property expression, and a membership degree, formatting these components into a parenthesized string structure. It invokes the superclass implementation to handle any generic processing before writing the formatted assertion. The output string asserts that the first individual is related to the second individual via the specified property with the provided degree of truth.

        :param i1: The subject individual of the object property assertion.
        :type i1: OWLIndividual
        :param i2: The target individual of the object property assertion.
        :type i2: OWLIndividual
        :param p: The object property expression representing the relationship between the two individuals.
        :type p: OWLObjectPropertyExpression
        :param d: The degree of membership (truth value) for the assertion.
        :type d: float
        """

        super().write_object_property_assertion_axiom(i1, i2, p, d)
        self.__write(
            f"(related {self.get_individual_name(i1)} {self.get_individual_name(i2)} {self.get_object_property_name(p)} {d})"
        )

    def write_data_property_assertion_axiom(
        self,
        i: OWLIndividual,
        lit: OWLLiteral,
        p: OWLDataPropertyExpression,
        d: float,
    ) -> None:
        """
        This method serializes a fuzzy data property assertion, asserting that a specific individual possesses a literal value for a given property with a specified degree of membership, and writes it to the FuzzyDL output file. It dynamically adapts the output syntax based on the literal's datatype: fuzzy datatypes are expressed as existential restrictions, while numerical and string literals are expressed as functional equations. When encountering a numerical property for the first time, the method automatically generates the necessary range and functional property axioms to define the property's domain. Additionally, it performs specific sanitization on string literals—such as replacing whitespace and handling leading digits—to ensure compatibility with the target FuzzyDL syntax.

        :param i: The subject of the data property assertion, representing the individual that possesses the specified literal value.
        :type i: OWLIndividual
        :param lit: The literal value assigned to the individual via the data property.
        :type lit: OWLLiteral
        :param p: The data property expression linking the individual to the literal value.
        :type p: OWLDataPropertyExpression
        :param d: The degree of membership (truth value) for the assertion.
        :type d: float
        """

        super().write_data_property_assertion_axiom(i, lit, p, d)
        datatype: OWLDatatype = lit.datatype
        dp_name: str = self.get_data_property_name(p)
        if datatype is None:
            self.__write(
                f"(instance {self.get_individual_name(i)} (= {dp_name} {lit}) {d})"
            )
        else:
            datatype_name: str = self.get_short_name(datatype)
            if datatype_name in self.fuzzy_datatypes:
                self.__write(
                    f"(instance {self.get_individual_name(i)} (some {dp_name} {datatype_name}) {d})"
                )
            else:
                if self.__is_real_datatype(lit) or self.__is_integer_datatype(lit):
                    if dp_name not in self.numerical_datatypes:
                        self.numerical_datatypes.add(dp_name)
                        self.write_functional_data_property_axiom(p)
                        if self.__is_integer_datatype(lit):
                            self.__write(
                                f"(range {dp_name} *integer* {FuzzyOwl2ToFuzzyDL.INTEGER_MIN_VALUE} {FuzzyOwl2ToFuzzyDL.INTEGER_MAX_VALUE})"
                            )
                        else:
                            self.__write(
                                f"(range {dp_name} *real* {FuzzyOwl2ToFuzzyDL.DOUBLE_MIN_VALUE} {FuzzyOwl2ToFuzzyDL.DOUBLE_MAX_VALUE})"
                            )
                    value: typing.Any = None
                    if self.__is_real_datatype(lit):
                        value = float(str(lit.value))
                    else:
                        value = int(str(lit.value))
                    self.__write(
                        f"(instance {self.get_individual_name(i)} (= {dp_name} {value}) {d})"
                    )
                else:
                    if dp_name not in self.string_datatypes:
                        self.string_datatypes.add(dp_name)
                        self.write_data_property_declaration(p)
                    l: str = str(lit)
                    l: str = re.sub(r"\s", "_", l)
                    l: str = re.sub(r"[\)\(]", "--", l)
                    l: str = re.sub(r"\"", "'", l)
                    if l[0] in string.digits:
                        l = f"_{l}"
                    self.__write(
                        f"(instance {self.get_individual_name(i)} (= {dp_name} {l}) {d})"
                    )

    def write_negative_object_property_assertion_axiom(
        self,
        i1: OWLIndividual,
        i2: OWLIndividual,
        p: OWLObjectPropertyExpression,
        d: float,
    ) -> None:
        """
        This method attempts to serialize a negative object property assertion, which specifies that a relationship does not hold between two individuals with a certain degree of membership. It accepts the source and target individuals, the object property, and the membership degree as arguments. While the method invokes the superclass implementation to handle the initial processing, it ultimately signals that this specific axiom type is not supported by the FuzzyDL converter by triggering an error message containing the assertion details.

        :param i1: The subject individual of the negative object property assertion.
        :type i1: OWLIndividual
        :param i2: The individual that is the object of the negative object property assertion.
        :type i2: OWLIndividual
        :param p: The object property expression representing the relationship that is being negated between the two individuals.
        :type p: OWLObjectPropertyExpression
        :param d: The degree of truth for the negative assertion.
        :type d: float
        """

        super().write_negative_object_property_assertion_axiom(i1, i2, p, d)
        Util.error(
            f"Negative object property assertion not supported -- NegativeObjectPropertyAssertion({p} {i1} {i2} {d})"
        )
        return None

    def write_negative_data_property_assertion_axiom(
        self,
        i: OWLIndividual,
        lit: OWLLiteral,
        p: OWLDataPropertyExpression,
        d: float,
    ) -> None:
        """
        This method processes negative data property assertions by attempting to write them to the FuzzyDL output file using the provided individual, literal, data property, and degree of membership. It invokes the superclass implementation to handle the initial processing steps. However, the method explicitly signals that negative data property assertions are not supported by the FuzzyDL target system by triggering an error utility. As a result, this function serves as a guardrail to identify unsupported constructs during the translation process rather than successfully generating valid output.

        :param i: The subject individual of the negative data property assertion.
        :type i: OWLIndividual
        :param lit: The literal value that the individual is asserted not to possess for the specified data property.
        :type lit: OWLLiteral
        :param p: The data property expression involved in the negative assertion.
        :type p: OWLDataPropertyExpression
        :param d: The degree of membership associated with the fuzzy assertion.
        :type d: float
        """

        super().write_negative_data_property_assertion_axiom(i, lit, p, d)
        Util.error(
            f"Negative data property assertion not supported -- NegativeDataPropertyAssertion({p} {i} {lit} {d})"
        )
        return None

    def write_same_individual_axiom(self, ind_set: set[OWLIndividual]) -> None:
        """
        Attempts to write an OWL same individual axiom to the output by invoking the superclass's implementation. Since the FuzzyDL syntax does not support same individual axioms, this method subsequently triggers an error to indicate that the feature is unsupported for the provided set of individuals. The method effectively halts further processing of this specific axiom while ensuring any necessary state updates from the parent class are executed.

        :param ind_set: A set of OWL individuals that are asserted to be identical.
        :type ind_set: set[OWLIndividual]
        """

        super().write_same_individual_axiom(ind_set)
        Util.error(
            f"Same individual axiom not supported -- SameIndividuals({self.__get_set_name(ind_set)})"
        )
        return None

    def write_different_individuals_axiom(self, ind_set: set[OWLIndividual]) -> None:
        """
        This method processes a 'DifferentIndividuals' axiom by first delegating the operation to the superclass implementation. It accepts a set of OWL individuals as input but explicitly signals that the target FuzzyDL language does not support this type of axiom. As a result, the method invokes an error reporting utility to log the unsupported feature, ensuring that the user is notified that these specific individuals cannot be defined as distinct within the generated output.

        :param ind_set: The set of individuals that are asserted to be pairwise distinct.
        :type ind_set: set[OWLIndividual]
        """

        super().write_different_individuals_axiom(ind_set)
        Util.error(
            f"Different individual axiom not supported -- DifferentIndividuals({self.__get_set_name(ind_set)})"
        )
        return None

    def write_disjoint_classes_axiom(self, class_set: set[OWLClassExpression]) -> None:
        """
        This method serializes a disjoint classes axiom into the FuzzyDL output format by processing a set of OWL class expressions. It first invokes the superclass implementation to handle any shared logic, then checks if the set contains at least two elements; if the set is empty or contains only a single class, the method returns without writing. For valid input, it constructs and writes a formatted string using the 'disjoint' keyword followed by the short names of the classes in the set.

        :param class_set: A collection of class expressions to be declared as mutually disjoint.
        :type class_set: set[OWLClassExpression]
        """

        super().write_disjoint_classes_axiom(class_set)
        if len(class_set) <= 1:
            return
        self.__write(
            f"(disjoint {' '.join(self.get_short_name(c) for c in class_set)})"
        )

    def write_disjoint_union_axiom(self, class_set: set[OWLClassExpression]) -> None:
        """
        Writes a disjoint union axiom to the FuzzyDL output file for the given set of class expressions. This method invokes the superclass implementation before processing the input. It handles edge cases by returning immediately if the set contains one or fewer elements. Furthermore, it enforces a strict type constraint where all elements in the set must be instances of OWLClass; complex class expressions are not supported and will trigger an error. If validation passes, the method generates the appropriate FuzzyDL syntax using the short names of the classes and writes it to the output.

        :param class_set: A set of OWL classes to be written as a disjoint union axiom. Must contain only atomic OWLClass instances, as complex expressions are not supported.
        :type class_set: set[OWLClassExpression]
        """

        super().write_disjoint_union_axiom(class_set)
        if len(class_set) <= 1:
            return
        for c in class_set:
            if not isinstance(c, OWLClass):
                Util.error("Concept type not supported in disjoint union axiom")
        self.__write(
            f"(disjoint-union {' '.join(self.get_short_name(c) for c in class_set)})"
        )

    def write_subclass_of_axiom(
        self, subclass: OWLClassExpression, superclass: OWLClassExpression, d: float
    ) -> None:
        """
        Translates a fuzzy subclass axiom into the appropriate FuzzyDL syntax and writes it to the output stream. The method distinguishes between crisp and fuzzy relationships: if the subclass is a simple named class and the degree of membership is exactly 1, it outputs a primitive concept definition. For complex subclass expressions or degrees less than 1, it outputs an implication statement including the specific degree value. Before writing, it delegates to the parent class's implementation to handle any generic processing.

        :param subclass: The OWL class expression representing the subclass in the axiom, used to generate the left-hand side of the FuzzyDL implication or primitive concept definition.
        :type subclass: OWLClassExpression
        :param superclass: The parent class or general concept that the subclass is being defined as a subset of.
        :type superclass: OWLClassExpression
        :param d: The degree of membership or truth value for the fuzzy implication.
        :type d: float
        """

        super().write_subclass_of_axiom(subclass, superclass, d)
        if isinstance(subclass, OWLClass) and d == 1:
            self.__write(
                f"(define-primitive-concept {self.get_short_name(subclass)} {self.get_class_name(superclass)})"
            )
        else:
            self.__write(
                f"(implies {self.get_class_name(subclass)} {self.get_class_name(superclass)} {d})"
            )

    def write_equivalent_classes_axiom(
        self, class_set: set[OWLClassExpression]
    ) -> None:
        """
        Serializes an OWL equivalent classes axiom into the FuzzyDL output format by analyzing the structure of the provided class expressions. The method first invokes the superclass implementation and then determines the appropriate FuzzyDL syntax based on whether a named OWLClass is present in the set. If no named class is found, it generates a single `equivalent-concepts` statement linking all expressions; otherwise, it treats the first named class as the primary concept and issues individual `define-concept` statements to equate it with every other expression in the set. This process directly writes to the underlying output stream.

        :param class_set: The set of class expressions involved in the equivalence axiom. The method attempts to locate a named class within this set to define it as equivalent to the remaining expressions.
        :type class_set: set[OWLClassExpression]
        """

        super().write_equivalent_classes_axiom(class_set)
        name: str = None
        left_class: OWLClassExpression = None
        for c in class_set:
            if isinstance(c, OWLClass):
                name = self.get_short_name(c)
                left_class = c
                break
        if name is None:
            self.__write(
                f"(equivalent-concepts {' '.join(self.get_class_name(c) for c in class_set)})"
            )
        else:
            for c in class_set:
                if c != left_class:
                    self.__write(f"(define-concept {name} {self.get_class_name(c)})")

    def write_sub_object_property_of_axiom(
        self,
        subproperty: OWLObjectPropertyExpression,
        superproperty: OWLObjectPropertyExpression,
        d: float,
    ) -> None:
        """
        Translates a fuzzy object property subsumption axiom into the specific syntax required by FuzzyDL and appends it to the output stream. It accepts the subproperty, superproperty, and a degree of membership, formatting these into an `(implies-role ...)` expression. Before writing, the method invokes the superclass implementation to ensure any inherited logic or state updates are executed.

        :param subproperty: The object property expression representing the subproperty in the SubObjectPropertyOf axiom.
        :type subproperty: OWLObjectPropertyExpression
        :param superproperty: The object property expression representing the superproperty (parent) in the sub-property relationship.
        :type superproperty: OWLObjectPropertyExpression
        :param d: The degree of membership (truth value) for the subproperty-superproperty implication.
        :type d: float
        """

        super().write_sub_object_property_of_axiom(subproperty, superproperty, d)
        self.__write(
            f"(implies-role {self.get_object_property_name(subproperty)} {self.get_object_property_name(superproperty)} {d})"
        )

    def write_sub_data_property_of_axiom(
        self,
        subproperty: OWLDataPropertyExpression,
        superproperty: OWLDataPropertyExpression,
        d: float,
    ) -> None:
        """
        Translates a fuzzy sub-data-property axiom into the specific syntax required by FuzzyDL and writes it to the output file. The method constructs a command string using the resolved names of the subproperty and superproperty, combined with the provided degree of membership, formatted as `(implies-role ... )`. It first delegates to the parent class's implementation to handle any shared processing logic before appending the formatted expression to the output stream, resulting in a direct side effect on the file or buffer being written to.

        :param subproperty: The data property expression representing the subproperty in the subproperty axiom.
        :type subproperty: OWLDataPropertyExpression
        :param superproperty: The parent data property expression that the subproperty is a subset of.
        :type superproperty: OWLDataPropertyExpression
        :param d: The degree of membership representing the strength of the implication.
        :type d: float
        """

        super().write_sub_data_property_of_axiom(subproperty, superproperty, d)
        self.__write(
            f"(implies-role {self.get_data_property_name(subproperty)} {self.get_data_property_name(superproperty)} {d})"
        )

    def write_sub_property_chain_of_axiom(
        self,
        chain: list[OWLObjectPropertyExpression],
        superproperty: OWLObjectPropertyExpression,
        d: float,
    ) -> None:
        """
        This method processes a sub-property chain axiom by accepting a list of object property expressions representing the chain, a superproperty expression, and a degree of membership. While it invokes the superclass method to handle the standard writing logic, it explicitly logs an error message indicating that subproperty chain axioms are not supported in the current implementation. As a result, the method does not successfully translate the axiom to the FuzzyDL output and instead reports the unsupported feature.

        :param chain: The ordered list of object property expressions forming the property chain.
        :type chain: list[OWLObjectPropertyExpression]
        :param superproperty: The object property expression that the property chain is a sub-property of.
        :type superproperty: OWLObjectPropertyExpression
        :param d: The degree of membership or truth value for the sub-property chain axiom.
        :type d: float
        """

        super().write_sub_property_chain_of_axiom(chain, superproperty, d)
        Util.error(
            f"Subproperty chain axiom not supported -- SubObjectPropertyOf(ObjectPropertyChain({self.__get_set_name(chain)}) {superproperty} {d})"
        )
        return None

    def write_equivalent_object_properties_axiom(
        self, class_set: set[OWLObjectPropertyExpression]
    ) -> None:
        """
        Translates a set of equivalent OWL object properties into the FuzzyDL syntax by generating mutual implication rules between them. The method selects the first property in the input set as a reference and iterates over the remaining properties, writing bidirectional `(implies-role)` statements to establish that each property implies the reference and vice versa. This approach effectively decomposes the equivalence axiom into a set of sub-role axioms required by the target language. It also invokes the superclass method to perform any preliminary processing. Note that the method expects the input set to be non-empty to successfully select a reference property.

        :param class_set: A set of object property expressions that are asserted to be equivalent.
        :type class_set: set[OWLObjectPropertyExpression]
        """

        super().write_equivalent_object_properties_axiom(class_set)
        first: OWLObjectPropertyExpression = next(class_set)
        first_name: str = self.get_object_property_name(first)
        for property in class_set - set([first]):
            property_name: str = self.get_object_property_name(property)
            self.__write(f"(implies-role {first_name} {property_name})")
            self.__write(f"(implies-role {property_name} {first_name})")

    def write_equivalent_data_properties_axiom(
        self, class_set: set[OWLDataPropertyExpression]
    ) -> None:
        """
        This method handles the translation of an OWL equivalent data properties axiom into the FuzzyDL syntax by writing the corresponding logical rules to the output file. It accepts a set of data property expressions that are semantically equivalent and processes them by first delegating to the superclass implementation. To represent equivalence, the method selects the first property in the set as a reference point and generates bidirectional implication statements—using the `(implies-role ...)` construct—between this reference property and every other property in the set. This approach ensures that all properties in the input set are treated as interchangeable within the FuzzyDL representation.

        :param class_set: The set of data property expressions that are mutually equivalent.
        :type class_set: set[OWLDataPropertyExpression]
        """

        super().write_equivalent_data_properties_axiom(class_set)
        first: OWLDataPropertyExpression = next(class_set)
        first_name: str = self.get_data_property_name(first)
        for property in class_set - set([first]):
            property_name: str = self.get_data_property_name(property)
            self.__write(f"(implies-role {first_name} {property_name})")
            self.__write(f"(implies-role {property_name} {first_name})")

    def write_transitive_object_property_axiom(
        self, p: OWLObjectPropertyExpression
    ) -> None:
        """
        This method serializes a transitive object property axiom into the text format expected by the FuzzyDL reasoner. It takes an object property expression, retrieves its specific name, and writes the corresponding `(transitive <property_name>)` command to the output file. Before writing, it delegates to the superclass implementation to ensure that any shared processing logic or state updates are executed.

        :param p: The object property expression to be asserted as transitive.
        :type p: OWLObjectPropertyExpression
        """

        super().write_transitive_object_property_axiom(p)
        self.__write(f"(transitive {self.get_object_property_name(p)})")

    def write_symmetric_object_property_axiom(
        self, p: OWLObjectPropertyExpression
    ) -> None:
        """
        This method translates an OWL symmetric object property axiom into the corresponding syntax for FuzzyDL and writes it to the output file. It accepts an object property expression, retrieves its specific name, and formats it within a `(symmetric ...)` statement. The operation involves a side effect of writing to the output stream and also invokes the superclass implementation to ensure any inherited processing logic is executed.

        :param p: The object property expression to be asserted as symmetric.
        :type p: OWLObjectPropertyExpression
        """

        super().write_symmetric_object_property_axiom(p)
        self.__write(f"(symmetric {self.get_object_property_name(p)})")

    def write_asymmetric_object_property_axiom(
        self, p: OWLObjectPropertyExpression
    ) -> None:
        """
        This method handles the translation of an asymmetric object property axiom for the FuzzyDL output format. It accepts an object property expression representing the property to be defined as asymmetric. However, since the FuzzyDL syntax does not support asymmetric object property axioms, the method invokes the superclass handler and subsequently logs an error message indicating that this feature is unsupported.

        :param p: The object property expression to be declared as asymmetric.
        :type p: OWLObjectPropertyExpression
        """

        super().write_asymmetric_object_property_axiom(p)
        Util.error(
            f"Asymmetric object property axiom not supported -- AsymmetricObjectProperty({p})"
        )

    def write_reflexive_object_property_axiom(
        self, p: OWLObjectPropertyExpression
    ) -> None:
        """
        Translates an OWL reflexive object property axiom into the specific syntax required by the FuzzyDL reasoner. The method accepts an object property expression and retrieves its corresponding name to construct the command string `(reflexive <name>)`. Before writing this command to the output file, it delegates to the superclass implementation to ensure any necessary preprocessing or logging is performed.

        :param p: The object property expression to be asserted as reflexive.
        :type p: OWLObjectPropertyExpression
        """

        super().write_reflexive_object_property_axiom(p)
        self.__write(f"(reflexive {self.get_object_property_name(p)})")

    def write_irreflexive_object_property_axiom(
        self, p: OWLObjectPropertyExpression
    ) -> None:
        """
        This method handles the processing of an irreflexive object property axiom during the conversion workflow. It accepts an object property expression as input and invokes the superclass implementation, but subsequently raises an error indicating that this specific axiom type is not supported by the FuzzyDL format. Consequently, the operation results in an error message rather than a successful translation of the semantic constraint.

        :param p: The object property expression that is asserted to be irreflexive.
        :type p: OWLObjectPropertyExpression
        """

        super().write_irreflexive_object_property_axiom(p)
        Util.error(
            f"Irreflexive object property axiom not supported -- IrreflexiveObjectProperty({p})"
        )

    def write_functional_object_property_axiom(
        self, p: OWLObjectPropertyExpression
    ) -> None:
        """
        Generates the FuzzyDL syntax for a functional object property axiom corresponding to the given OWL object property expression. This method ensures that the functional constraint is written exactly once by maintaining a registry of processed properties; if the property name is not found in this registry, it is added and the string `(functional <name>)` is written to the output file. Additionally, the method invokes the superclass implementation to perform any necessary preliminary actions.

        :param p: The object property expression to be declared functional.
        :type p: OWLObjectPropertyExpression
        """

        super().write_functional_object_property_axiom(p)
        name: str = self.get_object_property_name(p)
        if name not in self.processed_functional_object_properties:
            self.processed_functional_object_properties.add(name)
            self.__write(f"(functional {name})")

    def write_functional_data_property_axiom(
        self, p: OWLDataPropertyExpression
    ) -> None:
        """
        Translates an OWL functional data property axiom into the corresponding FuzzyDL syntax and writes it to the output file. The method first invokes the superclass implementation to handle any generic processing logic. It then retrieves the canonical name of the provided data property expression and checks against an internal registry to ensure that the functional constraint is written only once per property. If the property has not yet been processed, it is added to the registry and the specific FuzzyDL command declaring the property as functional is emitted.

        :param p: The data property expression to be declared functional.
        :type p: OWLDataPropertyExpression
        """

        super().write_functional_data_property_axiom(p)
        name: str = self.get_data_property_name(p)
        if name not in self.processed_functional_data_properties:
            self.processed_functional_data_properties.add(name)
            self.__write(f"(functional {name})")

    def write_inverse_object_property_axiom(
        self, p1: OWLObjectPropertyExpression, p2: OWLObjectPropertyExpression
    ) -> None:
        """
        Translates an OWL inverse object property axiom into the specific syntax required by FuzzyDL and writes it to the output file. It accepts two object property expressions, resolves their string representations using the internal naming strategy, and formats them into the structure '(inverse name1 name2)'. The method also invokes the superclass implementation to ensure that any inherited processing or state management is performed during the operation.

        :param p1: The object property expression that is the inverse of the second property.
        :type p1: OWLObjectPropertyExpression
        :param p2: The object property expression that is the inverse of the first property.
        :type p2: OWLObjectPropertyExpression
        """

        super().write_inverse_object_property_axiom(p1, p2)
        self.__write(
            f"(inverse {self.get_object_property_name(p1)} {self.get_object_property_name(p2)})"
        )

    def write_inverse_functional_object_property_axiom(
        self, p: OWLObjectPropertyExpression
    ) -> None:
        """
        Translates an OWL inverse functional object property axiom into the corresponding syntax for FuzzyDL and writes it to the output stream. The method first invokes the superclass implementation to ensure any necessary state updates or logging occur, then formats the provided object property expression into the specific FuzzyDL command structure. This ensures that the constraint, which dictates that the inverse of the property is functional, is correctly represented for the target reasoning engine.

        :param p: The object property expression to be declared as inverse functional.
        :type p: OWLObjectPropertyExpression
        """

        super().write_inverse_functional_object_property_axiom(p)
        self.__write(f"(inverse-functional {self.get_object_property_name(p)})")

    def write_object_property_domain_axiom(
        self, p: OWLObjectPropertyExpression, c: OWLClassExpression
    ) -> None:
        """
        Translates an OWL object property domain axiom into the FuzzyDL syntax and writes it to the output stream. The method accepts an object property expression and a class expression, formatting them into the FuzzyDL command structure '(domain property_name class_name)'. It ensures that any necessary preprocessing defined in the superclass is performed before the actual string is written.

        :param p: The object property expression whose domain is being defined.
        :type p: OWLObjectPropertyExpression
        :param c: The class expression representing the domain of the object property.
        :type c: OWLClassExpression
        """

        super().write_object_property_domain_axiom(p, c)
        self.__write(
            f"(domain {self.get_object_property_name(p)} {self.get_class_name(c)})"
        )

    def write_object_property_range_axiom(
        self, p: OWLObjectPropertyExpression, c: OWLClassExpression
    ) -> None:
        """
        Generates and writes the FuzzyDL syntax for an object property range axiom, defining that the range of the specified object property is restricted to the given class. The method resolves the internal names of the input property and class expressions and formats them into the specific string structure required by FuzzyDL. It invokes the superclass implementation to handle any shared processing or state updates before appending the formatted axiom to the underlying output destination.

        :param p: The object property expression for which the range is being defined.
        :type p: OWLObjectPropertyExpression
        :param c: The class expression defining the range of the object property.
        :type c: OWLClassExpression
        """

        super().write_object_property_range_axiom(p, c)
        self.__write(
            f"(range {self.get_object_property_name(p)} {self.get_class_name(c)})"
        )

    def write_data_property_domain_axiom(
        self, p: OWLDataPropertyExpression, c: OWLClassExpression
    ) -> None:
        """
        Translates an OWL data property domain axiom into the corresponding FuzzyDL syntax and writes it to the output stream. This method handles the serialization of the constraint that individuals possessing a specific data property must belong to a designated class. It first invokes the superclass implementation to ensure any base-level processing occurs, then resolves the provided property and class expressions into their string representations and formats them as a parenthesized domain statement. The resulting string is appended to the underlying file or buffer managed by the writer.

        :param p: The data property expression for which the domain is being defined.
        :type p: OWLDataPropertyExpression
        :param c: The class expression defining the domain of the data property.
        :type c: OWLClassExpression
        """

        super().write_data_property_domain_axiom(p, c)
        self.__write(
            f"(domain {self.get_data_property_name(p)} {self.get_class_name(c)})"
        )

    def write_data_property_range_axiom(
        self, p: OWLDataPropertyExpression, range: OWLDataRange
    ) -> None:
        """
        Converts an OWL data property range axiom into FuzzyDL-compatible syntax and writes it to the output stream. It inspects the data range to map standard OWL datatypes (such as strings or booleans) or restricted numerical ranges (defined by min/max facets) to specific FuzzyDL type keywords. When processing numerical restrictions, the method handles exclusive boundaries by adjusting values using a defined epsilon or integer increment. As a side effect, it automatically declares the property as functional and updates internal registries of string, boolean, or numerical datatypes. If the range is an unsupported construct, such as a data enumeration (oneOf) or a malformed intersection, the method reports an error.

        :param p: The data property expression for which the range is being defined.
        :type p: OWLDataPropertyExpression
        :param range: The data range defining the permissible values for the data property, which can be a specific datatype or a numerical restriction with bounds.
        :type range: OWLDataRange
        """

        super().write_data_property_range_axiom(p, range)
        range_str: str = None
        dp_name: str = self.get_data_property_name(p)
        if isinstance(range, OWLDatatype):
            datatype: OWLDatatype = range
            if datatype.is_string() or range.is_date() or range.is_anyuri():
                self.string_datatypes.add(dp_name)
                range_str = "*string*"
            elif datatype.is_boolean():
                self.boolean_datatypes.add(dp_name)
                range_str = "*boolean*"
        elif isinstance(range, OWLDataIntersectionOf):
            correctness: int = 0
            is_integer: int = 0
            min: float = 0.0
            max: float = 0.0
            data_range: set[OWLDataRange] = typing.cast(
                OWLDataIntersectionOf, range
            ).data_ranges
            if len(data_range) == 2:
                for dr in data_range:
                    if isinstance(dr, OWLDatatypeRestriction):
                        restrictions: list[OWLFacet] = typing.cast(
                            OWLDatatypeRestriction, dr
                        ).restrictions
                        if len(restrictions) != 1:
                            continue
                        facet: OWLFacet = restrictions[0]
                        val: str = str(facet.value.value)
                        if facet.value.is_integer():
                            is_integer += 1
                        k: float = float(val)
                        if facet.constraint_to_uriref() == OWLFacet.MIN_INCLUSIVE:
                            min = k
                            correctness += 1
                        elif facet.constraint_to_uriref() == OWLFacet.MIN_EXCLUSIVE:
                            if is_integer != 0:
                                min = k + 1
                            else:
                                min = k + FuzzyOwl2ToFuzzyDL.EPSILON
                            correctness += 1
                        elif facet.constraint_to_uriref() == OWLFacet.MAX_INCLUSIVE:
                            max = k
                            correctness += 1
                        elif facet.constraint_to_uriref() == OWLFacet.MAX_EXCLUSIVE:
                            if is_integer != 0:
                                min = k - 1
                            else:
                                min = k - FuzzyOwl2ToFuzzyDL.EPSILON
                            correctness += 1
            if correctness == 2:
                if is_integer == 2:
                    range_str = f"*integer* {min} {max}"
                else:
                    range_str = f"*real* {min} {max}"
                self.numerical_datatypes.add(dp_name)
            else:
                Util.error(
                    f"Data property range axiom with range {range} not supported -- DataPropertyRange({p} {range})"
                )
        if range_str is not None:
            self.write_functional_data_property_axiom(p)
            self.__write(f"(range {dp_name} {range_str})")
        else:
            if isinstance(range, OWLDataOneOf):
                Util.error(
                    f"Data one of range axiom not supported -- DataPropertyRange({p} {range})"
                )
            else:
                range_type: OWLDatatype = range
                if self.__is_real_datatype(range_type):
                    self.write_functional_data_property_axiom(p)
                    self.__write(
                        f"(range {dp_name} *real* {FuzzyOwl2ToFuzzyDL.DOUBLE_MIN_VALUE} {FuzzyOwl2ToFuzzyDL.DOUBLE_MAX_VALUE})"
                    )
                    self.numerical_datatypes.add(dp_name)
                elif self.__is_integer_datatype(range_type):
                    self.write_functional_data_property_axiom(p)
                    facets: float = self.__get_facets(str(range_type))
                    self.__write(f"(range {dp_name} *integer* {facets[0]} {facets[1]})")
                    self.numerical_datatypes.add(dp_name)
                else:
                    Util.error(
                        f"Data property range axiom with range {range} not supported -- DataPropertyRange({p} {range})"
                    )

    def write_disjoint_object_properties_axiom(
        self, class_set: set[OWLObjectPropertyExpression]
    ) -> None:
        """
        Processes a set of object property expressions intended to represent a disjoint object properties axiom. Although the method delegates to the superclass implementation, it ultimately reports an error because the target FuzzyDL syntax does not support disjoint object properties. Consequently, calling this method will trigger an error message indicating the unsupported feature rather than successfully writing the axiom to the output file.

        :param class_set: A set of object property expressions that are asserted to be pairwise disjoint.
        :type class_set: set[OWLObjectPropertyExpression]
        """

        super().write_disjoint_object_properties_axiom(class_set)
        Util.error(
            f"Disjoint object properties axiom not supported -- DisjointObjectProperties({self.__get_set_name(class_set)})"
        )

    def write_disjoint_data_properties_axiom(
        self, class_set: set[OWLDataPropertyExpression]
    ) -> None:
        """
        Handles the translation of a disjoint data properties axiom by accepting a set of data property expressions. Although it invokes the superclass method to perform standard processing, it immediately triggers an error to indicate that this specific axiom type is not supported by the FuzzyDL language. Consequently, the operation results in an error message rather than generating valid FuzzyDL syntax.

        :param class_set: A set of data property expressions to be declared mutually disjoint.
        :type class_set: set[OWLDataPropertyExpression]
        """

        super().write_disjoint_data_properties_axiom(class_set)
        Util.error(
            f"Disjoint data properties axiom not supported -- DisjointDataProperties({self.__get_set_name(class_set)})"
        )

    def write_triangular_modifier_definition(
        self, name: str, mod: TriangularModifier
    ) -> None:
        """
        This method outputs the definition of a triangular modifier in the FuzzyDL syntax. It takes the modifier's name and the `TriangularModifier` object as arguments to construct the definition. The method first delegates to the parent class's implementation to handle any shared initialization or processing. Subsequently, it writes the formatted S-expression command, `(define-modifier name mod)`, to the internal output stream, effectively serializing the fuzzy logic concept for the FuzzyDL reasoner.

        :param name: The symbolic name used to identify the triangular modifier in the output definition.
        :type name: str
        :param mod: The triangular modifier instance to be written to the output file.
        :type mod: fuzzy_dl_owl2.fuzzydl.modifier.triangular_modifier.TriangularModifier
        """

        super().write_triangular_modifier_definition(name, mod)
        self.__write(f"(define-modifier {name} {mod})")

    def write_linear_modifier_definition(self, name: str, mod: LinearModifier) -> None:
        """
        Serializes a linear modifier definition into the FuzzyDL syntax and writes it to the output stream. This method first delegates to the parent class implementation to handle any preliminary processing or state management. It then constructs the specific FuzzyDL command string using the provided name and modifier object, appending the formatted definition to the underlying file or buffer.

        :param name: The symbolic name used to identify the linear modifier in the definition.
        :type name: str
        :param mod: The LinearModifier instance containing the definition details to be written to the output file.
        :type mod: fuzzy_dl_owl2.fuzzydl.modifier.linear_modifier.LinearModifier
        """

        super().write_linear_modifier_definition(name, mod)
        self.__write(f"(define-modifier {name} {mod})")

    def write_crisp_function_definition(self, name: str, dat: CrispFunction) -> None:
        """
        Generates the specific FuzzyDL syntax required to define a crisp function, formatting it as a fuzzy concept declaration. This method first delegates to the parent class's implementation to perform any necessary preliminary processing or state updates. It then constructs the definition string using the provided name and `CrispFunction` object, writing the resulting `(define-fuzzy-concept ...)` expression to the underlying output stream.

        :param name: The identifier for the crisp function being defined.
        :type name: str
        :param dat: The crisp function instance containing the definition details to be written.
        :type dat: CrispFunction
        """

        super().write_crisp_function_definition(name, dat)
        self.__write(f"(define-fuzzy-concept {name} {dat})")

    def write_left_shoulder_function_definition(
        self, name: str, dat: LeftShoulderFunction
    ) -> None:
        """
        Generates and outputs the FuzzyDL representation of a left shoulder fuzzy membership function. It accepts a specific name and the function data object, formatting them into a `define-fuzzy-concept` expression. Before writing the definition, the method invokes the superclass implementation to ensure consistent state or logging. The resulting string is written to the internal output stream, effectively defining the concept for the FuzzyDL reasoner.

        :param name: The symbolic name for the left shoulder function being defined.
        :type name: str
        :param dat: The left shoulder function object containing the parameters defining the fuzzy concept.
        :type dat: LeftShoulderFunction
        """

        super().write_left_shoulder_function_definition(name, dat)
        self.__write(f"(define-fuzzy-concept {name} {dat})")

    def write_right_shoulder_function_definition(
        self, name: str, dat: RightShoulderFunction
    ) -> None:
        """
        Translates a right shoulder function object into the specific syntax required by the FuzzyDL reasoner and writes it to the output file. The method first invokes the parent class's implementation to handle any shared logic or state updates. It then constructs a command string formatted as `(define-fuzzy-concept name dat)` using the provided identifier and function data, appending it to the output stream.

        :param name: The identifier for the right shoulder function being defined.
        :type name: str
        :param dat: The right shoulder function instance containing the parameters defining the fuzzy set's shape.
        :type dat: RightShoulderFunction
        """

        super().write_right_shoulder_function_definition(name, dat)
        self.__write(f"(define-fuzzy-concept {name} {dat})")

    def write_linear_function_definition(self, name: str, dat: LinearFunction) -> None:
        """
        Generates and outputs the FuzzyDL representation of a linear function definition based on the provided name and data object. This method ensures that any necessary preprocessing is handled by the superclass before constructing the specific syntax string. It then writes the formatted definition, which follows the pattern `(define-fuzzy-concept name data)`, to the target output destination.

        :param name: The identifier for the linear function being defined.
        :type name: str
        :param dat: The linear function object to be defined in the output file.
        :type dat: LinearFunction
        """

        super().write_linear_function_definition(name, dat)
        self.__write(f"(define-fuzzy-concept {name} {dat})")

    def write_triangular_function_definition(
        self, name: str, dat: TriangularFunction
    ) -> None:
        """
        Translates a triangular fuzzy function definition into the specific syntax required by the FuzzyDL reasoner and writes it to the output stream. This method accepts a name and a data object representing the function's parameters, formatting them into a `define-fuzzy-concept` expression. It ensures that any necessary preprocessing is handled by the superclass before the definition is written, resulting in a direct modification of the target output file.

        :param name: The identifier used to name the triangular function in the output definition.
        :type name: str
        :param dat: The triangular function instance defining the membership parameters for the fuzzy concept.
        :type dat: TriangularFunction
        """

        super().write_triangular_function_definition(name, dat)
        self.__write(f"(define-fuzzy-concept {name} {dat})")

    def write_trapezoidal_function_definition(
        self, name: str, dat: TrapezoidalFunction
    ) -> None:
        """
        Generates and outputs the FuzzyDL syntax for defining a trapezoidal fuzzy concept based on the provided name and function parameters. This method invokes the superclass implementation to perform any preliminary processing before formatting the definition into the specific `(define-fuzzy-concept ...)` structure required by the FuzzyDL language. The resulting string is written directly to the target output stream, effectively appending the definition to the generated file. The behavior depends on the string representation of the `TrapezoidalFunction` object matching the expected FuzzyDL format.

        :param name: The identifier assigned to the trapezoidal function in the output definition.
        :type name: str
        :param dat: The trapezoidal function instance defining the shape of the fuzzy concept.
        :type dat: TrapezoidalFunction
        """

        super().write_trapezoidal_function_definition(name, dat)
        self.__write(f"(define-fuzzy-concept {name} {dat})")

    def write_modified_function_definition(
        self, name: str, dat: ModifiedFunction
    ) -> None:
        """
        This method serializes a modified function definition into the FuzzyDL syntax and writes it to the output file. It accepts the function's name and a `ModifiedFunction` object containing the definition details. The process begins by invoking the parent class's implementation to ensure any base-level processing occurs. Subsequently, it formats the definition as a FuzzyDL concept using the syntax `(define-concept <name> <dat>)` and writes this string to the underlying file stream, resulting in a direct side effect of appending data to the output destination.

        :param name: The identifier assigned to the modified function in the output definition.
        :type name: str
        :param dat: The modified function object containing the definition details to be written to the FuzzyDL output file.
        :type dat: ModifiedFunction
        """

        super().write_modified_function_definition(name, dat)
        self.__write(f"(define-concept {name} {dat})")

    def write_modified_property_definition(
        self, name: str, dat: ModifiedProperty
    ) -> None:
        """
        This method attempts to process and write the definition of a modified property to the FuzzyDL output file by first delegating to the superclass implementation. However, it immediately triggers an error to indicate that modified properties are not supported by this specific translator. The error message provides diagnostic details, including the property name, the fuzzy modifier, and the underlying property, formatted as an `EquivalentObjectProperties` axiom.

        :param name: The identifier for the modified property being defined.
        :type name: str
        :param dat: The modified property object containing the fuzzy modifier and the associated property.
        :type dat: ModifiedProperty
        """

        super().write_modified_property_definition(name, dat)
        Util.error(
            f"Modified property not supported -- EquivalentObjectProperties({name} <{dat.get_fuzzy_modifier()} {dat.get_property()}>)"
        )

    def write_modified_concept_definition(
        self, name: str, dat: ModifiedConcept
    ) -> None:
        """
        Generates and writes the FuzzyDL syntax for a modified concept definition to the output stream. The method formats the definition as an S-expression `(define-concept name dat)`, relying on the string representation of the provided `ModifiedConcept` object for the definition body. Before writing, it invokes the superclass implementation to ensure any necessary preprocessing or state tracking is performed.

        :param name: The name used to identify the modified concept in the output definition.
        :type name: str
        :param dat: The modified concept instance containing the definition details.
        :type dat: fuzzy_dl_owl2.fuzzydl.concept.modified.modified_concept.ModifiedConcept
        """

        super().write_modified_concept_definition(name, dat)
        self.__write(f"(define-concept {name} {dat})")

    def write_fuzzy_nominal_concept_definition(
        self, name: str, dat: FuzzyNominalConcept
    ) -> None:
        """
        This method attempts to serialize a fuzzy nominal concept definition to the output stream by invoking the superclass's implementation. Immediately following this attempt, it logs an error stating that fuzzy nominal concepts are not supported in this translation context. The error message includes the concept name and data to indicate the specific failure point, effectively signaling that the translation cannot proceed for this entity.

        :param name: The identifier or label for the fuzzy nominal concept being defined.
        :type name: str
        :param dat: The fuzzy nominal concept object containing the definition details to be written.
        :type dat: FuzzyNominalConcept
        """

        super().write_fuzzy_nominal_concept_definition(name, dat)
        Util.error(
            f"Fuzzy nominal not supported -- EquivalentConcepts({name} OneOf({dat}))"
        )

    def write_weighted_concept_definition(self, name: str, c: WeightedConcept) -> None:
        """
        Generates and writes a weighted concept definition in FuzzyDL syntax to the output file. It formats the provided name and WeightedConcept object into the specific `(define-concept ...)` structure required by the target language. The method also invokes the superclass implementation to handle any shared logic or state management before performing the write operation.

        :param name: The identifier assigned to the weighted concept in the output definition.
        :type name: str
        :param c: The weighted concept instance containing the definition details to be serialized to the output file.
        :type c: fuzzy_dl_owl2.fuzzydl.concept.weighted_concept.WeightedConcept
        """

        super().write_weighted_concept_definition(name, c)
        self.__write(f"(define-concept {name} {c})")

    def write_weighted_max_concept_definition(
        self, name: str, c: WeightedMaxConcept
    ) -> None:
        """
        Serializes a weighted maximum concept into the FuzzyDL syntax and appends the definition to the output file. It invokes the parent class's implementation to perform any necessary preliminary processing before constructing the specific definition string. The method formats the output using the `define-concept` keyword, mapping the provided name to the string representation of the concept object, which results in a direct modification of the underlying output stream.

        :param name: The identifier for the weighted max concept being defined.
        :type name: str
        :param c: The weighted max concept definition containing the constituent concepts and their associated weights.
        :type c: fuzzy_dl_owl2.fuzzydl.concept.weighted_max_concept.WeightedMaxConcept
        """

        super().write_weighted_max_concept_definition(name, c)
        self.__write(f"(define-concept {name} {c})")

    def write_weighted_min_concept_definition(
        self, name: str, c: WeightedMinConcept
    ) -> None:
        """
        Serializes a weighted minimum concept definition into the specific syntax required by FuzzyDL and writes it to the output stream. This method accepts a string identifier for the concept and the `WeightedMinConcept` object itself, formatting them into an S-expression structure. Before writing the definition, it invokes the superclass implementation to ensure any necessary preprocessing or validation occurs. The operation results in the formatted line being appended to the internal output buffer, relying on the string representation of the concept object to generate the definition body.

        :param name: Identifier for the weighted min concept being defined.
        :type name: str
        :param c: The WeightedMinConcept instance representing the definition to be written.
        :type c: fuzzy_dl_owl2.fuzzydl.concept.weighted_min_concept.WeightedMinConcept
        """

        super().write_weighted_min_concept_definition(name, c)
        self.__write(f"(define-concept {name} {c})")

    def write_weighted_sum_concept_definition(
        self, name: str, c: WeightedSumConcept
    ) -> None:
        """
        Serializes a weighted sum concept definition into the FuzzyDL syntax and writes it to the output stream. This method first delegates to the superclass implementation to ensure any prerequisite processing or validation occurs. It then formats the definition as an S-expression using the provided name and the string representation of the concept object, specifically generating a `(define-concept name c)` statement.

        :param name: The identifier assigned to the weighted sum concept being defined.
        :type name: str
        :param c: The weighted sum concept object containing the definition structure and weights.
        :type c: fuzzy_dl_owl2.fuzzydl.concept.weighted_sum_concept.WeightedSumConcept
        """

        super().write_weighted_sum_concept_definition(name, c)
        self.__write(f"(define-concept {name} {c})")

    def write_weighted_sum_zero_concept_definition(
        self, name: str, c: WeightedSumZeroConcept
    ) -> None:
        """
        Serializes a weighted sum zero concept into the FuzzyDL syntax and writes it to the output stream. The method first delegates to the parent class implementation to handle any necessary preprocessing or validation logic, ensuring consistency with the broader conversion framework. It then constructs the definition using the specific FuzzyDL command structure `(define-concept name concept)` and writes the formatted string to the target file. This operation relies on the string representation of the concept object being valid and modifies the output destination without returning a value.

        :param name: The identifier for the weighted sum zero concept.
        :type name: str
        :param c: The object containing the definition logic and weights to be written.
        :type c: fuzzy_dl_owl2.fuzzydl.concept.weighted_sum_zero_concept.WeightedSumZeroConcept
        """

        super().write_weighted_sum_zero_concept_definition(name, c)
        self.__write(f"(define-concept {name} {c})")

    def write_owa_concept_definition(self, name: str, c: OwaConcept) -> None:
        """
        This method generates and writes the definition for an Ordered Weighted Averaging (OWA) concept to the FuzzyDL output file. It first invokes the parent class's implementation to ensure any inherited processing or state tracking is performed. Afterward, it formats the provided concept name and object into the specific FuzzyDL syntax `(define-concept name c)` and writes the resulting string to the output stream, effectively appending the definition to the file.

        :param name: The symbolic name assigned to the OWA concept being defined.
        :type name: str
        :param c: The OWA concept instance to be defined.
        :type c: fuzzy_dl_owl2.fuzzydl.concept.owa_concept.OwaConcept
        """

        super().write_owa_concept_definition(name, c)
        self.__write(f"(define-concept {name} {c})")

    def write_choquet_concept_definition(self, name: str, c: ChoquetConcept) -> None:
        """
        Serializes a Choquet concept definition into the FuzzyDL syntax and writes it to the output file. The method accepts a string identifier and a ChoquetConcept object, formatting them into the specific S-expression structure `(define-concept name c)` required by the target language. Before writing the definition, it delegates to the superclass implementation to ensure any shared processing logic is executed, effectively appending the new definition to the current output stream.

        :param name: The identifier assigned to the Choquet concept in the output definition.
        :type name: str
        :param c: The Choquet concept object containing the definition details to be serialized.
        :type c: ChoquetConcept
        """

        super().write_choquet_concept_definition(name, c)
        self.__write(f"(define-concept {name} {c})")

    def write_sugeno_concept_definition(self, name: str, c: SugenoConcept) -> None:
        """
        Serializes a Sugeno concept into the FuzzyDL syntax and writes it to the output stream. This method constructs a definition string using the provided name and the string representation of the SugenoConcept object, formatted as an S-expression. It ensures that the parent class's handling of the concept is executed via a super call before writing the formatted line to the underlying output destination.

        :param name: The identifier for the Sugeno concept being defined.
        :type name: str
        :param c: The Sugeno concept instance containing the definition structure and parameters to be written.
        :type c: SugenoConcept
        """

        super().write_sugeno_concept_definition(name, c)
        self.__write(f"(define-concept {name} {c})")

    def write_quasi_sugeno_concept_definition(
        self, name: str, c: QsugenoConcept
    ) -> None:
        """
        Writes the definition of a quasi-Sugeno concept to the FuzzyDL output file by formatting the provided name and concept object into the appropriate syntax. The method first invokes the superclass implementation to ensure any necessary setup or validation occurs, then appends the formatted `(define-concept ...)` string to the output stream. This process results in a side effect where the internal file or buffer is updated with the new concept definition.

        :param name: The identifier for the quasi-Sugeno concept being defined.
        :type name: str
        :param c: The quasi-Sugeno concept object containing the definition to be written.
        :type c: QsugenoConcept
        """

        super().write_quasi_sugeno_concept_definition(name, c)
        self.__write(f"(define-concept {name} {c})")

    def write_qowa_concept_definition(self, name: str, c: QowaConcept) -> None:
        """
        Serializes a QOWA concept definition into the FuzzyDL syntax and writes it to the output file. The method accepts a concept name and a QowaConcept object, formatting them into the specific FuzzyDL command structure `(define-concept name c)`. It first invokes the superclass implementation to handle any preliminary processing or state updates before appending the formatted definition to the output stream. This operation results in a direct modification of the file content and assumes the QowaConcept object can be correctly represented as a string within the FuzzyDL syntax.

        :param name: The symbolic identifier for the QOWA concept.
        :type name: str
        :param c: The QOWA concept instance containing the definition details to be written.
        :type c: fuzzy_dl_owl2.fuzzydl.concept.qowa_concept.QowaConcept
        """

        super().write_qowa_concept_definition(name, c)
        self.__write(f"(define-concept {name} {c})")
