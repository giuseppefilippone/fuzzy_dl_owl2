from __future__ import annotations

import os
import typing
from functools import reduce

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
from fuzzy_dl_owl2.fuzzydl.degree.degree_variable import DegreeVariable  # Variable
from fuzzy_dl_owl2.fuzzydl.feature_function import FeatureFunction
from fuzzy_dl_owl2.fuzzydl.individual.individual import Individual
from fuzzy_dl_owl2.fuzzydl.knowledge_base import KnowledgeBase
from fuzzy_dl_owl2.fuzzydl.milp.expression import Expression
from fuzzy_dl_owl2.fuzzydl.milp.inequation import Inequation  # Inequation
from fuzzy_dl_owl2.fuzzydl.milp.term import Term  # Term
from fuzzy_dl_owl2.fuzzydl.milp.variable import Variable  # Variable
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
from fuzzy_dl_owl2.fuzzydl.util import constants
from fuzzy_dl_owl2.fuzzydl.util.config_reader import ConfigReader
from fuzzy_dl_owl2.fuzzydl.util.constants import VariableType  # Variable
from fuzzy_dl_owl2.fuzzydl.util.constants import (
    ConceptType,
    ConcreteFeatureType,
    FuzzyDLKeyword,
    FuzzyLogic,
    InequalityType,
    LogicOperatorType,
    RestrictionType,
)
from fuzzy_dl_owl2.fuzzydl.util.util import Util
from fuzzy_dl_owl2.fuzzydl.util.utils import class_debugging


