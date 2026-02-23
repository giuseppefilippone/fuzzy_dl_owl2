from __future__ import annotations

import os
import traceback
import typing

import pyparsing as pp

from fuzzy_dl_owl2.fuzzydl.knowledge_base import KnowledgeBase
from fuzzy_dl_owl2.fuzzydl.query.query import Query
from fuzzy_dl_owl2.fuzzydl.util import utils
from fuzzy_dl_owl2.fuzzydl.util.config_reader import ConfigReader
from fuzzy_dl_owl2.fuzzydl.util.util import Util
from fuzzy_dl_owl2.fuzzyowl2.owl_types.choquet_concept import ChoquetConcept
from fuzzy_dl_owl2.fuzzyowl2.owl_types.concept_definition import ConceptDefinition
from fuzzy_dl_owl2.fuzzyowl2.owl_types.fuzzy_datatype import FuzzyDatatype
from fuzzy_dl_owl2.fuzzyowl2.owl_types.fuzzy_modifier import FuzzyModifier
from fuzzy_dl_owl2.fuzzyowl2.owl_types.fuzzy_nominal_concept import FuzzyNominalConcept
from fuzzy_dl_owl2.fuzzyowl2.owl_types.left_shoulder_function import (
    LeftShoulderFunction,
)
from fuzzy_dl_owl2.fuzzyowl2.owl_types.linear_function import LinearFunction
from fuzzy_dl_owl2.fuzzyowl2.owl_types.linear_modifier import LinearModifier
from fuzzy_dl_owl2.fuzzyowl2.owl_types.modified_concept import ModifiedConcept
from fuzzy_dl_owl2.fuzzyowl2.owl_types.modified_property import ModifiedProperty
from fuzzy_dl_owl2.fuzzyowl2.owl_types.owa_concept import OwaConcept
from fuzzy_dl_owl2.fuzzyowl2.owl_types.qowa_concept import QowaConcept
from fuzzy_dl_owl2.fuzzyowl2.owl_types.quasi_sugeno_concept import QsugenoConcept
from fuzzy_dl_owl2.fuzzyowl2.owl_types.right_shoulder_function import (
    RightShoulderFunction,
)
from fuzzy_dl_owl2.fuzzyowl2.owl_types.sugeno_concept import SugenoConcept
from fuzzy_dl_owl2.fuzzyowl2.owl_types.trapezoidal_function import TrapezoidalFunction
from fuzzy_dl_owl2.fuzzyowl2.owl_types.triangular_function import TriangularFunction
from fuzzy_dl_owl2.fuzzyowl2.owl_types.triangular_modifer import TriangularModifier
from fuzzy_dl_owl2.fuzzyowl2.owl_types.weighted_concept import WeightedConcept
from fuzzy_dl_owl2.fuzzyowl2.owl_types.weighted_max_concept import WeightedMaxConcept
from fuzzy_dl_owl2.fuzzyowl2.owl_types.weighted_min_concept import WeightedMinConcept
from fuzzy_dl_owl2.fuzzyowl2.owl_types.weighted_sum_concept import WeightedSumConcept
from fuzzy_dl_owl2.fuzzyowl2.owl_types.weighted_sum_zero_concept import (
    WeightedSumZeroConcept,
)
from fuzzy_dl_owl2.fuzzyowl2.util.constants import FuzzyOWL2Keyword


def _to_number(tokens: pp.ParseResults) -> float | int:
    """
    Converts the first element of a pyparsing `ParseResults` object into a numeric value, returning either an integer or a float. The function extracts the initial token, converts it to a float, and checks if the value is mathematically an integer; if so, it returns an `int`, otherwise it returns the `float`. This is typically employed as a parse action to transform string matches into their appropriate Python numeric types, though it will raise errors if the token list is empty or the string is not a valid number representation.

    :param tokens: Parsed results containing the string representation of the numeric value to be converted.
    :type tokens: pp.ParseResults

    :return: The numeric value of the first parsed token, returned as an int if the value is an integer, otherwise as a float.

    :rtype: float | int
    """

    v: float = float(str(tokens.as_list()[0]))
    return int(v) if v.is_integer() else v


