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
from fuzzy_dl_owl2.fuzzydl.concept.sigma_concept import SigmaConcept
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
    """
    This class serves as a specialized parser for Fuzzy Description Logic, designed to interpret textual input and construct a corresponding knowledge base and set of queries. It utilizes the `pyparsing` library to define a comprehensive grammar that covers various fuzzy logic constructs, including concepts, roles, modifiers, axioms, and complex query types. The parser operates primarily through static methods that act as callbacks during the parsing process, transforming raw string tokens into domain-specific objects such as `Concept`, `Individual`, and `Degree` instances. Users typically interact with this class by calling the `get_kb` method, which accepts a file path, initializes the internal state, parses the file content, and returns the populated `KnowledgeBase` and a list of `Query` objects. The class handles semantic validation and logic-specific constraints (e.g., distinguishing between Zadeh and Lukasiewicz logic) during parsing, ensuring that the constructed knowledge base adheres to the specified fuzzy logic semantics. Additionally, it provides a `main` entry point to execute the parsing, solve the knowledge base, and process the resulting queries sequentially.

    :param kb: The KnowledgeBase instance constructed and populated by the parser with the parsed domain model.
    :type kb: KnowledgeBase
    :param queries_list: Accumulates Query objects extracted from the input during parsing, which are subsequently returned for execution against the knowledge base.
    :type queries_list: list[Query]
    """


    kb: KnowledgeBase = None
    queries_list: list[Query] = []

    @staticmethod
    def _check_abstract(c: Concept) -> None:
        """
        Validates that the provided `Concept` instance is abstract, ensuring it is not marked as concrete. If the concept is determined to be concrete, this method triggers an error reporting routine to signal a violation of the expected schema. This static method serves as a guard clause within the parsing logic to enforce structural constraints.

        :param c: The concept to validate as abstract.
        :type c: Concept
        """

        if c.is_concrete():
            Util.error(f"Error: Concept {c} should be abstract.")

    @staticmethod
    # @pp.trace_parse_action
    def _to_number(tokens: pp.ParseResults) -> float | int:
        """
        Converts the first element of the provided parse results into a numeric type, prioritizing integers when appropriate. The method extracts the initial token, ensures it is a string, and attempts to parse it as a floating-point number. If the parsed value is mathematically an integer, it is returned as an `int`; otherwise, it is returned as a `float`. This function assumes the input token represents a valid numeric string and will raise a `ValueError` if the conversion fails.

        :param tokens: The parsed results containing the string representation of the number to be converted.
        :type tokens: pp.ParseResults

        :return: The numeric representation of the input token, returned as an int if the value is a whole number, or as a float otherwise.

        :rtype: float | int
        """

        v: float = float(str(tokens.as_list()[0]))
        return int(v) if v.is_integer() else v

    @staticmethod
    # @pp.trace_parse_action
    def _fuzzy_logic_parser(tokens: pp.ParseResults) -> pp.ParseResults:
        """
        This static method acts as a parsing action to process and apply a specified fuzzy logic type to the system. It extracts the first token from the parse results, converts it to a lowercase string, and instantiates a corresponding FuzzyLogic object. The method then updates the Knowledge Base associated with the parser by setting this logic, effectively configuring the reasoning engine for the session. It returns the original tokens unchanged, assuming the input grammar guarantees the presence of at least one token to define the logic.

        :param tokens: The parse results containing the identifier for the fuzzy logic type to be applied to the knowledge base.
        :type tokens: pp.ParseResults

        :return: The original parse results containing the fuzzy logic identifier.

        :rtype: pp.ParseResults
        """

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_fuzzy_logic_parser -> {tokens}")
        DLParser.kb.set_logic(FuzzyLogic(str(tokens.as_list()[0]).lower()))
        return tokens

    @staticmethod
    # @pp.trace_parse_action
    def _to_concept(c: typing.Union[str, Concept]) -> Concept:
        """
        This static method ensures that the provided argument is returned as a Concept object, handling both string identifiers and existing Concept instances. If the input is already a Concept, it is returned unchanged; otherwise, the method treats the input as a string and attempts to retrieve the corresponding Concept from the parser's knowledge base. The operation includes a side effect of printing debug information if debug mode is enabled.

        :param c: A string identifier or Concept object to be resolved into a Concept instance.
        :type c: typing.Union[str, Concept]

        :return: The Concept object corresponding to the input string, or the input object itself if it is already a Concept.

        :rtype: Concept
        """

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_to_concept -> {c}")
        return c if isinstance(c, Concept) else DLParser.kb.get_concept(c)
        # return DLParser.kb.get_concept(str(c))

    @staticmethod
    # @pp.trace_parse_action
    def _to_top_bottom_concept(tokens: pp.ParseResults) -> pp.ParseResults:
        """
        Transforms the provided parse results into a specific concept object based on the content of the first token. If the token corresponds to the 'TOP' keyword, the method returns the universal truth concept; if it corresponds to 'BOTTOM', it returns the empty truth concept. For any other token, the method delegates the conversion to the internal `_to_concept` method to generate a standard Description Logic concept. The method may output debug information depending on the global configuration settings.

        :param tokens: Parsed results containing a keyword or identifier representing a top, bottom, or regular concept.
        :type tokens: pp.ParseResults

        :return: A ParseResults object containing the Top concept, Bottom concept, or a regular concept derived from the input tokens.

        :rtype: pp.ParseResults
        """

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
        """
        Retrieves a `Modifier` object from the shared knowledge base corresponding to the given string name. This method verifies that the modifier is defined; if the knowledge base is uninitialized or the name is not found, it invokes an error handling routine to signal the issue. Furthermore, it outputs debug logging details if the debug print configuration is active.

        :param m: The name of the modifier to retrieve from the knowledge base.
        :type m: str

        :return: The `Modifier` object associated with the specified name.

        :rtype: Modifier
        """

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_get_modifier -> {m}")
        if len(DLParser.kb.modifiers) == 0 or m not in DLParser.kb.modifiers:
            Util.error(f"Error: {m} modifier is not defined.")
        return DLParser.kb.modifiers.get(m)

    @staticmethod
    # @pp.trace_parse_action
    def _parse_binary_concept(tokens: pp.ParseResults) -> pp.ParseResults:
        """
        Parses a binary or n-ary concept expression from the provided parse results, identifying the specific operation based on the first token. The method handles a variety of logical constructs, including conjunctions, disjunctions, implications, quantifiers, value restrictions, and approximation operators, dynamically selecting the appropriate implementation (e.g., Lukasiewicz, Goedel, or Zadeh) based on the current fuzzy logic setting in the knowledge base. It validates that operands are abstract concepts, ensures referenced roles and individuals exist, and enforces logic-specific constraints by raising errors if fuzzy-specific operators are used within a classical logic context. If the operator token is already a Concept object, the method returns the input tokens unchanged.

        :param tokens: The parsed structure containing the operator and operands for the binary concept.
        :type tokens: pp.ParseResults

        :return: A ParseResults object containing the specific Concept instance (e.g., OperatorConcept, ImpliesConcept) constructed from the input tokens.

        :rtype: pp.ParseResults
        """

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
        """
        This static method processes a parsed unary concept expression, transforming raw tokens into a specific Concept object based on the operator provided. If the operator is a negation (NOT), it retrieves the operand concept, converts it to a Concept object, and returns its negation. If the operator is a self-reference (SELF), it validates that the associated role is not concrete, registers the role as abstract within the global knowledge base, and constructs a SelfConcept instance. The method modifies the global knowledge base by adding roles to the set of abstract roles when processing self-concepts, and it raises an error if a self-concept is applied to a concrete role.

        :param tokens: The parsed input containing the unary operator and the concept or role it modifies.
        :type tokens: pp.ParseResults

        :return: A ParseResults object containing the constructed unary concept, such as a negated concept or a self-concept, or the original tokens.

        :rtype: pp.ParseResults
        """

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
        """
        This static method processes a sequence of tokens representing a modifier applied to a concept, expecting the input list to contain exactly two elements. It extracts the modifier from the first token and the base concept from the second, resolving them into their respective object instances. The method then applies the modification logic to the concept and returns the resulting modified concept encapsulated within a `pp.ParseResults` object.

        :param tokens: The parsed tokens containing the modifier and concept components to be combined.
        :type tokens: pp.ParseResults

        :return: A ParseResults object containing the Concept resulting from applying the parsed Modifier to the parsed Concept.

        :rtype: pp.ParseResults
        """

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_parse_modifier_concept -> {tokens}")
        list_tokens: list[str] = tokens.as_list()
        mod: Modifier = DLParser._get_modifier(list_tokens[0])
        concept: Concept = DLParser._to_concept(list_tokens[1])
        return pp.ParseResults([mod.modify(concept)])

    @staticmethod
    # @pp.trace_parse_action
    def _parse_threshold_concept(tokens: pp.ParseResults):
        """
        Parses a threshold concept definition from the provided parse results tokens and constructs the corresponding concept object. The method expects a token list containing a comparison operator, a threshold value (which can be a numeric literal or a string representing a MILP variable), and a concept identifier. It converts the identifier to a Concept instance, validates that the concept is not abstract, and then instantiates either a standard ThresholdConcept or an ExtThresholdConcept based on the operator type and value type. The resulting object is wrapped in a ParseResults container and returned. If debug printing is enabled, the input tokens are logged to the console.

        :param tokens: The parsed elements of a threshold expression, structured as an operator, a threshold value (numeric or variable), and a concept.
        :type tokens: pp.ParseResults
        """

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
        """
        This static method processes a sequence of parsed tokens to construct a WeightedConcept object, typically serving as a parsing action callback. It extracts the first token as a floating-point weight and converts the second token into a Concept object using the `_to_concept` helper method. The resulting WeightedConcept instance is then wrapped in a ParseResults object and returned. The method assumes the input tokens contain at least two elements and may output debug information if the debug flag is enabled.

        :param tokens: The parsed elements containing the weight and concept string, where the first element is the weight and the second is the concept.
        :type tokens: pp.ParseResults

        :return: A ParseResults object containing the constructed WeightedConcept instance.

        :rtype: pp.ParseResults
        """

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_parse_weighted_concept_simple -> {tokens}")
        list_tokens: list[str] = tokens.as_list()
        weight: float = list_tokens[0]
        concept: Concept = DLParser._to_concept(list_tokens[1])
        return pp.ParseResults([WeightedConcept(weight, concept)])

    @staticmethod
    # @pp.trace_parse_action
    def _parse_weighted_concept(tokens: pp.ParseResults) -> pp.ParseResults:
        """
        Parses a weighted concept expression from the provided parse results, expecting the first token to be an operator and subsequent tokens to be WeightedConcept instances. It extracts the weights and underlying concepts, then validates them based on the specific operator type: sum-based operators require the total weight to be less than or equal to 1.0, while min/max operators require the maximum weight to be exactly 1.0. If validation fails, an error is triggered via the utility function. Upon success, it returns a new ParseResults object containing the appropriate specialized concept object, such as WeightedSumConcept or WeightedMaxConcept.

        :param tokens: Parse results containing an operator keyword and a list of WeightedConcept objects to be combined.
        :type tokens: pp.ParseResults

        :return: A ParseResults object wrapping the constructed weighted concept (WeightedSumConcept, WeightedMaxConcept, WeightedMinConcept, or WeightedSumZeroConcept) based on the parsed operator.

        :rtype: pp.ParseResults
        """

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
        """
        This static method processes a sequence of tokens to construct a Quantified OWA (Ordered Weighted Averaging) concept. It interprets the first token as the name of a fuzzy concrete concept, retrieving it from the knowledge base to serve as the aggregation function. The method enforces strict type checking, ensuring the retrieved function is either a `RightConcreteConcept` or `LeftConcreteConcept`, and triggers an error if the concept is undefined or of an incorrect type. Subsequent tokens are recursively parsed into standard `Concept` objects to serve as arguments. Finally, it returns a `ParseResults` object containing the fully initialized `QowaConcept`.

        :param tokens: Parsed results representing the components of a Q-OWA concept, comprising a fuzzy aggregation function identifier and a list of concepts to aggregate.
        :type tokens: pp.ParseResults

        :return: A ParseResults object containing the constructed QowaConcept instance.

        :rtype: pp.ParseResults
        """

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_parse_q_owa_concept -> {tokens}")
        list_tokens: list[str] = tokens.as_list()
        f: FuzzyConcreteConcept = DLParser.kb.concrete_concepts.get(list_tokens[0])
        if f is None:
            Util.error(f"Error: Fuzzy concept {f} has to be defined before being used.")
        if not isinstance(f, (RightConcreteConcept, LeftConcreteConcept)):
            Util.error(f"Error: Fuzzy concept {f} has to be a right or left functions.")
        concepts: list[Concept] = [
            DLParser._to_concept(concept) for concept in list_tokens[1:]
        ]
        return pp.ParseResults([QowaConcept(f, concepts)])

    @staticmethod
    # @pp.trace_parse_action
    def _parse_owa_integral_concept(tokens: pp.ParseResults) -> pp.ParseResults:
        """
        Parses a fuzzy logic integral concept—specifically OWA, Choquet, Sugeno, or Q-Sugeno—from the provided parse results. The method extracts the operator from the first token and divides the remaining tokens into two equal lists representing weights and concepts, converting the latter into `Concept` objects. It performs validation on the weights, ensuring they sum to 1.0 for OWA operators and that the maximum weight is 1.0 for Choquet, Sugeno, and Q-Sugeno operators, reporting an error if these conditions are not met. The result is returned as a `pp.ParseResults` object wrapping the appropriate specialized concept instance.

        :param tokens: The parsed results containing the integral operator, associated weights, and the list of concepts to be aggregated.
        :type tokens: pp.ParseResults

        :return: A ParseResults object wrapping the specific integral concept instance (OwaConcept, ChoquetIntegral, SugenoIntegral, or QsugenoIntegral) parsed from the input tokens.

        :rtype: pp.ParseResults
        """

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
    def _parse_sigma_count_concept(tokens: pp.ParseResults) -> pp.ParseResults:
        """
        Parses a sequence of tokens to construct a SigmaConcept, which represents a sigma count operation involving a specific role, concept, and set of individuals. The method extracts the role, the base concept, and a list of individuals from the input tokens, while the final token identifies a fuzzy concept used for the sigma count calculation. It performs validation to ensure the specified fuzzy concept exists in the knowledge base and is a concrete function type (specifically Left, Right, or Triangular), raising an error if these conditions are not met. The resulting SigmaConcept object is then wrapped in a ParseResults object and returned.

        :param tokens: The parsed output containing the role, concept, individuals, and fuzzy concept name required to construct a SigmaConcept.
        :type tokens: pp.ParseResults

        :return: A `pp.ParseResults` object containing the `SigmaConcept` instance constructed from the parsed tokens.

        :rtype: pp.ParseResults
        """

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_parse_sigma_count_concept -> {tokens}")
        list_tokens: list[str] = tokens.as_list()
        role: str = list_tokens[0]
        concept: Concept = DLParser._to_concept(list_tokens[1])
        individuals: list[Individual] = [
            DLParser.kb.get_individual(token) for token in list_tokens[2:-1]
        ]
        concept_name: str = list_tokens[-1]
        if concept_name not in DLParser.kb.concrete_concepts:
            Util.error(f"Error: Fuzzy concept {concept_name} has not been defined")
        fuzzy_concept: Concept = DLParser.kb.get_concept(concept_name)
        if not isinstance(
            fuzzy_concept,
            (RightConcreteConcept, LeftConcreteConcept, TriangularConcreteConcept),
        ):
            Util.error(
                f"Error: Fuzzy concept {fuzzy_concept} has to be a left, right or a triangular function."
            )
        return pp.ParseResults(
            [SigmaConcept(concept, role, individuals, fuzzy_concept)]
        )

    @staticmethod
    # @pp.trace_parse_action
    def _parse_modifier(tokens: pp.ParseResults) -> pp.ParseResults:
        """
        This static method processes a parsed modifier definition by extracting the modifier type and parameters from the provided tokens. It distinguishes between linear and triangular modifiers based on the specific keyword present, instantiating the corresponding `LinearModifier` or `TriangularModifier` object with the extracted arguments. The constructed modifier is then registered with the global knowledge base (`DLParser.kb`), effectively updating the application's state. The method returns the original tokens unchanged, but assumes the input list contains sufficient elements for the specific modifier type, potentially raising an error if the token structure is invalid.

        :param tokens: The parsed components of a modifier definition, including the name, type keyword, and associated parameters.
        :type tokens: pp.ParseResults

        :return: The original input tokens, returned unchanged.

        :rtype: pp.ParseResults
        """

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
        """
        This static method serves as a parsing action callback that processes tokens matched by a grammar rule for truth constants. It extracts the first two elements from the input `ParseResults` and updates the class-level knowledge base by invoking `set_truth_constants` with these values. The function returns the original tokens unchanged, allowing the parsing process to continue, though it assumes the input list contains at least two elements.

        :param tokens: The parsed results containing the truth constant values to be set in the knowledge base.
        :type tokens: pp.ParseResults

        :return: The input ParseResults object containing the parsed tokens.

        :rtype: pp.ParseResults
        """


        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_parse_truth_constants -> {tokens}")
        list_tokens: list[str] = tokens.as_list()
        DLParser.kb.set_truth_constants(list_tokens[0], list_tokens[1])
        return tokens

    @staticmethod
    # @pp.trace_parse_action
    def _parse_fuzzy_concept(tokens: pp.ParseResults) -> pp.ParseResults:
        """
        Parses a fuzzy concept definition from the provided tokens and registers the corresponding concrete concept object in the global knowledge base. The method validates that the concept name is not already defined and ensures that non-crisp concept types are not used with a classical reasoner. Depending on the keyword found in the tokens, it instantiates a specific concept class—such as `CrispConcreteConcept`, `TriangularConcreteConcept`, or `ModifiedConcreteConcept`—using the extracted parameters. For modified concepts, it verifies that the base concept exists prior to creation. As a side effect, adding a non-crisp concept sets a flag in the knowledge base indicating the presence of concrete fuzzy concepts. The original tokens are returned to allow parsing to continue.

        :param tokens: Parsed results containing the fuzzy concept definition, including the concept name, type keyword, and associated parameters or references.
        :type tokens: pp.ParseResults

        :return: The original ParseResults object, returned after adding the fuzzy concept to the knowledge base.

        :rtype: pp.ParseResults
        """

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
        """
        Extracts the lower and upper bounds from the provided parsing tokens to configure the range for triangular fuzzy numbers. This static method converts the input `ParseResults` into a list and invokes the `TriangularFuzzyNumber.set_range` method with the first two elements, resulting in a side effect that updates the class-level state. It returns the token list wrapped in a new `ParseResults` object, assuming the input contains at least two elements to define the range boundaries.

        :param tokens: The parsed results containing the values that define the fuzzy number range.
        :type tokens: pp.ParseResults

        :return: A pyparsing ParseResults object containing the parsed tokens representing the fuzzy number range.

        :rtype: pp.ParseResults
        """

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_parse_fuzzy_number_range -> {tokens}")
        tokens = tokens.as_list()
        TriangularFuzzyNumber.set_range(tokens[0], tokens[1])
        return pp.ParseResults(tokens)

    @staticmethod
    # @pp.trace_parse_action
    def _create_fuzzy_number(tokens: pp.ParseResults) -> pp.ParseResults:
        """
        This static method processes parse tokens to construct a `TriangularFuzzyNumber` instance, supporting multiple input formats. If a single numeric value is provided, it generates a crisp fuzzy number where the lower, middle, and upper bounds are equal. When a string identifier is encountered, the method retrieves the corresponding fuzzy number from the knowledge base; if the identifier is undefined, an error is triggered. If three numeric values are present, they are interpreted as the lower, middle, and upper bounds of the triangular distribution. Should the input not conform to these patterns, the original tokens are returned unchanged. The method also outputs debug information if the global debug flag is enabled.

        :param tokens: The parsed elements representing a fuzzy number, which can be a single numeric value, a string identifier referencing a predefined number, or a list of three numeric values.
        :type tokens: pp.ParseResults

        :return: A ParseResults object wrapping a TriangularFuzzyNumber instance derived from the input tokens, or the original tokens if they cannot be parsed.

        :rtype: pp.ParseResults
        """

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
        """
        Processes a parsed fuzzy number definition to construct a TriangularFuzzyNumber instance and register it within the global knowledge base. The method supports direct assignment and arithmetic operations—specifically addition, subtraction, multiplication, and division—by resolving string identifiers in the input tokens to existing fuzzy number objects. It validates that the target name is unique, reporting an error if a fuzzy number with that name already exists. As a side effect, the method updates the knowledge base with the new definition and sets a flag indicating the presence of concrete fuzzy concepts. The resulting TriangularFuzzyNumber is returned wrapped in a ParseResults object.

        :param tokens: Parsed components of a fuzzy number definition, including the identifier, the defining expression (value or operator), and associated operands.
        :type tokens: pp.ParseResults

        :return: A ParseResults object containing the TriangularFuzzyNumber instance that was defined or calculated and added to the knowledge base.

        :rtype: pp.ParseResults
        """

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
        """
        Processes a parsed feature definition to register a concrete feature within the global knowledge base. It inspects the provided token list to identify the feature's role and data type, dispatching to the appropriate definition method—such as defining integer or real ranges, or boolean and string types. This method mutates the knowledge base state by adding the new feature definition and returns the original tokens to allow the parsing process to continue.

        :param tokens: The parsed components of a feature definition, including the role name, data type, and optional numeric bounds.
        :type tokens: pp.ParseResults

        :return: A ParseResults object containing the list of tokens parsed from the feature definition.

        :rtype: pp.ParseResults
        """

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
        """
        This method processes a list of tokens generated by the parser to construct `FeatureFunction` objects representing various restriction types. It first normalizes the input by flattening nested lists and then inspects the token count and content to determine the specific structure to build. For single tokens, it wraps the value directly; for pairs starting with a number, it creates a weighted feature function. For longer sequences, it identifies specific keywords—such as multiplication, subtraction, or summation—to construct composite feature functions involving the surrounding operands. If the token structure does not match any of these defined patterns, the method returns the original tokens wrapped in a `ParseResults` object.

        :param tokens: The parsed tokens representing the components of a restriction expression, including operands and operators, used to construct FeatureFunction objects.
        :type tokens: pp.ParseResults

        :return: A pp.ParseResults object wrapping a FeatureFunction instance constructed from the tokens based on detected operators or structure, or the original tokens if no specific restriction pattern is identified.

        :rtype: typing.Any
        """


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
        """
        This static method processes a datatype restriction from the provided parse results, determining the restriction type (such as exact, at most, or at least) based on the operator token and identifying the associated concrete feature role. It validates that the role has been previously defined in the knowledge base and ensures that any triangular fuzzy numbers used have a defined range before proceeding. Depending on the value token's type, the method resolves strings to either existing fuzzy number concepts or new continuous variables, and handles triangular fuzzy numbers by extracting their crisp or fuzzy representations. The constructed restriction is then added to the global knowledge base, and the method returns a ParseResults object containing the added entity.

        :param tokens: The parsed components of the datatype restriction, containing the operator, the feature role, and the value or concept.
        :type tokens: pp.ParseResults

        :return: A ParseResults object containing the datatype restriction object that was added to the knowledge base.

        :rtype: pp.ParseResults
        """


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
        """
        This static method processes a parsed token sequence representing a single term within a mathematical expression and constructs a corresponding Term object. It handles two specific structures: a standalone variable name, which is interpreted as having an implicit coefficient of 1.0, and a triple consisting of a coefficient, an operator, and a variable name. In both cases, the variable string is resolved to a specific variable object via the MILP knowledge base associated with the parser. The resulting Term object is wrapped in a pp.ParseResults container to maintain compatibility with the parsing framework.

        :param tokens: The parsed result containing the components of a mathematical term, representing either a single variable or a coefficient and variable pair.
        :type tokens: pp.ParseResults

        :return: A ParseResults object wrapping a Term instance representing the parsed coefficient and variable, or the original tokens if the input structure is unexpected.

        :rtype: pp.ParseResults
        """

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
        """
        Converts raw parsing results into a structured Expression object, specifically handling the construction of additive expressions. The method first normalizes the input by unwrapping nested list structures. If the resulting list contains a single Term, it wraps that term in an Expression; if it contains a sequence of Terms separated by addition operators, it aggregates them into a single Expression. If the token structure does not match these expected patterns, the original tokens are returned unchanged.

        :param tokens: The raw parsing result containing the terms and operators that constitute the expression.
        :type tokens: pp.ParseResults

        :return: A ParseResults object containing the constructed Expression if the tokens represent a valid single term or sum of terms, otherwise the original tokens.

        :rtype: pp.ParseResults
        """

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
        """
        Processes a set of parsing tokens representing an inequation to construct a formal constraint and update the underlying mathematical model. If the tokens contain a valid expression followed by an operator and a constant, the method normalizes the expression by subtracting the constant and determines the specific inequality type based on the operator string. It then registers this constraint within the MILP model associated with the current knowledge base. The method returns a ParseResults object wrapping the newly created Inequation instance; if the input does not start with an Expression, the tokens are returned unmodified.

        :param tokens: The parsed components of the inequation, consisting of an expression, a comparison operator, and a constant value.
        :type tokens: pp.ParseResults

        :return: A ParseResults object wrapping the parsed Inequation instance. If the input tokens do not represent a valid expression, the original tokens are returned.

        :rtype: pp.ParseResults
        """

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
        """
        This static method processes parsed tokens to apply variable constraints to the Mixed-Integer Linear Programming (MILP) model associated with the parser's knowledge base. It examines the first token to identify the constraint type; if the token indicates a binary or free variable, the method retrieves the corresponding variable object by name and updates its type definition. The function returns the original tokens unchanged, functioning as a parsing action that modifies the global model state rather than transforming the data stream.

        :param tokens: Parsed results containing the constraint definition, used to extract the variable type and identifier for updating the MILP model.
        :type tokens: pp.ParseResults

        :return: The input ParseResults object, returned unchanged.

        :rtype: pp.ParseResults
        """

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
        """
        Processes the parsed tokens of a 'show-concrete-fillers' statement to update the MILP model's display configuration. It iterates through the provided tokens, treating each as a role identifier, and validates that the role exists in the knowledge base's set of concrete roles. If the role is valid, it is added to the list of variables to be shown in the MILP model; otherwise, an error is triggered indicating that only concrete roles are supported. The method returns the original tokens to facilitate parsing pipeline continuity.

        :param tokens: The parsed tokens containing the concrete roles to be displayed in the MILP model.
        :type tokens: pp.ParseResults

        :return: The original ParseResults object containing the parsed tokens.

        :rtype: pp.ParseResults
        """

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
        """
        Processes a parsed command to identify specific concrete role fillers associated with a given individual for display in the MILP model. The method extracts the individual name from the first token and iterates over the remaining tokens, treating them as role names. For each role, it verifies its existence within the knowledge base's set of concrete roles; if valid, it updates the MILP model's configuration to include the corresponding filler variable in the output. If a role is not concrete, an error is raised. The original tokens are returned to satisfy parsing requirements.

        :param tokens: The parsed results containing the individual name followed by the list of concrete roles to display fillers for.
        :type tokens: pp.ParseResults

        :return: The original ParseResults object passed as input.

        :rtype: pp.ParseResults
        """

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
        """
        This static method processes a parsed "show-concrete-instance-for" statement to update the MILP model's variable tracking configuration. It extracts the individual name, role, and a list of concept names from the input tokens, performing strict validation to ensure the role is defined as a concrete role and that the concepts are defined as concrete fuzzy concepts or fuzzy numbers within the knowledge base. If any validation fails, an error is raised. Upon success, it modifies the global knowledge base state by adding the specified concrete fillers to the list of variables to be displayed in the MILP model. The original tokens are returned to facilitate further parsing steps.

        :param tokens: Parsed results containing the individual name, role, and concrete concepts specified in the statement.
        :type tokens: pp.ParseResults

        :return: The ParseResults object containing the parsed tokens for the show-concrete-instance-for statement.

        :rtype: pp.ParseResults
        """

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
        """
        Parses the tokens associated with a 'show-abstract-fillers' statement to update the MILP model's display configuration. The method iterates over the roles specified in the input, ensuring they are abstract; if a concrete role is detected, an error is raised and that specific role is ignored. Successfully validated abstract roles are registered within the knowledge base's MILP structure to be included in the variable output.

        :param tokens: Parsed results containing the list of role identifiers extracted from the show-abstract-fillers statement.
        :type tokens: pp.ParseResults

        :return: The input tokens, returned to satisfy the pyparsing parse action contract.

        :rtype: pp.ParseResults
        """


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
        """
        Processes a parsed 'show-abstract-fillers-for' statement to configure the MILP model output. It validates that all specified roles are abstract; if a concrete role is found, an error is raised. Upon successful validation, it registers the variables representing the fillers of these roles for the given individual within the knowledge base's MILP display configuration.

        :param tokens: Parsed result containing the abstract roles and individual name specified in the show-abstract-fillers-for statement.
        :type tokens: pp.ParseResults

        :return: The original ParseResults object containing the parsed tokens.

        :rtype: pp.ParseResults
        """

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
        """
        This static method processes the tokens resulting from a "show-concepts" statement, extracting a list of individual names. It iterates through these names and updates the MILP model's configuration by adding each individual to the set of variables designated for display. The method returns the original tokens unchanged to facilitate parsing pipeline chaining and includes debug logging if enabled.

        :param tokens: Parsed results containing the list of individual identifiers to be displayed in the MILP model.
        :type tokens: pp.ParseResults

        :return: The input ParseResults object containing the list of individual names to show.

        :rtype: pp.ParseResults
        """

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_show_concepts -> {tokens}")
        list_tokens: list = tokens.as_list()
        for ind_name in list_tokens:
            DLParser.kb.milp.show_vars.add_individual_to_show(ind_name)
        return tokens

    @staticmethod
    # @pp.trace_parse_action
    def _show_instances(tokens: pp.ParseResults) -> pp.ParseResults:
        """
        This static method processes a 'show-instances' statement by extracting the specified concepts from the parse results and registering them for display within the MILP model. It iterates through the provided tokens, converting each item into a Concept object and adding it to the model's configuration of variables to show. This operation has a side effect of modifying the internal state of the knowledge base's MILP solver to ensure the instances of these concepts are tracked. The method returns the original tokens unchanged, allowing the parsing process to continue.

        :param tokens: Parsed results from a show-instances statement, containing the concepts to be added to the MILP display list.
        :type tokens: pp.ParseResults

        :return: The original ParseResults object containing the tokens for the show-instances statement.

        :rtype: pp.ParseResults
        """


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
        """
        Processes the parsed tokens of a show-variables statement to identify and register specific variables for display. It iterates through the list of variable names contained in the input tokens, retrieves the corresponding `Variable` objects from the MILP model, and adds them to the model's collection of variables to show. This method modifies the state of the MILP model's `show_vars` attribute and assumes that all provided variable names exist within the current model context. The original tokens are returned unchanged to support parsing pipeline continuity.

        :param tokens: The parsed results containing the list of variable names extracted from the show-variables statement.
        :type tokens: pp.ParseResults

        :return: The parsed tokens representing the show-variables statement.

        :rtype: pp.ParseResults
        """

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
        """
        This static method serves as a parsing action for a "show-languages" statement, modifying the state of the global knowledge base to indicate that language information should be displayed. It sets the `show_language` attribute of the `DLParser` knowledge base to `True`. Additionally, if debug mode is active, it logs the input tokens for troubleshooting purposes. The method returns the original tokens unchanged to allow the parsing process to continue.

        :param tokens: The parsed results representing the show-languages statement.
        :type tokens: pp.ParseResults

        :return: The ParseResults object containing the parsed tokens from the show-languages statement.

        :rtype: pp.ParseResults
        """

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_show_languages -> {tokens}")
        DLParser.kb.show_language = True
        return tokens

    @staticmethod
    # @pp.trace_parse_action
    def _parse_crisp_declarations(tokens: pp.ParseResults) -> pp.ParseResults:
        """
        This static method processes parsed tokens to identify and handle crisp declarations for either concepts or roles. Based on the leading keyword in the token list, it iterates through the remaining identifiers to update the global knowledge base. If the declaration targets concepts, it converts the identifiers to Concept objects and registers them as crisp; if it targets roles, it registers the role identifiers directly. The operation modifies the state of the knowledge base and returns the original tokens unchanged.

        :param tokens: The parsed results containing the declaration type keyword followed by the identifiers of the concepts or roles to be marked as crisp.
        :type tokens: pp.ParseResults

        :return: The ParseResults object containing the parsed crisp declaration tokens.

        :rtype: pp.ParseResults
        """

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
        """
        This static method processes a fuzzy similarity relation identified during the parsing phase. It extracts the primary identifier from the provided parse results and adds it to the parser's knowledge base as a similarity relation. The method returns the original tokens unchanged, serving primarily as a side-effect trigger that updates the internal state of the knowledge base.

        :param tokens: The parsed results containing the fuzzy similarity relation data extracted from the input string.
        :type tokens: pp.ParseResults

        :return: The original ParseResults object containing the parsed tokens.

        :rtype: pp.ParseResults
        """

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_parse_fuzzy_similarity -> {tokens}")
        list_tokens: list = tokens.as_list()
        DLParser.kb.add_similarity_relation(list_tokens[0])
        return tokens

    @staticmethod
    # @pp.trace_parse_action
    def _parse_fuzzy_equivalence(tokens: pp.ParseResults) -> pp.ParseResults:
        """
        Processes the parsed tokens corresponding to a fuzzy equivalence relation and updates the global knowledge base accordingly. This static method extracts the primary identifier from the token list and invokes the knowledge base's `add_equivalence_relation` method to register the relation. While it returns the original tokens to facilitate continued parsing, its primary effect is the mutation of the shared `DLParser.kb` state.

        :param tokens: The parsed results containing the fuzzy equivalence relation to be added to the knowledge base.
        :type tokens: pp.ParseResults

        :return: The original `ParseResults` object containing the fuzzy equivalence relation tokens.

        :rtype: pp.ParseResults
        """

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_parse_fuzzy_equivalence -> {tokens}")
        list_tokens: list = tokens.as_list()
        DLParser.kb.add_equivalence_relation(list_tokens[0])
        return tokens

    @staticmethod
    # @pp.trace_parse_action
    def _parse_degree(tokens: pp.ParseResults) -> pp.ParseResults:
        """
        Converts raw parsing tokens into specific semantic Degree objects based on the type of the first token found in the input. If the token is a numeric value, the method returns a `DegreeNumeric` object; if it is an `Expression` instance, it returns a `DegreeExpression` object. For string tokens, the method consults the knowledge base to check for a defined truth constant, returning a `DegreeNumeric` if a match is found, or otherwise treating the string as a variable name to retrieve and return a `DegreeVariable`. The resulting object is wrapped in a `pp.ParseResults` container to ensure compatibility with the parsing pipeline, and debug information may be logged if enabled.

        :param tokens: The parsed output containing the raw degree data, expected to be a numeric value, an expression, or a variable name.
        :type tokens: pp.ParseResults

        :return: A ParseResults object containing the specific Degree instance (Numeric, Expression, or Variable) derived from the input tokens.

        :rtype: pp.ParseResults
        """

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
        """
        Processes a list of parsed tokens representing Description Logic axioms and updates the global knowledge base accordingly. The method inspects the leading keyword to dispatch specific logic for various axiom types, including individual assertions, role relations, concept implications (supporting multiple fuzzy logic semantics such as Goedel, Lukasiewicz, and Zadeh), concept definitions, and disjointness constraints. Additionally, it manages role characteristics like domain, range, transitivity, symmetry, and inverse relationships, performing validation to ensure concrete roles are not used in invalid contexts. Fuzzy degrees are applied to assertions and implications where provided, defaulting to 1.0 otherwise. The method returns the original tokens to facilitate parsing pipeline continuity.

        :param tokens: The parsed result containing the axiom keyword and its associated arguments (e.g., concepts, individuals, roles) to be processed and added to the knowledge base.
        :type tokens: pp.ParseResults

        :return: The original parsed tokens, returned unchanged after updating the knowledge base.

        :rtype: pp.ParseResults
        """


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
        """
        Parses a list of tokens representing a query definition and constructs the appropriate query object to be added to the parser's query list. The method identifies the specific query type—such as satisfiability, subsumption, instance checking, or defuzzification—by examining the first token. It then instantiates the corresponding query class (e.g., `KbSatisfiableQuery`, `MaxSubsumesQuery`) using subsequent tokens as arguments, converting strings to concepts or individuals as needed. During this process, it performs validation checks, such as ensuring roles are not concrete for related queries and that features are defined for defuzzification operations, raising errors if these conditions are not met. Additionally, it may update the knowledge base's abstract roles set. The method returns the original input tokens to facilitate further parsing.

        :param tokens: Parsed result containing the query keyword and its associated arguments (e.g., concepts, individuals, roles) used to construct a specific query object.
        :type tokens: pp.ParseResults

        :return: The original ParseResults object containing the query tokens.

        :rtype: pp.ParseResults
        """

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
        Constructs and returns the pyparsing grammar definition for the fuzzy Description Logic language. This static method assembles a comprehensive set of parsing rules that cover the language's syntax, including concept definitions, fuzzy logic operators, modifiers, datatype restrictions, axioms, and various query types. As a side effect, it enables left recursion support within the pyparsing library to accommodate the recursive nature of concept expressions and arithmetic operations defined in the grammar.

        :return: The root pyparsing ParserElement for the fuzzy DL language grammar, capable of parsing one or more valid statements or formulas.

        :rtype: pp.ParserElement
        """

        pp.ParserElement.enable_left_recursion(force=True)

        lbrace = pp.Literal("(").set_results_name("lbrace").suppress()
        rbrace = pp.Literal(")").set_results_name("rbrace").suppress()
        lbbrace = pp.Literal("{").set_results_name("lbbrace").suppress()
        rbbrace = pp.Literal("}").set_results_name("rbbrace").suppress()
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
                | (
                    FuzzyDLKeyword.SIGMA_COUNT.get_value().suppress()
                    + variables  # role
                    + concept
                    + lbbrace
                    + variables[1, ...]  # list of individuals
                    + rbbrace
                    + variables  # fuzzy concept name
                )
                .set_results_name("sigma_count", list_all_matches=True)
                .set_parse_action(DLParser._parse_sigma_count_concept)
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
                + (
                    lbrace
                    + (
                        inequation
                        | FuzzyDLKeyword.BINARY.get_value() + variables
                        | FuzzyDLKeyword.FREE.get_value() + variables
                    )
                    + rbrace
                )[1, ...]
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
        """
        This static method serves as the primary entry point for parsing input strings according to the grammar defined within the `DLParser` class. It retrieves the compiled grammar structure and attempts to match the entire input string, ensuring that no unparsed trailing characters remain; consequently, the operation will fail if the input does not fully conform to the grammar from start to finish. The method is decorated to handle unlimited recursion, allowing it to process deeply nested structures without hitting Python's recursion limit. Upon successful parsing, it returns a `pyparsing.ParseResults` object containing the structured data extracted from the input.

        :param instring: The text content to be parsed according to the defined grammar.
        :type instring: str

        :return: A `ParseResults` object containing the structured tokens extracted from the input string, representing a successful parse of the entire input against the defined grammar.

        :rtype: pp.ParseResults
        """

        return DLParser.get_grammatics().parse_string(instring, parse_all=True)

    @staticmethod
    @utils.recursion_unlimited
    def parse_string_opt(
        filename: str,
    ) -> pp.ParseResults:
        """
        Reads the entire content of the file located at the specified path and processes it using the parser's defined grammar. The specific operation performed depends on the `DEBUG_PRINT` configuration flag: when disabled, the method executes a standard parse and returns the resulting structure; when enabled, it runs a test suite on the input string and writes the diagnostic output to a log file. This method involves file I/O operations and may raise exceptions if the file is inaccessible or if the input string fails to match the grammar rules.

        :param filename: Path to the file containing the content to be parsed.
        :type filename: str

        :return: A ParseResults object containing the results of parsing the file content according to the defined grammar.

        :rtype: pp.ParseResults
        """

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
        """
        This static method acts as a wrapper to load specific configuration parameters from a predefined INI file located in the current working directory. It constructs the file path for 'CONFIG.ini' and delegates the actual parsing and parameter extraction to the `ConfigReader` class, passing along the provided arguments to determine which specific settings to retrieve. The function relies on the presence of the configuration file in the file system and triggers side effects within the `ConfigReader` rather than returning a value directly. By accepting a variable length argument list, it allows for selective loading of configuration data based on the caller's needs.

        :param args: Keys specifying which configuration parameters to load from the file.
        :type args: typing.Any
        """

        ConfigReader.load_parameters(os.path.join(os.getcwd(), "CONFIG.ini"), args)

    @staticmethod
    def get_kb(*args) -> tuple[KnowledgeBase, list[Query]]:
        """
        Parses the input file specified by the arguments to construct a Knowledge Base and a list of Queries, initializing the necessary configuration and internal state. This method resets the class-level knowledge base and query list, sets the global logic semantics to Łukasiewicz fuzzy logic, and processes the file content using either a verbose line-by-line approach or an optimized path based on the debug configuration. It returns a tuple containing the populated `KnowledgeBase` object and the list of `Query` objects. Significant side effects include updates to class attributes and global constants; errors such as missing files or parsing failures are caught and logged rather than raised, resulting in a return value of None in those cases.

        :param args: Variable-length arguments where the first argument is the path to the input file, and any remaining arguments are passed to the configuration loader.
        :type args: typing.Any

        :return: A tuple containing the KnowledgeBase instance and the list of Query instances parsed from the input file.

        :rtype: tuple[KnowledgeBase, list[Query]]
        """


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
        """
        Serves as the primary entry point for the DLParser program, orchestrating the loading, solving, and querying of a fuzzy description logic knowledge base. It accepts variable arguments to configure the loading process, retrieving the knowledge base and a list of queries via the `get_kb` method. The method first solves the knowledge base to prepare it for inference, then iterates through each query to generate solutions. Special handling is provided for `AllInstancesQuery` instances when the knowledge base lacks individuals, logging a specific informational message. For general queries, it evaluates consistency and logs the solution or a default value of 1.0 if the knowledge base is inconsistent. Additionally, it logs execution time and optionally the description logic language used. The method includes robust error handling, catching ontology inconsistency exceptions to report a default answer and logging stack traces for unexpected errors.

        :param args: Variable length positional arguments used to specify configuration parameters and the input file for parsing.
        :type args: typing.Any
        """


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