@class_debugging()
class DLParser(object):
    """
    This class holds the semantic callbacks for the Fuzzy Description Logic parser, transforming raw string tokens into domain-specific objects such as `Concept`, `Individual`, and `Degree` instances. It is pyparsing-free: each static `_parse_*` method consumes a token list and either returns a constructed object (`Concept`, `Term`, `Degree`, `Expression`, `Inequation`, ...) or mutates the shared `KnowledgeBase` in place (side-effect callbacks return `None`). The hand-written recursive-descent driver in `dl_parser_fast.py` invokes these callbacks while walking the input. The class handles semantic validation and logic-specific constraints (e.g., distinguishing between Zadeh and Lukasiewicz logic), ensuring that the constructed knowledge base adheres to the specified fuzzy logic semantics. Parsed queries are accumulated in `queries_list`.

    :param kb: The KnowledgeBase instance constructed and populated by the parser with the parsed domain model.
    :type kb: KnowledgeBase
    :param queries_list: Accumulates Query objects extracted from the input during parsing, which are subsequently returned for execution against the knowledge base.
    :type queries_list: list[Query]
    """

    kb: KnowledgeBase = None
    queries_list: list[Query] = []

    @staticmethod
    def _is_non_decreasing(v: list[typing.Any]) -> bool:
        """
        Utility method to check if a list is sorted in non-decreasing order. It iterates through the list and compares each element with the next one, returning `False` if it finds any pair of elements that are out of order. If the entire list is traversed without finding any such pair, it returns `True`, indicating that the list is sorted.

        :param v: The list to be checked for sorted order.
        :type v: list[typing.Any]

        :return: A boolean value indicating whether the list is sorted in non-decreasing order.
        :rtype: bool
        """
        for i in range(len(v) - 1):
            if v[i] > v[i + 1]:
                return False
        return True

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
    def _to_number(tokens: list) -> float | int:
        """
        Converts the first element of the provided parse results into a numeric type, prioritizing integers when appropriate. The method extracts the initial token, ensures it is a string, and attempts to parse it as a floating-point number. If the parsed value is mathematically an integer, it is returned as an `int`; otherwise, it is returned as a `float`. This function assumes the input token represents a valid numeric string and will raise a `ValueError` if the conversion fails.

        :param tokens: The parsed results containing the string representation of the number to be converted.
        :type tokens: list

        :return: The numeric representation of the input token, returned as an int if the value is a whole number, or as a float otherwise.

        :rtype: float | int
        """

        v: float = float(str(tokens[0]))
        return int(v) if v.is_integer() else v

    @staticmethod
    def _fuzzy_logic_parser(tokens: list) -> None:
        """
        This static method acts as a semantic callback to process and apply a specified fuzzy logic type to the system. It extracts the first token, converts it to a lowercase string, and instantiates a corresponding FuzzyLogic object. The method then updates the Knowledge Base associated with the parser by setting this logic, effectively configuring the reasoning engine for the session. It assumes the input grammar guarantees the presence of at least one token to define the logic.

        :param tokens: The tokens containing the identifier for the fuzzy logic type to be applied to the knowledge base.
        :type tokens: list
        """

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_fuzzy_logic_parser -> {tokens}")
        DLParser.kb.set_logic(FuzzyLogic(str(tokens[0]).lower()))

    @staticmethod
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
    def _to_top_bottom_concept(tokens: list) -> Concept:
        """
        Transforms the provided parse results into a specific concept object based on the content of the first token. If the token corresponds to the 'TOP' keyword, the method returns the universal truth concept; if it corresponds to 'BOTTOM', it returns the empty truth concept. For any other token, the method delegates the conversion to the internal `_to_concept` method to generate a standard Description Logic concept. The method may output debug information depending on the global configuration settings.

        :param tokens: Parsed results containing a keyword or identifier representing a top, bottom, or regular concept.
        :type tokens: list

        :return: A Concept object representing the Top concept, Bottom concept, or a regular concept derived from the input tokens.

        :rtype: Concept
        """

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_to_top_bottom_concept -> {tokens}")
        if tokens[0] == FuzzyDLKeyword.TOP:
            return TruthConcept.get_top()
        elif tokens[0] == FuzzyDLKeyword.BOTTOM:
            return TruthConcept.get_bottom()
        else:
            return DLParser._to_concept(tokens[0])

    @staticmethod
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
    def _parse_binary_concept(tokens: list) -> Concept:
        """
        Parses a binary or n-ary concept expression from the provided parse results, identifying the specific operation based on the first token. The method handles a variety of logical constructs, including conjunctions, disjunctions, implications, quantifiers, value restrictions, and approximation operators, dynamically selecting the appropriate implementation (e.g., Lukasiewicz, Goedel, or Zadeh) based on the current fuzzy logic setting in the knowledge base. It validates that operands are abstract concepts, ensures referenced roles and individuals exist, and enforces logic-specific constraints by raising errors if fuzzy-specific operators are used within a classical logic context. If the operator token is already a Concept object, the method returns the input tokens unchanged.

        :param tokens: The parsed structure containing the operator and operands for the binary concept.
        :type tokens: list

        :return: The specific Concept instance (e.g., OperatorConcept, ImpliesConcept) constructed from the input tokens.

        :rtype: Concept
        """

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_parse_binary_concept -> {tokens}")
        operator: typing.Any = tokens[0]
        if isinstance(operator, Concept):
            return operator
        if operator == FuzzyDLKeyword.AND:
            tokens: list[Concept] = [DLParser._to_concept(t) for t in tokens[1:]]
            for c in tokens:
                DLParser._check_abstract(c)
            if len(tokens) == 1:
                return tokens[0]
            if DLParser.kb.get_logic() == FuzzyLogic.LUKASIEWICZ:
                return OperatorConcept.lukasiewicz_and(*tokens)
            elif DLParser.kb.get_logic() == FuzzyLogic.ZADEH:
                return OperatorConcept.goedel_and(*tokens)
            return OperatorConcept.and_(*tokens)
        elif operator == FuzzyDLKeyword.LUKASIEWICZ_AND:
            tokens: list[Concept] = [DLParser._to_concept(t) for t in tokens[1:]]
            if DLParser.kb.get_logic() == FuzzyLogic.CLASSICAL:
                Util.error(
                    "Error: LUKASIEWICZ_AND cannot be used under classical reasoner."
                )
            for c in tokens:
                DLParser._check_abstract(c)
            if len(tokens) == 1:
                return tokens[0]
            return OperatorConcept.lukasiewicz_and(*tokens)
        elif operator == FuzzyDLKeyword.GOEDEL_AND:
            tokens: list[Concept] = [DLParser._to_concept(t) for t in tokens[1:]]
            if DLParser.kb.get_logic() == FuzzyLogic.CLASSICAL:
                Util.error("Error: GOEDEL_AND cannot be used under classical reasoner.")
            for c in tokens:
                DLParser._check_abstract(c)
            if len(tokens) == 1:
                return tokens[0]
            return OperatorConcept.goedel_and(*tokens)
        elif operator == FuzzyDLKeyword.OR:
            tokens: list[Concept] = [DLParser._to_concept(t) for t in tokens[1:]]
            for c in tokens:
                DLParser._check_abstract(c)
            if len(tokens) == 1:
                return tokens[0]
            if DLParser.kb.get_logic() == FuzzyLogic.LUKASIEWICZ:
                return OperatorConcept.lukasiewicz_or(*tokens)
            elif DLParser.kb.get_logic() == FuzzyLogic.ZADEH:
                return OperatorConcept.goedel_or(*tokens)
            return OperatorConcept.or_(*tokens)
        elif operator == FuzzyDLKeyword.LUKASIEWICZ_OR:
            tokens: list[Concept] = [DLParser._to_concept(t) for t in tokens[1:]]
            if DLParser.kb.get_logic() == FuzzyLogic.CLASSICAL:
                Util.error(
                    "Error: LUKASIEWICZ_OR cannot be used under classical reasoner."
                )
            for c in tokens:
                DLParser._check_abstract(c)
            if len(tokens) == 1:
                return tokens[0]
            return OperatorConcept.lukasiewicz_or(*tokens)
        elif operator == FuzzyDLKeyword.GOEDEL_OR:
            tokens: list[Concept] = [DLParser._to_concept(t) for t in tokens[1:]]
            if DLParser.kb.get_logic() == FuzzyLogic.CLASSICAL:
                Util.error("Error: GOEDEL_OR cannot be used under classical reasoner.")
            for c in tokens:
                DLParser._check_abstract(c)
            if len(tokens) == 1:
                return tokens[0]
            return OperatorConcept.goedel_or(*tokens)
        elif operator in (
            FuzzyDLKeyword.IMPLIES,
            FuzzyDLKeyword.GOEDEL_IMPLIES,
            FuzzyDLKeyword.LUKASIEWICZ_IMPLIES,
            FuzzyDLKeyword.ZADEH_IMPLIES,
            FuzzyDLKeyword.KLEENE_DIENES_IMPLIES,
        ):
            tokens: list[Concept] = [DLParser._to_concept(t) for t in tokens[1:]]
            for c in tokens:
                DLParser._check_abstract(c)
            if len(tokens) == 1:
                return tokens[0]
            # degree: Degree = tokens[2] if len(tokens) == 3 else DegreeNumeric.get_one()
            # if operator == FuzzyDLKeyword.IMPLIES:
            #     return DLParser.kb.implies(tokens[0], tokens[1], degree)
            # elif operator == FuzzyDLKeyword.GOEDEL_IMPLIES:
            #     return DLParser.kb.goedel_implies(tokens[0], tokens[1], degree)
            # elif operator == FuzzyDLKeyword.LUKASIEWICZ_IMPLIES:
            #     return DLParser.kb.lukasiewicz_implies(tokens[0], tokens[1], degree)
            # elif operator == FuzzyDLKeyword.ZADEH_IMPLIES:
            #     return DLParser.kb.zadeh_implies(tokens[0], tokens[1])
            # elif operator == FuzzyDLKeyword.KLEENE_DIENES_IMPLIES:
            #     return DLParser.kb.kleene_dienes_implies(tokens[0], tokens[1], degree)
            if DLParser.kb.get_logic() == FuzzyLogic.ZADEH:
                return ImpliesConcept.zadeh_implies(tokens[0], tokens[1])
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
                return ImpliesConcept.goedel_implies(tokens[0], tokens[1])
            elif operator == FuzzyDLKeyword.ZADEH_IMPLIES:
                return ImpliesConcept.zadeh_implies(tokens[0], tokens[1])
            elif operator == FuzzyDLKeyword.KLEENE_DIENES_IMPLIES:
                return ImpliesConcept.kleene_dienes_implies(tokens[0], tokens[1])
            return ImpliesConcept.lukasiewicz_implies(tokens[0], tokens[1])
        elif operator == FuzzyDLKeyword.ALL:
            role: str = tokens[1]
            concept: Concept = DLParser._to_concept(tokens[2])
            DLParser.kb.check_role(role, concept)
            return AllSomeConcept.all(role, concept)
        elif operator == FuzzyDLKeyword.SOME:
            c: Concept = DLParser._to_concept(tokens[2])
            role: str = tokens[1]
            DLParser.kb.check_role(role, c)
            return AllSomeConcept.some(role, c)
        elif operator == FuzzyDLKeyword.HAS_VALUE:
            role: str = tokens[1]
            ind: Individual = DLParser.kb.get_individual(tokens[2])
            DLParser.kb.check_role(role, TruthConcept.get_top())
            return HasValueConcept.has_value(role, ind)
        elif operator in (
            FuzzyDLKeyword.TIGHT_UPPER_APPROXIMATION,
            FuzzyDLKeyword.TIGHT_LOWER_APPROXIMATION,
            FuzzyDLKeyword.UPPER_APPROXIMATION,
            FuzzyDLKeyword.LOWER_APPROXIMATION,
            FuzzyDLKeyword.LOOSE_UPPER_APPROXIMATION,
            FuzzyDLKeyword.LOOSE_LOWER_APPROXIMATION,
        ):
            role: str = tokens[1]
            concept: Concept = DLParser._to_concept(tokens[2])
            if role not in DLParser.kb.similarity_relations:
                Util.error(f"Error: Similarity relation {role} has not been defined.")

            if operator == FuzzyDLKeyword.TIGHT_UPPER_APPROXIMATION:
                return ApproximationConcept.tight_upper_approx(
                    role, concept
                ).to_all_some_concept()
            elif operator == FuzzyDLKeyword.TIGHT_LOWER_APPROXIMATION:
                return ApproximationConcept.tight_lower_approx(
                    role, concept
                ).to_all_some_concept()
            elif operator == FuzzyDLKeyword.UPPER_APPROXIMATION:
                return ApproximationConcept.upper_approx(
                    role, concept
                ).to_all_some_concept()
            elif operator == FuzzyDLKeyword.LOWER_APPROXIMATION:
                return ApproximationConcept.lower_approx(
                    role, concept
                ).to_all_some_concept()
            elif operator == FuzzyDLKeyword.LOOSE_UPPER_APPROXIMATION:
                return ApproximationConcept.loose_upper_approx(
                    role, concept
                ).to_all_some_concept()
            elif operator == FuzzyDLKeyword.LOOSE_LOWER_APPROXIMATION:
                return ApproximationConcept.loose_lower_approx(
                    role, concept
                ).to_all_some_concept()

    @staticmethod
    def _parse_unary_concept(tokens: list) -> Concept:
        """
        This static method processes a parsed unary concept expression, transforming raw tokens into a specific Concept object based on the operator provided. If the operator is a negation (NOT), it retrieves the operand concept, converts it to a Concept object, and returns its negation. If the operator is a self-reference (SELF), it validates that the associated role is not concrete, registers the role as abstract within the global knowledge base, and constructs a SelfConcept instance. The method modifies the global knowledge base by adding roles to the set of abstract roles when processing self-concepts, and it raises an error if a self-concept is applied to a concrete role.

        :param tokens: The parsed input containing the unary operator and the concept or role it modifies.
        :type tokens: list

        :return: The constructed unary concept, such as a negated concept or a self-concept.

        :rtype: Concept
        """

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_parse_unary_concept -> {tokens}")
        tokens: list[str] = tokens
        operator: str = tokens[0]
        if operator == FuzzyDLKeyword.NOT:
            concept: Concept = DLParser._to_concept(tokens[1])
            return -concept
        elif operator == FuzzyDLKeyword.SELF:
            role: str = tokens[1]
            if role in DLParser.kb.concrete_roles:
                Util.error(f"Error: Role {role} cannot be concrete and abstract.")
            DLParser.kb.abstract_roles.add(role)
            return SelfConcept.self(role)

    @staticmethod
    def _parse_modifier_concept(tokens: list) -> Concept:
        """
        This static method processes a sequence of tokens representing a modifier applied to a concept, expecting the input list to contain exactly two elements. It extracts the modifier from the first token and the base concept from the second, resolving them into their respective object instances. The method then applies the modification logic to the concept and returns the resulting modified concept.

        :param tokens: The parsed tokens containing the modifier and concept components to be combined.
        :type tokens: list

        :return: The Concept resulting from applying the parsed Modifier to the parsed Concept.

        :rtype: Concept
        """

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_parse_modifier_concept -> {tokens}")
        tokens: list[str] = tokens
        mod: Modifier = DLParser._get_modifier(tokens[0])
        concept: Concept = DLParser._to_concept(tokens[1])
        return mod.modify(concept)

    @staticmethod
    def _parse_threshold_concept(tokens: list) -> Concept:
        """
        Parses a threshold concept definition from the provided tokens and constructs the corresponding concept object. The method expects a token list containing a comparison operator, a threshold value (which can be a numeric literal or a string representing a MILP variable), and a concept identifier. It converts the identifier to a Concept instance, validates that the concept is not abstract, and then instantiates either a standard ThresholdConcept or an ExtThresholdConcept based on the operator type and value type. If debug printing is enabled, the input tokens are logged to the console.

        :param tokens: The parsed elements of a threshold expression, structured as an operator, a threshold value (numeric or variable), and a concept.
        :type tokens: list

        :return: The ThresholdConcept or ExtThresholdConcept built from the threshold expression.

        :rtype: Concept
        """

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_parse_threshold_concept -> {tokens}")
        tokens: list[str] = tokens
        operator: str = tokens[0]
        concept: Concept = DLParser._to_concept(tokens[2])
        DLParser._check_abstract(concept)
        if operator == FuzzyDLKeyword.GREATER_THAN_OR_EQUAL_TO:
            if isinstance(tokens[1], (int, float)):
                return ThresholdConcept.pos_threshold(tokens[1], concept)
            elif isinstance(tokens[1], str):
                return ExtThresholdConcept.extended_pos_threshold(
                    DLParser.kb.milp.get_variable(tokens[1]), concept
                )
        elif operator == FuzzyDLKeyword.LESS_THAN_OR_EQUAL_TO:
            if isinstance(tokens[1], (int, float)):
                return ThresholdConcept.neg_threshold(tokens[1], concept)
            elif isinstance(tokens[1], str):
                return ExtThresholdConcept.extended_neg_threshold(
                    DLParser.kb.milp.get_variable(tokens[1]), concept
                )

    @staticmethod
    def _parse_weighted_concept_simple(tokens: list) -> Concept:
        """
        This static method processes a sequence of parsed tokens to construct a WeightedConcept object, typically serving as a semantic callback. It extracts the first token as a floating-point weight and converts the second token into a Concept object using the `_to_concept` helper method. The method assumes the input tokens contain at least two elements and may output debug information if the debug flag is enabled.

        :param tokens: The parsed elements containing the weight and concept string, where the first element is the weight and the second is the concept.
        :type tokens: list

        :return: The constructed WeightedConcept instance.

        :rtype: Concept
        """

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_parse_weighted_concept_simple -> {tokens}")
        tokens: list[str] = tokens
        weight: float = tokens[0]
        concept: Concept = DLParser._to_concept(tokens[1])
        return WeightedConcept(weight, concept)

    @staticmethod
    def _parse_weighted_concept(tokens: list) -> Concept:
        """
        Parses a weighted concept expression from the provided tokens, expecting the first token to be an operator and subsequent tokens to be WeightedConcept instances. It extracts the weights and underlying concepts, then validates them based on the specific operator type: sum-based operators require the total weight to be less than or equal to 1.0, while min/max operators require the maximum weight to be exactly 1.0. If validation fails, an error is triggered via the utility function. Upon success, it returns the appropriate specialized concept object, such as WeightedSumConcept or WeightedMaxConcept.

        :param tokens: Tokens containing an operator keyword and a list of WeightedConcept objects to be combined.
        :type tokens: list

        :return: The constructed weighted concept (WeightedSumConcept, WeightedMaxConcept, WeightedMinConcept, or WeightedSumZeroConcept) based on the parsed operator.

        :rtype: Concept
        """

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_parse_weighted_concept -> {tokens}")
        tokens: list[str] = tokens
        operator: str = tokens[0]
        assert all(isinstance(c, WeightedConcept) for c in tokens[1:])
        weights: list[float] = list(map(lambda x: x.weight, tokens[1:]))
        concepts: list[Concept] = [
            DLParser._to_concept(w_concept.curr_concept) for w_concept in tokens[1:]
        ]
        if min(weights) < 0.0:
            Util.error("Error: The weights must be non-negative.")
        if max(weights) > 1.0:
            Util.error("Error: The weights must be less than or equal to 1.")

        if operator == FuzzyDLKeyword.W_SUM:
            if not (sum(weights) <= 1.0):
                Util.error(
                    "Error: The sum of the weights must be lower than or equal to 1."
                )
            return WeightedSumConcept(weights, concepts)
        elif operator == FuzzyDLKeyword.W_MAX:
            if max(weights) != 1.0:
                Util.error("Error: The maximum of the weights must be equal to 1.")
            return WeightedMaxConcept(weights, concepts)
        elif operator == FuzzyDLKeyword.W_MIN:
            if max(weights) != 1.0:
                Util.error("Error: The maximum of the weights must be equal to 1.")
            return WeightedMinConcept(weights, concepts)
        elif operator == FuzzyDLKeyword.W_SUM_ZERO:
            if not (sum(weights) <= 1.0):
                Util.error(
                    "Error: The sum of the weights must be lower than or equal to 1."
                )
            return WeightedSumZeroConcept(weights, concepts)

    @staticmethod
    def _parse_q_owa_concept(tokens: list) -> Concept:
        """
        This static method processes a sequence of tokens to construct a Quantified OWA (Ordered Weighted Averaging) concept. It interprets the first token as the name of a fuzzy concrete concept, retrieving it from the knowledge base to serve as the aggregation function. The method enforces strict type checking, ensuring the retrieved function is either a `RightConcreteConcept` or `LeftConcreteConcept`, and triggers an error if the concept is undefined or of an incorrect type. Subsequent tokens are recursively parsed into standard `Concept` objects to serve as arguments. Finally, it returns the fully initialized `QowaConcept`.

        :param tokens: Tokens representing the components of a Q-OWA concept, comprising a fuzzy aggregation function identifier and a list of concepts to aggregate.
        :type tokens: list

        :return: The constructed QowaConcept instance.

        :rtype: Concept
        """

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_parse_q_owa_concept -> {tokens}")
        tokens: list[str] = tokens
        f: FuzzyConcreteConcept = DLParser.kb.concrete_concepts.get(tokens[0])
        if f is None:
            Util.error(f"Error: Fuzzy concept {f} has to be defined before being used.")
        if not isinstance(f, (RightConcreteConcept, LeftConcreteConcept)):
            Util.error(f"Error: Fuzzy concept {f} has to be a right or left functions.")
        concepts: list[Concept] = [
            DLParser._to_concept(concept) for concept in tokens[1:]
        ]
        return QowaConcept(f, concepts)

    @staticmethod
    def _parse_owa_integral_concept(tokens: list) -> Concept:
        """
        Parses a fuzzy logic integral concept—specifically OWA, Choquet, Sugeno, or Q-Sugeno—from the provided tokens. The method extracts the operator from the first token and divides the remaining tokens into two equal lists representing weights and concepts, converting the latter into `Concept` objects. It performs validation on the weights, ensuring they sum to 1.0 for OWA operators and that the maximum weight is 1.0 for Choquet, Sugeno, and Q-Sugeno operators, reporting an error if these conditions are not met. The result is the appropriate specialized concept instance.

        :param tokens: The tokens containing the integral operator, associated weights, and the list of concepts to be aggregated.
        :type tokens: list

        :return: The specific integral concept instance (OwaConcept, ChoquetIntegral, SugenoIntegral, or QsugenoIntegral) parsed from the input tokens.

        :rtype: Concept
        """

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_parse_owa_integral_concept -> {tokens}")
        tokens: list[str] = tokens
        operator: str = tokens[0]
        length: int = len(tokens) - 1
        assert length % 2 == 0
        weights: list[float] = tokens[1:][: length // 2]
        concepts: list[Concept] = [
            DLParser._to_concept(concept) for concept in tokens[1:][length // 2 :]
        ]
        if min(weights) < 0.0:
            Util.error("Error: The weights must be non-negative.")
        if max(weights) > 1.0:
            Util.error("Error: The weights must be less than or equal to 1.")

        if operator == FuzzyDLKeyword.OWA:
            if sum(weights) != 1.0:
                Util.error("Error: The sum of the weights must be equal to 1.")
            return OwaConcept(weights, concepts)
        elif operator == FuzzyDLKeyword.CHOQUET:
            if not DLParser._is_non_decreasing(weights):
                Util.error("Error: The weights must be in non-decreasing order.")
            if max(weights) != 1.0:
                Util.error("Error: The maximum of the weights must be equal to 1.")
            return ChoquetIntegral(weights, concepts)
        elif operator == FuzzyDLKeyword.SUGENO:
            if not DLParser._is_non_decreasing(weights):
                Util.error("Error: The weights must be in non-decreasing order.")
            if max(weights) != 1.0:
                Util.error("Error: The maximum of the weights must be equal to 1.")
            return SugenoIntegral(weights, concepts)
        elif operator == FuzzyDLKeyword.QUASI_SUGENO:
            if not DLParser._is_non_decreasing(weights):
                Util.error("Error: The weights must be in non-decreasing order.")
            if max(weights) != 1.0:
                Util.error("Error: The maximum of the weights must be equal to 1.")
            return QsugenoIntegral(weights, concepts)

    @staticmethod
    def _parse_sigma_count_concept(tokens: list) -> Concept:
        """
        Parses a sequence of tokens to construct a SigmaConcept, which represents a sigma count operation involving a specific role, concept, and set of individuals. The method extracts the role, the base concept, and a list of individuals from the input tokens, while the final token identifies a fuzzy concept used for the sigma count calculation. It performs validation to ensure the specified fuzzy concept exists in the knowledge base and is a concrete function type (specifically Left, Right, or Triangular), raising an error if these conditions are not met.

        :param tokens: The parsed output containing the role, concept, individuals, and fuzzy concept name required to construct a SigmaConcept.
        :type tokens: list

        :return: The `SigmaConcept` instance constructed from the parsed tokens.

        :rtype: Concept
        """

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_parse_sigma_count_concept -> {tokens}")
        tokens: list[str] = tokens
        role: str = tokens[0]
        concept: Concept = DLParser._to_concept(tokens[1])
        individuals: list[Individual] = [
            # DLParser.kb.get_individual(token) for token in tokens[2:-1]
            DLParser.kb.get_individual(token)
            for token in tokens[2 : len(tokens) - 1]
        ]
        # concept_name: str = tokens[-1]
        concept_name: str = tokens[len(tokens) - 1]
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
        return SigmaConcept(concept, role, individuals, fuzzy_concept)

    @staticmethod
    def _parse_modifier(tokens: list) -> None:
        """
        This static method processes a parsed modifier definition by extracting the modifier type and parameters from the provided tokens. It distinguishes between linear and triangular modifiers based on the specific keyword present, instantiating the corresponding `LinearModifier` or `TriangularModifier` object with the extracted arguments. The constructed modifier is then registered with the global knowledge base (`DLParser.kb`), effectively updating the application's state. The method assumes the input list contains sufficient elements for the specific modifier type, potentially raising an error if the token structure is invalid.

        :param tokens: The parsed components of a modifier definition, including the name, type keyword, and associated parameters.
        :type tokens: list
        """

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_parse_modifier -> {tokens}")

        tokens: list[str] = tokens
        if tokens[1] == FuzzyDLKeyword.LINEAR_MODIFIER:
            DLParser.kb.add_modifier(tokens[0], LinearModifier(tokens[0], tokens[2]))
        elif tokens[1] == FuzzyDLKeyword.TRIANGULAR_MODIFIER:
            DLParser.kb.add_modifier(
                tokens[0],
                TriangularModifier(tokens[0], tokens[2], tokens[3], tokens[4]),
            )

    @staticmethod
    def _parse_truth_constants(tokens: list) -> None:
        """
        This static method serves as a semantic callback that processes tokens matched by a grammar rule for truth constants. It extracts the first two elements from the tokens and updates the class-level knowledge base by invoking `set_truth_constants` with these values. It assumes the input list contains at least two elements.

        :param tokens: The tokens containing the truth constant values to be set in the knowledge base.
        :type tokens: list
        """

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_parse_truth_constants -> {tokens}")
        tokens: list[str] = tokens
        DLParser.kb.set_truth_constants(tokens[0], tokens[1])

    @staticmethod
    def _parse_fuzzy_concept(tokens: list) -> None:
        """
        Parses a fuzzy concept definition from the provided tokens and registers the corresponding concrete concept object in the global knowledge base. The method validates that the concept name is not already defined and ensures that non-crisp concept types are not used with a classical reasoner. Depending on the keyword found in the tokens, it instantiates a specific concept class—such as `CrispConcreteConcept`, `TriangularConcreteConcept`, or `ModifiedConcreteConcept`—using the extracted parameters. For modified concepts, it verifies that the base concept exists prior to creation. As a side effect, adding a non-crisp concept sets a flag in the knowledge base indicating the presence of concrete fuzzy concepts.

        :param tokens: Tokens containing the fuzzy concept definition, including the concept name, type keyword, and associated parameters or references.
        :type tokens: list
        """

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_parse_fuzzy_concept -> {tokens}")

        if DLParser.kb.concrete_concepts.get(tokens[0]) is not None:
            Util.error(
                f"Error: Fuzzy concept {tokens[0]} has to be defined before being used."
            )
        if (
            tokens[1] != FuzzyDLKeyword.CRISP
            and DLParser.kb.get_logic() == FuzzyLogic.CLASSICAL
        ):
            Util.error(
                f"Error: Fuzzy concept {tokens[0]} cannot be used with the classical reasoner."
            )
        if tokens[1] == FuzzyDLKeyword.CRISP:
            DLParser.kb.add_concept(
                tokens[0],
                CrispConcreteConcept(
                    tokens[0],
                    tokens[2],
                    tokens[3],
                    tokens[4],
                    tokens[5],
                ),
            )
        elif tokens[1] == FuzzyDLKeyword.LEFT_SHOULDER:
            DLParser.kb.add_concept(
                tokens[0],
                LeftConcreteConcept(
                    tokens[0],
                    tokens[2],
                    tokens[3],
                    tokens[4],
                    tokens[5],
                ),
            )
            DLParser.kb.concrete_fuzzy_concepts = True
        elif tokens[1] == FuzzyDLKeyword.RIGHT_SHOULDER:
            DLParser.kb.add_concept(
                tokens[0],
                RightConcreteConcept(
                    tokens[0],
                    tokens[2],
                    tokens[3],
                    tokens[4],
                    tokens[5],
                ),
            )
            DLParser.kb.concrete_fuzzy_concepts = True
        elif tokens[1] == FuzzyDLKeyword.TRIANGULAR:
            DLParser.kb.add_concept(
                tokens[0],
                TriangularConcreteConcept(
                    tokens[0],
                    tokens[2],
                    tokens[3],
                    tokens[4],
                    tokens[5],
                    tokens[6],
                ),
            )
            DLParser.kb.concrete_fuzzy_concepts = True
        elif tokens[1] == FuzzyDLKeyword.TRAPEZOIDAL:
            DLParser.kb.add_concept(
                tokens[0],
                TrapezoidalConcreteConcept(
                    tokens[0],
                    tokens[2],
                    tokens[3],
                    tokens[4],
                    tokens[5],
                    tokens[6],
                    tokens[7],
                ),
            )
            DLParser.kb.concrete_fuzzy_concepts = True
        elif tokens[1] == FuzzyDLKeyword.LINEAR:
            DLParser.kb.add_concept(
                tokens[0],
                LinearConcreteConcept(
                    tokens[0],
                    tokens[2],
                    tokens[3],
                    tokens[4],
                    tokens[5],
                ),
            )
            DLParser.kb.concrete_fuzzy_concepts = True
        elif tokens[1] == FuzzyDLKeyword.MODIFIED:
            mod: Modifier = DLParser._get_modifier(tokens[2])
            if DLParser.kb.concrete_concepts.get(tokens[3]) is None:
                Util.error(
                    f"Error: Fuzzy concept {tokens[3]} has to be defined before being used."
                )
            DLParser.kb.add_concept(
                tokens[0],
                ModifiedConcreteConcept(
                    tokens[0],
                    mod,
                    DLParser.kb.concrete_concepts.get(tokens[3]),
                ),
            )
            DLParser.kb.concrete_fuzzy_concepts = True

    @staticmethod
    def _parse_fuzzy_number_range(tokens: list) -> None:
        """
        Extracts the lower and upper bounds from the provided tokens to configure the range for triangular fuzzy numbers. This static method invokes the `TriangularFuzzyNumber.set_range` method with the first two elements, resulting in a side effect that updates the class-level state. It assumes the input contains at least two elements to define the range boundaries.

        :param tokens: The tokens containing the values that define the fuzzy number range.
        :type tokens: list
        """

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_parse_fuzzy_number_range -> {tokens}")
        tokens = tokens
        TriangularFuzzyNumber.set_range(tokens[0], tokens[1])

    @staticmethod
    def _create_fuzzy_number(tokens: list) -> TriangularFuzzyNumber:
        """
        This static method processes parse tokens to construct a `TriangularFuzzyNumber` instance, supporting multiple input formats. If a single numeric value is provided, it generates a crisp fuzzy number where the lower, middle, and upper bounds are equal. When a string identifier is encountered, the method retrieves the corresponding fuzzy number from the knowledge base; if the identifier is undefined, an error is triggered. If three numeric values are present, they are interpreted as the lower, middle, and upper bounds of the triangular distribution. The method also outputs debug information if the global debug flag is enabled.

        :param tokens: The parsed elements representing a fuzzy number, which can be a single numeric value, a string identifier referencing a predefined number, or a list of three numeric values.
        :type tokens: list

        :return: A TriangularFuzzyNumber instance derived from the input tokens.

        :rtype: TriangularFuzzyNumber
        """

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_create_fuzzy_number -> {tokens}")
        tokens = tokens
        if len(tokens) == 1:
            if isinstance(tokens[0], (int, float)):
                return TriangularFuzzyNumber(tokens[0], tokens[0], tokens[0])
            elif isinstance(tokens[0], str):
                if tokens[0] not in DLParser.kb.fuzzy_numbers:
                    Util.error(
                        f"Error: Fuzzy number {tokens[0]} has to be defined before being used."
                    )
                return DLParser.kb.fuzzy_numbers.get(tokens[0])
        elif all(isinstance(t, (int, float)) for t in tokens):
            return TriangularFuzzyNumber(tokens[0], tokens[1], tokens[2])

    @staticmethod
    def _set_fuzzy_number(tokens: list) -> TriangularFuzzyNumber:
        """
        Processes a parsed fuzzy number definition to construct a TriangularFuzzyNumber instance and register it within the global knowledge base. The method supports direct assignment and arithmetic operations—specifically addition, subtraction, multiplication, and division—by resolving string identifiers in the input tokens to existing fuzzy number objects. It validates that the target name is unique, reporting an error if a fuzzy number with that name already exists. As a side effect, the method updates the knowledge base with the new definition and sets a flag indicating the presence of concrete fuzzy concepts.

        :param tokens: Parsed components of a fuzzy number definition, including the identifier, the defining expression (value or operator), and associated operands.
        :type tokens: list

        :return: The TriangularFuzzyNumber instance that was defined or calculated and added to the knowledge base.

        :rtype: TriangularFuzzyNumber
        """

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_set_fuzzy_number -> {tokens}")
        tokens = tokens
        if tokens[0] in DLParser.kb.fuzzy_numbers:
            Util.error(f"Error: Fuzzy number {tokens[0]} has already been defined.")
        for i in range(2, len(tokens)):
            if isinstance(tokens[i], str):
                tokens[i] = DLParser.kb.fuzzy_numbers.get(tokens[i])
        if isinstance(tokens[1], TriangularFuzzyNumber):
            DLParser.kb.add_fuzzy_number(tokens[0], tokens[1])
            DLParser.kb.concrete_fuzzy_concepts = True
            return tokens[1]
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
            return result
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
            return result

    @staticmethod
    def _parse_feature(tokens: list) -> None:
        """
        Processes a parsed feature definition to register a concrete feature within the global knowledge base. It inspects the provided token list to identify the feature's role and data type, dispatching to the appropriate definition method—such as defining integer or real ranges, or boolean and string types. This method mutates the knowledge base state by adding the new feature definition.

        :param tokens: The parsed components of a feature definition, including the role name, data type, and optional numeric bounds.
        :type tokens: list
        """

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_parse_feature -> {tokens}")
        tokens = tokens
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

    def _parse_restrictions(tokens: list) -> FeatureFunction:
        """
        This method processes a list of tokens generated by the parser to construct `FeatureFunction` objects representing various restriction types. It first normalizes the input by flattening nested lists and then inspects the token count and content to determine the specific structure to build. For single tokens, it wraps the value directly; for pairs starting with a number, it creates a weighted feature function. For longer sequences, it identifies specific keywords—such as multiplication, subtraction, or summation—to construct composite feature functions involving the surrounding operands.

        :param tokens: The parsed tokens representing the components of a restriction expression, including operands and operators, used to construct FeatureFunction objects.
        :type tokens: list

        :return: A FeatureFunction instance constructed from the tokens based on detected operators or structure.

        :rtype: FeatureFunction
        """

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_parse_restrictions -> {tokens}")
        tokens = tokens
        if isinstance(tokens[0], (list, tuple)):
            tokens = tokens[0]
        if len(tokens) == 1:
            if isinstance(tokens[0], str) or isinstance(tokens[0], constants.NUMBER):
                return FeatureFunction(tokens[0])
        elif len(tokens) == 2 and isinstance(tokens[0], (int, float)):
            return FeatureFunction(tokens[0], FeatureFunction(tokens[1]))
        elif len(tokens) >= 3:
            if FuzzyDLKeyword.MUL.get_value() in tokens:
                return FeatureFunction(tokens[0], FeatureFunction(tokens[2]))
            elif FuzzyDLKeyword.SUB.get_value() in tokens:
                return FeatureFunction(
                    FeatureFunction(tokens[0]), FeatureFunction(tokens[2])
                )
            elif FuzzyDLKeyword.SUM.get_value() in tokens:
                return FeatureFunction(list(map(FeatureFunction, tokens[::2])))

    @staticmethod
    def _parse_datatype_restriction(tokens: list) -> Concept:
        """
        This static method processes a datatype restriction from the provided tokens, determining the restriction type (such as exact, at most, or at least) based on the operator token and identifying the associated concrete feature role. It validates that the role has been previously defined in the knowledge base and ensures that any triangular fuzzy numbers used have a defined range before proceeding. Depending on the value token's type, the method resolves strings to either existing fuzzy number concepts or new continuous variables, and handles triangular fuzzy numbers by extracting their crisp or fuzzy representations. The constructed restriction is then added to the global knowledge base.

        :param tokens: The parsed components of the datatype restriction, containing the operator, the feature role, and the value or concept.
        :type tokens: list

        :return: The datatype restriction Concept that was added to the knowledge base.

        :rtype: Concept
        """

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_parse_datatype_restriction -> {tokens}")
        tokens = tokens
        role: str = tokens[1]
        if role not in DLParser.kb.concrete_features:
            Util.error(f"Error: Feature {role} has not been defined.")
        restriction_type: RestrictionType = RestrictionType.EXACT_VALUE
        if tokens[0] == FuzzyDLKeyword.LESS_THAN_OR_EQUAL_TO:
            restriction_type = RestrictionType.AT_MOST_VALUE
        elif tokens[0] == FuzzyDLKeyword.GREATER_THAN_OR_EQUAL_TO:
            restriction_type = RestrictionType.AT_LEAST_VALUE

        if isinstance(tokens[2], str):
            # if tokens.as_dict().get("string") == tokens[2] and not DLParser.kb.check_fuzzy_number_concept_exists(tokens[2]):
            #     return DLParser.kb.add_datatype_restriction(restriction_type, tokens[2], role)
            # else:
            feature_type: ConcreteFeatureType = DLParser.kb.concrete_features[
                role
            ].get_type()
            if feature_type == ConcreteFeatureType.STRING:
                return DLParser.kb.add_datatype_restriction(
                    restriction_type, tokens[2], role
                )
            if DLParser.kb.check_fuzzy_number_concept_exists(tokens[2]):
                return DLParser.kb.add_datatype_restriction(
                    restriction_type,
                    DLParser.kb.get_concept(tokens[2]),
                    role,
                )
            else:
                v: Variable = Variable(tokens[2], VariableType.CONTINUOUS)  # Variable
                return DLParser.kb.add_datatype_restriction(restriction_type, v, role)
        elif isinstance(tokens[2], TriangularFuzzyNumber):
            if not TriangularFuzzyNumber.has_defined_range():
                Util.error(
                    "Error: The range of the fuzzy numbers has to be defined before being used."
                )
            if tokens[2].is_number():
                return DLParser.kb.add_datatype_restriction(
                    restriction_type, tokens[2].get_a(), role
                )
            else:
                return DLParser.kb.add_datatype_restriction(
                    restriction_type, tokens[2], role
                )
        elif isinstance(tokens[2], FeatureFunction):
            return DLParser.kb.add_datatype_restriction(
                restriction_type, tokens[2], role
            )

    @staticmethod
    def _parse_term(tokens: list) -> Term:
        """
        This static method processes a parsed token sequence representing a single term within a mathematical expression and constructs a corresponding Term object. It handles two specific structures: a standalone variable name, which is interpreted as having an implicit coefficient of 1.0, and a triple consisting of a coefficient, an operator, and a variable name. In both cases, the variable string is resolved to a specific variable object via the MILP knowledge base associated with the parser.

        :param tokens: The parsed result containing the components of a mathematical term, representing either a single variable or a coefficient and variable pair.
        :type tokens: list

        :return: A Term instance representing the parsed coefficient and variable.

        :rtype: Term
        """

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_parse_term -> {tokens}")
        if len(tokens) == 1:
            return Term(1.0, DLParser.kb.milp.get_variable(tokens[0]))  # Term
        elif len(tokens) == 3:
            return Term(tokens[0], DLParser.kb.milp.get_variable(tokens[2]))  # Term

    @staticmethod
    def _parse_expression(tokens: list) -> Expression:
        """
        Converts raw parsing tokens into a structured Expression object, specifically handling the construction of additive expressions. The method first normalizes the input by unwrapping nested list structures. If the resulting list contains a single Term, it wraps that term in an Expression; if it contains a sequence of Terms separated by addition operators, it aggregates them into a single Expression.

        :param tokens: The raw parsing result containing the terms and operators that constitute the expression.
        :type tokens: list

        :return: The constructed Expression representing a single term or sum of terms.

        :rtype: Expression
        """

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_parse_expression -> {tokens}")
        expr: Expression = Expression(0)
        if isinstance(tokens[0], (tuple, list)):
            tokens = tokens[0]
        if len(tokens) == 1 and isinstance(tokens[0], Term):  # Term
            expr.add_term(tokens[0])
            return expr
        if "+" in tokens and all(
            isinstance(term, Term) for term in tokens[::2]  # Term
        ):
            for term in tokens[::2]:
                expr.add_term(term)
            return expr

    @staticmethod
    def _parse_inequation(tokens: list) -> Inequation:
        """
        Processes a set of parsing tokens representing an inequation to construct a formal constraint and update the underlying mathematical model. If the tokens contain a valid expression followed by an operator and a constant, the method normalizes the expression by subtracting the constant and determines the specific inequality type based on the operator string. It then registers this constraint within the MILP model associated with the current knowledge base.

        :param tokens: The parsed components of the inequation, consisting of an expression, a comparison operator, and a constant value.
        :type tokens: list

        :return: The parsed Inequation instance.

        :rtype: Inequation
        """

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_parse_inequation -> {tokens}")
        if isinstance(tokens[0], Expression):
            operator: str = tokens[1]
            constant: int | float = tokens[2]
            expr: Expression = tokens[0] - constant
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
            return Inequation(expr, operator_type)  # Inequation

    @staticmethod
    def _parse_constraints(tokens: list) -> None:
        """
        This static method processes parsed tokens to apply variable constraints to the Mixed-Integer Linear Programming (MILP) model associated with the parser's knowledge base. It examines the first token to identify the constraint type; if the token indicates a binary or free variable, the method retrieves the corresponding variable object by name and updates its type definition. It modifies the global model state rather than transforming the data stream.

        :param tokens: Tokens containing the constraint definition, used to extract the variable type and identifier for updating the MILP model.
        :type tokens: list
        """

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_parse_constraints -> {tokens}")
        if tokens[0] == FuzzyDLKeyword.BINARY:
            v: Variable = DLParser.kb.milp.get_variable(tokens[1])  # Variable
            v.set_type(VariableType.BINARY)  # Variable
        elif tokens[0] == FuzzyDLKeyword.FREE:
            v: Variable = DLParser.kb.milp.get_variable(tokens[1])  # Variable
            v.set_type(VariableType.CONTINUOUS)  # Variable

    @staticmethod
    def _show_concrete_fillers(tokens: list) -> None:
        """
        Processes the parsed tokens of a 'show-concrete-fillers' statement to update the MILP model's display configuration. It iterates through the provided tokens, treating each as a role identifier, and validates that the role exists in the knowledge base's set of concrete roles. If the role is valid, it is added to the list of variables to be shown in the MILP model; otherwise, an error is triggered indicating that only concrete roles are supported.

        :param tokens: The parsed tokens containing the concrete roles to be displayed in the MILP model.
        :type tokens: list
        """

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_show_concrete_fillers -> {tokens}")
        for role in tokens:
            if role in DLParser.kb.concrete_roles:
                DLParser.kb.milp.show_vars.add_concrete_filler_to_show(role)
            else:
                Util.error(
                    "Error: show-concrete-fillers can only be used with concrete roles."
                )

    @staticmethod
    def _show_concrete_fillers_for(tokens: list) -> None:
        """
        Processes a parsed command to identify specific concrete role fillers associated with a given individual for display in the MILP model. The method extracts the individual name from the first token and iterates over the remaining tokens, treating them as role names. For each role, it verifies its existence within the knowledge base's set of concrete roles; if valid, it updates the MILP model's configuration to include the corresponding filler variable in the output. If a role is not concrete, an error is raised.

        :param tokens: The tokens containing the individual name followed by the list of concrete roles to display fillers for.
        :type tokens: list
        """

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_show_concrete_fillers_for -> {tokens}")
        ind_name: str = tokens[0]
        for role in tokens[1:]:
            if role in DLParser.kb.concrete_roles:
                DLParser.kb.milp.show_vars.add_concrete_filler_to_show(role, ind_name)
            else:
                Util.error(
                    "Error: show-concrete-fillers-for can only be used with concrete roles."
                )

    @staticmethod
    def _show_concrete_instance_for(tokens: list) -> None:
        """
        This static method processes a parsed "show-concrete-instance-for" statement to update the MILP model's variable tracking configuration. It extracts the individual name, role, and a list of concept names from the input tokens, performing strict validation to ensure the role is defined as a concrete role and that the concepts are defined as concrete fuzzy concepts or fuzzy numbers within the knowledge base. If any validation fails, an error is raised. Upon success, it modifies the global knowledge base state by adding the specified concrete fillers to the list of variables to be displayed in the MILP model.

        :param tokens: Tokens containing the individual name, role, and concrete concepts specified in the statement.
        :type tokens: list
        """

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_show_concrete_instance_for -> {tokens}")
        ind_name: str = tokens[0]
        role: str = tokens[1]
        if role not in DLParser.kb.concrete_roles:
            Util.error(
                "Error: show-concrete-instance-for can only be used with concrete roles."
            )
        ar: list[FuzzyConcreteConcept] = []
        for c_name in tokens[2:]:
            concept: Concept = DLParser.kb.concrete_concepts.get(c_name)
            if concept is None:
                Util.error(
                    f"Error: Concrete fuzzy concept {c_name} has not been defined."
                )
            if concept.type not in (ConceptType.CONCRETE, ConceptType.FUZZY_NUMBER):
                Util.error(f"Error: {c_name} is not a concrete fuzzy concept.")
            ar.append(typing.cast(FuzzyConcreteConcept, concept))
        DLParser.kb.milp.show_vars.add_concrete_filler_to_show(role, ind_name, ar)

    @staticmethod
    def _show_abstract_fillers(tokens: list) -> None:
        """
        Parses the tokens associated with a 'show-abstract-fillers' statement to update the MILP model's display configuration. The method iterates over the roles specified in the input, ensuring they are abstract; if a concrete role is detected, an error is raised and that specific role is ignored. Successfully validated abstract roles are registered within the knowledge base's MILP structure to be included in the variable output.

        :param tokens: Tokens containing the list of role identifiers extracted from the show-abstract-fillers statement.
        :type tokens: list
        """

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_show_abstract_fillers -> {tokens}")
        for role in tokens:
            if role in DLParser.kb.concrete_roles:
                Util.error(
                    "Error: show-abstract-fillers can only be used with abstract roles."
                )
                continue
            DLParser.kb.milp.show_vars.add_abstract_filler_to_show(role)

    @staticmethod
    def _show_abstract_fillers_for(tokens: list) -> None:
        """
        Processes a parsed 'show-abstract-fillers-for' statement to configure the MILP model output. It validates that all specified roles are abstract; if a concrete role is found, an error is raised. Upon successful validation, it registers the variables representing the fillers of these roles for the given individual within the knowledge base's MILP display configuration.

        :param tokens: Tokens containing the abstract roles and individual name specified in the show-abstract-fillers-for statement.
        :type tokens: list
        """

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_show_abstract_fillers_for -> {tokens}")
        ind_name: str = tokens[0]
        for role in tokens[1:]:
            if role in DLParser.kb.concrete_roles:
                Util.error(
                    "Error: show-abstract-fillers-for can only be used with abstract roles."
                )
                continue
            DLParser.kb.milp.show_vars.add_abstract_filler_to_show(role, ind_name)

    @staticmethod
    def _show_concepts(tokens: list) -> None:
        """
        This static method processes the tokens resulting from a "show-concepts" statement, extracting a list of individual names. It iterates through these names and updates the MILP model's configuration by adding each individual to the set of variables designated for display. The method includes debug logging if enabled.

        :param tokens: Tokens containing the list of individual identifiers to be displayed in the MILP model.
        :type tokens: list
        """

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_show_concepts -> {tokens}")
        for ind_name in tokens:
            DLParser.kb.milp.show_vars.add_individual_to_show(ind_name)

    @staticmethod
    def _show_instances(tokens: list) -> None:
        """
        This static method processes a 'show-instances' statement by extracting the specified concepts from the tokens and registering them for display within the MILP model. It iterates through the provided tokens, converting each item into a Concept object and adding it to the model's configuration of variables to show. This operation has a side effect of modifying the internal state of the knowledge base's MILP solver to ensure the instances of these concepts are tracked.

        :param tokens: Tokens from a show-instances statement, containing the concepts to be added to the MILP display list.
        :type tokens: list
        """

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_show_instances -> {tokens}")
        for concept in tokens:
            concept: Concept = DLParser._to_concept(concept)
            DLParser.kb.milp.show_vars.add_concept_to_show(str(concept))

    @staticmethod
    def _show_variables(tokens: list) -> None:
        """
        Processes the parsed tokens of a show-variables statement to identify and register specific variables for display. It iterates through the list of variable names contained in the input tokens, retrieves the corresponding `Variable` objects from the MILP model, and adds them to the model's collection of variables to show. This method modifies the state of the MILP model's `show_vars` attribute and assumes that all provided variable names exist within the current model context.

        :param tokens: The tokens containing the list of variable names extracted from the show-variables statement.
        :type tokens: list
        """

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_show_variables -> {tokens}")
        for variable_name in tokens:
            var: Variable = DLParser.kb.milp.get_variable(variable_name)  # Variable
            DLParser.kb.milp.show_vars.add_variable(var, str(var))

    @staticmethod
    def _show_languages(tokens: list) -> None:
        """
        This static method serves as a semantic callback for a "show-languages" statement, modifying the state of the global knowledge base to indicate that language information should be displayed. It sets the `show_language` attribute of the `DLParser` knowledge base to `True`. Additionally, if debug mode is active, it logs the input tokens for troubleshooting purposes.

        :param tokens: The tokens representing the show-languages statement.
        :type tokens: list
        """

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_show_languages -> {tokens}")
        DLParser.kb.show_language = True

    @staticmethod
    def _parse_crisp_declarations(tokens: list) -> None:
        """
        This static method processes parsed tokens to identify and handle crisp declarations for either concepts or roles. Based on the leading keyword in the token list, it iterates through the remaining identifiers to update the global knowledge base. If the declaration targets concepts, it converts the identifiers to Concept objects and registers them as crisp; if it targets roles, it registers the role identifiers directly. The operation modifies the state of the knowledge base.

        :param tokens: The tokens containing the declaration type keyword followed by the identifiers of the concepts or roles to be marked as crisp.
        :type tokens: list
        """

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_parse_crisp_declarations -> {tokens}")
        if tokens[0] == FuzzyDLKeyword.CRISP_CONCEPT:
            for concept in tokens[1:]:
                concept: Concept = DLParser._to_concept(concept)
                DLParser.kb.set_crisp_concept(concept)
        elif tokens[0] == FuzzyDLKeyword.CRISP_ROLE:
            for role in tokens[1:]:
                DLParser.kb.set_crisp_role(role)

    @staticmethod
    def _parse_fuzzy_similarity(tokens: list) -> None:
        """
        This static method processes a fuzzy similarity relation identified during the parsing phase. It extracts the primary identifier from the provided tokens and adds it to the parser's knowledge base as a similarity relation. It serves as a side-effect trigger that updates the internal state of the knowledge base.

        :param tokens: The tokens containing the fuzzy similarity relation data extracted from the input string.
        :type tokens: list
        """

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_parse_fuzzy_similarity -> {tokens}")
        DLParser.kb.add_similarity_relation(tokens[0])

    @staticmethod
    def _parse_fuzzy_equivalence(tokens: list) -> None:
        """
        Processes the parsed tokens corresponding to a fuzzy equivalence relation and updates the global knowledge base accordingly. This static method extracts the primary identifier from the token list and invokes the knowledge base's `add_equivalence_relation` method to register the relation. Its primary effect is the mutation of the shared `DLParser.kb` state.

        :param tokens: The tokens containing the fuzzy equivalence relation to be added to the knowledge base.
        :type tokens: list
        """

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_parse_fuzzy_equivalence -> {tokens}")
        DLParser.kb.add_equivalence_relation(tokens[0])

    @staticmethod
    def _parse_degree(tokens: list) -> Degree:
        """
        Converts raw parsing tokens into specific semantic Degree objects based on the type of the first token found in the input. If the token is a numeric value, the method returns a `DegreeNumeric` object; if it is an `Expression` instance, it returns a `DegreeExpression` object. For string tokens, the method consults the knowledge base to check for a defined truth constant, returning a `DegreeNumeric` if a match is found, or otherwise treating the string as a variable name to retrieve and return a `DegreeVariable`. Debug information may be logged if enabled.

        :param tokens: The parsed output containing the raw degree data, expected to be a numeric value, an expression, or a variable name.
        :type tokens: list

        :return: The specific Degree instance (DegreeNumeric, DegreeExpression, or DegreeVariable) derived from the input tokens.

        :rtype: Degree
        """

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_parse_degree -> {tokens}")
        if isinstance(tokens[0], (int, float)):
            return DegreeNumeric.get_degree(float(tokens[0]))
        elif isinstance(tokens[0], Expression):
            return DegreeExpression.get_degree(tokens[0])
        elif isinstance(tokens[0], str):
            tc: typing.Optional[float] = DLParser.kb.get_truth_constants(tokens[0])
            if tc is not None:
                return DegreeNumeric.get_degree(float(tc))
            else:
                return DegreeVariable.get_degree(  # Variable
                    DLParser.kb.milp.get_variable(tokens[0])
                )

    @staticmethod
    def _parse_axioms(tokens: list) -> None:
        """
        Processes a list of parsed tokens representing Description Logic axioms and updates the global knowledge base accordingly. The method inspects the leading keyword to dispatch specific logic for various axiom types, including individual assertions, role relations, concept implications (supporting multiple fuzzy logic semantics such as Goedel, Lukasiewicz, and Zadeh), concept definitions, and disjointness constraints. Additionally, it manages role characteristics like domain, range, transitivity, symmetry, and inverse relationships, performing validation to ensure concrete roles are not used in invalid contexts. Fuzzy degrees are applied to assertions and implications where provided, defaulting to 1.0 otherwise.

        :param tokens: The parsed result containing the axiom keyword and its associated arguments (e.g., concepts, individuals, roles) to be processed and added to the knowledge base.
        :type tokens: list
        """

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_parse_axioms -> {tokens}")
        # Hot path first: large ontologies are dominated by concept
        # definitions, so checking these before the long keyword chain avoids
        # ~9 failed FuzzyDLKeyword.__eq__ comparisons per form.
        if tokens[0] == FuzzyDLKeyword.DEFINE_PRIMITIVE_CONCEPT:
            name: str = tokens[1]
            c: Concept = DLParser._to_concept(tokens[2])
            DLParser.kb.define_atomic_concept(name, c, LogicOperatorType.ZADEH, 1.0)
        elif tokens[0] == FuzzyDLKeyword.DEFINE_CONCEPT:
            name: str = tokens[1]
            c: Concept = DLParser._to_concept(tokens[2])
            DLParser.kb.define_concept(name, c)
        elif tokens[0] == FuzzyDLKeyword.INSTANCE:
            a: Individual = DLParser.kb.get_individual(tokens[1])
            c: Concept = DLParser._to_concept(tokens[2])
            d: Degree = tokens[3] if len(tokens) > 3 else DegreeNumeric.get_degree(1.0)
            DLParser.kb.add_assertion(a, c, d)
        elif tokens[0] == FuzzyDLKeyword.RELATED:
            a: Individual = DLParser.kb.get_individual(tokens[1])
            b: Individual = DLParser.kb.get_individual(tokens[2])
            role: str = tokens[3]
            d: Degree = tokens[4] if len(tokens) > 4 else DegreeNumeric.get_degree(1.0)
            if role in DLParser.kb.concrete_roles:
                Util.error(f"Error: Role {role} cannot be concrete and abstract.")
            DLParser.kb.add_relation(a, role, b, d)
        elif tokens[0] in (
            FuzzyDLKeyword.GOEDEL_IMPLIES,
            FuzzyDLKeyword.LUKASIEWICZ_IMPLIES,
            FuzzyDLKeyword.KLEENE_DIENES_IMPLIES,
            FuzzyDLKeyword.ZADEH_IMPLIES,
            FuzzyDLKeyword.IMPLIES,
        ):
            c1: Concept = DLParser._to_concept(tokens[1])
            c2: Concept = DLParser._to_concept(tokens[2])
            d: Degree = tokens[3] if len(tokens) > 3 else DegreeNumeric.get_degree(1.0)
            if tokens[0] == FuzzyDLKeyword.IMPLIES:
                DLParser.kb.implies(c1, c2, d)
            elif tokens[0] == FuzzyDLKeyword.GOEDEL_IMPLIES:
                DLParser.kb.goedel_implies(c1, c2, d)
            elif tokens[0] == FuzzyDLKeyword.LUKASIEWICZ_IMPLIES:
                DLParser.kb.lukasiewicz_implies(c1, c2, d)
            elif tokens[0] == FuzzyDLKeyword.KLEENE_DIENES_IMPLIES:
                DLParser.kb.kleene_dienes_implies(c1, c2, d)
            elif tokens[0] == FuzzyDLKeyword.ZADEH_IMPLIES:
                DLParser.kb.zadeh_implies(c1, c2)
        elif tokens[0] == FuzzyDLKeyword.ZADEH_IMPLIES:
            c1: Concept = DLParser._to_concept(tokens[1])
            c2: Concept = DLParser._to_concept(tokens[2])
            DLParser.kb.zadeh_implies(c1, c2)
        elif tokens[0] == FuzzyDLKeyword.EQUIVALENT_CONCEPTS:
            c1: Concept = DLParser._to_concept(tokens[1])
            c2: Concept = DLParser._to_concept(tokens[2])
            DLParser.kb.define_equivalent_concepts(c1, c2)
        elif tokens[0] == FuzzyDLKeyword.DISJOINT_UNION:
            concepts: list[str] = [str(DLParser._to_concept(t)) for t in tokens[1:]]
            DLParser.kb.add_disjoint_union_concept(concepts)
        elif tokens[0] == FuzzyDLKeyword.DISJOINT:
            concepts: list[Concept] = [DLParser._to_concept(t) for t in tokens[1:]]
            DLParser.kb.add_concepts_disjoint(concepts)
        elif tokens[0] in (FuzzyDLKeyword.RANGE, FuzzyDLKeyword.DOMAIN):
            role: str = tokens[1]
            concept: Concept = DLParser._to_concept(tokens[2])
            if tokens[0] == FuzzyDLKeyword.RANGE:
                DLParser.kb.check_role(role, concept)
                DLParser.kb.role_range(role, concept)
            else:
                DLParser.kb.role_domain(role, concept)
        elif tokens[0] == FuzzyDLKeyword.FUNCTIONAL:
            role: str = tokens[1]
            DLParser.kb.role_is_functional(role)
        elif tokens[0] == FuzzyDLKeyword.TRANSITIVE:
            role: str = tokens[1]
            DLParser.kb.role_is_transitive(role)
        elif tokens[0] == FuzzyDLKeyword.SYMMETRIC:
            role: str = tokens[1]
            DLParser.kb.role_is_symmetric(role)
        elif tokens[0] == FuzzyDLKeyword.REFLEXIVE:
            role: str = tokens[1]
            DLParser.kb.role_is_reflexive(role)
        elif tokens[0] == FuzzyDLKeyword.INVERSE_FUNCTIONAL:
            role: str = tokens[1]
            if role in DLParser.kb.concrete_roles:
                Util.error(f"Error: Concrete role {role} cannot have an inverse role.")
            DLParser.kb.role_is_inverse_functional(role)
        elif tokens[0] == FuzzyDLKeyword.INVERSE:
            role: str = tokens[1]
            inv_role: str = tokens[2]
            if role in DLParser.kb.concrete_roles:
                Util.error(f"Error: Concrete role {role} cannot have an inverse role.")
            elif inv_role in DLParser.kb.concrete_roles:
                Util.error(
                    f"Error: Concrete role {inv_role} cannot have an inverse role."
                )
            else:
                DLParser.kb.add_inverse_roles(role, inv_role)
        elif tokens[0] == FuzzyDLKeyword.IMPLIES_ROLE:
            role_c: str = tokens[1]
            role_p: str = tokens[2]
            d: float = tokens[3] if len(tokens) > 3 else 1.0
            DLParser.kb.role_implies(role_c, role_p, d)

    @staticmethod
    def _parse_queries(tokens: list) -> None:
        """
        Parses a list of tokens representing a query definition and constructs the appropriate query object to be added to the parser's query list. The method identifies the specific query type—such as satisfiability, subsumption, instance checking, or defuzzification—by examining the first token. It then instantiates the corresponding query class (e.g., `KbSatisfiableQuery`, `MaxSubsumesQuery`) using subsequent tokens as arguments, converting strings to concepts or individuals as needed. During this process, it performs validation checks, such as ensuring roles are not concrete for related queries and that features are defined for defuzzification operations, raising errors if these conditions are not met. Additionally, it may update the knowledge base's abstract roles set. The constructed query is appended to `DLParser.queries_list`.

        :param tokens: Parsed result containing the query keyword and its associated arguments (e.g., concepts, individuals, roles) used to construct a specific query object.
        :type tokens: list
        """

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"\t\t_parse_queries -> {tokens}")

        if tokens[0] == FuzzyDLKeyword.ALL_INSTANCES_QUERY:
            DLParser.queries_list.append(AllInstancesQuery(tokens[1]))
        elif tokens[0] == FuzzyDLKeyword.SAT_QUERY:
            DLParser.queries_list.append(KbSatisfiableQuery())
        elif tokens[0] in (
            FuzzyDLKeyword.MIN_SAT_QUERY,
            FuzzyDLKeyword.MAX_SAT_QUERY,
        ):
            _class: Query = (
                MinSatisfiableQuery
                if tokens[0] == FuzzyDLKeyword.MIN_SAT_QUERY
                else MaxSatisfiableQuery
            )
            c: Concept = DLParser._to_concept(tokens[1])
            if len(tokens) > 2:
                DLParser.queries_list.append(
                    _class(c, DLParser.kb.get_individual(tokens[2]))
                )
            else:
                DLParser.queries_list.append(_class(c))
        elif tokens[0] in (
            FuzzyDLKeyword.MAX_INSTANCE_QUERY,
            FuzzyDLKeyword.MIN_INSTANCE_QUERY,
        ):
            _class: Query = (
                MaxInstanceQuery
                if tokens[0] == FuzzyDLKeyword.MAX_INSTANCE_QUERY
                else MinInstanceQuery
            )
            a: Individual = DLParser.kb.get_individual(tokens[1])
            c: Concept = DLParser._to_concept(tokens[2])
            DLParser.queries_list.append(_class(c, a))
        elif tokens[0] in (
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
                if tokens[0].lower().startswith("max")
                else MinSubsumesQuery
            )
            c1: Concept = DLParser._to_concept(tokens[1])
            c2: Concept = DLParser._to_concept(tokens[2])
            if tokens[0] in (
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
            elif tokens[0] in (
                FuzzyDLKeyword.MAX_G_SUBS_QUERY,
                FuzzyDLKeyword.MIN_G_SUBS_QUERY,
            ):
                DLParser.queries_list.append(_class(c1, c2, LogicOperatorType.GOEDEL))
            elif tokens[0] in (
                FuzzyDLKeyword.MAX_L_SUBS_QUERY,
                FuzzyDLKeyword.MIN_L_SUBS_QUERY,
            ):
                DLParser.queries_list.append(
                    _class(c1, c2, LogicOperatorType.LUKASIEWICZ)
                )
            elif tokens[0] in (
                FuzzyDLKeyword.MAX_KD_SUBS_QUERY,
                FuzzyDLKeyword.MIN_KD_SUBS_QUERY,
            ):
                DLParser.queries_list.append(
                    _class(c1, c2, LogicOperatorType.KLEENE_DIENES)
                )
        elif tokens[0] in (
            FuzzyDLKeyword.MAX_RELATED_QUERY,
            FuzzyDLKeyword.MIN_RELATED_QUERY,
        ):
            a: Individual = DLParser.kb.get_individual(tokens[1])
            b: Individual = DLParser.kb.get_individual(tokens[2])
            role: str = tokens[3]
            if role in DLParser.kb.concrete_roles:
                Util.error(f"Error: Role {role} cannot be concrete and abstract.")
            DLParser.kb.abstract_roles.add(role)
            if tokens[0] == FuzzyDLKeyword.MAX_RELATED_QUERY:
                DLParser.queries_list.append(MaxRelatedQuery(a, b, role))
            else:
                DLParser.queries_list.append(MinRelatedQuery(a, b, role))
        elif tokens[0] == FuzzyDLKeyword.MAX_VAR_QUERY:
            DLParser.queries_list.append(MaxQuery(tokens[1]))
        elif tokens[0] == FuzzyDLKeyword.MIN_VAR_QUERY:
            DLParser.queries_list.append(MinQuery(tokens[1]))
        elif tokens[0] in (
            FuzzyDLKeyword.DEFUZZIFY_LOM_QUERY,
            FuzzyDLKeyword.DEFUZZIFY_SOM_QUERY,
            FuzzyDLKeyword.DEFUZZIFY_MOM_QUERY,
        ):
            c: Concept = DLParser._to_concept(tokens[1])
            a: Individual = DLParser.kb.get_individual(tokens[2])
            role: str = tokens[3]
            if DLParser.kb.concrete_features.get(role) is None:
                Util.error(f"Error: Feature {role} has not been defined.")
            if tokens[0] == FuzzyDLKeyword.DEFUZZIFY_LOM_QUERY:
                DLParser.queries_list.append(LomDefuzzifyQuery(c, a, role))
            elif tokens[0] == FuzzyDLKeyword.DEFUZZIFY_SOM_QUERY:
                DLParser.queries_list.append(SomDefuzzifyQuery(c, a, role))
            elif tokens[0] == FuzzyDLKeyword.DEFUZZIFY_MOM_QUERY:
                DLParser.queries_list.append(MomDefuzzifyQuery(c, a, role))
        elif tokens[0] == FuzzyDLKeyword.BNP_QUERY:
            if not TriangularFuzzyNumber.has_defined_range():
                Util.error(
                    "Error: The range of the fuzzy numbers has to be defined before being used."
                )
            DLParser.queries_list.append(
                BnpQuery(
                    tokens[1]
                    if isinstance(tokens[1], TriangularFuzzyNumber)
                    else DLParser.kb.fuzzy_numbers.get(tokens[1])
                )
            )

    @staticmethod
    def load_config(**kwargs) -> None:
        """
        This static method acts as a wrapper to load specific configuration parameters from a predefined INI file located in the current working directory. It constructs the file path for 'CONFIG.ini' and delegates the actual parsing and parameter extraction to the `ConfigReader` class, passing along the provided arguments to determine which specific settings to retrieve. The function relies on the presence of the configuration file in the file system and triggers side effects within the `ConfigReader` rather than returning a value directly. By accepting a variable length argument list, it allows for selective loading of configuration data based on the caller's needs.

        :param kwargs: Keys specifying which configuration parameters to load from the file.
        :type kwargs: typing.Any
        """

        ConfigReader.load_parameters(os.path.join(os.getcwd(), "CONFIG.ini"), **kwargs)