def _parse_fuzzy_datatype(tokens: pp.ParseResults) -> FuzzyDatatype:
    """
    Parses a list of tokens resulting from a grammar parsing operation to construct a specific fuzzy datatype object. The function inspects the first token to determine the type of fuzzy function to instantiate, supporting left shoulder, right shoulder, linear, triangular, and trapezoidal functions. It extracts the necessary parameters from the subsequent tokens to initialize the corresponding function objects. If the first token does not match a known fuzzy keyword, the original tokens are returned unchanged. Additionally, the function logs the input tokens for debugging purposes.

    :param tokens: Parsed tokens representing a fuzzy datatype definition, containing the function type keyword and its associated numeric parameters.
    :type tokens: pp.ParseResults

    :return: A specific FuzzyDatatype instance (such as LeftShoulderFunction or TriangularFunction) constructed from the parsed tokens based on the identified keyword. Returns the original tokens if the input does not match a known fuzzy datatype pattern.

    :rtype: FuzzyDatatype
    """

    Util.debug(f"_parse_fuzzy_datatype -> {tokens}")
    list_tokens: list = tokens.as_list()
    if list_tokens[0] == FuzzyOWL2Keyword.LEFT_SHOULDER:
        return LeftShoulderFunction(list_tokens[1], list_tokens[2])
    elif list_tokens[0] == FuzzyOWL2Keyword.RIGHT_SHOULDER:
        return RightShoulderFunction(list_tokens[1], list_tokens[2])
    elif list_tokens[0] == FuzzyOWL2Keyword.LINEAR:
        return LinearFunction(list_tokens[1], list_tokens[2])
    elif list_tokens[0] == FuzzyOWL2Keyword.TRIANGULAR:
        return TriangularFunction(list_tokens[1], list_tokens[2], list_tokens[3])
    elif list_tokens[0] == FuzzyOWL2Keyword.TRAPEZOIDAL:
        return TrapezoidalFunction(
            list_tokens[1], list_tokens[2], list_tokens[3], list_tokens[4]
        )
    return tokens


def _parse_modifier_function(tokens: pp.ParseResults) -> FuzzyModifier:
    """
    This internal helper function processes a list of parsing tokens to construct a specific fuzzy modifier object based on the keyword found at the beginning of the list. If the first token corresponds to a linear modifier, it instantiates a `LinearModifier` using the subsequent token as an argument. If the first token indicates a triangular modifier, it instantiates a `TriangularModifier` using the following three tokens as parameters. In cases where the keyword is unrecognized, the function returns the original input tokens unchanged. Additionally, the function logs the incoming tokens for debugging purposes.

    :param tokens: Parsed elements containing the modifier keyword and the associated arguments used to instantiate a specific FuzzyModifier object.
    :type tokens: pp.ParseResults

    :return: A FuzzyModifier instance (LinearModifier or TriangularModifier) initialized with the parsed parameters, or the raw tokens if the modifier type is unrecognized.

    :rtype: FuzzyModifier
    """

    Util.debug(f"_parse_modifier_function -> {tokens}")
    list_tokens: list = tokens.as_list()
    if list_tokens[0] == FuzzyOWL2Keyword.LINEAR:
        return LinearModifier(list_tokens[1])
    elif list_tokens[0] == FuzzyOWL2Keyword.TRIANGULAR:
        return TriangularModifier(list_tokens[1], list_tokens[2], list_tokens[3])
    return tokens


def _parse_weighted_concept(tokens: pp.ParseResults) -> ConceptDefinition:
    """
    This function serves as a parse action to transform raw parsing tokens into a structured `WeightedConcept` object. It accepts a `pyparsing.ParseResults` object, converts it into a list, and extracts the first two elements to initialize the `WeightedConcept`. The function logs the input tokens for debugging purposes before performing the conversion. Note that if the input token list contains fewer than two elements, this function will raise an `IndexError`.

    :param tokens: Parsed results containing the concept and weight components required to construct a WeightedConcept.
    :type tokens: pp.ParseResults

    :return: A `WeightedConcept` instance representing the parsed weighted concept, constructed from the first two elements of the provided tokens.

    :rtype: ConceptDefinition
    """

    Util.debug(f"_parse_weighted_concept -> {tokens}")
    list_tokens: list = tokens.as_list()
    return WeightedConcept(list_tokens[0], list_tokens[1])


