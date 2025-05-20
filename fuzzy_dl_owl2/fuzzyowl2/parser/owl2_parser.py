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
    v: float = float(str(tokens.as_list()[0]))
    return int(v) if v.is_integer() else v


def _parse_fuzzy_datatype(tokens: pp.ParseResults) -> FuzzyDatatype:
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
    Util.debug(f"_parse_modifier_function -> {tokens}")
    list_tokens: list = tokens.as_list()
    if list_tokens[0] == FuzzyOWL2Keyword.LINEAR:
        return LinearModifier(list_tokens[1])
    elif list_tokens[0] == FuzzyOWL2Keyword.TRIANGULAR:
        return TriangularModifier(list_tokens[1], list_tokens[2], list_tokens[3])
    return tokens


def _parse_weighted_concept(tokens: pp.ParseResults) -> ConceptDefinition:
    Util.debug(f"_parse_weighted_concept -> {tokens}")
    list_tokens: list = tokens.as_list()
    return WeightedConcept(list_tokens[0], list_tokens[1])


def _parse_modified_concept(tokens: pp.ParseResults) -> ConceptDefinition:
    Util.debug(f"_parse_modified_concept -> {tokens}")
    list_tokens: list = tokens.as_list()
    return ModifiedConcept(list_tokens[0], list_tokens[1])


def _parse_q_owa_concept(tokens: pp.ParseResults) -> ConceptDefinition:
    Util.debug(f"_parse_q_owa_concept -> {tokens}")
    list_tokens: list = tokens.as_list()
    return QowaConcept(list_tokens[0], list_tokens[1])


def _parse_fuzzy_nominal(tokens: pp.ParseResults) -> ConceptDefinition:
    Util.debug(f"_parse_fuzzy_nominal -> {tokens}")
    list_tokens: list = tokens.as_list()
    return FuzzyNominalConcept(list_tokens[0], list_tokens[1])


def _parse_weighted_complex_concept(tokens: pp.ParseResults) -> ConceptDefinition:
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
    Util.debug(f"_parse_property -> {tokens}")
    list_tokens: list = tokens.as_list()
    assert isinstance(list_tokens[0], ModifiedConcept)
    w: ModifiedConcept = typing.cast(ModifiedConcept, list_tokens[0])
    return ModifiedProperty(w.get_fuzzy_modifier(), w.get_fuzzy_concept())


class FuzzyOwl2Parser(object):

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
