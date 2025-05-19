from __future__ import annotations

import datetime
import os
import time
import traceback
import typing
from functools import reduce

import pyparsing as pp

from fuzzy_dl_owl2.fuzzydl.concept.all_some_concept import AllSomeConcept
from fuzzy_dl_owl2.fuzzydl.concept.approximation_concept import ApproximationConcept
from fuzzy_dl_owl2.fuzzydl.concept.choquet_integral import ChoquetIntegral
from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.concept.concrete.crisp_concrete_concept import (
    CrispConcreteConcept,
)
from fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_concrete_concept import (
    FuzzyConcreteConcept,
)
from fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_number.triangular_fuzzy_number import (
    TriangularFuzzyNumber,
)
from fuzzy_dl_owl2.fuzzydl.concept.concrete.left_concrete_concept import (
    LeftConcreteConcept,
)
from fuzzy_dl_owl2.fuzzydl.concept.concrete.linear_concrete_concept import (
    LinearConcreteConcept,
)
from fuzzy_dl_owl2.fuzzydl.concept.concrete.modified_concrete_concept import (
    ModifiedConcreteConcept,
)
from fuzzy_dl_owl2.fuzzydl.concept.concrete.right_concrete_concept import (
    RightConcreteConcept,
)
from fuzzy_dl_owl2.fuzzydl.concept.concrete.trapezoidal_concrete_concept import (
    TrapezoidalConcreteConcept,
)
from fuzzy_dl_owl2.fuzzydl.concept.concrete.triangular_concrete_concept import (
    TriangularConcreteConcept,
)
from fuzzy_dl_owl2.fuzzydl.concept.ext_threshold_concept import ExtThresholdConcept
from fuzzy_dl_owl2.fuzzydl.concept.has_value_concept import HasValueConcept
from fuzzy_dl_owl2.fuzzydl.concept.implies_concept import ImpliesConcept
from fuzzy_dl_owl2.fuzzydl.concept.operator_concept import OperatorConcept
from fuzzy_dl_owl2.fuzzydl.concept.owa_concept import OwaConcept
from fuzzy_dl_owl2.fuzzydl.concept.qowa_concept import QowaConcept
from fuzzy_dl_owl2.fuzzydl.concept.quasi_sugeno_integral import QsugenoIntegral
from fuzzy_dl_owl2.fuzzydl.concept.self_concept import SelfConcept
from fuzzy_dl_owl2.fuzzydl.concept.sugeno_integral import SugenoIntegral
from fuzzy_dl_owl2.fuzzydl.concept.threshold_concept import ThresholdConcept
from fuzzy_dl_owl2.fuzzydl.concept.truth_concept import TruthConcept
from fuzzy_dl_owl2.fuzzydl.concept.weighted_concept import WeightedConcept
from fuzzy_dl_owl2.fuzzydl.concept.weighted_max_concept import WeightedMaxConcept
from fuzzy_dl_owl2.fuzzydl.concept.weighted_min_concept import WeightedMinConcept
from fuzzy_dl_owl2.fuzzydl.concept.weighted_sum_concept import WeightedSumConcept
from fuzzy_dl_owl2.fuzzydl.concept.weighted_sum_zero_concept import (
    WeightedSumZeroConcept,
)
from fuzzy_dl_owl2.fuzzydl.degree.degree import Degree
from fuzzy_dl_owl2.fuzzydl.degree.degree_expression import DegreeExpression
from fuzzy_dl_owl2.fuzzydl.degree.degree_numeric import DegreeNumeric
from fuzzy_dl_owl2.fuzzydl.degree.degree_variable import DegreeVariable
from fuzzy_dl_owl2.fuzzydl.exception.inconsistent_ontology_exception import (
    InconsistentOntologyException,
)
from fuzzy_dl_owl2.fuzzydl.feature_function import FeatureFunction
from fuzzy_dl_owl2.fuzzydl.individual.individual import Individual
from fuzzy_dl_owl2.fuzzydl.knowledge_base import KnowledgeBase
from fuzzy_dl_owl2.fuzzydl.milp.expression import Expression
from fuzzy_dl_owl2.fuzzydl.milp.inequation import Inequation
from fuzzy_dl_owl2.fuzzydl.milp.solution import Solution
from fuzzy_dl_owl2.fuzzydl.milp.term import Term
from fuzzy_dl_owl2.fuzzydl.milp.variable import Variable
from fuzzy_dl_owl2.fuzzydl.modifier.linear_modifier import LinearModifier
from fuzzy_dl_owl2.fuzzydl.modifier.modifier import Modifier
from fuzzy_dl_owl2.fuzzydl.modifier.triangular_modifier import TriangularModifier
from fuzzy_dl_owl2.fuzzydl.query.all_instances_query import AllInstancesQuery
from fuzzy_dl_owl2.fuzzydl.query.bnp_query import BnpQuery
from fuzzy_dl_owl2.fuzzydl.query.defuzzify.lom_defuzzify_query import LomDefuzzifyQuery
from fuzzy_dl_owl2.fuzzydl.query.defuzzify.mom_defuzzify_query import MomDefuzzifyQuery
from fuzzy_dl_owl2.fuzzydl.query.defuzzify.som_defuzzify_query import SomDefuzzifyQuery
from fuzzy_dl_owl2.fuzzydl.query.kb_satisfiable_query import KbSatisfiableQuery
from fuzzy_dl_owl2.fuzzydl.query.max.max_instance_query import MaxInstanceQuery
from fuzzy_dl_owl2.fuzzydl.query.max.max_query import MaxQuery
from fuzzy_dl_owl2.fuzzydl.query.max.max_related_query import MaxRelatedQuery
from fuzzy_dl_owl2.fuzzydl.query.max.max_satisfiable_query import MaxSatisfiableQuery
from fuzzy_dl_owl2.fuzzydl.query.max.max_subsumes_query import MaxSubsumesQuery
from fuzzy_dl_owl2.fuzzydl.query.min.min_instance_query import MinInstanceQuery
from fuzzy_dl_owl2.fuzzydl.query.min.min_query import MinQuery
from fuzzy_dl_owl2.fuzzydl.query.min.min_related_query import MinRelatedQuery
from fuzzy_dl_owl2.fuzzydl.query.min.min_satisfiable_query import MinSatisfiableQuery
from fuzzy_dl_owl2.fuzzydl.query.min.min_subsumes_query import MinSubsumesQuery
from fuzzy_dl_owl2.fuzzydl.query.query import Query
from fuzzy_dl_owl2.fuzzydl.util import constants, utils
from fuzzy_dl_owl2.fuzzydl.util.config_reader import ConfigReader
from fuzzy_dl_owl2.fuzzydl.util.constants import (
    ConceptType,
    FuzzyDLKeyword,
    FuzzyLogic,
    InequalityType,
    LogicOperatorType,
    RestrictionType,
    VariableType,
)
from fuzzy_dl_owl2.fuzzydl.util.util import Util
from fuzzy_dl_owl2.fuzzydl.util.utils import class_debugging

TODAY: datetime.datetime = datetime.datetime.today()
LOG_DIR: str = os.path.join(
    ".", "logs", "parser", str(TODAY.year), str(TODAY.month), str(TODAY.day)
)
FILENAME: str = (
    f"fuzzydl_{str(TODAY.hour).zfill(2)}-{str(TODAY.minute).zfill(2)}-{str(TODAY.second).zfill(2)}.log"
)

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)