def _parse_modified_concept(tokens: pp.ParseResults) -> ConceptDefinition:
    """
    This internal helper function serves as a parsing callback to construct a domain object from raw pyparsing tokens. It converts the input `ParseResults` into a list and instantiates a `ModifiedConcept` using the first two elements found in the token sequence. The function performs a side effect of logging the input tokens for debugging purposes. It assumes that the input tokens contain at least two elements; failure to meet this condition will result in an IndexError.

    :param tokens: The parsed results containing the matched tokens that constitute the modified concept.
    :type tokens: pp.ParseResults

    :return: A `ModifiedConcept` instance representing the parsed modified concept, constructed from the first two elements of the input tokens.

    :rtype: ConceptDefinition
    """

    Util.debug(f"_parse_modified_concept -> {tokens}")
    list_tokens: list = tokens.as_list()
    return ModifiedConcept(list_tokens[0], list_tokens[1])


def _parse_q_owa_concept(tokens: pp.ParseResults) -> ConceptDefinition:
    """
    This internal function processes the results of a pyparsing match to construct a `QowaConcept` instance. It converts the input `ParseResults` object into a standard list and extracts the first two elements to pass as arguments to the `QowaConcept` constructor. The function logs the incoming tokens for debugging purposes before returning the constructed concept definition. It assumes the input tokens contain at least two elements; otherwise, an `IndexError` will occur.

    :param tokens: The parsed result object containing the sequence of elements extracted from the input, specifically the first two elements which are used to construct the QowaConcept.
    :type tokens: pp.ParseResults

    :return: A ConceptDefinition object representing the parsed Q-OWA concept, initialized with the first two elements of the parsed tokens.

    :rtype: ConceptDefinition
    """

    Util.debug(f"_parse_q_owa_concept -> {tokens}")
    list_tokens: list = tokens.as_list()
    return QowaConcept(list_tokens[0], list_tokens[1])


def _parse_fuzzy_nominal(tokens: pp.ParseResults) -> ConceptDefinition:
    """
    This internal parsing function constructs a FuzzyNominalConcept instance from a pyparsing.ParseResults object. It converts the input tokens into a standard list and extracts the first two elements to serve as arguments for the concept constructor. The function triggers a debug log operation with the input tokens before returning the new concept definition. Note that the function assumes the input list contains at least two elements; otherwise, an IndexError will occur.

    :param tokens: Parsed results containing the elements required to construct a FuzzyNominalConcept.
    :type tokens: pp.ParseResults

    :return: A FuzzyNominalConcept instance constructed from the parsed tokens, representing a fuzzy nominal concept definition.

    :rtype: ConceptDefinition
    """

    Util.debug(f"_parse_fuzzy_nominal -> {tokens}")
    list_tokens: list = tokens.as_list()
    return FuzzyNominalConcept(list_tokens[0], list_tokens[1])


def _parse_weighted_complex_concept(tokens: pp.ParseResults) -> ConceptDefinition:
    """
    Constructs a specific weighted complex concept definition from a list of parsed tokens, typically used as a callback or action within a parsing grammar. The function interprets the first element of the token list as a fuzzy OWL2 keyword determining the aggregation logic—such as weighted maximum, minimum, sum, or sum-zero—and treats all subsequent elements as operands. It asserts that these operands are instances of WeightedConcept before instantiating and returning the appropriate concrete class (e.g., WeightedMaxConcept or WeightedSumConcept) containing the list of weighted concepts. This process includes a debug logging step and will raise an AssertionError if the operand types are invalid.

    :param tokens: Parsed elements where the first item is the aggregation operator keyword and the remaining items are WeightedConcept instances.
    :type tokens: pp.ParseResults

    :return: Returns a ConceptDefinition object representing a weighted aggregation (maximum, minimum, sum, or sum-zero) of the parsed weighted concepts.

    :rtype: ConceptDefinition
    """

    Util.debug(f"_parse_weighted_complex_concept -> {tokens}")
    list_tokens: list = tokens.as_list()
    assert all(isinstance(a, WeightedConcept) for a in list_tokens[1:])
    wc: list[WeightedConcept] = [
        typing.cast(WeightedConcept, w) for w in list_tokens[1:]
    ]
    if list_tokens[0] == FuzzyOWL2Keyword.WEIGHTED_MAXIMUM:
        return WeightedMaxConcept(wc)
    elif list_tokens[0] == FuzzyOWL2Keyword.WEIGHTED_MINIMUM:
        return WeightedMinConcept(wc)
    elif list_tokens[0] == FuzzyOWL2Keyword.WEIGHTED_SUM:
        return WeightedSumConcept(wc)
    elif list_tokens[0] == FuzzyOWL2Keyword.WEIGHTED_SUMZERO:
        return WeightedSumZeroConcept(wc)


