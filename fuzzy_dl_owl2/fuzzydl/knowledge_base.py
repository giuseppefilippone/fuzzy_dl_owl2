from __future__ import annotations

import copy
import typing
from collections import deque

import networkx as nx
import trycast
from sortedcontainers import SortedSet

from fuzzy_dl_owl2.fuzzydl.assertion.assertion import Assertion
from fuzzy_dl_owl2.fuzzydl.concept.all_some_concept import AllSomeConcept
from fuzzy_dl_owl2.fuzzydl.concept.approximation_concept import ApproximationConcept
from fuzzy_dl_owl2.fuzzydl.concept.atomic_concept import AtomicConcept
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
from fuzzy_dl_owl2.fuzzydl.concept.interface.has_concepts_interface import (
    HasConceptsInterface,
)
from fuzzy_dl_owl2.fuzzydl.concept.interface.has_role_interface import HasRoleInterface
from fuzzy_dl_owl2.fuzzydl.concept.interface.has_value_interface import (
    HasValueInterface,
)
from fuzzy_dl_owl2.fuzzydl.concept.modified.modified_concept import ModifiedConcept
from fuzzy_dl_owl2.fuzzydl.concept.modified.triangularly_modified_concept import (
    TriangularlyModifiedConcept,
)
from fuzzy_dl_owl2.fuzzydl.concept.negated_nominal import NegatedNominal
from fuzzy_dl_owl2.fuzzydl.concept.operator_concept import OperatorConcept
from fuzzy_dl_owl2.fuzzydl.concept.owa_concept import OwaConcept
from fuzzy_dl_owl2.fuzzydl.concept.qowa_concept import QowaConcept
from fuzzy_dl_owl2.fuzzydl.concept.quasi_sugeno_integral import QsugenoIntegral
from fuzzy_dl_owl2.fuzzydl.concept.self_concept import SelfConcept
from fuzzy_dl_owl2.fuzzydl.concept.sugeno_integral import SugenoIntegral
from fuzzy_dl_owl2.fuzzydl.concept.threshold_concept import ThresholdConcept
from fuzzy_dl_owl2.fuzzydl.concept.truth_concept import TruthConcept
from fuzzy_dl_owl2.fuzzydl.concept.value_concept import ValueConcept
from fuzzy_dl_owl2.fuzzydl.concept.weighted_concept import WeightedConcept
from fuzzy_dl_owl2.fuzzydl.concept.weighted_max_concept import WeightedMaxConcept
from fuzzy_dl_owl2.fuzzydl.concept.weighted_min_concept import WeightedMinConcept
from fuzzy_dl_owl2.fuzzydl.concept.weighted_sum_concept import WeightedSumConcept
from fuzzy_dl_owl2.fuzzydl.concept.weighted_sum_zero_concept import (
    WeightedSumZeroConcept,
)
from fuzzy_dl_owl2.fuzzydl.concept_equivalence import ConceptEquivalence
from fuzzy_dl_owl2.fuzzydl.concrete_feature import ConcreteFeature
from fuzzy_dl_owl2.fuzzydl.degree.degree import Degree
from fuzzy_dl_owl2.fuzzydl.degree.degree_expression import DegreeExpression
from fuzzy_dl_owl2.fuzzydl.degree.degree_numeric import DegreeNumeric
from fuzzy_dl_owl2.fuzzydl.degree.degree_variable import DegreeVariable
from fuzzy_dl_owl2.fuzzydl.exception.inconsistent_ontology_exception import (
    InconsistentOntologyException,
)
from fuzzy_dl_owl2.fuzzydl.feature_function import FeatureFunction
from fuzzy_dl_owl2.fuzzydl.general_concept_inclusion import GeneralConceptInclusion
from fuzzy_dl_owl2.fuzzydl.individual.created_individual import CreatedIndividual
from fuzzy_dl_owl2.fuzzydl.individual.individual import Individual
from fuzzy_dl_owl2.fuzzydl.individual.representative_individual import (
    RepresentativeIndividual,
)
from fuzzy_dl_owl2.fuzzydl.milp.expression import Expression
from fuzzy_dl_owl2.fuzzydl.milp.milp_helper import MILPHelper
from fuzzy_dl_owl2.fuzzydl.milp.solution import Solution
from fuzzy_dl_owl2.fuzzydl.milp.term import Term
from fuzzy_dl_owl2.fuzzydl.milp.variable import Variable
from fuzzy_dl_owl2.fuzzydl.modifier.linear_modifier import LinearModifier
from fuzzy_dl_owl2.fuzzydl.modifier.modifier import Modifier
from fuzzy_dl_owl2.fuzzydl.modifier.triangular_modifier import TriangularModifier
from fuzzy_dl_owl2.fuzzydl.primitive_concept_definition import (
    PrimitiveConceptDefinition,
)
from fuzzy_dl_owl2.fuzzydl.relation import Relation
from fuzzy_dl_owl2.fuzzydl.restriction.has_value_restriction import HasValueRestriction
from fuzzy_dl_owl2.fuzzydl.restriction.restriction import Restriction
from fuzzy_dl_owl2.fuzzydl.util import constants
from fuzzy_dl_owl2.fuzzydl.util.config_reader import ConfigReader
from fuzzy_dl_owl2.fuzzydl.util.constants import (
    BlockingDynamicType,
    ConceptType,
    ConcreteFeatureType,
    CreatedIndividualBlockingType,
    FeatureFunctionType,
    FuzzyLogic,
    InequalityType,
    KnowledgeBaseRules,
    LogicOperatorType,
    RepresentativeIndividualType,
    RestrictionType,
    VariableType,
)
from fuzzy_dl_owl2.fuzzydl.util.util import Util
from fuzzy_dl_owl2.fuzzydl.util.utils import class_debugging


@class_debugging()
class KnowledgeBase:

    def __init__(self) -> None:
        Variable.VARIABLE_NUMBER = 0
        self.language: str = ""

        self.milp: MILPHelper = MILPHelper()

        self.blocking_type: BlockingDynamicType = BlockingDynamicType.DOUBLE_BLOCKING

        self.max_depth: int = 1
        self.num_assertions: int = 0
        self.num_defined_concepts: int = 0
        self.num_defined_individuals: int = 0
        self.num_relations: int = 0
        self.old_01_variables: int = 0
        self.old_binary_variables: int = 0

        self.ABOX_EXPANDED: bool = False
        self.KB_LOADED: bool = False
        self.KB_UNSAT: bool = False
        self.concrete_fuzzy_concepts: bool = False
        self.lazy_unfondable: bool = False
        self.show_language: bool = False
        self.acyclic_tbox: bool = False
        self.blocking_dynamic: bool = False
        self.rule_acyclic_tbox: bool = False

        self.applied_trans_role_rules: list[str] = []
        self.assertions: list[Assertion] = []
        self.exist_assertions: list[Assertion] = []
        self.positive_concrete_value_assertions: list[Assertion] = []
        self.t_G: list[GeneralConceptInclusion] = []
        self.axioms_C_equiv_D: list[ConceptEquivalence] = []
        self.temp_string_concept_list: list[Concept] = []
        self.temp_string_list: list[str] = []
        self.tmp_features: list[str] = []

        self.abstract_roles: set[str] = set()
        self.reflexive_roles: set[str] = set()
        self.symmetric_roles: set[str] = set()
        self.transitive_roles: set[str] = set()
        self.concrete_roles: set[str] = set()
        self.functional_roles: set[str] = set()
        self.inverse_functional_roles: set[str] = set()
        self.similarity_relations: set[str] = set()
        self.processed_assertions: set[int] = set()

        self.atomic_concepts: dict[str, Concept] = dict()
        self.concept_individual_list: dict[int, SortedSet[CreatedIndividual]] = dict()
        self.blocked_assertions: dict[str, list[Assertion]] = dict()
        self.blocked_exist_assertions: dict[str, list[Assertion]] = dict()
        self.directly_blocked_children: dict[str, list[str]] = dict()
        self.concrete_concepts: dict[str, FuzzyConcreteConcept] = dict()
        self.concrete_features: dict[str, ConcreteFeature] = dict()
        self.disjoint_variables: dict[str, set[str]] = dict()
        self.fuzzy_numbers: dict[str, TriangularFuzzyNumber] = dict()
        self.individuals: dict[str, Individual] = dict()
        self.inverse_roles: dict[str, set[str]] = dict()
        self.labels_with_nodes: dict[str, set[str]] = dict()
        self.modifiers: dict[str, Modifier] = dict()
        self.number_of_concepts: dict[str, int] = dict()
        self.number_of_roles: dict[str, int] = dict()
        self.t_disjoints: dict[str, set[str]] = dict()
        self.t_definitions: dict[str, Concept] = dict()
        self.t_inclusions: dict[str, set[PrimitiveConceptDefinition]] = dict()
        self.t_synonyms: dict[str, set[str]] = dict()
        self.temp_relations_list: dict[str, list[Relation]] = dict()

        self.order: dict[str, int] = dict()
        self.truth_constants: dict[str, float] = dict()
        self.r_successors: dict[str, list[str]] = dict()
        self.domain_restrictions: dict[str, set[Concept]] = dict()
        self.range_restrictions: dict[str, set[Concept]] = dict()
        self.roles_with_all_parents: dict[str, dict[str, float]] = dict()
        self.roles_with_parents: dict[str, dict[str, float]] = dict()
        self.roles_with_trans_children: dict[str, list[str]] = dict()

        self.rules_applied: dict[KnowledgeBaseRules, int] = {
            rule: 0 for rule in list(KnowledgeBaseRules)
        }

        self.x_prime_individuals: dict[str, list[str]] = dict()
        self.y_prime_individuals: dict[str, list[str]] = dict()

        self.axioms_A_equiv_C: dict[str, set[Concept]] = dict()
        self.axioms_A_is_a_B: dict[str, set[PrimitiveConceptDefinition]] = dict()
        self.axioms_A_is_a_C: dict[str, set[PrimitiveConceptDefinition]] = dict()
        self.axioms_C_is_a_A: dict[str, set[GeneralConceptInclusion]] = dict()
        self.axioms_C_is_a_D: dict[str, set[GeneralConceptInclusion]] = dict()
        self.axioms_to_do_A_is_a_B: dict[str, set[PrimitiveConceptDefinition]] = dict()
        self.axioms_to_do_A_is_a_C: dict[str, set[PrimitiveConceptDefinition]] = dict()
        self.axioms_to_do_C_is_a_A: dict[str, set[GeneralConceptInclusion]] = dict()
        self.axioms_to_do_C_is_a_D: dict[str, set[GeneralConceptInclusion]] = dict()
        self.axioms_to_do_tmp_A_is_a_C: dict[str, set[PrimitiveConceptDefinition]] = (
            dict()
        )
        self.axioms_to_do_tmp_C_is_a_A: dict[str, set[GeneralConceptInclusion]] = dict()
        self.axioms_to_do_tmp_C_is_a_D: dict[str, set[GeneralConceptInclusion]] = dict()

    def clone(self) -> typing.Self:
        kb: KnowledgeBase = self.clone_without_abox()
        kb.assertions = [ass.clone() for ass in self.assertions]
        kb.individuals = {i: indiv.clone() for i, indiv in self.individuals.items()}
        kb.labels_with_nodes = copy.deepcopy(self.labels_with_nodes)
        kb.milp = self.milp.clone()
        kb.blocked_assertions = {
            k: [a.clone() for a in ass] for k, ass in self.blocked_assertions.items()
        }
        kb.blocked_exist_assertions = {
            k: [a.clone() for a in ass]
            for k, ass in self.blocked_exist_assertions.items()
        }

        kb.tmp_features = copy.deepcopy(self.tmp_features)
        kb.truth_constants = copy.deepcopy(self.truth_constants)

        kb.directly_blocked_children = copy.deepcopy(self.directly_blocked_children)
        kb.num_defined_concepts = self.num_defined_concepts
        kb.num_defined_individuals = self.num_defined_individuals
        kb.r_successors = copy.deepcopy(self.r_successors)
        kb.x_prime_individuals = copy.deepcopy(self.x_prime_individuals)
        kb.y_prime_individuals = copy.deepcopy(self.y_prime_individuals)
        kb.max_depth = self.max_depth
        kb.num_assertions = self.num_assertions
        kb.num_relations = self.num_relations
        kb.old_01_variables = self.old_01_variables
        kb.old_binary_variables = self.old_binary_variables
        kb.rules_applied = copy.deepcopy(self.rules_applied)
        return kb

    def clone_without_abox(self) -> typing.Self:
        kb: KnowledgeBase = KnowledgeBase()
        kb.ABOX_EXPANDED = self.ABOX_EXPANDED
        kb.abstract_roles = copy.deepcopy(self.abstract_roles)
        kb.acyclic_tbox = self.acyclic_tbox
        kb.applied_trans_role_rules = copy.deepcopy(self.applied_trans_role_rules)

        kb.atomic_concepts = {k: c.clone() for k, c in self.atomic_concepts.items()}

        kb.axioms_A_equiv_C = {
            k: set([c.clone() for c in cs]) for k, cs in self.axioms_A_equiv_C.items()
        }

        kb.axioms_A_is_a_B = {
            k: set([pcd.clone() for pcd in pcds])
            for k, pcds in self.axioms_A_is_a_B.items()
        }

        kb.axioms_A_is_a_C = {
            k: set([pcd.clone() for pcd in pcds])
            for k, pcds in self.axioms_A_is_a_C.items()
        }

        kb.axioms_C_equiv_D = [ce.clone() for ce in self.axioms_C_equiv_D]

        kb.axioms_C_is_a_A = {
            k: set([gci.clone() for gci in gcis])
            for k, gcis in self.axioms_C_is_a_A.items()
        }

        kb.axioms_C_is_a_D = {
            k: set([gci.clone() for gci in gcis])
            for k, gcis in self.axioms_C_is_a_D.items()
        }

        kb.blocking_dynamic = self.blocking_dynamic
        kb.blocking_type = self.blocking_type

        kb.tmp_features = copy.deepcopy(self.tmp_features)
        kb.truth_constants = copy.deepcopy(self.truth_constants)

        kb.concept_individual_list = {
            k: SortedSet([c.clone() for c in v])
            for k, v in self.concept_individual_list.items()
        }

        kb.concrete_concepts = {k: c.clone() for k, c in self.concrete_concepts.items()}

        kb.concrete_features = {k: f.clone() for k, f in self.concrete_features.items()}

        kb.concrete_fuzzy_concepts = self.concrete_fuzzy_concepts

        kb.concrete_roles = copy.deepcopy(self.concrete_roles)
        kb.disjoint_variables = copy.deepcopy(self.disjoint_variables)

        kb.domain_restrictions = {
            k: set([c.clone() for c in v]) for k, v in self.domain_restrictions.items()
        }

        kb.exist_assertions = [a.clone() for a in self.exist_assertions]

        kb.functional_roles = copy.deepcopy(self.functional_roles)

        kb.fuzzy_numbers = {k: f.clone() for k, f in self.fuzzy_numbers.items()}

        kb.inverse_functional_roles = copy.deepcopy(self.inverse_functional_roles)
        kb.inverse_roles = copy.deepcopy(self.inverse_roles)
        kb.KB_LOADED = self.KB_LOADED
        kb.KB_UNSAT = self.KB_UNSAT
        kb.language = self.language
        kb.lazy_unfondable = self.lazy_unfondable
        kb.milp.show_vars = self.milp.show_vars.clone()

        kb.modifiers = {k: m.clone() for k, m in self.modifiers.items()}

        kb.number_of_concepts = copy.deepcopy(self.number_of_concepts)
        kb.number_of_roles = copy.deepcopy(self.number_of_roles)
        kb.order = copy.deepcopy(self.order)

        kb.positive_concrete_value_assertions = [
            a.clone() for a in self.positive_concrete_value_assertions
        ]

        kb.processed_assertions = copy.deepcopy(self.processed_assertions)

        kb.range_restrictions = {
            k: set([c.clone() for c in v]) for k, v in self.range_restrictions.items()
        }

        kb.reflexive_roles = copy.deepcopy(self.reflexive_roles)
        kb.roles_with_all_parents = copy.deepcopy(self.roles_with_all_parents)
        kb.roles_with_parents = copy.deepcopy(self.roles_with_parents)
        kb.roles_with_trans_children = copy.deepcopy(self.roles_with_trans_children)
        kb.rule_acyclic_tbox = self.rule_acyclic_tbox
        kb.show_language = self.show_language
        kb.similarity_relations = copy.deepcopy(self.similarity_relations)
        kb.symmetric_roles = copy.deepcopy(self.symmetric_roles)
        kb.t_definitions = {k: c.clone() for k, c in self.t_definitions.items()}
        kb.t_disjoints = copy.deepcopy(self.t_disjoints)
        kb.temp_relations_list = {
            k: [r.clone() for r in v] for k, v in self.temp_relations_list.items()
        }
        kb.t_G = [gci.clone() for gci in self.t_G]
        kb.t_inclusions = {
            k: set([pcd.clone() for pcd in v]) for k, v in self.t_inclusions.items()
        }
        kb.transitive_roles = copy.deepcopy(self.transitive_roles)
        kb.t_synonyms = copy.deepcopy(self.t_synonyms)
        return kb

    def save_to_file(self, file_name: str) -> None:
        try:
            with open(file_name, "w") if file_name else None as f:
                output = f.write if f else print
                output(f"(define-fuzzy-logic {constants.KNOWLEDGE_BASE_SEMANTICS})")

                # Save concrete concepts
                for c in self.concrete_concepts.values():
                    output(f"(define-fuzzy-concept {c.name} {c.compute_name()})")

                # Save modifiers
                for mod in self.modifiers.values():
                    output(f"(define-modifier {mod} {mod.compute_name()})")

                # Save concrete features
                for feature in self.concrete_features.values():
                    name: str = feature.get_name()
                    output(f"(functional {name})")
                    feature_type: ConcreteFeatureType = feature.get_type()

                    if feature_type == ConcreteFeatureType.STRING:
                        output(f"(range {name} *string*)")
                    elif feature_type == ConcreteFeatureType.INTEGER:
                        k1 = feature.get_k1()
                        k2 = feature.get_k2()
                        output(f"(range {name} *integer* {k1} {k2})")
                    elif feature_type == ConcreteFeatureType.REAL:
                        k1 = float(feature.get_k1())
                        k2 = float(feature.get_k2())
                        output(f"(range {name} *real* {k1} {k2})")
                    elif feature_type == ConcreteFeatureType.BOOLEAN:
                        output(f"(range {name} *boolean*")

                # Save assertions
                for ass in self.assertions:
                    deg: str = self.degree_if_not_one(ass.get_lower_limit())
                    if ":" not in deg:
                        output(
                            f"(instance {ass.get_individual()} {ass.get_concept()} {deg})"
                        )

                # Save role relations
                for ind in self.individuals.values():
                    for relations in ind.role_relations.values():
                        for rel in relations:
                            deg: str = self.degree_if_not_one(rel.get_degree())
                            if ":" not in deg:
                                output(
                                    f"(related {ind} {rel.get_object_individual()} {rel.get_role_name()} {deg})"
                                )

                # Save TBox
                if self.KB_LOADED:
                    self.save_absorbed_tbox_to_file(output)
                else:
                    self.save_tbox_to_file(output)

                # Save role properties
                for r in self.reflexive_roles:
                    output(f"(reflexive {r})")

                for r in self.symmetric_roles:
                    output(f"(symmetric {r})")

                for r in self.transitive_roles:
                    output(f"(transitive {r})")

                # Save inverse roles
                for r, inv in self.inverse_roles.items():
                    if inv is None:
                        continue
                    for s in inv:
                        output(f"(inverse {r} {s})")

                # Save role hierarchies
                for r, parents in self.roles_with_parents.items():
                    if parents is None:
                        continue
                    for s, degree in parents.items():
                        output(
                            f"(implies-role {r} {s} {self.degree_if_not_one(degree)})"
                        )

                # Save functional roles
                for r in self.functional_roles:
                    if r not in self.concrete_features:
                        output(f"(functional {r})")

        except Exception as e:
            Util.error(f"Error writing to the file {file_name}: {str(e)}")

    def save_absorbed_tbox_to_file(self, output: typing.Callable) -> None:
        for atomic_concept, pcds in self.t_inclusions.items():
            for pcd in pcds:
                c: Concept = pcd.get_definition()
                deg: float = pcd.get_degree()
                if deg == 1.0:
                    output(f"(define-primitive-concept {atomic_concept} {c})")
                    continue
                implies_type: str = None
                if pcd.get_type() == LogicOperatorType.LUKASIEWICZ:
                    implies_type = "l-implies"
                elif pcd.get_type() == LogicOperatorType.GOEDEL:
                    implies_type = "g-implies"
                elif pcd.get_type() == LogicOperatorType.KLEENE_DIENES:
                    implies_type = "kd-implies"
                elif pcd.get_type() == LogicOperatorType.ZADEH:
                    implies_type = "implies"
                output(f"({implies_type} {atomic_concept} {c} {deg})")

        for atomic_concept, concept in self.t_definitions.items():
            output(f"(equivalent-concepts {atomic_concept} {concept})")

        for atomic_concept, concepts in self.t_synonyms.items():
            for c in concepts:
                output(f"(equivalent-concepts {atomic_concept} {c})")

        for gci in self.t_G:
            implies_type: str = None
            if gci.get_type() == LogicOperatorType.LUKASIEWICZ:
                implies_type = "l-implies"
            elif gci.get_type() == LogicOperatorType.GOEDEL:
                implies_type = "g-implies"
            elif gci.get_type() == LogicOperatorType.KLEENE_DIENES:
                implies_type = "kd-implies"
            elif gci.get_type() == LogicOperatorType.ZADEH:
                implies_type = "implies"
            output(
                f"({implies_type} {gci.get_subsumed()} {gci.get_subsumer()} {self.degree_if_not_one(gci.get_degree())})"
            )

        self.save_tbox_common_part_to_file(output)

    def save_tbox_to_file(self, output: typing.Callable) -> None:
        for atomic_concept, concepts in self.axioms_A_equiv_C.items():
            for c in concepts:
                output(f"(define-concept {atomic_concept} {c})")

        for atomic_concept, pcds in self.axioms_A_is_a_B.items():
            for pcd in pcds:
                c: Concept = pcd.get_definition()
                deg: float = pcd.get_degree()
                if deg == 1.0:
                    output(f"(define-primitive-concept {atomic_concept} {c})")
                    continue
                implies_type: str = None
                if pcd.get_type() == LogicOperatorType.LUKASIEWICZ:
                    implies_type = "l-implies"
                elif pcd.get_type() == LogicOperatorType.GOEDEL:
                    implies_type = "g-implies"
                elif pcd.get_type() == LogicOperatorType.KLEENE_DIENES:
                    implies_type = "kd-implies"
                elif pcd.get_type() == LogicOperatorType.ZADEH:
                    implies_type = "implies"
                output(f"({implies_type} {atomic_concept} {c} {deg})")

        for atomic_concept, pcds in self.axioms_A_is_a_C.items():
            for pcd in pcds:
                c: Concept = pcd.get_definition()
                deg: float = pcd.get_degree()
                if deg == 1.0:
                    output(f"(define-primitive-concept {atomic_concept} {c})")
                    continue
                implies_type: str = None
                if pcd.get_type() == LogicOperatorType.LUKASIEWICZ:
                    implies_type = "l-implies"
                elif pcd.get_type() == LogicOperatorType.GOEDEL:
                    implies_type = "g-implies"
                elif pcd.get_type() == LogicOperatorType.KLEENE_DIENES:
                    implies_type = "kd-implies"
                elif pcd.get_type() == LogicOperatorType.ZADEH:
                    implies_type = "implies"

                output(f"({implies_type} {atomic_concept} {c} {deg})")

        for gcis in self.axioms_C_is_a_D.values():
            for gci in gcis:
                implies_type: str = None
                if gci.get_type() == LogicOperatorType.LUKASIEWICZ:
                    implies_type = "l-implies"
                elif gci.get_type() == LogicOperatorType.GOEDEL:
                    implies_type = "g-implies"
                elif gci.get_type() == LogicOperatorType.KLEENE_DIENES:
                    implies_type = "kd-implies"
                elif gci.get_type() == LogicOperatorType.ZADEH:
                    implies_type = "implies"
                output(
                    f"({implies_type} {gci.get_subsumed()} {gci.get_subsumer()} {self.degree_if_not_one(gci.get_degree())})"
                )

        for gcis in self.axioms_C_is_a_A.values():
            for gci in gcis:
                implies_type: str = None
                if gci.get_type() == LogicOperatorType.LUKASIEWICZ:
                    implies_type = "l-implies"
                elif gci.get_type() == LogicOperatorType.GOEDEL:
                    implies_type = "g-implies"
                elif gci.get_type() == LogicOperatorType.KLEENE_DIENES:
                    implies_type = "kd-implies"
                elif gci.get_type() == LogicOperatorType.ZADEH:
                    implies_type = "implies"
                output(
                    f"({implies_type} {gci.get_subsumed()} {gci.get_subsumer()} {self.degree_if_not_one(gci.get_degree())})"
                )

        for ce in self.axioms_C_equiv_D:
            output(f"(equivalent-concepts {ce.get_c1()} {ce.get_c2()})")

        self.save_tbox_common_part_to_file(output)

    def save_tbox_common_part_to_file(self, output: typing.Callable) -> None:
        for a, disj_c_set in self.t_disjoints.items():
            for disj_c in disj_c_set:
                if a < disj_c:
                    output(f"(disjoint {a} {disj_c})")

        for role, concepts in self.domain_restrictions.items():
            for c in concepts:
                output(f"(domain {role} {c})")

        for role, concepts in self.range_restrictions.items():
            for c in concepts:
                output(f"(range {role} {c})")

    def get_individuals(self) -> dict[str, Individual]:
        return self.individuals

    def add_tmp_feature(self, feature: str) -> None:
        if feature in self.tmp_features:
            Util.error(f"Feature {feature} has already defined.")
        self.tmp_features.append(feature)

    def get_tmp_feature(self, feature: str) -> str:
        if feature not in self.tmp_features:
            Util.error(f"Feature {feature} has to be defined before.")
        return self.tmp_features.pop(self.tmp_features.index(feature))

    def set_truth_constants(self, s: str, w: float) -> None:
        if s in self.truth_constants:
            Util.error(f"Error: Truth constant {s} already defined.")
        self.truth_constants[s] = w

    def get_truth_constants(self, s: str) -> typing.Optional[float]:
        return self.truth_constants.get(s)

    def add_individual(self, ind_name: str, ind: Individual) -> None:
        self.individuals[ind_name] = ind
        if self.is_loaded():
            self.solve_gci(ind)
            self.solve_reflexive_roles(ind)

    def add_created_individual(self, ind_name: str, ind: CreatedIndividual) -> None:
        self.individuals[ind_name] = ind
        if self.is_loaded() and not ind.is_concrete():
            self.solve_gci(ind)
            self.solve_reflexive_roles(ind)

    def get_individual(
        self, ind_name: str
    ) -> typing.Union[Individual, CreatedIndividual]:
        if self.check_individual_exists(ind_name):
            return self.individuals.get(ind_name)
        ind: Individual = Individual(ind_name)
        self.add_individual(ind_name, ind)
        return ind

    def check_individual_exists(self, ind_name: str) -> bool:
        if len(self.individuals) == 0 or ind_name not in self.individuals:
            return False
        return True

    def add_concept(self, concept_name: str, conc: FuzzyConcreteConcept) -> None:
        if concept_name in self.abstract_roles or concept_name in self.concrete_roles:
            Util.warning(
                f"Warning: {concept_name} is the name of both a concept and a role."
            )
        self.concrete_concepts[concept_name] = conc

    def concept_exists(self, name: str) -> bool:
        return (
            self.atomic_concepts.get(name) or self.concrete_concepts.get(name)
        ) is not None

    def get_concept(self, name: str) -> Concept:
        c: Concept = self.atomic_concepts.get(name) or self.concrete_concepts.get(name)
        if c is not None:
            return c
        if name in self.abstract_roles or name in self.concrete_roles:
            Util.warning(f"Warning: {name} is the name of both a concept and a role.")

        c: Concept = AtomicConcept(name)
        self.atomic_concepts[name] = c
        return c

    def add_fuzzy_number(self, f_name: str, f: TriangularFuzzyNumber) -> None:
        self.add_concept(f_name, f)
        self.fuzzy_numbers[f_name] = f

    def check_fuzzy_number_concept_exists(self, conc_name: str) -> bool:
        if conc_name not in self.concrete_concepts:
            return False
        c: Concept = self.concrete_concepts.get(conc_name)
        return c.type == ConceptType.FUZZY_NUMBER

    def add_modifier(self, mod_name: str, mod: Modifier) -> None:
        if mod_name in self.modifiers:
            Util.error(f"Error: {mod_name} modifier is already defined")
        else:
            self.modifiers[mod_name] = mod

    def add_assertions(self, list_of_assertions: list[Assertion]) -> None:
        self.assertions.extend(list_of_assertions)

    @typing.overload
    def add_assertion(self, new_ass: Assertion) -> None: ...

    @typing.overload
    def add_assertion(self, a: Individual, c: Concept, n: Degree) -> None: ...

    @typing.overload
    def add_assertion(self, a: Individual, restrict: Restriction) -> None: ...

    def add_assertion(self, *args) -> None:
        assert len(args) in [1, 2, 3]
        if len(args) == 1:
            assert isinstance(args[0], Assertion)
            self.__add_assertion_1(*args)
        elif len(args) == 2:
            assert isinstance(args[0], Individual)
            assert isinstance(args[1], Restriction)
            self.__add_assertion_3(*args)
        elif len(args) == 3:
            assert isinstance(args[0], Individual)
            assert isinstance(args[1], Concept)
            assert isinstance(args[2], Degree)
            self.__add_assertion_2(*args)
        else:
            raise ValueError

    def __add_assertion_1(self, new_ass: Assertion) -> None:
        deg: Degree = new_ass.get_lower_limit()
        if deg.is_numeric() and deg.is_number_zero():
            return
        if self.is_assertion_processed(new_ass):
            Util.debug(f"Assertion (without the degree): {new_ass} already processed")
            self.milp.add_new_constraint(new_ass)
        else:
            Util.debug(f"Adding assertion: {new_ass}")
            self.num_assertions += 1
            self.assertions.append(new_ass)
            c: Concept = new_ass.get_concept()
            ind: Individual = new_ass.get_individual()
            if c.type != ConceptType.TOP and ind.is_blockable():
                aux: int = self.get_number_from_concept(str(c))
                ind: CreatedIndividual = typing.cast(CreatedIndividual, ind)
                ind.concept_list.add(aux)
                ind.directly_blocked = CreatedIndividualBlockingType.UNCHECKED
                Util.debug(f"Mark node.directly_blocked = {ind.name} as unchecked")
                self.add_individual_to_concept(aux, ind)

    def __add_assertion_2(self, a: Individual, c: Concept, n: Degree) -> None:
        self.add_assertion(Assertion(a, c, n))

    def __add_assertion_3(self, a: Individual, restrict: Restriction) -> None:

        if isinstance(restrict, HasValueRestriction):
            for_all: Concept = -HasValueConcept(
                restrict.get_role_name(), restrict.get_individual()
            )
            self.add_assertion(a, for_all, restrict.get_degree())
        else:
            self.add_assertion(
                a,
                AllSomeConcept.all(restrict.get_role_name(), restrict.get_concept()),
                restrict.get_degree(),
            )

    def add_individual_to_concept(self, concept_id: int, ind: Individual) -> None:
        if not isinstance(ind, CreatedIndividual):
            return

        self.concept_individual_list[concept_id] = self.concept_individual_list.get(
            concept_id, SortedSet()
        ) | SortedSet([ind])

        Util.debug(
            f"List of individual for concept ID: {concept_id} descr : {self.get_concept_from_number(concept_id)} : {self.concept_individual_list[concept_id]}"
        )

    def add_relation(
        self, ind_A: Individual, role: str, ind_B: Individual, degree: Degree
    ) -> Relation:
        self.abstract_roles.add(role)
        rel: Relation = IndividualHandler.add_relation(ind_A, role, ind_B, degree, self)
        if self.is_loaded() and role in self.functional_roles:
            self.merge_fillers(ind_A, role)
        return rel

    def define_synonym(self, concept_name_1: str, concept_name_2: str) -> None:
        self.t_synonyms[concept_name_1] = self.t_synonyms.get(
            concept_name_1, set()
        ) | set([concept_name_2])
        self.get_concept(concept_name_1)

    def define_synonyms(self, concept_name_1: str, concept_name_2: str) -> None:
        self.define_synonym(concept_name_1, concept_name_2)
        self.define_synonym(concept_name_2, concept_name_1)

    def define_concept(self, concept_name: str, conc: Concept) -> None:
        self.get_concept(concept_name)
        if ConfigReader.OPTIMIZATIONS != 0:
            if concept_name == str(conc):
                return
            if conc.type == ConceptType.ATOMIC:
                self.define_synonyms(concept_name, str(conc))
                return
        self.add_axiom_to_A_equiv_C(concept_name, conc)

    def get_A_t_C(self) -> dict[str, int]:
        size: int = 0
        A_t_C: dict[str, int] = dict()
        for e in self.atomic_concepts:
            A_t_C[e] = size
            size += 1
        return A_t_C

    def add_tdef_links(
        self, g: nx.DiGraph, A_t_C: dict[str, int], use_tdr: bool
    ) -> bool:
        for a in self.t_definitions:
            v1: int = A_t_C.get(a)
            c: Concept = self.t_definitions[a]
            for b in c.get_atomic_concepts():
                b_name: str = str(b)
                name_set: set[str] = self.t_synonyms.get(a)
                if name_set is not None and b_name in name_set:
                    return True
                v2: int = A_t_C.get(b_name)
                g.add_edge(v1, v2)
            if use_tdr and self.add_tdr_links(g, A_t_C, c.get_roles(), v1):
                return True
        return False

    def add_tinc_links(
        self, g: nx.DiGraph, A_t_C: dict[str, int], use_tdr: bool
    ) -> bool:
        for a in self.t_inclusions:
            v1: int = A_t_C.get(a)
            for pcd in self.t_inclusions[a]:
                c: Concept = pcd.get_definition()
                for b in c.get_atomic_concepts():
                    b_name: str = str(b)
                    name_set: set[str] = self.t_synonyms.get(a)
                    if name_set is not None and b_name in name_set:
                        return True
                    v2: int = A_t_C.get(b_name)
                    g.add_edge(v1, v2)
                if use_tdr and self.add_tdr_links(g, A_t_C, c.get_roles(), v1):
                    return True
        return False

    def add_tdr_links(
        self, g: nx.DiGraph, A_t_C: dict[str, int], used_roles: set[str], v: int
    ) -> bool:
        roles_to_be_checked: set[str] = copy.deepcopy(used_roles)
        for used_role in used_roles:
            roles_to_be_checked.add(used_role)
            parents: dict[str, float] = self.roles_with_all_parents.get(used_role)
            if parents is not None:
                roles_to_be_checked.update(set(list(parents.keys())))

        for s in roles_to_be_checked:
            restrictions: set[Concept] = set()
            aux: set[Concept] = self.domain_restrictions.get(s)
            if aux is not None:
                restrictions.update(aux)
            aux = self.range_restrictions.get(s)
            if aux is not None:
                restrictions.update(aux)

            for d in restrictions:
                for used_concept in d.get_atomic_concepts():
                    name_set: set[str] = self.t_synonyms.get(str(d))
                    if name_set is not None and str(used_concept) in name_set:
                        return True
                    w: int = A_t_C.get(str(used_concept))
                    g.add_edge(v, w)
        return False

    def is_tbox_acyclic(self) -> bool:
        g: nx.DiGraph = nx.DiGraph()
        A_t_C: dict[str, int] = self.get_A_t_C()
        if self.add_tinc_links(g, A_t_C, True):
            return False
        if self.add_tdef_links(g, A_t_C, True):
            return False
        try:
            _ = nx.find_cycle(g, orientation="original")
            return False
        except nx.NetworkXNoCycle:
            return True

    def define_atomic_concept(
        self,
        concept_name: str,
        conc: Concept,
        implication: LogicOperatorType,
        n: float,
    ) -> None:
        self.get_concept(concept_name)
        if n == 1.0 and implication != LogicOperatorType.KLEENE_DIENES:
            implication = LogicOperatorType.LUKASIEWICZ
        if self.is_redundant_A_is_a_C(concept_name, conc, implication, n):
            return
        conc_def = PrimitiveConceptDefinition(concept_name, conc, implication, n)
        if conc.is_atomic():
            self.axioms_A_is_a_B[concept_name] = self.axioms_A_is_a_B.get(
                concept_name, set()
            ) | set([conc_def])
        else:
            self.axioms_A_is_a_C[concept_name] = self.axioms_A_is_a_C.get(
                concept_name, set()
            ) | set([conc_def])

    def gci_transform_define_atomic_concept(
        self,
        concept_name: str,
        conc: Concept,
        implication: LogicOperatorType,
        n: float,
    ):
        self.get_concept(concept_name)
        if self.is_redundant_A_is_a_C(concept_name, conc, implication, n):
            return

        conc_def: PrimitiveConceptDefinition = PrimitiveConceptDefinition(
            concept_name, conc, implication, n
        )
        if conc.is_atomic():
            self.axioms_A_is_a_B[concept_name] = self.axioms_A_is_a_B.get(
                concept_name, set()
            ) | set([conc_def])
        else:
            self.axioms_to_do_tmp_A_is_a_C[concept_name] = (
                self.axioms_to_do_tmp_A_is_a_C.get(concept_name, set())
                | set([conc_def])
            )

    def is_redundant_A_is_a_C(
        self,
        concept_name: str,
        conc: Concept,
        implication: LogicOperatorType,
        n: float,
    ) -> bool:
        if conc.type == ConceptType.TOP:
            return True
        if concept_name == str(conc) and implication != LogicOperatorType.KLEENE_DIENES:
            return True
        if conc.type in (
            ConceptType.OR,
            ConceptType.GOEDEL_OR,
            ConceptType.LUKASIEWICZ_OR,
        ):
            conc: OperatorConcept = typing.cast(OperatorConcept, conc)
            for ci in conc.concepts:
                if concept_name == str(ci):
                    return True
        return False

    def set_unsatisfiable_KB(self) -> None:
        self.KB_UNSAT = True
        self.milp.add_contradiction()

    def is_redundant_gci(
        self, C: Concept, D: Concept, implication: LogicOperatorType, n: float
    ) -> bool:
        if D.type == ConceptType.TOP:
            return True
        if C.type == ConceptType.BOTTOM:
            return True
        if C.type == ConceptType.TOP and D.type == ConceptType.BOTTOM:
            self.set_unsatisfiable_KB()
            raise InconsistentOntologyException("Unsatisfiable fuzzy KB")
        if str(C) == str(D) and implication != LogicOperatorType.KLEENE_DIENES:
            return True
        if implication != LogicOperatorType.KLEENE_DIENES:
            if D.type in (
                ConceptType.OR,
                ConceptType.GOEDEL_OR,
                ConceptType.LUKASIEWICZ_OR,
            ):
                D: OperatorConcept = typing.cast(OperatorConcept, D)
                for ci in D.concepts:
                    if str(ci) == str(C):
                        return True
            if C.type in (
                ConceptType.AND,
                ConceptType.GOEDEL_AND,
                ConceptType.LUKASIEWICZ_AND,
            ):
                C: OperatorConcept = typing.cast(OperatorConcept, C)
                for ci in C.concepts:
                    if str(ci) == str(D):
                        return True
        return False

    def synonym_absorption_A_is_a_B(self, pcd1: PrimitiveConceptDefinition) -> bool:
        a: str = pcd1.get_defined_concept()
        conc: Concept = pcd1.get_definition()
        implication: LogicOperatorType = pcd1.get_type()
        n: float = pcd1.get_degree()
        if (
            conc.is_atomic()
            and str(conc) != a
            and (
                constants.KNOWLEDGE_BASE_SEMANTICS == FuzzyLogic.CLASSICAL
                or n == 1.0
                and implication != LogicOperatorType.KLEENE_DIENES
            )
        ):
            b: str = str(conc)
            hs2: set[PrimitiveConceptDefinition] = self.axioms_A_is_a_B.get(b, set())
            hs3: set[PrimitiveConceptDefinition] = self.t_inclusions.get(b, set())
            for pcd2 in hs2:
                if (
                    str(pcd2.get_definition()) != a
                    or constants.KNOWLEDGE_BASE_SEMANTICS != FuzzyLogic.CLASSICAL
                    and (
                        pcd2.get_degree() != 1.0
                        or pcd2.get_type() == LogicOperatorType.KLEENE_DIENES
                    )
                ):
                    continue
                self.define_synonyms(a, b)
                self.remove_A_is_a_B(a, pcd1)
                self.remove_A_is_a_B(b, pcd2)
                Util.debug(
                    f"{constants.SEPARATOR}Synonym absorption from axioms_A_is_a_B: {a} = {b}"
                )
                return True
            for pcd3 in hs3:
                if (
                    str(pcd3.get_definition()) != a
                    or constants.KNOWLEDGE_BASE_SEMANTICS != FuzzyLogic.CLASSICAL
                    and (
                        pcd3.get_degree() != 1.0
                        or pcd3.get_type() == LogicOperatorType.KLEENE_DIENES
                    )
                ):
                    continue
                self.define_synonyms(a, b)
                self.remove_A_is_a_B(a, pcd1)
                hs3.remove(pcd3)
                if len(hs3) == 0:
                    del self.t_inclusions[b]
                Util.debug(
                    f"{constants.SEPARATOR}Synonym absorption from t_inc: {a} = {b}"
                )
                return True
        return False

    def synonym_absorption_to_do_A_is_a_B(
        self, pcd1: PrimitiveConceptDefinition
    ) -> bool:
        a: str = pcd1.get_defined_concept()
        conc: Concept = pcd1.get_definition()
        implication: LogicOperatorType = pcd1.get_type()
        n: float = pcd1.get_degree()
        if (
            conc.is_atomic()
            and str(conc) != a
            and (
                constants.KNOWLEDGE_BASE_SEMANTICS == FuzzyLogic.CLASSICAL
                or n == 1.0
                and implication != LogicOperatorType.KLEENE_DIENES
            )
        ):
            b: str = str(conc)
            hs2: set[PrimitiveConceptDefinition] = self.axioms_A_is_a_B.get(b, set())
            hs3: set[PrimitiveConceptDefinition] = self.t_inclusions.get(b, set())
            hs4: set[PrimitiveConceptDefinition] = self.axioms_to_do_A_is_a_B.get(
                b, set()
            )
            for pcd2 in hs2:
                if (
                    str(pcd2.get_definition()) != a
                    or constants.KNOWLEDGE_BASE_SEMANTICS != FuzzyLogic.CLASSICAL
                    and (
                        pcd2.get_degree() != 1.0
                        or pcd2.get_type() == LogicOperatorType.KLEENE_DIENES
                    )
                ):
                    continue
                self.define_synonyms(a, b)
                self.remove_A_is_a_X(a, pcd1, self.t_inclusions)
                self.remove_A_is_a_B(b, pcd2)
                Util.debug(f"Synonym absorption from axioms_A_is_a_B: {a} = {b}")
                return True
            for pcd3 in hs3:
                if (
                    str(pcd3.get_definition()) != a
                    or constants.KNOWLEDGE_BASE_SEMANTICS != FuzzyLogic.CLASSICAL
                    and (
                        pcd3.get_degree() != 1.0
                        or pcd3.get_type() == LogicOperatorType.KLEENE_DIENES
                    )
                ):
                    continue
                self.define_synonyms(a, b)
                self.remove_A_is_a_X(a, pcd1, self.t_inclusions)
                self.remove_A_is_a_X(b, pcd3, self.t_inclusions)
                Util.debug(f"Synonym absorption from t_inc: {a} = {b}")
                return True
            for pcd4 in hs4:
                if (
                    str(pcd4.get_definition()) != a
                    or constants.KNOWLEDGE_BASE_SEMANTICS != FuzzyLogic.CLASSICAL
                    and (
                        pcd4.get_degree() != 1.0
                        or pcd4.get_type() == LogicOperatorType.KLEENE_DIENES
                    )
                ):
                    continue
                self.define_synonyms(a, b)
                self.remove_A_is_a_X(a, pcd1, self.axioms_to_do_A_is_a_B)
                self.remove_A_is_a_X(b, pcd4, self.axioms_to_do_A_is_a_B)
                Util.debug(f"Synonym absorption from axioms_to_do_A_is_a_B: {a} = {b}")
                return True
        return False

    def add_atomic_concepts_disjoint(self, disjoint_concepts: list[str]) -> None:
        Util.debug(f"Disjoint axioms: {disjoint_concepts}")
        for i, c1 in enumerate(disjoint_concepts):
            self.get_concept(c1)
            for c2 in disjoint_concepts[i + 1 :]:
                self.add_mutually_disjoint(c1, c2)

    @typing.overload
    def add_concepts_disjoint(self, disjoint_concepts: list[str]) -> None: ...

    @typing.overload
    def add_concepts_disjoint(self, c1: str, c2: str) -> None: ...

    @typing.overload
    def add_concepts_disjoint(self, c: Concept, d: Concept) -> None: ...

    def add_concepts_disjoint(self, *args) -> None:
        assert len(args) in [1, 2]
        if len(args) == 1:
            assert isinstance(args[0], typing.Sequence) and all(
                isinstance(a, Concept) for a in args[0]
            )
            self.__add_concepts_disjoint_1(*args)
        elif len(args) == 2:
            if isinstance(args[0], str) and isinstance(args[1], str):
                self.__add_concepts_disjoint_2(*args)
            elif isinstance(args[0], Concept) and isinstance(args[1], Concept):
                self.__add_concepts_disjoint_3(*args)
            else:
                raise ValueError
        else:
            raise ValueError

    def __add_concepts_disjoint_1(self, disjoint_concepts: list[Concept]) -> None:
        Util.debug(f"Disjoint axioms: {disjoint_concepts}")
        for i, c1 in enumerate(disjoint_concepts):
            for c2 in disjoint_concepts[i + 1 :]:
                self.add_concepts_disjoint(c1, c2)

    def __add_concepts_disjoint_2(self, c1: str, c2: str) -> None:
        if c1 == c2:
            return
        self.t_disjoints[c1] = self.t_disjoints.get(c1, set()) | set([c2])

    def __add_concepts_disjoint_3(self, c: Concept, d: Concept) -> None:
        if str(c) == str(d):
            return
        if c.is_atomic() and d.is_atomic():
            self.add_mutually_disjoint(str(c), str(d))
        else:
            a: Concept = self.get_new_atomic_concept()
            b: Concept = self.get_new_atomic_concept()
            self.zadeh_implies(c, a)
            self.zadeh_implies(d, b)
            self.add_mutually_disjoint(str(a), str(b))

    def add_mutually_disjoint(self, c1: str, c2: str) -> None:
        self.add_concepts_disjoint(c1, c2)
        self.add_concepts_disjoint(c2, c1)

    def get_new_atomic_concept(self) -> Concept:
        self.num_defined_concepts += 1
        concept_name: str = f"{Concept.DEFAULT_NAME}{self.num_defined_concepts}"
        return AtomicConcept(concept_name)

    def add_equivalent_roles(self, equiv_roles: list[str]) -> None:
        if len(equiv_roles) < 2:
            return
        r1: str = equiv_roles[0]
        for r2 in equiv_roles[1:]:
            self.role_implies(r1, r2)
            self.role_implies(r2, r1)
            r1 = r2

    def add_equivalent_concepts(self, equiv_concepts: list[Concept]) -> None:
        if len(equiv_concepts) < 2:
            return
        c1: Concept = equiv_concepts[0]
        for c2 in equiv_concepts[1:]:
            if c1.type == ConceptType.ATOMIC:
                self.define_concept(str(c1), c2)
            elif c2.type == ConceptType.ATOMIC:
                self.define_concept(str(c2), c1)
            else:
                self.define_equivalent_concepts(c1, c2)

    def define_equivalent_concepts(self, c1: Concept, c2: Concept) -> None:
        self.lukasiewicz_implies(c1, c2, DegreeNumeric.get_one())
        self.lukasiewicz_implies(c2, c1, DegreeNumeric.get_one())

    def add_disjoint_union_concept(self, disjoint_union_concepts: list[str]) -> None:
        if len(disjoint_union_concepts) < 2:
            return
        name1: str = disjoint_union_concepts[0]
        if len(disjoint_union_concepts) == 2:
            name2: str = disjoint_union_concepts[1]
            c2: Concept = self.get_concept(name2)
            self.define_concept(name1, c2)
        else:
            big_or: Concept = None
            for name_i in disjoint_union_concepts[1:]:
                ci: Concept = self.get_concept(name_i)
                big_or = ci if big_or is None else OperatorConcept.or_(big_or, ci)

            self.define_concept(name1, big_or)
            del disjoint_union_concepts[0]
            self.add_atomic_concepts_disjoint(disjoint_union_concepts)

    def role_is_functional(self, role: str) -> None:
        self.functional_roles.add(role)

    def role_is_inverse_functional(self, role: str) -> None:
        self.inverse_functional_roles.add(role)
        iv: set[str] = self.inverse_roles.get(role)
        if iv is not None:
            for inverse in iv:
                self.functional_roles.add(inverse)
        else:
            inverse: str = f"{role}{Concept.SPECIAL_STRING}inverse"
            self.add_inverse_roles(role, inverse)
            self.abstract_roles.add(inverse)
            self.functional_roles.add(inverse)

    def role_is_transitive(self, role: str) -> None:
        if role not in self.transitive_roles:
            self.abstract_roles.add(role)
            self.transitive_roles.add(role)

    def role_is_reflexive(self, role: str) -> None:
        if role not in self.reflexive_roles:
            self.abstract_roles.add(role)
            self.reflexive_roles.add(role)

    def role_is_symmetric(self, role: str) -> None:
        self.abstract_roles.add(role)
        self.symmetric_roles.add(role)
        inv_name: str = f"{role}{Concept.SPECIAL_STRING}inverse"
        self.add_inverse_roles(role, inv_name)
        self.role_implies(role, inv_name)
        self.role_implies(inv_name, role)

    def add_similarity_relation(self, role: str) -> None:
        if role not in self.similarity_relations:
            self.role_is_reflexive(role)
            self.role_is_symmetric(role)
            self.similarity_relations.add(role)

    def add_equivalence_relation(self, role: str) -> None:
        self.add_similarity_relation(role)
        self.role_is_transitive(role)

    def get_inverses_of_inverse_role(self, role: str) -> typing.Optional[set[str]]:
        inv: set[str] = self.inverse_roles.get(role)
        if inv is None or len(inv) == 0:
            return None
        for r in inv:
            inv2: set[str] = self.inverse_roles.get(r)
            if inv2 is None or len(inv2) == 0:
                return None
            return inv2
        return None

    def add_inverse_roles(self, role: str, inv_role: str) -> None:
        self.abstract_roles.add(role)
        self.abstract_roles.add(inv_role)
        a: set[str] = self.get_inverses_of_inverse_role(role) or set()
        for r in a:
            if role != r:
                self.add_simple_inverse_roles(inv_role, r)
        b: set[str] = self.get_inverses_of_inverse_role(inv_role) or set()
        for r in b:
            if inv_role != r:
                self.add_simple_inverse_roles(inv_role, r)
        a: set[str] = self.inverse_roles.get(role)
        b: set[str] = self.inverse_roles.get(inv_role)
        if a is not None and b is not None:
            for r1 in a:
                for r2 in b:
                    if r1 != inv_role and role != r2:
                        self.add_simple_inverse_roles(r1, r2)
        self.add_simple_inverse_roles(role, inv_role)

    def add_simple_inverse_roles(self, role: str, inv_role: str) -> None:
        self.inverse_roles[role] = self.inverse_roles.get(role, set()) | set([inv_role])
        self.inverse_roles[inv_role] = self.inverse_roles.get(inv_role, set()) | set(
            [role]
        )
        if role in self.inverse_functional_roles:
            self.functional_roles.add(inv_role)
        if inv_role in self.inverse_functional_roles:
            self.functional_roles.add(role)

    @typing.overload
    def role_implies(self, subsumed: str, subsumer: str) -> None: ...

    @typing.overload
    def role_implies(self, subsumed: str, subsumer: str, n: float) -> None: ...

    def role_implies(self, *args) -> None:
        assert len(args) in [2, 3]
        if len(args) == 2:
            assert isinstance(args[0], str)
            assert isinstance(args[1], str)
            self.__role_implies_1(*args)
        elif len(args) == 3:
            assert isinstance(args[0], str)
            assert isinstance(args[1], str)
            assert isinstance(args[2], constants.NUMBER)
            self.__role_implies_2(*args)
        else:
            raise ValueError

    def __role_implies_1(self, subsumed: str, subsumer: str) -> None:
        self.role_subsumes(subsumer, subsumed, 1.0)

    def __role_implies_2(self, subsumed: str, subsumer: str, n: float) -> None:
        self.role_subsumes(subsumer, subsumed, n)

    def role_range(self, role: str, conc: Concept) -> None:
        if conc == TruthConcept.get_top():
            return
        self.range_restrictions[role] = self.range_restrictions.get(role, set()) | set(
            [conc]
        )

    def role_domain(self, role: str, conc: Concept) -> None:
        if conc == TruthConcept.get_top():
            return
        self.domain_restrictions[role] = self.domain_restrictions.get(
            role, set()
        ) | set([conc])

    def solve_inverse_roles(self) -> None:
        self.form_inv_role_inc_axioms()
        self.form_inv_trans_roles()
        self.form_inv_role_relations()

    def form_inv_role_relations(self) -> None:
        temp_role_relations: dict[str, list[Relation]] = dict()
        for ind_a in self.individuals.values():
            for role, relations in ind_a.role_relations.items():
                if role not in self.inverse_roles:
                    continue
                for rel in relations:
                    ind_b: Individual = rel.get_object_individual()
                    ind_b_name: str = str(ind_b)
                    temp_rels: list[Relation] = temp_role_relations.get(ind_b_name, [])
                    for inv_role in self.inverse_roles[role]:
                        var1: Variable = self.milp.get_variable(ind_a, ind_b, role)
                        var2: Variable = self.milp.get_variable(ind_b, ind_a, inv_role)
                        self.milp.add_new_constraint(
                            Expression(Term(1.0, var1), Term(-1.0, var2)),
                            InequalityType.EQUAL,
                        )
                        temp_rel: Relation = Relation(
                            inv_role, ind_b, ind_a, DegreeVariable.get_degree(var2)
                        )
                        temp_rels.append(temp_rel)
                    temp_role_relations[ind_b_name] = temp_rels

        for _, rels in temp_role_relations.items():
            if rels is None:
                continue
            for r in rels:
                IndividualHandler.add_relation(
                    r.get_subject_individual(),
                    r.get_role_name(),
                    r.get_object_individual(),
                    r.get_degree(),
                    self,
                )

    def form_inv_role_inc_axioms(self) -> None:
        to_do: dict[str, dict[str, float]] = copy.deepcopy(self.roles_with_parents)
        no_more_role_inclusions: bool = len(to_do) == 0
        while not no_more_role_inclusions:
            no_more_role_inclusions = True
            roles_with_parents_tmp: dict[str, dict[str, float]] = {}
            for role_r in to_do:
                if role_r not in self.inverse_roles:
                    continue
                parents: dict[str, float] = self.roles_with_parents.get(role_r, {})
                for role_p, n in parents.items():
                    if role_p not in self.inverse_roles:
                        continue
                    n = n or 1.0
                    for inv_role_r in self.inverse_roles[role_r]:
                        for inv_role_p in self.inverse_roles[role_p]:
                            no_more_role_inclusions = (
                                no_more_role_inclusions
                                and not self.role_subsumes_bool(
                                    inv_role_p, inv_role_r, n, roles_with_parents_tmp
                                )
                            )
            to_do.clear()
            to_do: dict = copy.deepcopy(roles_with_parents_tmp)
            if no_more_role_inclusions:
                continue
            no_more_role_inclusions = True
            for r, parents_tmp in roles_with_parents_tmp.items():
                for p, n in parents_tmp.items():
                    n = n or 1.0
                    add_role: bool = self.role_subsumes_bool(p, r, n)
                    no_more_role_inclusions = no_more_role_inclusions and not add_role

    def form_inv_trans_roles(self) -> None:
        to_do: set[str] = copy.deepcopy(self.transitive_roles)
        no_more_roles: bool = len(to_do) == 0
        while not no_more_roles:
            no_more_roles = True
            trans_roles_tmp: set[str] = set()
            for trans_role in to_do:
                if self.inverse_roles.get(trans_role) is None:
                    continue
                for inv_role in self.inverse_roles[trans_role]:
                    if (
                        trans_role not in self.inverse_roles
                        or inv_role in self.transitive_roles
                    ):
                        continue
                    trans_roles_tmp.add(inv_role)
                    no_more_roles = False
            to_do.clear()
            to_do.update(trans_roles_tmp)
            self.transitive_roles.update(trans_roles_tmp)

    @typing.overload
    def solve_role_inclusion_axioms(self) -> None: ...

    @typing.overload
    def solve_role_inclusion_axioms(self, ind: Individual, r: Relation) -> None: ...

    def solve_role_inclusion_axioms(self, *args) -> None:
        assert len(args) in [0, 2]
        if len(args) == 0:
            self.__solve_role_inclusion_axioms_1()
        else:
            assert isinstance(args[0], Individual)
            assert isinstance(args[1], Relation)
            self.__solve_role_inclusion_axioms_2(*args)

    def __solve_role_inclusion_axioms_1(self) -> None:
        self.create_roles_with_all_parents()
        self.create_roles_with_trans_children()
        for ind in self.individuals.values():
            for role in ind.role_relations:
                if role not in self.roles_with_all_parents:
                    continue
                self.temp_relations_list[role] = ind.role_relations.get(role)
            for role_c in self.temp_relations_list:
                parents: dict[str, float] = self.roles_with_all_parents.get(
                    role_c, dict()
                )
                for role_p, n in parents.items():
                    self.add_relation_with_role_parent(ind, role_c, role_p, n)

    def __solve_role_inclusion_axioms_2(self, ind: Individual, r: Relation) -> None:
        role_c: str = r.get_role_name()
        parents: dict[str, float] = self.roles_with_all_parents.get(role_c)
        if parents is not None:
            for role_p, n in parents.items():
                Util.debug(
                    f"Adding new relations, since {role_p} is an ancestor of {r.get_role_name()} with degree {n}"
                )
                if constants.KNOWLEDGE_BASE_SEMANTICS == FuzzyLogic.LUKASIEWICZ:
                    deg: Degree = r.get_degree()
                    if deg.is_numeric():
                        aux: float = typing.cast(
                            DegreeNumeric, deg
                        ).get_numerical_value()
                        luk_tnorm: float = max(0.0, n - 1.0 + aux)
                        IndividualHandler.add_relation(
                            ind,
                            role_p,
                            r.get_object_individual(),
                            DegreeNumeric.get_degree(luk_tnorm),
                            self,
                        )
                        if role_p not in self.functional_roles:
                            continue
                        self.merge_fillers(ind, role_p)
                        continue
                    self.old_01_variables += 2
                    self.old_binary_variables += 1
                    x: Variable = self.milp.get_new_variable(
                        VariableType.SEMI_CONTINUOUS
                    )
                    new_l: Variable = self.milp.get_new_variable(
                        VariableType.SEMI_CONTINUOUS
                    )
                    yn: Variable = self.milp.get_new_variable(VariableType.BINARY)

                    self.milp.add_new_constraint(
                        Expression(Term(1.0, x)), InequalityType.EQUAL, deg
                    )
                    self.milp.add_new_constraint(
                        Expression(1.0, Term(-1.0, yn)),
                        InequalityType.GREATER_THAN,
                        DegreeVariable.get_degree(new_l),
                    )
                    self.milp.add_new_constraint(
                        Expression(-1.0 + n, Term(1.0, x), Term(1.0, yn)),
                        InequalityType.EQUAL,
                        DegreeVariable.get_degree(new_l),
                    )
                    self.milp.add_new_constraint(
                        Expression(-1.0, Term(1.0, x), Term(1.0, yn)),
                        InequalityType.LESS_THAN,
                    )
                    self.milp.add_new_constraint(
                        Expression(-1.0 + n, Term(1.0, yn)),
                        InequalityType.LESS_THAN,
                    )
                    IndividualHandler.add_relation(
                        ind,
                        role_p,
                        r.get_object_individual(),
                        DegreeVariable.get_degree(new_l),
                        self,
                    )
                    if role_p not in self.functional_roles:
                        continue
                    self.merge_fillers(ind, role_p)
                    continue
                IndividualHandler.add_relation(
                    ind, role_p, r.get_object_individual(), r.get_degree(), self
                )
                if role_p not in self.functional_roles:
                    continue
                self.merge_fillers(ind, role_p)

    def add_relation_with_role_parent(
        self, ind: Individual, role_c: str, role_p: str, n: float
    ) -> None:
        relations: list[Relation] = ind.role_relations.get(role_c, [])
        if constants.KNOWLEDGE_BASE_SEMANTICS == FuzzyLogic.LUKASIEWICZ:
            for r in relations:
                self.add_relation_with_role_parent_in_lukasiewicz(r, role_p, n)
        else:
            for r in relations:
                self.add_relation(
                    ind, role_p, r.get_object_individual(), r.get_degree()
                )

    def add_relation_with_role_parent_in_lukasiewicz(
        self, r: Relation, role_p: str, n: float
    ) -> None:
        deg: Degree = r.get_degree()
        if deg.is_numeric():
            aux: float = typing.cast(DegreeNumeric, deg).get_numerical_value()
            luk_tnorm: float = max(0.0, n - 1.0 + aux)
            self.add_relation(
                r.get_subject_individual(),
                role_p,
                r.get_object_individual(),
                DegreeNumeric.get_degree(luk_tnorm),
            )
        else:
            self.old_01_variables += 2
            self.old_binary_variables += 1
            x: Variable = self.milp.get_new_variable(VariableType.SEMI_CONTINUOUS)
            new_l: Variable = self.milp.get_new_variable(VariableType.SEMI_CONTINUOUS)
            yn: Variable = self.milp.get_new_variable(VariableType.BINARY)

            self.milp.add_new_constraint(
                Expression(Term(1.0, x)), InequalityType.EQUAL, deg
            )
            self.milp.add_new_constraint(
                Expression(1.0, Term(-1.0, yn)),
                InequalityType.GREATER_THAN,
                DegreeVariable.get_degree(new_l),
            )
            self.milp.add_new_constraint(
                Expression(-1.0 + n, Term(1.0, x), Term(1.0, yn)),
                InequalityType.EQUAL,
                DegreeVariable.get_degree(new_l),
            )
            self.milp.add_new_constraint(
                Expression(-1.0, Term(1.0, x), Term(1.0, yn)),
                InequalityType.LESS_THAN,
            )
            self.milp.add_new_constraint(
                Expression(-1.0 + n, Term(1.0, yn)), InequalityType.LESS_THAN
            )
            self.add_relation(
                r.get_subject_individual(),
                role_p,
                r.get_object_individual(),
                DegreeVariable.get_degree(new_l),
            )

    @typing.overload
    def solve_gci(self, ind: Individual, gci: GeneralConceptInclusion) -> None: ...

    @typing.overload
    def solve_gci(self, ind: Individual) -> None: ...

    def solve_gci(self, *args) -> None:
        assert len(args) in [1, 2]
        assert isinstance(args[0], Individual)
        if len(args) == 1:
            self.__solve_gci_2(*args)
        elif len(args) == 2:
            assert isinstance(args[1], GeneralConceptInclusion)
            self.__solve_gci_1(*args)
        else:
            raise ValueError

    def __solve_gci_1(self, ind: Individual, gci: GeneralConceptInclusion) -> None:
        if (
            gci.get_subsumed().type == ConceptType.MODIFIED
            and typing.cast(ModifiedConcept, gci.get_subsumed()).curr_concept.type
            == ConceptType.CONCRETE
        ):
            return
        if (
            gci.get_subsumer().type == ConceptType.MODIFIED
            and typing.cast(ModifiedConcept, gci.get_subsumer()).curr_concept.type
            == ConceptType.CONCRETE
        ):
            return

        gci_type: LogicOperatorType = gci.get_type()
        if gci_type == LogicOperatorType.LUKASIEWICZ:
            self.solve_lukasiewicz_gci(ind, gci)
        elif gci_type == LogicOperatorType.GOEDEL:
            self.solve_goedel_gci(ind, gci)
        elif gci_type == LogicOperatorType.KLEENE_DIENES:
            self.solve_kleene_dienes_gci(ind, gci)
        elif gci_type == LogicOperatorType.ZADEH:
            self.solve_zadeh_gci(ind, gci)

    def __solve_gci_2(self, ind: Individual) -> None:
        for gci in self.t_G:
            self.solve_gci(ind, gci)

    def solve_lukasiewicz_gci(
        self, ind: Individual, gci: GeneralConceptInclusion
    ) -> None:
        c: Concept = gci.get_subsumed()
        d: Concept = gci.get_subsumer()
        l: Degree = gci.get_degree()
        Util.debug(f"{constants.SEPARATOR}Applying GCI{constants.SEPARATOR}")
        Util.debug(f"{d} l-subsumes {c} >= {l}")

        if c.type == ConceptType.TOP:
            if d.type == ConceptType.BOTTOM:
                self.milp.add_new_constraint(
                    Expression(1.0), InequalityType.EQUAL, DegreeNumeric.get_degree(0.0)
                )
            else:
                new_ass: Assertion = Assertion(ind, d, l)
                self.add_assertion(new_ass)
        else:
            not_c: Concept = -c
            if d.type == ConceptType.BOTTOM:
                new_ass: Assertion = Assertion(ind, not_c, l)
                self.add_assertion(new_ass)
            else:
                x_ind_is_not_c: Variable = self.milp.get_variable(ind, not_c)
                x_ind_is_d: Variable = self.milp.get_variable(ind, d)

                self.add_assertion(
                    ind, not_c, DegreeVariable.get_degree(x_ind_is_not_c)
                )
                self.add_assertion(ind, d, DegreeVariable.get_degree(x_ind_is_d))

                if (
                    l.is_numeric()
                    and typing.cast(DegreeNumeric, l).get_numerical_value() == 1.0
                ):
                    self.old_01_variables += 1
                    self.milp.add_new_constraint(
                        Expression(
                            1.0,
                            Term(-1.0, x_ind_is_not_c),
                            Term(-1.0, x_ind_is_d),
                        ),
                        InequalityType.LESS_THAN,
                    )
                else:
                    self.old_01_variables += 2
                    self.milp.add_new_constraint(
                        Expression(Term(1.0, x_ind_is_not_c), Term(1.0, x_ind_is_d)),
                        InequalityType.GREATER_THAN,
                        l,
                    )
        Util.debug(f"{constants.SEPARATOR}GCI completed{constants.SEPARATOR}")

    def solve_goedel_gci(self, ind: Individual, gci: GeneralConceptInclusion) -> None:
        c: Concept = gci.get_subsumed()
        d: Concept = gci.get_subsumer()
        Util.debug(f"{constants.SEPARATOR}Applying GCI{constants.SEPARATOR}")
        Util.debug(f"{d} g-subsumes {c} >= {gci.get_degree()}")
        l: Degree = gci.get_degree()

        if c.type == ConceptType.TOP:
            if d.type == ConceptType.BOTTOM:
                self.milp.add_new_constraint(
                    Expression(1.0), InequalityType.EQUAL, DegreeNumeric.get_degree(0.0)
                )
            else:
                new_ass: Assertion = Assertion(ind, d, l)
                self.add_assertion(new_ass)
        else:
            not_c: Concept = -c
            if d.type == ConceptType.BOTTOM:
                new_ass: Assertion = Assertion(ind, not_c, l)
                self.add_assertion(new_ass)
            else:
                x_ind_is_not_c: Variable = self.milp.get_variable(ind, not_c)
                x_ind_is_d: Variable = self.milp.get_variable(ind, d)
                self.add_assertion(
                    ind, not_c, DegreeVariable.get_degree(x_ind_is_not_c)
                )
                self.add_assertion(ind, d, DegreeVariable.get_degree(x_ind_is_d))

                if (
                    l.is_numeric()
                    and typing.cast(DegreeNumeric, l).get_numerical_value() == 1.0
                ):
                    self.old_01_variables += 1
                    self.milp.add_new_constraint(
                        Expression(
                            1.0,
                            Term(-1.0, x_ind_is_not_c),
                            Term(-1.0, x_ind_is_d),
                        ),
                        InequalityType.LESS_THAN,
                    )
                else:
                    c_impl_d: Concept = ImpliesConcept.goedel_implies(c, d)
                    self.add_assertion(Assertion(ind, c_impl_d, l))
        Util.debug(f"{constants.SEPARATOR}GCI completed{constants.SEPARATOR}")

    def solve_kleene_dienes_gci(
        self, ind: Individual, gci: GeneralConceptInclusion
    ) -> None:
        c: Concept = gci.get_subsumed()
        d: Concept = gci.get_subsumer()
        c_impl_d: Concept = ImpliesConcept.kleene_dienes_implies(c, d)
        Util.debug(f"{constants.SEPARATOR}Applying GCI{constants.SEPARATOR}")
        Util.debug(f"{d} kd-subsumes {c} >= {gci.get_degree()}")
        if c.type == ConceptType.TOP:
            self.add_assertion(Assertion(ind, d, gci.get_degree()))
        else:
            self.add_assertion(Assertion(ind, c_impl_d, gci.get_degree()))
        Util.debug(f"{constants.SEPARATOR}GCI completed{constants.SEPARATOR}")

    def solve_zadeh_gci(self, ind: Individual, gci: GeneralConceptInclusion) -> None:
        c: Concept = gci.get_subsumed()
        d: Concept = gci.get_subsumer()
        Util.debug(f"{constants.SEPARATOR}Applying GCI{constants.SEPARATOR}")
        Util.debug(f"{d} z-subsumes {c}")
        if c.type == ConceptType.TOP:
            self.add_assertion(Assertion(ind, d, DegreeNumeric.get_degree(1.0)))
        else:
            self.old_01_variables += 1
            not_c: Concept = -c
            x_ind_is_not_c: Variable = self.milp.get_variable(ind, not_c)
            x_ind_is_d: Variable = self.milp.get_variable(ind, d)
            self.add_assertion(ind, not_c, DegreeVariable.get_degree(x_ind_is_not_c))
            self.add_assertion(ind, d, DegreeVariable.get_degree(x_ind_is_d))
            self.milp.add_new_constraint(
                Expression(1.0, Term(-1.0, x_ind_is_not_c), Term(-1.0, x_ind_is_d)),
                InequalityType.LESS_THAN,
            )
        Util.debug(f"{constants.SEPARATOR}GCI completed{constants.SEPARATOR}")

    def solve_reflexive_role(self, role: str) -> None:
        for ind in self.individuals.values():
            self.add_relation(ind, role, ind, DegreeNumeric.get_degree(1.0))

    @typing.overload
    def solve_reflexive_roles(self, ind: Individual) -> None: ...

    @typing.overload
    def solve_reflexive_roles(self) -> None: ...

    def solve_reflexive_roles(self, *args) -> None:
        assert len(args) in [0, 1]
        if len(args) == 0:
            self.__solve_reflexive_roles_2()
        else:
            assert isinstance(args[0], Individual)
            self.__solve_reflexive_roles_1(*args)

    def __solve_reflexive_roles_1(self, ind: Individual) -> None:
        for role in self.reflexive_roles:
            self.add_relation(ind, role, ind, DegreeNumeric.get_degree(1.0))

    def __solve_reflexive_roles_2(self) -> None:
        for role in self.reflexive_roles:
            self.solve_reflexive_role(role)

    @typing.overload
    def get_correct_version_of_individual(self, ass: Assertion) -> None: ...

    @typing.overload
    def get_correct_version_of_individual(self, rel: Relation) -> None: ...

    def get_correct_version_of_individual(self, *args) -> None:
        assert len(args) == 1
        if isinstance(args[0], Assertion):
            self.__get_correct_version_of_individual_1(*args)
        elif isinstance(args[0], Relation):
            self.__get_correct_version_of_individual_2(*args)
        else:
            raise ValueError

    def __get_correct_version_of_individual_1(self, ass: Assertion) -> None:
        ind: Individual = ass.get_individual()
        ind2: Individual = self.individuals.get(str(ind))
        if id(ind) == id(ind2):
            return
        if ind2 is None:
            ind2 = self.get_individual(str(ind))
        if not ind.is_blockable():
            ass.set_individual(ind2)

    def __get_correct_version_of_individual_2(self, rel: Relation) -> None:
        ind: Individual = rel.get_object_individual()
        ind2: Individual = self.individuals.get(str(ind))
        if id(ind) == id(ind2):
            return
        if ind2 is None:
            ind2 = self.get_individual(str(ind))
        if not ind.is_blockable():
            rel.set_object_individual(ind2)

    def solve_concrete_value_assertions(self) -> None:
        for ass in self.positive_concrete_value_assertions:
            Util.debug(
                f"{constants.SEPARATOR}Processing Positive Datatype Assertion{constants.SEPARATOR}"
            )
            Util.debug(f"{ass}")
            if (
                ass.get_individual().is_blockable()
                and CreatedIndividualHandler.is_blocked(
                    typing.cast(CreatedIndividual, ass.get_individual()), self
                )
            ):
                return
            if self.num_defined_individuals == ConfigReader.MAX_INDIVIDUALS:
                Util.error(
                    f"Error: Maximal number of individuals created: {self.num_defined_individuals}"
                )
                continue
            self.get_correct_version_of_individual(ass)
            self.rules_applied[KnowledgeBaseRules.RULE_DATATYPE] += 1
            if ass.get_type() == ConceptType.AT_MOST_VALUE:
                DatatypeReasoner.apply_at_most_value_rule(ass, self)
            elif ass.get_type() == ConceptType.AT_LEAST_VALUE:
                DatatypeReasoner.apply_at_least_value_rule(ass, self)
            elif ass.get_type() == ConceptType.EXACT_VALUE:
                DatatypeReasoner.apply_exact_value_rule(ass, self)
            Util.debug(f"{constants.SEPARATOR}")

        self.positive_concrete_value_assertions.clear()
        for a in self.individuals.values():
            for f_name in a.concrete_role_restrictions:
                ar: list[Relation] = a.role_relations.get(f_name)
                if ar is None:
                    continue
                b: CreatedIndividual = typing.cast(
                    CreatedIndividual, ar[0].get_object_individual()
                )
                restrics: list[Assertion] = a.concrete_role_restrictions.get(f_name, [])
                for ass in restrics:
                    Util.debug(
                        f"{constants.SEPARATOR}Processing Negative Datatype Assertion{constants.SEPARATOR}"
                    )
                    Util.debug(f"{ass}")
                    self.get_correct_version_of_individual(ass)
                    self.rules_applied[KnowledgeBaseRules.RULE_NOT_DATATYPE] += 1
                    if OperatorConcept.is_not_at_most_value(ass.get_concept()):
                        self.rule_complemented_at_most_datatype_restriction(b, ass)
                    elif OperatorConcept.is_not_at_least_value(ass.get_concept()):
                        self.rule_complemented_at_least_datatype_restriction(b, ass)
                    elif OperatorConcept.is_not_exact_value(ass.get_concept()):
                        self.rule_complemented_exact_datatype_restriction(b, ass)
                    Util.debug(f"{constants.SEPARATOR * 2}")

    def solve_functional_roles(self) -> None:
        for role in self.functional_roles:
            for name, ind in self.individuals.items():
                if str(ind) != name:
                    continue
                self.merge_fillers(ind, role)

    def merge_fillers(self, ind: Individual, func_role: str) -> None:
        rels: list[Relation] = ind.role_relations.get(func_role)
        if rels is None:
            return
        a_name: str = str(rels[0].get_object_individual())
        a: Individual = self.individuals.get(a_name)
        for rel in rels[1:]:
            b_name: str = str(rel.get_object_individual())
            b: Individual = self.individuals.get(b_name)
            if a != b:
                self.merge(a, b)
                self.individuals[b_name] = a

    def merge(self, a: Individual, b: Individual) -> None:
        """
        Merges two individuals.
        """

        if isinstance(a, CreatedIndividual) and not isinstance(b, CreatedIndividual):
            # Swap b and a, so the created individual is merged into the root individual
            a, b = b, a

        a_name, b_name = str(a), str(b)
        Util.debug(f"Merging individual {b_name} into {a_name}")
        # To do: nominal variables needed only if language contains "B"

        # Unique Name Assumption
        if not isinstance(a, CreatedIndividual) and not isinstance(
            b, CreatedIndividual
        ):
            # xAisA + xBisB <= 1
            x_a_is_a: Variable = self.milp.get_nominal_variable(a_name)
            x_b_is_b: Variable = self.milp.get_nominal_variable(b_name, b_name)
            self.milp.add_new_constraint(
                Expression(-1.0, Term(1.0, x_a_is_a), Term(1.0, x_b_is_b)),
                InequalityType.LESS_THAN,
            )
            # Add { b } to a
            self.add_labels_with_nodes(b_name, a_name)

        # --------------------------------------------------------------
        # 1. Move edges leading to b so that they lead to a
        # --------------------------------------------------------------
        for i in self.individuals.values():
            for array in i.role_relations.values():
                for r in array:
                    if r.get_object_individual() == b:
                        r.set_object_individual(a)

        # --------------------------------------------------------------------------
        # 2. Move edges leading from b to a nominal node so that they lead from a
        # --------------------------------------------------------------------------
        to_remove: set[str] = set()
        for role, b_rels in b.role_relations.items():
            new_rels: list[Relation] = []
            a_rels: list[Relation] = a.role_relations.get(role, [])
            for r in b_rels:
                if not r.get_object_individual().is_blockable():
                    r.set_subject_individual(a)
                    a_rels.append(r)
                else:
                    new_rels.append(r)

            a.role_relations[role] = a_rels
            if len(new_rels) == 0:
                to_remove.add(role)
            else:
                b.role_relations[role] = new_rels

        for role in to_remove:
            del b.role_relations[role]

        # -------------------------------------------------------
        # 3. Concept assertions using b, now use a
        # -----------------------------------------------------
        for ass in self.assertions:
            if str(ass.get_individual()) == b_name:
                ass.set_individual(a)

        for ass in self.exist_assertions:
            if str(ass.get_individual()) == b_name:
                ass.set_individual(a)

        # -----------------------------------------
        # 4. Variables using b, now use a
        # -----------------------------------------
        param: bool = isinstance(b, CreatedIndividual)
        self.milp.change_variable_names(b_name, a_name, param)

        # -----------------------------------------
        # 5. Prune
        # -----------------------------------------
        b.prune()

    def goedel_implies(self, conc1: Concept, conc2: Concept, degree: Degree) -> None:
        self.add_subsumption(conc2, conc1, degree, LogicOperatorType.GOEDEL)

    def lukasiewicz_implies(
        self, conc1: Concept, conc2: Concept, degree: Degree
    ) -> None:
        self.add_subsumption(conc2, conc1, degree, LogicOperatorType.LUKASIEWICZ)

    def kleene_dienes_implies(
        self, conc1: Concept, conc2: Concept, degree: Degree
    ) -> None:
        self.add_subsumption(conc2, conc1, degree, LogicOperatorType.KLEENE_DIENES)

    def zadeh_implies(self, conc1: Concept, conc2: Concept) -> None:
        self.add_subsumption(
            conc2, conc1, DegreeNumeric.get_degree(1.0), LogicOperatorType.ZADEH
        )

    def add_subsumption(
        self,
        conc2: Concept,
        conc1: Concept,
        degree: Degree,
        logic_type: LogicOperatorType,
    ) -> None:
        n: float = typing.cast(DegreeNumeric, degree).get_numerical_value()
        if n == 1.0 and logic_type != LogicOperatorType.KLEENE_DIENES:
            logic_type = LogicOperatorType.LUKASIEWICZ
        if self.is_redundant_gci(conc1, conc2, logic_type, n):
            return
        if conc1.type == ConceptType.ATOMIC:
            self.define_atomic_concept(str(conc1), conc2, logic_type, n)
        else:
            self.add_gci(conc2, conc1, degree, logic_type)

    @typing.overload
    def concept_absorption(
        self, pcd: PrimitiveConceptDefinition, atomic: bool
    ) -> bool: ...

    @typing.overload
    def concept_absorption(
        self, tau: GeneralConceptInclusion, atomic: bool
    ) -> bool: ...

    def concept_absorption(self, *args) -> bool:
        assert len(args) == 2
        assert isinstance(args[1], bool)
        if isinstance(args[0], PrimitiveConceptDefinition):
            return self.__concept_absorption_1(*args)
        elif isinstance(args[0], GeneralConceptInclusion):
            return self.__concept_absorption_2(*args)
        else:
            raise ValueError

    def __concept_absorption_1(
        self, pcd: PrimitiveConceptDefinition, atomic: bool
    ) -> bool:
        a: str = pcd.get_defined_concept()
        if a not in self.t_definitions:
            self.add_axiom_to_inc(a, pcd)
            self.remove_A_is_a_X(a, pcd, atomic)
            Util.debug(f"Absorbed axioms_A_is_a_C CA0, FA0: {pcd}")
            return True
        return False

    def __concept_absorption_2(
        self, tau: GeneralConceptInclusion, atomic: bool
    ) -> bool:
        degree: Degree = tau.get_degree()
        n: float = typing.cast(DegreeNumeric, degree).get_numerical_value()
        degree_is_one: bool = n == 1.0
        conc1: Concept = tau.get_subsumed()
        conc2: Concept = tau.get_subsumer()
        key: str = str(conc1)
        implication_type: LogicOperatorType = tau.get_type()
        type_c1: ConceptType = conc1.type
        type_c2: ConceptType = conc2.type
        if conc2.is_complemented_atomic() and degree_is_one:
            conc2: OperatorConcept = typing.cast(OperatorConcept, conc2)
            if str(conc2.concepts[0]) not in self.t_definitions:
                cp: PrimitiveConceptDefinition = PrimitiveConceptDefinition(
                    str(conc2.concepts[0]),
                    -conc1,
                    implication_type,
                    1.0,
                )
                self.add_axiom_to_inc(str(conc2.concepts[0]), cp)
                self.add_axiom_to_do_A_is_a_X(str(conc2.concepts[0]), cp)
                self.remove_C_is_a_X(key, tau, atomic)
                Util.debug(
                    f"Absorbed axioms_C_is_a_D CA1, FA1: {conc2.concepts[0]} ==> {-conc1}"
                )
                return True
        if (
            type_c2 == ConceptType.OR
            or type_c2 == ConceptType.LUKASIEWICZ_OR
            and implication_type == LogicOperatorType.LUKASIEWICZ
            or type_c2 == ConceptType.GOEDEL_OR
            and implication_type == LogicOperatorType.KLEENE_DIENES
            or type_c2 == ConceptType.LUKASIEWICZ_OR
            and implication_type == LogicOperatorType.ZADEH
        ):
            conc2: OperatorConcept = typing.cast(OperatorConcept, conc2)
            vc: list[Concept] = [c.clone() for c in conc2.concepts]
            for j, ci in enumerate(conc2.concepts):
                if ci.is_complemented_atomic():
                    new_c1: Concept = -ci
                    if str(new_c1) not in self.t_definitions:
                        vc[j] = -conc1
                        if type_c2 == ConceptType.LUKASIEWICZ_OR:
                            new_c2: Concept = OperatorConcept.lukasiewicz_or(*vc)
                        elif type_c2 == ConceptType.GOEDEL_OR:
                            new_c2: Concept = OperatorConcept.goedel_or(*vc)
                        else:
                            new_c2: Concept = OperatorConcept.or_(*vc)
                        cp: PrimitiveConceptDefinition = PrimitiveConceptDefinition(
                            str(new_c1),
                            new_c2,
                            implication_type,
                            n,
                        )
                        self.add_axiom_to_inc(str(new_c1), cp)
                        self.add_axiom_to_do_A_is_a_X(str(new_c1), cp)
                        self.remove_C_is_a_X(key, tau, atomic)
                        Util.debug(
                            f"Absorbed axioms_C_is_a_D CA2, FA2.1: {new_c1} ==> {new_c2}"
                        )
                        return True
        if (
            type_c1 == ConceptType.AND
            or type_c1 == ConceptType.LUKASIEWICZ_AND
            and implication_type == LogicOperatorType.LUKASIEWICZ
            or type_c1 == ConceptType.GOEDEL_AND
            and implication_type == LogicOperatorType.GOEDEL
            or type_c1 == ConceptType.GOEDEL_AND
            and implication_type == LogicOperatorType.ZADEH
            or type_c1 == ConceptType.GOEDEL_AND
            and implication_type == LogicOperatorType.LUKASIEWICZ
            and n == 1.0
        ):
            conc1: OperatorConcept = typing.cast(OperatorConcept, conc1)
            vc: list[Concept] = [c.clone() for c in conc1.concepts]
            Util.debug(f"{constants.SEPARATOR}test CA3, FA3{constants.SEPARATOR}")
            Util.debug(f"VC -> {vc}")
            Util.debug(f"Conc1 -> {conc1}")
            Util.debug(f"Conc1 size -> {len(conc1.concepts)}")
            for j, ci in enumerate(conc1.concepts):
                if ci.is_atomic() and str(ci) not in self.t_definitions:
                    del vc[j]
                    if type_c1 == ConceptType.LUKASIEWICZ_AND:
                        new_c1: Concept = ImpliesConcept.lukasiewicz_implies(
                            OperatorConcept.lukasiewicz_and(*vc), conc2
                        )
                    elif type_c1 == ConceptType.GOEDEL_AND:
                        new_c1: Concept = ImpliesConcept.goedel_implies(
                            OperatorConcept.goedel_and(*vc), conc2
                        )
                    else:
                        new_c1: Concept = ImpliesConcept.lukasiewicz_implies(
                            OperatorConcept.and_(*vc), conc2
                        )
                    if (
                        type_c1 == ConceptType.GOEDEL_AND
                        and implication_type != LogicOperatorType.GOEDEL
                    ):
                        implication_type = LogicOperatorType.LUKASIEWICZ
                    cp: PrimitiveConceptDefinition = PrimitiveConceptDefinition(
                        str(ci),
                        new_c1,
                        implication_type,
                        n,
                    )
                    self.add_axiom_to_inc(str(ci), cp)
                    self.add_axiom_to_do_A_is_a_X(str(ci), cp)
                    self.remove_C_is_a_X(key, tau, atomic)
                    Util.debug(f"Absorbed axioms_C_is_a_D CA3, FA3: {ci} ==> {new_c1}")
                    return True
        if (
            type_c2 == ConceptType.GOEDEL_IMPLIES
            and implication_type == LogicOperatorType.GOEDEL
            and typing.cast(ImpliesConcept, conc2).concepts[0].is_atomic()
        ):
            conc2: ImpliesConcept = typing.cast(ImpliesConcept, conc2)
            if str(conc2.concepts[0]) not in self.t_definitions:
                g_imp: Concept = ImpliesConcept.goedel_implies(conc1, conc2.concepts[1])
                cp: PrimitiveConceptDefinition = PrimitiveConceptDefinition(
                    str(conc2.concepts[0]),
                    g_imp,
                    implication_type,
                    n,
                )
                self.add_axiom_to_inc(str(conc2.concepts[0]), cp)
                self.add_axiom_to_do_A_is_a_X(str(conc2.concepts[0]), cp)
                self.remove_C_is_a_X(key, tau, atomic)
                Util.debug(
                    f"Absorbed axioms_C_is_a_D FA2.2: {conc2.concepts[0]} ==> {g_imp}"
                )
                return True
        return False

    @typing.overload
    def role_absorption(self, tau: PrimitiveConceptDefinition) -> bool: ...

    @typing.overload
    def role_absorption(self, tau: GeneralConceptInclusion, atomic: bool) -> bool: ...

    def role_absorption(self, *args) -> bool:
        assert len(args) in [1, 2]
        if len(args) == 1:
            assert isinstance(args[0], PrimitiveConceptDefinition)
            return self.__role_absorption_1(*args)
        else:
            assert isinstance(args[0], GeneralConceptInclusion)
            assert isinstance(args[1], bool)
            return self.__role_absorption_2(*args)

    def __role_absorption_1(self, tau: PrimitiveConceptDefinition) -> bool:
        conc1: Concept = self.get_concept(tau.get_defined_concept())
        conc2: Concept = tau.get_definition()
        key: str = str(conc1)
        implication_type: LogicOperatorType = tau.get_type()
        type_c2: ConceptType = conc2.type
        n: float = tau.get_degree()
        degree_is_one: bool = n == 1.0
        if type_c2 == ConceptType.ALL and degree_is_one:
            role: str = conc2.role
            conc2: AllSomeConcept = typing.cast(AllSomeConcept, conc2)
            if self.is_crisp_role(role) and (
                implication_type != LogicOperatorType.KLEENE_DIENES
                or constants.KNOWLEDGE_BASE_SEMANTICS == FuzzyLogic.CLASSICAL
            ):
                c: Concept = ImpliesConcept.goedel_implies(conc1, conc2)
                self.role_domain(role, c)
                self.remove_A_is_a_C(key, tau)
                Util.debug(f"Absorbed: domain {role}, {c}")
                return True
            if (
                constants.KNOWLEDGE_BASE_SEMANTICS == FuzzyLogic.CLASSICAL
                or constants.KNOWLEDGE_BASE_SEMANTICS == FuzzyLogic.LUKASIEWICZ
                and implication_type == LogicOperatorType.LUKASIEWICZ
                or constants.KNOWLEDGE_BASE_SEMANTICS == FuzzyLogic.ZADEH
                and implication_type == LogicOperatorType.ZADEH
            ):
                c: Concept = ImpliesConcept.goedel_implies(
                    AllSomeConcept.some(role, -conc2.curr_concept),
                    -conc1,
                )
                self.role_domain(role, c)
                self.remove_A_is_a_C(key, tau)
                Util.debug(f"Absorbed: domain {role}, {c}")
                return True
        return False

    def __role_absorption_2(self, tau: GeneralConceptInclusion, atomic: bool) -> bool:
        degree: Degree = tau.get_degree()
        n: float = typing.cast(DegreeNumeric, degree).get_numerical_value()
        degree_is_one: bool = n == 1.0
        conc1: Concept = tau.get_subsumed()
        conc2: Concept = tau.get_subsumer()
        key: str = str(conc1)
        implication_type: LogicOperatorType = tau.get_type()
        type_c1: ConceptType = conc1.type
        type_c2: ConceptType = conc2.type

        if (
            type_c1 == ConceptType.SOME
            and typing.cast(AllSomeConcept, conc1).curr_concept
            == TruthConcept.get_top()
            and degree_is_one
        ):
            conc1: AllSomeConcept = typing.cast(AllSomeConcept, conc1)
            assert isinstance(conc1, AllSomeConcept)

            self.role_domain(conc1.role, conc2)
            self.remove_C_is_a_X(key, tau, atomic)
            Util.debug(f"Absorbed: domain {conc1.role}, {conc2}")
            return True
        elif (
            conc1 == TruthConcept.get_top()
            and (type_c2 == ConceptType.ALL or OperatorConcept.is_not_has_value(conc2))
            and degree_is_one
        ):
            role: str = None
            if type_c2 == ConceptType.ALL:
                role = typing.cast(AllSomeConcept, conc2).role
                c_range: Concept = typing.cast(AllSomeConcept, conc2).curr_concept
            else:
                assert isinstance(conc2, OperatorConcept)
                has_value: Concept = conc2.get_atom()
                assert isinstance(has_value, HasValueInterface)
                role = has_value.role
                c_range: Concept = NegatedNominal(str(has_value.value))
            self.role_range(role, c_range)
            self.remove_C_is_a_X(key, tau, atomic)
            Util.debug(f"Absorbed: range {role}, {c_range}")
            return True
        elif type_c1 in (ConceptType.SOME, ConceptType.HAS_VALUE) and degree_is_one:
            assert isinstance(conc1, HasRoleInterface)
            c: Concept = ImpliesConcept.goedel_implies(conc1, conc2)
            self.role_domain(conc1.role, c)
            self.remove_C_is_a_X(key, tau, atomic)
            Util.debug(f"Absorbed: domain {conc1.role}, {c}")
            return True
        else:
            if (
                type_c2 == ConceptType.ALL or OperatorConcept.is_not_has_value(conc2)
            ) and degree_is_one:
                if OperatorConcept.is_not_has_value(conc2):
                    atom: Concept = typing.cast(OperatorConcept, conc2).get_atom()
                    assert isinstance(atom, HasRoleInterface)
                    role: str = atom.role
                else:
                    assert isinstance(conc2, HasRoleInterface)
                    role: str = conc2.role

                if self.is_crisp_role(role) and (
                    implication_type != LogicOperatorType.KLEENE_DIENES
                    or constants.KNOWLEDGE_BASE_SEMANTICS == FuzzyLogic.CLASSICAL
                ):
                    c: Concept = ImpliesConcept.goedel_implies(conc1, conc2)
                    self.role_domain(role, c)
                    self.remove_C_is_a_X(key, tau, atomic)
                    Util.debug(f"Absorbed: domain {role}, {c}")
                    return True
                if (
                    constants.KNOWLEDGE_BASE_SEMANTICS == FuzzyLogic.CLASSICAL
                    or constants.KNOWLEDGE_BASE_SEMANTICS == FuzzyLogic.LUKASIEWICZ
                    and implication_type == LogicOperatorType.LUKASIEWICZ
                    or constants.KNOWLEDGE_BASE_SEMANTICS == FuzzyLogic.ZADEH
                    and implication_type == LogicOperatorType.ZADEH
                ):
                    if type_c2 == ConceptType.ALL:
                        g_imp_concept: Concept = ImpliesConcept.goedel_implies(
                            AllSomeConcept.some(
                                role, -typing.cast(AllSomeConcept, conc2).curr_concept
                            ),
                            -conc1,
                        )
                    else:
                        g_imp_concept: Concept = ImpliesConcept.goedel_implies(
                            HasValueConcept(
                                role,
                                str(
                                    typing.cast(
                                        HasValueConcept,
                                        typing.cast(OperatorConcept, conc2).get_atom(),
                                    ).value
                                ),
                            ),
                            -conc1,
                        )
                    self.role_domain(role, g_imp_concept)
                    self.remove_C_is_a_X(key, tau, atomic)
                    Util.debug(f"Absorbed: domain {role}, {g_imp_concept}")
                    return True
            Util.debug(
                f"Test RE4 conditions: type1 = {type_c1} : type inclusion = {implication_type}"
            )
            if (
                type_c1 == ConceptType.AND
                or type_c1 == ConceptType.LUKASIEWICZ_AND
                and implication_type == LogicOperatorType.LUKASIEWICZ
                or type_c1 == ConceptType.GOEDEL_AND
                and implication_type
                in (
                    LogicOperatorType.LUKASIEWICZ,
                    LogicOperatorType.GOEDEL,
                    LogicOperatorType.ZADEH,
                )
            ) and degree_is_one:
                conc1: OperatorConcept = typing.cast(OperatorConcept, conc1)
                vc: list[Concept] = [c.clone() for c in conc1.concepts]
                for j, ci in enumerate(conc1.concepts):
                    if ci.type in (ConceptType.SOME, ConceptType.HAS_VALUE):
                        del vc[j]
                        if ci.type == ConceptType.SOME:
                            ci: AllSomeConcept = typing.cast(AllSomeConcept, ci)
                        else:
                            ci: HasValueConcept = typing.cast(HasValueConcept, ci)

                        if type_c1 == ConceptType.LUKASIEWICZ_AND:
                            new_c1: Concept = ImpliesConcept.lukasiewicz_implies(
                                OperatorConcept.lukasiewicz_and(*vc), conc2
                            )
                        elif type_c1 == ConceptType.GOEDEL_AND:
                            new_c1: Concept = ImpliesConcept.goedel_implies(
                                OperatorConcept.goedel_and(*vc), conc2
                            )
                        else:
                            new_c1: Concept = ImpliesConcept.lukasiewicz_implies(
                                OperatorConcept.and_(*vc), conc2
                            )
                        self.role_domain(ci.role, new_c1)
                        self.remove_C_is_a_X(key, tau, atomic)
                        Util.debug(f"Absorbed RE4: domain {ci.role}, {new_c1}")
                        return True
            return False

    @typing.overload
    def gci_transformation(
        self, tau: GeneralConceptInclusion, atomic: bool
    ) -> bool: ...

    @typing.overload
    def gci_transformation(self, pcd: PrimitiveConceptDefinition) -> bool: ...

    def gci_transformation(self, *args) -> bool:
        assert len(args) in [1, 2]
        if len(args) == 1:
            assert isinstance(args[0], PrimitiveConceptDefinition)
            return self.__gci_transformation_2(*args)
        else:
            assert isinstance(args[0], GeneralConceptInclusion)
            assert isinstance(args[1], bool)
            return self.__gci_transformation_1(*args)

    def __gci_transformation_1(
        self, tau: GeneralConceptInclusion, atomic: bool
    ) -> bool:
        degree: Degree = tau.get_degree()
        n: float = typing.cast(DegreeNumeric, degree).get_numerical_value()
        conc1: Concept = tau.get_subsumed()
        conc2: Concept = tau.get_subsumer()
        implication_type: LogicOperatorType = tau.get_type()
        type_c1: ConceptType = conc1.type
        type_c2: ConceptType = conc2.type
        if type_c2 in (ConceptType.AND, ConceptType.GOEDEL_AND):
            conc2: OperatorConcept = typing.cast(OperatorConcept, conc2)
            for ci in conc2.concepts:
                self.gci_transformation_add_axiom_to_C_is_a_X(
                    ci, conc1, degree, implication_type
                )
                Util.debug(f"Absorbed CT1, FT1: {conc1} ==> {ci}")
            return True
        if type_c1 in (ConceptType.OR, ConceptType.GOEDEL_OR):
            conc1: OperatorConcept = typing.cast(OperatorConcept, conc1)
            for ci in conc1.concepts:
                if ci.is_atomic():
                    self.gci_transform_define_atomic_concept(
                        str(ci), conc2, implication_type, n
                    )
                    Util.debug(f"Absorbed CT2, FT2: {ci} ==> {conc2}")
                    continue
                self.gci_transformation_add_axiom_to_C_is_a_X(
                    conc2, ci, degree, implication_type
                )
                Util.debug(f"Absorbed CT2, FT2: {ci} ==> {conc2}")
            return True
        return False

    def __gci_transformation_2(self, pcd: PrimitiveConceptDefinition) -> bool:
        a: str = pcd.get_defined_concept()
        conc2: Concept = pcd.get_definition()
        implication_type: LogicOperatorType = pcd.get_type()
        n: float = pcd.get_degree()
        type_c2: ConceptType = conc2.type
        if type_c2 in (ConceptType.AND, ConceptType.GOEDEL_AND):
            conc2: OperatorConcept = typing.cast(OperatorConcept, conc2)
            for ci in conc2.concepts:
                self.gci_transform_define_atomic_concept(a, ci, implication_type, n)
                Util.debug(f"Absorbed CT1, FT1: {a} ==> {ci}")
            return True
        return False

    def nominal_absorption(
        self, conc1: Concept, conc2: Concept, degree: Degree
    ) -> bool:
        if conc2.type == ConceptType.HAS_VALUE:
            conc2: HasValueConcept = typing.cast(HasValueConcept, conc2)

            r: str = conc2.role
            o: Individual = self.get_individual(str(conc2.value))
            iv: set[str] = self.inverse_roles.get(r)
            if iv is not None:
                inv_r: str = next(iv)
            else:
                inv_r: str = f"{r}{Concept.SPECIAL_STRING}inverse"
                self.add_inverse_roles(r, inv_r)
                self.abstract_roles.add(inv_r)
            c_all: Concept = AllSomeConcept.all(inv_r, conc1)
            self.add_assertion(o, c_all, degree)
            return True
        return False

    def add_gci(
        self,
        conc1: Concept,
        conc2: Concept,
        degree: Degree,
        logic_type: LogicOperatorType,
    ) -> None:
        new_degree: float = typing.cast(DegreeNumeric, degree).get_numerical_value()
        if new_degree == 1.0 and logic_type != LogicOperatorType.KLEENE_DIENES:
            logic_type = LogicOperatorType.LUKASIEWICZ
        if self.is_redundant_gci(conc2, conc1, logic_type, new_degree):
            return
        if self.nominal_absorption(conc1, conc2, degree):
            return
        is_c1_atomic: bool = conc1.is_atomic()
        if is_c1_atomic:
            gcis: set[GeneralConceptInclusion] = self.axioms_C_is_a_A.get(
                str(conc2), set()
            )
        else:
            gcis: set[GeneralConceptInclusion] = self.axioms_C_is_a_D.get(
                str(conc2), set()
            )
        for curr_gci in gcis:
            old_c1: Concept = curr_gci.get_subsumer()
            old_c2: Concept = curr_gci.get_subsumed()
            old_degree: float = typing.cast(
                DegreeNumeric, curr_gci.get_degree()
            ).get_numerical_value()
            if conc1 != old_c1 or conc2 != old_c2 or curr_gci.get_type() != logic_type:
                continue
            if new_degree > old_degree:
                self.remove_C_is_a_X(str(old_c2), curr_gci, is_c1_atomic)
                self.add_axiom_to_C_is_a_X(
                    conc1, conc2, degree, logic_type, is_c1_atomic
                )
                Util.debug(f"Axiom {conc1} subsumes {conc2} has the degree updated.")
            else:
                Util.debug(
                    f"Axiom {conc1} subsumes {conc2} is been already processed hence ignored."
                )
            return
        self.add_axiom_to_C_is_a_X(conc1, conc2, degree, logic_type, is_c1_atomic)

    def add_axiom_to_C_is_a_A(
        self,
        conc1: Concept,
        conc2: Concept,
        degree: Degree,
        logic_type: LogicOperatorType,
    ) -> None:
        n: float = typing.cast(DegreeNumeric, degree).get_numerical_value()
        if self.is_redundant_gci(conc2, conc1, logic_type, n):
            return
        if self.nominal_absorption(conc1, conc2, degree):
            return
        new_gci: GeneralConceptInclusion = GeneralConceptInclusion(
            conc1, conc2, degree, logic_type
        )
        key: str = str(new_gci.get_subsumed())
        gci_set: set[GeneralConceptInclusion] = self.axioms_C_is_a_A.get(key, set())
        for curr_gci in gci_set:
            if (
                conc1 != curr_gci.get_subsumer()
                or conc2 != curr_gci.get_subsumed()
                or curr_gci.get_type() != logic_type
            ):
                continue
            old_degree: float = typing.cast(
                DegreeNumeric, curr_gci.get_degree()
            ).get_numerical_value()
            if n > old_degree:
                curr_gci.set_degree(degree)
            return
        gci_set.add(new_gci)
        self.axioms_C_is_a_A[key] = gci_set

    def gci_transformation_add_axiom_to_C_is_a_X(
        self,
        conc1: Concept,
        conc2: Concept,
        degree: Degree,
        logic_type: LogicOperatorType,
    ) -> None:
        n: float = typing.cast(DegreeNumeric, degree).get_numerical_value()
        if self.is_redundant_gci(conc2, conc1, logic_type, n):
            return
        new_gci: GeneralConceptInclusion = GeneralConceptInclusion(
            conc1, conc2, degree, logic_type
        )
        key: str = str(new_gci.get_subsumed())
        if conc1.is_atomic():
            self.axioms_to_do_tmp_C_is_a_A[key] = self.axioms_to_do_tmp_C_is_a_A.get(
                key, set()
            ) | set([new_gci])
        else:
            self.axioms_to_do_tmp_C_is_a_D[key] = self.axioms_to_do_tmp_C_is_a_D.get(
                key, set()
            ) | set([new_gci])

    def add_axiom_to_C_is_a_X(
        self,
        conc1: Concept,
        conc2: Concept,
        degree: Degree,
        logic_type: LogicOperatorType,
        atomic: bool,
    ) -> None:
        if atomic:
            self.add_axiom_to_C_is_a_A(conc1, conc2, degree, logic_type)
        else:
            self.add_axiom_to_C_is_a_D(conc1, conc2, degree, logic_type)

    def add_axiom_to_C_is_a_D(
        self,
        conc1: Concept,
        conc2: Concept,
        degree: Degree,
        logic_type: LogicOperatorType,
    ) -> None:
        n: float = typing.cast(DegreeNumeric, degree).get_numerical_value()
        if self.is_redundant_gci(conc2, conc1, logic_type, n):
            return
        if self.nominal_absorption(conc1, conc2, degree):
            return
        new_gci: GeneralConceptInclusion = GeneralConceptInclusion(
            conc1, conc2, degree, logic_type
        )
        key: str = str(new_gci.get_subsumed())
        self.axioms_C_is_a_D[key] = self.axioms_C_is_a_D.get(key, set()) | set(
            [new_gci]
        )

    def implies(
        self,
        conc1: Concept,
        conc2: Concept,
        degree: Degree,
    ) -> None:
        if constants.KNOWLEDGE_BASE_SEMANTICS == FuzzyLogic.LUKASIEWICZ:
            self.add_subsumption(conc2, conc1, degree, LogicOperatorType.LUKASIEWICZ)
        else:
            self.add_subsumption(
                conc2,
                conc1,
                DegreeNumeric.get_degree(1.0),
                LogicOperatorType.LUKASIEWICZ,
            )

    def get_inclusion_degree(self, subsumed: str, subsumer: str) -> float:
        parents: dict[str, float] = self.roles_with_all_parents.get(subsumed)
        if parents is not None:
            d: float = parents.get(subsumer)
            if d is not None:
                return d
        return 0.0

    def create_roles_with_all_parents(self) -> None:
        for role_c, parents in self.roles_with_parents.items():
            all_parents: dict[str, float] = dict()
            for role_d, n in parents.items():
                if role_c == role_d:
                    continue
                if role_d not in all_parents:
                    all_parents[role_d] = n
                    if role_d in self.roles_with_parents:
                        self.add_parent_recursively(role_c, all_parents, role_d, n)
                    continue
                old_n: float = all_parents.get(role_d)
                if n <= old_n:
                    continue
                all_parents[role_d] = n
                if role_d not in self.roles_with_parents:
                    continue
                self.add_parent_recursively(role_c, all_parents, role_d, n)
            self.roles_with_all_parents[role_c] = all_parents
            if role_c in self.functional_roles:
                continue
            for r2 in all_parents:
                n: float = parents.get(r2, 0.0)
                if r2 not in self.functional_roles or n != 1.0:
                    continue
                self.functional_roles.add(role_c)

    def add_parent_recursively(
        self, role_c: str, all_parents: dict[str, float], current_role: str, n1: float
    ) -> None:
        parents: dict[str, float] = self.roles_with_parents.get(current_role, set())
        for parent, n2 in parents.items():
            if parent == role_c:
                continue
            if parent not in all_parents:
                all_parents[parent] = n1 + n2 - 1.0
                if parent in self.roles_with_parents:
                    self.add_parent_recursively(
                        role_c, all_parents, parent, n1 + n2 - 1.0
                    )
                continue
            old_n: float = all_parents.get(parent)
            if n1 + n2 - 1.0 <= old_n:
                continue
            all_parents[parent] = n1 + n2 - 1.0
            if parent in self.roles_with_parents:
                self.add_parent_recursively(role_c, all_parents, parent, n1 + n2 - 1.0)

    def create_roles_with_trans_children(self) -> None:
        for role_c in self.roles_with_all_parents:
            if role_c not in self.transitive_roles:
                continue
            parents: dict[str, float] = self.roles_with_all_parents.get(role_c, dict())
            for role_p in parents:
                self.roles_with_trans_children[role_p] = (
                    self.roles_with_trans_children.get(role_p, []) + [role_c]
                )

    def role_subsumes(self, subsumer: str, subsumed: str, n: float) -> None:
        if subsumer == subsumed:
            return
        parents: dict[str, float] = self.roles_with_parents.get(subsumed, dict())
        if subsumer not in parents:
            parents[subsumer] = n
            self.roles_with_parents[subsumed] = parents
        else:
            old: float = parents.get(subsumer)
            if n > old:
                parents[subsumer] = n
            else:
                return

        Util.debug(f"Add: {subsumed} ==> {subsumer}, {n}")

    @typing.overload
    def role_subsumes_bool(self, subsumer: str, subsumed: str, n: float) -> bool: ...

    @typing.overload
    def role_subsumes_bool(
        self,
        subsumer: str,
        subsumed: str,
        n: float,
        p_list: dict[str, dict[str, float]],
    ) -> bool: ...

    def role_subsumes_bool(self, *args) -> bool:
        assert len(args) in [3, 4]
        assert isinstance(args[0], str)
        assert isinstance(args[1], str)
        assert isinstance(args[2], constants.NUMBER)
        if len(args) == 3:
            return self.__role_subsumes_bool_1(*args)
        elif len(args) == 4:
            trycast.checkcast(dict[str, dict[str, float]], args[3])
            return self.__role_subsumes_bool_2(*args)
        else:
            raise ValueError

    def __role_subsumes_bool_1(self, subsumer: str, subsumed: str, n: float) -> bool:
        if subsumer == subsumed:
            return False
        parents: dict[str, float] = self.roles_with_parents.get(subsumed, dict())
        if subsumer not in parents:
            parents[subsumer] = n
            self.roles_with_parents[subsumed] = parents
        else:
            old: float = parents.get(subsumer)
            if n > old:
                parents[subsumer] = n
            else:
                return False
        Util.debug(f"Add: {subsumed} ==> {subsumer}, {n}")
        return True

    def __role_subsumes_bool_2(
        self,
        subsumer: str,
        subsumed: str,
        n: float,
        p_list: dict[str, dict[str, float]],
    ) -> bool:
        if subsumer == subsumed:
            return False
        parents: dict[str, float] = p_list.get(subsumed, dict())
        if subsumer not in parents:
            parents[subsumer] = n
            p_list[subsumed] = parents
        else:
            old: float = parents.get(subsumer)
            if n > old:
                parents[subsumer] = n
            else:
                return False
        Util.debug(f"Add tmp: {subsumed} ==> {subsumer}, {n}")
        return True

    def unblock_children(self, ancestor: str) -> None:
        db_children: list[str] = self.directly_blocked_children.get(ancestor)
        if db_children is None:
            return
        del self.directly_blocked_children[ancestor]
        for name in db_children:
            self.unblock_individual(name)

    def unblock_individual(self, node_name: str) -> None:
        node: CreatedIndividual = typing.cast(
            CreatedIndividual, self.individuals.get(node_name)
        )
        CreatedIndividualHandler.unblock_directly_blocked(node, self)
        CreatedIndividualHandler.mark_indirectly_simple_unchecked(node, self)
        # node.unblock_directly_blocked(self)
        # node.mark_indirectly_simple_unchecked(self)

    def check_trans_role_applied(self, rel: Relation, restrict: Restriction) -> bool:
        already_applied: bool = False
        rule: str = f"{rel} {restrict.get_name_without_degree()}"
        if rule in self.applied_trans_role_rules:
            already_applied = True
        else:
            self.applied_trans_role_rules.append(rule)
        Util.debug(f"Checking rule applied {rule} is {already_applied}")
        return already_applied

    def add_datatype_restriction(
        self, restriction_type: RestrictionType, o: typing.Any, f_name: str
    ) -> Concept:
        t: ConcreteFeature = self.concrete_features.get(f_name)
        if t is None:
            Util.error(f"Error: Concrete feature {f_name} is not defined")
        if isinstance(o, FeatureFunction):
            fun: FeatureFunction = typing.cast(FeatureFunction, o)
            f_type: FeatureFunctionType = fun.get_type()
            if f_type == FeatureFunctionType.ATOMIC:
                name: str = str(fun)
                tfn: TriangularFuzzyNumber = self.fuzzy_numbers.get(name)
                if tfn is not None:
                    o = tfn
                else:
                    bv: bool = self.milp.has_variable(name)
                    if bv:
                        o = self.milp.get_variable(name)
            elif f_type == FeatureFunctionType.NUMBER:
                o = fun.get_number()
        t_type: ConcreteFeatureType = t.get_type()
        if not isinstance(o, Variable):
            if t_type == ConcreteFeatureType.STRING:
                if not isinstance(o, str):
                    return TruthConcept.get_bottom()
                self.temp_string_list.append(str(o))
            elif t_type in (ConcreteFeatureType.INTEGER, ConcreteFeatureType.REAL):
                if not isinstance(
                    o, (int, float, FeatureFunction, TriangularFuzzyNumber)
                ):
                    return TruthConcept.get_bottom()
            elif t_type == ConcreteFeatureType.BOOLEAN:
                if isinstance(o, str):
                    Util.error(f"Error: Found '{o}' instead of a boolean value.")
                if str(o).lower() not in ["true", "false"]:
                    Util.error(f"Error: Found '{o}' instead of a boolean value.")
                if restriction_type != RestrictionType.EXACT_VALUE:
                    Util.error(
                        "Error: Only = restrictions are allowed for boolean values."
                    )
                o = str(o).lower() == "true"
        if restriction_type == RestrictionType.AT_MOST_VALUE:
            c: Concept = ValueConcept.at_most_value(f_name, o)
        elif restriction_type == RestrictionType.AT_LEAST_VALUE:
            c: Concept = ValueConcept.at_least_value(f_name, o)
        else:
            c: Concept = ValueConcept.exact_value(f_name, o)
        if t_type == ConcreteFeatureType.STRING:
            self.temp_string_concept_list.append(c)
        return c

    def get_language(self) -> str:
        return self.language

    def compute_language(self) -> None:
        if len(self.transitive_roles) != 0:
            self.language = "S"
        else:
            self.language = "ALC"
        if len(self.roles_with_parents) != 0 or len(self.symmetric_roles) != 0:
            self.language += "H"
        if self.has_nominals_in_tbox() or self.has_nominals_in_abox():
            self.language += "B"
        if len(self.inverse_roles) != 0 or len(self.symmetric_roles) != 0:
            self.language += "I"
        if len(self.functional_roles) != 0:
            self.language += "F"
        if self.concrete_fuzzy_concepts:
            self.language += "(D)"
        Util.debug(f"Expressivity = {self.language}")

    def has_nominals_in_abox(self) -> bool:
        for ass in self.assertions:
            if ass.get_concept().has_nominals():
                return True
        return False

    def has_nominals_in_tbox(self) -> bool:
        for equivs in self.axioms_A_equiv_C.values():
            for c in equivs:
                if c.has_nominals():
                    return True
        for pcds in self.axioms_A_is_a_C.values():
            for pcd in pcds:
                if pcd.get_definition().has_nominals():
                    return True
        for equiv in self.axioms_C_equiv_D:
            if equiv.get_c1().has_nominals() or equiv.get_c2().has_nominals():
                return True
        for gcis in self.axioms_C_is_a_A.values():
            for gci in gcis:
                if gci.get_subsumed().has_nominals():
                    return True
        for gcis in self.axioms_C_is_a_D.values():
            for gci in gcis:
                if (
                    gci.get_subsumed().has_nominals()
                    or gci.get_subsumer().has_nominals()
                ):
                    return True
        for gci in self.t_G:
            if gci.get_subsumed().has_nominals() or gci.get_subsumer().has_nominals():
                return True
        for c in self.t_definitions.values():
            if c.has_nominals():
                return True
        for pcds in self.t_inclusions.values():
            for pcd in pcds:
                if pcd.get_definition().has_nominals():
                    return True
        return False

    def compute_blocking_type(self) -> None:
        Util.debug(f"{constants.SEPARATOR}Blocking Type{constants.SEPARATOR}")
        if ConfigReader.OPTIMIZATIONS == 0:
            self.blocking_type = BlockingDynamicType.DOUBLE_BLOCKING
            self.blocking_dynamic = True
            Util.debug("No optimization: DOUBLE_BLOCKING + dynamicblocking")
            return
        if len(self.inverse_roles) == 0 or len(self.functional_roles) == 0:
            if len(self.t_G) == 0 and self.is_tbox_acyclic():
                self.blocking_type = BlockingDynamicType.NO_BLOCKING
                Util.debug("NO_BLOCKING")
            else:
                self.blocking_dynamic = (
                    len(self.inverse_roles) != 0 or len(self.domain_restrictions) != 0
                )
                Util.debug(f"Dynamic Blocking = {self.blocking_dynamic}")
                if len(self.transitive_roles) == 0 and len(self.functional_roles) == 0:
                    if ConfigReader.ANYWHERE_SIMPLE_BLOCKING:
                        if not self.blocking_dynamic:
                            self.blocking_type = (
                                BlockingDynamicType.ANYWHERE_SUBSET_BLOCKING
                            )
                            Util.debug("ANYWHERE_SUBSET_BLOCKING")
                        else:
                            self.blocking_type = (
                                BlockingDynamicType.ANYWHERE_SET_BLOCKING
                            )
                            Util.debug("ANYWHERE_SET_BLOCKING")
                    else:
                        self.blocking_type = BlockingDynamicType.SUBSET_BLOCKING
                        Util.debug("SUBSET_BLOCKING")
                elif ConfigReader.ANYWHERE_SIMPLE_BLOCKING:
                    self.blocking_type = BlockingDynamicType.ANYWHERE_SET_BLOCKING
                    Util.debug("ANYWHERE_SET_BLOCKING")
                else:
                    self.blocking_type = BlockingDynamicType.SET_BLOCKING
                    Util.debug("SET_BLOCKING")
        elif not ConfigReader.ANYWHERE_DOUBLE_BLOCKING:
            self.blocking_type = BlockingDynamicType.DOUBLE_BLOCKING
            self.blocking_dynamic = True
            Util.debug(f"DOUBLE_BLOCKING + dynamicblocking")
        else:
            self.blocking_type = BlockingDynamicType.ANYWHERE_DOUBLE_BLOCKING
            self.blocking_dynamic = True
            Util.debug(f"ANYWHERE PAIRWISE BLOCKING + dynamicblocking")

    def convert_strings_into_integers(self) -> None:
        if self.temp_string_list != None:
            num_strings: int = 0
            self.temp_string_list = sorted(self.temp_string_list)
            if len(self.temp_string_list) > 0:
                num_strings += 1
                previous: str = self.temp_string_list[0]
                self.order[previous] = int(num_strings)
                for current in self.temp_string_list[1:]:
                    if previous != current:
                        num_strings += 1
                        self.order[current] = num_strings
                    previous = current
            if num_strings > 0:
                for t in self.concrete_features.values():
                    if t.get_type() == ConcreteFeatureType.STRING:
                        t.set_type(ConcreteFeatureType.INTEGER)
                        t.set_range(0, num_strings + 1)
                for con in self.temp_string_concept_list:
                    assert isinstance(con, HasValueInterface)
                    old_value: str = str(con.value)
                    aux: int = self.order.get(old_value)
                    con.value = aux
                    self.milp.add_string_value(old_value, aux - 1)
            self.temp_string_list = None
            self.temp_string_concept_list = None

    @typing.overload
    def restrict_range(self, x_b: Variable, k1: float, k2: float) -> None: ...

    @typing.overload
    def restrict_range(
        self, x_b: Variable, x_f: Variable, k1: float, k2: float
    ) -> None: ...

    def restrict_range(self, *args) -> None:
        assert len(args) in [3, 4]
        assert isinstance(args[0], Variable)
        if len(args) == 3:
            assert isinstance(args[1], constants.NUMBER)
            assert isinstance(args[2], constants.NUMBER)
            self.__restrict_range_1(*args)
        else:
            assert isinstance(args[1], Variable)
            assert isinstance(args[2], constants.NUMBER)
            assert isinstance(args[3], constants.NUMBER)
            self.__restrict_range_2(*args)

    def __restrict_range_1(self, x_b: Variable, k1: float, k2: float) -> None:
        self.milp.add_new_constraint(
            Expression(-k1, Term(1.0, x_b)), InequalityType.GREATER_THAN
        )
        self.milp.add_new_constraint(
            Expression(-k2, Term(1.0, x_b)), InequalityType.LESS_THAN
        )

    def __restrict_range_2(
        self, x_b: Variable, x_f: Variable, k1: float, k2: float
    ) -> None:
        """
        Restricts the range of a variable to [k1, k2] if x_f not zero
        """
        # x_b \geq k1
        self.milp.add_new_constraint(
            Expression(
                constants.MAXVAL,
                Term(1.0, x_b),
                Term(-k1, x_f),
                Term(-constants.MAXVAL, x_f),
            ),
            InequalityType.GREATER_THAN,
        )
        # x_b \leq k2
        self.milp.add_new_constraint(
            Expression(
                -constants.MAXVAL,
                Term(1.0, x_b),
                Term(-k2, x_f),
                Term(constants.MAXVAL, x_f),
            ),
            InequalityType.LESS_THAN,
        )

    @typing.overload
    def get_new_individual(self) -> CreatedIndividual: ...

    @typing.overload
    def get_new_individual(
        self, parent: Individual, f_name: str
    ) -> CreatedIndividual: ...

    def get_new_individual(self, *args) -> CreatedIndividual:
        assert len(args) in [0, 2]
        if len(args) == 0:
            return self.__get_new_individual_1()
        else:
            assert args[0] is None or isinstance(args[0], Individual)
            assert args[1] is None or isinstance(args[1], str)
            return self.__get_new_individual_2(*args)

    def __get_new_individual_1(self) -> CreatedIndividual:
        return self.get_new_individual(None, None)

    def __get_new_individual_2(
        self, parent: Individual, f_name: str
    ) -> CreatedIndividual:
        b: CreatedIndividual = self.get_new_individual_common_code(parent, f_name)
        self.add_individual(str(b), b)
        return b

    def get_new_individual_common_code(
        self, parent: Individual, f_name: str
    ) -> CreatedIndividual:
        self.num_defined_individuals += 1
        ind_name: str = f"i{self.num_defined_individuals}"
        b: CreatedIndividual = CreatedIndividual(ind_name, parent, f_name)
        CreatedIndividualHandler.update_role_successors(ind_name, f_name, self)
        if b.get_depth() > self.max_depth:
            self.max_depth = b.get_depth()
        return b

    def get_new_concrete_individual(
        self, parent: Individual, f_name: str
    ) -> CreatedIndividual:

        b: CreatedIndividual = self.get_new_individual_common_code(parent, f_name)
        b.set_concrete_individual()
        self.add_created_individual(str(b), b)
        return b

    def solve_one_exist_assertion(self) -> None:
        while len(self.exist_assertions) > 0:
            ass: Assertion = self.exist_assertions[0]
            Util.debug(
                f"{constants.SEPARATOR}Processing Existential Assertion{constants.SEPARATOR}"
            )
            Util.debug(f"{ass}")
            if self.is_assertion_processed(ass):
                Util.debug(f"Assertion (without the degree): {ass} already processed.")
                del self.exist_assertions[0]
            else:
                if ass.get_individual().is_blockable():
                    subject: CreatedIndividual = typing.cast(
                        CreatedIndividual, ass.get_individual()
                    )
                    Util.debug(f"Testing if created individual {subject} is blocked.")
                    if CreatedIndividualHandler.is_blocked(subject, self):
                        name: str = str(ass.get_individual())
                        self.blocked_exist_assertions[name] = (
                            self.blocked_exist_assertions.get(name, []) + [ass]
                        )
                        del self.exist_assertions[0]
                        continue
                if self.num_defined_individuals == ConfigReader.MAX_INDIVIDUALS:
                    Util.error(
                        f"Error: Maximal number of individuals created: {self.num_defined_individuals}"
                    )
                else:
                    Util.debug("NO blocking")
                    self.rule_some(ass)
                self.mark_process_assertion(ass)
                del self.exist_assertions[0]
                return

    def solve_kb(self) -> None:
        if constants.KNOWLEDGE_BASE_SEMANTICS is None:
            self.set_logic(FuzzyLogic.LUKASIEWICZ)
        self.compute_language()
        self.convert_strings_into_integers()
        self.solve_inverse_roles()
        self.solve_role_inclusion_axioms()
        self.solve_reflexive_roles()
        self.solve_functional_roles()
        self.preprocess_tbox()
        self.print_tbox()
        self.compute_blocking_type()
        self.KB_LOADED = True

    def solve_domain_and_range_axioms(self) -> None:
        for ind in self.individuals.values():
            for rels in ind.role_relations.values():
                for rel in rels:
                    for domain_role in self.domain_restrictions:
                        self.rule_domain_lazy_unfolding(domain_role, rel)
                    for range_role in self.range_restrictions:
                        self.rule_range_lazy_unfolding(range_role, rel)

    def rule_domain_lazy_unfolding(self, domain_role: str, rel: Relation) -> None:
        role: str = rel.get_role_name()
        n: float = self.get_inclusion_degree(role, domain_role)
        if domain_role == role:
            n = 1.0
        if n > 0.0:
            a: Individual = rel.get_subject_individual()
            if a.is_blockable() and CreatedIndividualHandler.is_indirectly_blocked(
                typing.cast(CreatedIndividual, a), self
            ):
                return
            for c in self.domain_restrictions.get(domain_role):
                a_is_c: Variable = self.milp.get_variable(a, c)
                x_rel: Variable = self.milp.get_variable(rel)
                self.add_assertion(a, c, DegreeVariable.get_degree(a_is_c))
                if constants.KNOWLEDGE_BASE_SEMANTICS == FuzzyLogic.LUKASIEWICZ:
                    LukasiewiczSolver.and_geq_equation(a_is_c, x_rel, n, self.milp)
                    continue
                ZadehSolver.and_geq_equation(a_is_c, x_rel, n, self.milp)

    def rule_range_lazy_unfolding(self, range_role: str, rel: Relation) -> None:
        role: str = rel.get_role_name()
        n: float = self.get_inclusion_degree(role, range_role)
        if range_role == role:
            n = 1.0
        if n > 0.0:
            b: Individual = rel.get_object_individual()
            if b.is_blockable() and CreatedIndividualHandler.is_indirectly_blocked(
                typing.cast(CreatedIndividual, b), self
            ):
                return
            for c in self.range_restrictions.get(range_role):
                if isinstance(c, NegatedNominal):
                    b_is_c: Variable = self.milp.get_negated_nominal_variable(
                        str(b), typing.cast(NegatedNominal, c).ind_name
                    )
                else:
                    b_is_c: Variable = self.milp.get_variable(b, c)
                    self.add_assertion(b, c, DegreeVariable.get_degree(b_is_c))
                x_rel: Variable = self.milp.get_variable(rel)
                if constants.KNOWLEDGE_BASE_SEMANTICS == FuzzyLogic.LUKASIEWICZ:
                    LukasiewiczSolver.and_geq_equation(b_is_c, x_rel, n, self.milp)
                    continue
                ZadehSolver.and_geq_equation(b_is_c, x_rel, n, self.milp)

    def solve_abox(self) -> None:
        if not self.ABOX_EXPANDED:
            self.solve_assertions()
            self.ABOX_EXPANDED = True

    def solve_assertions(self) -> None:
        if self.KB_UNSAT:
            raise InconsistentOntologyException("Unsatisfiable fuzzy KB")

        while True:
            for ass in self.assertions:
                Util.debug(
                    f"{constants.SEPARATOR}Processing assertion{constants.SEPARATOR}"
                )
                Util.debug(f"{ass}")
                deg: Degree = ass.get_lower_limit()
                if deg.is_numeric() and deg.is_number_zero():
                    self.mark_process_assertion(ass)
                    Util.debug(
                        f"{constants.SEPARATOR}Assertion completed{constants.SEPARATOR}"
                    )
                    continue

                # Use right version of the individual (needed when we clone the KB or merge individuals)
                self.get_correct_version_of_individual(ass)
                if ass.get_individual().is_blockable():
                    Util.debug(
                        f"Direct Blocking status {typing.cast(CreatedIndividual, ass.get_individual()).directly_blocked}"
                    )
                    Util.debug(
                        f"Indirect Blocking status {typing.cast(CreatedIndividual, ass.get_individual()).indirectly_blocked}"
                    )

                # If the individual is indirectly blocked we skip the assertion
                if (
                    ass.get_individual().is_blockable()
                    and CreatedIndividualHandler.is_indirectly_blocked(
                        typing.cast(CreatedIndividual, ass.get_individual()), self
                    )
                ):
                    name: str = str(ass.get_individual())
                    Util.debug(
                        "Skipping assertion (it has an indirectly blocked individual)"
                    )
                    self.blocked_assertions[name] = self.blocked_assertions.get(
                        name, []
                    ) + [ass]
                    continue

                # Add xAss >= lowerBound
                self.milp.add_new_constraint(ass)
                if self.is_assertion_processed(ass):
                    Util.debug(
                        f"Assertion (without the degree): {ass} already processed."
                    )
                    continue

                ind: Individual = ass.get_individual()
                ci: Concept = ass.get_concept()
                self.add_negated_equations(ind, ci)
                c_type: ConceptType = ass.get_type()

                # Apply reasoning rule according to the type of the assertion
                if c_type == ConceptType.ATOMIC:
                    self.rule_atomic(ass)
                elif ci.is_complemented_atomic():
                    self.rule_complemented_atomic(ass)
                elif c_type == ConceptType.AND:
                    self.rule_and(ass)
                elif c_type == ConceptType.OR:
                    self.rule_or(ass)
                elif c_type in (ConceptType.SOME, ConceptType.HAS_VALUE):
                    self.exist_assertions.append(ass)
                    continue
                elif c_type == ConceptType.ALL:
                    self.rule_all(ass)
                elif OperatorConcept.is_not_has_value(ci):
                    self.rule_complemented_has_value(ass)
                elif c_type == ConceptType.CONCRETE:
                    self.rule_concrete(ass)
                elif OperatorConcept.is_not_concrete(ci):
                    self.rule_complemented_concrete(ass)
                elif c_type == ConceptType.FUZZY_NUMBER:
                    self.rule_fuzzy_number(ass)
                elif OperatorConcept.is_not_fuzzy_number(ci):
                    self.rule_complemented_fuzzy_number(ass)
                elif c_type == ConceptType.MODIFIED:
                    self.rule_modified(ass)
                elif OperatorConcept.is_not_modified(ci):
                    self.rule_complemented_modified(ass)
                elif c_type == ConceptType.TOP:
                    self.rule_top(ass)
                elif c_type == ConceptType.BOTTOM:
                    self.rule_bottom(ass)
                elif c_type in (
                    ConceptType.AT_MOST_VALUE,
                    ConceptType.AT_LEAST_VALUE,
                    ConceptType.EXACT_VALUE,
                ):
                    self.positive_concrete_value_assertions.append(ass)
                elif (
                    OperatorConcept.is_not_at_least_value(ci)
                    or OperatorConcept.is_not_at_most_value(ci)
                    or OperatorConcept.is_not_exact_value(ci)
                ):
                    self.add_negated_datatype_restriction(ass)
                elif c_type == ConceptType.SELF:
                    self.rule_self(ass)
                elif OperatorConcept.is_not_self(ci):
                    self.rule_complemented_self(ass)
                elif c_type == ConceptType.UPPER_APPROX:
                    self.rule_upper_approximation(ass)
                elif c_type == ConceptType.TIGHT_UPPER_APPROX:
                    self.rule_tight_upper_approximation(ass)
                elif c_type == ConceptType.LOOSE_UPPER_APPROX:
                    self.rule_loose_upper_approximation(ass)
                elif c_type == ConceptType.LOWER_APPROX:
                    self.rule_lower_approximation(ass)
                elif c_type == ConceptType.TIGHT_LOWER_APPROX:
                    self.rule_tight_lower_approximation(ass)
                elif c_type == ConceptType.LOOSE_LOWER_APPROX:
                    self.rule_loose_lower_approximation(ass)
                elif c_type == ConceptType.GOEDEL_AND:
                    self.rule_goedel_and(ass)
                elif c_type == ConceptType.LUKASIEWICZ_AND:
                    self.rule_lukasiewicz_and(ass)
                elif c_type == ConceptType.GOEDEL_OR:
                    self.rule_goedel_or(ass)
                elif c_type == ConceptType.LUKASIEWICZ_OR:
                    self.rule_lukasiewicz_or(ass)
                elif c_type == ConceptType.GOEDEL_IMPLIES:
                    self.rule_goedel_implication(ass)
                elif OperatorConcept.is_not_goedel_implies(ci):
                    self.rule_complemented_goedel_implication(ass)
                elif c_type == ConceptType.ZADEH_IMPLIES:
                    self.rule_zadeh_implication(ass)
                elif OperatorConcept.is_not_zadeh_implies(ci):
                    self.rule_complemented_zadeh_implication(ass)
                elif c_type == ConceptType.W_SUM:
                    self.rule_weighted_sum(ass)
                elif OperatorConcept.is_not_weighted_sum(ci):
                    self.rule_complemented_weighted_sum(ass)
                elif c_type == ConceptType.W_SUM_ZERO:
                    self.rule_weighted_sum_zero(ass)
                elif OperatorConcept.is_not_weighted_sum_zero(ci):
                    self.rule_complemented_weighted_sum_zero(ass)
                elif c_type == ConceptType.WEIGHTED:
                    self.rule_weighted_concept(ass)
                elif OperatorConcept.is_not_weighted(ci):
                    self.rule_complemented_weighted_concept(ass)
                elif c_type == ConceptType.POS_THRESHOLD:
                    self.rule_positive_threshold(ass)
                elif OperatorConcept.is_not_pos_threshold(ci):
                    self.rule_complemented_positive_threshold(ass)
                elif c_type == ConceptType.NEG_THRESHOLD:
                    self.rule_negative_threshold(ass)
                elif OperatorConcept.is_not_neg_threshold(ci):
                    self.rule_complemented_negative_threshold(ass)
                elif c_type == ConceptType.EXT_POS_THRESHOLD:
                    self.rule_extended_positive_threshold(ass)
                elif OperatorConcept.is_not_ext_pos_threshold(ci):
                    self.rule_complemented_extended_positive_threshold(ass)
                elif c_type == ConceptType.EXT_NEG_THRESHOLD:
                    self.rule_extended_negative_threshold(ass)
                elif OperatorConcept.is_not_ext_neg_threshold(ci):
                    self.rule_complemented_extended_negative_threshold(ass)
                elif c_type == ConceptType.OWA:
                    self.rule_owa(ass)
                elif OperatorConcept.is_not_owa(ci):
                    self.rule_complemented_owa(ass)
                elif c_type == ConceptType.QUANTIFIED_OWA:
                    self.rule_quantified_owa(ass)
                elif OperatorConcept.is_not_qowa(ci):
                    self.rule_complemented_quantified_owa(ass)
                elif c_type == ConceptType.CHOQUET_INTEGRAL:
                    self.rule_choquet(ass)
                elif OperatorConcept.is_not_choquet(ci):
                    self.rule_complemented_choquet(ass)
                elif c_type == ConceptType.SUGENO_INTEGRAL:
                    self.rule_sugeno(ass)
                elif OperatorConcept.is_not_sugeno(ci):
                    self.rule_complemented_sugeno(ass)
                elif c_type == ConceptType.QUASI_SUGENO_INTEGRAL:
                    self.rule_quasi_sugeno(ass)
                elif OperatorConcept.is_not_quasi_sugeno(ci):
                    self.rule_complemented_quasi_sugeno(ass)
                elif c_type == ConceptType.W_MIN:
                    self.rule_weighted_min(ass)
                elif OperatorConcept.is_not_weighted_min(ci):
                    self.rule_complemented_weighted_min(ass)
                elif c_type == ConceptType.W_MAX:
                    self.rule_weighted_max(ass)
                elif OperatorConcept.is_not_weighted_max(ci):
                    self.rule_complemented_weighted_max(ass)
                else:
                    Util.warning(f"Warning: Assertion with type {c_type}")

                # For each node in labelsWithNodes, apply AssNom rule
                nodes: set[str] = self.labels_with_nodes.get(str(ind))
                if nodes is not None:
                    for node in nodes:
                        self.rule_ass_nom(ind, ci, node)

                self.mark_process_assertion(ass)
                ind.add_concept(ci)
                Util.debug(
                    f"{constants.SEPARATOR}Assertion completed{constants.SEPARATOR}"
                )
            self.assertions.clear()

            # Solve one some rule
            if len(self.assertions) == 0:
                self.solve_one_exist_assertion()

            # Check if there are more assertions
            if len(self.assertions) == 0 and len(self.exist_assertions) == 0:
                break
        # Concrete assertions
        self.solve_concrete_value_assertions()

    def solve_concept_assertion(self, ind: Individual, concept: Concept) -> None:
        if isinstance(concept, ChoquetIntegral):
            self.solve_choquet_integral_assertion(ind, concept)
        elif isinstance(concept, (SugenoIntegral, QsugenoIntegral)):
            self.solve_sugeno_integral_assertion(ind, concept)
        elif isinstance(concept, (OwaConcept, QowaConcept)):
            self.solve_owa_assertion(ind, concept)
        elif isinstance(concept, WeightedMaxConcept):
            self.solve_w_max_assertion(ind, concept)
        elif isinstance(concept, WeightedMinConcept):
            self.solve_w_min_assertion(ind, concept)
        elif isinstance(concept, WeightedSumConcept):
            self.solve_w_sum_assertion(ind, concept)
        elif isinstance(concept, WeightedSumZeroConcept):
            self.solve_w_sum_zero_assertion(ind, concept)
        elif isinstance(concept, CrispConcreteConcept):
            self.solve_crisp_concrete_concept_assertion(ind, concept)
        elif isinstance(concept, LinearConcreteConcept):
            self.solve_linear_concrete_concept_assertion(ind, concept)
        elif isinstance(concept, LeftConcreteConcept):
            self.solve_left_concrete_concept_assertion(ind, concept)
        elif isinstance(concept, RightConcreteConcept):
            self.solve_right_concrete_concept_assertion(ind, concept)
        elif isinstance(concept, TriangularConcreteConcept):
            self.solve_triangular_concrete_concept_assertion(ind, concept)
        elif isinstance(concept, TrapezoidalConcreteConcept):
            self.solve_trapezoidal_concrete_concept_assertion(ind, concept)
        elif isinstance(concept, (ModifiedConcept, ModifiedConcreteConcept)):
            self.solve_modifier_assertion(ind, concept, concept.modifier)
        else:
            raise ValueError

    def solve_concept_complemented_assertion(
        self, ind: Individual, lower_limit: Degree, concept: Concept
    ) -> None:
        if OperatorConcept.is_not_choquet(concept):
            self.solve_choquet_integral_complemented_assertion(ind, concept)
        elif OperatorConcept.is_not_sugeno(
            concept
        ) or OperatorConcept.is_not_quasi_sugeno(concept):
            self.solve_sugeno_integral_complemented_assertion(ind, concept)
        elif OperatorConcept.is_not_owa(concept) or OperatorConcept.is_not_qowa(
            concept
        ):
            self.solve_owa_complemented_assertion(ind, concept)
        elif OperatorConcept.is_not_weighted_max(concept):
            self.solve_w_max_complemented_assertion(ind, concept)
        elif OperatorConcept.is_not_weighted_min(concept):
            self.solve_w_min_complemented_assertion(ind, concept)
        elif OperatorConcept.is_not_weighted_sum(concept):
            self.solve_w_sum_complemented_assertion(ind, concept)
        elif OperatorConcept.is_not_weighted_sum_zero(concept):
            self.solve_w_sum_zero_complemented_assertion(ind, concept)
        elif isinstance(concept, OperatorConcept) and isinstance(
            concept.get_atom(), (ModifiedConcept, ModifiedConcreteConcept)
        ):
            self.solve_modifier_complemented_assertion(ind, concept, lower_limit)
        elif isinstance(concept, OperatorConcept) and isinstance(
            concept.get_atom(), FuzzyConcreteConcept
        ):
            self.solve_fuzzy_concrete_concept_complement_assertion(
                ind, lower_limit, concept
            )
        else:
            raise ValueError

    def solve_modifier_assertion(
        self, ind: Individual, concept: Concept, modifier: Modifier
    ) -> None:
        if isinstance(modifier, LinearModifier):
            self.solve_linear_modifier_assertion(ind, concept, modifier)
        elif isinstance(modifier, TriangularModifier):
            self.solve_triangular_modifier_assertion(ind, concept, modifier)
        else:
            raise ValueError

    def solve_choquet_integral_assertion(
        self, ind: Individual, c: ChoquetIntegral
    ) -> None:
        n: int = len(c.concepts)
        x: list[Variable] = [None] * n
        for i in range(n):
            ci = c.concepts[i]
            x[i] = self.milp.get_variable(ind, ci)
            self.add_assertion(ind, ci, DegreeVariable.get_degree(x[i]))

        z: list[list[Variable]] = [
            [self.milp.get_new_variable(VariableType.BINARY) for _ in range(n)]
            for _ in range(n)
        ]
        y: list[Variable] = self.milp.get_ordered_permutation(x, z)

        exp: Expression = Expression(0.0)
        exp.add_term(Term(c.weights[0], y[0]))
        for k in range(1, n):
            exp.add_term(Term(c.weights[k] - c.weights[k - 1], y[k]))

        degree: DegreeVariable = DegreeVariable.get_degree(
            self.milp.get_variable(ind, c)
        )
        self.milp.add_new_constraint(exp, InequalityType.EQUAL, degree)

    def solve_choquet_integral_complemented_assertion(
        self, ind: Individual, c: OperatorConcept
    ) -> None:
        assert isinstance(c.get_atom(), ChoquetIntegral)
        ci: ChoquetIntegral = c.get_atom()

        n: int = len(ci.concepts)
        x: list[Variable] = [None] * n
        for i in range(n):
            not_ci = -ci.concepts[i]
            x[i] = self.milp.get_variable(ind, not_ci)
            self.add_assertion(ind, not_ci, DegreeVariable.get_degree(x[i]))

        z: list[list[Variable]] = [
            [self.milp.get_new_variable(VariableType.BINARY) for _ in range(n)]
            for _ in range(n)
        ]
        y: list[Variable] = self.milp.get_ordered_permutation(x, z)

        exp = Expression(1.0)
        exp.add_term(Term(-ci.weights[0], y[0]))
        for k in range(1, n):
            exp.add_term(Term(ci.weights[k - 1] - ci.weights[k], y[k]))

        degree: DegreeVariable = DegreeVariable.get_degree(
            self.milp.get_variable(ind, c)
        )
        self.milp.add_new_constraint(exp, InequalityType.EQUAL, degree)
        self.rule_complemented(ind, c)

    def solve_owa_assertion(
        self, ind: Individual, c: typing.Union[OwaConcept, QowaConcept]
    ) -> None:
        if ConfigReader.OPTIMIZATIONS == 0:
            n: int = len(c.concepts)
            x: list[Variable] = []
            for i in range(n):
                ci: Concept = c.concepts[i]
                x.append(self.milp.get_variable(ind, ci))
                self.add_assertion(ind, ci, DegreeVariable.get_degree(x[i]))

            y: list[Variable] = self.milp.get_ordered_permutation(x)
            exp: Expression = Expression()
            for j in range(n):
                exp.add_term(Term(c.weights[j], y[j]))
            degree: DegreeVariable = DegreeVariable.get_degree(
                self.milp.get_variable(ind, c)
            )
            self.milp.add_new_constraint(exp, InequalityType.EQUAL, degree)
        else:
            n: int = len(c.concepts)
            w1: float = c.weights[0]
            wn: float = c.weights[n - 1]
            a: float = 1.0 / n - (wn - w1) / 2.0
            exp: Expression = Expression()
            x: list[Variable] = []
            for i in range(n):
                ci: Concept = c.concepts[i]
                x.append(self.milp.get_variable(ind, ci))
                self.add_assertion(ind, ci, DegreeVariable.get_degree(x[i]))
                exp.add_term(Term(a, x[i]))

            b: float = (wn - w1) / (n - 1)
            for j in range(n - 1):
                for k in range(j + 1, n):
                    min_var: Variable = self.milp.get_new_variable(
                        VariableType.SEMI_CONTINUOUS
                    )
                    ZadehSolver.and_equation(min_var, x[j], x[k], self.milp)
                    exp.add_term(Term(b, min_var))
            degree: DegreeVariable = DegreeVariable.get_degree(
                self.milp.get_variable(ind, c)
            )
            self.milp.add_new_constraint(exp, InequalityType.EQUAL, degree)

    def solve_owa_complemented_assertion(
        self, ind: Individual, curr_concept: OperatorConcept
    ) -> None:
        assert isinstance(curr_concept.get_atom(), (OwaConcept, QowaConcept))

        c: typing.Union[OwaConcept, QowaConcept] = curr_concept.get_atom()
        x_A_in_not_WS: Variable = self.milp.get_variable(ind, c)
        n: int = len(c.concepts)
        x: list[Variable] = []
        terms: list[Term] = []
        for i in range(n):
            ci: Concept = c.concepts[i]
            not_ci: Concept = -ci
            xi: Variable = self.milp.get_variable(ind, ci)
            x_not_i: Variable = self.milp.get_variable(ind, not_ci)
            terms.append(Term(-c.weights[i], xi))
            x.append(self.milp.get_variable(ind, ci))
            self.add_assertion(ind, not_ci, DegreeVariable.get_degree(x_not_i))

        y: list[Variable] = self.milp.get_ordered_permutation(x)
        exp: Expression = Expression(1.0, Term(-1.0, x_A_in_not_WS))
        for j in range(n):
            exp.add_term(Term(-c.weights[j], y[j]))
        self.milp.add_new_constraint(exp, InequalityType.EQUAL)
        self.rule_complemented(ind, curr_concept)

    def solve_sugeno_integral_assertion(
        self, ind: Individual, concept: typing.Union[SugenoIntegral, QsugenoIntegral]
    ) -> None:
        n: int = len(concept.concepts)
        x: list[Variable] = []
        for i in range(n):
            ci: Concept = concept.concepts[i]
            x.append(self.milp.get_variable(ind, ci))
            self.add_assertion(ind, ci, DegreeVariable.get_degree(x[i]))
        z: list[list[Variable]] = [
            [self.milp.get_new_variable(VariableType.BINARY) for _ in range(n)]
            for _ in range(n)
        ]
        y: list[Variable] = self.milp.get_ordered_permutation(x, z)
        ow: list[Variable] = [
            self.milp.get_new_variable(VariableType.SEMI_CONTINUOUS) for _ in range(n)
        ]

        for k in range(n):
            for i in range(n):
                self.milp.add_new_constraint(
                    Expression(
                        -concept.weights[k],
                        Term(concept.weights[k], z[k][i]),
                        Term(1.0, ow[i]),
                    ),
                    InequalityType.GREATER_THAN,
                )
                self.milp.add_new_constraint(
                    Expression(
                        -concept.weights[k], Term(-1.0, z[k][i]), Term(1.0, ow[i])
                    ),
                    InequalityType.LESS_THAN,
                )

        a: list[Variable] = [
            self.milp.get_new_variable(VariableType.SEMI_CONTINUOUS) for _ in range(n)
        ]
        self.milp.add_new_constraint(
            Expression(Term(1.0, a[0]), Term(-1.0, ow[0])), InequalityType.EQUAL
        )

        for m in range(1, n):
            vx: list[Variable] = [ow[m], a[m - 1]]
            LukasiewiczSolver.or_equation(vx, a[m], self.milp)

        c: list[Variable] = [
            self.milp.get_new_variable(VariableType.SEMI_CONTINUOUS) for _ in range(n)
        ]

        if isinstance(concept, QsugenoIntegral):
            for i in range(n):
                LukasiewiczSolver.and_equation(c[i], y[i], a[i], self.milp)
        elif isinstance(concept, SugenoIntegral):
            for i in range(n):
                ZadehSolver.and_equation(c[i], y[i], a[i], self.milp)

        degree: DegreeVariable = DegreeVariable.get_degree(
            self.milp.get_variable(ind, concept)
        )
        b: list[Variable] = [
            self.milp.get_new_variable(VariableType.BINARY) for _ in range(n)
        ]
        for i in range(n):
            self.milp.add_new_constraint(
                Expression(Term(1.0, b[i]), Term(1.0, c[i])),
                InequalityType.GREATER_THAN,
                degree,
            )

        exp: Expression = Expression()
        for i in range(n):
            exp.add_term(Term(1.0, b[i]))
        self.milp.add_new_constraint(exp, InequalityType.EQUAL, n - 1)

    def solve_sugeno_integral_complemented_assertion(
        self, ind: Individual, curr_concept: OperatorConcept
    ) -> None:
        assert isinstance(curr_concept.get_atom(), (SugenoIntegral, QsugenoIntegral))
        concept: typing.Union[SugenoIntegral, QsugenoIntegral] = curr_concept.get_atom()

        n: int = len(concept.concepts)
        x: list[Variable] = []
        for i in range(n):
            ci: Concept = concept.concepts[i]
            not_ci: Concept = -ci
            x.append(self.milp.get_variable(ind, ci))
            x_not_i: Variable = self.milp.get_variable(ind, not_ci)
            self.add_assertion(ind, not_ci, DegreeVariable.get_degree(x_not_i))

        z: list[list[Variable]] = [
            [self.milp.get_new_variable(VariableType.BINARY) for _ in range(n)]
            for _ in range(n)
        ]
        y: list[Variable] = self.milp.get_ordered_permutation(x, z)
        ow: list[Variable] = [
            self.milp.get_new_variable(VariableType.SEMI_CONTINUOUS) for _ in range(n)
        ]

        for k in range(n):
            for i in range(n):
                self.milp.add_new_constraint(
                    Expression(
                        -concept.weights[k],
                        Term(concept.weights[k], z[k][i]),
                        Term(1.0, ow[i]),
                    ),
                    InequalityType.GREATER_THAN,
                )
                self.milp.add_new_constraint(
                    Expression(
                        -concept.weights[k], Term(-1.0, z[k][i]), Term(1.0, ow[i])
                    ),
                    InequalityType.LESS_THAN,
                )

        a: list[Variable] = [
            self.milp.get_new_variable(VariableType.SEMI_CONTINUOUS) for _ in range(n)
        ]
        self.milp.add_new_constraint(
            Expression(Term(1.0, a[0]), Term(-1.0, ow[0])), InequalityType.EQUAL
        )
        for m in range(1, n):
            vx: list[Variable] = [ow[m], a[m - 1]]
            LukasiewiczSolver.or_equation(vx, a[m], self.milp)

        c: list[Variable] = [
            self.milp.get_new_variable(VariableType.SEMI_CONTINUOUS) for _ in range(n)
        ]

        if isinstance(concept, QsugenoIntegral):
            for i in range(n):
                LukasiewiczSolver.and_equation(c[i], y[i], a[i], self.milp)
        elif isinstance(concept, SugenoIntegral):
            for i in range(n):
                ZadehSolver.and_equation(c[i], y[i], a[i], self.milp)

        degree: DegreeVariable = DegreeVariable.get_degree(
            self.milp.get_variable(ind, curr_concept)
        )
        b: list[Variable] = [
            self.milp.get_new_variable(VariableType.BINARY) for _ in range(n)
        ]
        for i in range(n):
            self.milp.add_new_constraint(
                Expression(Term(1.0, b[i]), Term(1.0, c[i])),
                InequalityType.GREATER_THAN,
                degree,
            )

        exp: Expression = Expression()
        for i in range(n):
            exp.add_term(Term(1.0, b[i]))
        self.milp.add_new_constraint(exp, InequalityType.EQUAL, n - 1)
        self.rule_complemented(ind, curr_concept)

    def solve_w_max_assertion(
        self, ind: Individual, concept: WeightedMaxConcept
    ) -> None:
        x_A_in_WS: Variable = self.milp.get_variable(ind, concept)
        min_vars: list[Variable] = []
        for ci, weight in zip(concept.concepts, concept.weights):
            xi: Variable = self.milp.get_variable(ind, ci)
            self.add_assertion(ind, ci, DegreeVariable.get_degree(xi))
            min_var: Variable = self.milp.get_new_variable(VariableType.SEMI_CONTINUOUS)
            ZadehSolver.and_equation(min_var, xi, weight, self.milp)
            min_vars.append(min_var)
        ZadehSolver.or_equation(min_vars, x_A_in_WS, self.milp)

    def solve_w_max_complemented_assertion(
        self, ind: Individual, curr_concept: OperatorConcept
    ) -> None:
        assert isinstance(curr_concept.get_atom(), WeightedMaxConcept)
        concept: WeightedMaxConcept = curr_concept.get_atom()

        x_A_in_WS: Variable = self.milp.get_variable(ind, curr_concept)
        negmin: list[Variable] = []
        for ci, weight in zip(concept.concepts, concept.weights):
            not_ci: Concept = -ci
            xi: Variable = self.milp.get_variable(ind, ci)
            x_not_i: Variable = self.milp.get_variable(ind, not_ci)
            self.add_assertion(ind, not_ci, DegreeVariable.get_degree(x_not_i))
            max_var: Variable = self.milp.get_new_variable(VariableType.SEMI_CONTINUOUS)
            ZadehSolver.or_negated_equation(max_var, xi, 1.0 - weight, self.milp)
            negmin.append(max_var)
        ZadehSolver.and_equation(negmin, x_A_in_WS, self.milp)
        self.rule_complemented(ind, curr_concept)

    def solve_w_min_assertion(
        self, ind: Individual, concept: WeightedMinConcept
    ) -> None:
        x_A_in_WS: Variable = self.milp.get_variable(ind, concept)
        max_vars: list[Variable] = []
        for ci, weight in zip(concept.concepts, concept.weights):
            xi: Variable = self.milp.get_variable(ind, ci)
            self.add_assertion(ind, ci, DegreeVariable.get_degree(xi))
            max_var: Variable = self.milp.get_new_variable(VariableType.SEMI_CONTINUOUS)
            ZadehSolver.or_equation(max_var, xi, 1.0 - weight, self.milp)
            max_vars.append(max_var)
        ZadehSolver.and_equation(max_vars, x_A_in_WS, self.milp)

    def solve_w_min_complemented_assertion(
        self, ind: Individual, curr_concept: OperatorConcept
    ) -> None:
        assert isinstance(curr_concept.get_atom(), WeightedMinConcept)
        concept: WeightedMinConcept = curr_concept.get_atom()

        x_A_in_WS: Variable = self.milp.get_variable(ind, curr_concept)
        negmax: list[Variable] = []
        for ci, weight in zip(concept.concepts, concept.weights):
            not_ci: Concept = -ci
            xi: Variable = self.milp.get_variable(ind, ci)
            x_not_i: Variable = self.milp.get_variable(ind, not_ci)
            self.add_assertion(ind, not_ci, DegreeVariable.get_degree(x_not_i))
            max_var: Variable = self.milp.get_new_variable(VariableType.SEMI_CONTINUOUS)
            ZadehSolver.and_negated_equation(max_var, xi, weight, self.milp)
            negmax.append(max_var)
        ZadehSolver.or_equation(negmax, x_A_in_WS, self.milp)
        self.rule_complemented(ind, curr_concept)

    def solve_w_sum_assertion(
        self, ind: Individual, concept: WeightedSumConcept
    ) -> None:
        x_A_in_WS: Variable = self.milp.get_variable(ind, concept)
        terms: list[Term] = []
        for ci, weight in zip(concept.concepts, concept.weights):
            xi: Variable = self.milp.get_variable(ind, ci)
            terms.append(Term(weight, xi))
            self.add_assertion(ind, ci, DegreeVariable.get_degree(xi))
        self.milp.add_new_constraint(
            Expression(*terms),
            InequalityType.EQUAL,
            DegreeVariable.get_degree(x_A_in_WS),
        )

    def solve_w_sum_complemented_assertion(
        self, ind: Individual, curr_concept: OperatorConcept
    ) -> None:
        assert isinstance(curr_concept.get_atom(), WeightedSumConcept)
        concept: WeightedSumConcept = curr_concept.get_atom()

        x_A_in_not_WS: Variable = self.milp.get_variable(ind, curr_concept)
        terms: list[Term] = []
        for ci, weight in zip(concept.concepts, concept.weights):
            not_ci: Concept = -ci
            xi: Variable = self.milp.get_variable(ind, ci)
            x_not_i: Variable = self.milp.get_variable(ind, not_ci)
            terms.append(Term(-weight, xi))
            self.add_assertion(ind, not_ci, DegreeVariable.get_degree(x_not_i))
        self.milp.add_new_constraint(
            Expression(1.0, *terms),
            InequalityType.EQUAL,
            DegreeVariable.get_degree(x_A_in_not_WS),
        )
        self.rule_complemented(ind, curr_concept)

    def solve_w_sum_zero_assertion(
        self, ind: Individual, concept: WeightedSumZeroConcept
    ) -> None:
        terms: list[Term] = []
        vx: list[Variable] = []
        x_A_in_ws: Variable = self.milp.get_variable(ind, concept)
        y: Variable = self.milp.get_new_variable(VariableType.BINARY)
        z: Variable = self.milp.get_new_variable(VariableType.SEMI_CONTINUOUS)
        for ci, weight in zip(concept.concepts, concept.weights):
            xi: Variable = self.milp.get_variable(ind, ci)
            self.add_assertion(ind, ci, DegreeVariable.get_degree(xi))
            self.milp.add_new_constraint(
                Expression(Term(1.0, z), Term(-1.0, xi)), InequalityType.LESS_THAN
            )
            vx.append(xi)
            terms.append(Term(weight, xi))
        terms.append(Term(-1.0, x_A_in_ws))
        ZadehSolver.and_equation(vx, z, self.milp)
        ZadehSolver.goedel_not_equation(y, z, self.milp)
        self.milp.add_new_constraint(
            Expression(-1.0, Term(1.0, y), Term(1.0, x_A_in_ws)),
            InequalityType.LESS_THAN,
        )
        exp1: Expression = Expression(*terms)
        exp1.add_term(Term(-1.0, y))
        self.milp.add_new_constraint(exp1, InequalityType.LESS_THAN)
        exp2: Expression = Expression(*terms)
        exp2.add_term(Term(1.0, y))
        self.milp.add_new_constraint(exp2, InequalityType.GREATER_THAN)
        self.rule_complemented(ind, concept)

    def solve_w_sum_zero_complemented_assertion(
        self, ind: Individual, curr_concept: OperatorConcept
    ) -> None:
        assert isinstance(curr_concept.get_atom(), WeightedSumZeroConcept)
        concept: WeightedSumZeroConcept = curr_concept.get_atom()

        terms: list[Term] = []
        vx: list[Variable] = []
        x_A_in_not_ws: Variable = self.milp.get_variable(ind, curr_concept)
        y: Variable = self.milp.get_new_variable(VariableType.BINARY)
        z: Variable = self.milp.get_new_variable(VariableType.SEMI_CONTINUOUS)
        for ci, weight in zip(concept.concepts, concept.weights):
            not_ci: Concept = -ci
            xi: Variable = self.milp.get_variable(ind, ci)
            x_not_i: Variable = self.milp.get_variable(ind, not_ci)
            self.add_assertion(ind, not_ci, DegreeVariable.get_degree(x_not_i))
            vx.append(xi)
            terms.append(Term(-weight, xi))
        terms.append(Term(-1.0, x_A_in_not_ws))
        ZadehSolver.and_equation(vx, z, self.milp)
        ZadehSolver.goedel_not_equation(y, z, self.milp)
        self.milp.add_new_constraint(
            Expression(Term(-1.0, y), Term(1.0, x_A_in_not_ws)),
            InequalityType.GREATER_THAN,
        )
        exp1: Expression = Expression(*terms)
        exp1.add_term(Term(-1.0, y))
        self.milp.add_new_constraint(exp1, InequalityType.LESS_THAN)
        exp2: Expression = Expression(*terms)
        exp2.add_term(Term(1.0, y))
        self.milp.add_new_constraint(exp2, InequalityType.GREATER_THAN)
        self.rule_complemented(ind, curr_concept)

    def solve_crisp_concrete_concept_assertion(
        self, ind: Individual, concept: CrispConcreteConcept
    ) -> None:
        """
        This function define the equations for the individual belonging to the crisp set.

        Args:
            ind (Individual): current individual

            Variables:
                - x     => variable associated with the individual
                - x'    => generic variable associated with an individual belonging to this crisp concept

            Draw the four lines:
                - (b, 1) -- (k_2, 0) -> y_2 <= (x - k_2) / (k_2 - b)
                - (a, 1) -- (k_2, 0) -> y_1 <= (x - k_2) / (k_2 - a)
                - (b, 1) -- (k_1, 0) -> y_3 >= (x - k_1) / (k_1 - b)
                - (a, 1) -- (k_1, 0) -> y_2 >= (x - k_1) / (k_1 - a)

            Along with the following constraints:
                - y_1 + y_2 + y_3 = 1
                - x' + y_1 + y_3 <= 1
                - x' - y_2 >= 0
        """
        x_c: Variable = self.milp.get_variable(ind)
        x_ass: Variable = self.milp.get_variable(ind, concept)
        y1: Variable = self.milp.get_new_variable(VariableType.BINARY)
        y2: Variable = self.milp.get_new_variable(VariableType.BINARY)
        y3: Variable = self.milp.get_new_variable(VariableType.BINARY)

        self.milp.add_new_constraint(
            Expression(Term(1.0, y1), Term(1.0, y2), Term(1.0, y3)),
            InequalityType.EQUAL,
            1.0,
        )
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_c), Term(concept.k1 - concept.a, y2)),
            InequalityType.GREATER_THAN,
            concept.k1,
        )
        self.milp.add_new_constraint(
            Expression(
                Term(1.0, x_c), Term(concept.k1 - concept.b - ConfigReader.EPSILON, y3)
            ),
            InequalityType.GREATER_THAN,
            concept.k1,
        )
        self.milp.add_new_constraint(
            Expression(
                Term(1.0, x_c), Term(concept.k2 - concept.a + ConfigReader.EPSILON, y1)
            ),
            InequalityType.LESS_THAN,
            concept.k2,
        )
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_c), Term(concept.k2 - concept.b, y2)),
            InequalityType.LESS_THAN,
            concept.k2,
        )
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_ass), Term(1.0, y1), Term(1.0, y3)),
            InequalityType.LESS_THAN,
            1.0,
        )
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_ass), Term(-1.0, y2)), InequalityType.GREATER_THAN
        )

    def solve_fuzzy_concrete_concept_complement_assertion(
        self,
        ind: CreatedIndividual,
        lower_limit: Degree,
        curr_concept: OperatorConcept,
    ) -> None:
        """Solve a complement assertion"""
        assert isinstance(curr_concept.get_atom(), FuzzyConcreteConcept)
        assertion: Assertion = Assertion(ind, curr_concept, lower_limit)
        self.rule_complemented_complex_assertion(assertion)

    def solve_left_concrete_concept_assertion(
        self, ind: CreatedIndividual, concept: LeftConcreteConcept
    ) -> None:
        x_c: Variable = self.milp.get_variable(ind)
        x_ass: Variable = self.milp.get_variable(ind, concept)
        y1: Variable = self.milp.get_new_variable(VariableType.BINARY)
        y2: Variable = self.milp.get_new_variable(VariableType.BINARY)
        y3: Variable = self.milp.get_new_variable(VariableType.BINARY)
        self.milp.add_new_constraint(
            Expression(Term(1.0, y1), Term(1.0, y2), Term(1.0, y3)),
            InequalityType.EQUAL,
            1.0,
        )
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_c), Term(concept.k1 - concept.a, y2)),
            InequalityType.GREATER_THAN,
            concept.k1,
        )
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_c), Term(concept.k1 - concept.b, y3)),
            InequalityType.GREATER_THAN,
            concept.k1,
        )
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_c), Term(concept.k2 - concept.a, y1)),
            InequalityType.LESS_THAN,
            concept.k2,
        )
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_c), Term(concept.k2 - concept.b, y2)),
            InequalityType.LESS_THAN,
            concept.k2,
        )
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_ass), Term(1.0, y3)), InequalityType.LESS_THAN, 1.0
        )
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_ass), Term(-1.0, y1)), InequalityType.GREATER_THAN
        )
        self.milp.add_new_constraint(
            Expression(
                Term(1.0, x_c),
                Term(concept.b - concept.a, x_ass),
                Term(concept.k2 - concept.a, y2),
            ),
            InequalityType.LESS_THAN,
            concept.k2 + concept.b - concept.a,
        )
        self.milp.add_new_constraint(
            Expression(
                Term(1.0, x_c),
                Term(concept.b - concept.a, x_ass),
                Term(concept.k1 - concept.b, y2),
            ),
            InequalityType.GREATER_THAN,
            concept.k1,
        )

    def solve_linear_concrete_concept_assertion(
        self, ind: CreatedIndividual, concept: LinearConcreteConcept
    ) -> None:
        x_A_is_C: Variable = self.milp.get_variable(ind)
        x_ass: Variable = self.milp.get_variable(ind, concept)
        y: Variable = self.milp.get_variable(VariableType.BINARY)
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_A_is_C), Term(concept.a - concept.k2, y)),
            InequalityType.LESS_THAN,
            concept.a,
        )
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_A_is_C), Term(concept.k1 - concept.a, y)),
            InequalityType.GREATER_THAN,
            concept.k1,
        )
        self.milp.add_new_constraint(
            Expression(
                Term(concept.k1 - concept.a, x_ass),
                Term(concept.a - concept.k1, y),
                Term(concept.b, x_A_is_C),
            ),
            InequalityType.GREATER_THAN,
            concept.b * concept.k1,
        )
        self.milp.add_new_constraint(
            Expression(
                Term(concept.k1 - concept.a, x_ass),
                Term(concept.b * (concept.k1 - concept.k2), y),
                Term(concept.b, x_A_is_C),
            ),
            InequalityType.LESS_THAN,
            concept.b * concept.k1,
        )
        self.milp.add_new_constraint(
            Expression(
                Term(concept.a - concept.k2, x_ass),
                Term((1.0 - concept.b) * (concept.k1 - concept.k2), y),
                Term(1.0 - concept.b, x_A_is_C),
            ),
            InequalityType.GREATER_THAN,
            concept.a - concept.k2 - concept.k1 * concept.b + concept.k1,
        )
        self.milp.add_new_constraint(
            Expression(
                Term(concept.a - concept.k2, x_ass),
                Term(concept.k2 - concept.a, y),
                Term(1.0 - concept.b, x_A_is_C),
            ),
            InequalityType.LESS_THAN,
            concept.k2 - concept.b * concept.k2,
        )

    def solve_right_concrete_concept_assertion(
        self, ind: CreatedIndividual, concept: RightConcreteConcept
    ) -> None:
        x_c: Variable = self.milp.get_variable(ind)
        x_ass: Variable = self.milp.get_variable(ind, concept)
        y1: Variable = self.milp.get_new_variable(VariableType.BINARY)
        y2: Variable = self.milp.get_new_variable(VariableType.BINARY)
        y3: Variable = self.milp.get_new_variable(VariableType.BINARY)

        self.milp.add_new_constraint(
            Expression(Term(1.0, y1), Term(1.0, y2), Term(1.0, y3)),
            InequalityType.EQUAL,
            1.0,
        )
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_c), Term(concept.k1 - concept.a, y2)),
            InequalityType.GREATER_THAN,
            concept.k1,
        )
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_c), Term(concept.k1 - concept.b, y3)),
            InequalityType.GREATER_THAN,
            concept.k1,
        )
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_c), Term(concept.k2 - concept.a, y1)),
            InequalityType.LESS_THAN,
            concept.k2,
        )
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_c), Term(concept.k2 - concept.b, y2)),
            InequalityType.LESS_THAN,
            concept.k2,
        )
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_ass), Term(1.0, y1)), InequalityType.LESS_THAN, 1.0
        )
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_ass), Term(-1.0, y3)), InequalityType.GREATER_THAN
        )
        self.milp.add_new_constraint(
            Expression(
                Term(1.0, x_c),
                Term(concept.a - concept.b, x_ass),
                Term(concept.k2 - concept.a, y2),
            ),
            InequalityType.LESS_THAN,
            concept.k2,
        )
        self.milp.add_new_constraint(
            Expression(
                Term(1.0, x_c),
                Term(concept.a - concept.b, x_ass),
                Term(concept.k1 - concept.b, y2),
            ),
            InequalityType.GREATER_THAN,
            concept.k1 + concept.a - concept.b,
        )

    def solve_trapezoidal_concrete_concept_assertion(
        self, ind: CreatedIndividual, concept: TrapezoidalConcreteConcept
    ) -> None:
        x_c: Variable = self.milp.get_variable(ind)
        x_ass: Variable = self.milp.get_variable(typing.cast(Individual, ind), concept)
        y1: Variable = self.milp.get_new_variable(VariableType.BINARY)
        y2: Variable = self.milp.get_new_variable(VariableType.BINARY)
        y3: Variable = self.milp.get_new_variable(VariableType.BINARY)
        y4: Variable = self.milp.get_new_variable(VariableType.BINARY)
        y5: Variable = self.milp.get_new_variable(VariableType.BINARY)

        self.milp.add_new_constraint(
            Expression(
                Term(1.0, y1),
                Term(1.0, y2),
                Term(1.0, y3),
                Term(1.0, y4),
                Term(1.0, y5),
            ),
            InequalityType.EQUAL,
            1.0,
        )

        self.milp.add_new_constraint(
            Expression(Term(1.0, x_c), Term(concept.k1 - concept.a, y2)),
            InequalityType.GREATER_THAN,
            concept.k1,
        )
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_c), Term(concept.k1 - concept.b, y3)),
            InequalityType.GREATER_THAN,
            concept.k1,
        )
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_c), Term(concept.k1 - concept.c, y4)),
            InequalityType.GREATER_THAN,
            concept.k1,
        )
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_c), Term(concept.k1 - concept.d, y5)),
            InequalityType.GREATER_THAN,
            concept.k1,
        )
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_c), Term(concept.k2 - concept.a, y1)),
            InequalityType.LESS_THAN,
            concept.k2,
        )
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_c), Term(concept.k2 - concept.b, y2)),
            InequalityType.LESS_THAN,
            concept.k2,
        )
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_c), Term(concept.k2 - concept.c, y3)),
            InequalityType.LESS_THAN,
            concept.k2,
        )
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_c), Term(concept.k2 - concept.d, y4)),
            InequalityType.LESS_THAN,
            concept.k2,
        )

        self.milp.add_new_constraint(
            Expression(Term(1.0, x_ass), Term(1.0, y1), Term(1.0, y5)),
            InequalityType.LESS_THAN,
            1.0,
        )
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_ass), Term(-1.0, y3)), InequalityType.GREATER_THAN
        )

        self.milp.add_new_constraint(
            Expression(
                Term(1.0, x_c),
                Term(concept.a - concept.b, x_ass),
                Term(concept.k2 - concept.a, y2),
            ),
            InequalityType.LESS_THAN,
            concept.k2,
        )
        self.milp.add_new_constraint(
            Expression(
                Term(1.0, x_c),
                Term(concept.a - concept.b, x_ass),
                Term(concept.k1 - concept.b, y2),
            ),
            InequalityType.GREATER_THAN,
            concept.k1 + concept.a - concept.b,
        )
        self.milp.add_new_constraint(
            Expression(
                Term(1.0, x_c),
                Term(concept.d - concept.c, x_ass),
                Term(concept.k2 - concept.c, y4),
            ),
            InequalityType.LESS_THAN,
            concept.k2 + concept.d - concept.c,
        )
        self.milp.add_new_constraint(
            Expression(
                Term(1.0, x_c),
                Term(concept.d - concept.c, x_ass),
                Term(concept.k1 - concept.d, y4),
            ),
            InequalityType.GREATER_THAN,
            concept.k1,
        )

    def solve_triangular_concrete_concept_assertion(
        self, individual: CreatedIndividual, concept: TriangularConcreteConcept
    ) -> None:
        x_c: Variable = self.milp.get_variable(individual)
        x_ass: Variable = self.milp.get_variable(
            typing.cast(Individual, individual), concept
        )
        y1: Variable = self.milp.get_new_variable(VariableType.BINARY)
        y2: Variable = self.milp.get_new_variable(VariableType.BINARY)
        y3: Variable = self.milp.get_new_variable(VariableType.BINARY)
        y4: Variable = self.milp.get_new_variable(VariableType.BINARY)

        self.milp.add_new_constraint(
            Expression(Term(1.0, y1), Term(1.0, y2), Term(1.0, y3), Term(1.0, y4)),
            InequalityType.EQUAL,
            1.0,
        )
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_c), Term(concept.k1 - concept.a, y2)),
            InequalityType.GREATER_THAN,
            concept.k1,
        )
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_c), Term(concept.k1 - concept.b, y3)),
            InequalityType.GREATER_THAN,
            concept.k1,
        )
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_c), Term(concept.k1 - concept.c, y4)),
            InequalityType.GREATER_THAN,
            concept.k1,
        )
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_c), Term(concept.k2 - concept.a, y1)),
            InequalityType.LESS_THAN,
            concept.k2,
        )
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_c), Term(concept.k2 - concept.b, y2)),
            InequalityType.LESS_THAN,
            concept.k2,
        )
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_c), Term(concept.k2 - concept.c, y3)),
            InequalityType.LESS_THAN,
            concept.k2,
        )
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_ass), Term(1.0, y1), Term(1.0, y4)),
            InequalityType.LESS_THAN,
            1.0,
        )
        self.milp.add_new_constraint(
            Expression(
                Term(1.0, x_c),
                Term(concept.a - concept.b, x_ass),
                Term(concept.k2 - concept.a, y2),
            ),
            InequalityType.LESS_THAN,
            concept.k2,
        )
        self.milp.add_new_constraint(
            Expression(
                Term(1.0, x_c),
                Term(concept.a - concept.b, x_ass),
                Term(concept.k1 - concept.b, y2),
            ),
            InequalityType.GREATER_THAN,
            concept.k1 + concept.a - concept.b,
        )
        self.milp.add_new_constraint(
            Expression(
                Term(1.0, x_c),
                Term(concept.c - concept.b, x_ass),
                Term(concept.k2 - concept.b, y3),
            ),
            InequalityType.LESS_THAN,
            concept.k2 + concept.c - concept.b,
        )
        self.milp.add_new_constraint(
            Expression(
                Term(1.0, x_c),
                Term(concept.c - concept.b, x_ass),
                Term(concept.k1 - concept.c, y3),
            ),
            InequalityType.GREATER_THAN,
            concept.k1,
        )

    def solve_modifier_complemented_assertion(
        self, ind: Individual, concept: OperatorConcept, degree: Degree
    ) -> None:
        assert isinstance(concept, OperatorConcept) and isinstance(
            concept.get_atom(), (ModifiedConcept, ModifiedConcreteConcept)
        )
        ass: Assertion = Assertion(ind, concept, degree)
        self.rule_complemented_complex_assertion(ass)

    def solve_linear_modifier_assertion(
        self, ind: Individual, con: Concept, modifier: LinearModifier
    ) -> None:
        if isinstance(con, ModifiedConcreteConcept):
            modified: FuzzyConcreteConcept = typing.cast(
                ModifiedConcreteConcept, con
            ).modified

            x_A_is_C: Variable = self.milp.get_variable(ind, modified)
            self.add_assertion(ind, modified, DegreeVariable.get_degree(x_A_is_C))
            x_A_is_mod_C: Variable = self.milp.get_variable(ind, con)
        else:
            x_A_is_C: Variable = self.milp.get_variable(ind, con)
            self.add_assertion(ind, con, DegreeVariable.get_degree(x_A_is_C))
            modified: TriangularlyModifiedConcept = TriangularlyModifiedConcept(
                con, modifier
            )
            x_A_is_mod_C: Variable = self.milp.get_variable(ind, modified)

        y: Variable = self.milp.get_new_variable(VariableType.BINARY)
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_A_is_C), Term(-1.0, y)),
            InequalityType.LESS_THAN,
            modifier.a,
        )
        self.milp.add_new_constraint(
            Expression(
                Term(-modifier.a / modifier.b, x_A_is_mod_C),
                Term(1.0, x_A_is_C),
                Term(modifier.a / modifier.b, y),
            ),
            InequalityType.GREATER_THAN,
        )
        self.milp.add_new_constraint(
            Expression(
                Term(-modifier.a / modifier.b, x_A_is_mod_C),
                Term(1.0, x_A_is_C),
                Term(-1.0, y),
            ),
            InequalityType.LESS_THAN,
        )
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_A_is_C), Term(-modifier.a, y)),
            InequalityType.GREATER_THAN,
        )
        self.milp.add_new_constraint(
            Expression(
                Term(modifier.a - 1.0, x_A_is_mod_C),
                Term(1.0 - modifier.b, x_A_is_C),
                Term(modifier.b - modifier.a + 2.0, y),
            ),
            InequalityType.LESS_THAN,
            2.0,
        )
        self.milp.add_new_constraint(
            Expression(
                Term(modifier.a - 1.0, x_A_is_mod_C),
                Term(1.0 - modifier.b, x_A_is_C),
                Term(modifier.b - modifier.a - 2.0, y),
            ),
            InequalityType.GREATER_THAN,
            -2.0,
        )

    def solve_triangular_modifier_assertion(
        self,
        individual: Individual,
        concept: Concept,
        modifier: TriangularModifier,
    ) -> None:
        if isinstance(concept, ModifiedConcreteConcept):
            modified: FuzzyConcreteConcept = concept.modified
            x_A_is_C: Variable = self.milp.get_variable(individual, modified)
            self.add_assertion(
                individual, modified, DegreeVariable.get_degree(x_A_is_C)
            )
            x_A_is_mod_C: Variable = self.milp.get_variable(individual, concept)
        else:
            modified: TriangularlyModifiedConcept = TriangularlyModifiedConcept(
                concept, modifier
            )
            x_A_is_C: Variable = self.milp.get_variable(individual, concept)
            self.add_assertion(individual, concept, DegreeVariable.get_degree(x_A_is_C))
            x_A_is_mod_C: Variable = self.milp.get_variable(individual, modified)

        y1: Variable = self.milp.get_new_variable(VariableType.BINARY)
        y2: Variable = self.milp.get_new_variable(VariableType.BINARY)
        y3: Variable = self.milp.get_new_variable(VariableType.BINARY)
        y4: Variable = self.milp.get_new_variable(VariableType.BINARY)

        self.milp.add_new_constraint(
            Expression(Term(1.0, y1), Term(1.0, y2), Term(1.0, y3), Term(1.0, y4)),
            InequalityType.EQUAL,
            1.0,
        )
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_A_is_C), Term(-modifier.a, y2)),
            InequalityType.GREATER_THAN,
        )
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_A_is_C), Term(-modifier.b, y3)),
            InequalityType.GREATER_THAN,
        )
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_A_is_C), Term(-modifier.c, y4)),
            InequalityType.GREATER_THAN,
        )
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_A_is_C), Term(1.0 - modifier.a, y1)),
            InequalityType.LESS_THAN,
            1.0,
        )
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_A_is_C), Term(1.0 - modifier.b, y2)),
            InequalityType.LESS_THAN,
            1.0,
        )
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_A_is_C), Term(1.0 - modifier.c, y3)),
            InequalityType.LESS_THAN,
            1.0,
        )
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_A_is_mod_C), Term(1.0, y1), Term(1.0, y4)),
            InequalityType.LESS_THAN,
            1.0,
        )
        self.milp.add_new_constraint(
            Expression(
                Term(1.0, x_A_is_C),
                Term(modifier.a - modifier.b, x_A_is_mod_C),
                Term(1.0 - modifier.a, y2),
            ),
            InequalityType.LESS_THAN,
            1.0,
        )
        self.milp.add_new_constraint(
            Expression(
                Term(1.0, x_A_is_C),
                Term(modifier.a - modifier.b, x_A_is_mod_C),
                Term(-modifier.b, y2),
            ),
            InequalityType.GREATER_THAN,
            modifier.a - modifier.b,
        )
        self.milp.add_new_constraint(
            Expression(
                Term(1.0, x_A_is_C),
                Term(modifier.c - modifier.b, x_A_is_mod_C),
                Term(1.0 - modifier.b, y3),
            ),
            InequalityType.LESS_THAN,
            1.0 + modifier.c - modifier.b,
        )
        self.milp.add_new_constraint(
            Expression(
                Term(1.0, x_A_is_C),
                Term(modifier.c - modifier.b, x_A_is_mod_C),
                Term(-modifier.c, y3),
            ),
            InequalityType.GREATER_THAN,
        )

    def add_negated_datatype_restriction(self, ass: Assertion) -> None:
        a: Individual = ass.get_individual()
        op: Concept = ass.get_concept()
        assert isinstance(op, OperatorConcept) and op.type == ConceptType.COMPLEMENT
        c: Concept = op.get_atom()
        assert isinstance(c, HasRoleInterface)
        f_name: str = c.role
        a.add_concrete_restriction(f_name, ass)

    def rule_n2(self) -> None:
        for o in self.individuals.values():
            o_name: str = str(o)
            vars: set[Variable] = set()
            if not isinstance(o, CreatedIndividual) and len(o.get_nominal_list()) != 0:
                x_O_is_O: Variable = self.milp.get_nominal_variable(o_name, o_name)
                vars.add(x_O_is_O)
            for b_name in o.get_nominal_list():
                x_O_is_B: Variable = self.milp.get_nominal_variable(o_name, b_name)
                vars.add(x_O_is_B)
            if len(vars) >= 2:
                sum_vars: Expression = Expression(vars)
                self.milp.add_new_constraint(
                    Expression.add_constant(sum_vars, -1.0), InequalityType.LESS_THAN
                )
                Util.debug(f"Rule_n2: {sum_vars} <= 1")

    def rule_n3(self) -> None:
        for o_name, nodes in self.labels_with_nodes.items():
            if nodes is not None and len(nodes) > 1:
                v: list[Variable] = [
                    self.milp.get_nominal_variable(node, o_name) for node in nodes
                ]
                exp: Expression = Expression(v)
                exp.set_constant(-1.0)
                self.milp.add_new_constraint(exp, InequalityType.EQUAL)
                Util.debug(f"Rule_n3: {exp}")

    def rule_ass_nom(self, a: Individual, c: Concept, v: str) -> None:
        a_name = str(a)
        i: Individual = self.get_individual(v)
        a_is_c: Variable = self.milp.get_variable(a, c)
        v_is_a: Variable = self.milp.get_nominal_variable(v, a_name)
        v_is_c: Variable = self.milp.get_variable(i, c)
        self.add_assertion(i, c, DegreeVariable.get_degree(v_is_c))
        Util.debug(f"Adding equation {v_is_a} => {v_is_c} >= {a_is_c}")
        ZadehSolver.zadeh_implies_leq_equation(a_is_c, v_is_a, v_is_c, self.milp)

    def exists_primite_concept_definition(
        self, pcds: set[PrimitiveConceptDefinition], pcd: PrimitiveConceptDefinition
    ) -> bool:
        c: Concept = pcd.get_definition()
        for p in pcds:
            if p.get_definition() != c:
                continue
            old_degree: float = p.get_degree()
            new_degree: float = pcd.get_degree()
            if new_degree > old_degree:
                pcd.set_degree(new_degree)
            return True
        return False

    def add_axiom_to_inc(self, a: str, pcd: PrimitiveConceptDefinition) -> None:
        c: Concept = pcd.get_definition()
        pcd_type: LogicOperatorType = pcd.get_type()
        n: float = pcd.get_degree()
        if self.is_redundant_A_is_a_C(a, c, pcd_type, n):
            return
        pcds: set[PrimitiveConceptDefinition] = self.t_inclusions.get(a)
        if pcds is not None and self.exists_primite_concept_definition(pcds, pcd):
            return
        self.t_inclusions[a] = self.t_inclusions.get(a, set()) | set([pcd])

    def add_axiom_to_do_A_is_a_X(self, a: str, pcd: PrimitiveConceptDefinition) -> None:
        c: Concept = pcd.get_definition()
        pcd_type: LogicOperatorType = pcd.get_type()
        n: float = pcd.get_degree()
        if self.is_redundant_A_is_a_C(a, c, pcd_type, n):
            return
        if c.is_atomic():
            pcds: set[PrimitiveConceptDefinition] = self.axioms_to_do_A_is_a_B.get(a)
        else:
            pcds: set[PrimitiveConceptDefinition] = self.axioms_to_do_A_is_a_C.get(a)
        if pcds is not None and self.exists_primite_concept_definition(pcds, pcd):
            return
        if c.is_atomic():
            self.axioms_to_do_A_is_a_B[a] = self.axioms_to_do_A_is_a_B.get(
                a, set()
            ) | set([pcd])
        else:
            self.axioms_to_do_A_is_a_C[a] = self.axioms_to_do_A_is_a_C.get(
                a, set()
            ) | set([pcd])

    def add_axiom_to_A_is_a_C(
        self,
        a: str,
        pcd: PrimitiveConceptDefinition,
        pcd_dict: dict[str, set[PrimitiveConceptDefinition]],
    ) -> None:
        c: Concept = pcd.get_definition()
        pcd_type: LogicOperatorType = pcd.get_type()
        n: float = pcd.get_degree()
        if self.is_redundant_A_is_a_C(a, c, pcd_type, n):
            return
        pcds: set[PrimitiveConceptDefinition] = pcd_dict.get(a)
        if pcds is not None and self.exists_primite_concept_definition(pcds, pcd):
            return
        pcd_dict[a] = pcd_dict.get(a, set()) | set([pcd])

    def add_axiom_to_A_equiv_C(self, a: str, conc: Concept) -> None:
        hs: set[Concept] = self.axioms_A_equiv_C.get(a, set())
        for c in hs:
            if c == conc:
                return
        if conc not in hs:
            self.axioms_A_equiv_C[a] = hs | set([conc])

    def add_axioms_to_tg(self) -> None:
        for cname in self.axioms_A_equiv_C:
            a: Concept = AtomicConcept(cname)
            for b in self.axioms_A_equiv_C.get(cname):
                self.define_equivalent_concepts(a, b)
        for ce in self.axioms_C_equiv_D:
            a: Concept = ce.get_c1()
            b: Concept = ce.get_c2()
            self.define_equivalent_concepts(a, b)
        self.axioms_A_equiv_C.clear()
        self.axioms_C_equiv_D.clear()

    def disjoint_with_defined_concept(self, a: str) -> bool:
        for b in self.t_disjoints.get(a, set()):
            if b in self.t_definitions:
                return False
        return True

    def definition_absorption(self, gci: GeneralConceptInclusion) -> bool:
        a: str = str(gci.get_subsumer())
        aux: str = str(gci.get_subsumed())
        implication: LogicOperatorType = gci.get_type()
        d: Degree = gci.get_degree()
        n: float = typing.cast(DegreeNumeric, d).get_numerical_value()
        if constants.KNOWLEDGE_BASE_SEMANTICS != FuzzyLogic.CLASSICAL and (
            n != 1.0 or implication == LogicOperatorType.ZADEH
        ):
            return False
        if self.axioms_A_is_a_C.get(a) is not None:
            for pcd in self.axioms_A_is_a_C.get(a):
                conc: Concept = pcd.get_definition()
                if (
                    gci.get_subsumed() != conc
                    or str(gci.get_subsumer()) != a
                    or constants.KNOWLEDGE_BASE_SEMANTICS != FuzzyLogic.CLASSICAL
                    and (
                        not d.is_numeric()
                        or n != 1.0
                        or implication == LogicOperatorType.KLEENE_DIENES
                    )
                    or a in self.t_definitions
                    or a in self.t_inclusions
                    or self.disjoint_with_defined_concept(a)
                ):
                    continue
                self.t_definitions[a] = conc
                self.remove_A_is_a_X(a, pcd, False)
                self.remove_C_is_a_A(aux, gci)
                Util.debug(f"Definition Absorbed: {a} = {conc}")
                return True
        if self.t_inclusions.get(a) is not None:
            for pcd in self.t_inclusions.get(a, set()):
                conc: Concept = pcd.get_definition()
                if (
                    gci.get_subsumed() != conc
                    or str(gci.get_subsumer()) != a
                    or constants.KNOWLEDGE_BASE_SEMANTICS != FuzzyLogic.CLASSICAL
                    and (
                        not d.is_numeric()
                        or n != 1.0
                        or implication == LogicOperatorType.KLEENE_DIENES
                    )
                    or a in self.t_definitions
                    or len(self.t_inclusions.get(a, set())) > 1
                ):
                    continue
                self.t_definitions[a] = conc
                self.remove_A_is_a_X(a, pcd, self.t_inclusions)
                self.remove_C_is_a_A(aux, gci)
                Util.debug(f"Definition Absorbed: {a} = {conc}")
                return True
        return False

    def definition_absorption_to_do(self, pcd: PrimitiveConceptDefinition) -> bool:
        a: str = pcd.get_defined_concept()
        implication: LogicOperatorType = pcd.get_type()
        n: float = pcd.get_degree()
        if constants.KNOWLEDGE_BASE_SEMANTICS != FuzzyLogic.CLASSICAL and (
            n != 1.0 or implication == LogicOperatorType.ZADEH
        ):
            return False
        if self.axioms_C_is_a_A.get(a) is not None:
            conc: Concept = pcd.get_definition()
            for gci in self.axioms_C_is_a_A.get(a):
                d: Degree = gci.get_degree()
                if (
                    gci.get_subsumed() != conc
                    or str(gci.get_subsumer()) != a
                    or constants.KNOWLEDGE_BASE_SEMANTICS != FuzzyLogic.CLASSICAL
                    and (
                        not d.is_numeric()
                        or typing.cast(DegreeNumeric, d).get_numerical_value() != 1.0
                        or gci.get_type() == LogicOperatorType.KLEENE_DIENES
                    )
                    and a in self.t_definitions
                    and len(self.t_inclusions.get(a, set())) > 1
                ):
                    continue
                self.t_definitions[a] = conc
                self.remove_A_is_a_X(a, pcd, self.axioms_to_do_A_is_a_C)
                self.remove_A_is_a_X(a, pcd, self.t_inclusions)
                self.remove_C_is_a_A(str(conc), gci)
                Util.debug(f"Definition Absorbed: {a} = {conc}")
                return True
        return False

    @typing.overload
    def remove_A_is_a_X(
        self,
        key: str,
        pcd: PrimitiveConceptDefinition,
        pcd_dict: dict[str, set[PrimitiveConceptDefinition]],
    ) -> None: ...

    @typing.overload
    def remove_A_is_a_X(
        self, key: str, pcd: PrimitiveConceptDefinition, atomic: bool
    ) -> None: ...

    def remove_A_is_a_X(self, *args) -> None:
        assert len(args) == 3
        assert isinstance(args[0], str)
        assert isinstance(args[1], PrimitiveConceptDefinition)
        if isinstance(args[2], bool):
            self.__remove_A_is_a_X_2(*args)
        elif trycast.checkcast(dict[str, set[PrimitiveConceptDefinition]], args[2]):
            self.__remove_A_is_a_X_1(*args)
        else:
            raise ValueError

    def __remove_A_is_a_X_1(
        self,
        key: str,
        pcd: PrimitiveConceptDefinition,
        pcd_dict: dict[str, set[PrimitiveConceptDefinition]],
    ) -> None:
        pcd_dict.get(key).remove(pcd)
        if len(pcd_dict.get(key)) == 0:
            del pcd_dict[key]

    def __remove_A_is_a_X_2(
        self, key: str, pcd: PrimitiveConceptDefinition, atomic: bool
    ) -> None:
        if atomic:
            self.remove_A_is_a_B(key, pcd)
        else:
            self.remove_A_is_a_C(key, pcd)

    def remove_A_is_a_B(self, key: str, pcd: PrimitiveConceptDefinition) -> None:
        self.axioms_A_is_a_B.get(key).remove(pcd)
        if len(self.axioms_A_is_a_B.get(key)) == 0:
            del self.axioms_A_is_a_B[key]

    def remove_A_is_a_C(self, key: str, pcd: PrimitiveConceptDefinition) -> None:
        self.axioms_A_is_a_C.get(key).remove(pcd)
        if len(self.axioms_A_is_a_C.get(key)) == 0:
            del self.axioms_A_is_a_C[key]

    def remove_C_is_a_A(self, key: str, gci: GeneralConceptInclusion) -> None:
        self.axioms_C_is_a_A.get(key).remove(gci)
        if len(self.axioms_C_is_a_A.get(key)) == 0:
            del self.axioms_C_is_a_A[key]

    def remove_C_is_a_D(self, key: str, gci: GeneralConceptInclusion) -> None:
        self.axioms_C_is_a_D.get(key).remove(gci)
        if len(self.axioms_C_is_a_D.get(key)) == 0:
            del self.axioms_C_is_a_D[key]

    def remove_C_is_a_X(
        self, key: str, gci: GeneralConceptInclusion, atomic: bool
    ) -> None:
        if atomic:
            self.remove_C_is_a_A(key, gci)
        else:
            self.remove_C_is_a_D(key, gci)

    def gci_transformations_A_is_a_C(self) -> None:
        Util.debug(
            f"{constants.SEPARATOR}gci_transformations_A_is_a_C{constants.SEPARATOR}"
        )
        for pcds in self.axioms_to_do_A_is_a_C.values():
            for tau in list(pcds):
                if not self.gci_transformation(tau):
                    self.add_axiom_to_A_is_a_C(
                        tau.get_defined_concept(), tau, self.axioms_A_is_a_C
                    )

    def gci_transformations_C_is_a_A(self) -> None:
        Util.debug(
            f"{constants.SEPARATOR}gci_transformations_C_is_a_A{constants.SEPARATOR}"
        )
        for gcis in self.axioms_to_do_C_is_a_A.values():
            for tau in list(gcis):
                if not self.gci_transformation(tau, True):
                    self.add_axiom_to_C_is_a_A(
                        tau.get_subsumer(),
                        tau.get_subsumed(),
                        tau.get_degree(),
                        tau.get_type(),
                    )

    def gci_transformations_C_is_a_D(self) -> None:
        Util.debug(
            f"{constants.SEPARATOR}gci_transformations_C_is_a_D{constants.SEPARATOR}"
        )
        for gcis in self.axioms_to_do_C_is_a_D.values():
            for tau in list(gcis):
                if self.gci_transformation(tau, False):
                    continue
                self.add_axiom_to_C_is_a_D(
                    tau.get_subsumer(),
                    tau.get_subsumed(),
                    tau.get_degree(),
                    tau.get_type(),
                )

    def partition_loop_A_is_a_B(self) -> None:
        cp: dict[str, set[PrimitiveConceptDefinition]] = {
            k: [c.clone() for c in v] for k, v in self.axioms_A_is_a_B.items()
        }
        for pcds_tmp in cp.values():
            pcds: set[PrimitiveConceptDefinition] = set([c.clone() for c in pcds_tmp])
            for tau in pcds:
                if not self.synonym_absorption_A_is_a_B(
                    tau
                ) and not self.concept_absorption(tau, True):
                    continue

    def partition_loop_to_do_A_is_a_B(self) -> None:
        cp: dict[str, set[PrimitiveConceptDefinition]] = {
            k: [c.clone() for c in v] for k, v in self.axioms_to_do_A_is_a_B.items()
        }
        for pcds_tmp in cp.values():
            pcds: set[PrimitiveConceptDefinition] = set([c.clone() for c in pcds_tmp])
            for tau in pcds:
                if not self.synonym_absorption_to_do_A_is_a_B(tau):
                    continue
        self.axioms_to_do_A_is_a_B.clear()

    def partition_loop_A_is_a_C(self) -> None:
        cp: dict[str, set[PrimitiveConceptDefinition]] = {
            k: [c.clone() for c in v] for k, v in self.axioms_A_is_a_C.items()
        }
        for pcds_tmp in cp.values():
            pcds: set[PrimitiveConceptDefinition] = set([c.clone() for c in pcds_tmp])
            for tau in pcds:
                if not self.concept_absorption(tau, False) and not self.role_absorption(
                    tau
                ):
                    continue

    def partition_loop_to_do_A_is_a_C(self) -> None:
        cp: dict[str, set[PrimitiveConceptDefinition]] = {
            k: [c.clone() for c in v] for k, v in self.axioms_to_do_A_is_a_C.items()
        }
        for pcds_tmp in cp.values():
            pcds: set[PrimitiveConceptDefinition] = set([c.clone() for c in pcds_tmp])
            for tau in pcds:
                if not self.definition_absorption_to_do(tau):
                    continue
        self.axioms_to_do_A_is_a_C.clear()

    def partition_loop_C_is_a_A(self) -> None:
        cp: dict[str, set[GeneralConceptInclusion]] = {
            k: [c.clone() for c in v] for k, v in self.axioms_C_is_a_A.items()
        }
        for gcis_tmp in cp.values():
            gcis: set[GeneralConceptInclusion] = set([c.clone() for c in gcis_tmp])
            for tau in gcis:
                if (
                    not self.concept_absorption(tau, True)
                    and not self.definition_absorption(tau)
                    and not self.role_absorption(tau, True)
                ):
                    continue

    def partition_loop_C_is_a_D(self) -> None:
        cp: dict[str, set[GeneralConceptInclusion]] = {
            k: [c.clone() for c in v] for k, v in self.axioms_C_is_a_D.items()
        }
        for gcis_tmp in cp.values():
            gcis: set[GeneralConceptInclusion] = set([c.clone() for c in gcis_tmp])
            for tau in gcis:
                if not self.concept_absorption(tau, False) and not self.role_absorption(
                    tau, False
                ):
                    continue

    def preprocess_tbox(self) -> None:
        no_abs: bool = False
        if ConfigReader.OPTIMIZATIONS == 0 or no_abs:
            Util.debug("No Absorption...")
            self.represent_tbox_with_gcis()
            return
        if self.is_lazy_unfoldable():
            Util.debug("Already lazy unfoldable")
            self.lazy_unfoldable = True
            for a, hs in self.axioms_A_equiv_C.items():
                for c in hs:
                    self.t_definitions[a] = c
            for a, hs in self.axioms_A_is_a_C.items():
                for pcd in hs:
                    self.add_axiom_to_inc(a, pcd)
            for a, hs in self.axioms_A_is_a_B.items():
                for pcd in hs:
                    self.add_axiom_to_inc(a, pcd)
            self.solve_domain_and_range_axioms()
            return
        self.add_axioms_to_tg()
        self.axioms_to_do_A_is_a_B = dict()
        self.axioms_to_do_A_is_a_C = {
            k: set([c.clone() for c in v]) for k, v in self.axioms_A_is_a_C.items()
        }
        self.axioms_to_do_C_is_a_A = {
            k: set([c.clone() for c in v]) for k, v in self.axioms_C_is_a_A.items()
        }
        self.axioms_to_do_C_is_a_D = {
            k: set([c.clone() for c in v]) for k, v in self.axioms_C_is_a_D.items()
        }
        self.axioms_A_is_a_C.clear()
        self.axioms_C_is_a_A.clear()
        self.axioms_C_is_a_D.clear()
        self.axioms_to_do_tmp_A_is_a_C = dict()
        self.axioms_to_do_tmp_C_is_a_A = dict()
        self.axioms_to_do_tmp_C_is_a_D = dict()
        while not (
            len(self.axioms_to_do_A_is_a_C) == 0
            and len(self.axioms_to_do_C_is_a_A) == 0
            and len(self.axioms_to_do_C_is_a_D) == 0
        ):
            self.gci_transformations_A_is_a_C()
            self.gci_transformations_C_is_a_A()
            self.gci_transformations_C_is_a_D()
            self.axioms_to_do_A_is_a_C = {
                k: set([c.clone() for c in v])
                for k, v in self.axioms_to_do_tmp_A_is_a_C.items()
            }
            self.axioms_to_do_C_is_a_A = {
                k: set([c.clone() for c in v])
                for k, v in self.axioms_to_do_tmp_C_is_a_A.items()
            }
            self.axioms_to_do_C_is_a_D = {
                k: set([c.clone() for c in v])
                for k, v in self.axioms_to_do_tmp_C_is_a_D.items()
            }
            self.axioms_to_do_tmp_A_is_a_C.clear()
            self.axioms_to_do_tmp_C_is_a_A.clear()
            self.axioms_to_do_tmp_C_is_a_D.clear()
        self.partition_loop_A_is_a_B()
        self.partition_loop_A_is_a_C()
        self.partition_loop_C_is_a_A()
        self.partition_loop_C_is_a_D()
        self.partition_loop_to_do_A_is_a_B()
        self.partition_loop_to_do_A_is_a_C()
        self.exit_condition()
        for ind in self.individuals.values():
            for gci in self.t_G:
                self.solve_gci(ind, gci)
        self.solve_domain_and_range_axioms()

    def is_lazy_unfoldable(self) -> bool:
        if len(self.axioms_C_is_a_A) != 0:
            return False
        if len(self.axioms_C_is_a_D) != 0:
            return False
        if len(self.axioms_C_equiv_D) != 0:
            return False
        if len(self.axioms_A_equiv_C) != 0:
            for a in self.axioms_A_equiv_C:
                if (
                    a not in self.axioms_A_is_a_B
                    and a not in self.axioms_A_is_a_C
                    and len(self.axioms_A_equiv_C[a]) <= 1
                ):
                    continue
                return False
        for a in self.t_disjoints:
            for b in self.t_disjoints.get(a):
                if a not in self.axioms_A_equiv_C or b not in self.axioms_A_equiv_C:
                    continue
                return False
        return True

    def exit_condition(self) -> None:
        Util.debug(f"{constants.SEPARATOR}Exit condition{constants.SEPARATOR}")
        for pcds in self.axioms_A_is_a_B.values():
            for pcd in pcds:
                self.exit_condition_A_is_a_X(pcd)
        for pcds in self.axioms_A_is_a_C.values():
            for pcd in pcds:
                self.exit_condition_A_is_a_X(pcd)
        for gcis in self.axioms_C_is_a_A.values():
            for gci in gcis:
                self.exit_condition_C_is_a_X(gci)
        for gcis in self.axioms_C_is_a_D.values():
            for gci in gcis:
                self.exit_condition_C_is_a_X(gci)

    def exit_condition_C_is_a_X(self, gci: GeneralConceptInclusion) -> None:
        c1: Concept = gci.get_subsumed()
        c2: Concept = gci.get_subsumer()
        if c1.type == ConceptType.TOP:
            self.t_G.append(gci)
        else:
            gci_type: LogicOperatorType = gci.get_type()
            if gci_type == LogicOperatorType.GOEDEL:
                self.t_G.append(
                    GeneralConceptInclusion(
                        ImpliesConcept.goedel_implies(c1, c2),
                        TruthConcept.get_top(),
                        gci.get_degree(),
                        LogicOperatorType.GOEDEL,
                    )
                )
            elif gci_type == LogicOperatorType.KLEENE_DIENES:
                self.t_G.append(
                    GeneralConceptInclusion(
                        ImpliesConcept.kleene_dienes_implies(c1, c2),
                        TruthConcept.get_top(),
                        gci.get_degree(),
                        LogicOperatorType.KLEENE_DIENES,
                    )
                )
            elif gci_type == LogicOperatorType.LUKASIEWICZ:
                self.t_G.append(
                    GeneralConceptInclusion(
                        ImpliesConcept.lukasiewicz_implies(c1, c2),
                        TruthConcept.get_top(),
                        gci.get_degree(),
                        LogicOperatorType.LUKASIEWICZ,
                    )
                )
            else:
                self.t_G.append(
                    GeneralConceptInclusion(
                        ImpliesConcept.lukasiewicz_implies(c1, c2),
                        TruthConcept.get_top(),
                        DegreeNumeric.get_one(),
                        LogicOperatorType.ZADEH,
                    )
                )

    def exit_condition_A_is_a_X(self, pcd: PrimitiveConceptDefinition) -> None:
        c1: Concept = self.get_concept(pcd.get_defined_concept())
        c2: Concept = pcd.get_definition()
        implication_type: LogicOperatorType = pcd.get_type()
        n: float = pcd.get_degree()
        gci: GeneralConceptInclusion = GeneralConceptInclusion(
            c2,
            c1,
            DegreeNumeric.get_degree(n),
            implication_type,
        )

        if c1.type == ConceptType.TOP:
            self.t_G.append(gci)
        else:
            if gci.get_type() == LogicOperatorType.GOEDEL:
                self.t_G.append(
                    GeneralConceptInclusion(
                        ImpliesConcept.goedel_implies(c1, c2),
                        TruthConcept.get_top(),
                        gci.get_degree(),
                        LogicOperatorType.GOEDEL,
                    )
                )
            elif gci.get_type() == LogicOperatorType.KLEENE_DIENES:
                self.t_G.append(
                    GeneralConceptInclusion(
                        ImpliesConcept.kleene_dienes_implies(c1, c2),
                        TruthConcept.get_top(),
                        gci.get_degree(),
                        LogicOperatorType.KLEENE_DIENES,
                    )
                )
            elif gci.get_type() == LogicOperatorType.LUKASIEWICZ:
                self.t_G.append(
                    GeneralConceptInclusion(
                        ImpliesConcept.lukasiewicz_implies(c1, c2),
                        TruthConcept.get_top(),
                        gci.get_degree(),
                        LogicOperatorType.LUKASIEWICZ,
                    )
                )
            else:
                self.t_G.append(
                    GeneralConceptInclusion(
                        ImpliesConcept.lukasiewicz_implies(c1, c2),
                        TruthConcept.get_top(),
                        DegreeNumeric.get_one(),
                        LogicOperatorType.ZADEH,
                    )
                )

    def is_loaded(self) -> bool:
        return self.KB_LOADED

    def check_role(self, role_name: str, conc: Concept) -> None:
        if (
            self.atomic_concepts.get(role_name) is not None
            or self.concrete_concepts.get(role_name) is not None
        ):
            Util.warning(
                f"Warning: {role_name} is the name of both a concept and a role."
            )
        if conc.is_concrete():
            if role_name in self.abstract_roles:
                Util.error(f"Error: Role {role_name} cannot be concrete and abstract.")
            self.concrete_roles.add(role_name)
        else:
            if role_name in self.concrete_roles:
                Util.error(f"Error: Role {role_name} cannot be concrete and abstract.")
            self.abstract_roles.add(role_name)

    @typing.overload
    def degree_if_not_one(self, deg: Degree) -> str: ...

    @typing.overload
    def degree_if_not_one(self, d: float) -> str: ...

    def degree_if_not_one(self, *args) -> str:
        assert len(args) == 1
        if isinstance(args[0], Degree):
            return self.__degree_if_not_one_1(*args)
        elif isinstance(args[0], constants.NUMBER):
            return self.__degree_if_not_one_2(*args)
        else:
            raise ValueError

    def __degree_if_not_one_1(self, deg: Degree) -> str:
        if deg.is_numeric():
            return self.degree_if_not_one(
                typing.cast(DegreeNumeric, deg).get_numerical_value()
            )
        return str(deg)

    def __degree_if_not_one_2(self, d: float) -> str:
        return "" if d == 1.0 else str(d)

    def define_concreate_feature(self, role: str) -> None:
        if role in self.concrete_features:
            return
        if role in self.abstract_roles:
            Util.error(f"Error: Role {role} cannot be concrete and abstract.")
        self.concrete_roles.add(role)
        self.functional_roles.add(role)
        self.concrete_fuzzy_concepts = True
        self.milp.add_string_feature(role)

    def define_boolean_concrete_feature(self, fun_role: str) -> None:
        self.define_concreate_feature(fun_role)
        self.concrete_features[fun_role] = ConcreteFeature(fun_role, True)

    def define_string_concrete_feature(self, fun_role: str) -> None:
        self.define_concreate_feature(fun_role)
        self.concrete_features[fun_role] = ConcreteFeature(fun_role)

    def define_integer_concrete_feature(self, fun_role: str, d1: int, d2: int) -> None:
        self.define_concreate_feature(fun_role)
        self.concrete_features[fun_role] = ConcreteFeature(fun_role, int(d1), int(d2))

    def define_real_concrete_feature(self, fun_role: str, d1: float, d2: float) -> None:
        self.define_concreate_feature(fun_role)
        self.concrete_features[fun_role] = ConcreteFeature(
            fun_role, float(d1), float(d2)
        )

    def set_logic(self, logic: FuzzyLogic) -> None:
        constants.KNOWLEDGE_BASE_SEMANTICS = logic
        Util.debug(f"Fuzzy logic: {logic}")

    def get_logic(self) -> FuzzyLogic:
        return constants.KNOWLEDGE_BASE_SEMANTICS

    def rule_atomic(self, ass: Assertion) -> None:
        self.rules_applied[KnowledgeBaseRules.RULE_ATOMIC] += 1
        self.old_01_variables += 1
        self.rule_lazy_unfolding(ass)

    def rule_complemented_lazy_unfolding(self, ass: Assertion) -> None:
        ind: Individual = ass.get_individual()
        not_a: Concept = ass.get_concept()
        x_a_not_a: Variable = self.milp.get_variable(ass)
        a: Concept = -not_a
        a_name: str = str(a)
        syns: set[str] = self.t_synonyms.get(a_name, set())
        for syn in syns:
            not_c: Concept = -self.atomic_concepts.get(syn)
            x_not_c: Variable = self.milp.get_variable(ind, not_c)
            self.add_assertion(ind, not_c, DegreeVariable.get_degree(x_not_c))
            self.milp.add_new_constraint(
                Expression(Term(1.0, x_not_c), Term(-1.0, x_a_not_a)),
                InequalityType.EQUAL,
            )
            self.old_01_variables += 1
        c: Concept = self.t_definitions.get(a_name)
        if c is not None:
            not_c: Concept = -c
            x_a_not_c: Variable = self.milp.get_variable(ind, not_c)
            self.add_assertion(ind, not_c, DegreeVariable.get_degree(x_a_not_c))
            self.milp.add_new_constraint(
                Expression(Term(1.0, x_a_not_a), Term(-1.0, x_a_not_c)),
                InequalityType.EQUAL,
            )

    def rule_lazy_unfolding(self, ass: Assertion) -> None:
        ind: Individual = ass.get_individual()
        a: Concept = ass.get_concept()
        a_name: str = str(a)
        var_a: Variable = self.milp.get_variable(ind, a)
        ind_a: Variable = self.milp.get_variable(ind, a)
        pcds: set[PrimitiveConceptDefinition] = self.t_inclusions.get(a_name, set())
        for pcd in pcds:
            if pcd.get_type() == LogicOperatorType.KLEENE_DIENES:
                kd: Concept = ImpliesConcept.kleene_dienes_implies(
                    a, pcd.get_definition()
                )
                self.add_assertion(ind, kd, DegreeNumeric.get_degree(pcd.get_degree()))
                continue
            self.old_01_variables += 1
            self.old_binary_variables += 1
            concept: Concept = pcd.get_definition()
            ind_c: Variable = self.milp.get_variable(ind, concept)
            self.add_assertion(ind, concept, DegreeVariable(ind_c))
            n: float = pcd.get_degree()
            if n == 1.0:
                self.milp.add_new_constraint(
                    Expression(Term(1.0, ind_c), Term(-1.0, ind_a)),
                    InequalityType.GREATER_THAN,
                )
                continue
            if pcd.get_type() == LogicOperatorType.LUKASIEWICZ:
                LukasiewiczSolver.and_geq_equation(ind_c, ind_a, n, self.milp)
            elif pcd.get_type() == LogicOperatorType.GOEDEL:
                ZadehSolver.and_geq_equation(ind_c, ind_a, n, self.milp)
            elif pcd.get_type() == LogicOperatorType.ZADEH:
                self.milp.add_new_constraint(
                    Expression(Term(1.0, ind_c), Term(-1.0, ind_a)),
                    InequalityType.GREATER_THAN,
                )
        syns: set[str] = self.t_synonyms.get(a_name)
        if syns is not None:
            Util.debug(f"Lazy unfolding for synonyms: {a_name}")
            for syn in syns:
                Util.debug(f"Synonym with: {syn}")
                concept: Concept = self.atomic_concepts.get(syn)
                ind_c: Variable = self.milp.get_variable(ind, concept)
                self.add_assertion(ind, concept, DegreeVariable.get_degree(ind_c))
                self.milp.add_new_constraint(
                    Expression(Term(1.0, ind_c), Term(-1.0, ind_a)),
                    InequalityType.EQUAL,
                )
                self.old_01_variables += 1
        c: Concept = self.t_definitions.get(a_name)
        if c is not None:
            var_c: Variable = self.milp.get_variable(ind, c)
            self.add_assertion(ind, c, DegreeVariable.get_degree(var_c))
            self.milp.add_new_constraint(
                Expression(Term(1.0, var_c), Term(-1.0, var_a)), InequalityType.EQUAL
            )
        disj_concs: set[str] = self.t_disjoints.get(a_name)
        if disj_concs is not None:
            Util.debug(f"Lazy unfolding Disjoint axioms: {a_name}")
            hs2: set[str] = self.disjoint_variables.get(a_name, set())
            for name in disj_concs:
                Util.debug(f"Disjoint with: {name}")
                self.old_binary_variables += 1
                var_disj: Variable = self.milp.get_variable(ind, name)
                self.add_assertion(
                    ind, AtomicConcept(name), DegreeVariable.get_degree(var_disj)
                )
                if str(var_disj) not in hs2:
                    ZadehSolver.and_equation(var_a, var_disj, self.milp)
                    hs2.add(str(var_disj))
            self.disjoint_variables[a_name] = hs2

    def rule_complemented_atomic(self, ass: Assertion) -> None:
        self.rules_applied[KnowledgeBaseRules.RULE_COMPLEMENT] += 1
        ind: Individual = ass.get_individual()
        not_a: Concept = ass.get_concept()
        x_a_not_a: Variable = self.milp.get_variable(ass)
        a: Concept = -not_a
        x_a_is_a: Variable = self.milp.get_variable(ind, a)
        self.milp.add_new_constraint(
            Expression(1.0, Term(-1.0, x_a_is_a), Term(-1.0, x_a_not_a)),
            InequalityType.EQUAL,
        )
        self.rule_complemented_lazy_unfolding(ass)

    def rule_and(self, ass: Assertion) -> None:
        if constants.KNOWLEDGE_BASE_SEMANTICS == FuzzyLogic.LUKASIEWICZ:
            self.rules_applied[KnowledgeBaseRules.RULE_LUKASIEWICZ_AND] += 1
            LukasiewiczSolver.solve_and(ass, self)
            return
        elif constants.KNOWLEDGE_BASE_SEMANTICS == FuzzyLogic.ZADEH:
            self.rules_applied[KnowledgeBaseRules.RULE_GOEDEL_AND] += 1
            ZadehSolver.solve_and(ass, self)
            return
        self.rules_applied[KnowledgeBaseRules.RULE_GOEDEL_AND] += 1
        ClassicalSolver.solve_and(ass, self)

    def rule_or(self, ass: Assertion) -> None:
        if constants.KNOWLEDGE_BASE_SEMANTICS == FuzzyLogic.LUKASIEWICZ:
            self.rules_applied[KnowledgeBaseRules.RULE_LUKASIEWICZ_OR] += 1
            LukasiewiczSolver.solve_or(ass, self)
            return
        elif constants.KNOWLEDGE_BASE_SEMANTICS == FuzzyLogic.ZADEH:
            self.rules_applied[KnowledgeBaseRules.RULE_GOEDEL_OR] += 1
            ZadehSolver.solve_or(ass, self)
            return
        self.rules_applied[KnowledgeBaseRules.RULE_LUKASIEWICZ_OR] += 1
        ClassicalSolver.solve_or(ass, self)

    def rule_has_value(self, ass: Assertion) -> None:
        a: Individual = ass.get_individual()
        c: Concept = ass.get_concept()
        d: Degree = ass.get_lower_limit()
        assert isinstance(c, HasValueInterface)

        r: str = c.role
        o_name: str = str(c.value)
        o: Individual = self.get_individual(o_name)
        self.rules_applied[KnowledgeBaseRules.RULE_HAS_VALUE] += 1
        if r in self.functional_roles and r in a.role_relations:
            rel_set: list[Relation] = a.role_relations.get(r)
            rel: Relation = rel_set[0]
            self.get_correct_version_of_individual(rel)
            b: Individual = rel.get_object_individual()
            b_name: str = str(b)
            x_b_is_o: Variable = self.milp.get_nominal_variable(b_name, o_name)
            if b.is_blockable():
                self.merge(o, b)
            elif b_name != str(o):
                self.merge(b, o)
            rel2: Relation = Relation(r, a, o, d)
            x_rel: Variable = self.milp.get_variable(rel2)
            x_ass: Variable = self.milp.get_variable(a, c)
            x_impl: Variable = self.milp.get_new_variable(VariableType.SEMI_CONTINUOUS)
            ZadehSolver.zadeh_implies_equation(x_impl, x_ass, x_rel, self.milp)
            ZadehSolver.zadeh_implies_equation(1.0, x_b_is_o, x_impl, self.milp)
            ZadehSolver.and_leq_equation(x_ass, x_b_is_o, x_rel, self.milp)
        else:
            self.add_relation(a, r, o, d)

    def add_labels_with_nodes(self, node: str, ind_name: str) -> None:
        name_set: set[str] = self.labels_with_nodes.get(node, set())
        if ind_name not in name_set:
            name_set.add(ind_name)
            self.labels_with_nodes[node] = name_set
            i: Individual = self.get_individual(node)
            for c in i.get_concepts():
                self.rule_ass_nom(i, c, ind_name)

    def rule_some(self, ass: Assertion) -> None:
        if ass.get_type() == ConceptType.HAS_VALUE:
            self.rule_has_value(ass)
        else:
            if constants.KNOWLEDGE_BASE_SEMANTICS == FuzzyLogic.LUKASIEWICZ:
                LukasiewiczSolver.solve_some(ass, self)
            elif constants.KNOWLEDGE_BASE_SEMANTICS == FuzzyLogic.ZADEH:
                ZadehSolver.solve_some(ass, self)
            else:
                ClassicalSolver.solve_some(ass, self)

    def rule_all(self, ass: Assertion) -> None:
        concept: AllSomeConcept = typing.cast(AllSomeConcept, ass.get_concept())

        if concept.curr_concept.type == ConceptType.TOP:
            self.add_assertion(
                ass.get_individual(), TruthConcept.get_top(), ass.get_lower_limit()
            )
        else:
            IndividualHandler.add_restriction(
                ass.get_individual(),
                concept.role,
                concept.curr_concept,
                ass.get_lower_limit(),
                self,
            )

    def rule_complemented_has_value(self, ass: Assertion) -> None:
        a: Individual = ass.get_individual()

        c: Concept = ass.get_concept()
        assert isinstance(c, OperatorConcept)
        c: Concept = c.get_atom()
        assert isinstance(c, HasValueInterface)

        r: str = c.role
        b: str = str(c.value)
        IndividualHandler.add_restriction(a, r, b, ass.get_lower_limit(), self)

    def compute_variables_old_calculus(self, fcc: FuzzyConcreteConcept) -> None:
        if isinstance(fcc, CrispConcreteConcept):
            self.old_binary_variables += 1
        elif isinstance(fcc, LeftConcreteConcept):
            self.old_binary_variables += 3
        elif isinstance(fcc, RightConcreteConcept):
            self.old_binary_variables += 3
        elif isinstance(fcc, TriangularConcreteConcept):
            self.old_binary_variables += 4
        elif isinstance(fcc, TrapezoidalConcreteConcept):
            self.old_binary_variables += 5
        elif isinstance(fcc, LinearConcreteConcept):
            self.old_01_variables += 1
            self.old_binary_variables += 1

    def rule_concrete(self, ass: Assertion) -> None:
        self.rules_applied[KnowledgeBaseRules.RULE_CONCRETE] += 1
        fcc: FuzzyConcreteConcept = typing.cast(FuzzyConcreteConcept, ass.get_concept())
        self.compute_variables_old_calculus(fcc)
        ind: CreatedIndividual = typing.cast(CreatedIndividual, ass.get_individual())

        self.solve_concept_assertion(ind, fcc)
        # fcc.solve_assertion(ind, ass.get_lower_limit(), self)

    def rule_complemented_concrete(self, ass: Assertion) -> None:
        self.rules_applied[KnowledgeBaseRules.RULE_NOT_CONCRETE] += 1
        c: Concept = ass.get_concept()
        assert isinstance(c, OperatorConcept)
        fcc: FuzzyConcreteConcept = typing.cast(FuzzyConcreteConcept, c.get_atom())

        self.compute_variables_old_calculus(fcc)
        ind: CreatedIndividual = typing.cast(CreatedIndividual, ass.get_individual())

        self.solve_concept_complemented_assertion(ind, ass.get_lower_limit(), c)
        # fcc.solve_complement_assertion(ind, ass.get_lower_limit(), self)

    def rule_fuzzy_number(self, ass: Assertion) -> None:
        self.rules_applied[KnowledgeBaseRules.RULE_FUZZY_NUMBER] += 1
        self.rule_concrete(ass)

    def rule_complemented_fuzzy_number(self, ass: Assertion) -> None:
        self.rules_applied[KnowledgeBaseRules.RULE_NOT_FUZZY_NUMBER] += 1
        self.rule_complemented_concrete(ass)

    def rule_modified(self, ass: Assertion) -> None:
        mod: ModifiedConcept = typing.cast(ModifiedConcept, ass.get_concept())
        if isinstance(mod, TriangularlyModifiedConcept):
            self.old_01_variables += 2
        else:
            self.old_01_variables += 1
            self.old_binary_variables += 1
        self.rules_applied[KnowledgeBaseRules.RULE_MODIFIED] += 1

        self.solve_modifier_assertion(
            ass.get_individual(), mod.curr_concept, mod.modifier
        )
        # mod.solve_assertion(ass.get_individual(), ass.get_lower_limit(), self)

    def rule_complemented_modified(self, ass: Assertion) -> None:
        c: Concept = ass.get_concept()
        assert isinstance(c, OperatorConcept)
        mod: ModifiedConcept = typing.cast(ModifiedConcept, c.get_atom())

        if isinstance(mod, TriangularlyModifiedConcept):
            self.old_01_variables += 1
            self.old_binary_variables += 1
        else:
            self.old_01_variables += 2
            self.old_binary_variables += 2
        self.rules_applied[KnowledgeBaseRules.RULE_NOT_MODIFIED] += 1
        # mod.solve_complement_assertion(
        #     ass.get_individual(), ass.get_lower_limit(), self
        # )
        self.solve_modifier_complemented_assertion(
            ass.get_individual(), c, ass.get_lower_limit()
        )

    def rule_bottom(self, ass: Assertion) -> None:
        self.rules_applied[KnowledgeBaseRules.RULE_BOTTOM] += 1
        x_ass: Variable = self.milp.get_variable(ass)
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_ass)), InequalityType.EQUAL, 0.0
        )

    def rule_top(self, ass: Assertion) -> None:
        self.rules_applied[KnowledgeBaseRules.RULE_TOP] += 1
        self.milp.add_new_constraint(ass, 1.0)

    def rule_self(self, ass: Assertion) -> None:
        self.rules_applied[KnowledgeBaseRules.RULE_SELF] += 1
        a: Individual = ass.get_individual()
        c: Concept = ass.get_concept()

        assert isinstance(c, HasRoleInterface)

        role: str = c.role
        r: Relation = IndividualHandler.add_relation(
            a, role, a, ass.get_lower_limit(), self
        )
        self.solve_role_inclusion_axioms(a, r)

    def rule_complemented_self(self, ass: Assertion) -> None:
        self.rules_applied[KnowledgeBaseRules.RULE_NOT_SELF] += 1
        a: Individual = ass.get_individual()
        c: Concept = ass.get_concept()
        assert isinstance(c, OperatorConcept)
        assert isinstance(c.concepts[0], HasRoleInterface)
        c: Concept = c.concepts[0]
        IndividualHandler.add_not_self_restriction(a, c.role, self)

    def rule_upper_approximation(self, ass: Assertion) -> None:
        a: Individual = ass.get_individual()
        con: Concept = ass.get_concept()
        assert isinstance(con, ApproximationConcept)

        self.add_assertion(
            Assertion(
                a,
                AllSomeConcept.some(con.role, con.curr_concept),
                ass.get_lower_limit(),
            )
        )

    def rule_lower_approximation(self, ass: Assertion) -> None:
        a: Individual = ass.get_individual()
        con: Concept = ass.get_concept()
        assert isinstance(con, ApproximationConcept)

        self.add_assertion(
            Assertion(
                a, AllSomeConcept.all(con.role, con.curr_concept), ass.get_lower_limit()
            )
        )

    def rule_tight_upper_approximation(self, ass: Assertion) -> None:
        a: Individual = ass.get_individual()
        con: Concept = ass.get_concept()
        assert isinstance(con, ApproximationConcept)

        self.add_assertion(
            Assertion(
                a,
                AllSomeConcept.all(
                    con.role, AllSomeConcept.some(con.role, con.curr_concept)
                ),
                ass.get_lower_limit(),
            )
        )

    def rule_tight_lower_approximation(self, ass: Assertion) -> None:
        a: Individual = ass.get_individual()
        con: Concept = ass.get_concept()
        assert isinstance(con, ApproximationConcept)

        self.add_assertion(
            Assertion(
                a,
                AllSomeConcept.all(
                    con.role, AllSomeConcept.all(con.role, con.curr_concept)
                ),
                ass.get_lower_limit(),
            )
        )

    def rule_loose_upper_approximation(self, ass: Assertion) -> None:
        a: Individual = ass.get_individual()
        con: Concept = ass.get_concept()
        assert isinstance(con, ApproximationConcept)

        self.add_assertion(
            Assertion(
                a,
                AllSomeConcept.some(
                    con.role, AllSomeConcept.some(con.role, con.curr_concept)
                ),
                ass.get_lower_limit(),
            )
        )

    def rule_loose_lower_approximation(self, ass: Assertion) -> None:
        a: Individual = ass.get_individual()
        con: Concept = ass.get_concept()
        assert isinstance(con, ApproximationConcept)

        self.add_assertion(
            Assertion(
                a,
                AllSomeConcept.some(
                    con.role, AllSomeConcept.all(con.role, con.curr_concept)
                ),
                ass.get_lower_limit(),
            )
        )

    def rule_goedel_and(self, ass: Assertion) -> None:
        self.rules_applied[KnowledgeBaseRules.RULE_GOEDEL_AND] += 1
        ZadehSolver.solve_and(ass, self)

    def rule_goedel_or(self, ass: Assertion) -> None:
        self.rules_applied[KnowledgeBaseRules.RULE_GOEDEL_OR] += 1
        ZadehSolver.solve_or(ass, self)

    def rule_lukasiewicz_and(self, ass: Assertion) -> None:
        self.rules_applied[KnowledgeBaseRules.RULE_LUKASIEWICZ_AND] += 1
        LukasiewiczSolver.solve_and(ass, self)

    def rule_lukasiewicz_or(self, ass: Assertion) -> None:
        self.rules_applied[KnowledgeBaseRules.RULE_LUKASIEWICZ_OR] += 1
        LukasiewiczSolver.solve_or(ass, self)

    def rule_goedel_implication(self, ass: Assertion) -> None:
        self.old_01_variables += 2
        self.old_binary_variables += 1
        self.rules_applied[KnowledgeBaseRules.RULE_GOEDEL_IMPLIES] += 1
        ind: Individual = ass.get_individual()
        goedel_impl: ImpliesConcept = typing.cast(ImpliesConcept, ass.get_concept())
        x_is_c: Variable = self.milp.get_variable(ind, goedel_impl)
        c1: Concept = goedel_impl.concepts[0]
        x_is_c1: Variable = self.milp.get_variable(ind, c1)
        not_c1: Concept = -c1
        x_is_not_c1: Variable = self.milp.get_variable(ind, not_c1)
        c2: Concept = goedel_impl.concepts[1]
        x_is_c2: Variable = self.milp.get_variable(ind, c2)
        self.add_assertion(ind, not_c1, DegreeVariable.get_degree(x_is_not_c1))
        self.rule_complemented(ind, not_c1)
        self.add_assertion(ind, c2, DegreeVariable.get_degree(x_is_c2))
        ZadehSolver.goedel_implies_equation(x_is_c, x_is_c1, x_is_c2, self.milp)

    def rule_zadeh_implication(self, ass: Assertion) -> None:
        self.old_01_variables += 2
        self.old_binary_variables += 1
        self.rules_applied[KnowledgeBaseRules.RULE_ZADEH_IMPLIES] += 1
        ind: Individual = ass.get_individual()
        z_impl: ImpliesConcept = typing.cast(ImpliesConcept, ass.get_concept())
        x_is_c: Variable = self.milp.get_variable(ind, z_impl)
        c1: Concept = z_impl.concepts[0]
        x_is_c1: Variable = self.milp.get_variable(ind, c1)
        not_c1: Concept = -c1
        x_is_not_c1: Variable = self.milp.get_variable(ind, not_c1)
        c2: Concept = z_impl.concepts[1]
        x_is_c2: Variable = self.milp.get_variable(ind, c2)
        self.add_assertion(ind, not_c1, DegreeVariable.get_degree(x_is_not_c1))
        self.rule_complemented(ind, not_c1)
        self.add_assertion(ind, c2, DegreeVariable.get_degree(x_is_c2))
        ZadehSolver.zadeh_implies_equation(x_is_c, x_is_c1, x_is_c2, self.milp)

    def rule_complemented_goedel_implication(self, ass: Assertion) -> None:
        self.old_01_variables += 2
        self.old_binary_variables += 1
        self.rules_applied[KnowledgeBaseRules.RULE_NOT_GOEDEL_IMPLIES] += 1
        ind: Individual = ass.get_individual()
        c: Concept = ass.get_concept()
        assert isinstance(c, OperatorConcept)
        goedel_impl: ImpliesConcept = typing.cast(ImpliesConcept, c.concepts[0])
        x_is_c: Variable = self.milp.get_variable(ind, -goedel_impl)
        c1: Concept = goedel_impl.concepts[0]
        x_is_c1: Variable = self.milp.get_variable(ind, c1)
        c2: Concept = goedel_impl.concepts[1]
        x_is_c2: Variable = self.milp.get_variable(ind, c2)
        not_c2: Concept = -c2
        x_is_not_c2: Variable = self.milp.get_variable(ind, not_c2)
        self.add_assertion(ind, c1, DegreeVariable.get_degree(x_is_c1))
        self.add_assertion(ind, not_c2, DegreeVariable.get_degree(x_is_not_c2))
        ZadehSolver.goedel_implies_equation(x_is_c, x_is_c1, x_is_c2, self.milp)
        self.rule_complemented(ind, goedel_impl)

    def rule_complemented_zadeh_implication(self, ass: Assertion) -> None:
        self.old_01_variables += 2
        self.old_binary_variables += 1
        self.rules_applied[KnowledgeBaseRules.RULE_NOT_ZADEH_IMPLIES] += 1
        ind: Individual = ass.get_individual()
        c: Concept = ass.get_concept()
        assert isinstance(c, OperatorConcept)
        z_impl: ImpliesConcept = typing.cast(ImpliesConcept, c.concepts[0])
        x_is_c: Variable = self.milp.get_variable(ind, -z_impl)
        c1: Concept = z_impl.concepts[0]
        x_is_c1: Variable = self.milp.get_variable(ind, c1)
        c2: Concept = z_impl.concepts[1]
        x_is_c2: Variable = self.milp.get_variable(ind, c2)
        not_c2: Concept = -c2
        x_is_not_c2: Variable = self.milp.get_variable(ind, not_c2)
        self.add_assertion(ind, c1, DegreeVariable.get_degree(x_is_c1))
        self.add_assertion(ind, not_c2, DegreeVariable.get_degree(x_is_not_c2))
        ZadehSolver.zadeh_implies_equation(x_is_c, x_is_c1, x_is_c2, self.milp)
        self.rule_complemented(ind, z_impl)

    def rule_positive_threshold(self, ass: Assertion) -> None:
        self.old_binary_variables += 1
        self.rules_applied[KnowledgeBaseRules.RULE_THRESHOLD] += 1
        i: Individual = ass.get_individual()
        tc: ThresholdConcept = typing.cast(ThresholdConcept, ass.get_concept())
        x_a_in_tc: Variable = self.milp.get_variable(i, tc)
        c: Concept = tc.curr_concept
        x_a_in_c: Variable = self.milp.get_variable(i, c)
        x: float = tc.weight
        self.add_assertion(i, c, DegreeVariable.get_degree(x_a_in_c))
        y: Variable = self.milp.get_new_variable(VariableType.BINARY)
        self.rule_threshold_common(x_a_in_c, x_a_in_tc, y)
        self.milp.add_new_constraint(
            Expression(-x + ConfigReader.EPSILON, Term(-1.0, y), Term(1.0, x_a_in_c)),
            InequalityType.LESS_THAN,
        )
        self.milp.add_new_constraint(
            Expression(1.0 - x, Term(1.0, x_a_in_tc), Term(-1.0, y)),
            InequalityType.GREATER_THAN,
        )

    def rule_threshold_common(
        self, x_a_in_c: Variable, x_a_in_tc: Variable, y: Variable
    ) -> None:
        self.milp.add_new_constraint(
            Expression(-1.0, Term(1.0, x_a_in_tc), Term(-1.0, x_a_in_c), Term(1.0, y)),
            InequalityType.LESS_THAN,
        )
        self.milp.add_new_constraint(
            Expression(1.0, Term(1.0, x_a_in_tc), Term(-1.0, x_a_in_c), Term(-1.0, y)),
            InequalityType.GREATER_THAN,
        )
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_a_in_tc), Term(-1.0, y)), InequalityType.LESS_THAN
        )

    def rule_complemented_positive_threshold(self, ass: Assertion) -> None:
        self.old_01_variables += 2
        self.old_binary_variables += 1
        self.rules_applied[KnowledgeBaseRules.RULE_NOT_THRESHOLD] += 1
        self.rule_complemented_complex_assertion(ass)

    def rule_negative_threshold(self, ass: Assertion) -> None:
        self.old_01_variables += 1
        self.rules_applied[KnowledgeBaseRules.RULE_THRESHOLD] += 1
        i: Individual = ass.get_individual()
        tc: ThresholdConcept = typing.cast(ThresholdConcept, ass.get_concept())
        x_a_in_tc: Variable = self.milp.get_variable(i, tc)
        c: Concept = tc.curr_concept
        x_a_in_c: Variable = self.milp.get_variable(i, c)
        x: float = tc.weight
        self.add_assertion(Assertion(i, c, DegreeVariable.get_degree(x_a_in_c)))
        y: Variable = self.milp.get_new_variable(VariableType.BINARY)
        self.rule_threshold_common(x_a_in_c, x_a_in_tc, y)
        self.milp.add_new_constraint(
            Expression(-x - ConfigReader.EPSILON, Term(2.0, y), Term(1.0, x_a_in_c)),
            InequalityType.GREATER_THAN,
        )
        self.milp.add_new_constraint(
            Expression(-1.0 - x, Term(1.0, x_a_in_tc), Term(1.0, y)),
            InequalityType.LESS_THAN,
        )

    def rule_complemented_negative_threshold(self, ass: Assertion) -> None:
        self.old_01_variables += 2
        self.old_binary_variables += 1
        self.rules_applied[KnowledgeBaseRules.RULE_NOT_THRESHOLD] += 1
        self.rule_complemented_complex_assertion(ass)

    def rule_extended_positive_threshold(self, ass: Assertion) -> None:
        self.old_01_variables += 1
        self.rules_applied[KnowledgeBaseRules.RULE_THRESHOLD] += 1
        i: Individual = ass.get_individual()
        tc: ExtThresholdConcept = typing.cast(ExtThresholdConcept, ass.get_concept())
        x_a_in_tc: Variable = self.milp.get_variable(i, tc)
        c: Concept = tc.curr_concept
        x_a_in_c: Variable = self.milp.get_variable(i, c)
        x: Variable = tc.weight_variable
        self.add_assertion(Assertion(i, c, DegreeVariable.get_degree(x_a_in_c)))
        y: Variable = self.milp.get_new_variable(VariableType.BINARY)
        self.rule_threshold_common(x_a_in_c, x_a_in_tc, y)
        self.milp.add_new_constraint(
            Expression(
                ConfigReader.EPSILON,
                Term(-1.0, x),
                Term(-1.0, y),
                Term(1.0, x_a_in_c),
            ),
            InequalityType.LESS_THAN,
        )
        self.milp.add_new_constraint(
            Expression(1.0, Term(-1.0, x), Term(1.0, x_a_in_tc), Term(-1.0, y)),
            InequalityType.GREATER_THAN,
        )

    def rule_complemented_extended_positive_threshold(self, ass: Assertion) -> None:
        self.old_01_variables += 2
        self.old_binary_variables += 1
        self.rules_applied[KnowledgeBaseRules.RULE_NOT_THRESHOLD] += 1
        self.rule_complemented_complex_assertion(ass)

    def rule_extended_negative_threshold(self, ass: Assertion) -> None:
        self.old_binary_variables += 1
        self.rules_applied[KnowledgeBaseRules.RULE_THRESHOLD] += 1
        i: Individual = ass.get_individual()
        tc: ExtThresholdConcept = typing.cast(ExtThresholdConcept, ass.get_concept())
        x_a_in_tc: Variable = self.milp.get_variable(i, tc)
        c: Concept = tc.curr_concept
        x_a_in_c: Variable = self.milp.get_variable(i, c)
        x: Variable = tc.weight_variable
        self.add_assertion(Assertion(i, c, DegreeVariable.get_degree(x_a_in_c)))
        y: Variable = self.milp.get_new_variable(VariableType.BINARY)
        self.rule_threshold_common(x_a_in_c, x_a_in_tc, y)
        self.milp.add_new_constraint(
            Expression(
                -ConfigReader.EPSILON,
                Term(-1.0, x),
                Term(2.0, y),
                Term(1.0, x_a_in_c),
            ),
            InequalityType.GREATER_THAN,
        )
        self.milp.add_new_constraint(
            Expression(-1.0, Term(-1.0, x), Term(1.0, x_a_in_tc), Term(1.0, y)),
            InequalityType.LESS_THAN,
        )

    def rule_complemented_extended_negative_threshold(self, ass: Assertion) -> None:
        self.old_01_variables += 2
        self.old_binary_variables += 1
        self.rules_applied[KnowledgeBaseRules.RULE_NOT_THRESHOLD] += 1
        self.rule_complemented_complex_assertion(ass)

    def rule_weighted_concept(self, ass: Assertion) -> None:
        self.rules_applied[KnowledgeBaseRules.RULE_WEIGHTED] += 1
        i: Individual = ass.get_individual()
        wc: WeightedConcept = typing.cast(WeightedConcept, ass.get_concept())
        x_a_in_wc: Variable = self.milp.get_variable(i, wc)
        c: Concept = wc.curr_concept
        x_a_in_c: Variable = self.milp.get_variable(i, c)
        w: float = wc.weight
        self.add_assertion(Assertion(i, c, DegreeVariable.get_degree(x_a_in_c)))
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_a_in_wc), Term(-w, x_a_in_c)), InequalityType.EQUAL
        )

    def rule_complemented_weighted_concept(self, ass: Assertion) -> None:
        self.rules_applied[KnowledgeBaseRules.RULE_NOT_WEIGHTED] += 1
        i: Individual = ass.get_individual()
        c: Concept = ass.get_concept()
        assert isinstance(c, OperatorConcept)
        wc: WeightedConcept = typing.cast(WeightedConcept, c.get_atom())
        x_a_in_wc: Variable = self.milp.get_variable(i, -wc)
        not_c: Concept = -wc.curr_concept
        x_a_in_c: Variable = self.milp.get_variable(i, wc.curr_concept)
        x_a_in_not_c: Variable = self.milp.get_variable(i, not_c)
        w: float = wc.weight
        self.add_assertion(Assertion(i, not_c, DegreeVariable.get_degree(x_a_in_not_c)))
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_a_in_wc), Term(-w, x_a_in_c)), InequalityType.EQUAL
        )
        self.rule_complemented(i, c)

    def rule_complemented_complex_assertion(self, ass: Assertion) -> None:
        i: Individual = ass.get_individual()
        c: Concept = -ass.get_concept()
        x: Variable = self.milp.get_variable(i, c)
        self.rule_complemented(i, c)
        self.add_assertion(Assertion(i, c, DegreeVariable.get_degree(x)))

    def rule_complemented(self, i: Individual, c: Concept) -> None:
        x: Variable = self.milp.get_variable(i, c)
        c2: Concept = -c
        x2: Variable = self.milp.get_variable(i, c2)
        self.milp.add_new_constraint(
            Expression(1.0, Term(-1.0, x), Term(-1.0, x2)), InequalityType.EQUAL
        )

    def rule_weighted_sum(self, ass: Assertion) -> None:
        n: int = len(typing.cast(WeightedSumConcept, ass.get_concept()).concepts)
        self.old_01_variables += n
        self.rules_applied[KnowledgeBaseRules.RULE_W_SUM] += 1
        # typing.cast(WeightedSumConcept, ass.get_concept()).solve_assertion(
        #     ass.get_individual(), self
        # )
        self.solve_concept_assertion(
            ass.get_individual(), typing.cast(WeightedSumConcept, ass.get_concept())
        )

    def rule_complemented_weighted_sum(self, ass: Assertion) -> None:
        c: Concept = ass.get_concept()
        assert isinstance(c, OperatorConcept)
        ws: WeightedSumConcept = typing.cast(WeightedSumConcept, c.get_atom())

        n: int = len(ws.concepts)
        self.old_01_variables += n
        self.rules_applied[KnowledgeBaseRules.RULE_NOT_W_SUM] += 1

        # ws.solve_complemented_assertion(ass.get_individual(), self)
        self.solve_concept_complemented_assertion(ass.get_individual(), None, c)

    def rule_weighted_sum_zero(self, ass: Assertion) -> None:
        n: int = len(typing.cast(WeightedSumZeroConcept, ass.get_concept()).concepts)
        self.old_01_variables += n
        self.rules_applied[KnowledgeBaseRules.RULE_W_SUM_ZERO] += 1
        # typing.cast(WeightedSumZeroConcept, ass.get_concept()).solve_assertion(
        #     ass.get_individual(), self
        # )
        self.solve_concept_assertion(
            ass.get_individual(), typing.cast(WeightedSumZeroConcept, ass.get_concept())
        )

    def rule_complemented_weighted_sum_zero(self, ass: Assertion) -> None:
        c: Concept = ass.get_concept()
        assert isinstance(c, OperatorConcept)
        assert isinstance(c.get_atom(), WeightedSumZeroConcept)

        self.rules_applied[KnowledgeBaseRules.RULE_NOT_W_SUM_ZERO] += 1
        # wsz.solve_complemented_assertion(ass.get_individual(), self)
        self.solve_concept_complemented_assertion(ass.get_individual(), None, c)

    def rule_weighted_min(self, ass: Assertion) -> None:
        self.rules_applied[KnowledgeBaseRules.RULE_W_MIN] += 1
        # typing.cast(WeightedMinConcept, ass.get_concept()).solve_assertion(
        #     ass.get_individual(), self
        # )
        self.solve_concept_assertion(
            ass.get_individual(), typing.cast(WeightedMinConcept, ass.get_concept())
        )

    def rule_complemented_weighted_min(self, ass: Assertion) -> None:
        c: Concept = ass.get_concept()
        assert isinstance(c, OperatorConcept)
        assert isinstance(c.get_atom(), WeightedMinConcept)

        self.rules_applied[KnowledgeBaseRules.RULE_NOT_W_MIN] += 1
        # wm.solve_complemented_assertion(ass.get_individual(), self)
        self.solve_concept_complemented_assertion(ass.get_individual(), None, c)

    def rule_weighted_max(self, ass: Assertion) -> None:
        self.rules_applied[KnowledgeBaseRules.RULE_W_MAX] += 1
        # typing.cast(WeightedMaxConcept, ass.get_concept()).solve_assertion(
        #     ass.get_individual(), self
        # )
        self.solve_concept_assertion(
            ass.get_individual(), typing.cast(WeightedMaxConcept, ass.get_concept())
        )

    def rule_complemented_weighted_max(self, ass: Assertion) -> None:
        c: Concept = ass.get_concept()
        assert isinstance(c, OperatorConcept)
        assert isinstance(c.get_atom(), WeightedMaxConcept)

        self.rules_applied[KnowledgeBaseRules.RULE_NOT_W_MAX] += 1
        # wm.solve_complemented_assertion(ass.get_individual(), self)
        self.solve_concept_complemented_assertion(ass.get_individual(), None, c)

    def rule_owa(self, ass: Assertion) -> None:
        n: int = len(typing.cast(OwaConcept, ass.get_concept()).concepts)
        self.old_01_variables += 3 * n
        self.old_binary_variables += n
        self.rules_applied[KnowledgeBaseRules.RULE_OWA] += 1
        # typing.cast(OwaConcept, ass.get_concept()).solve_assertion(
        #     ass.get_individual(), self
        # )
        self.solve_concept_assertion(
            ass.get_individual(), typing.cast(OwaConcept, ass.get_concept())
        )

    def rule_complemented_owa(self, ass: Assertion) -> None:
        c: Concept = ass.get_concept()
        assert isinstance(c, OperatorConcept)
        oc: OwaConcept = typing.cast(OwaConcept, c.get_atom())

        n: int = len(oc.concepts)
        self.old_01_variables += 3 * n
        self.old_binary_variables += n
        self.rules_applied[KnowledgeBaseRules.RULE_NOT_OWA] += 1
        # oc.solve_complemented_assertion(ass.get_individual(), self)

        self.solve_concept_complemented_assertion(ass.get_individual(), None, c)

    def rule_quantified_owa(self, ass: Assertion) -> None:
        self.rules_applied[KnowledgeBaseRules.RULE_OWA] += 1
        # typing.cast(QowaConcept, ass.get_concept()).solve_complemented_assertion(
        #     ass.get_individual(), self
        # )

        self.solve_concept_complemented_assertion(
            ass.get_individual(), None, typing.cast(QowaConcept, ass.get_concept())
        )

    def rule_complemented_quantified_owa(self, ass: Assertion) -> None:
        self.rules_applied[KnowledgeBaseRules.RULE_NOT_OWA] += 1
        self.rule_complemented_complex_assertion(ass)

    def rule_choquet(self, ass: Assertion) -> None:
        self.rules_applied[KnowledgeBaseRules.RULE_CHOQUET_INTEGRAL] += 1
        # typing.cast(ChoquetIntegral, ass.get_concept()).solve_assertion(
        #     ass.get_individual(), self
        # )
        self.solve_concept_assertion(
            ass.get_individual(), typing.cast(ChoquetIntegral, ass.get_concept())
        )

    def rule_complemented_choquet(self, ass: Assertion) -> None:
        c: Concept = ass.get_concept()
        assert isinstance(c, OperatorConcept)
        assert isinstance(c.get_atom(), ChoquetIntegral)

        self.rules_applied[KnowledgeBaseRules.RULE_NOT_CHOQUET_INTEGRAL] += 1
        # ci.solve_complemented_assertion(ass.get_individual(), self)

        self.solve_concept_complemented_assertion(ass.get_individual(), None, c)

    def rule_sugeno(self, ass: Assertion) -> None:
        self.rules_applied[KnowledgeBaseRules.RULE_SUGENO_INTEGRAL] += 1
        # typing.cast(SugenoIntegral, ass.get_concept()).solve_assertion(
        #     ass.get_individual(), self
        # )
        self.solve_concept_assertion(
            ass.get_individual(), typing.cast(SugenoIntegral, ass.get_concept())
        )

    def rule_complemented_sugeno(self, ass: Assertion) -> None:
        c: Concept = ass.get_concept()
        assert isinstance(c, OperatorConcept)
        assert isinstance(c.get_atom(), SugenoIntegral)

        self.rules_applied[KnowledgeBaseRules.RULE_NOT_SUGENO_INTEGRAL] += 1
        # si.solve_complemented_assertion(ass.get_individual(), self)
        self.solve_concept_complemented_assertion(ass.get_individual(), None, c)

    def rule_quasi_sugeno(self, ass: Assertion) -> None:
        self.rules_applied[KnowledgeBaseRules.RULE_QUASI_SUGENO_INTEGRAL] += 1
        # typing.cast(QsugenoIntegral, ass.get_concept()).solve_assertion(
        #     ass.get_individual(), self
        # )
        self.solve_concept_assertion(
            ass.get_individual(), typing.cast(QsugenoIntegral, ass.get_concept())
        )

    def rule_complemented_quasi_sugeno(self, ass: Assertion) -> None:
        c: Concept = ass.get_concept()
        assert isinstance(c, OperatorConcept)
        assert isinstance(c.get_atom(), QsugenoIntegral)

        self.rules_applied[KnowledgeBaseRules.RULE_NOT_QUASI_SUGENO_INTEGRAL] += 1
        # qsi.solve_complemented_assertion(ass.get_individual(), self)
        self.solve_concept_complemented_assertion(ass.get_individual(), None, c)

    def rule_complemented_at_most_datatype_restriction(
        self, b: CreatedIndividual, ass: Assertion
    ) -> None:
        self.rules_applied[KnowledgeBaseRules.RULE_NOT_DATATYPE] += 1
        DatatypeReasoner.apply_not_at_most_value_rule(b, ass, self)

    def rule_complemented_at_least_datatype_restriction(
        self, b: CreatedIndividual, ass: Assertion
    ) -> None:
        self.rules_applied[KnowledgeBaseRules.RULE_NOT_DATATYPE] += 1
        DatatypeReasoner.apply_not_at_least_value_rule(b, ass, self)

    def rule_complemented_exact_datatype_restriction(
        self, b: CreatedIndividual, ass: Assertion
    ) -> None:
        self.rules_applied[KnowledgeBaseRules.RULE_NOT_DATATYPE] += 1
        DatatypeReasoner.apply_not_exact_value_rule(b, ass, self)

    def set_crisp_concept(self, c: Concept) -> None:
        self.milp.add_crisp_concept(str(c))

    def set_crisp_role(self, role_name: str) -> None:
        self.milp.add_crisp_role(role_name)

    def set_dynamic_blocking(self) -> None:
        self.blocking_dynamic = True

    def is_crisp_role(self, role_name: str) -> bool:
        return (
            constants.KNOWLEDGE_BASE_SEMANTICS == FuzzyLogic.CLASSICAL
            or self.milp.is_crisp_role(role_name)
        )

    def is_crisp_concept(self, concept_name: str) -> bool:
        return (
            constants.KNOWLEDGE_BASE_SEMANTICS == FuzzyLogic.CLASSICAL
            or self.milp.is_crisp_concept(concept_name)
        )

    def is_atomic_crisp_concept(self, c: Concept) -> bool:
        return c.is_atomic() and self.is_crisp_concept(str(c))

    def optimize(self, e: Expression) -> Solution:
        if constants.KNOWLEDGE_BASE_SEMANTICS == FuzzyLogic.CLASSICAL:
            self.milp.set_binary_variables()
        self.rule_n2()
        self.rule_n3()
        sol: Solution = self.milp.optimize(e)
        self.show_statistics()
        return sol

    def show_statistics(self) -> None:
        Util.debug("Processed TBox:")
        Util.debug(f"\t\tA = B: {len(self.t_synonyms)}")
        Util.debug(f"\t\tA = C: {len(self.t_definitions)}")
        Util.debug(f"\t\tA isA X: {len(self.t_inclusions)}")
        Util.debug(f"\t\tC isA X (not absorbed): {len(self.t_G)}")
        Util.debug(
            f"\t\tDomain restrictions: {self.get_number_of_domain_restrictions()}"
        )
        Util.debug(f"\t\tRange restrictions: {self.get_number_of_range_restrictions()}")
        Util.debug("Tableau:")
        Util.debug(f"\t\tIndividuals: {len(self.individuals)}")
        Util.debug(f"\t\tConcept assertions: {self.num_assertions}")
        Util.debug(f"\t\tRole assertions: {self.num_relations}")
        Util.debug(f"\t\tMaximal forest depth: {self.max_depth}")
        Util.debug("Reasoning rules:")
        for rule, count in self.rules_applied.items():
            if count != 0:
                Util.debug(f"\t\tRule {rule}: {count}")
        Util.debug("Old calculus:")
        Util.debug(
            f"\t\t{{0,1}} binary variables (old calculus): {self.old_binary_variables}"
        )
        Util.debug(
            f"\t\t[0,1] semi continuous variables (old calculus): {self.old_01_variables}"
        )
        Util.debug("Answer:")

    def get_number_of_domain_restrictions(self) -> int:
        return sum(len(s) for s in self.domain_restrictions.values())

    def get_number_of_range_restrictions(self) -> int:
        return sum(len(s) for s in self.range_restrictions.values())

    def add_negated_equations(self, i: Individual, c: Concept) -> None:
        if c.type in (
            ConceptType.SOME,
            ConceptType.ALL,
            ConceptType.TOP,
            ConceptType.BOTTOM,
            ConceptType.HAS_VALUE,
        ) or OperatorConcept.is_not_has_value(c):
            self.rule_complemented(i, c)

    def is_concrete_type(self, c: Concept) -> bool:
        return (
            c.type in (ConceptType.CONCRETE, ConceptType.FUZZY_NUMBER)
            or OperatorConcept.is_not_concrete(c)
            or OperatorConcept.is_not_fuzzy_number(c)
        )

    def has_only_crisp_sub_concepts(self, c: Concept) -> bool:
        assert isinstance(c, HasConceptsInterface)

        for ci in c.concepts:
            if not self.is_atomic_crisp_concept(ci):
                return False
        return True

    def get_number_from_concept(self, concept_name: str) -> int:
        number: int = self.number_of_concepts.get(concept_name)
        if number is None:
            value: int = len(self.number_of_concepts)
            self.number_of_concepts[concept_name] = value
            return value
        return number

    def get_concept_from_number(self, n: int) -> typing.Optional[str]:
        for name, count in self.number_of_concepts.items():
            if count == n:
                return name
        return None

    def mark_process_assertion(self, ass: Assertion) -> None:
        n: int = self.milp.get_number_for_assertion(ass)
        Util.debug(f"Add assertion to processed_assertions: {n}")
        self.processed_assertions.add(n)

    def is_assertion_processed(self, ass: Assertion) -> None:
        return self.milp.get_number_for_assertion(ass) in self.processed_assertions

    def represent_tbox_with_gcis(self) -> None:
        for atomic_concept in self.t_synonyms:
            a: Concept = self.get_concept(atomic_concept)
            for b in self.t_synonyms.get(atomic_concept):
                self.t_G.append(
                    GeneralConceptInclusion(
                        self.get_concept(b),
                        a,
                        DegreeNumeric.get_one(),
                        LogicOperatorType.LUKASIEWICZ,
                    )
                )
        for atomic_concept in self.axioms_A_is_a_B:
            a: Concept = self.get_concept(atomic_concept)
            for pcd in self.axioms_A_is_a_B.get(atomic_concept):
                self.t_G.append(
                    GeneralConceptInclusion(
                        pcd.get_definition(),
                        a,
                        DegreeNumeric.get_degree(pcd.get_degree()),
                        pcd.get_type(),
                    )
                )
        for atomic_concept in self.axioms_A_equiv_C:
            a: Concept = self.get_concept(atomic_concept)
            for c in self.axioms_A_equiv_C.get(atomic_concept):
                self.t_G.append(
                    GeneralConceptInclusion(
                        a, c, DegreeNumeric.get_one(), LogicOperatorType.LUKASIEWICZ
                    )
                )
                self.t_G.append(
                    GeneralConceptInclusion(
                        c, a, DegreeNumeric.get_one(), LogicOperatorType.LUKASIEWICZ
                    )
                )
        for atomic_concept in self.axioms_A_is_a_C:
            a: Concept = self.get_concept(atomic_concept)
            for pcd in self.axioms_A_is_a_C.get(atomic_concept):
                self.t_G.append(
                    GeneralConceptInclusion(
                        pcd.get_definition(),
                        a,
                        DegreeNumeric.get_degree(pcd.get_degree()),
                        pcd.get_type(),
                    )
                )
        for ce in self.axioms_C_equiv_D:
            a: Concept = ce.get_c1()
            b: Concept = ce.get_c2()
            self.define_equivalent_concepts(a, b)
        for gcis in self.axioms_C_is_a_A.values():
            self.t_G.extend(list(gcis))
        for gcis in self.axioms_C_is_a_D.values():
            self.t_G.extend(list(gcis))
        for a in self.t_disjoints:
            for c in self.t_disjoints.get(a):
                self.t_G.append(
                    GeneralConceptInclusion(
                        TruthConcept.get_bottom(),
                        OperatorConcept.goedel_and(
                            self.get_concept(a), self.get_concept(c)
                        ),
                        DegreeNumeric.get_one(),
                        LogicOperatorType.LUKASIEWICZ,
                    )
                )
        for ind in self.individuals.values():
            for gci in self.t_G:
                self.solve_gci(ind, gci)
        self.solve_domain_and_range_axioms()

    def print_tbox(self) -> None:
        Util.debug(f"{constants.STAR_SEPARATOR}TBox{constants.STAR_SEPARATOR}")
        Util.debug("tInc:")
        for hs in self.t_inclusions.values():
            for pcd in hs:
                Util.debug(f"\t\t{pcd}")
        Util.debug("tDef:")
        for s, v in self.t_definitions.items():
            Util.debug(f"\t\t{s} = {v}")
        Util.debug("tSyn:")
        for s in self.t_synonyms:
            for syn in self.t_synonyms.get(s):
                if s < syn:
                    continue
                Util.debug(f"\t\t{s} = {syn}")
        Util.debug("tDomain Restriction:")
        for role in self.domain_restrictions:
            for c in self.domain_restrictions.get(role):
                Util.debug(f"\t\t(domain {role} {c})")
        Util.debug("tRange Restriction:")
        for role in self.range_restrictions:
            for c in self.range_restrictions.get(role):
                Util.debug(f"\t\t(range {role} {c})")
        Util.debug("tDisjoints:")
        for atomic_concept in self.t_disjoints:
            Util.debug(
                f"\t\t(disjoint {atomic_concept} {' '.join(disj_c for disj_c in self.t_disjoints.get(atomic_concept))})"
            )
        Util.debug("tG:")
        for gci in self.t_G:
            Util.debug(f"\t\t{gci}")
        Util.debug(f"{constants.STAR_SEPARATOR * 2}")


@class_debugging()
class DatatypeReasoner:

    @staticmethod
    def get_feature(f_name: str, kb: KnowledgeBase) -> ConcreteFeature:
        t = kb.concrete_features.get(f_name)
        if t is None:
            Util.error(f"Error: Concrete feature {f_name} is not defined")
        return t

    @staticmethod
    def get_bounds(t: ConcreteFeature) -> typing.Optional[list[float]]:
        if t.type == ConcreteFeatureType.BOOLEAN:
            return None
        if t.get_type() == ConcreteFeatureType.INTEGER:
            return [float(t.get_k1()), float(t.get_k2())]
        else:
            return [t.get_k1(), t.get_k2()]

    @staticmethod
    def get_created_individual_and_variables(
        ind: Individual,
        role: str,
        t: ConcreteFeature,
        k: list[float],
        kb: KnowledgeBase,
    ) -> list[typing.Any]:
        f_name: str = t.get_name()
        new_variable: bool = False
        if role in ind.role_relations:
            rel_set: list[Relation] = ind.role_relations[role]
            b: Individual = rel_set[0].get_object_individual()
            x_f: Variable = kb.milp.get_variable(ind, b, f_name, VariableType.BINARY)
        else:
            new_variable = True
            b: CreatedIndividual = kb.get_new_concrete_individual(ind, f_name)
            x_f: Variable = kb.milp.get_variable(ind, b, f_name, VariableType.BINARY)
            IndividualHandler.add_relation(
                ind, role, b, DegreeVariable.get_degree(x_f), kb
            )
        x_b: Variable = DatatypeReasoner.get_xb(b, t, kb)
        if new_variable and k is not None:
            kb.restrict_range(x_b, x_f, k[0], k[1])
        return [b, x_b, x_f]

    @staticmethod
    def rule_not_triangular_fuzzy_number(
        b: CreatedIndividual,
        kb: KnowledgeBase,
        f_name: str,
        x_b: Variable,
        x_f: Variable,
        x_is_c: Variable,
        n: TriangularFuzzyNumber,
        k: list[float],
        type: InequalityType,
    ) -> None:
        b_prime: CreatedIndividual = CreatedIndividualHandler.get_representative(
            b, RepresentativeIndividualType.GREATER_EQUAL, f_name, n, kb
        )
        x_b_prime: Variable = kb.milp.get_variable(b_prime, VariableType.CONTINUOUS)
        x_b_prime_is_f: Variable = kb.milp.get_variable(
            typing.cast(Individual, b_prime), n
        )

        # n.solve_assertion(b_prime, DegreeVariable.get_degree(x_b_prime_is_f), kb)
        kb.solve_concept_assertion(b_prime, n)

        x_is_f: Variable = kb.milp.get_variable(typing.cast(Individual, b_prime), n)

        DatatypeReasoner.write_not_fuzzy_number_equation(
            x_b, x_b_prime, x_b_prime_is_f, x_f, x_is_c, x_is_f, k, type, kb
        )

    @staticmethod
    def rule_triangular_fuzzy_number(
        b: CreatedIndividual,
        kb: KnowledgeBase,
        f_name: str,
        x_b: Variable,
        x_f: Variable,
        x_is_c: Variable,
        n: TriangularFuzzyNumber,
        type: InequalityType,
    ) -> None:
        b_prime: CreatedIndividual = CreatedIndividualHandler.get_representative(
            b, RepresentativeIndividualType.GREATER_EQUAL, f_name, n, kb
        )
        x_b_prime: Variable = kb.milp.get_variable(b_prime, VariableType.CONTINUOUS)
        x_b_prime_is_f = kb.milp.get_variable(typing.cast(Individual, b_prime), n)

        # n.solve_assertion(b_prime, DegreeVariable.get_degree(x_b_prime_is_f), kb)
        kb.solve_concept_assertion(b_prime, n)

        kb.milp.add_new_constraint(
            Expression(Term(1.0, x_is_c), Term(-1.0, x_b_prime_is_f)),
            InequalityType.LESS_THAN,
        )

        DatatypeReasoner.write_fuzzy_number_equation(x_f, x_b, x_b_prime, type, kb)

    @staticmethod
    def rule_feature_function(
        ind: Individual,
        t: ConcreteFeature,
        fun: FeatureFunction,
        kb: KnowledgeBase,
        x_b: Variable,
        x_is_c: Variable,
        x_f: Variable,
        k: list[float],
        type: InequalityType,
    ) -> None:
        # Gets fillers bi from every feature fi
        array: set[str] = fun.get_features()
        new_variable: bool = False
        for feature in array:
            ti: ConcreteFeature = DatatypeReasoner.get_feature(feature, kb)
            ki: list[float] = DatatypeReasoner.get_bounds(ti)
            if feature in ind.role_relations:
                rel_set: list[Relation] = ind.role_relations[feature]
                bi: CreatedIndividual = typing.cast(
                    CreatedIndividual, rel_set[0].get_object_individual()
                )
                x_fi: Variable = kb.milp.get_variable(
                    ind, bi, feature, VariableType.BINARY
                )
            else:
                new_variable = True
                bi: CreatedIndividual = kb.get_new_concrete_individual(ind, feature)
                x_fi: Variable = kb.milp.get_variable(
                    ind, bi, feature, VariableType.BINARY
                )
                # (a,bi):Fi >= x_{(a,bi):Fi}
                IndividualHandler.add_relation(
                    ind, feature, bi, DegreeVariable.get_degree(x_fi), kb
                )
            x_bi: Variable = kb.milp.get_variable(
                bi,
                (
                    VariableType.INTEGER
                    if t.get_type() == ConcreteFeatureType.INTEGER
                    else VariableType.CONTINUOUS
                ),
            )
            if new_variable and ki is not None:
                kb.restrict_range(x_bi, x_fi, ki[0], ki[1])
            # xIsC <= xFi
            kb.milp.add_new_constraint(
                Expression(Term(1.0, x_is_c), Term(-1.0, x_fi)),
                InequalityType.LESS_THAN,
            )
            # xF \in {0,1}
            x_fi.set_binary_variable()
            # xB is a datatype filler
            x_bi.set_datatype_filler_variable()
        DatatypeReasoner.write_feature_equation(ind, fun, x_b, x_is_c, x_f, k, type, kb)

    @staticmethod
    def write_fuzzy_number_equation(
        x_f: Variable,
        x_b: Variable,
        x_b_prime: Variable,
        type: InequalityType,
        kb: KnowledgeBase,
    ):
        if type == InequalityType.EQUAL:
            DatatypeReasoner.write_fuzzy_number_equation(
                x_f, x_b, x_b_prime, InequalityType.GREATER_THAN, kb
            )
            DatatypeReasoner.write_fuzzy_number_equation(
                x_f, x_b, x_b_prime, InequalityType.LESS_THAN, kb
            )
        elif type == InequalityType.GREATER_THAN:
            kb.milp.add_new_constraint(
                Expression(
                    constants.MAXVAL2,
                    Term(1.0, x_b),
                    Term(-1.0, x_b_prime),
                    Term(-constants.MAXVAL2, x_f),
                ),
                InequalityType.GREATER_THAN,
            )
            kb.milp.add_new_constraint(
                Expression(constants.MAXVAL, Term(1.0, x_b_prime)),
                InequalityType.GREATER_THAN,
            )
            kb.milp.add_new_constraint(
                Expression(constants.MAXVAL, Term(-1.0, x_b_prime)),
                InequalityType.GREATER_THAN,
            )
        elif type == InequalityType.LESS_THAN:
            kb.milp.add_new_constraint(
                Expression(
                    -constants.MAXVAL2,
                    Term(1.0, x_b),
                    Term(-1.0, x_b_prime),
                    Term(constants.MAXVAL2, x_f),
                ),
                InequalityType.LESS_THAN,
            )
            kb.milp.add_new_constraint(
                Expression(constants.MAXVAL, Term(1.0, x_b_prime)),
                InequalityType.GREATER_THAN,
            )
            kb.milp.add_new_constraint(
                Expression(constants.MAXVAL, Term(-1.0, x_b_prime)),
                InequalityType.GREATER_THAN,
            )

    @staticmethod
    def write_feature_equation(
        ind: Individual,
        fun: FeatureFunction,
        x_b: Variable,
        x_is_c: Variable,
        x_f: Variable,
        k: list[float],
        type: InequalityType,
        kb: KnowledgeBase,
    ):
        deg: DegreeExpression = DegreeExpression(fun.to_expression(ind, kb.milp))
        if type == InequalityType.EQUAL:
            DatatypeReasoner.write_feature_equation(
                ind, fun, x_b, x_is_c, x_f, k, InequalityType.GREATER_THAN, kb
            )
            DatatypeReasoner.write_feature_equation(
                ind, fun, x_b, x_is_c, x_f, k, InequalityType.LESS_THAN, kb
            )
        elif type == InequalityType.GREATER_THAN:
            kb.milp.add_new_constraint(
                Expression(
                    constants.MAXVAL2,
                    Term(1.0, x_b),
                    Term(-constants.MAXVAL2, x_f),
                ),
                InequalityType.GREATER_THAN,
                deg,
            )
            kb.milp.add_new_constraint(
                Expression(-constants.MAXVAL),
                InequalityType.LESS_THAN,
                deg,
            )
            kb.milp.add_new_constraint(
                Expression(constants.MAXVAL),
                InequalityType.GREATER_THAN,
                deg,
            )
        elif type == InequalityType.LESS_THAN:
            kb.milp.add_new_constraint(
                Expression(
                    -constants.MAXVAL2,
                    Term(1.0, x_b),
                    Term(constants.MAXVAL2, x_f),
                ),
                InequalityType.LESS_THAN,
                deg,
            )
            kb.milp.add_new_constraint(
                Expression(-constants.MAXVAL),
                InequalityType.LESS_THAN,
                deg,
            )
            kb.milp.add_new_constraint(
                Expression(constants.MAXVAL),
                InequalityType.GREATER_THAN,
                deg,
            )

    @staticmethod
    def rule_simple_restriction(
        n: typing.Any,
        kb: KnowledgeBase,
        x_b: Variable,
        x_is_c: Variable,
        x_f: Variable,
        k: list[float],
        type: InequalityType,
    ) -> None:
        if type == InequalityType.EQUAL:
            DatatypeReasoner.rule_simple_restriction(
                n, kb, x_b, x_is_c, x_f, k, InequalityType.GREATER_THAN
            )
            DatatypeReasoner.rule_simple_restriction(
                n, kb, x_b, x_is_c, x_f, k, InequalityType.LESS_THAN
            )
        elif type == InequalityType.GREATER_THAN:
            if isinstance(n, constants.NUMBER):
                kb.milp.add_new_constraint(
                    Expression(
                        constants.MAXVAL,
                        Term(1.0, x_b),
                        Term(-constants.MAXVAL, x_f),
                        Term(-n, x_f),
                    ),
                    InequalityType.GREATER_THAN,
                )
            elif isinstance(n, Variable):
                kb.milp.add_new_constraint(
                    Expression(
                        constants.MAXVAL2,
                        Term(-1.0, n),
                        Term(1.0, x_b),
                        Term(-constants.MAXVAL2, x_f),
                    ),
                    InequalityType.GREATER_THAN,
                )
                kb.milp.add_new_constraint(
                    Expression(constants.MAXVAL, Term(1.0, n)),
                    InequalityType.GREATER_THAN,
                )
                kb.milp.add_new_constraint(
                    Expression(constants.MAXVAL, Term(-1.0, n)),
                    InequalityType.GREATER_THAN,
                )
        elif type == InequalityType.LESS_THAN:
            if isinstance(n, constants.NUMBER):
                kb.milp.add_new_constraint(
                    Expression(
                        -constants.MAXVAL,
                        Term(1.0, x_b),
                        Term(constants.MAXVAL, x_f),
                        Term(-n, x_f),
                    ),
                    InequalityType.LESS_THAN,
                )
            elif isinstance(n, Variable):
                kb.milp.add_new_constraint(
                    Expression(
                        -constants.MAXVAL2,
                        Term(-1.0, n),
                        Term(1.0, x_b),
                        Term(constants.MAXVAL2, x_f),
                    ),
                    InequalityType.LESS_THAN,
                )
                kb.milp.add_new_constraint(
                    Expression(constants.MAXVAL, Term(1.0, n)),
                    InequalityType.GREATER_THAN,
                )
                kb.milp.add_new_constraint(
                    Expression(constants.MAXVAL, Term(-1.0, n)),
                    InequalityType.GREATER_THAN,
                )

    @staticmethod
    def apply_rule(ass: Assertion, kb: KnowledgeBase, type: InequalityType) -> None:
        a: Individual = ass.get_individual()
        c: Concept = ass.get_concept()

        assert isinstance(c, HasValueInterface)

        f_name: str = c.role
        t: ConcreteFeature = DatatypeReasoner.get_feature(f_name, kb)
        k: typing.Optional[list[float]] = DatatypeReasoner.get_bounds(t)
        return_value: list[typing.Any] = (
            DatatypeReasoner.get_created_individual_and_variables(a, f_name, t, k, kb)
        )
        b: CreatedIndividual = typing.cast(CreatedIndividual, return_value[0])
        x_b: Variable = typing.cast(Variable, return_value[1])
        x_f: Variable = typing.cast(Variable, return_value[2])
        x_is_c: Variable = kb.milp.get_variable(ass)
        kb.old_binary_variables += 1
        kb.milp.add_new_constraint(
            Expression(Term(1.0, x_is_c), Term(-1.0, x_f)), InequalityType.LESS_THAN
        )
        x_f.set_binary_variable()
        x_b.set_datatype_filler_variable()
        n: typing.Any = c.value
        if isinstance(n, TriangularFuzzyNumber):
            DatatypeReasoner.rule_triangular_fuzzy_number(
                b,
                kb,
                f_name,
                x_b,
                x_f,
                x_is_c,
                typing.cast(TriangularFuzzyNumber, n),
                type,
            )
        else:
            x_is_c.set_binary_variable()
            if isinstance(n, FeatureFunction):
                DatatypeReasoner.rule_feature_function(
                    a,
                    t,
                    typing.cast(FeatureFunction, n),
                    kb,
                    x_b,
                    x_is_c,
                    x_f,
                    k,
                    type,
                )
            elif t.get_type() == ConcreteFeatureType.BOOLEAN:
                x_b.set_binary_variable()
                value: int = 1 if n == True else 0
                kb.milp.add_new_constraint(
                    Expression(1.0 + value, Term(-1.0, x_b), Term(-1.0, x_f)),
                    InequalityType.GREATER_THAN,
                )
                kb.milp.add_new_constraint(
                    Expression(1.0 - value, Term(1.0, x_b), Term(-1.0, x_f)),
                    InequalityType.GREATER_THAN,
                )
            else:
                DatatypeReasoner.rule_simple_restriction(
                    n, kb, x_b, x_is_c, x_f, k, type
                )

    @staticmethod
    def apply_at_least_value_rule(ass: Assertion, kb: KnowledgeBase) -> None:
        DatatypeReasoner.apply_rule(ass, kb, InequalityType.GREATER_THAN)

    @staticmethod
    def apply_at_most_value_rule(ass: Assertion, kb: KnowledgeBase) -> None:
        DatatypeReasoner.apply_rule(ass, kb, InequalityType.LESS_THAN)

    @staticmethod
    def apply_exact_value_rule(ass: Assertion, kb: KnowledgeBase) -> None:
        DatatypeReasoner.apply_rule(ass, kb, InequalityType.EQUAL)

    @staticmethod
    def get_xb(b: CreatedIndividual, t: ConcreteFeature, kb: KnowledgeBase) -> Variable:
        if t.get_type() == ConcreteFeatureType.INTEGER:
            return kb.milp.get_variable(b, VariableType.INTEGER)
        return kb.milp.get_variable(b, VariableType.CONTINUOUS)

    @staticmethod
    def rule_not_simple_restriction(
        n: typing.Any,
        kb: KnowledgeBase,
        x_b: Variable,
        x_f: Variable,
        x_is_c: Variable,
        k: list[float],
        type: InequalityType,
    ) -> None:
        if type == InequalityType.GREATER_THAN:
            if isinstance(n, constants.NUMBER):
                # x_b <= (n - \epsilon) + (2 k_\infty + \epsilon) (1 - x_f) + (2k_\infty + \epsilon) x_is_c
                kb.milp.add_new_constraint(
                    Expression(
                        constants.MAXVAL2 + n,
                        Term(-1.0, x_b),
                        Term(-constants.MAXVAL2 - ConfigReader.EPSILON, x_f),
                        Term(constants.MAXVAL2 + ConfigReader.EPSILON, x_is_c),
                    ),
                    InequalityType.GREATER_THAN,
                )
            elif isinstance(n, Variable):
                # x_b <= x - \epsilon x_f + 2k_\infty (1 - x_f) + (2k_\infty + \epsilon) x_is_c
                kb.milp.add_new_constraint(
                    Expression(
                        constants.MAXVAL2,
                        Term(-1.0, x_b),
                        Term(1.0, n),
                        Term(-constants.MAXVAL2 - ConfigReader.EPSILON, x_f),
                        Term(constants.MAXVAL2 + ConfigReader.EPSILON, x_is_c),
                    ),
                    InequalityType.GREATER_THAN,
                )
                # x \geq -max_val
                kb.milp.add_new_constraint(
                    Expression(constants.MAXVAL, Term(1.0, n)),
                    InequalityType.GREATER_THAN,
                )
                # x \leq max_val
                kb.milp.add_new_constraint(
                    Expression(constants.MAXVAL, Term(-1.0, n)),
                    InequalityType.GREATER_THAN,
                )
        elif type == InequalityType.LESS_THAN:
            if isinstance(n, constants.NUMBER):
                # x_b >= (n + \epsilon) - (2 k_\infty + \epsilon) (1 - x_f) - (2k_\infty + \epsilon) x_is_c
                kb.milp.add_new_constraint(
                    Expression(
                        -constants.MAXVAL2 + n,
                        Term(-1.0, x_b),
                        Term(constants.MAXVAL2 + ConfigReader.EPSILON, x_f),
                        Term(-constants.MAXVAL2 - ConfigReader.EPSILON, x_is_c),
                    ),
                    InequalityType.LESS_THAN,
                )
            elif isinstance(n, Variable):
                # x_b >= x + \epsilon x_f - 2k_\infty (1 - x_f) - (2k_\infty + \epsilon) x_is_c
                kb.milp.add_new_constraint(
                    Expression(
                        -constants.MAXVAL2,
                        Term(-1.0, x_b),
                        Term(1.0, n),
                        Term(-constants.MAXVAL2 + ConfigReader.EPSILON, x_f),
                        Term(constants.MAXVAL2 + ConfigReader.EPSILON, x_is_c),
                    ),
                    InequalityType.LESS_THAN,
                )
                # x \geq -max_val
                kb.milp.add_new_constraint(
                    Expression(constants.MAXVAL, Term(1.0, n)),
                    InequalityType.GREATER_THAN,
                )
                # x \leq max_val
                kb.milp.add_new_constraint(
                    Expression(constants.MAXVAL, Term(-1.0, n)),
                    InequalityType.GREATER_THAN,
                )
        elif type == InequalityType.EQUAL:
            if isinstance(n, constants.NUMBER):
                # x_b <= (n - \epsilon) y + k_\infty (1 - y) + (2 k_\infty + \epsilon) (1 - x_f) + (2k_\infty + \epsilon) x_is_c
                y: Variable = kb.milp.get_new_variable(VariableType.BINARY)
                kb.milp.add_new_constraint(
                    Expression(
                        3 * constants.MAXVAL + ConfigReader.EPSILON,
                        Term(n - ConfigReader.EPSILON - constants.MAXVAL, y),
                        Term(-1.0, x_b),
                        Term(-constants.MAXVAL2 - ConfigReader.EPSILON, x_f),
                        Term(constants.MAXVAL2 + ConfigReader.EPSILON, x_is_c),
                    ),
                    InequalityType.GREATER_THAN,
                )
                # x_b >= (n + \epsilon) (1 - y) - k_\infty y - (2 k_\infty + \epsilon) (1 - x_f) - (2k_\infty + \epsilon) x_is_c
                kb.milp.add_new_constraint(
                    Expression(
                        -constants.MAXVAL2 + n,
                        Term(-1.0, x_b),
                        Term(constants.MAXVAL2 - n, y),
                        Term(constants.MAXVAL2 + ConfigReader.EPSILON, x_f),
                        Term(-constants.MAXVAL2 - ConfigReader.EPSILON, x_is_c),
                    ),
                    InequalityType.LESS_THAN,
                )
            elif isinstance(n, Variable):
                # x_b <= x - \epsilon x_f + (2k_\infty + \epsilon) (1 - y) + 2k_\infty (1 - x_f) + (2k_\infty + \epsilon) x_is_c
                y: Variable = kb.milp.get_new_variable(VariableType.BINARY)
                kb.milp.add_new_constraint(
                    Expression(
                        4 * constants.MAXVAL + ConfigReader.EPSILON,
                        Term(constants.MAXVAL + n + ConfigReader.EPSILON, y),
                        Term(-1.0, x_b),
                        Term(1.0, n),
                        Term(-constants.MAXVAL2 - ConfigReader.EPSILON, x_f),
                        Term(constants.MAXVAL2 + ConfigReader.EPSILON, x_is_c),
                    ),
                    InequalityType.GREATER_THAN,
                )
                # x_b >= x + \epsilon x_f - (2k_\infty + \epsilon) y - 2k_\infty (1 - x_f) - (2k_\infty + \epsilon) x_is_c
                kb.milp.add_new_constraint(
                    Expression(
                        -constants.MAXVAL2,
                        Term(-1.0, x_b),
                        Term(1.0, n),
                        Term(constants.MAXVAL2 + ConfigReader.EPSILON, y),
                        Term(constants.MAXVAL2 + ConfigReader.EPSILON, x_f),
                        Term(-constants.MAXVAL2 - ConfigReader.EPSILON, x_is_c),
                    ),
                    InequalityType.LESS_THAN,
                )
                # x \geq -maxval
                kb.milp.add_new_constraint(
                    Expression(constants.MAXVAL, Term(1.0, n)),
                    InequalityType.GREATER_THAN,
                )
                # x \leq maxval
                kb.milp.add_new_constraint(
                    Expression(constants.MAXVAL, Term(-1.0, n)),
                    InequalityType.GREATER_THAN,
                )

    @staticmethod
    def write_not_feature_equation(
        deg: DegreeExpression,
        x_b: Variable,
        x_f: Variable,
        x_is_c: Variable,
        k: list[float],
        type: InequalityType,
        kb: KnowledgeBase,
    ) -> None:
        kb.milp.add_new_constraint(
            Expression(-constants.MAXVAL), InequalityType.LESS_THAN, deg
        )
        kb.milp.add_new_constraint(
            Expression(constants.MAXVAL), InequalityType.GREATER_THAN, deg
        )
        if type == InequalityType.GREATER_THAN:
            kb.milp.add_new_constraint(
                Expression(
                    -constants.MAXVAL2,
                    Term(constants.MAXVAL2 + ConfigReader.EPSILON, x_f),
                    Term(-constants.MAXVAL2 - ConfigReader.EPSILON, x_is_c),
                    Term(1.0, x_b),
                ),
                InequalityType.LESS_THAN,
                deg,
            )
        elif type == InequalityType.LESS_THAN:
            kb.milp.add_new_constraint(
                Expression(
                    constants.MAXVAL2,
                    Term(-constants.MAXVAL2 - ConfigReader.EPSILON, x_f),
                    Term(constants.MAXVAL2 + ConfigReader.EPSILON, x_is_c),
                    Term(1.0, x_b),
                ),
                InequalityType.GREATER_THAN,
                deg,
            )
        elif type == InequalityType.EQUAL:
            y: Variable = kb.milp.get_new_variable(VariableType.BINARY)
            kb.milp.add_new_constraint(
                Expression(
                    -2 * constants.MAXVAL2 - ConfigReader.EPSILON,
                    Term(constants.MAXVAL2 + ConfigReader.EPSILON, x_f),
                    Term(constants.MAXVAL2 + ConfigReader.EPSILON, y),
                    Term(-constants.MAXVAL2 - ConfigReader.EPSILON, x_is_c),
                    Term(1.0, x_b),
                ),
                InequalityType.LESS_THAN,
                deg,
            )
            kb.milp.add_new_constraint(
                Expression(
                    constants.MAXVAL2,
                    Term(-constants.MAXVAL2 - ConfigReader.EPSILON, x_f),
                    Term(constants.MAXVAL2 + ConfigReader.EPSILON, y),
                    Term(constants.MAXVAL2 + ConfigReader.EPSILON, x_is_c),
                    Term(1.0, x_b),
                ),
                InequalityType.GREATER_THAN,
                deg,
            )

    @staticmethod
    def write_not_fuzzy_number_equation(
        x_b: Variable,
        x_b_prime: Variable,
        x_b_prime_is_f: Variable,
        x_f: Variable,
        x_is_c: Variable,
        x_is_f: Variable,
        k: list[float],
        type: InequalityType,
        kb: KnowledgeBase,
    ) -> None:
        y1: Variable = kb.milp.get_new_variable(VariableType.BINARY)
        y2: Variable = kb.milp.get_new_variable(VariableType.BINARY)
        if type == InequalityType.GREATER_THAN:
            DatatypeReasoner.geq_equation(y1, x_b_prime, x_b, kb.milp)
            DatatypeReasoner.geq_equation(y2, x_b_prime_is_f, x_is_c, kb.milp)
            kb.milp.add_new_constraint(
                Expression(-2.0, Term(1.0, x_f), Term(1.0, y1), Term(1.0, y2)),
                InequalityType.LESS_THAN,
            )
        elif type == InequalityType.LESS_THAN:
            DatatypeReasoner.geq_equation(y1, x_b, x_b_prime, kb.milp)
            DatatypeReasoner.geq_equation(y2, x_b_prime_is_f, x_is_c, kb.milp)
            kb.milp.add_new_constraint(
                Expression(-2.0, Term(1.0, x_f), Term(1.0, y1), Term(1.0, y2)),
                InequalityType.LESS_THAN,
            )
        elif type == InequalityType.EQUAL:
            y3: Variable = kb.milp.get_new_variable(VariableType.BINARY)
            y4: Variable = kb.milp.get_new_variable(VariableType.BINARY)
            DatatypeReasoner.geq_equation(y1, x_b_prime, x_b, kb.milp)
            DatatypeReasoner.geq_equation(y2, x_b_prime_is_f, x_is_c, kb.milp)
            DatatypeReasoner.geq_equation(y3, x_b, x_b_prime, kb.milp)
            kb.milp.add_new_constraint(
                Expression(
                    -2.0,
                    Term(1.0, x_f),
                    Term(1.0, y1),
                    Term(1.0, y2),
                    Term(-1.0, y4),
                ),
                InequalityType.LESS_THAN,
            )
            kb.milp.add_new_constraint(
                Expression(
                    -3.0,
                    Term(1.0, x_f),
                    Term(1.0, y3),
                    Term(1.0, y2),
                    Term(1.0, y4),
                ),
                InequalityType.LESS_THAN,
            )

    @staticmethod
    def geq_equation(y: Variable, x1: Variable, x2: Variable, milp: MILPHelper) -> None:
        z: Variable = milp.get_new_variable(VariableType.CONTINUOUS)
        milp.add_new_constraint(
            Expression(constants.MAXVAL, Term(1.0, z)),
            InequalityType.GREATER_THAN,
        )
        milp.add_new_constraint(
            Expression(constants.MAXVAL, Term(-1.0, z)),
            InequalityType.GREATER_THAN,
        )
        milp.add_new_constraint(
            Expression(Term(1.0, z), Term(-1.0, x1), Term(1.0, x2)),
            InequalityType.GREATER_THAN,
        )
        milp.add_new_constraint(
            Expression(Term(1.0, z), Term(-1.0, x1), Term(1.0, x2)),
            InequalityType.LESS_THAN,
        )
        milp.add_new_constraint(
            Expression(
                constants.MAXVAL,
                Term(1.0, z),
                Term(-constants.MAXVAL - ConfigReader.EPSILON, y),
            ),
            InequalityType.GREATER_THAN,
        )
        milp.add_new_constraint(
            Expression(
                Term(1.0, z),
                Term(-constants.MAXVAL, y),
            ),
            InequalityType.LESS_THAN,
        )

    @staticmethod
    def apply_not_rule(
        b: CreatedIndividual, ass: Assertion, kb: KnowledgeBase, type: InequalityType
    ) -> None:
        a: Individual = ass.get_individual()
        not_c: Concept = ass.get_concept()
        assert isinstance(not_c, OperatorConcept)
        c: Concept = not_c.get_atom()
        assert isinstance(c, HasValueInterface)

        f_name: str = c.role
        t: ConcreteFeature = DatatypeReasoner.get_feature(f_name, kb)
        k: typing.Optional[list[float]] = DatatypeReasoner.get_bounds(t)
        return_value: list[typing.Any] = (
            DatatypeReasoner.get_created_individual_and_variables(a, f_name, t, k, kb)
        )
        x_f: Variable = typing.cast(Variable, return_value[2])
        x_is_not_c: Variable = kb.milp.get_variable(ass)
        kb.old_binary_variables += 1
        x_f.set_binary_variable()
        x_b: Variable = DatatypeReasoner.get_xb(b, t, kb)
        # c: Concept = -not_c
        x_is_c: Variable = kb.milp.get_variable(a, c)
        x_b.set_datatype_filler_variable()
        kb.milp.add_new_constraint(
            Expression(1.0, Term(-1.0, x_is_c), Term(-1.0, x_is_not_c)),
            InequalityType.EQUAL,
        )
        n: typing.Any = c.value
        if isinstance(n, TriangularFuzzyNumber):
            if type == InequalityType.EQUAL:
                kb.old_binary_variables += 3
            else:
                kb.old_binary_variables += 4
            DatatypeReasoner.rule_not_triangular_fuzzy_number(
                b,
                kb,
                f_name,
                x_b,
                x_f,
                x_is_c,
                typing.cast(TriangularFuzzyNumber, n),
                k,
                type,
            )
        else:
            if type == InequalityType.EQUAL:
                kb.old_binary_variables += 3
            else:
                kb.old_binary_variables += 2
            x_is_not_c.set_binary_variable()
            x_is_c.set_binary_variable()
            if isinstance(n, FeatureFunction):
                # If n is a FeatureFunction, check that there exist fillers
                fun: FeatureFunction = typing.cast(FeatureFunction, n)
                array: set[str] = fun.get_features()
                for feature in array:
                    if a.role_relations.get(feature) is None:
                        Util.debug(f"No fillers for feature {feature}")
                        return
                deg: DegreeExpression = DegreeExpression(fun.to_expression(a, kb.milp))
                DatatypeReasoner.write_not_feature_equation(
                    deg, x_b, x_f, x_is_c, k, type, kb
                )
            elif t.get_type() == ConcreteFeatureType.BOOLEAN:
                value: int = 0 if n == True else 1
                kb.milp.add_new_constraint(
                    Expression(
                        1.0 + value,
                        Term(-1.0, x_b),
                        Term(-1.0, x_f),
                        Term(1.0, x_is_c),
                    ),
                    InequalityType.GREATER_THAN,
                )
                kb.milp.add_new_constraint(
                    Expression(
                        1.0 - value,
                        Term(1.0, x_b),
                        Term(-1.0, x_f),
                        Term(1.0, x_is_c),
                    ),
                    InequalityType.GREATER_THAN,
                )
            else:
                DatatypeReasoner.rule_not_simple_restriction(
                    n, kb, x_b, x_f, x_is_c, k, type
                )

    @staticmethod
    def apply_not_at_least_value_rule(
        b: CreatedIndividual, ass: Assertion, kb: KnowledgeBase
    ) -> None:
        DatatypeReasoner.apply_not_rule(b, ass, kb, InequalityType.GREATER_THAN)

    @staticmethod
    def apply_not_at_most_value_rule(
        b: CreatedIndividual, ass: Assertion, kb: KnowledgeBase
    ) -> None:
        DatatypeReasoner.apply_not_rule(b, ass, kb, InequalityType.LESS_THAN)

    @staticmethod
    def apply_not_exact_value_rule(
        b: CreatedIndividual, ass: Assertion, kb: KnowledgeBase
    ) -> None:
        DatatypeReasoner.apply_not_rule(b, ass, kb, InequalityType.EQUAL)


@class_debugging()
class LukasiewiczSolver:
    @staticmethod
    def solve_and(ass: Assertion, kb: KnowledgeBase) -> None:
        c: Concept = ass.get_concept()

        assert isinstance(c, HasConceptsInterface)

        ind: Individual = ass.get_individual()
        x_ass: Variable = kb.milp.get_variable(ass)
        kb.old_01_variables += 2 * len(c.concepts) - 1
        kb.old_binary_variables += len(c.concepts) - 1

        v: list[Variable] = []
        for ci in c.concepts:
            var: Variable = kb.milp.get_variable(ind, ci)
            kb.add_assertion(ind, ci, DegreeVariable.get_degree(var))
            v.append(var)
        LukasiewiczSolver.and_equation(v, x_ass, kb.milp)

    @staticmethod
    def solve_or(ass: Assertion, kb: KnowledgeBase) -> None:
        c: Concept = ass.get_concept()

        assert isinstance(c, HasConceptsInterface)

        ind: Individual = ass.get_individual()
        x_ass: Variable = kb.milp.get_variable(ass)

        v: list[Variable] = []
        for ci in c.concepts:
            var: Variable = kb.milp.get_variable(ind, ci)
            kb.add_assertion(ind, ci, DegreeVariable.get_degree(var))
            v.append(var)
        LukasiewiczSolver.or_equation(v, x_ass, kb.milp)

    @staticmethod
    def solve_some(ass: Assertion, kb: KnowledgeBase) -> None:
        a: Individual = ass.get_individual()
        concept: AllSomeConcept = typing.cast(AllSomeConcept, ass.get_concept())
        role: str = concept.role
        c: Concept = concept.curr_concept
        kb.rules_applied[KnowledgeBaseRules.RULE_LUKASIEWICZ_SOME] += 1

        kb.old_01_variables += 2
        kb.old_binary_variables += 1

        if role in kb.functional_roles and role in a.role_relations:
            b: Individual = a.role_relations[role][0].get_object_individual()
        elif kb.is_concrete_type(c):
            b: Individual = kb.get_new_concrete_individual(a, role)
        else:
            b: Individual = kb.get_new_individual(a, role)

        r_var: Variable = kb.milp.get_variable(a, b, role)
        c_var: Variable = kb.milp.get_variable(b, c)

        kb.add_assertion(b, c, DegreeVariable.get_degree(c_var))

        r: Relation = IndividualHandler.add_relation(
            a, role, b, DegreeVariable.get_degree(r_var), kb
        )
        x_ass: Variable = kb.milp.get_variable(ass)
        LukasiewiczSolver.and_leq_equation(x_ass, c_var, r_var, kb.milp)

        kb.solve_role_inclusion_axioms(a, r)

        list_inverse_roles: list[str] = kb.inverse_roles.get(ass.get_concept().role, [])
        for inv_role in list_inverse_roles:
            var: Variable = kb.milp.get_variable(b, ass.get_individual(), inv_role)
            IndividualHandler.add_relation(
                b, inv_role, ass.get_individual(), DegreeVariable.get_degree(var), kb
            )
            kb.milp.add_new_constraint(
                Expression(Term(1.0, r_var), Term(-1.0, var)), InequalityType.EQUAL
            )
            kb.solve_role_inclusion_axioms(b, r)

    @staticmethod
    def solve_all(rel: Relation, restrict: Restriction, kb: KnowledgeBase) -> None:
        if not rel.get_degree().is_numeric() or not restrict.get_degree().is_numeric():
            kb.old_01_variables += 1

        a: Individual = rel.get_subject_individual()
        b: Individual = rel.get_object_individual()

        if isinstance(restrict, HasValueRestriction):
            x_bin_c: Variable = kb.milp.get_negated_nominal_variable(
                str(b), restrict.get_individual()
            )
            kb.rules_applied[KnowledgeBaseRules.RULE_NOT_HAS_VALUE] += 1
        else:
            c: Concept = restrict.get_concept()
            x_bin_c: Variable = kb.milp.get_variable(b, c)
            kb.add_assertion(b, c, DegreeVariable.get_degree(x_bin_c))
            kb.rules_applied[KnowledgeBaseRules.RULE_LUKASIEWICZ_ALL] += 1

        x_rel: Variable = kb.milp.get_variable(rel)
        x_for_all: Variable = kb.milp.get_variable(a, restrict)

        if (
            restrict.get_role_name() in kb.transitive_roles
            and not kb.check_trans_role_applied(rel, restrict)
        ):
            if isinstance(restrict, HasValueRestriction):
                for_all: Concept = -HasValueConcept(
                    restrict.get_role_name(), restrict.get_individual()
                )
            else:
                for_all: Concept = AllSomeConcept.all(
                    restrict.get_role_name(), restrict.get_concept()
                )
            x_for_all_b: Variable = kb.milp.get_variable(b, for_all)
            kb.add_assertion(b, for_all, DegreeVariable.get_degree(x_for_all_b))
            LukasiewiczSolver.and_geq_equation(x_for_all_b, x_for_all, x_rel, kb.milp)

        if (
            restrict.get_role_name() in kb.roles_with_trans_children
            and not kb.check_trans_role_applied(rel, restrict)
        ):
            trans_children: list[str] = kb.roles_with_trans_children[
                restrict.get_role_name()
            ]
            for tc in trans_children:
                n: float = kb.get_inclusion_degree(tc, restrict.get_role_name())
                if isinstance(restrict, HasValueRestriction):
                    all_concept: Concept = -HasValueConcept(
                        tc, restrict.get_individual()
                    )
                else:
                    all_concept: Concept = AllSomeConcept.all(
                        tc, restrict.get_concept()
                    )
                if n != 1.0:
                    kb.old_01_variables += 1
                    x_b_all_c: Variable = kb.milp.get_variable(b, all_concept)
                    kb.add_assertion(
                        b,
                        AllSomeConcept.all(tc, all_concept),
                        DegreeVariable.get_degree(x_b_all_c),
                    )
                    kb.milp.add_new_constraint(
                        Expression(
                            2.0 - n,
                            Term(1.0, x_b_all_c),
                            Term(-1.0, x_rel),
                            Term(-1.0, x_for_all),
                        ),
                        InequalityType.GREATER_THAN,
                    )
                else:
                    kb.add_assertion(
                        b, all_concept, DegreeVariable.get_degree(x_for_all)
                    )

        LukasiewiczSolver.and_geq_equation(x_bin_c, x_rel, x_for_all, kb.milp)

    @typing.overload
    @staticmethod
    def and_equation(x: list[Variable], z: Variable, milp: MILPHelper) -> None: ...

    @typing.overload
    @staticmethod
    def and_equation(
        z: Variable, x1: Variable, x2: float, milp: MILPHelper
    ) -> None: ...

    @typing.overload
    @staticmethod
    def and_equation(
        z: Variable, x1: Variable, x2: Variable, milp: MILPHelper
    ) -> None: ...

    @staticmethod
    def and_equation(*args) -> None:
        assert len(args) in [3, 4]
        if len(args) == 3:
            assert isinstance(args[0], typing.Sequence) and all(
                isinstance(a, Variable) for a in args[0]
            )
            assert isinstance(args[1], Variable)
            assert isinstance(args[2], MILPHelper)
            LukasiewiczSolver.__and_equation_1(*args)
        else:
            assert isinstance(args[0], Variable)
            assert isinstance(args[1], Variable)
            if isinstance(args[2], constants.NUMBER):
                assert isinstance(args[3], MILPHelper)
                LukasiewiczSolver.__and_equation_2(*args)
            elif isinstance(args[2], Variable):
                assert isinstance(args[3], MILPHelper)
                LukasiewiczSolver.__and_equation_3(*args)
            else:
                raise ValueError

    @staticmethod
    def __and_equation_1(x: list[Variable], z: Variable, milp: MILPHelper) -> None:
        y: Variable = milp.get_new_variable(VariableType.BINARY)
        N: int = len(x)
        exp: Expression = Expression(x)
        exp.add_term(Term(-1.0, z))
        exp.set_constant(1.0 - N)
        milp.add_new_constraint(exp, InequalityType.LESS_THAN)
        milp.add_new_constraint(
            Expression(1.0, Term(-1.0, z), Term(-1.0, y)),
            InequalityType.GREATER_THAN,
        )
        exp2: Expression = Expression(exp)
        exp2.add_term(Term(N - 1.0, y))
        milp.add_new_constraint(exp2, InequalityType.GREATER_THAN)

    @staticmethod
    def __and_equation_2(
        z: Variable, x1: Variable, x2: float, milp: MILPHelper
    ) -> None:
        y: Variable = milp.get_new_variable(VariableType.BINARY)
        milp.add_new_constraint(
            Expression(1.0 - x2, Term(-1.0, x1), Term(1.0, z)),
            InequalityType.GREATER_THAN,
        )
        milp.add_new_constraint(
            Expression(1.0 - x2, Term(-1.0, x1), Term(1.0, z), Term(-1.0, y)),
            InequalityType.LESS_THAN,
        )
        milp.add_new_constraint(
            Expression(-1.0, Term(1.0, z), Term(1.0, y)),
            InequalityType.LESS_THAN,
        )

    @staticmethod
    def __and_equation_3(
        z: Variable, x1: Variable, x2: Variable, milp: MILPHelper
    ) -> None:
        y: Variable = milp.get_new_variable(VariableType.BINARY)
        milp.add_new_constraint(
            Expression(1.0, Term(-1.0, x1), Term(-1.0, x2), Term(1.0, z)),
            InequalityType.GREATER_THAN,
        )
        milp.add_new_constraint(
            Expression(
                1.0,
                Term(-1.0, x1),
                Term(-1.0, x2),
                Term(1.0, z),
                Term(-1.0, y),
            ),
            InequalityType.LESS_THAN,
        )
        milp.add_new_constraint(
            Expression(-1.0, Term(1.0, z), Term(1.0, y)),
            InequalityType.LESS_THAN,
        )

    @staticmethod
    def and_leq_equation(
        z: Variable, x1: Variable, x2: Variable, milp: MILPHelper
    ) -> None:
        y: Variable = milp.get_new_variable(VariableType.BINARY)
        milp.add_new_constraint(
            Expression(1.0, Term(-1.0, z), Term(-1.0, y)),
            InequalityType.GREATER_THAN,
        )
        milp.add_new_constraint(
            Expression(-1.0, Term(1.0, x1), Term(1.0, x2), Term(-1.0, z), Term(1.0, y)),
            InequalityType.GREATER_THAN,
        )

    @typing.overload
    @staticmethod
    def and_geq_equation(
        z: Variable, x1: Variable, x2: Variable, milp: MILPHelper
    ) -> None: ...

    @typing.overload
    @staticmethod
    def and_geq_equation(
        z: Variable, x1: Variable, x2: float, milp: MILPHelper
    ) -> None: ...

    @staticmethod
    def and_geq_equation(*args) -> None:
        assert len(args) == 4
        assert isinstance(args[0], Variable)
        assert isinstance(args[1], Variable)
        assert isinstance(args[3], MILPHelper)
        if isinstance(args[2], Variable):
            LukasiewiczSolver.__and_geq_equation_1(*args)
        elif isinstance(args[2], constants.NUMBER):
            LukasiewiczSolver.__and_geq_equation_2(*args)
        else:
            raise ValueError

    @staticmethod
    def __and_geq_equation_1(
        z: Variable, x1: Variable, x2: Variable, milp: MILPHelper
    ) -> None:
        milp.add_new_constraint(
            Expression(-1.0, Term(-1.0, z), Term(1.0, x1), Term(1.0, x2)),
            InequalityType.LESS_THAN,
        )

    @staticmethod
    def __and_geq_equation_2(
        z: Variable, x1: Variable, x2: float, milp: MILPHelper
    ) -> None:
        milp.add_new_constraint(
            Expression(-1.0 + x2, Term(-1.0, z), Term(1.0, x1)),
            InequalityType.LESS_THAN,
        )

    @staticmethod
    def or_equation(x: list[Variable], z: Variable, milp: MILPHelper) -> None:
        y: Variable = milp.get_new_variable(VariableType.BINARY)
        N: int = len(x)

        exp: Expression = Expression(x)
        exp.add_term(Term(-1.0, z))
        milp.add_new_constraint(exp, InequalityType.GREATER_THAN)
        milp.add_new_constraint(
            Expression(Term(1.0, y), Term(-1.0, z)), InequalityType.LESS_THAN
        )

        exp2: Expression = Expression(exp)
        exp2.add_term(Term(1.0 - N, y))
        milp.add_new_constraint(exp2, InequalityType.LESS_THAN)


@class_debugging()
class ZadehSolver:

    @staticmethod
    def solve_and(ass: Assertion, kb: KnowledgeBase) -> None:
        c: Concept = ass.get_concept()
        assert isinstance(c, HasConceptsInterface)

        ind: Individual = ass.get_individual()
        x_ass: Variable = kb.milp.get_variable(ass)
        v: list[Variable] = []
        for ci in c.concepts:
            var: Variable = kb.milp.get_variable(ind, ci)
            kb.add_assertion(ind, ci, DegreeVariable.get_degree(var))
            v.append(var)
        ZadehSolver.and_equation(v, x_ass, kb.milp)

    @typing.overload
    @staticmethod
    def and_equation(x: list[Variable], z: Variable, milp: MILPHelper) -> None: ...

    @typing.overload
    @staticmethod
    def and_equation(x: list[Variable], t: Term, milp: MILPHelper) -> None: ...

    @typing.overload
    @staticmethod
    def and_equation(
        z: Variable, x1: Variable, x2: float, milp: MILPHelper
    ) -> None: ...

    @typing.overload
    @staticmethod
    def and_equation(
        z: Variable, x1: Variable, x2: Variable, milp: MILPHelper
    ) -> None: ...

    @typing.overload
    @staticmethod
    def and_equation(x1: Variable, x2: Variable, milp: MILPHelper) -> None: ...

    @staticmethod
    def and_equation(*args) -> None:
        assert len(args) in [3, 4]
        if len(args) == 3:
            assert isinstance(args[2], MILPHelper)
            if isinstance(args[0], list) and all(
                isinstance(a, Variable) for a in args[0]
            ):
                if isinstance(args[1], Variable):
                    ZadehSolver.__and_equation_1(*args)
                elif isinstance(args[1], Term):
                    ZadehSolver.__and_equation_2(*args)
                else:
                    raise ValueError
            elif isinstance(args[0], Variable) and isinstance(args[1], Variable):
                ZadehSolver.__and_equation_5(*args)
            else:
                raise ValueError
        else:
            assert isinstance(args[0], Variable)
            assert isinstance(args[1], Variable)
            assert isinstance(args[3], MILPHelper)
            if isinstance(args[2], Variable):
                ZadehSolver.__and_equation_4(*args)
            elif isinstance(args[2], constants.NUMBER):
                ZadehSolver.__and_equation_3(*args)
            else:
                raise ValueError

    @staticmethod
    def __and_equation_1(x: list[Variable], z: Variable, milp: MILPHelper) -> None:
        ZadehSolver.and_equation(x, Term(1.0, z), milp)

    @staticmethod
    def __and_equation_2(x: list[Variable], t: Term, milp: MILPHelper) -> None:
        N: int = len(x)
        M: float = Util.log2(N)
        for xi in x:
            milp.add_new_constraint(
                Expression(t, Term(-1.0, xi)), InequalityType.LESS_THAN
            )
        y: list[Variable] = [
            milp.get_new_variable(VariableType.BINARY) for _ in range(M)
        ]
        for i, xi in enumerate(x):
            dividendo: int = i
            exp: Expression = Expression(t, Term(-1.0, xi))
            for n in range(M):
                if (dividendo % 2) == 0:
                    exp.add_term(Term(1.0, y[n]))
                else:
                    exp.add_term(Term(-1.0, y[n]))
                    exp.increment_constant()
                dividendo //= 2
            milp.add_new_constraint(exp, InequalityType.GREATER_THAN)

        exp2: Expression = Expression(1.0 - N)
        k: float = 1.0
        for m in range(M):
            exp2.add_term(Term(k, y[m]))
            k *= 2.0
        milp.add_new_constraint(exp2, InequalityType.LESS_THAN)

    @staticmethod
    def __and_equation_3(
        z: Variable, x1: Variable, x2: float, milp: MILPHelper
    ) -> None:
        y: Variable = milp.get_new_variable(VariableType.BINARY)
        milp.add_new_constraint(
            Expression(Term(1.0, z), Term(-1.0, x1)), InequalityType.LESS_THAN
        )
        milp.add_new_constraint(Expression(Term(1.0, z)), InequalityType.LESS_THAN, x2)
        milp.add_new_constraint(
            Expression(Term(1.0, x1), Term(-1.0, z), Term(-1.0, y)),
            InequalityType.LESS_THAN,
        )
        milp.add_new_constraint(
            Expression(-1.0 + x2, Term(-1.0, z), Term(1.0, y)),
            InequalityType.LESS_THAN,
        )

    @staticmethod
    def __and_equation_4(
        z: Variable, x1: Variable, x2: Variable, milp: MILPHelper
    ) -> None:
        y: Variable = milp.get_new_variable(VariableType.BINARY)
        milp.add_new_constraint(
            Expression(Term(1.0, z), Term(-1.0, x1)), InequalityType.LESS_THAN
        )
        milp.add_new_constraint(
            Expression(Term(1.0, z), Term(-1.0, x2)), InequalityType.LESS_THAN
        )
        milp.add_new_constraint(
            Expression(Term(1.0, x1), Term(-1.0, z), Term(-1.0, y)),
            InequalityType.LESS_THAN,
        )
        milp.add_new_constraint(
            Expression(-1.0, Term(1.0, x2), Term(-1.0, z), Term(1.0, y)),
            InequalityType.LESS_THAN,
        )

    @staticmethod
    def __and_equation_5(x1: Variable, x2: Variable, milp: MILPHelper) -> None:
        y: Variable = milp.get_new_variable(VariableType.BINARY)
        milp.add_new_constraint(
            Expression(Term(-1.0, y), Term(1.0, x1)), InequalityType.LESS_THAN
        )
        milp.add_new_constraint(
            Expression(1.0, Term(-1.0, y), Term(-1.0, x2)),
            InequalityType.GREATER_THAN,
        )

    @staticmethod
    def and_negated_equation(
        z: Variable, x1: Variable, x2: float, milp: MILPHelper
    ) -> None:
        y: Variable = milp.get_new_variable(VariableType.BINARY)
        milp.add_new_constraint(
            Expression(-1.0, Term(1.0, z), Term(1.0, x1)),
            InequalityType.LESS_THAN,
        )
        milp.add_new_constraint(Expression(Term(1.0, z)), InequalityType.LESS_THAN, x2)
        milp.add_new_constraint(
            Expression(1.0, Term(-1.0, x1), Term(-1.0, z), Term(-1.0, y)),
            InequalityType.LESS_THAN,
        )
        milp.add_new_constraint(
            Expression(-1.0 + x2, Term(-1.0, z), Term(1.0, y)),
            InequalityType.LESS_THAN,
        )

    @staticmethod
    def and_leq_equation(
        z: Variable, x1: Variable, x2: Variable, milp: MILPHelper
    ) -> None:
        milp.add_new_constraint(
            Expression(Term(-1.0, x1), Term(1.0, z)), InequalityType.LESS_THAN
        )
        milp.add_new_constraint(
            Expression(Term(-1.0, x2), Term(1.0, z)), InequalityType.LESS_THAN
        )

    @typing.overload
    @staticmethod
    def and_geq_equation(
        z: Variable, x1: Variable, x2: Variable, milp: MILPHelper
    ) -> None: ...

    @typing.overload
    @staticmethod
    def and_geq_equation(
        z: Variable, x1: Variable, x2: float, milp: MILPHelper
    ) -> None: ...

    @staticmethod
    def and_geq_equation(*args) -> None:
        assert len(args) == 4
        assert isinstance(args[0], Variable)
        assert isinstance(args[1], Variable)
        assert isinstance(args[3], MILPHelper)
        if isinstance(args[2], Variable):
            ZadehSolver.__and_geq_equation_1(*args)
        elif isinstance(args[2], constants.NUMBER):
            ZadehSolver.__and_geq_equation_2(*args)
        else:
            raise ValueError

    @staticmethod
    def __and_geq_equation_1(
        z: Variable, x1: Variable, x2: Variable, milp: MILPHelper
    ) -> None:
        y: Variable = milp.get_new_variable(VariableType.BINARY)
        milp.add_new_constraint(
            Expression(Term(1.0, y), Term(1.0, z), Term(-1.0, x1)),
            InequalityType.GREATER_THAN,
        )
        milp.add_new_constraint(
            Expression(1.0, Term(-1.0, y), Term(1.0, z), Term(-1.0, x2)),
            InequalityType.GREATER_THAN,
        )

    @staticmethod
    def __and_geq_equation_2(
        z: Variable, x1: Variable, x2: float, milp: MILPHelper
    ) -> None:
        y: Variable = milp.get_new_variable(VariableType.BINARY)
        milp.add_new_constraint(
            Expression(Term(1.0, y), Term(1.0, z), Term(-1.0, x1)),
            InequalityType.GREATER_THAN,
        )
        milp.add_new_constraint(
            Expression(1.0, Term(-1.0, y), Term(1.0, z)),
            InequalityType.GREATER_THAN,
            x2,
        )

    @staticmethod
    def solve_or(ass: Assertion, kb: KnowledgeBase) -> None:
        c: Concept = ass.get_concept()
        assert isinstance(c, HasConceptsInterface)

        ind: Individual = ass.get_individual()
        x_ass: Variable = kb.milp.get_variable(ass)
        kb.old_01_variables += 2 * len(c.concepts) - 1
        kb.old_binary_variables += len(c.concepts) - 1
        v: list[Variable] = []
        for ci in c.concepts:
            var: Variable = kb.milp.get_variable(ind, ci)
            kb.add_assertion(ind, ci, DegreeVariable.get_degree(var))
            v.append(var)
        ZadehSolver.or_equation(v, x_ass, kb.milp)

    @staticmethod
    def solve_some(ass: Assertion, kb: KnowledgeBase) -> None:
        a: Individual = ass.get_individual()
        concept: AllSomeConcept = typing.cast(AllSomeConcept, ass.get_concept())
        role: str = concept.role
        c: Concept = concept.curr_concept
        kb.rules_applied[KnowledgeBaseRules.RULE_GOEDEL_SOME] += 1

        if role in kb.functional_roles and role in a.role_relations:
            rel_set: list[Relation] = a.role_relations[role]
            b: Individual = rel_set[0].get_object_individual()
        elif kb.is_concrete_type(c):
            b: Individual = kb.get_new_concrete_individual(a, role)
        else:
            b: Individual = kb.get_new_individual(a, role)

        r_var: Variable = kb.milp.get_variable(a, b, role)
        c_var: Variable = kb.milp.get_variable(b, c)
        kb.add_assertion(b, c, DegreeVariable.get_degree(c_var))
        r: Relation = IndividualHandler.add_relation(
            a, role, b, DegreeVariable.get_degree(r_var), kb
        )
        x_ass: Variable = kb.milp.get_variable(ass)
        ZadehSolver.and_leq_equation(x_ass, c_var, r_var, kb.milp)
        kb.solve_role_inclusion_axioms(a, r)
        list_inverse_roles: list[str] = kb.inverse_roles.get(concept.role, [])
        for inv_role in list_inverse_roles:
            IndividualHandler.add_relation(
                b, inv_role, ass.get_individual(), DegreeVariable.get_degree(r_var), kb
            )
            kb.solve_role_inclusion_axioms(b, r)

    @staticmethod
    def solve_all(rel: Relation, restrict: Restriction, kb: KnowledgeBase) -> None:
        if not rel.get_degree().is_numeric() or not restrict.get_degree().is_numeric():
            kb.old_01_variables += 1

        b: Individual = rel.get_object_individual()
        if isinstance(restrict, HasValueRestriction):
            x_B_in_C: Variable = kb.milp.get_negated_nominal_variable(
                str(b), restrict.get_individual()
            )
            kb.rules_applied[KnowledgeBaseRules.RULE_NOT_HAS_VALUE] += 1
        else:
            c: Concept = restrict.get_concept()
            x_B_in_C: Variable = kb.milp.get_variable(b, c)
            kb.add_assertion(b, c, DegreeVariable.get_degree(x_B_in_C))
            kb.rules_applied[KnowledgeBaseRules.RULE_GOEDEL_ALL] += 1

        if (
            restrict.get_role_name() in kb.transitive_roles
            and not kb.check_trans_role_applied(rel, restrict)
        ):
            if isinstance(restrict, HasValueRestriction):
                for_all: Concept = -HasValueConcept(
                    restrict.get_role_name(), restrict.get_individual()
                )
            else:
                for_all: Concept = AllSomeConcept.all(
                    restrict.get_role_name(), restrict.get_concept()
                )
            x_for_all_b: Variable = kb.milp.get_variable(b, for_all)
            d: DegreeVariable = DegreeVariable.get_degree(x_for_all_b)
            kb.add_assertion(b, for_all, d)
            a: Individual = rel.get_subject_individual()
            x_for_all: Variable = kb.milp.get_variable(a, restrict)
            x_rel: Variable = kb.milp.get_variable(rel)
            ZadehSolver.kleene_dienes_implies_equation(
                x_for_all, x_rel, x_for_all_b, kb.milp
            )
        if (
            restrict.get_role_name() in kb.roles_with_trans_children
            and not kb.check_trans_role_applied(rel, restrict)
        ):
            trans_children: list[str] = kb.roles_with_trans_children[
                restrict.get_role_name()
            ]
            for tc in trans_children:
                if isinstance(restrict, HasValueRestriction):
                    all_concept: Concept = -HasValueConcept(
                        tc, restrict.get_individual()
                    )
                else:
                    all_concept: Concept = AllSomeConcept.all(
                        tc, restrict.get_concept()
                    )
                x_for_all_b: Variable = kb.milp.get_variable(b, all_concept)
                d: DegreeVariable = DegreeVariable.get_degree(x_for_all_b)
                kb.add_assertion(b, all_concept, d)
                a: Individual = rel.get_subject_individual()
                x_for_all: Variable = kb.milp.get_variable(a, restrict)
                x_rel: Variable = kb.milp.get_variable(rel)
                ZadehSolver.kleene_dienes_implies_equation(
                    x_for_all, x_rel, x_for_all_b, kb.milp
                )

        x_rel: Variable = kb.milp.get_variable(rel)
        x_for_all: Variable = kb.milp.get_variable(
            rel.get_subject_individual(), restrict
        )
        ZadehSolver.kleene_dienes_implies_equation(x_for_all, x_rel, x_B_in_C, kb.milp)

    @staticmethod
    def kleene_dienes_implies_equation(
        z: Variable, x1: Variable, x2: Variable, milp: MILPHelper
    ) -> None:
        y: Variable = milp.get_new_variable(VariableType.BINARY)
        milp.add_new_constraint(
            Expression(Term(1.0, x2), Term(1.0, y), Term(-1.0, z)),
            InequalityType.GREATER_THAN,
        )
        milp.add_new_constraint(
            Expression(2.0, Term(-1.0, y), Term(-1.0, z), Term(-1.0, x1)),
            InequalityType.GREATER_THAN,
        )

    @staticmethod
    def goedel_implies_equation(
        z: Variable, x1: Variable, x2: Variable, milp: MILPHelper
    ) -> None:
        y: Variable = milp.get_new_variable(VariableType.BINARY)
        milp.add_new_constraint(
            Expression(Term(2.0, y), Term(1.0, x1), Term(-1.0, x2)),
            InequalityType.GREATER_THAN,
            ConfigReader.EPSILON,
        )
        milp.add_new_constraint(
            Expression(Term(1.0, y), Term(1.0, x2), Term(-1.0, z)),
            InequalityType.GREATER_THAN,
        )
        milp.add_new_constraint(
            Expression(Term(1.0, x2), Term(-1.0, z), Term(-1.0, y)),
            InequalityType.LESS_THAN,
        )
        milp.add_new_constraint(
            Expression(Term(1.0, z), Term(-1.0, y)), InequalityType.GREATER_THAN
        )
        milp.add_new_constraint(
            Expression(-1.0, Term(1.0, x1), Term(-1.0, x2), Term(1.0, y)),
            InequalityType.LESS_THAN,
        )

    @typing.overload
    @staticmethod
    def zadeh_implies_equation(
        z: Variable, x1: Variable, x2: Variable, milp: MILPHelper
    ) -> None: ...

    @typing.overload
    @staticmethod
    def zadeh_implies_equation(
        z: float, x1: Variable, x2: Variable, milp: MILPHelper
    ) -> None: ...

    @staticmethod
    def zadeh_implies_equation(*args) -> None:
        assert len(args) == 4
        assert isinstance(args[1], Variable)
        assert isinstance(args[2], Variable)
        assert isinstance(args[3], MILPHelper)
        if isinstance(args[0], constants.NUMBER):
            ZadehSolver.__zadeh_implies_equation_2(*args)
        elif isinstance(args[0], Variable):
            ZadehSolver.__zadeh_implies_equation_1(*args)
        else:
            raise ValueError

    @staticmethod
    def __zadeh_implies_equation_1(
        z: Variable, x1: Variable, x2: Variable, milp: MILPHelper
    ) -> None:
        y: Variable = milp.get_new_variable(VariableType.BINARY)
        milp.add_new_constraint(
            Expression(Term(2.0, y), Term(1.0, x1), Term(-1.0, x2)),
            InequalityType.GREATER_THAN,
        )
        milp.add_new_constraint(
            Expression(Term(1.0, z), Term(-1.0, y)), InequalityType.EQUAL
        )
        milp.add_new_constraint(
            Expression(-1.0, Term(1.0, x1), Term(-1.0, x2), Term(1.0, y)),
            InequalityType.LESS_THAN,
        )

    @staticmethod
    def __zadeh_implies_equation_2(
        z: float, x1: Variable, x2: Variable, milp: MILPHelper
    ) -> None:
        y: Variable = milp.get_new_variable(VariableType.BINARY)
        milp.add_new_constraint(
            Expression(Term(2.0, y), Term(1.0, x1), Term(-1.0, x2)),
            InequalityType.GREATER_THAN,
            ConfigReader.EPSILON,
        )
        milp.add_new_constraint(Expression(z, Term(-1.0, y)), InequalityType.EQUAL)
        milp.add_new_constraint(
            Expression(-1.0, Term(1.0, x1), Term(-1.0, x2), Term(1.0, y)),
            InequalityType.LESS_THAN,
        )

    @staticmethod
    def zadeh_implies_leq_equation(
        z: Variable, x1: Variable, x2: Variable, milp: MILPHelper
    ) -> None:
        milp.add_new_constraint(
            Expression(1.0, Term(-1.0, x1), Term(1.0, x2), Term(-1.0, z)),
            InequalityType.GREATER_THAN,
        )

    @staticmethod
    def goedel_not_equation(y: Variable, z: Variable, milp: MILPHelper) -> None:
        if y.get_lower_bound() != 66.0:
            y.set_type(VariableType.BINARY)
        milp.add_new_constraint(
            Expression(-1.0, Term(1.0, z), Term(1.0, y)),
            InequalityType.LESS_THAN,
        )
        milp.add_new_constraint(
            Expression(-ConfigReader.EPSILON, Term(1.0, z), Term(1.0, y)),
            InequalityType.GREATER_THAN,
        )

    @typing.overload
    @staticmethod
    def or_equation(
        z: Variable, x1: Variable, x2: Variable, milp: MILPHelper
    ) -> None: ...

    @typing.overload
    @staticmethod
    def or_equation(x: list[Variable], z: Variable, milp: MILPHelper) -> None: ...

    @staticmethod
    def or_equation(*args) -> None:
        assert len(args) in [3, 4]
        if len(args) == 3:
            assert isinstance(args[0], list) and all(
                isinstance(a, Variable) for a in args[0]
            )
            assert isinstance(args[1], Variable)
            assert isinstance(args[2], MILPHelper)
            ZadehSolver.__or_equation_2(*args)
        else:
            assert isinstance(args[0], Variable)
            assert isinstance(args[1], Variable)
            assert isinstance(args[2], constants.NUMBER)
            assert isinstance(args[3], MILPHelper)
            ZadehSolver.__or_equation_1(*args)

    @staticmethod
    def __or_equation_1(z: Variable, x1: Variable, x2: float, milp: MILPHelper) -> None:
        y: Variable = milp.get_new_variable(VariableType.BINARY)
        milp.add_new_constraint(
            Expression(Term(1.0, z), Term(-1.0, x1)), InequalityType.GREATER_THAN
        )
        milp.add_new_constraint(
            Expression(Term(1.0, z)), InequalityType.GREATER_THAN, x2
        )
        milp.add_new_constraint(
            Expression(Term(1.0, x1), Term(1.0, y), Term(-1.0, z)),
            InequalityType.GREATER_THAN,
        )
        milp.add_new_constraint(
            Expression(1.0 + x2, Term(-1.0, y), Term(-1.0, z)),
            InequalityType.GREATER_THAN,
        )

    @staticmethod
    def __or_equation_2(x: list[Variable], z: Variable, milp: MILPHelper) -> None:
        N: int = len(x)
        M: float = Util.log2(N)
        for xi in x:
            milp.add_new_constraint(
                Expression(Term(1.0, z), Term(-1.0, xi)), InequalityType.GREATER_THAN
            )
        y: list[Variable] = [
            milp.get_new_variable(VariableType.BINARY) for _ in range(int(M))
        ]
        for i, xi in enumerate(x):
            dividendo: int = i
            exp: Expression = Expression(Term(-1.0, z), Term(1.0, xi))
            for n in range(int(M)):
                if dividendo % 2 == 0:
                    exp.add_term(Term(1.0, y[n]))
                else:
                    exp.add_term(Term(-1.0, y[n]))
                    exp.increment_constant()
                dividendo //= 2
            i += 1
            milp.add_new_constraint(exp, InequalityType.GREATER_THAN)

        exp2: Expression = Expression(1.0 - N)
        k: float = 1.0
        for m in range(int(M)):
            exp2.add_term(Term(k, y[m]))
            k *= 2.0
        milp.add_new_constraint(exp2, InequalityType.LESS_THAN)

    @staticmethod
    def or_negated_equation(
        z: Variable, x1: Variable, x2: Variable, milp: MILPHelper
    ) -> None:
        y: Variable = milp.get_new_variable(VariableType.BINARY)

        milp.add_new_constraint(
            Expression(1.0, Term(1.0, z), Term(1.0, x1)), InequalityType.GREATER_THAN
        )
        milp.add_new_constraint(
            Expression(Term(1.0, z)), InequalityType.GREATER_THAN, x2
        )
        milp.add_new_constraint(
            Expression(1.0, Term(-1.0, x1), Term(1.0, y), Term(-1.0, z)),
            InequalityType.GREATER_THAN,
        )
        milp.add_new_constraint(
            Expression(
                1.0 + x2,
                Term(-1.0, y),
                Term(-1.0, z),
            ),
            InequalityType.GREATER_THAN,
        )

    @staticmethod
    def and_(n1: float, n2: float) -> float:
        if n2 < n1:
            return n2
        return n1


@class_debugging()
class ClassicalSolver:
    @staticmethod
    def solve_and(ass: Assertion, kb: KnowledgeBase) -> None:
        ZadehSolver.solve_and(ass, kb)

    @staticmethod
    def solve_or(ass: Assertion, kb: KnowledgeBase) -> None:
        LukasiewiczSolver.solve_or(ass, kb)

    @staticmethod
    def solve_some(ass: Assertion, kb: KnowledgeBase) -> None:
        ZadehSolver.solve_some(ass, kb)

    @staticmethod
    def solve_all(rel: Relation, restrict: Restriction, kb: KnowledgeBase) -> None:
        ZadehSolver.solve_all(rel, restrict, kb)


@class_debugging()
class IndividualHandler:

    @staticmethod
    def add_relation(
        ind: Individual,
        role_name: str,
        b: Individual,
        degree: Degree,
        kb: KnowledgeBase,
    ) -> typing.Optional[Relation]:
        add_new_rel: bool = True
        rels: list[Relation] = ind.role_relations.get(role_name, [])
        rel: Relation = Relation(role_name, ind, b, degree)

        if degree.is_numeric():
            new_degree: float = typing.cast(DegreeNumeric, degree).get_numerical_value()
            for i in range(len(rels)):
                old_rel: Relation = rels[i]
                old_role: str = old_rel.get_role_name()
                old_ind: Individual = old_rel.get_object_individual()
                if (
                    b == old_ind
                    and old_role == role_name
                    and old_rel.get_degree().is_numeric()
                ):
                    add_new_rel = False
                    old_degree: float = typing.cast(
                        DegreeNumeric, old_rel.get_degree()
                    ).get_numerical_value()
                    if new_degree > old_degree:
                        add_new_rel = False
                        rels[i] = rel
                        ind.role_relations[role_name] = rels
                    Util.debug(
                        f"Relation {ind.name}, {b} through role {role_name} has already been processed hence ignored"
                    )
                    break
        if add_new_rel:
            Util.debug(f"Adding ({ind}, {b}): {role_name}")
            kb.num_relations += 1
            rels.append(rel)
            ind.role_relations[role_name] = rels
            ass_var: Variable = kb.milp.get_variable(rel)
            if str(degree) != str(ass_var):
                kb.milp.add_new_constraint(
                    Expression(Term(1.0, ass_var)), InequalityType.GREATER_THAN, degree
                )
            b_is_B: Variable = kb.milp.get_nominal_variable(str(b))
            kb.milp.add_new_constraint(
                Expression(Term(1.0, b_is_B), Term(-1.0, ass_var)),
                InequalityType.GREATER_THAN,
            )
            if kb.milp.show_vars.show_abstract_role_fillers(role_name, str(ind)):
                kb.milp.show_vars.add_individual_to_show(str(b))
            if kb.is_loaded():
                for r in kb.domain_restrictions:
                    kb.rule_domain_lazy_unfolding(r, rel)
                for r in kb.range_restrictions:
                    kb.rule_range_lazy_unfolding(r, rel)
                if role_name in kb.inverse_roles:
                    var1: Variable = kb.milp.get_variable(ind, b, role_name)
                    for inv_role in kb.inverse_roles.get(role_name):
                        var2: Variable = kb.milp.get_variable(b, ind, inv_role)
                        kb.milp.add_new_constraint(
                            Expression(Term(1.0, var1), Term(-1.0, var2)),
                            InequalityType.EQUAL,
                        )
            restricts: list[Restriction] = ind.role_restrictions.get(role_name, [])
            for r in restricts:
                IndividualHandler.solve_relation_restriction(rel, r, kb)
            if b == ind and role_name in ind.not_self_roles:
                IndividualHandler.solve_not_self_rule(ind, role_name, kb)
        return rel

    @staticmethod
    def solve_not_self_rule(ind: Individual, role_name: str, kb: KnowledgeBase) -> None:
        var1: Variable = kb.milp.get_variable(ind, ind, role_name)
        c: Concept = -SelfConcept(role_name)
        var2: Variable = kb.milp.get_variable(ind, c)
        kb.milp.add_new_constraint(
            Expression(1.0, Term(-1.0, var1), Term(-1.0, var2)),
            InequalityType.EQUAL,
        )

    @staticmethod
    def solve_relation_restriction(
        rel: Relation, restrict: Restriction, kb: KnowledgeBase
    ) -> None:
        if kb.get_logic() == FuzzyLogic.LUKASIEWICZ:
            LukasiewiczSolver.solve_all(rel, restrict, kb)
        elif kb.get_logic() == FuzzyLogic.ZADEH:
            ZadehSolver.solve_all(rel, restrict, kb)
        elif kb.get_logic() == FuzzyLogic.CLASSICAL:
            ClassicalSolver.solve_all(rel, restrict, kb)
        if kb.blocking_dynamic:
            CreatedIndividualHandler.unblock(rel.get_object_individual(), kb)

    @staticmethod
    def unblock_simple(ind: Individual, kb: KnowledgeBase) -> None:
        Util.debug(f"Simple Unblock children of {ind.name}")
        if ind.name in kb.directly_blocked_children:
            kb.unblock_children(ind.name)

    @typing.overload
    @staticmethod
    def add_restriction(
        ind: Individual, role_name: str, c: Concept, degree: Degree, kb: KnowledgeBase
    ) -> None: ...

    @typing.overload
    @staticmethod
    def add_restriction(
        ind: Individual,
        role_name: str,
        ind_name: str,
        degree: Degree,
        kb: KnowledgeBase,
    ) -> None: ...

    def add_restriction(*args):
        from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept

        assert len(args) == 5
        assert isinstance(args[0], Individual)
        assert isinstance(args[1], str)
        if (
            isinstance(args[2], Concept)
            and isinstance(args[3], Degree)
            and isinstance(args[4], KnowledgeBase)
        ):
            IndividualHandler.__add_restriction_1(*args)
        elif (
            isinstance(args[2], str)
            and isinstance(args[3], Degree)
            and isinstance(args[4], KnowledgeBase)
        ):
            IndividualHandler.__add_restriction_2(*args)
        else:
            raise ValueError

    def __add_restriction_1(
        ind: Individual, role_name: str, c: Concept, degree: Degree, kb: KnowledgeBase
    ) -> None:
        restrict: Restriction = Restriction(role_name, c, degree)
        IndividualHandler.common_part_add_restriction(ind, role_name, restrict, kb)

    def __add_restriction_2(
        ind: Individual,
        role_name: str,
        ind_name: str,
        degree: Degree,
        kb: KnowledgeBase,
    ) -> None:
        restrict: HasValueRestriction = HasValueRestriction(role_name, ind_name, degree)
        IndividualHandler.common_part_add_restriction(ind, role_name, restrict, kb)

    @staticmethod
    def common_part_add_restriction(
        ind: Individual, role_name: str, restrict: Restriction, kb: KnowledgeBase
    ) -> None:
        ind.role_restrictions[role_name] = ind.role_restrictions.get(role_name, []) + [
            restrict
        ]
        rels: list[Relation] = ind.role_relations.get(role_name, [])
        for r in rels:
            Util.debug(f"Adding universal restriction {restrict} to relation {r}")
            IndividualHandler.solve_relation_restriction(r, restrict, kb)

    @staticmethod
    def add_not_self_restriction(ind: Individual, role: str, kb: KnowledgeBase) -> None:
        if role in ind.not_self_roles:
            return
        ind.not_self_roles.add(role)
        rels: list[Relation] = ind.role_relations.get(role, [])
        for r in rels:
            if r.get_object_individual() == ind:
                IndividualHandler.solve_not_self_rule(role, kb)
                return


@class_debugging()
class CreatedIndividualHandler:

    @staticmethod
    def update_role_successors(name: str, role_name: str, kb: KnowledgeBase) -> None:
        if role_name is not None:
            Util.debug("Update list of role-successors")
            kb.r_successors[role_name] = kb.r_successors.get(role_name, []) + [name]
            Util.debug(
                f"R-successor list -> {role_name} : {kb.r_successors[role_name]}"
            )

    @staticmethod
    def get_representative(
        current_individual: CreatedIndividual,
        type: InequalityType,
        f_name: str,
        f: TriangularFuzzyNumber,
        kb: KnowledgeBase,
    ) -> CreatedIndividual:
        i: CreatedIndividual = current_individual.get_representative_if_exists(
            type, f_name, f
        )
        if i is not None:
            return i
        i: CreatedIndividual = kb.get_new_concrete_individual(None, None)
        ind: RepresentativeIndividual = RepresentativeIndividual(type, f_name, f, i)
        current_individual.representatives.append(ind)
        return i

    @staticmethod
    def unblock_pairwise(
        current_individual: CreatedIndividual, kb: KnowledgeBase
    ) -> None:
        """
        Unblock the individual
        """
        Util.debug(f"Test of Pair-wise Unblock children of {current_individual.name}")
        # "current_individual" is a blocking Y node: unblock blocked nodes
        if current_individual.name in kb.directly_blocked_children:
            Util.debug(f"{current_individual.name} is a blocking Y node")
            # remove Y from the Yprime list
            y_prime: CreatedIndividual = typing.cast(
                CreatedIndividual,
                typing.cast(CreatedIndividual, current_individual).parent,
            )
            y_individuals: list[str] = kb.y_prime_individuals.get(str(y_prime), [])
            y_individuals.remove(current_individual.name)

            # update Xprime list
            if len(y_individuals) > 0:
                kb.y_prime_individuals[str(y_prime)] = y_individuals
            else:
                del kb.y_prime_individuals[str(y_prime)]

            for x_name in kb.directly_blocked_children.get(current_individual.name):
                Util.debug(f"Processing X node {x_name}")
                # remove Xname from the  Xprime list
                x: CreatedIndividual = typing.cast(
                    CreatedIndividual, kb.individuals.get(x_name)
                )
                x_prime: CreatedIndividual = typing.cast(
                    CreatedIndividual, x.get_parent()
                )
                x_individuals: list[str] = kb.x_prime_individuals.get(str(x_prime), [])
                x_individuals.remove(x_name)
                if len(x_individuals) > 0:
                    kb.x_prime_individuals[str(x_prime)] = x_individuals
                else:
                    del kb.x_prime_individuals[str(x_prime)]
                # at last, unblock
                kb.unblock_individual(x_name)

            # now, Y (= current_individual) cannot be a blocking node anymore
            del kb.directly_blocked_children[current_individual.name]

        # if "current_individual" is a Yprime node: unblock blocking Y nodes
        if current_individual.name in kb.y_prime_individuals:
            Util.debug(f"{current_individual.name} is a y_prime node")
            for y_name in kb.y_prime_individuals.get(current_individual.name):
                Util.debug(f"Processing Y node {y_name}")
                for x_name in kb.directly_blocked_children.get(y_name):
                    Util.debug(f"Processing X node {x_name}")
                    # remove X from the  Xprime list
                    x: CreatedIndividual = typing.cast(
                        CreatedIndividual, kb.individuals.get(x_name)
                    )
                    x_prime: CreatedIndividual = typing.cast(
                        CreatedIndividual, x.get_parent()
                    )

                    if x_prime is not None:
                        Util.debug(f"{constants.STAR_SEPARATOR}{x_prime}")
                        x_individuals: list[str] = kb.x_prime_individuals.get(
                            str(x_prime), []
                        )
                        x_individuals.remove(x_name)
                        if len(x_individuals) > 0:
                            kb.x_prime_individuals[str(x_prime)] = x_individuals
                        else:
                            del kb.x_prime_individuals[str(x_prime)]
                    # unblock X
                    kb.unblock_individual(x_name)
                # now, Yname cannot be a blocking node anymore
                del kb.directly_blocked_children[y_name]
            # now, remove Yprime from the Yprime list
            del kb.y_prime_individuals[current_individual.name]

        # if "current_individual" is a Xprime node: unblock blocked X nodes
        if current_individual.name in kb.x_prime_individuals:
            Util.debug(f"{current_individual.name} is a x_prime node")
            x_individuals: list[str] = kb.x_prime_individuals.get(
                current_individual.name, []
            )
            for x_name in x_individuals:
                Util.debug(f"Processing X node {x_name}")
                # remove X from the  directlyBlockedChildren list
                x: CreatedIndividual = typing.cast(
                    CreatedIndividual, kb.individuals.get(x_name)
                )
                y_name: str = x.blocking_ancestor
                if y_name is not None:
                    y: CreatedIndividual = typing.cast(
                        CreatedIndividual, kb.individuals.get(y_name)
                    )
                    blocked_by_y: list[str] = kb.directly_blocked_children[y_name]
                    blocked_by_y.remove(x_name)

                    if len(blocked_by_y) > 0:
                        kb.directly_blocked_children[y_name] = blocked_by_y
                    else:
                        del kb.directly_blocked_children[y_name]
                        # update Yprime list
                        y_prime: CreatedIndividual = typing.cast(
                            CreatedIndividual, y.get_parent()
                        )
                        y_individuals: list[str] = kb.x_prime_individuals.get(
                            str(y_prime)
                        )
                        y_individuals.remove(y_name)

                        if len(y_individuals) > 0:
                            kb.y_prime_individuals[str(y_prime)] = x_individuals
                        else:
                            del kb.y_prime_individuals[str(y_prime)]
                #  unblock X
                kb.unblock_individual(x_name)
            # now, remove Xprime from the Xprime list
            del kb.x_prime_individuals[current_individual.name]

    @staticmethod
    def unblock(current_individual: CreatedIndividual, kb: KnowledgeBase) -> None:
        b_type: BlockingDynamicType = kb.blocking_type
        dynamic: bool = kb.blocking_dynamic

        if not isinstance(current_individual, CreatedIndividual):
            return
        if not dynamic:
            return

        if b_type == BlockingDynamicType.NO_BLOCKING:
            return
        elif b_type in (
            BlockingDynamicType.SUBSET_BLOCKING,
            BlockingDynamicType.SET_BLOCKING,
            BlockingDynamicType.ANYWHERE_SUBSET_BLOCKING,
            BlockingDynamicType.ANYWHERE_SET_BLOCKING,
        ):
            IndividualHandler.unblock_simple(current_individual, kb)
        else:
            CreatedIndividualHandler.unblock_pairwise(current_individual, kb)

    @staticmethod
    def is_indirectly_blocked(
        current_individual: CreatedIndividual, kb: KnowledgeBase
    ) -> bool:
        """
        A node v is indirectly blocked iff one of its ancestors are blocked.
        """
        Util.debug(
            f'Testing indirect blocking "{current_individual}" at depth {current_individual.depth}'
        )
        type: BlockingDynamicType = kb.blocking_type
        dynamic: bool = kb.blocking_dynamic
        if type == BlockingDynamicType.NO_BLOCKING:
            return False
        elif type in (
            BlockingDynamicType.SUBSET_BLOCKING,
            BlockingDynamicType.SET_BLOCKING,
        ):
            if not dynamic:
                return False
            return CreatedIndividualHandler.is_indirectly_simple_blocked(
                current_individual, kb
            )
        elif type in (
            BlockingDynamicType.ANYWHERE_SUBSET_BLOCKING,
            BlockingDynamicType.ANYWHERE_SET_BLOCKING,
        ):
            if not dynamic:
                return False
            return CreatedIndividualHandler.is_indirectly_anywhere_simple_blocked(
                current_individual, kb
            )
        elif type == BlockingDynamicType.DOUBLE_BLOCKING:
            return CreatedIndividualHandler.is_indirectly_pairwise_blocked(
                current_individual, kb
            )
        return CreatedIndividualHandler.is_indirectly_anywhere_pairwise_blocked(
            current_individual, kb
        )

    @staticmethod
    def is_indirectly_simple_blocked(
        current_individual: CreatedIndividual, kb: KnowledgeBase
    ) -> bool:
        """
        A node v is indirectly blocked iff one of its ancestors are blocked.
        """
        if current_individual.depth < 4:
            Util.debug("Depth < 4, node is not indirectly blocked")
            current_individual.indirectly_blocked = (
                CreatedIndividualBlockingType.NOT_BLOCKED
            )
            return False
        if (
            current_individual.indirectly_blocked
            == CreatedIndividualBlockingType.BLOCKED
        ):
            Util.debug("Already checked if indirectly blocked, node IS blocked")
            return True
        if (
            current_individual.indirectly_blocked
            == CreatedIndividualBlockingType.NOT_BLOCKED
        ):
            Util.debug("Already checked if indirectly blocked, node is not blocked")
            return False
        current_individual.indirectly_blocked = (
            CreatedIndividualBlockingType.NOT_BLOCKED
        )
        anc: typing.Optional[Individual] = current_individual.get_parent()
        while anc and anc.is_blockable():
            ancestor: CreatedIndividual = typing.cast(CreatedIndividual, anc)
            Util.debug(
                f"Indirect blocking: check if directly blocked {ancestor.name} at depth {ancestor.depth}"
            )
            if CreatedIndividualHandler.is_directly_blocked(ancestor, kb):
                current_individual.indirectly_blocked = (
                    CreatedIndividualBlockingType.BLOCKED
                )
                current_individual.blocking_ancestor = str(ancestor)
                Util.debug(
                    f"{current_individual.name} IS INDIRECTLY blocked by {ancestor}"
                )
                break
            anc = ancestor.get_parent()
        return (
            current_individual.indirectly_blocked
            == CreatedIndividualBlockingType.BLOCKED
        )

    @staticmethod
    def is_indirectly_anywhere_simple_blocked(
        current_individual: CreatedIndividual, kb: KnowledgeBase
    ) -> bool:
        if current_individual.depth < 3:
            Util.debug("Depth < 3, node is not indirectly anywhere blocked")
            current_individual.indirectly_blocked = (
                CreatedIndividualBlockingType.NOT_BLOCKED
            )
            return False
        if (
            current_individual.indirectly_blocked
            == CreatedIndividualBlockingType.BLOCKED
        ):
            Util.debug("Already checked if indirectly blocked, node IS blocked")
            return True
        if (
            current_individual.indirectly_blocked
            == CreatedIndividualBlockingType.NOT_BLOCKED
        ):
            Util.debug("Already checked if indirectly blocked, node is not blocked")
            return False
        current_individual.indirectly_blocked = (
            CreatedIndividualBlockingType.NOT_BLOCKED
        )
        anc: typing.Optional[Individual] = current_individual.get_parent()
        while anc and anc.is_blockable():
            ancestor: CreatedIndividual = typing.cast(CreatedIndividual, anc)
            Util.debug(
                f"Indirect blocking: check if directly blocked {ancestor.name} at depth {ancestor.depth}"
            )
            if CreatedIndividualHandler.is_directly_blocked(ancestor, kb):
                current_individual.indirectly_blocked = (
                    CreatedIndividualBlockingType.BLOCKED
                )
                current_individual.blocking_ancestor = str(ancestor)
                Util.debug(
                    f"{current_individual.name} IS INDIRECTLY anywhere simple blocked by {ancestor}"
                )
                break
            anc = ancestor.get_parent()
        return (
            current_individual.indirectly_blocked
            == CreatedIndividualBlockingType.BLOCKED
        )

    @staticmethod
    def is_indirectly_pairwise_blocked(
        current_individual: CreatedIndividual, kb: KnowledgeBase
    ) -> bool:
        if current_individual.depth < 5:
            Util.debug("Depth < 5, node is not indirectly blocked")
            current_individual.indirectly_blocked = (
                CreatedIndividualBlockingType.NOT_BLOCKED
            )
            return False
        if (
            current_individual.indirectly_blocked
            == CreatedIndividualBlockingType.BLOCKED
        ):
            Util.debug("Already checked if indirectly blocked, node IS blocked")
            return True
        if (
            current_individual.indirectly_blocked
            == CreatedIndividualBlockingType.NOT_BLOCKED
        ):
            Util.debug("Already checked if indirectly blocked, node is not blocked")
            return False
        current_individual.indirectly_blocked = (
            CreatedIndividualBlockingType.NOT_BLOCKED
        )
        anc: typing.Optional[Individual] = current_individual.get_parent()
        while anc and anc.is_blockable():
            ancestor: CreatedIndividual = typing.cast(CreatedIndividual, anc)
            Util.debug(
                f"Indirect blocking: check if directly blocked {ancestor.name} at depth {ancestor.depth}"
            )
            if CreatedIndividualHandler.is_directly_blocked(ancestor, kb):
                current_individual.indirectly_blocked = (
                    CreatedIndividualBlockingType.BLOCKED
                )
                current_individual.blocking_ancestor = str(ancestor)
                Util.debug(
                    f"{current_individual.name} IS INDIRECTLY blocked by {ancestor}"
                )
                break
            anc = ancestor.get_parent()
        return (
            current_individual.indirectly_blocked
            == CreatedIndividualBlockingType.BLOCKED
        )

    @staticmethod
    def is_indirectly_anywhere_pairwise_blocked(
        current_individual: CreatedIndividual, kb: KnowledgeBase
    ) -> bool:
        if current_individual.depth < 4:
            Util.debug("Depth < 4, node is not indirectly anywhere pairwise blocked")
            current_individual.indirectly_blocked = (
                CreatedIndividualBlockingType.NOT_BLOCKED
            )
            return False
        if (
            current_individual.indirectly_blocked
            == CreatedIndividualBlockingType.BLOCKED
        ):
            Util.debug(
                "Already checked if indirectly anywhere pairwise blocked, node IS blocked"
            )
            return True
        if (
            current_individual.indirectly_blocked
            == CreatedIndividualBlockingType.NOT_BLOCKED
        ):
            Util.debug(
                "Already checked if indirectly anywhere pairwise blocked, node is not blocked"
            )
            return False
        current_individual.indirectly_blocked = (
            CreatedIndividualBlockingType.NOT_BLOCKED
        )
        anc: typing.Optional[Individual] = current_individual.get_parent()
        while anc and anc.is_blockable():
            ancestor: CreatedIndividual = typing.cast(CreatedIndividual, anc)
            Util.debug(
                f"Indirect anywhere pairwise blocking: check if directly blocked {ancestor.name} at depth {ancestor.depth}"
            )
            if CreatedIndividualHandler.is_directly_blocked(ancestor, kb):
                current_individual.indirectly_blocked = (
                    CreatedIndividualBlockingType.BLOCKED
                )
                current_individual.blocking_ancestor = str(ancestor)
                Util.debug(
                    f"{current_individual.name} IS INDIRECTLY anywhere pairwise blocked by {ancestor}"
                )
                break
            anc = ancestor.get_parent()
        return (
            current_individual.indirectly_blocked
            == CreatedIndividualBlockingType.BLOCKED
        )

    @staticmethod
    def is_directly_blocked(
        current_individual: CreatedIndividual, kb: KnowledgeBase
    ) -> bool:
        """
        A node v is directly blocked iff none of its ancestors are blocked
        and there exists an ancestor w such that
                                    L(v) = L(w),
        where L(*) is the set of Concept's labels for a node.
        In this case we say that w directly blocks v.
        """
        type: BlockingDynamicType = kb.blocking_type
        if type == BlockingDynamicType.NO_BLOCKING:
            return False
        elif type in (
            BlockingDynamicType.SUBSET_BLOCKING,
            BlockingDynamicType.SET_BLOCKING,
        ):
            return CreatedIndividualHandler.is_directly_simple_blocked(
                current_individual, kb
            )
        elif type in (
            BlockingDynamicType.ANYWHERE_SUBSET_BLOCKING,
            BlockingDynamicType.ANYWHERE_SET_BLOCKING,
        ):
            return CreatedIndividualHandler.is_directly_anywhere_simple_blocked(
                current_individual, kb
            )
        elif type == BlockingDynamicType.DOUBLE_BLOCKING:
            return CreatedIndividualHandler.is_directly_pairwise_blocked(
                current_individual, kb
            )
        return CreatedIndividualHandler.is_directly_anywhere_pairwise_blocked(
            current_individual, kb
        )

    @staticmethod
    def is_directly_simple_blocked(
        current_individual: CreatedIndividual, kb: KnowledgeBase
    ) -> bool:
        Util.debug(
            f"Directly Simple blocking status {current_individual.directly_blocked}"
        )
        if current_individual.depth < 3:
            Util.debug("Depth < 3, node is not blocked")
            current_individual.directly_blocked = (
                CreatedIndividualBlockingType.NOT_BLOCKED
            )
            return False
        if current_individual.directly_blocked == CreatedIndividualBlockingType.BLOCKED:
            Util.debug(
                f"Already directly blocked by {current_individual.blocking_ancestor}"
            )
            return True
        if (
            current_individual.directly_blocked
            == CreatedIndividualBlockingType.NOT_BLOCKED
        ):
            Util.debug("Already checked if directly blocked, node is not blocked")
            return False
        current_individual.directly_blocked = CreatedIndividualBlockingType.NOT_BLOCKED
        Util.debug(f"Testing direct blocking: {current_individual}")
        anc: typing.Optional[Individual] = current_individual.get_parent()
        while anc and anc.is_blockable():
            ancestor: CreatedIndividual = typing.cast(CreatedIndividual, anc)
            Util.debug(
                f"Compare with created individual {ancestor.name} of depth {ancestor.depth}"
            )
            if CreatedIndividualHandler.match_concept_labels(
                current_individual, ancestor, kb
            ):
                current_individual.directly_blocked = (
                    CreatedIndividualBlockingType.BLOCKED
                )
                current_individual.blocking_ancestor = str(anc)
                blocked_children: typing.Optional[list[str]] = (
                    kb.directly_blocked_children.get(
                        current_individual.blocking_ancestor, []
                    )
                )
                if current_individual.name not in blocked_children:
                    blocked_children.append(current_individual.name)
                kb.directly_blocked_children[str(anc)] = blocked_children
                Util.debug(f"{current_individual.name} IS DIRECTLY blocked by {anc}")
                current_individual.mark_indirectly_blocked()
                break
            Util.debug(f"{current_individual.name} IS NOT directly blocked by {anc}")
            anc = ancestor.get_parent()
        return (
            current_individual.directly_blocked == CreatedIndividualBlockingType.BLOCKED
        )

    @staticmethod
    def is_directly_anywhere_simple_blocked(
        current_individual: CreatedIndividual, kb: KnowledgeBase
    ) -> bool:
        Util.debug(
            f"Directly Anywhere Simple blocking status {current_individual.directly_blocked}"
        )
        node_id: int = current_individual.get_integer_id()
        if node_id <= 1:
            Util.debug(f"Node ID : {node_id} <= 1 : node is not blocked")
            current_individual.directly_blocked = (
                CreatedIndividualBlockingType.NOT_BLOCKED
            )
            return False
        if current_individual.depth < 2:
            Util.debug("Depth < 2, node is not blocked")
            current_individual.directly_blocked = (
                CreatedIndividualBlockingType.NOT_BLOCKED
            )
            return False
        if current_individual.directly_blocked == CreatedIndividualBlockingType.BLOCKED:
            Util.debug(
                f"Already directly blocked by {current_individual.blocking_ancestor}"
            )
            return True
        if (
            current_individual.directly_blocked
            == CreatedIndividualBlockingType.NOT_BLOCKED
        ):
            Util.debug("Already checked if directly blocked, node is not blocked")
            return False
        current_individual.directly_blocked = CreatedIndividualBlockingType.NOT_BLOCKED
        Util.debug(f"Testing direct anywhere blocking: {current_individual}")
        candidate_ind: SortedSet[CreatedIndividual] = (
            CreatedIndividualHandler.matching_individual(current_individual, kb)
        )
        Util.debug(f"Anywhere blocking: Found individuals: {candidate_ind}")
        if len(candidate_ind) > 0:
            anc: CreatedIndividual = candidate_ind.pop()
            current_individual.directly_blocked = CreatedIndividualBlockingType.BLOCKED
            current_individual.blocking_ancestor = str(anc)
            blocked_children: list[str] = kb.directly_blocked_children.get(
                current_individual.blocking_ancestor, []
            )
            if current_individual.name not in blocked_children:
                blocked_children.append(current_individual.name)
            kb.directly_blocked_children[str(anc)] = blocked_children
            Util.debug(
                f"{current_individual.name} IS DIRECTLY ANYWHERE blocked by {anc}"
            )
            current_individual.mark_indirectly_blocked()
        else:
            Util.debug(f"{current_individual.name} IS NOT directly ANYWHERE blocked")
        return (
            current_individual.directly_blocked == CreatedIndividualBlockingType.BLOCKED
        )

    @staticmethod
    def mark_indirectly_simple_unchecked(
        current_individual: CreatedIndividual, kb: KnowledgeBase
    ) -> None:
        Util.debug(
            f"{constants.SEPARATOR}MARK UNCHECKED subtree of: {current_individual.name}"
        )
        queue: deque[CreatedIndividual] = deque()
        queue.append(current_individual)
        while len(queue) > 0:
            ind: CreatedIndividual = queue.popleft()
            if not ind.role_relations:
                break
            for role in ind.role_relations:
                rels: list[Relation] = copy.deepcopy(ind.role_relations[role])
                for rel in rels:
                    Util.debug(
                        f"{rel.get_subject_individual()} has role {rel.get_role_name()} with filler {rel.get_object_individual()}"
                    )
                    son: Individual = rel.get_object_individual()
                    if son != ind.parent:
                        if not son.is_blockable():
                            continue
                        son: CreatedIndividual = typing.cast(CreatedIndividual, son)
                        Util.debug(
                            f"Filler is not {current_individual.name}'s parent, so mark {son} as UNCHECKED"
                        )
                        CreatedIndividualHandler.unblock_indirectly_blocked(son, kb)
                        if rel.get_subject_individual() != rel.get_object_individual():
                            queue.append(son)
                    Util.debug("Filler is parent, so skip")
        Util.debug(
            f"{constants.SEPARATOR}MARK END UNCHECKED subtree of {current_individual.name}{constants.SEPARATOR}"
        )

    @staticmethod
    def is_directly_pairwise_blocked(
        current_individual: CreatedIndividual, kb: KnowledgeBase
    ) -> bool:
        Util.debug(
            f"Directly pairwise blocking status {current_individual.directly_blocked}"
        )
        if current_individual.depth < 4:
            Util.debug("Depth < 4, node is not directly blocked")
            current_individual.directly_blocked = (
                CreatedIndividualBlockingType.NOT_BLOCKED
            )
            return False
        if current_individual.directly_blocked == CreatedIndividualBlockingType.BLOCKED:
            Util.debug(
                f"Already directly blocked by {current_individual.blocking_ancestor}"
            )
            return True
        if (
            current_individual.directly_blocked
            == CreatedIndividualBlockingType.NOT_BLOCKED
        ):
            Util.debug("Already checked if directly blocked, node is not blocked")
            return False
        current_individual.directly_blocked = CreatedIndividualBlockingType.NOT_BLOCKED
        Util.debug(f"Testing direct pair-wise blocking: {current_individual}")
        node_x_prime: CreatedIndividual = typing.cast(
            CreatedIndividual, current_individual.get_parent()
        )
        node_y: CreatedIndividual = typing.cast(
            CreatedIndividual, current_individual.get_parent()
        )
        while node_y.get_parent() and node_y.get_parent().is_blockable():
            node_y_prime: CreatedIndividual = typing.cast(
                CreatedIndividual, node_y.get_parent()
            )
            Util.debug(
                f"{node_x_prime.name} : {current_individual.role_name} : {current_individual.name}"
            )
            Util.debug(f"{node_y_prime.name} : {node_y.role_name} : {node_y.name}")
            if (
                current_individual.role_name == node_y.role_name
                and CreatedIndividualHandler.match_concept_labels(
                    current_individual, node_y, kb
                )
                and CreatedIndividualHandler.match_concept_labels(
                    node_x_prime, node_y_prime, kb
                )
            ):
                current_individual.directly_blocked = (
                    CreatedIndividualBlockingType.BLOCKED
                )
                current_individual.blocking_ancestor = str(node_y)
                blocked_children: list[str] = kb.directly_blocked_children.get(
                    current_individual.blocking_ancestor, []
                )
                if current_individual.name not in blocked_children:
                    blocked_children.append(current_individual.name)
                kb.directly_blocked_children[current_individual.blocking_ancestor] = (
                    blocked_children
                )

                y_prime: str = str(node_y_prime)
                y_individuals: list[str] = []
                if y_prime in kb.y_prime_individuals:
                    y_individuals = kb.y_prime_individuals.get(y_prime)
                if current_individual.blocking_ancestor not in y_individuals:
                    y_individuals.append(current_individual.blocking_ancestor)
                kb.y_prime_individuals[y_prime] = y_individuals
                x_prime: str = str(node_x_prime)
                x_individuals: list[str] = []
                if x_prime in kb.x_prime_individuals:
                    x_individuals = kb.x_prime_individuals.get(x_prime)
                if current_individual.name not in x_individuals:
                    x_individuals.append(current_individual.name)
                kb.x_prime_individuals[x_prime] = x_individuals
                Util.debug(
                    f"BLOCKING: x ={current_individual.name} is directly blocked with y = {node_y}, x' = {node_x_prime}, y' = {node_y_prime}"
                )
                current_individual.mark_indirectly_blocked()
                break
            node_y = typing.cast(CreatedIndividual, node_y.get_parent())
        return (
            current_individual.directly_blocked == CreatedIndividualBlockingType.BLOCKED
        )

    @staticmethod
    def is_directly_anywhere_pairwise_blocked(
        current_individual: CreatedIndividual, kb: KnowledgeBase
    ) -> bool:
        Util.debug(
            f"Directly anywhere pairwise blocking status {current_individual.directly_blocked}"
        )
        if current_individual.depth < 3:
            Util.debug("Depth < 3, node is not directly  anywhere pairwise blocked")
            current_individual.directly_blocked = CreatedIndividualBlockingType.BLOCKED
            return False
        if current_individual.directly_blocked == CreatedIndividualBlockingType.BLOCKED:
            Util.debug(
                f"Already directly  anywhere pairwise blocked by {current_individual.blocking_ancestor}"
            )
            return True
        if (
            current_individual.directly_blocked
            == CreatedIndividualBlockingType.NOT_BLOCKED
        ):
            Util.debug(
                "Already checked if directly anywhere pairwise blocked, node is not blocked"
            )
            return False
        current_individual.directly_blocked = CreatedIndividualBlockingType.NOT_BLOCKED
        Util.debug(f"Testing direct anywhere pairwise blocking: {current_individual}")
        node_x_prime: CreatedIndividual = typing.cast(
            CreatedIndividual, current_individual.get_parent()
        )
        x_prime: str = str(node_x_prime)
        node_x: CreatedIndividual = current_individual
        role_name: str = current_individual.role_name
        Util.debug(
            f"Edge node_x_prime:role:node_x = {x_prime} : {node_x.role_name} : {node_x.name}"
        )
        rsuccs: list[str] = kb.r_successors.get(role_name, [])
        index_node_x: int = rsuccs.index(node_x.name)

        Util.debug(f"Successors list -> {rsuccs}")
        Util.debug(f"\t\tPosition -> {index_node_x}")
        i: int = 0
        while i < index_node_x:
            ynode: str = rsuccs[i]
            node_y: CreatedIndividual = typing.cast(
                CreatedIndividual, kb.get_individual(ynode)
            )
            Util.debug(f"Node y {ynode} depth = {node_y.depth}")
            if node_y.depth < 3:
                Util.debug("Depth < 3, node cannot be node_y")
                i += 1
                continue
            node_y_prime: CreatedIndividual = typing.cast(
                CreatedIndividual, node_y.get_parent()
            )
            Util.debug(
                f"{x_prime} : {current_individual.role_name} : {current_individual.name}"
            )
            Util.debug(f"{node_y_prime.name} : {node_y.role_name} : {node_y.name}")
            if CreatedIndividualHandler.match_concept_labels(
                current_individual, node_y, kb
            ) and CreatedIndividualHandler.match_concept_labels(
                node_x_prime, node_y_prime, kb
            ):
                current_individual.directly_blocked = (
                    CreatedIndividualBlockingType.BLOCKED
                )
                current_individual.blocking_ancestor = str(node_y)
                blocked_children: list[str] = kb.directly_blocked_children.get(
                    current_individual.blocking_ancestor, []
                )
                if current_individual.name not in blocked_children:
                    blocked_children.append(current_individual.name)
                kb.directly_blocked_children[current_individual.blocking_ancestor] = (
                    blocked_children
                )
                y_prime: str = str(node_y_prime)
                y_individuals: list[str] = kb.y_prime_individuals.get(y_prime, [])
                if current_individual.blocking_ancestor not in y_individuals:
                    y_individuals.append(current_individual.blocking_ancestor)
                kb.y_prime_individuals[y_prime] = y_individuals
                x_individuals: list[str] = kb.x_prime_individuals.get(x_prime, [])
                if current_individual.name not in x_individuals:
                    x_individuals.append(current_individual.name)
                kb.x_prime_individuals[x_prime] = x_individuals
                Util.debug(
                    f"BLOCKING: x = {current_individual.name} is directly blocked with y = {node_y}, x' = {node_x_prime}, y' = {node_y_prime}"
                )
                current_individual.blocking_ancestor = str(node_x_prime)
                current_individual.blocking_ancestor_y = str(node_y)
                current_individual.blocking_ancestor_y_prime = str(node_y_prime)
                current_individual.mark_indirectly_blocked()
                break
            i += 1
        return (
            current_individual.directly_blocked == CreatedIndividualBlockingType.BLOCKED
        )

    @staticmethod
    def is_blocked(current_individual: CreatedIndividual, kb: KnowledgeBase) -> bool:
        return CreatedIndividualHandler.is_indirectly_blocked(
            current_individual, kb
        ) or CreatedIndividualHandler.is_directly_blocked(current_individual, kb)

    @staticmethod
    def matching_individual(
        current_individual: CreatedIndividual, kb: KnowledgeBase
    ) -> set[CreatedIndividual]:
        Util.debug(
            f"Find matching individual for : {current_individual.name} ID : {current_individual.get_integer_id()} size : {len(current_individual.concept_list)}"
        )
        Util.debug(f"Concept list: {current_individual.concept_list}")
        type: BlockingDynamicType = kb.blocking_type
        first_concept: bool = True
        candidate_set: SortedSet[CreatedIndividual] = SortedSet()
        for concept in current_individual.concept_list:
            Util.debug(
                f"Process concept {concept}: {kb.get_concept_from_number(concept)}"
            )
            current_ind: SortedSet[CreatedIndividual] = kb.concept_individual_list.get(
                concept, SortedSet()
            )
            Util.debug(f"Individuals List -> {current_ind}")
            if not first_concept:
                tmp_current_ind: SortedSet[CreatedIndividual] = (
                    current_individual.individual_set_intersection_of(
                        candidate_set, current_ind
                    )
                )
                if len(tmp_current_ind) == 0:
                    continue
                return tmp_current_ind
            candidate_set: SortedSet[CreatedIndividual] = SortedSet()
            for ind in current_ind:
                assert isinstance(ind, CreatedIndividual)

                if ind.get_integer_id() >= current_individual.get_integer_id():
                    break
                Util.debug(
                    f"Individual {ind.name} ID : {ind.get_integer_id()} size : {len(ind.concept_list)}"
                )
                Util.debug(f"Concept list -> {ind.concept_list}")
                is_blocked: bool = (
                    ind.directly_blocked == CreatedIndividualBlockingType.BLOCKED
                    or ind.indirectly_blocked == CreatedIndividualBlockingType.BLOCKED
                )
                Util.debug(f"Blocked? -> {is_blocked}")
                if (
                    ind.get_integer_id() >= current_individual.get_integer_id()
                    or is_blocked
                ):
                    continue
                if type == BlockingDynamicType.ANYWHERE_SUBSET_BLOCKING and len(
                    ind.concept_list
                ) >= len(current_individual.concept_list):
                    candidate_set.add(ind)
                elif type == BlockingDynamicType.ANYWHERE_SET_BLOCKING and len(
                    ind.concept_list
                ) == len(current_individual.concept_list):
                    candidate_set.add(ind)
            Util.debug(f"Candidate set -> {candidate_set}")
            if len(candidate_set) == 0:
                return candidate_set
            first_concept = False
        return candidate_set

    @staticmethod
    def match_concept_labels(
        current_individual: CreatedIndividual, b: CreatedIndividual, kb: KnowledgeBase
    ) -> bool:
        Util.debug(f"Concept label comparison: {current_individual.name} with {b.name}")
        Util.debug(
            f"Individual {current_individual.name} size: {len(current_individual.concept_list)}"
        )
        for l1 in current_individual.concept_list:
            Util.debug(f"Concept {l1}: {kb.get_concept_from_number(l1)}")
        Util.debug(f"Individual {b.name} size: {len(b.concept_list)}")
        for l2 in b.concept_list:
            Util.debug(f"Concept {l2}: {kb.get_concept_from_number(l2)}")
        type: BlockingDynamicType = kb.blocking_type
        if type == BlockingDynamicType.NO_BLOCKING:
            return False
        elif type in (
            BlockingDynamicType.SUBSET_BLOCKING,
            BlockingDynamicType.ANYWHERE_SUBSET_BLOCKING,
        ):
            return CreatedIndividualHandler.match_subset_concept_labels(
                current_individual, b
            )
        return CreatedIndividualHandler.match_set_concept_labels(current_individual, b)

    @staticmethod
    def match_subset_concept_labels(
        current_individual: CreatedIndividual, b: CreatedIndividual
    ) -> bool:
        if b is None:
            return False
        return current_individual.concept_list.issubset(b.concept_list)

    @staticmethod
    def match_set_concept_labels(
        current_individual: CreatedIndividual, b: CreatedIndividual
    ) -> bool:
        if b is None:
            return False
        return current_individual.concept_list == b.concept_list

    @staticmethod
    def unblock_directly_blocked(
        current_individual: CreatedIndividual, kb: KnowledgeBase
    ) -> None:
        Util.debug(
            f"Directly blocked individual : {current_individual} : now unchecked"
        )
        current_individual.directly_blocked = CreatedIndividualBlockingType.UNCHECKED
        current_individual.blocking_ancestor = None
        blocked_assertions: list[Assertion] = kb.blocked_exist_assertions.get(
            str(current_individual)
        )
        if blocked_assertions is not None:
            kb.exist_assertions.extend(blocked_assertions)
            del kb.blocked_exist_assertions[str(current_individual)]

    @staticmethod
    def unblock_indirectly_blocked(
        current_individual: CreatedIndividual, kb: KnowledgeBase
    ) -> None:
        Util.debug(
            f"Indirectly blocked individual : {current_individual} : now unchecked"
        )
        current_individual.indirectly_blocked = CreatedIndividualBlockingType.UNCHECKED
        current_individual.blocking_ancestor = None
        blocked_assertions: list[Assertion] = kb.blocked_exist_assertions.get(
            str(current_individual)
        )
        if blocked_assertions is not None:
            kb.exist_assertions.extend(blocked_assertions)
            del kb.blocked_exist_assertions[str(current_individual)]

        blocked_assertions: list[Assertion] = kb.blocked_assertions.get(
            str(current_individual)
        )
        if blocked_assertions is not None:
            kb.add_assertions(blocked_assertions)
            del kb.blocked_assertions[str(current_individual)]