@class_debugging()
class DLParser(object):

    kb: KnowledgeBase = None
    queries_list: list[Query] = []

    @staticmethod
    def _check_abstract(c: Concept) -> None:
        if c.is_concrete():
            Util.error(f"Error: Concept {c} should be abstract.")

    @staticmethod
    # @pp.trace_parse_action
    def _to_number(tokens: pp.ParseResults) -> float | int:
        v: float = float(str(tokens.as_list()[0]))
        return int(v) if v.is_integer() else v

    @staticmethod
    # @pp.trace_parse_action
    def _fuzzy_logic_parser(tokens: pp.ParseResults) -> pp.ParseResults:
        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_fuzzy_logic_parser -> {tokens}")
        DLParser.kb.set_logic(FuzzyLogic(str(tokens.as_list()[0]).lower()))
        return tokens

    @staticmethod
    # @pp.trace_parse_action
    def _to_concept(c: typing.Union[str, Concept]) -> Concept:

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_to_concept -> {c}")
        return c if isinstance(c, Concept) else DLParser.kb.get_concept(c)
        # return DLParser.kb.get_concept(str(c))

    @staticmethod
    # @pp.trace_parse_action
    def _to_top_bottom_concept(tokens: pp.ParseResults) -> pp.ParseResults:
        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_to_top_bottom_concept -> {tokens}")
        list_tokens: list = tokens.as_list()
        if list_tokens[0] == FuzzyDLKeyword.TOP:
            return pp.ParseResults([TruthConcept.get_top()])
        elif list_tokens[0] == FuzzyDLKeyword.BOTTOM:
            return pp.ParseResults([TruthConcept.get_bottom()])
        else:
            return pp.ParseResults([DLParser._to_concept(list_tokens[0])])

    @staticmethod
    # @pp.trace_parse_action
    def _get_modifier(m: str) -> Modifier:
        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_get_modifier -> {m}")
        if len(DLParser.kb.modifiers) == 0 or m not in DLParser.kb.modifiers:
            Util.error(f"Error: {m} modifier is not defined.")
        return DLParser.kb.modifiers.get(m)

    @staticmethod
    # @pp.trace_parse_action
    def _parse_binary_concept(tokens: pp.ParseResults) -> pp.ParseResults:

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_parse_binary_concept -> {tokens}")
        list_tokens: list = tokens.as_list()
        operator: str = list_tokens[0]
        if isinstance(operator, Concept):
            return tokens
        if operator == FuzzyDLKeyword.AND:
            list_tokens: list[Concept] = [
                DLParser._to_concept(t) for t in list_tokens[1:]
            ]
            for c in list_tokens:
                DLParser._check_abstract(c)
            if DLParser.kb.get_logic() == FuzzyLogic.LUKASIEWICZ:
                return pp.ParseResults([OperatorConcept.lukasiewicz_and(*list_tokens)])
            elif DLParser.kb.get_logic() == FuzzyLogic.ZADEH:
                return pp.ParseResults([OperatorConcept.goedel_and(*list_tokens)])
            return pp.ParseResults([OperatorConcept.and_(*list_tokens)])
        elif operator == FuzzyDLKeyword.LUKASIEWICZ_AND:
            list_tokens: list[Concept] = [
                DLParser._to_concept(t) for t in list_tokens[1:]
            ]
            if DLParser.kb.get_logic() == FuzzyLogic.CLASSICAL:
                Util.error(
                    "Error: LUKASIEWICZ_AND cannot be used under classical reasoner."
                )
            for c in list_tokens:
                DLParser._check_abstract(c)
            return pp.ParseResults([OperatorConcept.lukasiewicz_and(*list_tokens)])
        elif operator == FuzzyDLKeyword.GOEDEL_AND:
            list_tokens: list[Concept] = [
                DLParser._to_concept(t) for t in list_tokens[1:]
            ]
            if DLParser.kb.get_logic() == FuzzyLogic.CLASSICAL:
                Util.error("Error: GOEDEL_AND cannot be used under classical reasoner.")
            for c in list_tokens:
                DLParser._check_abstract(c)
            return pp.ParseResults([OperatorConcept.goedel_and(*list_tokens)])
        elif operator == FuzzyDLKeyword.OR:
            list_tokens: list[Concept] = [
                DLParser._to_concept(t) for t in list_tokens[1:]
            ]
            for c in list_tokens:
                DLParser._check_abstract(c)
            if DLParser.kb.get_logic() == FuzzyLogic.LUKASIEWICZ:
                return pp.ParseResults([OperatorConcept.lukasiewicz_or(*list_tokens)])
            elif DLParser.kb.get_logic() == FuzzyLogic.ZADEH:
                return pp.ParseResults([OperatorConcept.goedel_or(*list_tokens)])
            return pp.ParseResults([OperatorConcept.or_(*list_tokens)])
        elif operator == FuzzyDLKeyword.LUKASIEWICZ_OR:
            list_tokens: list[Concept] = [
                DLParser._to_concept(t) for t in list_tokens[1:]
            ]
            if DLParser.kb.get_logic() == FuzzyLogic.CLASSICAL:
                Util.error(
                    "Error: LUKASIEWICZ_OR cannot be used under classical reasoner."
                )
            for c in list_tokens:
                DLParser._check_abstract(c)
            return pp.ParseResults([OperatorConcept.lukasiewicz_or(*list_tokens)])
        elif operator == FuzzyDLKeyword.GOEDEL_OR:
            list_tokens: list[Concept] = [
                DLParser._to_concept(t) for t in list_tokens[1:]
            ]
            if DLParser.kb.get_logic() == FuzzyLogic.CLASSICAL:
                Util.error("Error: GOEDEL_OR cannot be used under classical reasoner.")
            for c in list_tokens:
                DLParser._check_abstract(c)
            return pp.ParseResults([OperatorConcept.goedel_or(*list_tokens)])
        elif operator in (
            FuzzyDLKeyword.IMPLIES,
            FuzzyDLKeyword.GOEDEL_IMPLIES,
            FuzzyDLKeyword.LUKASIEWICZ_IMPLIES,
            FuzzyDLKeyword.ZADEH_IMPLIES,
            FuzzyDLKeyword.KLEENE_DIENES_IMPLIES,
        ):
            list_tokens: list[Concept] = [
                DLParser._to_concept(t) for t in list_tokens[1:]
            ]
            for c in list_tokens:
                DLParser._check_abstract(c)
            # degree: Degree = list_tokens[2] if len(list_tokens) == 3 else DegreeNumeric.get_one()
            # if operator == FuzzyDLKeyword.IMPLIES:
            #     return pp.ParseResults([DLParser.kb.implies(list_tokens[0], list_tokens[1], degree)])
            # elif operator == FuzzyDLKeyword.GOEDEL_IMPLIES:
            #     return pp.ParseResults([DLParser.kb.goedel_implies(list_tokens[0], list_tokens[1], degree)])
            # elif operator == FuzzyDLKeyword.LUKASIEWICZ_IMPLIES:
            #     return pp.ParseResults([DLParser.kb.lukasiewicz_implies(list_tokens[0], list_tokens[1], degree)])
            # elif operator == FuzzyDLKeyword.ZADEH_IMPLIES:
            #     return pp.ParseResults([DLParser.kb.zadeh_implies(list_tokens[0], list_tokens[1])])
            # elif operator == FuzzyDLKeyword.KLEENE_DIENES_IMPLIES:
            #     return pp.ParseResults([DLParser.kb.kleene_dienes_implies(list_tokens[0], list_tokens[1], degree)])
            if DLParser.kb.get_logic() == FuzzyLogic.ZADEH:
                return pp.ParseResults(
                    [ImpliesConcept.zadeh_implies(list_tokens[0], list_tokens[1])]
                )
            elif DLParser.kb.get_logic() == FuzzyLogic.CLASSICAL:
                if operator == FuzzyDLKeyword.GOEDEL_IMPLIES:
                    Util.error(
                        "Error: GOEDEL_IMPLIES cannot be used under classical reasoner."
                    )
                elif operator == FuzzyDLKeyword.LUKASIEWICZ_IMPLIES:
                    Util.error(
                        "Error: LUKASIEWICZ_IMPLIES cannot be used under classical reasoner."
                    )
                elif operator == FuzzyDLKeyword.ZADEH_IMPLIES:
                    Util.error(
                        "Error: ZADEH_IMPLIES cannot be used under classical reasoner."
                    )
                elif operator == FuzzyDLKeyword.KLEENE_DIENES_IMPLIES:
                    Util.error(
                        "Error: KLEENE_DIENES_IMPLIES cannot be used under classical reasoner."
                    )
            if operator == FuzzyDLKeyword.GOEDEL_IMPLIES:
                return pp.ParseResults(
                    [ImpliesConcept.goedel_implies(list_tokens[0], list_tokens[1])]
                )
            elif operator == FuzzyDLKeyword.ZADEH_IMPLIES:
                return pp.ParseResults(
                    [ImpliesConcept.zadeh_implies(list_tokens[0], list_tokens[1])]
                )
            elif operator == FuzzyDLKeyword.KLEENE_DIENES_IMPLIES:
                return pp.ParseResults(
                    [
                        ImpliesConcept.kleene_dienes_implies(
                            list_tokens[0], list_tokens[1]
                        )
                    ]
                )
            return pp.ParseResults(
                [ImpliesConcept.lukasiewicz_implies(list_tokens[0], list_tokens[1])]
            )
        elif operator == FuzzyDLKeyword.ALL:
            role: str = list_tokens[1]
            concept: Concept = DLParser._to_concept(list_tokens[2])
            DLParser.kb.check_role(role, concept)
            return pp.ParseResults([AllSomeConcept.all(role, concept)])
        elif operator == FuzzyDLKeyword.SOME:
            c: Concept = DLParser._to_concept(list_tokens[2])
            role: str = list_tokens[1]
            DLParser.kb.check_role(role, c)
            return pp.ParseResults([AllSomeConcept.some(role, c)])
        elif operator == FuzzyDLKeyword.HAS_VALUE:
            ind: Individual = DLParser.kb.get_individual(list_tokens[2])
            DLParser.kb.check_role(role, TruthConcept.get_top())
            return pp.ParseResults([HasValueConcept.has_value(role, ind)])
        elif operator in (
            FuzzyDLKeyword.TIGHT_UPPER_APPROXIMATION,
            FuzzyDLKeyword.TIGHT_LOWER_APPROXIMATION,
            FuzzyDLKeyword.UPPER_APPROXIMATION,
            FuzzyDLKeyword.LOWER_APPROXIMATION,
            FuzzyDLKeyword.LOOSE_UPPER_APPROXIMATION,
            FuzzyDLKeyword.LOOSE_LOWER_APPROXIMATION,
        ):
            role: str = list_tokens[1]
            concept: Concept = DLParser._to_concept(list_tokens[2])
            if role not in DLParser.kb.similarity_relations:
                Util.error(f"Error: Similarity relation {role} has not been defined.")

            if operator == FuzzyDLKeyword.TIGHT_UPPER_APPROXIMATION:
                return pp.ParseResults(
                    [
                        ApproximationConcept.tight_upper_approx(
                            role, concept
                        ).to_all_some_concept()
                    ]
                )
            elif operator == FuzzyDLKeyword.TIGHT_LOWER_APPROXIMATION:
                return pp.ParseResults(
                    [
                        ApproximationConcept.tight_lower_approx(
                            role, concept
                        ).to_all_some_concept()
                    ]
                )
            elif operator == FuzzyDLKeyword.UPPER_APPROXIMATION:
                return pp.ParseResults(
                    [
                        ApproximationConcept.upper_approx(
                            role, concept
                        ).to_all_some_concept()
                    ]
                )
            elif operator == FuzzyDLKeyword.LOWER_APPROXIMATION:
                return pp.ParseResults(
                    [
                        ApproximationConcept.lower_approx(
                            role, concept
                        ).to_all_some_concept()
                    ]
                )
            elif operator == FuzzyDLKeyword.LOOSE_UPPER_APPROXIMATION:
                return pp.ParseResults(
                    [
                        ApproximationConcept.loose_upper_approx(
                            role, concept
                        ).to_all_some_concept()
                    ]
                )
            elif operator == FuzzyDLKeyword.LOOSE_LOWER_APPROXIMATION:
                return pp.ParseResults(
                    [
                        ApproximationConcept.loose_lower_approx(
                            role, concept
                        ).to_all_some_concept()
                    ]
                )
        return tokens

    @staticmethod
    # @pp.trace_parse_action
    def _parse_unary_concept(tokens: pp.ParseResults) -> pp.ParseResults:

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_parse_unary_concept -> {tokens}")
        list_tokens: list[str] = tokens.as_list()
        operator: str = list_tokens[0]
        if operator == FuzzyDLKeyword.NOT:
            concept: Concept = DLParser._to_concept(list_tokens[1])
            return pp.ParseResults([-concept])
        elif operator == FuzzyDLKeyword.SELF:
            role: str = list_tokens[1]
            if role in DLParser.kb.concrete_roles:
                Util.error(f"Error: Role {role} cannot be concrete and abstract.")
            DLParser.kb.abstract_roles.add(role)
            return pp.ParseResults([SelfConcept.self(role)])
        return tokens

    @staticmethod
    # @pp.trace_parse_action
    def _parse_modifier_concept(tokens: pp.ParseResults) -> pp.ParseResults:

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_parse_modifier_concept -> {tokens}")
        list_tokens: list[str] = tokens.as_list()
        mod: Modifier = DLParser._get_modifier(list_tokens[0])
        concept: Concept = DLParser._to_concept(list_tokens[1])
        return pp.ParseResults([mod.modify(concept)])

    @staticmethod
    # @pp.trace_parse_action
    def _parse_threshold_concept(tokens: pp.ParseResults):

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_parse_threshold_concept -> {tokens}")
        list_tokens: list[str] = tokens.as_list()
        operator: str = list_tokens[0]
        concept: Concept = DLParser._to_concept(list_tokens[2])
        DLParser._check_abstract(concept)
        if operator == FuzzyDLKeyword.GREATER_THAN_OR_EQUAL_TO:
            if isinstance(list_tokens[1], (int, float)):
                return pp.ParseResults(
                    [ThresholdConcept.pos_threshold(list_tokens[1], concept)]
                )
            elif isinstance(list_tokens[1], str):
                return pp.ParseResults(
                    [
                        ExtThresholdConcept.extended_pos_threshold(
                            DLParser.kb.milp.get_variable(list_tokens[1]), concept
                        )
                    ]
                )
        elif operator == FuzzyDLKeyword.LESS_THAN_OR_EQUAL_TO:
            if isinstance(list_tokens[1], (int, float)):
                return pp.ParseResults(
                    [ThresholdConcept.neg_threshold(list_tokens[1], concept)]
                )
            elif isinstance(list_tokens[1], str):
                return pp.ParseResults(
                    [
                        ExtThresholdConcept.extended_neg_threshold(
                            DLParser.kb.milp.get_variable(list_tokens[1]), concept
                        )
                    ]
                )
        elif operator == FuzzyDLKeyword.EQUALS:
            if isinstance(list_tokens[1], (int, float)):
                return pp.ParseResults([ThresholdConcept.ea(list_tokens[1], concept)])
            elif isinstance(list_tokens[1], str):
                return pp.ParseResults(
                    [
                        ExtThresholdConcept.extended_neg_threshold(
                            DLParser.kb.milp.get_variable(list_tokens[1]), concept
                        )
                    ]
                )
        return tokens

    @staticmethod
    # @pp.trace_parse_action
    def _parse_weighted_concept_simple(tokens: pp.ParseResults) -> pp.ParseResults:

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_parse_weighted_concept_simple -> {tokens}")
        list_tokens: list[str] = tokens.as_list()
        weight: float = list_tokens[0]
        concept: Concept = DLParser._to_concept(list_tokens[1])
        return pp.ParseResults([WeightedConcept(weight, concept)])

    @staticmethod
    # @pp.trace_parse_action
    def _parse_weighted_concept(tokens: pp.ParseResults) -> pp.ParseResults:

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_parse_weighted_concept -> {tokens}")
        list_tokens: list[str] = tokens.as_list()
        operator: str = list_tokens[0]
        assert all(isinstance(c, WeightedConcept) for c in list_tokens[1:])
        weights: list[float] = list(map(lambda x: x.weight, list_tokens[1:]))
        concepts: list[Concept] = [
            DLParser._to_concept(w_concept.curr_concept)
            for w_concept in list_tokens[1:]
        ]
        if operator == FuzzyDLKeyword.W_SUM:
            if not (sum(weights) <= 1.0):
                Util.error(
                    "Error: The sum of the weights must be lower than or equal to 1."
                )
            return pp.ParseResults([WeightedSumConcept(weights, concepts)])
        elif operator == FuzzyDLKeyword.W_MAX:
            if max(weights) != 1.0:
                Util.error("Error: The maximum of the weights must be equal to 1.")
            return pp.ParseResults([WeightedMaxConcept(weights, concepts)])
        elif operator == FuzzyDLKeyword.W_MIN:
            if max(weights) != 1.0:
                Util.error("Error: The maximum of the weights must be equal to 1.")
            return pp.ParseResults([WeightedMinConcept(weights, concepts)])
        elif operator == FuzzyDLKeyword.W_SUM_ZERO:
            if not (sum(weights) <= 1.0):
                Util.error(
                    "Error: The sum of the weights must be lower than or equal to 1."
                )
            return pp.ParseResults([WeightedSumZeroConcept(weights, concepts)])
        return tokens

    @staticmethod
    # @pp.trace_parse_action
    def _parse_q_owa_concept(tokens: pp.ParseResults) -> pp.ParseResults:

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_parse_q_owa_concept -> {tokens}")
        list_tokens: list[str] = tokens.as_list()
        f: FuzzyConcreteConcept = DLParser.kb.concrete_concepts.get(list_tokens[0])
        if f is None:
            Util.error(f"Error: Fuzzy concept {f} has to be defined before being used.")
        if not isinstance(f, (RightConcreteConcept, LeftConcreteConcept)):
            Util.error(
                f"Error: Fuzzy concept {f} has to be a right or a linear function."
            )
        concepts: list[Concept] = [
            DLParser._to_concept(concept) for concept in list_tokens[1:]
        ]
        return pp.ParseResults([QowaConcept(f, concepts)])

    @staticmethod
    # @pp.trace_parse_action
    def _parse_owa_integral_concept(tokens: pp.ParseResults) -> pp.ParseResults:

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_parse_owa_integral_concept -> {tokens}")
        list_tokens: list[str] = tokens.as_list()
        operator: str = list_tokens[0]
        length: int = len(list_tokens) - 1
        assert length % 2 == 0
        weights: list[float] = list_tokens[1:][: length // 2]
        concepts: list[Concept] = [
            DLParser._to_concept(concept) for concept in list_tokens[1:][length // 2 :]
        ]
        if operator == FuzzyDLKeyword.OWA:
            if sum(weights) != 1.0:
                Util.error("Error: The sum of the weights must be equal to 1.")
            return pp.ParseResults([OwaConcept(weights, concepts)])
        elif operator == FuzzyDLKeyword.CHOQUET:
            if max(weights) != 1.0:
                Util.error("Error: The maximum of the weights must be equal to 1.")
            return pp.ParseResults([ChoquetIntegral(weights, concepts)])
        elif operator == FuzzyDLKeyword.SUGENO:
            if max(weights) != 1.0:
                Util.error("Error: The maximum of the weights must be equal to 1.")
            return pp.ParseResults([SugenoIntegral(weights, concepts)])
        elif operator == FuzzyDLKeyword.QUASI_SUGENO:
            if max(weights) != 1.0:
                Util.error("Error: The maximum of the weights must be equal to 1.")
            return pp.ParseResults([QsugenoIntegral(weights, concepts)])
        return tokens

    @staticmethod
    # @pp.trace_parse_action
    def _parse_modifier(tokens: pp.ParseResults) -> pp.ParseResults:

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_parse_modifier -> {tokens}")

        list_tokens: list[str] = tokens.as_list()
        if list_tokens[1] == FuzzyDLKeyword.LINEAR_MODIFIER:
            DLParser.kb.add_modifier(
                list_tokens[0], LinearModifier(list_tokens[0], list_tokens[2])
            )
        elif list_tokens[1] == FuzzyDLKeyword.TRIANGULAR_MODIFIER:
            DLParser.kb.add_modifier(
                list_tokens[0],
                TriangularModifier(
                    list_tokens[0], list_tokens[2], list_tokens[3], list_tokens[4]
                ),
            )
        return tokens

    @staticmethod
    # @pp.trace_parse_action
    def _parse_truth_constants(tokens: pp.ParseResults) -> pp.ParseResults:

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_parse_truth_constants -> {tokens}")
        list_tokens: list[str] = tokens.as_list()
        DLParser.kb.set_truth_constants(list_tokens[0], list_tokens[1])
        return tokens

    @staticmethod
    # @pp.trace_parse_action
    def _parse_fuzzy_concept(tokens: pp.ParseResults) -> pp.ParseResults:

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_parse_fuzzy_concept -> {tokens}")
        list_tokens: list = tokens.as_list()
        if DLParser.kb.concrete_concepts.get(list_tokens[0]) is not None:
            Util.error(
                f"Error: Fuzzy concept {list_tokens[0]} has to be defined before being used."
            )
        if (
            list_tokens[1] != FuzzyDLKeyword.CRISP
            and DLParser.kb.get_logic() == FuzzyLogic.CLASSICAL
        ):
            Util.error(
                f"Error: Fuzzy concept {list_tokens[0]} cannot be used with the classical reasoner."
            )
        if list_tokens[1] == FuzzyDLKeyword.CRISP:
            DLParser.kb.add_concept(
                list_tokens[0],
                CrispConcreteConcept(
                    list_tokens[0],
                    list_tokens[2],
                    list_tokens[3],
                    list_tokens[4],
                    list_tokens[5],
                ),
            )
        elif list_tokens[1] == FuzzyDLKeyword.LEFT_SHOULDER:
            DLParser.kb.add_concept(
                list_tokens[0],
                LeftConcreteConcept(
                    list_tokens[0],
                    list_tokens[2],
                    list_tokens[3],
                    list_tokens[4],
                    list_tokens[5],
                ),
            )
            DLParser.kb.concrete_fuzzy_concepts = True
        elif list_tokens[1] == FuzzyDLKeyword.RIGHT_SHOULDER:
            DLParser.kb.add_concept(
                list_tokens[0],
                RightConcreteConcept(
                    list_tokens[0],
                    list_tokens[2],
                    list_tokens[3],
                    list_tokens[4],
                    list_tokens[5],
                ),
            )
            DLParser.kb.concrete_fuzzy_concepts = True
        elif list_tokens[1] == FuzzyDLKeyword.TRIANGULAR:
            DLParser.kb.add_concept(
                list_tokens[0],
                TriangularConcreteConcept(
                    list_tokens[0],
                    list_tokens[2],
                    list_tokens[3],
                    list_tokens[4],
                    list_tokens[5],
                    list_tokens[6],
                ),
            )
            DLParser.kb.concrete_fuzzy_concepts = True
        elif list_tokens[1] == FuzzyDLKeyword.TRAPEZOIDAL:
            DLParser.kb.add_concept(
                list_tokens[0],
                TrapezoidalConcreteConcept(
                    list_tokens[0],
                    list_tokens[2],
                    list_tokens[3],
                    list_tokens[4],
                    list_tokens[5],
                    list_tokens[6],
                    list_tokens[7],
                ),
            )
            DLParser.kb.concrete_fuzzy_concepts = True
        elif list_tokens[1] == FuzzyDLKeyword.LINEAR:
            DLParser.kb.add_concept(
                list_tokens[0],
                LinearConcreteConcept(
                    list_tokens[0],
                    list_tokens[2],
                    list_tokens[3],
                    list_tokens[4],
                    list_tokens[5],
                ),
            )
            DLParser.kb.concrete_fuzzy_concepts = True
        elif list_tokens[1] == FuzzyDLKeyword.MODIFIED:
            mod: Modifier = DLParser._get_modifier(list_tokens[2])
            if DLParser.kb.concrete_concepts.get(list_tokens[3]) is None:
                Util.error(
                    f"Error: Fuzzy concept {list_tokens[3]} has to be defined before being used."
                )
            DLParser.kb.add_concept(
                list_tokens[0],
                ModifiedConcreteConcept(
                    list_tokens[0],
                    mod,
                    DLParser.kb.concrete_concepts.get(list_tokens[3]),
                ),
            )
            DLParser.kb.concrete_fuzzy_concepts = True
        return tokens

    @staticmethod
    # @pp.trace_parse_action
    def _parse_fuzzy_number_range(tokens: pp.ParseResults) -> pp.ParseResults:

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_parse_fuzzy_number_range -> {tokens}")
        tokens = tokens.as_list()
        TriangularFuzzyNumber.set_range(tokens[0], tokens[1])
        return pp.ParseResults(tokens)

    @staticmethod
    # @pp.trace_parse_action
    def _create_fuzzy_number(tokens: pp.ParseResults) -> pp.ParseResults:

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_create_fuzzy_number -> {tokens}")
        tokens = tokens.as_list()
        if len(tokens) == 1:
            if isinstance(tokens[0], (int, float)):
                return pp.ParseResults(
                    [TriangularFuzzyNumber(tokens[0], tokens[0], tokens[0])]
                )
            elif tokens[0] == str:
                if tokens[0] not in DLParser.kb.fuzzy_numbers:
                    Util.error(
                        f"Error: Fuzzy number {tokens[0]} has to be defined before being used."
                    )
                return pp.ParseResults([DLParser.kb.fuzzy_numbers.get(tokens[0])])
        elif all(isinstance(t, (int, float)) for t in tokens):
            return pp.ParseResults(
                [TriangularFuzzyNumber(tokens[0], tokens[1], tokens[2])]
            )
        return pp.ParseResults(tokens)

    @staticmethod
    # @pp.trace_parse_action
    def _set_fuzzy_number(tokens: pp.ParseResults) -> pp.ParseResults:

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_set_fuzzy_number -> {tokens}")
        tokens = tokens.as_list()
        if tokens[0] in DLParser.kb.fuzzy_numbers:
            Util.error(f"Error: Fuzzy number {tokens[0]} has already been defined.")
        for i in range(2, len(tokens)):
            if isinstance(tokens[i], str):
                tokens[i] = DLParser.kb.fuzzy_numbers.get(tokens[i])
        if isinstance(tokens[1], TriangularFuzzyNumber):
            DLParser.kb.add_fuzzy_number(tokens[0], tokens[1])
            DLParser.kb.concrete_fuzzy_concepts = True
            return pp.ParseResults([tokens[1]])
        elif tokens[1] in (FuzzyDLKeyword.FEATURE_SUM, FuzzyDLKeyword.FEATURE_MUL):
            ts: TriangularFuzzyNumber = [
                typing.cast(TriangularFuzzyNumber, t) for t in tokens[2:]
            ]
            result: TriangularFuzzyNumber = reduce(
                (
                    TriangularFuzzyNumber.add
                    if tokens[1] == FuzzyDLKeyword.FEATURE_SUM
                    else TriangularFuzzyNumber.times
                ),
                ts,
            )
            DLParser.kb.add_fuzzy_number(
                tokens[0],
                result,
            )
            DLParser.kb.concrete_fuzzy_concepts = True
            return pp.ParseResults([result])
        elif tokens[1] in (FuzzyDLKeyword.FEATURE_SUB, FuzzyDLKeyword.FEATURE_DIV):
            t1: TriangularFuzzyNumber = typing.cast(TriangularFuzzyNumber, tokens[2])
            t2: TriangularFuzzyNumber = typing.cast(TriangularFuzzyNumber, tokens[3])
            result: TriangularFuzzyNumber = (
                t1 - t2 if tokens[1] == FuzzyDLKeyword.FEATURE_SUB else t1 / t2
            )
            DLParser.kb.add_fuzzy_number(
                tokens[0],
                result,
            )
            DLParser.kb.concrete_fuzzy_concepts = True
            return pp.ParseResults([result])
        return pp.ParseResults(tokens)

    @staticmethod
    # @pp.trace_parse_action
    def _parse_feature(tokens: pp.ParseResults) -> pp.ParseResults:

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_parse_feature -> {tokens}")
        tokens = tokens.as_list()
        role: str = tokens[1]
        if tokens[2] == FuzzyDLKeyword.INTEGER:
            DLParser.kb.define_integer_concrete_feature(
                role, int(tokens[3]), int(tokens[4])
            )
        elif tokens[2] == FuzzyDLKeyword.REAL:
            DLParser.kb.define_real_concrete_feature(
                role, float(tokens[3]), float(tokens[4])
            )
        elif tokens[2] == FuzzyDLKeyword.BOOLEAN:
            DLParser.kb.define_boolean_concrete_feature(role)
        elif tokens[2] == FuzzyDLKeyword.STRING:
            DLParser.kb.define_string_concrete_feature(role)
        return pp.ParseResults(tokens)

    def _parse_restrictions(tokens: pp.ParseResults) -> typing.Any:

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_parse_restrictions -> {tokens}")
        tokens = tokens.as_list()
        if isinstance(tokens[0], (list, tuple)):
            tokens = tokens[0]
        if len(tokens) == 1:
            if isinstance(tokens[0], str) or isinstance(tokens[0], constants.NUMBER):
                return pp.ParseResults([FeatureFunction(tokens[0])])
        elif len(tokens) == 2 and isinstance(tokens[0], (int, float)):
            return pp.ParseResults(
                [FeatureFunction(tokens[0], FeatureFunction(tokens[1]))]
            )
        elif len(tokens) >= 3:
            if FuzzyDLKeyword.MUL.get_value() in tokens:
                return pp.ParseResults(
                    [FeatureFunction(tokens[0], FeatureFunction(tokens[2]))]
                )
            elif FuzzyDLKeyword.SUB.get_value() in tokens:
                return pp.ParseResults(
                    [
                        FeatureFunction(
                            FeatureFunction(tokens[0]), FeatureFunction(tokens[2])
                        )
                    ]
                )
            elif FuzzyDLKeyword.SUM.get_value() in tokens:
                return pp.ParseResults(
                    [FeatureFunction(list(map(FeatureFunction, tokens[::2])))]
                )
        return pp.ParseResults(tokens)

    @staticmethod
    # @pp.trace_parse_action
    def _parse_datatype_restriction(tokens: pp.ParseResults) -> pp.ParseResults:

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_parse_datatype_restriction -> {tokens}")
        list_tokens = tokens.as_list()
        role: str = list_tokens[1]
        if role not in DLParser.kb.concrete_features:
            Util.error(f"Error: Feature {role} has not been defined.")
        restriction_type: RestrictionType = RestrictionType.EXACT_VALUE
        if list_tokens[0] == FuzzyDLKeyword.LESS_THAN_OR_EQUAL_TO:
            restriction_type = RestrictionType.AT_MOST_VALUE
        elif list_tokens[0] == FuzzyDLKeyword.GREATER_THAN_OR_EQUAL_TO:
            restriction_type = RestrictionType.AT_LEAST_VALUE
        if isinstance(list_tokens[2], str):
            # if tokens.as_dict().get("string") == tokens[2] and not DLParser.kb.check_fuzzy_number_concept_exists(list_tokens[2]):
            #     return pp.ParseResults(
            #         [DLParser.kb.add_datatype_restriction(restriction_type, list_tokens[2], role)]
            #     )
            # else:
            if DLParser.kb.check_fuzzy_number_concept_exists(list_tokens[2]):
                return pp.ParseResults(
                    [
                        DLParser.kb.add_datatype_restriction(
                            restriction_type,
                            DLParser.kb.get_concept(list_tokens[2]),
                            role,
                        )
                    ]
                )
            else:
                v: Variable = Variable(list_tokens[2], VariableType.CONTINUOUS)
                return pp.ParseResults(
                    [DLParser.kb.add_datatype_restriction(restriction_type, v, role)]
                )
        elif isinstance(list_tokens[2], TriangularFuzzyNumber):
            if not TriangularFuzzyNumber.has_defined_range():
                Util.error(
                    "Error: The range of the fuzzy numbers has to be defined before being used."
                )
            if list_tokens[2].is_number():
                return pp.ParseResults(
                    [
                        DLParser.kb.add_datatype_restriction(
                            restriction_type, list_tokens[2].get_a(), role
                        )
                    ]
                )
            else:
                return pp.ParseResults(
                    [
                        DLParser.kb.add_datatype_restriction(
                            restriction_type, list_tokens[2], role
                        )
                    ]
                )
        elif isinstance(list_tokens[2], FeatureFunction):
            return pp.ParseResults(
                [
                    DLParser.kb.add_datatype_restriction(
                        restriction_type, list_tokens[2], role
                    )
                ]
            )
        return tokens

    @staticmethod
    # @pp.trace_parse_action
    def _parse_term(tokens: pp.ParseResults) -> pp.ParseResults:

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_parse_term -> {tokens}")
        list_tokens: list = tokens.as_list()[0]
        if len(list_tokens) == 1:
            return pp.ParseResults(
                [Term(1.0, DLParser.kb.milp.get_variable(list_tokens[0]))]
            )
        elif len(list_tokens) == 3:
            return pp.ParseResults(
                [Term(list_tokens[0], DLParser.kb.milp.get_variable(list_tokens[2]))]
            )
        return tokens

    @staticmethod
    # @pp.trace_parse_action
    def _parse_expression(tokens: pp.ParseResults) -> pp.ParseResults:

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_parse_expression -> {tokens}")
        list_tokens: list = tokens.as_list()
        expr: Expression = Expression(0)
        if isinstance(list_tokens[0], (tuple, list)):
            list_tokens = list_tokens[0]
        if len(list_tokens) == 1 and isinstance(list_tokens[0], Term):
            expr.add_term(list_tokens[0])
            return expr
        if "+" in list_tokens and all(
            isinstance(term, Term) for term in list_tokens[::2]
        ):
            for term in list_tokens[::2]:
                expr.add_term(term)
            return pp.ParseResults([expr])
        return tokens

    @staticmethod
    # @pp.trace_parse_action
    def _parse_inequation(tokens: pp.ParseResults) -> pp.ParseResults:

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_parse_inequation -> {tokens}")
        list_tokens: list = tokens.as_list()
        if isinstance(list_tokens[0], Expression):
            operator: str = list_tokens[1]
            constant: int | float = list_tokens[2]
            expr: Expression = list_tokens[0] - constant
            operator_type: InequalityType = (
                InequalityType.EQUAL
                if operator == FuzzyDLKeyword.EQUALS
                else (
                    InequalityType.GREATER_THAN
                    if operator == FuzzyDLKeyword.GREATER_THAN_OR_EQUAL_TO
                    else InequalityType.LESS_THAN
                )
            )
            DLParser.kb.milp.add_new_constraint(expr, operator_type)
            return pp.ParseResults([Inequation(expr, operator_type)])
        return tokens

    @staticmethod
    # @pp.trace_parse_action
    def _parse_constraints(tokens: pp.ParseResults) -> pp.ParseResults:

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_parse_constraints -> {tokens}")
        list_tokens: list = tokens.as_list()
        if list_tokens[0] == FuzzyDLKeyword.BINARY:
            v: Variable = DLParser.kb.milp.get_variable(list_tokens[1])
            v.set_type(VariableType.BINARY)
        elif list_tokens[0] == FuzzyDLKeyword.FREE:
            v: Variable = DLParser.kb.milp.get_variable(list_tokens[1])
            v.set_type(VariableType.CONTINUOUS)
        return tokens

    @staticmethod
    # @pp.trace_parse_action
    def _show_concrete_fillers(tokens: pp.ParseResults) -> pp.ParseResults:

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_show_concrete_fillers -> {tokens}")
        list_tokens: list = tokens.as_list()
        for role in list_tokens:
            if role in DLParser.kb.concrete_roles:
                DLParser.kb.milp.show_vars.add_concrete_filler_to_show(role)
            else:
                Util.error(
                    "Error: show-concrete-fillers can only be used with concrete roles."
                )
        return tokens

    @staticmethod
    # @pp.trace_parse_action
    def _show_concrete_fillers_for(tokens: pp.ParseResults) -> pp.ParseResults:

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_show_concrete_fillers_for -> {tokens}")
        list_tokens: list = tokens.as_list()
        ind_name: str = list_tokens[0]
        for role in list_tokens[1:]:
            if role in DLParser.kb.concrete_roles:
                DLParser.kb.milp.show_vars.add_concrete_filler_to_show(role, ind_name)
            else:
                Util.error(
                    "Error: show-concrete-fillers-for can only be used with concrete roles."
                )
        return tokens

    @staticmethod
    # @pp.trace_parse_action
    def _show_concrete_instance_for(tokens: pp.ParseResults) -> pp.ParseResults:

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_show_concrete_instance_for -> {tokens}")
        list_tokens: list = tokens.as_list()
        ind_name: str = list_tokens[0]
        role: str = list_tokens[1]
        if role not in DLParser.kb.concrete_roles:
            Util.error(
                "Error: show-concrete-instance-for can only be used with concrete roles."
            )
        ar: list[FuzzyConcreteConcept] = []
        for c_name in list_tokens[2:]:
            concept: Concept = DLParser.kb.concrete_concepts.get(c_name)
            if concept is None:
                Util.error(
                    f"Error: Concrete fuzzy concept {c_name} has not been defined."
                )
            if concept.type not in (ConceptType.CONCRETE, ConceptType.FUZZY_NUMBER):
                Util.error(f"Error: {c_name} is not a concrete fuzzy concept.")
            ar.append(typing.cast(FuzzyConcreteConcept, concept))
        DLParser.kb.milp.show_vars.add_concrete_filler_to_show(role, ind_name, ar)
        return tokens

    @staticmethod
    # @pp.trace_parse_action
    def _show_abstract_fillers(tokens: pp.ParseResults) -> pp.ParseResults:

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_show_abstract_fillers -> {tokens}")
        list_tokens: list = tokens.as_list()
        for role in list_tokens:
            if role in DLParser.kb.concrete_roles:
                Util.error(
                    "Error: show-abstract-fillers can only be used with abstract roles."
                )
                continue
            DLParser.kb.milp.show_vars.add_abstract_filler_to_show(role)
        return tokens

    @staticmethod
    # @pp.trace_parse_action
    def _show_abstract_fillers_for(tokens: pp.ParseResults) -> pp.ParseResults:

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_show_abstract_fillers_for -> {tokens}")
        list_tokens: list = tokens.as_list()
        ind_name: str = list_tokens[1:]
        for role in list_tokens:
            if role in DLParser.kb.concrete_roles:
                Util.error(
                    "Error: show-abstract-fillers-for can only be used with abstract roles."
                )
            DLParser.kb.milp.show_vars.add_abstract_filler_to_show(role, ind_name)
        return tokens

    @staticmethod
    # @pp.trace_parse_action
    def _show_concepts(tokens: pp.ParseResults) -> pp.ParseResults:

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_show_concepts -> {tokens}")
        list_tokens: list = tokens.as_list()
        for ind_name in list_tokens:
            DLParser.kb.milp.show_vars.add_individual_to_show(ind_name)
        return tokens

    @staticmethod
    # @pp.trace_parse_action
    def _show_instances(tokens: pp.ParseResults) -> pp.ParseResults:

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_show_instances -> {tokens}")
        list_tokens: list = tokens.as_list()
        for concept in list_tokens:
            concept: Concept = DLParser._to_concept(concept)
            DLParser.kb.milp.show_vars.add_concept_to_show(str(concept))
        return tokens

    @staticmethod
    # @pp.trace_parse_action
    def _show_variables(tokens: pp.ParseResults) -> pp.ParseResults:

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_show_variables -> {tokens}")
        list_tokens: list = tokens.as_list()
        for variable_name in list_tokens:
            var: Variable = DLParser.kb.milp.get_variable(variable_name)
            DLParser.kb.milp.show_vars.add_variable(var, str(var))
        return tokens

    @staticmethod
    # @pp.trace_parse_action
    def _show_languages(tokens: pp.ParseResults) -> pp.ParseResults:

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_show_languages -> {tokens}")
        DLParser.kb.show_language = True
        return tokens

    @staticmethod
    # @pp.trace_parse_action
    def _parse_crisp_declarations(tokens: pp.ParseResults) -> pp.ParseResults:

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_parse_crisp_declarations -> {tokens}")
        list_tokens: list = tokens.as_list()
        if list_tokens[0] == FuzzyDLKeyword.CRISP_CONCEPT:
            for concept in list_tokens[1:]:
                concept: Concept = DLParser._to_concept(concept)
                DLParser.kb.set_crisp_concept(concept)
        elif list_tokens[0] == FuzzyDLKeyword.CRISP_ROLE:
            for role in list_tokens[1:]:
                DLParser.kb.set_crisp_role(role)
        return tokens

    @staticmethod
    # @pp.trace_parse_action
    def _parse_fuzzy_similarity(tokens: pp.ParseResults) -> pp.ParseResults:

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_parse_fuzzy_similarity -> {tokens}")
        list_tokens: list = tokens.as_list()
        DLParser.kb.add_similarity_relation(list_tokens[0])
        return tokens

    @staticmethod
    # @pp.trace_parse_action
    def _parse_fuzzy_equivalence(tokens: pp.ParseResults) -> pp.ParseResults:

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_parse_fuzzy_equivalence -> {tokens}")
        list_tokens: list = tokens.as_list()
        DLParser.kb.add_equivalence_relation(list_tokens[0])
        return tokens

    @staticmethod
    # @pp.trace_parse_action
    def _parse_degree(tokens: pp.ParseResults) -> pp.ParseResults:

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_parse_degree -> {tokens}")

        list_tokens: list = tokens.as_list()
        if isinstance(list_tokens[0], (int, float)):
            return pp.ParseResults([DegreeNumeric.get_degree(float(list_tokens[0]))])
        elif isinstance(list_tokens[0], Expression):
            return pp.ParseResults([DegreeExpression.get_degree(list_tokens[0])])
        elif isinstance(list_tokens[0], str):
            tc: typing.Optional[float] = DLParser.kb.get_truth_constants(list_tokens[0])
            if tc is not None:
                return pp.ParseResults([DegreeNumeric.get_degree(float(tc))])
            else:
                return pp.ParseResults(
                    [
                        DegreeVariable.get_degree(
                            DLParser.kb.milp.get_variable(list_tokens[0])
                        )
                    ]
                )
        return tokens

    @staticmethod
    # @pp.trace_parse_action
    def _parse_axioms(tokens: pp.ParseResults) -> pp.ParseResults:

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_parse_axioms -> {tokens}")

        list_tokens: list = tokens.as_list()[0]
        if list_tokens[0] == FuzzyDLKeyword.INSTANCE:
            a: Individual = DLParser.kb.get_individual(list_tokens[1])
            c: Concept = DLParser._to_concept(list_tokens[2])
            d: Degree = (
                list_tokens[3]
                if len(list_tokens) > 3
                else DegreeNumeric.get_degree(1.0)
            )
            DLParser.kb.add_assertion(a, c, d)
        elif list_tokens[0] == FuzzyDLKeyword.RELATED:
            a: Individual = DLParser.kb.get_individual(list_tokens[1])
            b: Individual = DLParser.kb.get_individual(list_tokens[2])
            role: str = list_tokens[3]
            d: Degree = (
                list_tokens[4]
                if len(list_tokens) > 4
                else DegreeNumeric.get_degree(1.0)
            )
            if role in DLParser.kb.concrete_roles:
                Util.error(f"Error: Role {role} cannot be concrete and abstract.")
            DLParser.kb.add_relation(a, role, b, d)
        elif list_tokens[0] in (
            FuzzyDLKeyword.GOEDEL_IMPLIES,
            FuzzyDLKeyword.LUKASIEWICZ_IMPLIES,
            FuzzyDLKeyword.KLEENE_DIENES_IMPLIES,
            FuzzyDLKeyword.ZADEH_IMPLIES,
            FuzzyDLKeyword.IMPLIES,
        ):
            c1: Concept = DLParser._to_concept(list_tokens[1])
            c2: Concept = DLParser._to_concept(list_tokens[2])
            d: Degree = (
                list_tokens[3]
                if len(list_tokens) > 3
                else DegreeNumeric.get_degree(1.0)
            )
            if list_tokens[0] == FuzzyDLKeyword.IMPLIES:
                DLParser.kb.implies(c1, c2, d)
            elif list_tokens[0] == FuzzyDLKeyword.GOEDEL_IMPLIES:
                DLParser.kb.goedel_implies(c1, c2, d)
            elif list_tokens[0] == FuzzyDLKeyword.LUKASIEWICZ_IMPLIES:
                DLParser.kb.lukasiewicz_implies(c1, c2, d)
            elif list_tokens[0] == FuzzyDLKeyword.KLEENE_DIENES_IMPLIES:
                DLParser.kb.kleene_dienes_implies(c1, c2, d)
            elif list_tokens[0] == FuzzyDLKeyword.ZADEH_IMPLIES:
                DLParser.kb.zadeh_implies(c1, c2)
        elif list_tokens[0] == FuzzyDLKeyword.ZADEH_IMPLIES:
            c1: Concept = DLParser._to_concept(list_tokens[1])
            c2: Concept = DLParser._to_concept(list_tokens[2])
            DLParser.kb.zadeh_implies(c1, c2)
        elif list_tokens[0] == FuzzyDLKeyword.DEFINE_CONCEPT:
            name: str = list_tokens[1]
            c: Concept = DLParser._to_concept(list_tokens[2])
            DLParser.kb.define_concept(name, c)
        elif list_tokens[0] == FuzzyDLKeyword.DEFINE_PRIMITIVE_CONCEPT:
            name: str = list_tokens[1]
            c: Concept = DLParser._to_concept(list_tokens[2])
            DLParser.kb.define_atomic_concept(name, c, LogicOperatorType.ZADEH, 1.0)
        elif list_tokens[0] == FuzzyDLKeyword.EQUIVALENT_CONCEPTS:
            c1: Concept = DLParser._to_concept(list_tokens[1])
            c2: Concept = DLParser._to_concept(list_tokens[2])
            DLParser.kb.define_equivalent_concepts(c1, c2)
        elif list_tokens[0] == FuzzyDLKeyword.DISJOINT_UNION:
            concepts: list[str] = [
                str(DLParser._to_concept(t)) for t in list_tokens[1:]
            ]
            DLParser.kb.add_disjoint_union_concept(concepts)
        elif list_tokens[0] == FuzzyDLKeyword.DISJOINT:
            concepts: list[Concept] = [DLParser._to_concept(t) for t in list_tokens[1:]]
            DLParser.kb.add_concepts_disjoint(concepts)
        elif list_tokens[0] in (FuzzyDLKeyword.RANGE, FuzzyDLKeyword.DOMAIN):
            role: str = list_tokens[1]
            concept: Concept = DLParser._to_concept(list_tokens[2])
            if list_tokens[0] == FuzzyDLKeyword.RANGE:
                DLParser.kb.check_role(role, concept)
                DLParser.kb.role_range(role, concept)
            else:
                DLParser.kb.role_domain(role, concept)
        elif list_tokens[0] == FuzzyDLKeyword.FUNCTIONAL:
            role: str = list_tokens[1]
            DLParser.kb.role_is_functional(role)
        elif list_tokens[0] == FuzzyDLKeyword.TRANSITIVE:
            role: str = list_tokens[1]
            DLParser.kb.role_is_transitive(role)
        elif list_tokens[0] == FuzzyDLKeyword.SYMMETRIC:
            role: str = list_tokens[1]
            DLParser.kb.role_is_symmetric(role)
        elif list_tokens[0] == FuzzyDLKeyword.REFLEXIVE:
            role: str = list_tokens[1]
            DLParser.kb.role_is_reflexive(role)
        elif list_tokens[0] == FuzzyDLKeyword.INVERSE_FUNCTIONAL:
            role: str = list_tokens[1]
            if role in DLParser.kb.concrete_roles:
                Util.error(f"Error: Concrete role {role} cannot have an inverse role.")
            DLParser.kb.role_is_inverse_functional(role)
        elif list_tokens[0] == FuzzyDLKeyword.INVERSE:
            role: str = list_tokens[1]
            inv_role: str = list_tokens[2]
            if role in DLParser.kb.concrete_roles:
                Util.error(f"Error: Concrete role {role} cannot have an inverse role.")
            elif inv_role in DLParser.kb.concrete_roles:
                Util.error(
                    f"Error: Concrete role {inv_role} cannot have an inverse role."
                )
            else:
                DLParser.kb.add_inverse_roles(role, inv_role)
        elif list_tokens[0] == FuzzyDLKeyword.IMPLIES_ROLE:
            role_c: str = list_tokens[1]
            role_p: str = list_tokens[2]
            d: float = list_tokens[3] if len(list_tokens) > 3 else 1.0
            DLParser.kb.role_implies(role_c, role_p, d)
        return tokens

    @staticmethod
    # @pp.trace_parse_action
    def _parse_queries(tokens: pp.ParseResults) -> pp.ParseResults:

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_parse_queries -> {tokens}")

        list_tokens: list[str] = tokens.as_list()[0]

        if list_tokens[0] == FuzzyDLKeyword.ALL_INSTANCES_QUERY:
            DLParser.queries_list.append(AllInstancesQuery(list_tokens[1]))
        elif list_tokens[0] == FuzzyDLKeyword.SAT_QUERY:
            DLParser.queries_list.append(KbSatisfiableQuery())
        elif list_tokens[0] in (
            FuzzyDLKeyword.MIN_SAT_QUERY,
            FuzzyDLKeyword.MAX_SAT_QUERY,
        ):
            _class: Query = (
                MinSatisfiableQuery
                if list_tokens[0] == FuzzyDLKeyword.MIN_SAT_QUERY
                else MaxSatisfiableQuery
            )
            c: Concept = DLParser._to_concept(list_tokens[1])
            if len(list_tokens) > 2:
                DLParser.queries_list.append(
                    _class(c, DLParser.kb.get_individual(list_tokens[2]))
                )
            else:
                DLParser.queries_list.append(_class(c))
        elif list_tokens[0] in (
            FuzzyDLKeyword.MAX_INSTANCE_QUERY,
            FuzzyDLKeyword.MIN_INSTANCE_QUERY,
        ):
            _class: Query = (
                MaxInstanceQuery
                if list_tokens[0] == FuzzyDLKeyword.MAX_INSTANCE_QUERY
                else MinInstanceQuery
            )
            a: Individual = DLParser.kb.get_individual(list_tokens[1])
            c: Concept = DLParser._to_concept(list_tokens[2])
            DLParser.queries_list.append(_class(c, a))
        elif list_tokens[0] in (
            FuzzyDLKeyword.MAX_SUBS_QUERY,
            FuzzyDLKeyword.MIN_SUBS_QUERY,
            FuzzyDLKeyword.MAX_G_SUBS_QUERY,
            FuzzyDLKeyword.MIN_G_SUBS_QUERY,
            FuzzyDLKeyword.MAX_L_SUBS_QUERY,
            FuzzyDLKeyword.MIN_L_SUBS_QUERY,
            FuzzyDLKeyword.MAX_KD_SUBS_QUERY,
            FuzzyDLKeyword.MIN_KD_SUBS_QUERY,
        ):
            _class = (
                MaxSubsumesQuery
                if list_tokens[0].lower().startswith("max")
                else MinSubsumesQuery
            )
            c1: Concept = DLParser._to_concept(list_tokens[1])
            c2: Concept = DLParser._to_concept(list_tokens[2])
            if list_tokens[0] in (
                FuzzyDLKeyword.MAX_SUBS_QUERY,
                FuzzyDLKeyword.MIN_SUBS_QUERY,
            ):
                if DLParser.kb.get_logic() == FuzzyLogic.LUKASIEWICZ:
                    DLParser.queries_list.append(
                        _class(c1, c2, LogicOperatorType.LUKASIEWICZ)
                    )
                else:
                    DLParser.queries_list.append(
                        _class(c1, c2, LogicOperatorType.ZADEH)
                    )
            elif list_tokens[0] in (
                FuzzyDLKeyword.MAX_G_SUBS_QUERY,
                FuzzyDLKeyword.MIN_G_SUBS_QUERY,
            ):
                DLParser.queries_list.append(_class(c1, c2, LogicOperatorType.GOEDEL))
            elif list_tokens[0] in (
                FuzzyDLKeyword.MAX_L_SUBS_QUERY,
                FuzzyDLKeyword.MIN_L_SUBS_QUERY,
            ):
                DLParser.queries_list.append(
                    _class(c1, c2, LogicOperatorType.LUKASIEWICZ)
                )
            elif list_tokens[0] in (
                FuzzyDLKeyword.MAX_KD_SUBS_QUERY,
                FuzzyDLKeyword.MIN_KD_SUBS_QUERY,
            ):
                DLParser.queries_list.append(
                    _class(c1, c2, LogicOperatorType.KLEENE_DIENES)
                )
        elif list_tokens[0] in (
            FuzzyDLKeyword.MAX_RELATED_QUERY,
            FuzzyDLKeyword.MIN_RELATED_QUERY,
        ):
            a: Individual = DLParser.kb.get_individual(list_tokens[1])
            b: Individual = DLParser.kb.get_individual(list_tokens[2])
            role: str = list_tokens[3]
            if role in DLParser.kb.concrete_roles:
                Util.error(f"Error: Role {role} cannot be concrete and abstract.")
            DLParser.kb.abstract_roles.add(role)
            if list_tokens[0] == FuzzyDLKeyword.MAX_RELATED_QUERY:
                DLParser.queries_list.append(MaxRelatedQuery(a, b, role))
            else:
                DLParser.queries_list.append(MinRelatedQuery(a, b, role))
        elif list_tokens[0] == FuzzyDLKeyword.MAX_VAR_QUERY:
            DLParser.queries_list.append(MaxQuery(list_tokens[1]))
        elif list_tokens[0] == FuzzyDLKeyword.MIN_VAR_QUERY:
            DLParser.queries_list.append(MinQuery(list_tokens[1]))
        elif list_tokens[0] in (
            FuzzyDLKeyword.DEFUZZIFY_LOM_QUERY,
            FuzzyDLKeyword.DEFUZZIFY_SOM_QUERY,
            FuzzyDLKeyword.DEFUZZIFY_MOM_QUERY,
        ):
            c: Concept = DLParser._to_concept(list_tokens[1])
            a: Individual = DLParser.kb.get_individual(list_tokens[2])
            role: str = list_tokens[3]
            if DLParser.kb.concrete_features.get(role) is None:
                Util.error(f"Error: Feature {role} has not been defined.")
            if list_tokens[0] == FuzzyDLKeyword.DEFUZZIFY_LOM_QUERY:
                DLParser.queries_list.append(LomDefuzzifyQuery(c, a, role))
            elif list_tokens[0] == FuzzyDLKeyword.DEFUZZIFY_SOM_QUERY:
                DLParser.queries_list.append(SomDefuzzifyQuery(c, a, role))
            elif list_tokens[0] == FuzzyDLKeyword.DEFUZZIFY_MOM_QUERY:
                DLParser.queries_list.append(MomDefuzzifyQuery(c, a, role))
        elif list_tokens[0] == FuzzyDLKeyword.BNP_QUERY:
            if not TriangularFuzzyNumber.has_defined_range():
                Util.error(
                    "Error: The range of the fuzzy numbers has to be defined before being used."
                )
            DLParser.queries_list.append(
                BnpQuery(
                    list_tokens[1]
                    if isinstance(list_tokens[1], TriangularFuzzyNumber)
                    else DLParser.kb.fuzzy_numbers.get(list_tokens[1])
                )
            )
        return tokens

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

        lbrace = pp.Literal("(").set_results_name("lbrace").suppress()
        rbrace = pp.Literal(")").set_results_name("rbrace").suppress()
        comment = pp.one_of(["#", "%"]).set_results_name("comment").suppress()
        any_not_newline = (
            pp.Regex("[^\n]+").set_results_name("any_not_newline").suppress()
        )

        digits = pp.Word(pp.nums)
        numbers = (
            pp.Combine(pp.Opt(pp.one_of(["+", "-"])) + digits + pp.Opt("." + digits))
            .set_results_name("number", list_all_matches=True)
            .set_parse_action(DLParser._to_number)
        )

        simple_string = pp.Word(pp.alphas + "_", pp.alphanums + "_'").set_results_name(
            "string", list_all_matches=True
        )  # pp.Regex(r"[a-zA-Z_][a-zA-Z0-9_]*")
        strings = (
            pp.Opt(pp.one_of(['"', "'"])).suppress()
            + simple_string.set_results_name("string", list_all_matches=True)
            + pp.Opt(pp.one_of(['"', "'"])).suppress()
        )
        variables = (
            strings | simple_string.set_results_name("variable", list_all_matches=True)
        ).set_results_name("variables", list_all_matches=True)

        fuzzy_logic = (
            (
                lbrace
                + FuzzyDLKeyword.DEFINE_FUZZY_LOGIC.get_value().suppress()
                + (
                    FuzzyDLKeyword.LUKASIEWICZ.get_value()
                    | FuzzyDLKeyword.ZADEH.get_value()
                    | FuzzyDLKeyword.CLASSICAL.get_value()
                ).set_results_name("fuzzy_logic")
                + rbrace
            )
            .set_results_name("fuzzy_logics", list_all_matches=True)
            .add_parse_action(DLParser._fuzzy_logic_parser)
        )

        comment_line = (comment + any_not_newline).set_results_name(
            "comments", list_all_matches=True
        )

        concept = pp.Forward()

        weighted_concept_part = (
            (lbrace + numbers + concept + rbrace)
            .set_results_name("simple_weighted_concepts_single", list_all_matches=True)
            .set_parse_action(DLParser._parse_weighted_concept_simple)
        )

        simple_fuzzy_number = (
            (
                variables
                | lbrace
                + (numbers[3] | pp.DelimitedList(numbers, min=3, max=3))
                + rbrace
                | numbers
            )
            .set_results_name("simple_fuzzy_numbers", list_all_matches=True)
            .set_parse_action(DLParser._create_fuzzy_number)
        )

        fuzzy_number_expr = pp.Forward()
        fuzzy_number_expr <<= (
            simple_fuzzy_number
            | lbrace
            + pp.one_of(
                [
                    FuzzyDLKeyword.FEATURE_SUM.get_name(),
                    FuzzyDLKeyword.FEATURE_MUL.get_name(),
                ]
            )
            + fuzzy_number_expr[1, ...]
            + rbrace
            | lbrace
            + pp.one_of(
                [
                    FuzzyDLKeyword.FEATURE_DIV.get_name(),
                    FuzzyDLKeyword.FEATURE_SUB.get_name(),
                ]
            )
            + fuzzy_number_expr[2]
            + rbrace
        ).set_results_name("fuzzy_number_expressions", list_all_matches=True)

        fuzzy_numbers = (
            (
                lbrace
                + FuzzyDLKeyword.DEFINE_FUZZY_NUMBER.get_value().suppress()
                + variables
                + fuzzy_number_expr
                + rbrace
            )
            .set_results_name("fuzzy_numbers", list_all_matches=True)
            .set_parse_action(DLParser._set_fuzzy_number)
        )

        datatype_restriction_operand = pp.Forward()
        datatype_restriction_function = pp.Forward()

        datatype_restriction_mul_expressions = pp.Group(
            (
                lbrace
                + numbers
                + pp.Opt(FuzzyDLKeyword.MUL.get_value()).suppress()
                + datatype_restriction_function
                + rbrace
            )
            .set_results_name("restrictions", list_all_matches=True)
            .set_parse_action(DLParser._parse_restrictions)
        )
        datatype_restriction_sub_expressions = pp.Group(
            (
                lbrace
                + datatype_restriction_function
                + FuzzyDLKeyword.SUB.get_value()
                + datatype_restriction_function
                + rbrace
            )
            .set_results_name("restrictions", list_all_matches=True)
            .set_parse_action(DLParser._parse_restrictions)
        )
        datatype_restriction_operand <<= (
            (
                datatype_restriction_mul_expressions
                | datatype_restriction_sub_expressions
                | variables
                | numbers
            )
            .set_results_name("restrictions", list_all_matches=True)
            .set_parse_action(DLParser._parse_restrictions)
        )
        datatype_restriction_function <<= (
            pp.infix_notation(
                datatype_restriction_operand,
                [
                    (FuzzyDLKeyword.SUM.get_value(), 2, pp.OpAssoc.LEFT),
                ],
            )
            .set_results_name("restrictions", list_all_matches=True)
            .set_parse_action(DLParser._parse_restrictions)
        )

        datatype_restrictions = (
            (
                lbrace
                + pp.one_of(
                    [
                        FuzzyDLKeyword.LESS_THAN_OR_EQUAL_TO.get_name(),
                        FuzzyDLKeyword.GREATER_THAN_OR_EQUAL_TO.get_name(),
                        FuzzyDLKeyword.EQUALS.get_name(),
                    ]
                )
                + variables
                + (variables | datatype_restriction_function | fuzzy_number_expr)
                + rbrace
            )
            .set_results_name("datatype_restrictions", list_all_matches=True)
            .set_parse_action(DLParser._parse_datatype_restriction)
        )

        concept <<= (
            (
                variables
                | FuzzyDLKeyword.TOP.get_value()
                | FuzzyDLKeyword.BOTTOM.get_value()
            )
            .set_results_name("truth_constants", list_all_matches=True)
            .set_parse_action(DLParser._to_top_bottom_concept)
            | datatype_restrictions.set_results_name(
                "restriction_concepts", list_all_matches=True
            )
            | weighted_concept_part.set_results_name(
                "simple_weighted_concept", list_all_matches=True
            )
            | lbrace
            + (
                (
                    (
                        pp.Literal("[").suppress()
                        + pp.one_of(
                            [
                                FuzzyDLKeyword.LESS_THAN_OR_EQUAL_TO.get_name(),
                                FuzzyDLKeyword.GREATER_THAN_OR_EQUAL_TO.get_name(),
                            ]
                        )
                        + (variables | numbers)
                        + pp.Literal("]").suppress()
                        + concept
                    )
                    .set_results_name("threshold_concepts", list_all_matches=True)
                    .set_parse_action(DLParser._parse_threshold_concept)
                    | (
                        pp.one_of(
                            [
                                FuzzyDLKeyword.GOEDEL_AND.get_name(),
                                FuzzyDLKeyword.LUKASIEWICZ_AND.get_name(),
                                FuzzyDLKeyword.AND.get_name(),
                                FuzzyDLKeyword.GOEDEL_OR.get_name(),
                                FuzzyDLKeyword.LUKASIEWICZ_OR.get_name(),
                                FuzzyDLKeyword.OR.get_name(),
                                FuzzyDLKeyword.GOEDEL_IMPLIES.get_name(),
                                FuzzyDLKeyword.LUKASIEWICZ_IMPLIES.get_name(),
                                FuzzyDLKeyword.KLEENE_DIENES_IMPLIES.get_name(),
                                FuzzyDLKeyword.IMPLIES.get_name(),
                            ]
                        )
                        + concept[2, ...]
                    ).set_results_name("implies_concepts", list_all_matches=True)
                    | (
                        FuzzyDLKeyword.SOME.get_value()
                        + variables
                        + (variables | concept)
                    ).set_results_name("some_concepts", list_all_matches=True)
                    | (
                        FuzzyDLKeyword.HAS_VALUE.get_value() + variables[2]
                    ).set_results_name("has_value_concepts", list_all_matches=True)
                    | pp.one_of(
                        [
                            FuzzyDLKeyword.ALL.get_name(),
                            FuzzyDLKeyword.TIGHT_UPPER_APPROXIMATION.get_name(),
                            FuzzyDLKeyword.LOOSE_UPPER_APPROXIMATION.get_name(),
                            FuzzyDLKeyword.UPPER_APPROXIMATION.get_name(),
                            FuzzyDLKeyword.TIGHT_LOWER_APPROXIMATION.get_name(),
                            FuzzyDLKeyword.LOOSE_LOWER_APPROXIMATION.get_name(),
                            FuzzyDLKeyword.LOWER_APPROXIMATION.get_name(),
                        ]
                    )
                    + variables
                    + concept
                )
                .set_results_name("binary_concepts", list_all_matches=True)
                .set_parse_action(DLParser._parse_binary_concept)
                | (
                    FuzzyDLKeyword.NOT.get_value() + concept
                    | FuzzyDLKeyword.SELF.get_value() + variables
                )
                .set_results_name("unary_concepts", list_all_matches=True)
                .set_parse_action(DLParser._parse_unary_concept)
                | (variables + concept)
                .set_results_name("modifier_concepts", list_all_matches=True)
                .set_parse_action(DLParser._parse_modifier_concept)
                | (
                    pp.one_of(
                        [
                            FuzzyDLKeyword.W_SUM_ZERO.get_name(),
                            FuzzyDLKeyword.W_SUM.get_name(),
                            FuzzyDLKeyword.W_MAX.get_name(),
                            FuzzyDLKeyword.W_MIN.get_name(),
                        ]
                    )
                    + pp.OneOrMore(weighted_concept_part)
                )
                .set_results_name("weighted_concepts", list_all_matches=True)
                .set_parse_action(DLParser._parse_weighted_concept)
                | (
                    FuzzyDLKeyword.Q_OWA.get_value().suppress()
                    + variables
                    + concept[1, ...]
                )
                .set_results_name("q_owas", list_all_matches=True)
                .set_parse_action(DLParser._parse_q_owa_concept)
                | (
                    pp.one_of(
                        [
                            FuzzyDLKeyword.OWA.get_name(),
                            FuzzyDLKeyword.CHOQUET.get_name(),
                            FuzzyDLKeyword.QUASI_SUGENO.get_name(),
                            FuzzyDLKeyword.SUGENO.get_name(),
                        ]
                    )
                    + lbrace
                    + numbers[1, ...]
                    + rbrace
                    + lbrace
                    + concept[1, ...]
                    + rbrace
                )
                .set_results_name("owa_integrals", list_all_matches=True)
                .set_parse_action(DLParser._parse_owa_integral_concept)
            )
            + rbrace
        )

        modifier = (
            (
                lbrace
                + FuzzyDLKeyword.DEFINE_MODIFIER.get_value().suppress()
                + variables
                + (
                    FuzzyDLKeyword.LINEAR_MODIFIER.get_value()
                    + lbrace
                    + numbers
                    + rbrace
                    | FuzzyDLKeyword.TRIANGULAR_MODIFIER.get_value()
                    + lbrace
                    + (numbers[3] | pp.DelimitedList(numbers, min=3, max=3))
                    + rbrace
                )
                + rbrace
            )
            .set_results_name("modifiers", list_all_matches=True)
            .set_parse_action(DLParser._parse_modifier)
        )

        truth_constants = (
            (
                lbrace
                + FuzzyDLKeyword.DEFINE_TRUTH_CONSTANT.get_value().suppress()
                + variables
                + numbers
                + rbrace
            )
            .set_results_name("truth_concepts", list_all_matches=True)
            .set_parse_action(DLParser._parse_truth_constants)
        )

        fuzzy_concept = (
            (
                lbrace
                + FuzzyDLKeyword.DEFINE_FUZZY_CONCEPT.get_value().suppress()
                + variables
                + (
                    FuzzyDLKeyword.CRISP.get_value()
                    + lbrace
                    + pp.DelimitedList(numbers, min=4, max=4)
                    + rbrace
                    | FuzzyDLKeyword.LEFT_SHOULDER.get_value()
                    + lbrace
                    + pp.DelimitedList(numbers, min=4, max=4)
                    + rbrace
                    | FuzzyDLKeyword.RIGHT_SHOULDER.get_value()
                    + lbrace
                    + pp.DelimitedList(numbers, min=4, max=4)
                    + rbrace
                    | FuzzyDLKeyword.TRIANGULAR.get_value()
                    + lbrace
                    + pp.DelimitedList(numbers, min=5, max=5)
                    + rbrace
                    | FuzzyDLKeyword.TRAPEZOIDAL.get_value()
                    + lbrace
                    + pp.DelimitedList(numbers, min=6, max=6)
                    + rbrace
                    | FuzzyDLKeyword.LINEAR.get_value()
                    + lbrace
                    + pp.DelimitedList(numbers, min=4, max=4)
                    + rbrace
                    | FuzzyDLKeyword.MODIFIED.get_value()
                    + lbrace
                    + pp.DelimitedList(variables, min=2, max=2)
                    + rbrace
                )
                + rbrace
            )
            .set_results_name("fuzzy_concepts", list_all_matches=True)
            .set_parse_action(DLParser._parse_fuzzy_concept)
        )

        fuzzy_range = (
            (
                lbrace
                + FuzzyDLKeyword.DEFINE_FUZZY_NUMBER_RANGE.get_value().suppress()
                + numbers[2]
                + rbrace
            )
            .set_results_name("fuzzy_ranges", list_all_matches=True)
            .set_parse_action(DLParser._parse_fuzzy_number_range)
        )

        features = (
            (
                lbrace
                + (
                    # Keyword.FUNCTIONAL.get_value() + variables |
                    FuzzyDLKeyword.RANGE.get_value()
                    + variables
                    + (
                        pp.one_of(
                            [
                                FuzzyDLKeyword.INTEGER.get_name(),
                                FuzzyDLKeyword.REAL.get_name(),
                            ]
                        )
                        + numbers[2]
                        | pp.one_of(
                            [
                                FuzzyDLKeyword.STRING.get_name(),
                                FuzzyDLKeyword.BOOLEAN.get_name(),
                            ]
                        )
                    )
                )
                + rbrace
            )
            .set_results_name("features", list_all_matches=True)
            .set_parse_action(DLParser._parse_feature)
        )

        term = (
            pp.infix_notation(
                numbers | variables,
                [
                    (FuzzyDLKeyword.MUL.get_value(), 2, pp.OpAssoc.LEFT),
                ],
            )
            .set_results_name("term", list_all_matches=True)
            .set_parse_action(DLParser._parse_term)
        )

        expression = (
            # pp.DelimitedList(
            #     numbers + FuzzyDLKeyword.MUL.get_value() + variables, delim="+"
            # )
            pp.infix_notation(
                term, [(FuzzyDLKeyword.SUM.get_value(), 2, pp.OpAssoc.LEFT)]
            )
            .set_results_name("expressions", list_all_matches=True)
            .set_parse_action(DLParser._parse_expression)
        )

        inequation = (
            (
                expression
                + pp.one_of(
                    [
                        FuzzyDLKeyword.LESS_THAN_OR_EQUAL_TO.get_name(),
                        FuzzyDLKeyword.GREATER_THAN_OR_EQUAL_TO.get_name(),
                        FuzzyDLKeyword.EQUALS.get_name(),
                    ]
                )
                + numbers
            )
            .set_results_name("inequations", list_all_matches=True)
            .set_parse_action(DLParser._parse_inequation)
        )

        constraints = (
            (
                lbrace
                + FuzzyDLKeyword.CONSTRAINTS.get_value()
                + lbrace
                + (
                    inequation
                    | FuzzyDLKeyword.BINARY.get_value() + variables
                    | FuzzyDLKeyword.FREE.get_value() + variables
                )
                + rbrace
                + rbrace
            )
            .set_results_name("constraints", list_all_matches=True)
            .set_parse_action(DLParser._parse_constraints)
        )

        show_concrete_fillers = (
            (
                lbrace
                + FuzzyDLKeyword.SHOW_CONCRETE_FILLERS.get_value().suppress()
                + variables[1, ...]
                + rbrace
            )
            .set_results_name("show_concrete_fillers", list_all_matches=True)
            .set_parse_action(DLParser._show_concrete_fillers)
        )

        show_concrete_fillers_for = (
            (
                lbrace
                + FuzzyDLKeyword.SHOW_CONCRETE_FILLERS_FOR.get_value().suppress()
                + variables[2, ...]
                + rbrace
            )
            .set_results_name("show_concrete_fillers_for", list_all_matches=True)
            .set_parse_action(DLParser._show_concrete_fillers_for)
        )

        show_concrete_instance_for = (
            (
                lbrace
                + FuzzyDLKeyword.SHOW_CONCRETE_INSTANCE_FOR.get_value().suppress()
                + variables[3, ...]
                + rbrace
            )
            .set_results_name("show_concrete_instance_for", list_all_matches=True)
            .set_parse_action(DLParser._show_concrete_instance_for)
        )

        show_abstract_fillers = (
            (
                lbrace
                + FuzzyDLKeyword.SHOW_ABSTRACT_FILLERS.get_value().suppress()
                + variables[1, ...]
                + rbrace
            )
            .set_results_name("show_abstract_fillers", list_all_matches=True)
            .set_parse_action(DLParser._show_abstract_fillers)
        )

        show_abstract_fillers_for = (
            (
                lbrace
                + FuzzyDLKeyword.SHOW_ABSTRACT_FILLERS_FOR.get_value().suppress()
                + variables[2, ...]
                + rbrace
            )
            .set_results_name("show_abstract_fillers_for", list_all_matches=True)
            .set_parse_action(DLParser._show_abstract_fillers_for)
        )

        show_concepts = (
            (
                lbrace
                + FuzzyDLKeyword.SHOW_CONCEPTS.get_value().suppress()
                + variables[1, ...]
                + rbrace
            )
            .set_results_name("show_concepts", list_all_matches=True)
            .set_parse_action(DLParser._show_concepts)
        )

        show_instances = (
            (
                lbrace
                + FuzzyDLKeyword.SHOW_INSTANCES.get_value().suppress()
                + concept[1, ...]
                + rbrace
            )
            .set_results_name("show_instances", list_all_matches=True)
            .set_parse_action(DLParser._show_instances)
        )

        show_variables = (
            (
                lbrace
                + FuzzyDLKeyword.SHOW_VARIABLES.get_value().suppress()
                + variables[1, ...]
                + rbrace
            )
            .set_results_name("show_variables", list_all_matches=True)
            .set_parse_action(DLParser._show_variables)
        )

        show_languages = (
            (lbrace + FuzzyDLKeyword.SHOW_LANGUAGE.get_value().suppress() + rbrace)
            .set_results_name("show_languages", list_all_matches=True)
            .set_parse_action(DLParser._show_languages)
        )

        show_statements = (
            show_concrete_fillers_for
            | show_concrete_fillers
            | show_concrete_instance_for
            | show_abstract_fillers_for
            | show_abstract_fillers
            | show_concepts
            | show_instances
            | show_variables
            | show_languages
        )

        crisp_declarations = (
            (
                lbrace
                + (
                    FuzzyDLKeyword.CRISP_CONCEPT.get_value()
                    | FuzzyDLKeyword.CRISP_ROLE.get_value()
                )
                + variables[1, ...]
                + rbrace
            )
            .set_results_name("crisp_declarations", list_all_matches=True)
            .set_parse_action(DLParser._parse_crisp_declarations)
        )

        fuzzy_similarity = (
            (
                lbrace
                + FuzzyDLKeyword.DEFINE_FUZZY_SIMILARITY.get_value().suppress()
                + variables
                + rbrace
            )
            .set_results_name("fuzzy_similarities", list_all_matches=True)
            .set_parse_action(DLParser._parse_fuzzy_similarity)
        )

        fuzzy_equivalence = (
            (
                lbrace
                + FuzzyDLKeyword.DEFINE_FUZZY_EQUIVALENCE.get_value().suppress()
                + variables
                + rbrace
            )
            .set_results_name("fuzzy_equivalences", list_all_matches=True)
            .set_parse_action(DLParser._parse_fuzzy_equivalence)
        )

        degree = (
            (numbers | expression | variables)
            .set_results_name("degrees", list_all_matches=True)
            .set_parse_action(DLParser._parse_degree)
        )

        axioms = (
            (
                lbrace
                + pp.Group(
                    FuzzyDLKeyword.INSTANCE.get_value()
                    + variables
                    + concept
                    + pp.Opt(degree)
                    | FuzzyDLKeyword.RELATED.get_value() + variables[3] + pp.Opt(degree)
                    | FuzzyDLKeyword.IMPLIES_ROLE.get_value()
                    + variables[2]
                    + pp.Opt(numbers)
                    | FuzzyDLKeyword.ZADEH_IMPLIES.get_value() + concept + concept
                    | pp.one_of(
                        [
                            FuzzyDLKeyword.ZADEH_IMPLIES.get_name(),
                            FuzzyDLKeyword.GOEDEL_IMPLIES.get_name(),
                            FuzzyDLKeyword.LUKASIEWICZ_IMPLIES.get_name(),
                            FuzzyDLKeyword.KLEENE_DIENES_IMPLIES.get_name(),
                            FuzzyDLKeyword.IMPLIES.get_name(),
                        ]
                    )
                    + concept[2]
                    + pp.Opt(degree)
                    | FuzzyDLKeyword.DEFINE_CONCEPT.get_value() + variables + concept
                    | FuzzyDLKeyword.DEFINE_PRIMITIVE_CONCEPT.get_value()
                    + variables
                    + concept
                    | FuzzyDLKeyword.EQUIVALENT_CONCEPTS.get_value() + concept[2]
                    | FuzzyDLKeyword.DISJOINT_UNION.get_value() + concept[1, ...]
                    | FuzzyDLKeyword.DISJOINT.get_value() + concept[1, ...]
                    | FuzzyDLKeyword.RANGE.get_value() + variables + concept
                    | FuzzyDLKeyword.DOMAIN.get_value() + variables + concept
                    | pp.one_of(
                        [
                            FuzzyDLKeyword.INVERSE_FUNCTIONAL.get_name(),
                            FuzzyDLKeyword.FUNCTIONAL.get_name(),
                            FuzzyDLKeyword.REFLEXIVE.get_name(),
                            FuzzyDLKeyword.SYMMETRIC.get_name(),
                            FuzzyDLKeyword.TRANSITIVE.get_name(),
                        ]
                    )
                    + variables
                    | FuzzyDLKeyword.INVERSE.get_value() + variables[2],
                )
                + rbrace
            )
            .set_results_name("axioms", list_all_matches=True)
            .set_parse_action(DLParser._parse_axioms)
        )

        queries = (
            (
                lbrace
                + pp.Group(
                    FuzzyDLKeyword.ALL_INSTANCES_QUERY.get_value() + concept
                    | FuzzyDLKeyword.SAT_QUERY.get_value()
                    | pp.one_of(
                        [
                            FuzzyDLKeyword.MAX_INSTANCE_QUERY.get_name(),
                            FuzzyDLKeyword.MIN_INSTANCE_QUERY.get_name(),
                        ]
                    )
                    + variables
                    + concept
                    | pp.one_of(
                        [
                            FuzzyDLKeyword.MAX_SUBS_QUERY.get_name(),
                            FuzzyDLKeyword.MIN_SUBS_QUERY.get_name(),
                            FuzzyDLKeyword.MAX_G_SUBS_QUERY.get_name(),
                            FuzzyDLKeyword.MIN_G_SUBS_QUERY.get_name(),
                            FuzzyDLKeyword.MAX_L_SUBS_QUERY.get_name(),
                            FuzzyDLKeyword.MIN_L_SUBS_QUERY.get_name(),
                            FuzzyDLKeyword.MAX_KD_SUBS_QUERY.get_name(),
                            FuzzyDLKeyword.MIN_KD_SUBS_QUERY.get_name(),
                        ]
                    )
                    + concept[2]
                    | pp.one_of(
                        [
                            FuzzyDLKeyword.MAX_RELATED_QUERY.get_name(),
                            FuzzyDLKeyword.MIN_RELATED_QUERY.get_name(),
                        ]
                    )
                    + variables[3]
                    | pp.one_of(
                        [
                            FuzzyDLKeyword.MAX_SAT_QUERY.get_name(),
                            FuzzyDLKeyword.MIN_SAT_QUERY.get_name(),
                        ]
                    )
                    + concept
                    + pp.Opt(variables)
                    | pp.one_of(
                        [
                            FuzzyDLKeyword.MAX_VAR_QUERY.get_name(),
                            FuzzyDLKeyword.MIN_VAR_QUERY.get_name(),
                        ]
                    )
                    + expression
                    | pp.one_of(
                        [
                            FuzzyDLKeyword.DEFUZZIFY_LOM_QUERY.get_name(),
                            FuzzyDLKeyword.DEFUZZIFY_SOM_QUERY.get_name(),
                            FuzzyDLKeyword.DEFUZZIFY_MOM_QUERY.get_name(),
                        ]
                    )
                    + concept
                    + variables[2]
                    | FuzzyDLKeyword.BNP_QUERY.get_value() + fuzzy_number_expr,
                )
                + rbrace
            )
            .set_results_name("queries", list_all_matches=True)
            .set_parse_action(DLParser._parse_queries)
        )

        gformula = (
            comment_line
            | fuzzy_logic
            | axioms
            | truth_constants
            | modifier
            | fuzzy_concept
            | fuzzy_range
            | fuzzy_numbers
            | features
            | constraints
            | show_statements
            | crisp_declarations
            | concept
            | fuzzy_similarity
            | fuzzy_equivalence
            | queries
        )
        return pp.OneOrMore(gformula)

    @staticmethod
    @utils.recursion_unlimited
    def parse_string(
        instring: str,
    ) -> pp.ParseResults:
        return DLParser.get_grammatics().parse_string(instring, parse_all=True)

    @staticmethod
    @utils.recursion_unlimited
    def parse_string_opt(
        filename: str,
    ) -> pp.ParseResults:
        with open(filename, "r") as file:
            instring = file.read()

        if ConfigReader.DEBUG_PRINT:
            return DLParser.get_grammatics().run_tests(
                instring,
                failure_tests=True,
                file=open(os.path.join(LOG_DIR, FILENAME), "w"),
            )
        else:
            return DLParser.get_grammatics().parse_string(instring)

    @staticmethod
    def load_config(*args) -> None:
        ConfigReader.load_parameters(os.path.join(os.getcwd(), "CONFIG.ini"), args)

    @staticmethod
    def get_kb(*args) -> tuple[KnowledgeBase, list[Query]]:
        try:
            starting_time: float = time.perf_counter_ns()
            DLParser.load_config(*args)
            DLParser.kb = KnowledgeBase()
            DLParser.queries_list = []
            constants.KNOWLEDGE_BASE_SEMANTICS = FuzzyLogic.LUKASIEWICZ

            if ConfigReader.DEBUG_PRINT:
                with open(args[0], "r") as file:
                    lines = file.readlines()
                for i, line in enumerate(lines):
                    line = line.strip()
                    if line == "":
                        continue
                    if ConfigReader.DEBUG_PRINT:
                        Util.debug(f"Line -> {line}")
                    _ = DLParser.parse_string(line)
            else:
                _ = DLParser.parse_string_opt(args[0])
            ending_time: float = time.perf_counter_ns() - starting_time
            Util.info(f"Knowledge Base parsed in {(ending_time * 1e-9)}s")
            return DLParser.kb, DLParser.queries_list
        except FileNotFoundError as e:
            Util.error(f"Error: File {args[0]} not found.")
        except Exception as e:
            Util.error(e)
            Util.error(traceback.format_exc())

    @staticmethod
    def main(*args) -> None:
        try:
            kb, queries = DLParser.get_kb(*args)
            kb.solve_kb()
            for query in queries:
                if (
                    isinstance(query, AllInstancesQuery)
                    and not kb.get_individuals().values()
                ):
                    Util.info(f"{query} -- There are no individuals in the fuzzy KB")
                else:
                    result: Solution = query.solve(kb)
                    if result.is_consistent_kb():
                        Util.info(f"{query}{result}")
                    else:
                        Util.info("KnowledgeBase inconsistent: Answer is 1.0.")
                Util.info(f"Time (s): {query.get_total_time()}")
                if kb.show_language:
                    Util.info(f"The language of the KB is {kb.get_language()}")
        except InconsistentOntologyException as e:
            Util.error("KnowledgeBase inconsistent: Any answer is 1.0.")
        except Exception as e:
            Util.error(e)
            Util.error(traceback.format_exc())


if __name__ == "__main__":
    DLParser.main("./test.txt")