def _parse_integral_concept(tokens: pp.ParseResults) -> ConceptDefinition:
    """
    This internal helper function processes a list of parsed tokens to construct a specific fuzzy integral concept definition based on the identified keyword. It inspects the first element of the token list to determine the integral type—checking against OWA, Sugeno, Quasi-Sugeno, or Choquet keywords—and instantiates the corresponding `ConceptDefinition` subclass, passing the second and third elements of the list as arguments to the constructor. The function logs the input tokens for debugging purposes; however, it assumes the token list contains at least three elements and matches one of the expected keywords, potentially raising an `IndexError` or returning `None` implicitly if these conditions are not met.

    :param tokens: The parsed results containing the integral type keyword followed by the necessary arguments to construct the concept definition.
    :type tokens: pp.ParseResults

    :return: A specific ConceptDefinition instance (OwaConcept, SugenoConcept, QsugenoConcept, or ChoquetConcept) corresponding to the integral type identified in the tokens.

    :rtype: ConceptDefinition
    """

    Util.debug(f"_parse_integral_concept -> {tokens}")
    list_tokens: list = tokens.as_list()
    if list_tokens[0] == FuzzyOWL2Keyword.OWA:
        return OwaConcept(list_tokens[1], list_tokens[2])
    elif list_tokens[0] == FuzzyOWL2Keyword.SUGENO:
        return SugenoConcept(list_tokens[1], list_tokens[2])
    elif list_tokens[0] == FuzzyOWL2Keyword.QUASI_SUGENO:
        return QsugenoConcept(list_tokens[1], list_tokens[2])
    elif list_tokens[0] == FuzzyOWL2Keyword.CHOQUET:
        return ChoquetConcept(list_tokens[1], list_tokens[2])


def _parse_property(tokens: pp.ParseResults) -> ModifiedProperty:
    """
    This internal helper function processes parsing results to construct a `ModifiedProperty` instance. It expects the input tokens to contain a `ModifiedConcept` object as the first element; otherwise, it raises an `AssertionError`. The function extracts the fuzzy modifier and fuzzy concept from this `ModifiedConcept` and uses them to instantiate the new `ModifiedProperty`. Additionally, it logs the incoming tokens for debugging purposes.

    :param tokens: The parsed results expected to contain a `ModifiedConcept` as the primary element.
    :type tokens: pp.ParseResults

    :return: A ModifiedProperty instance constructed from the fuzzy modifier and concept extracted from the parsed tokens.

    :rtype: ModifiedProperty
    """

    Util.debug(f"_parse_property -> {tokens}")
    list_tokens: list = tokens.as_list()
    assert isinstance(list_tokens[0], ModifiedConcept)
    w: ModifiedConcept = typing.cast(ModifiedConcept, list_tokens[0])
    return ModifiedProperty(w.get_fuzzy_modifier(), w.get_fuzzy_concept())


class FuzzyOwl2Parser(object):
    """
    This class provides a specialized parser for the Fuzzy OWL 2 ontology language, designed to interpret XML-based annotation strings and transform them into structured data objects, specifically a KnowledgeBase and a list of Query instances. It leverages the pyparsing library to construct a detailed grammar capable of handling complex fuzzy logic constructs, such as modified concepts, weighted aggregations (including OWA and Choquet integrals), fuzzy datatypes (e.g., triangular or trapezoidal), and axioms with degree definitions. The primary interface is the static main method, which orchestrates configuration loading and parsing while managing error handling, though direct access to the underlying grammar and parsing logic is available via get_grammatics and parse_string.
    """

    @staticmethod
    def get_grammatics() -> pp.ParserElement:
        """
        This function generate the grammatics to parse the predicate wih formula "formula".

        Parameters
        ---------------------------
        formula := The predicate formula used for the parsing.

        Returns
        ---------------------------
        The parsed result given by pyparsing.
        """
        pp.ParserElement.enable_left_recursion(force=True)

        open_tag = FuzzyOWL2Keyword.OPEN_TAG.get_value().suppress()
        close_tag = FuzzyOWL2Keyword.CLOSE_TAG.get_value().suppress()
        slash = FuzzyOWL2Keyword.SLASH.get_value().suppress()
        single_close_tag = FuzzyOWL2Keyword.SINGLE_CLOSE_TAG.get_value().suppress()

        digits = pp.Word(pp.nums)
        numbers = (
            (
                pp.Opt(pp.one_of(['"', "'"])).suppress()
                + pp.Combine(
                    pp.Opt(pp.one_of(["+", "-"])) + digits + pp.Opt("." + digits)
                )
                + pp.Opt(pp.one_of(['"', "'"])).suppress()
            )
            .set_results_name("number")
            .set_parse_action(_to_number)
        )

        simple_string = pp.Word(
            pp.alphas + "_", pp.alphanums + "_'"
        )  # pp.Regex(r"[a-zA-Z_][a-zA-Z0-9_]*")
        strings = (
            pp.Opt(pp.one_of(['"', "'"])).suppress()
            + simple_string.set_results_name("string")
            + pp.Opt(pp.one_of(['"', "'"])).suppress()
        )
        variables = strings | simple_string.set_results_name("variable")

        common_start = (
            open_tag
            + FuzzyOWL2Keyword.FUZZY_OWL_2.get_value().suppress()
            + FuzzyOWL2Keyword.FUZZY_TYPE.get_value().suppress()
            + FuzzyOWL2Keyword.EQUAL.get_value().suppress()
        )
        common_end = (
            open_tag
            + slash
            + FuzzyOWL2Keyword.FUZZY_OWL_2.get_value().suppress()
            + close_tag
        )

        fuzzy_logic = (
            common_start
            + FuzzyOWL2Keyword.ONTOLOGY.get_value().suppress()
            + close_tag
            + open_tag
            + FuzzyOWL2Keyword.FUZZY_LOGIC.get_value().suppress()
            + FuzzyOWL2Keyword.LOGIC.get_value().suppress()
            + FuzzyOWL2Keyword.EQUAL.get_value().suppress()
            + (
                FuzzyOWL2Keyword.LUKASIEWICZ.get_value()
                | FuzzyOWL2Keyword.ZADEH.get_value()
            ).set_results_name("fuzzy_logic")
            + single_close_tag
            + common_end
        )

        comment_line = (
            pp.Literal("<!--") + pp.Regex(".*") + pp.Literal("-->")
        ).suppress()

        concept = pp.Forward()

        modified_role_concept = (
            FuzzyOWL2Keyword.CONCEPT.get_value().suppress()
            + FuzzyOWL2Keyword.TYPE.get_value().suppress()
            + FuzzyOWL2Keyword.EQUAL.get_value().suppress()
            + FuzzyOWL2Keyword.MODIFIED.get_value().suppress()
            + FuzzyOWL2Keyword.MODIFIER.get_value().suppress()
            + FuzzyOWL2Keyword.EQUAL.get_value().suppress()
            + variables
            + FuzzyOWL2Keyword.BASE.get_value().suppress()
            + FuzzyOWL2Keyword.EQUAL.get_value().suppress()
            + variables
        ).add_parse_action(_parse_modified_concept)

        weighted_concept = (
            open_tag
            + FuzzyOWL2Keyword.CONCEPT.get_value().suppress()
            + FuzzyOWL2Keyword.TYPE.get_value().suppress()
            + FuzzyOWL2Keyword.EQUAL.get_value().suppress()
            + FuzzyOWL2Keyword.WEIGHTED.get_value().suppress()
            + FuzzyOWL2Keyword.DEGREE_VALUE.get_value().suppress()
            + FuzzyOWL2Keyword.EQUAL.get_value().suppress()
            + numbers
            + FuzzyOWL2Keyword.BASE.get_value().suppress()
            + FuzzyOWL2Keyword.EQUAL.get_value().suppress()
            + variables
            + single_close_tag
        ).add_parse_action(_parse_weighted_concept)

        weights = (
            open_tag
            + FuzzyOWL2Keyword.WEIGHTS.get_value().suppress()
            + close_tag
            + (
                open_tag
                + FuzzyOWL2Keyword.WEIGHT.get_value().suppress()
                + close_tag
                + numbers
                + open_tag
                + slash
                + FuzzyOWL2Keyword.WEIGHT.get_value().suppress()
                + close_tag
            )[1, ...]
            + open_tag
            + slash
            + FuzzyOWL2Keyword.WEIGHTS.get_value().suppress()
            + close_tag
        )

        concepts = (
            open_tag
            + FuzzyOWL2Keyword.CONCEPT_NAMES.get_value().suppress()
            + close_tag
            + (
                open_tag
                + FuzzyOWL2Keyword.NAME.get_value().suppress()
                + close_tag
                + variables
                + open_tag
                + slash
                + FuzzyOWL2Keyword.NAME.get_value().suppress()
                + close_tag
            )[1, ...]
            + open_tag
            + slash
            + FuzzyOWL2Keyword.CONCEPT_NAMES.get_value().suppress()
            + close_tag
        )

        q_owa_concept = (
            FuzzyOWL2Keyword.QUANTIFIER.get_value().suppress()
            + FuzzyOWL2Keyword.EQUAL.get_value().suppress()
            + variables
            + close_tag
            + concepts
        ).add_parse_action(_parse_q_owa_concept)

        concept <<= (
            common_start
            + FuzzyOWL2Keyword.CONCEPT.get_value().suppress()
            + close_tag
            + (
                open_tag
                + FuzzyOWL2Keyword.CONCEPT.get_value().suppress()
                + FuzzyOWL2Keyword.TYPE.get_value().suppress()
                + FuzzyOWL2Keyword.EQUAL.get_value().suppress()
                + (
                    (
                        modified_role_concept + single_close_tag
                        | (
                            (
                                FuzzyOWL2Keyword.WEIGHTED_MAXIMUM.get_value()
                                | FuzzyOWL2Keyword.WEIGHTED_MINIMUM.get_value()
                                | FuzzyOWL2Keyword.WEIGHTED_SUM.get_value()
                                | FuzzyOWL2Keyword.WEIGHTED_SUMZERO.get_value()
                            )
                            + close_tag
                            + weighted_concept[1, ...]
                        ).add_parse_action(_parse_weighted_complex_concept)
                        | (
                            (
                                FuzzyOWL2Keyword.OWA.get_value()
                                | FuzzyOWL2Keyword.CHOQUET.get_value()
                                | FuzzyOWL2Keyword.SUGENO.get_value()
                                | FuzzyOWL2Keyword.QUASI_SUGENO.get_value()
                            )
                            + close_tag
                            + weights
                            + concepts
                        ).add_parse_action(_parse_integral_concept)
                        | FuzzyOWL2Keyword.Q_OWA.get_value().suppress() + q_owa_concept
                    )
                    + open_tag
                    + slash
                    + FuzzyOWL2Keyword.CONCEPT.get_value().suppress()
                    + close_tag
                    | weighted_concept + single_close_tag
                    | (
                        FuzzyOWL2Keyword.NOMINAL.get_value().suppress()
                        + FuzzyOWL2Keyword.DEGREE_DEF.get_value().suppress()
                        + FuzzyOWL2Keyword.EQUAL.get_value().suppress()
                        + numbers
                        + FuzzyOWL2Keyword.INDIVIDUAL.get_value().suppress()
                        + FuzzyOWL2Keyword.EQUAL.get_value().suppress()
                        + variables
                        + single_close_tag
                    ).add_parse_action(_parse_fuzzy_nominal)
                )
            )
            + common_end
        )

        property = (
            common_start
            + FuzzyOWL2Keyword.ROLE.get_value().suppress()
            + close_tag
            + open_tag
            + FuzzyOWL2Keyword.ROLE.get_value().suppress()
            + FuzzyOWL2Keyword.TYPE.get_value().suppress()
            + FuzzyOWL2Keyword.EQUAL.get_value().suppress()
            + modified_role_concept
            + slash
            + close_tag
            + common_end
        ).add_parse_action(_parse_property)

        fuzzy_datatype = (
            (
                (
                    FuzzyOWL2Keyword.LEFT_SHOULDER.get_value()
                    | FuzzyOWL2Keyword.RIGHT_SHOULDER.get_value()
                    | FuzzyOWL2Keyword.LINEAR.get_value()
                )
                + FuzzyOWL2Keyword.A.get_value().suppress()
                + FuzzyOWL2Keyword.EQUAL.get_value().suppress()
                + numbers
                + FuzzyOWL2Keyword.B.get_value().suppress()
                + FuzzyOWL2Keyword.EQUAL.get_value().suppress()
                + numbers
            )
            | (
                FuzzyOWL2Keyword.TRIANGULAR.get_value()
                + FuzzyOWL2Keyword.A.get_value().suppress()
                + FuzzyOWL2Keyword.EQUAL.get_value().suppress()
                + numbers
                + FuzzyOWL2Keyword.B.get_value().suppress()
                + FuzzyOWL2Keyword.EQUAL.get_value().suppress()
                + numbers
                + FuzzyOWL2Keyword.C.get_value().suppress()
                + FuzzyOWL2Keyword.EQUAL.get_value().suppress()
                + numbers
            )
            | (
                FuzzyOWL2Keyword.TRAPEZOIDAL.get_value()
                + FuzzyOWL2Keyword.A.get_value().suppress()
                + FuzzyOWL2Keyword.EQUAL.get_value().suppress()
                + numbers
                + FuzzyOWL2Keyword.B.get_value().suppress()
                + FuzzyOWL2Keyword.EQUAL.get_value().suppress()
                + numbers
                + FuzzyOWL2Keyword.C.get_value().suppress()
                + FuzzyOWL2Keyword.EQUAL.get_value().suppress()
                + numbers
                + FuzzyOWL2Keyword.D.get_value().suppress()
                + FuzzyOWL2Keyword.EQUAL.get_value().suppress()
                + numbers
            )
            | modified_role_concept
        ).add_parse_action(_parse_fuzzy_datatype)

        modifier = (
            (
                FuzzyOWL2Keyword.TRIANGULAR.get_value()
                + FuzzyOWL2Keyword.A.get_value().suppress()
                + FuzzyOWL2Keyword.EQUAL.get_value().suppress()
                + numbers
                + FuzzyOWL2Keyword.B.get_value().suppress()
                + FuzzyOWL2Keyword.EQUAL.get_value().suppress()
                + numbers
                + FuzzyOWL2Keyword.C.get_value().suppress()
                + FuzzyOWL2Keyword.EQUAL.get_value().suppress()
                + numbers
            )
            | (
                FuzzyOWL2Keyword.LINEAR.get_value()
                + FuzzyOWL2Keyword.C.get_value().suppress()
                + FuzzyOWL2Keyword.EQUAL.get_value().suppress()
                + numbers
            )
        ).add_parse_action(_parse_modifier_function)

        datatype = (
            common_start
            + (
                FuzzyOWL2Keyword.DATATYPE.get_value().suppress()
                + close_tag
                + open_tag
                + FuzzyOWL2Keyword.DATATYPE.get_value().suppress()
                + FuzzyOWL2Keyword.TYPE.get_value().suppress()
                + FuzzyOWL2Keyword.EQUAL.get_value().suppress()
                + fuzzy_datatype
                + slash
                + close_tag
                | FuzzyOWL2Keyword.MODIFIER.get_value().suppress()
                + close_tag
                + open_tag
                + FuzzyOWL2Keyword.MODIFIER.get_value().suppress()
                + FuzzyOWL2Keyword.TYPE.get_value().suppress()
                + FuzzyOWL2Keyword.EQUAL.get_value().suppress()
                + modifier
                + slash
                + close_tag
            )
            + common_end
        )

        axiom = (
            common_start
            + FuzzyOWL2Keyword.AXIOM.get_value().suppress()
            + close_tag
            + open_tag
            + FuzzyOWL2Keyword.DEGREE_DEF.get_value().suppress()
            + FuzzyOWL2Keyword.DEGREE_VALUE.get_value().suppress()
            + FuzzyOWL2Keyword.EQUAL.get_value().suppress()
            + numbers
            + slash
            + close_tag
            + common_end
        )

        gformula = comment_line | fuzzy_logic | concept | property | datatype | axiom
        return gformula

    @staticmethod
    @utils.recursion_unlimited
    def parse_string(
        instring: str,
        parse_all: bool = False,
        *,
        parseAll: bool = False,
    ) -> pp.ParseResults:
        return FuzzyOwl2Parser.get_grammatics().parse_string(
            instring, parse_all=parse_all, parseAll=parseAll
        )

    @staticmethod
    def load_config(*args) -> None:
        ConfigReader.load_parameters(os.path.join(os.getcwd(), "CONFIG.ini"), args)

    @staticmethod
    def main(annotation: str, *args) -> tuple[KnowledgeBase, list[Query]]:
        try:
            FuzzyOwl2Parser.load_config(*args)
            return FuzzyOwl2Parser.parse_string(annotation)
        except FileNotFoundError as e:
            Util.error(f"Error: File {args[0]} not found.")
        except Exception as e:
            Util.error(e)
            Util.error(traceback.format_exc())
