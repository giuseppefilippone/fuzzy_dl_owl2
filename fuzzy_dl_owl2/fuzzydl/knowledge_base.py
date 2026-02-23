from __future__ import annotations

import copy
import pickle
import typing
from collections import deque

import networkx as nx
import trycast
from sortedcontainers import SortedSet

from fuzzy_dl_owl2.fuzzydl.assertion.assertion import Assertion
from fuzzy_dl_owl2.fuzzydl.classification_node import ClassificationNode
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
from fuzzy_dl_owl2.fuzzydl.concept.sigma_concept import SigmaConcept
from fuzzy_dl_owl2.fuzzydl.concept.sigma_count import SigmaCount
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
    """
    This class serves as the central container for a fuzzy ontology, managing the TBox, ABox, and RBox within a fuzzy description logic framework. It facilitates reasoning tasks such as consistency checking, concept satisfiability, and subsumption by implementing a tableau algorithm that translates fuzzy logic constraints into a Mixed-Integer Linear Programming (MILP) problem. The class handles complex operations including TBox normalization and absorption, ABox expansion with blocking strategies to ensure termination, and the management of concrete domains and aggregation operators. It supports multiple fuzzy semantics, such as Lukasiewicz, Zadeh, and Goedel, allowing users to define axioms and subsequently solve for truth degrees or optimize specific expressions.

    :param language: The description logic language expressivity of the knowledge base, such as SHOIN(D) or SROIQ(D), computed based on the features present in the ontology.
    :type language: str
    :param milp: Manages the Mixed-Integer Linear Programming (MILP) model, including variables, constraints, and optimization, required for reasoning tasks within the fuzzy knowledge base.
    :type milp: MILPHelper
    :param blocking_type: Specifies the blocking strategy (e.g., subset, set, double, or anywhere blocking) used during reasoning to ensure termination, indicating whether the blocking is static or dynamic.
    :type blocking_type: BlockingDynamicType
    :param max_depth: The maximal depth of the completion forest reached during the reasoning process, used to limit the search space and track statistics.
    :type max_depth: int
    :param num_assertions: The number of assertions in the ABox.
    :type num_assertions: int
    :param num_defined_concepts: The number of new atomic concepts dynamically generated during the reasoning process, used to assign unique names and track the size of the TBox.
    :type num_defined_concepts: int
    :param num_defined_individuals: The number of new individuals created during the reasoning process, used to track the size of the ABox.
    :type num_defined_individuals: int
    :param num_relations: The number of relations in the knowledge base, used to track the size of the RBox.
    :type num_relations: int
    :param old_01_variables: The number of semi-continuous variables in the [0, 1] range that would be generated by the old calculus, used to track the size of MILP problems for comparison.
    :type old_01_variables: int
    :param old_binary_variables: The number of binary variables that would be created by the old calculus for MILP problems.
    :type old_binary_variables: int
    :param CLASSIFIED: Indicates whether the knowledge base has been classified.
    :type CLASSIFIED: bool
    :param ABOX_EXPANDED: Indicates whether the ABox has been completely expanded.
    :type ABOX_EXPANDED: bool
    :param KB_LOADED: A flag that indicates whether the knowledge base has been completely loaded and processed.
    :type KB_LOADED: bool
    :param KB_UNSAT: Flag indicating whether the knowledge base is unsatisfiable.
    :type KB_UNSAT: bool
    :param concrete_fuzzy_concepts: Indicates whether the knowledge base contains concrete fuzzy concepts, affecting the computed description logic language expressivity.
    :type concrete_fuzzy_concepts: bool
    :param lazy_unfondable: Indicates whether the knowledge base is lazy unfoldable, allowing for lazy unfolding optimizations.
    :type lazy_unfondable: bool
    :param show_language: Indicates whether the description logic language of the knowledge base should be displayed to the user.
    :type show_language: bool
    :param acyclic_tbox: Flag indicating whether the TBox is acyclic, meaning it contains no cyclic dependencies in its concept definitions or inclusions.
    :type acyclic_tbox: bool
    :param blocking_dynamic: Indicates whether the blocking strategy used during reasoning is dynamic, which is typically required when inverse roles or domain restrictions are present.
    :type blocking_dynamic: bool
    :param rule_acyclic_tbox: Indicates whether the TBox is rule acyclic.
    :type rule_acyclic_tbox: bool
    :param applied_trans_role_rules: A list of identifiers for applications of the transitive role rule that have already been performed, used to track reasoning progress and prevent redundant rule applications.
    :type applied_trans_role_rules: list[str]
    :param assertions: A list of fuzzy assertions representing facts about individuals in the ABox, used to track concept and role memberships during reasoning.
    :type assertions: list[Assertion]
    :param exist_assertions: A list of assertions involving existential restrictions that are queued for processing during the tableau expansion.
    :type exist_assertions: list[Assertion]
    :param positive_concrete_value_assertions: A list of positive datatype restrictions in the ABox, specifically at-most, at-least, and exact value assertions, stored for processing.
    :type positive_concrete_value_assertions: list[Assertion]
    :param t_G: A list of General Concept Inclusions (GCIs) from the TBox that could not be absorbed or simplified via lazy unfolding.
    :type t_G: list[GeneralConceptInclusion]
    :param axioms_C_equiv_D: A list of concept equivalence axioms of the form C = D, used to track equivalent concepts within the TBox.
    :type axioms_C_equiv_D: list[ConceptEquivalence]
    :param temp_string_concept_list: A temporary list of concepts involving string datatypes, used to track and convert string values to integers during the reasoning process.
    :type temp_string_concept_list: list[Concept]
    :param temp_string_list: A temporary buffer storing string values from datatype restrictions before they are mapped to integers for reasoning.
    :type temp_string_list: list[str]
    :param tmp_features: A temporary list of feature names used by the DL parser to store parsed features during the knowledge base loading process.
    :type tmp_features: list[str]
    :param nodes_classification: A list of classification nodes representing the atomic concepts and their hierarchical structure derived during the classification process.
    :type nodes_classification: list[ClassificationNode]
    :param abstract_roles: A set of names for the abstract roles defined in the knowledge base, representing relationships between individuals.
    :type abstract_roles: set[str]
    :param reflexive_roles: A set of names for the reflexive roles defined in the knowledge base, indicating that every individual is related to itself via these roles.
    :type reflexive_roles: set[str]
    :param symmetric_roles: A set containing the names of the symmetric roles defined in the knowledge base.
    :type symmetric_roles: set[str]
    :param transitive_roles: Stores the names of relations in the knowledge base that satisfy the transitivity property.
    :type transitive_roles: set[str]
    :param concrete_roles: A set of names of the concrete roles (features) in the knowledge base, used to track roles that link individuals to concrete domain values.
    :type concrete_roles: set[str]
    :param functional_roles: Stores the names of the functional roles defined in the knowledge base, used during reasoning to enforce functionality constraints by merging individuals with multiple fillers for the same role.
    :type functional_roles: set[str]
    :param inverse_functional_roles: A set of names of the inverse functional roles in the knowledge base.
    :type inverse_functional_roles: set[str]
    :param similarity_relations: A set of role names representing the similarity relations defined in the knowledge base.
    :type similarity_relations: set[str]
    :param processed_assertions: A set of integer identifiers for assertions that have been processed during the reasoning process.
    :type processed_assertions: set[int]
    :param atomic_concepts: A dictionary mapping concept names to Concept objects representing the atomic fuzzy concepts in the TBox.
    :type atomic_concepts: dict[str, Concept]
    :param concept_individual_list: Maps concept identifiers to sorted sets of created individuals, used to track which individuals are associated with specific concepts during the reasoning process.
    :type concept_individual_list: dict[int, SortedSet[CreatedIndividual]]
    :param blocked_assertions: A dictionary mapping the names of blocked individuals to lists of their corresponding assertions, used to track assertions suspended during the reasoning process.
    :type blocked_assertions: dict[str, list[Assertion]]
    :param blocked_exist_assertions: A dictionary mapping the names of blocked individuals to lists of their corresponding blocked existential assertions, used to track these assertions during the reasoning process.
    :type blocked_exist_assertions: dict[str, list[Assertion]]
    :param directly_blocked_children: A dictionary mapping the name of a blocking individual to a list of names of individuals directly blocked by it, used to track and manage blocking dependencies during the reasoning process.
    :type directly_blocked_children: dict[str, list[str]]
    :param concrete_concepts: A dictionary mapping concept names to fuzzy concrete concept objects defined in the TBox.
    :type concrete_concepts: dict[str, FuzzyConcreteConcept]
    :param concrete_features: A dictionary mapping the names of concrete features to their corresponding ConcreteFeature objects in the knowledge base.
    :type concrete_features: dict[str, ConcreteFeature]
    :param disjoint_variables: Registry of variables marked as disjoint for specific concepts during reasoning to avoid redundant processing. Maps concept names to sets of variable identifiers.
    :type disjoint_variables: dict[str, set[str]]
    :param fuzzy_numbers: A dictionary mapping the names of fuzzy numbers to their corresponding TriangularFuzzyNumber objects defined in the TBox.
    :type fuzzy_numbers: dict[str, TriangularFuzzyNumber]
    :param individuals: Maps individual names to their corresponding objects, storing all individuals in the ABox, including both named and created individuals.
    :type individuals: dict[str, Individual]
    :param inverse_roles: A dictionary mapping role names to sets of their corresponding inverse role names, used to track inverse role axioms in the RBox.
    :type inverse_roles: dict[str, set[str]]
    :param labels_with_nodes: A dictionary mapping each nominal to the set of nodes in the completion forest labeled with that nominal.
    :type labels_with_nodes: dict[str, set[str]]
    :param modifiers: A dictionary mapping the names of fuzzy modifiers to their corresponding Modifier objects, representing the modifiers defined in the TBox.
    :type modifiers: dict[str, Modifier]
    :param number_of_concepts: A dictionary mapping concept names to unique integer identifiers assigned sequentially during reasoning to facilitate efficient tracking and indexing.
    :type number_of_concepts: dict[str, int]
    :param number_of_roles: A dictionary mapping role names to unique integer identifiers used for internal tracking during the reasoning process.
    :type number_of_roles: dict[str, int]
    :param t_disjoints: Stores the disjoint concept axioms from the TBox that are eligible for lazy unfolding, mapping each concept name to a set of concept names that are disjoint with it.
    :type t_disjoints: dict[str, set[str]]
    :param t_definitions: A dictionary storing concept definitions from the TBox of the form A = C that are eligible for lazy unfolding. The keys are the names of the atomic concepts, and the values are the corresponding Concept objects.
    :type t_definitions: dict[str, Concept]
    :param t_inclusions: A dictionary storing primitive concept inclusions (A is a C) from the TBox that are applicable to lazy unfolding. The keys are the names of the subsumed concepts, and the values are sets of the corresponding primitive concept definitions.
    :type t_inclusions: dict[str, set[PrimitiveConceptDefinition]]
    :param t_synonyms: A dictionary mapping atomic concept names to sets of synonymous atomic concept names, representing equivalence axioms (A = B) in the TBox used for lazy unfolding and reasoning.
    :type t_synonyms: dict[str, set[str]]
    :param temp_relations_list: A temporary dictionary mapping role names to lists of relations, used to cache an individual's relations while solving role inclusion axioms.
    :type temp_relations_list: dict[str, list[Relation]]
    :param subsumption_flags: Stores the subsumption degrees between concepts in a classified ontology, mapping each concept name to a dictionary of subsumer concept names and their associated degrees.
    :type subsumption_flags: dict[str, dict[str, float]]
    :param order: A dictionary mapping string values to integer indices, used to transform string datatype restrictions into integer restrictions for MILP processing.
    :type order: dict[str, int]
    :param truth_constants: A dictionary mapping string names to their corresponding floating-point truth constant values.
    :type truth_constants: dict[str, float]
    :param r_successors: A dictionary mapping individual names to the list of their R-successors (neighbors in the completion forest), used to track the graph structure during the reasoning process.
    :type r_successors: dict[str, list[str]]
    :param domain_restrictions: A dictionary mapping role names to sets of concepts defining their domains, used to enforce that individuals participating in a role belong to the specified concepts during reasoning.
    :type domain_restrictions: dict[str, set[Concept]]
    :param range_restrictions: A dictionary mapping role names to sets of concepts representing the range restrictions for those roles.
    :type range_restrictions: dict[str, set[Concept]]
    :param roles_with_all_parents: A dictionary mapping each role to its transitive ancestors and the corresponding fuzzy inclusion degrees, representing the transitive closure of the role hierarchy.
    :type roles_with_all_parents: dict[str, dict[str, float]]
    :param roles_with_parents: Stores the direct role hierarchy, mapping each role to a dictionary of its parent roles and the corresponding fuzzy degree of the role inclusion.
    :type roles_with_parents: dict[str, dict[str, float]]
    :param roles_with_trans_children: A dictionary mapping role names to lists of their transitive sub-roles (children) within the role hierarchy.
    :type roles_with_trans_children: dict[str, list[str]]
    :param rules_applied: A dictionary mapping each reasoning rule to the number of times it has been applied during the reasoning process.
    :type rules_applied: dict[KnowledgeBaseRules, int]
    :param x_prime_individuals: A dictionary mapping individual names to lists of their corresponding x' individuals, used to track indirect blocking conditions during the reasoning process.
    :type x_prime_individuals: dict[str, list[str]]
    :param y_prime_individuals: A dictionary of the y' individuals for indirect blocking, where the keys are the names of the individuals and the values are lists of the names of the corresponding y' individuals.
    :type y_prime_individuals: dict[str, list[str]]
    :param axioms_A_equiv_C: A dictionary mapping atomic concept names to sets of equivalent concepts, representing axioms of the form A = C.
    :type axioms_A_equiv_C: dict[str, set[Concept]]
    :param axioms_A_is_a_B: Stores primitive concept inclusion axioms of the form A is-a B, where both the subsumed concept A and the subsumer concept B are atomic. The keys are the names of the subsumed concepts A, and the values are sets of the corresponding primitive concept definitions.
    :type axioms_A_is_a_B: dict[str, set[PrimitiveConceptDefinition]]
    :param axioms_A_is_a_C: A dictionary storing primitive concept inclusion axioms where the sub-concept is atomic and the super-concept is complex. Keys are atomic concept names, and values are sets of PrimitiveConceptDefinition objects representing the axioms.
    :type axioms_A_is_a_C: dict[str, set[PrimitiveConceptDefinition]]
    :param axioms_C_is_a_A:
    :type axioms_C_is_a_A: dict[str, set[GeneralConceptInclusion]]
    :param axioms_C_is_a_D: Maps the name of the subsumed concept to a set of General Concept Inclusion objects representing axioms of the form C is a D.
    :type axioms_C_is_a_D: dict[str, set[GeneralConceptInclusion]]
    :param axioms_to_do_A_is_a_B: Stores primitive concept definitions of the form A isA B that are pending lazy unfolding or absorption processing during TBox preprocessing.
    :type axioms_to_do_A_is_a_B: dict[str, set[PrimitiveConceptDefinition]]
    :param axioms_to_do_A_is_a_C: A dictionary of primitive concept definitions A is a C pending processing for lazy unfolding or absorption during TBox preprocessing.
    :type axioms_to_do_A_is_a_C: dict[str, set[PrimitiveConceptDefinition]]
    :param axioms_to_do_C_is_a_A: A temporary dictionary holding General Concept Inclusions of the form C isA A that are pending transformation or absorption during TBox preprocessing. The keys are the names of the atomic concepts A, and the values are sets of the corresponding GeneralConceptInclusion objects.
    :type axioms_to_do_C_is_a_A: dict[str, set[GeneralConceptInclusion]]
    :param axioms_to_do_C_is_a_D: Holds General Concept Inclusions of the form C is a D pending processing for lazy unfolding or transformation during TBox preprocessing.
    :type axioms_to_do_C_is_a_D: dict[str, set[GeneralConceptInclusion]]
    :param axioms_to_do_tmp_A_is_a_C: A temporary dictionary of TBox axioms of the form A is a C that are candidates for lazy unfolding, used as a buffer during GCI transformations. Keys are concept names and values are sets of primitive concept definitions.
    :type axioms_to_do_tmp_A_is_a_C: dict[str, set[PrimitiveConceptDefinition]]
    :param axioms_to_do_tmp_C_is_a_A: Temporary buffer for General Concept Inclusions of the form C isA A generated during the GCI transformation phase, mapping atomic concept names to sets of axioms to be processed in the next iteration.
    :type axioms_to_do_tmp_C_is_a_A: dict[str, set[GeneralConceptInclusion]]
    :param axioms_to_do_tmp_C_is_a_D: A temporary dictionary acting as a buffer for General Concept Inclusions of the form C isA D generated during TBox preprocessing, where the keys are the names of the subsumed concepts and the values are sets of the corresponding axioms.
    :type axioms_to_do_tmp_C_is_a_D: dict[str, set[GeneralConceptInclusion]]

    :raises InconsistentOntologyException: Raised when the knowledge base is determined to be unsatisfiable or inconsistent, typically due to contradictory axioms such as the universal concept being subsumed by the bottom concept.
    :raises ValueError: Raised when a method is called with an invalid number of arguments for its supported overloads, or when an unsupported concept or modifier type is encountered during reasoning.
    """

    def __init__(self) -> None:
        """Initializes a new instance of the KnowledgeBase class, setting up the necessary data structures to represent a Description Logic ontology. This constructor resets the global variable counter to zero and instantiates a helper object for Mixed-Integer Linear Programming (MILP). It configures default reasoning parameters, such as the maximum depth of the completion forest and the blocking strategy, while initializing empty collections for storing concepts, roles, individuals, axioms, and classification results. Additionally, it establishes various flags and counters to track the state of the knowledge base, including whether it has been loaded, classified, or determined to be unsatisfiable."""

        Variable.VARIABLE_NUMBER = 0

        # DL language
        self.language: str = ""

        # MILP problem manager
        self.milp: MILPHelper = MILPHelper()

        # Type of the blocking that must be checked for this KB
        self.blocking_type: BlockingDynamicType = BlockingDynamicType.DOUBLE_BLOCKING

        # Maximal depth of the completion forest
        self.max_depth: int = 1
        # Number of assertions
        self.num_assertions: int = 0
        # Number of new concepts
        self.num_defined_concepts: int = 0
        # Number of new individuals
        self.num_defined_individuals: int = 0
        # Number of relations
        self.num_relations: int = 0
        # Number of variables that the old calculus would create
        self.old_01_variables: int = 0
        self.old_binary_variables: int = 0

        # Classified ontology
        self.CLASSIFIED: bool = False
        # ABox completely expanded
        self.ABOX_EXPANDED: bool = False
        # KB completely loaded from file
        self.KB_LOADED: bool = False
        # true: unsatisfiable KB; false: satisfiable KB or unknown
        self.KB_UNSAT: bool = False
        # Concrete fuzzy concepts
        self.concrete_fuzzy_concepts: bool = False
        # Already lazy unfoldable
        self.lazy_unfondable: bool = False
        # Show the logic language to the user or not
        self.show_language: bool = False
        # Acyclic TBox
        self.acyclic_tbox: bool = False
        # Dynamism of blocking
        self.blocking_dynamic: bool = False
        # Rule acyclic TBox
        self.rule_acyclic_tbox: bool = False

        # Appplications of the transitive funcRole rule
        self.applied_trans_role_rules: list[str] = []
        # Fuzzy assertions
        self.assertions: list[Assertion] = []
        # Exists assertions
        self.exist_assertions: list[Assertion] = []
        # Positive datatype restrictions
        self.positive_concrete_value_assertions: list[Assertion] = []
        # Part of the TBox to which we cannot apply lazy unfolding
        self.t_G: list[GeneralConceptInclusion] = []
        # Equivalent concepts C = D
        self.axioms_C_equiv_D: list[ConceptEquivalence] = []
        # Used by string datatypes
        self.temp_string_concept_list: list[Concept] = []
        # Used by string datatypes
        self.temp_string_list: list[str] = []
        # Used by DL parser to memorize the features parsed
        self.tmp_features: list[str] = []
        # Classified atomic concepts
        self.nodes_classification: list[ClassificationNode] = list()

        # Abstract roles
        self.abstract_roles: set[str] = set()
        # Reflexive roles
        self.reflexive_roles: set[str] = set()
        # Symmetric roles
        self.symmetric_roles: set[str] = set()
        # Transitive roles
        self.transitive_roles: set[str] = set()
        # Concrete roles
        self.concrete_roles: set[str] = set()
        # Functional roles
        self.functional_roles: set[str] = set()
        # Inverse functional roles
        self.inverse_functional_roles: set[str] = set()
        # Similarity relations
        self.similarity_relations: set[str] = set()
        # Processed assertion
        self.processed_assertions: set[int] = set()

        # Fuzzy concepts
        self.atomic_concepts: dict[str, Concept] = dict()
        # Set of created individuals that have a concept in the concept list conceptList
        self.concept_individual_list: dict[int, SortedSet[CreatedIndividual]] = dict()
        # Blocked assertions
        self.blocked_assertions: dict[str, list[Assertion]] = dict()
        # Blocked existential assertions
        self.blocked_exist_assertions: dict[str, list[Assertion]] = dict()
        # Direcyly blocked children
        self.directly_blocked_children: dict[str, list[str]] = dict()
        # Fuzzy concrete concepts
        self.concrete_concepts: dict[str, FuzzyConcreteConcept] = dict()
        # Concrete features
        self.concrete_features: dict[str, ConcreteFeature] = dict()
        # Disjoint variables
        self.disjoint_variables: dict[str, set[str]] = dict()
        # Fuzzy numbers
        self.fuzzy_numbers: dict[str, TriangularFuzzyNumber] = dict()
        # Individuals
        self.individuals: dict[str, Individual] = dict()
        # Inverse roles
        self.inverse_roles: dict[str, set[str]] = dict()
        # For every nominal in a node, a list of the nodes where it appears
        self.labels_with_nodes: dict[str, set[str]] = dict()
        # Fuzzy modifiers
        self.modifiers: dict[str, Modifier] = dict()
        # Assigns a number to a concept name
        self.number_of_concepts: dict[str, int] = dict()
        # Assigns a number to a role name
        self.number_of_roles: dict[str, int] = dict()
        # Part of the TBox with disjoitn axioms which we can apply lazy unfolding
        self.t_disjoints: dict[str, set[str]] = dict()
        # Part of the TBox with axioms A = C to which we can apply lazy unfolding
        self.t_definitions: dict[str, Concept] = dict()
        # Part of the TBox with axioms A isA C to which we can apply lazy unfolding
        self.t_inclusions: dict[str, set[PrimitiveConceptDefinition]] = dict()
        # GCIs of the form A = B with both A and B being atomic
        self.t_synonyms: dict[str, set[str]] = dict()
        # Used by string datatypes
        self.temp_relations_list: dict[str, list[Relation]] = dict()
        # Subsumption degrees in classified ontologies
        self.subsumption_flags: dict[str, dict[str, float]] = dict()

        # Strings appearing in concrete concepts and their associated real numbers
        self.order: dict[str, int] = dict()
        self.truth_constants: dict[str, float] = dict()
        # R-successors
        self.r_successors: dict[str, list[str]] = dict()
        # Domain restrictions
        self.domain_restrictions: dict[str, set[Concept]] = dict()
        # Range restrictions
        self.range_restrictions: dict[str, set[Concept]] = dict()
        # All parents for a role constructed from all role inclusions in KB
        self.roles_with_all_parents: dict[str, dict[str, float]] = dict()
        # Direct parents of a role directly defined
        self.roles_with_parents: dict[str, dict[str, float]] = dict()
        # Transitive childrens of a role
        self.roles_with_trans_children: dict[str, list[str]] = dict()

        # Number of application of the rules
        self.rules_applied: dict[KnowledgeBaseRules, int] = {
            rule: 0 for rule in list(KnowledgeBaseRules)
        }

        # x' individuals for indirect blocking
        self.x_prime_individuals: dict[str, list[str]] = dict()
        # y' individuals for indirect blocking
        self.y_prime_individuals: dict[str, list[str]] = dict()

        # Definitions A = C
        self.axioms_A_equiv_C: dict[str, set[Concept]] = dict()
        # Primitive concept definitions A isA B
        self.axioms_A_is_a_B: dict[str, set[PrimitiveConceptDefinition]] = dict()
        # Primitive concept definitions A isA C.
        self.axioms_A_is_a_C: dict[str, set[PrimitiveConceptDefinition]] = dict()
        # Primitive concept definitions C isA A
        self.axioms_C_is_a_A: dict[str, set[GeneralConceptInclusion]] = dict()
        # GCIs C isA D
        self.axioms_C_is_a_D: dict[str, set[GeneralConceptInclusion]] = dict()

        # Part of the TBox with axioms A isA B and A isa C for further absorption processing
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
        """
        Creates and returns a deep copy of the current `KnowledgeBase` instance, ensuring that the new object is independent of the original. The method initiates the copy by generating a clone of the base structure without the ABox via `clone_without_abox`, then systematically reconstructs the ABox by duplicating all assertions, individuals, and nominal nodes. Additionally, it replicates internal components such as the MILP model, blocking states, parser-specific data, and statistical counters, using deep copies or element-wise cloning where necessary to preserve the integrity of complex nested structures.

        :return: A deep copy of the current knowledge base instance, including all assertions, individuals, and internal state.

        :rtype: typing.Self
        """

        kb: KnowledgeBase = self.clone_without_abox()

        # Clone assertions
        kb.assertions = [ass.clone() for ass in self.assertions]

        # Clone individuals
        kb.individuals = {i: indiv.clone() for i, indiv in self.individuals.items()}

        # Cloner nominal nodes
        kb.labels_with_nodes = copy.deepcopy(self.labels_with_nodes)

        # Clone milp
        kb.milp = self.milp.clone()

        # Clone blocking
        kb.blocked_assertions = {
            k: [a.clone() for a in ass] for k, ass in self.blocked_assertions.items()
        }
        kb.blocked_exist_assertions = {
            k: [a.clone() for a in ass]
            for k, ass in self.blocked_exist_assertions.items()
        }
        kb.directly_blocked_children = copy.deepcopy(self.directly_blocked_children)
        kb.num_defined_concepts = self.num_defined_concepts
        kb.num_defined_individuals = self.num_defined_individuals
        kb.r_successors = copy.deepcopy(self.r_successors)
        kb.x_prime_individuals = copy.deepcopy(self.x_prime_individuals)
        kb.y_prime_individuals = copy.deepcopy(self.y_prime_individuals)

        # Clone data used by DL parser
        kb.tmp_features = copy.deepcopy(self.tmp_features)
        kb.truth_constants = copy.deepcopy(self.truth_constants)

        # Clone statistics
        kb.max_depth = self.max_depth
        kb.num_assertions = self.num_assertions
        kb.num_relations = self.num_relations
        kb.old_01_variables = self.old_01_variables
        kb.old_binary_variables = self.old_binary_variables
        kb.rules_applied = copy.deepcopy(self.rules_applied)

        return kb

    def clone_without_abox(self) -> typing.Self:
        """
        Creates a copy of the knowledge base that preserves the TBox (terminological axioms), RBox (role definitions), and configuration settings while excluding the ABox (assertional data). The method instantiates a new `KnowledgeBase` and transfers the state by deep copying primitive attributes and invoking clone methods on complex objects like concepts, axioms, and roles to ensure the new instance is independent of the original. It also replicates processing flags and internal data structures used by the parser and reasoner, returning a fully initialized clone of the schema.

        :return: Returns a new KnowledgeBase instance that is a copy of the current instance, containing the TBox (terminology), RBox (roles), and configuration, but excluding the ABox (assertions about individuals).

        :rtype: typing.Self
        """

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
        kb.CLASSIFIED = self.CLASSIFIED

        # Clone data used by DL parser
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
        kb.subsumption_flags = copy.deepcopy(self.subsumption_flags)
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
        """
        Serializes the current state of the fuzzy Knowledge Base into a structured text format and writes it to the specified file. If the file name argument is None, the output is printed to the console instead of being written to disk. The output encompasses the fuzzy logic definition, concrete concepts, modifiers, features with their specific ranges, ABox assertions (instances and relations), TBox axioms, and RBox properties including role hierarchies and characteristics. It handles various feature types and filters specific assertions based on their degree values. The operation opens the file in write mode, potentially overwriting existing data, and utilizes a general exception handler to report any errors encountered during the writing process.

        :param file_name: The path to the file where the knowledge base will be saved. If None, the output is printed to the console.
        :type file_name: str
        """

        try:
            with open(file_name, "w") if file_name else None as f:
                output = f.write if f else print

                # Fuzzy logic
                output(f"(define-fuzzy-logic {constants.KNOWLEDGE_BASE_SEMANTICS})")

                # Save concrete concepts
                for c in self.concrete_concepts.values():
                    output(f"(define-fuzzy-concept {c.name} {c.compute_name()})")

                # Save modifiers
                for mod in self.modifiers.values():
                    output(f"(define-modifier {mod} {mod.compute_name()})")

                # Save features
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

                # Save ABox
                for ass in self.assertions:
                    deg: str = self.degree_if_not_one(ass.get_lower_limit())
                    if ":" in deg:
                        continue
                    output(
                        f"(instance {ass.get_individual()} {ass.get_concept()} {deg})"
                    )

                for ind in self.individuals.values():
                    for relations in ind.role_relations.values():
                        for rel in relations:
                            deg: str = self.degree_if_not_one(rel.get_degree())
                            if ":" in deg:
                                continue
                            output(
                                f"(related {ind} {rel.get_object_individual()} {rel.get_role_name()} {deg})"
                            )

                # Save TBox
                if self.KB_LOADED:
                    self.save_absorbed_tbox_to_file(output)
                else:
                    self.save_tbox_to_file(output)

                # Save RBox
                for r in self.reflexive_roles:
                    output(f"(reflexive {r})")

                for r in self.symmetric_roles:
                    output(f"(symmetric {r})")

                for r in self.transitive_roles:
                    output(f"(transitive {r})")

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
        """
        Serializes the absorbed TBox component of the fuzzy knowledge base into a structured text format by delegating the writing process to a provided callable. The method iterates through internal representations of primitive concept inclusions, concept definitions, synonyms, and General Concept Inclusions (GCIs), formatting them into a specific Lisp-like syntax. It handles fuzzy logic degrees by omitting them if they equal 1.0 and dynamically selects the appropriate implication operator (e.g., Lukasiewicz, Godel) based on the specific logic type of each inclusion. The process concludes by invoking `save_tbox_common_part_to_file` to append any shared TBox information to the output.

        :param output: A callable that accepts a string and writes it to the desired destination, such as a file handle or the console.
        :type output: typing.Callable
        """

        for atomic_concept, pcds in self.t_inclusions.items():
            for pcd in pcds:
                c: Concept = pcd.get_definition()
                deg: float = pcd.get_degree()
                if deg == 1.0:
                    output(f"(define-primitive-concept {atomic_concept} {c})")
                else:
                    output(f"(define-primitive-concept {atomic_concept} {c} {deg})")
                # continue
                # implies_type: str = None
                # if pcd.get_type() == LogicOperatorType.LUKASIEWICZ:
                #     implies_type = "l-implies"
                # elif pcd.get_type() == LogicOperatorType.GOEDEL:
                #     implies_type = "g-implies"
                # elif pcd.get_type() == LogicOperatorType.KLEENE_DIENES:
                #     implies_type = "kd-implies"
                # elif pcd.get_type() == LogicOperatorType.ZADEH:
                #     implies_type = "implies"
                # output(f"({implies_type} {atomic_concept} {c} {deg})")

        for atomic_concept, concept in self.t_definitions.items():
            output(f"(equivalent-concepts {atomic_concept} {concept})")

        for atomic_concept, concepts in self.t_synonyms.items():
            for c in concepts:
                output(f"(equivalent-concepts {atomic_concept} {c})")

        for gci in self.t_G:
            implies_type: str = None
            deg: str = self.degree_if_not_one(gci.get_degree()).strip()
            if gci.get_type() == LogicOperatorType.LUKASIEWICZ:
                implies_type = "l-implies"
            elif gci.get_type() == LogicOperatorType.GOEDEL:
                implies_type = "g-implies"
            elif gci.get_type() == LogicOperatorType.KLEENE_DIENES:
                implies_type = "kd-implies"
            elif gci.get_type() == LogicOperatorType.ZADEH:
                implies_type = "implies"
            if deg != "":
                output(
                    f"({implies_type} {gci.get_subsumed()} {gci.get_subsumer()} {deg})"
                )
            else:
                output(f"({implies_type} {gci.get_subsumed()} {gci.get_subsumer()})")

        self.save_tbox_common_part_to_file(output)

    def save_tbox_to_file(self, output: typing.Callable) -> None:
        """
        Serializes the terminological component (TBox) of the fuzzy knowledge base into a structured text format by delegating the actual writing to a provided callback function. The method iterates through various categories of axioms, including concept equivalences, primitive concept definitions, and general concept inclusions, converting them into a Lisp-like syntax. It specifically handles fuzzy logic degrees by omitting the degree value if it equals 1.0 and maps internal logic operator types to their corresponding string representations, such as "l-implies" for Lukasiewicz logic. The process concludes by invoking a helper method to output any remaining common TBox components.

        :param output: A callable that accepts a string and writes it to the desired destination, such as a file or standard output.
        :type output: typing.Callable
        """

        for atomic_concept, concepts in self.axioms_A_equiv_C.items():
            for c in concepts:
                output(f"(define-concept {atomic_concept} {c})")

        for atomic_concept, pcds in self.axioms_A_is_a_B.items():
            for pcd in pcds:
                c: Concept = pcd.get_definition()
                deg: float = pcd.get_degree()
                if deg == 1.0:
                    output(f"(define-primitive-concept {atomic_concept} {c})")
                    # continue
                else:
                    output(f"(define-primitive-concept {atomic_concept} {c} {deg})")
                # implies_type: str = None
                # if pcd.get_type() == LogicOperatorType.LUKASIEWICZ:
                #     implies_type = "l-implies"
                # elif pcd.get_type() == LogicOperatorType.GOEDEL:
                #     implies_type = "g-implies"
                # elif pcd.get_type() == LogicOperatorType.KLEENE_DIENES:
                #     implies_type = "kd-implies"
                # elif pcd.get_type() == LogicOperatorType.ZADEH:
                #     implies_type = "implies"
                # output(f"({implies_type} {atomic_concept} {c} {deg})")

        for atomic_concept, pcds in self.axioms_A_is_a_C.items():
            for pcd in pcds:
                c: Concept = pcd.get_definition()
                deg: float = pcd.get_degree()
                if deg == 1.0:
                    output(f"(define-primitive-concept {atomic_concept} {c})")
                    # continue
                else:
                    output(f"(define-primitive-concept {atomic_concept} {c} {deg})")
                # implies_type: str = None
                # if pcd.get_type() == LogicOperatorType.LUKASIEWICZ:
                #     implies_type = "l-implies"
                # elif pcd.get_type() == LogicOperatorType.GOEDEL:
                #     implies_type = "g-implies"
                # elif pcd.get_type() == LogicOperatorType.KLEENE_DIENES:
                #     implies_type = "kd-implies"
                # elif pcd.get_type() == LogicOperatorType.ZADEH:
                #     implies_type = "implies"
                # output(f"({implies_type} {atomic_concept} {c} {deg})")

        for gcis in self.axioms_C_is_a_D.values():
            for gci in gcis:
                implies_type: str = None
                deg: str = self.degree_if_not_one(gci.get_degree()).strip()
                if gci.get_type() == LogicOperatorType.LUKASIEWICZ:
                    implies_type = "l-implies"
                elif gci.get_type() == LogicOperatorType.GOEDEL:
                    implies_type = "g-implies"
                elif gci.get_type() == LogicOperatorType.KLEENE_DIENES:
                    implies_type = "kd-implies"
                elif gci.get_type() == LogicOperatorType.ZADEH:
                    implies_type = "implies"
                if deg != "":
                    output(
                        f"({implies_type} {gci.get_subsumed()} {gci.get_subsumer()} {deg})"
                    )
                else:
                    output(
                        f"({implies_type} {gci.get_subsumed()} {gci.get_subsumer()})"
                    )

        for gcis in self.axioms_C_is_a_A.values():
            for gci in gcis:
                implies_type: str = None
                deg: str = self.degree_if_not_one(gci.get_degree()).strip()
                if gci.get_type() == LogicOperatorType.LUKASIEWICZ:
                    implies_type = "l-implies"
                elif gci.get_type() == LogicOperatorType.GOEDEL:
                    implies_type = "g-implies"
                elif gci.get_type() == LogicOperatorType.KLEENE_DIENES:
                    implies_type = "kd-implies"
                elif gci.get_type() == LogicOperatorType.ZADEH:
                    implies_type = "implies"
                if deg != "":
                    output(
                        f"({implies_type} {gci.get_subsumed()} {gci.get_subsumer()} {deg})"
                    )
                else:
                    output(
                        f"({implies_type} {gci.get_subsumed()} {gci.get_subsumer()})"
                    )

        for ce in self.axioms_C_equiv_D:
            output(f"(equivalent-concepts {ce.get_c1()} {ce.get_c2()})")

        self.save_tbox_common_part_to_file(output)

    def save_tbox_common_part_to_file(self, output: typing.Callable) -> None:
        """
        Writes the common TBox axioms—specifically disjoint concept assertions, domain restrictions, and range restrictions—to a destination defined by a provided callable. The method iterates through the knowledge base's internal collections of disjoint sets and role restrictions, formatting each entry into a string representation and passing it to the output function. To prevent redundancy, disjoint concept pairs are only emitted if the first concept is lexicographically or numerically smaller than the second. This design decouples the serialization logic from the specific output mechanism, enabling the data to be written to files, buffers, or other streams.

        :param output: A callable that accepts a string and writes it to the intended destination (e.g., a file or standard output).
        :type output: typing.Callable
        """

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

    def write_object_to_file(self, file_path: str) -> None:
        """
        Serializes the current `KnowledgeBase` instance to a binary file located at the specified path using the `pickle` module, enabling the object's state to be persisted for later use. This method opens the target file in write-binary mode, which will create the file if it does not exist or completely overwrite any existing file at that location. Care should be taken to ensure that the object does not contain unpicklable elements, such as open file handles or database connections, as attempting to serialize such data will result in an error.

        :param file_path: Path to the file where the pickled object will be written.
        :type file_path: str
        """

        with open(file_path, "wb") as file:
            pickle.dump(self, file)

    def read_object_from_file(self, file_path: str) -> KnowledgeBase:
        """
        Deserializes a KnowledgeBase instance from the specified file path using the pickle module. The method opens the file in binary read mode, reconstructs the object, and updates the global KNOWLEDGE_BASE_SEMANTICS constant with the logic semantics retrieved from the loaded instance. It returns the deserialized knowledge base, provided the file contains valid data; otherwise, standard file I/O or unpickling errors may occur.

        :param file_path: Path to the file from which to load the pickled KnowledgeBase object.
        :type file_path: str

        :return: The KnowledgeBase object deserialized from the specified file.

        :rtype: KnowledgeBase
        """

        with open(file_path, "rb") as file:
            kb = pickle.load(file, encoding="utf-8")
        kb = typing.cast(KnowledgeBase, kb)
        constants.KNOWLEDGE_BASE_SEMANTICS = kb.get_logic()
        return kb

    def get_individuals(self) -> dict[str, Individual]:
        """
        Retrieves the complete collection of individuals currently managed by the Knowledge Base, returning a dictionary that maps string identifiers to their corresponding Individual objects. Because this method returns a direct reference to the internal storage rather than a copy, any modifications made to the returned dictionary will directly affect the state of the Knowledge Base.

        :return: A dictionary mapping string identifiers to all `Individual` objects currently stored in the knowledge base.

        :rtype: dict[str, Individual]
        """

        return self.individuals

    def get_named_individuals(self) -> list[Individual]:
        """
        Retrieves a list of all individuals within the knowledge base that are classified as named entities, effectively filtering out any that are considered blockable. The method iterates over the internal collection of individuals and returns a new list containing only those for which the blockable condition is false. This operation is read-only and does not modify the state of the knowledge base or the individual objects; if no such individuals exist, an empty list is returned.

        :return: A list of all named (non-blockable) individuals in the knowledge base.

        :rtype: list[Individual]
        """

        return [i for i in self.individuals.values() if not i.is_blockable()]

    def add_tmp_feature(self, feature: str) -> None:
        """
        Registers a feature string to the knowledge base's temporary feature storage, typically utilized during the parsing phase. The method enforces uniqueness by checking if the feature already exists in the temporary collection; if a duplicate is detected, an error is raised. As a side effect, the provided feature is appended to the internal list of temporary features, modifying the object's state.

        :param feature: The feature identifier to be added. It must be unique within the temporary features list, or an error will be raised.
        :type feature: str
        """

        if feature in self.tmp_features:
            Util.error(f"Feature {feature} has already defined.")
        self.tmp_features.append(feature)

    def get_tmp_feature(self, feature: str) -> str:
        """
        Retrieves a specific temporary feature from the internal storage, removing it from the collection upon retrieval. This destructive read operation ensures that the feature is consumed and cannot be accessed again in subsequent calls. If the requested feature has not been defined or is not present in the temporary features list, the method triggers an error condition.

        :param feature: The name of the temporary feature to retrieve and remove from the parser's storage.
        :type feature: str

        :return: The requested feature, removed from the temporary features collection.

        :rtype: str
        """

        if feature not in self.tmp_features:
            Util.error(f"Feature {feature} has to be defined before.")
        return self.tmp_features.pop(self.tmp_features.index(feature))

    def set_truth_constants(self, s: str, w: float) -> None:
        """
        Registers a truth constant within the knowledge base by mapping a string identifier to a floating-point value. This operation enforces strict uniqueness for constant names; if the provided identifier already exists in the current set of truth constants, the method triggers an error to prevent redefinition. If the identifier is unique, it is added to the internal dictionary, making the constant available for subsequent logical operations or queries.

        :param s: The unique identifier for the truth constant to be defined.
        :type s: str
        :param w: The floating-point value to assign to the truth constant.
        :type w: float
        """

        if s in self.truth_constants:
            Util.error(f"Error: Truth constant {s} already defined.")
        self.truth_constants[s] = w

    def get_truth_constants(self, s: str) -> typing.Optional[float]:
        """
        Retrieves the numeric value associated with a specific truth constant name stored in the knowledge base. This method queries the internal mapping of truth constants using the provided string identifier. If the identifier exists, the corresponding floating-point value is returned; if the identifier is not found, the method returns None. This operation performs a read-only lookup and does not modify the state of the knowledge base.

        :param s: The name of the truth constant to retrieve.
        :type s: str

        :return: The numeric value associated with the specified truth constant name, or None if the constant is not defined.

        :rtype: typing.Optional[float]
        """

        return self.truth_constants.get(s)

    def add_individual(self, ind_name: str, ind: Individual) -> None:
        """
        Registers a specific individual instance within the knowledge base under the provided name, updating the internal registry of individuals. If an individual with the same name already exists, it will be overwritten by this operation. Additionally, if the knowledge base is currently loaded, the method triggers reasoning tasks for the new individual, specifically resolving General Concept Inclusions and processing reflexive roles.

        :param ind_name: The unique name or identifier for the individual.
        :type ind_name: str
        :param ind: The `Individual` object to be added to the knowledge base.
        :type ind: Individual
        """

        self.individuals[ind_name] = ind
        if self.is_loaded():
            self.solve_gci(ind)
            self.solve_reflexive_roles(ind)

    def add_created_individual(self, ind_name: str, ind: CreatedIndividual) -> None:
        """
        Registers a CreatedIndividual instance within the knowledge base, mapping it to the provided name for future retrieval. This method updates the internal state of the knowledge base by storing the individual in its registry. Additionally, if the knowledge base is in a loaded state and the individual is not concrete, the method triggers side effects by executing inference logic to resolve General Concept Inclusions (GCI) and reflexive roles associated with the new individual.

        :param ind_name: The unique name or identifier used as the key for the created individual in the knowledge base.
        :type ind_name: str
        :param ind: The individual object to be added to the knowledge base.
        :type ind: CreatedIndividual
        """

        self.individuals[ind_name] = ind
        if self.is_loaded() and not ind.is_concrete():
            self.solve_gci(ind)
            self.solve_reflexive_roles(ind)

    def get_individual(
        self, ind_name: str
    ) -> typing.Union[Individual, CreatedIndividual]:
        """
        Retrieves an individual entity from the knowledge base corresponding to the specified name. If the individual does not already exist within the base, a new instance is created, registered internally, and returned. This method ensures that a valid individual object is always available for the given identifier, modifying the knowledge base's state only when necessary to accommodate new entities.

        :param ind_name: Name identifying the individual to retrieve or create.
        :type ind_name: str

        :return: The Individual object with the specified name. If the individual does not exist, a new one is created, stored, and returned.

        :rtype: typing.Union[Individual, CreatedIndividual]
        """

        if self.check_individual_exists(ind_name):
            return self.individuals.get(ind_name)
        ind: Individual = Individual(ind_name)
        self.add_individual(ind_name, ind)
        return ind

    def check_individual_exists(self, ind_name: str) -> bool:
        """
        Verifies the presence of an individual entity identified by the provided name within the knowledge base's internal registry. The method evaluates the collection of stored individuals to determine if the specific identifier exists, returning True if found and False otherwise. This check accounts for scenarios where the registry is empty or the name is simply absent. The operation is read-only and does not alter the state of the knowledge base or its contained entities.

        :param ind_name: The name of the individual to check for existence.
        :type ind_name: str

        :return: True if an individual with the given name exists, False otherwise.

        :rtype: bool
        """

        if len(self.individuals) == 0 or ind_name not in self.individuals:
            return False
        return True

    def add_concept(self, concept_name: str, conc: FuzzyConcreteConcept) -> None:
        """
        Adds a fuzzy concrete concept to the knowledge base, mapping the provided name to the specific concept object. This operation updates the internal dictionary of concrete concepts, potentially overwriting any existing concept associated with the same name. Additionally, the method checks for naming conflicts with existing roles; if the name is already in use by an abstract or concrete role, a warning is issued to indicate the overlap.

        :param concept_name: The unique identifier used as the key to store the fuzzy concept in the knowledge base.
        :type concept_name: str
        :param conc: The concrete fuzzy concept instance to be stored in the knowledge base.
        :type conc: FuzzyConcreteConcept
        """

        if concept_name in self.abstract_roles or concept_name in self.concrete_roles:
            Util.warning(
                f"Warning: {concept_name} is the name of both a concept and a role."
            )
        self.concrete_concepts[concept_name] = conc

    def concept_exists(self, name: str) -> bool:
        """
        Determines if a concept with the given name is present in the knowledge base by searching through both the atomic concepts and concrete concepts dictionaries. The method returns True if the name is found in either collection, and False if it is absent from both. This is a non-destructive query that does not alter the state of the knowledge base or its stored data.

        :param name: The identifier of the concept to check for existence.
        :type name: str

        :return: True if a concept with the specified name exists, False otherwise.

        :rtype: bool
        """

        return (
            self.atomic_concepts.get(name) or self.concrete_concepts.get(name)
        ) is not None

    def get_concept(self, name: str) -> Concept:
        """
        Retrieves a concept from the knowledge base using the specified name, searching through both atomic and concrete concepts. If the concept does not already exist, a new AtomicConcept is instantiated, registered within the knowledge base, and returned. Additionally, the method checks for naming conflicts with existing abstract or concrete roles and issues a warning if the provided name is currently in use by a role.

        :param name: The identifier for the concept to retrieve. If a concept with this name does not exist, a new AtomicConcept is created and stored.
        :type name: str

        :return: The concept with the specified name. If the concept does not already exist, a new AtomicConcept is created and returned.

        :rtype: Concept
        """

        c: Concept = self.atomic_concepts.get(name) or self.concrete_concepts.get(name)
        if c is not None:
            return c
        if name in self.abstract_roles or name in self.concrete_roles:
            Util.warning(f"Warning: {name} is the name of both a concept and a role.")

        c: Concept = AtomicConcept(name)
        self.atomic_concepts[name] = c
        return c

    def add_fuzzy_number(self, f_name: str, f: TriangularFuzzyNumber) -> None:
        """
        Registers a triangular fuzzy number within the knowledge base, associating it with a specific string identifier. This method updates the internal state by storing the fuzzy number in the dedicated `fuzzy_numbers` dictionary for direct lookup, while also integrating it into the broader conceptual framework through a call to `add_concept`. Consequently, the fuzzy number becomes available for subsequent operations and queries within the system.

        :param f_name: The name or identifier used to label and store the fuzzy number in the knowledge base.
        :type f_name: str
        :param f: The triangular fuzzy number instance to be stored in the knowledge base.
        :type f: TriangularFuzzyNumber
        """

        self.add_concept(f_name, f)
        self.fuzzy_numbers[f_name] = f

    def check_fuzzy_number_concept_exists(self, conc_name: str) -> bool:
        """
        Verifies whether a concept with the specified name is defined as a fuzzy number within the knowledge base. The method first checks for the existence of the concept name in the collection of concrete concepts; if found, it further validates that the concept's type is explicitly `FUZZY_NUMBER`. It returns `False` if the concept is missing or if the type does not match, and the operation does not modify the state of the knowledge base.

        :param conc_name: The name of the fuzzy number concept to verify.
        :type conc_name: str

        :return: True if a concept with the given name exists and is of type fuzzy number; otherwise, False.

        :rtype: bool
        """

        if conc_name not in self.concrete_concepts:
            return False
        c: Concept = self.concrete_concepts.get(conc_name)
        return c.type == ConceptType.FUZZY_NUMBER

    def add_modifier(self, mod_name: str, mod: Modifier) -> None:
        """
        Registers a fuzzy logic modifier within the knowledge base, associating it with a specific string identifier for later reference. The method ensures uniqueness by checking if a modifier with the provided name already exists; if a duplicate is detected, an error is triggered to prevent overwriting. Upon successful validation, the modifier object is stored in the internal collection, updating the state of the knowledge base.

        :param mod_name: The unique name used to identify and store the fuzzy modifier.
        :type mod_name: str
        :param mod: The fuzzy modifier instance to be stored in the knowledge base.
        :type mod: Modifier
        """

        if mod_name in self.modifiers:
            Util.error(f"Error: {mod_name} modifier is already defined")
        else:
            self.modifiers[mod_name] = mod

    def add_assertions(self, list_of_assertions: list[Assertion]) -> None:
        """
        Appends a collection of fuzzy assertions to the internal storage of the knowledge base. This method modifies the instance state by extending the existing list of assertions with the provided items, allowing for batch updates. It does not enforce uniqueness or perform validation on the input list beyond the type hint, meaning duplicates will be added and an empty input list will result in no changes.

        :param list_of_assertions: A list of fuzzy assertions to append to the existing collection.
        :type list_of_assertions: list[Assertion]
        """

        self.assertions.extend(list_of_assertions)

    @typing.overload
    def add_assertion(self, new_ass: Assertion) -> None: ...

    @typing.overload
    def add_assertion(self, a: Individual, c: Concept, n: Degree) -> None: ...

    @typing.overload
    def add_assertion(self, a: Individual, restrict: Restriction) -> None: ...

    def add_assertion(self, *args) -> None:
        """
        Incorporates a fuzzy assertion into the knowledge base using a flexible argument structure that supports multiple invocation patterns. The method allows for the addition of a pre-constructed `Assertion` object, the association of an `Individual` with a `Concept` and a fuzzy `Degree`, or the linking of an `Individual` to a `Restriction`. It validates the count and types of the provided arguments to route the call to the appropriate internal handler. If the arguments do not conform to the expected signatures, an `AssertionError` or `ValueError` is raised. This operation modifies the internal state of the knowledge base by persisting the new assertion.

        :param args: Variable-length arguments defining the fuzzy assertion, accepting either an existing Assertion object, or components to construct one: an Individual and a Restriction, or an Individual, Concept, and Degree.
        :type args: typing.Any

        :raises ValueError: Raised when the provided arguments do not match any of the supported signatures: an Assertion, an Individual with a Restriction, or an Individual with a Concept and a Degree.
        """

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
        """
        Adds a fuzzy assertion to the knowledge base, performing validation and state updates based on the assertion's properties and processing status. If the assertion's lower degree limit is zero, the method returns immediately without taking further action. For assertions that have already been processed, the method adds a corresponding constraint to the internal MILP model rather than storing the assertion again. For new assertions, the method increments the assertion counter, stores the assertion in the internal list, and updates the associated individual and concept mappings; specifically, if the concept is not the universal concept and the individual is blockable, it adds the concept to the individual's list, sets the individual's blocking status to "UNCHECKED", and registers the individual under the concept.

        :param new_ass: The fuzzy assertion to be processed and integrated, either by adding it to the internal list or generating a MILP constraint.
        :type new_ass: Assertion
        """

        deg: Degree = new_ass.get_lower_limit()
        if deg.is_numeric() and deg.is_number_zero():
            return
        if self.is_assertion_processed(new_ass):
            Util.debug(f"Assertion (without the degree): {new_ass} already processed")
            # Add xNewAss >= lowerBound
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
        """
        This internal helper method adds a fuzzy assertion to the knowledge base, representing the statement that a specific individual belongs to a concept with a minimum degree of truth. It constructs an `Assertion` object from the provided individual, concept, and degree, and then delegates the actual storage logic to the public `add_assertion` method. The function performs no direct validation or storage itself, relying entirely on the side effects of the delegated method to update the knowledge base's state.

        :param a: The individual representing the subject of the assertion.
        :type a: Individual
        :param c: The fuzzy concept representing the property or category being asserted about the individual.
        :type c: Concept
        :param n: The lower bound degree of truth for the fuzzy assertion.
        :type n: Degree
        """

        self.add_assertion(Assertion(a, c, n))

    def __add_assertion_3(self, a: Individual, restrict: Restriction) -> None:
        """
        This private helper method adds a fuzzy assertion of the form (a : forall R.C >= n) to the knowledge base by translating a restriction object into a specific concept type. It distinguishes between `HasValueRestriction` instances, which are converted into negated `HasValueConcept` objects, and other restrictions, which are mapped to `AllSomeConcept` objects representing universal quantification. The method ultimately delegates the storage of the assertion to the `add_assertion` method, passing the individual, the constructed concept, and the degree of truth associated with the restriction.

        :param a: The individual instance that serves as the subject of the fuzzy assertion.
        :type a: Individual
        :param restrict: A fuzzy restriction defining a universal quantification constraint, specifying the role, the target concept, and the degree of truth.
        :type restrict: Restriction
        """

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
        """
        Associates a specific individual with a concept identified by its ID within the knowledge base. The method verifies that the provided individual is an instance of `CreatedIndividual`; if this check fails, the operation terminates silently without modifying the state. Upon successful validation, the individual is added to the sorted collection of individuals associated with the specified concept ID, ensuring the internal mapping is updated. This operation also triggers a debug log entry that records the updated list of individuals for the concept.

        :param concept_id: Unique identifier of the concept to which the individual should be added.
        :type concept_id: int
        :param ind: The individual to add to the concept's list. Only instances of CreatedIndividual will be processed.
        :type ind: Individual
        """

        # Add only if created individual
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
        """
        Adds a fuzzy relation connecting a subject individual to an object individual via a specific role and degree to the knowledge base. This method automatically registers the provided role string within the set of known abstract roles. The actual relation construction is delegated to the IndividualHandler. A side effect occurs if the knowledge base is currently loaded and the specified role is functional; in this case, the method triggers a merge of fillers for the subject individual to resolve potential conflicts. The method returns the newly created Relation object.

        :param ind_A: The subject individual of the fuzzy relation.
        :type ind_A: Individual
        :param role: The abstract role defining the relationship between the subject and object individuals.
        :type role: str
        :param ind_B: The object individual involved in the relation.
        :type ind_B: Individual
        :param degree: The degree of truth or membership value for the fuzzy relation.
        :type degree: Degree

        :return: The `Relation` object representing the fuzzy relation that was added.

        :rtype: Relation
        """

        self.abstract_roles.add(role)
        rel: Relation = IndividualHandler.add_relation(ind_A, role, ind_B, degree, self)
        if self.is_loaded() and role in self.functional_roles:
            self.merge_fillers(ind_A, role)
        return rel

    def define_synonym(self, concept_name_1: str, concept_name_2: str) -> None:
        """
        Registers a fuzzy synonym link between two concept names, specifically adding the second name to the synonym set of the first. The operation updates the internal mapping to reflect this association, utilizing set logic to prevent duplicate entries if the relationship already exists. As a side effect, this method ensures that the primary concept exists within the knowledge base by invoking the concept retrieval logic.

        :param concept_name_1: The name of the primary concept to which the synonym is being added.
        :type concept_name_1: str
        :param concept_name_2: The concept name to be added as a synonym for the first concept.
        :type concept_name_2: str
        """

        self.t_synonyms[concept_name_1] = self.t_synonyms.get(
            concept_name_1, set()
        ) | set([concept_name_2])
        self.get_concept(concept_name_1)

    def define_synonyms(self, concept_name_1: str, concept_name_2: str) -> None:
        """
        Establishes a bidirectional synonym relationship between two specified concepts within the knowledge base. This method ensures that the two concept names are treated as semantically equivalent by registering the relationship in both directions. As a side effect, it modifies the internal state of the knowledge base to reflect this new association.

        :param concept_name_1: The name of the first concept to be linked as a synonym.
        :type concept_name_1: str
        :param concept_name_2: The name of the concept to establish a fuzzy synonym relationship with.
        :type concept_name_2: str
        """

        self.define_synonym(concept_name_1, concept_name_2)
        self.define_synonym(concept_name_2, concept_name_1)

    def define_concept(self, concept_name: str, conc: Concept) -> None:
        """
        Adds a fuzzy concept definition to the knowledge base, associating a specific name with a provided concept object. The method first ensures the concept is registered within the system. If optimizations are enabled, it handles specific edge cases: if the concept name is identical to its string representation, the method returns immediately; if the concept is atomic, it is treated as a synonym rather than a complex definition. In standard cases or when optimizations are disabled, the method adds an equivalence axiom to the knowledge base's internal logic.

        :param concept_name: The name or label identifying the concept to be defined.
        :type concept_name: str
        :param conc: The definition or structure of the concept to be associated with the provided name.
        :type conc: Concept
        """

        # Declares the atomic concept
        self.get_concept(concept_name)
        if ConfigReader.OPTIMIZATIONS != 0:
            if concept_name == str(conc):
                return
            if conc.type == ConceptType.ATOMIC:
                self.define_synonyms(concept_name, str(conc))
                return

        # Add to axioms_A_equiv_C
        self.add_axiom_to_A_equiv_C(concept_name, conc)

    def get_A_t_C(self) -> dict[str, int]:
        """
        Generates a dictionary mapping each atomic concept name to a unique integer identifier, effectively creating an index for the concepts. The method iterates through the knowledge base's atomic concepts, assigning sequential integers starting from zero to serve as compact node identifiers. This mapping is essential for constructing the graph used to verify the acyclicity of the TBox, as it allows graph algorithms to operate on efficient integer indices rather than string names. The method does not modify the internal state of the knowledge base and returns an empty dictionary if no atomic concepts are present.

        :return: A dictionary mapping atomic concept names to unique integer indices, used for building the graph to check TBox acyclicity.

        :rtype: dict[str, int]
        """

        size: int = 0
        A_t_C: dict[str, int] = dict()
        for e in self.atomic_concepts:
            A_t_C[e] = size
            size += 1
        return A_t_C

    def add_tdef_links(
        self, g: nx.DiGraph, A_t_C: dict[str, int], use_tdr: bool
    ) -> bool:
        """
        This method constructs a dependency graph by adding edges to the provided directed graph `g` based on the TBox definitions stored in the knowledge base. It iterates through each defined concept, mapping concept names to integer identifiers using the `A_t_C` dictionary, and creates directed edges from the defined concept to the atomic concepts used in its definition. During this process, the method checks for immediate cycles by verifying if a dependent concept is a synonym of the defined concept; if detected, it returns `True`. If the `use_tdr` flag is set, the method also processes domain and range axioms, potentially adding further edges and checking for cycles. The graph `g` is modified in-place, and the method returns `True` if a cycle is identified through synonyms or domain/range axioms, otherwise returning `False`, though a `False` result does not guarantee the absence of cycles in the broader context.

        :param g: The directed graph to which edges representing concept definitions are added.
        :type g: nx.DiGraph
        :param A_t_C: Mapping of atomic concept names to integer node identifiers.
        :type A_t_C: dict[str, int]
        :param use_tdr: Indicates whether to consider domain and range axioms when adding links.
        :type use_tdr: bool

        :return: True if a cycle is detected due to synonyms or domain/range axioms while adding definition links; False otherwise. Note that a return value of False does not guarantee the graph is acyclic.

        :rtype: bool
        """

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
            # Consider domain and range axioms
            if use_tdr and self.add_tdr_links(g, A_t_C, c.get_roles(), v1):
                return True
        return False

    def add_tinc_links(
        self, g: nx.DiGraph, A_t_C: dict[str, int], use_tdr: bool
    ) -> bool:
        """
        Populates the provided directed graph with edges representing terminological inclusions defined in the knowledge base. For each atomic concept involved in an inclusion, the method retrieves the corresponding node identifier from the provided mapping and creates directed edges to the atomic concepts found within the inclusion's definition. During this process, it specifically checks for cycles arising from synonym relationships; if an included concept is identified as a synonym of the source concept, the method immediately returns True. Additionally, if the `use_tdr` flag is enabled, the method incorporates domain and range axioms by invoking `add_tdr_links` and propagates any cycle detection result from that call. The graph is modified in place, and while a return value of True confirms the existence of cycles due to synonyms or domain/range axioms, a return value of False does not guarantee the graph is acyclic.

        :param g: The directed graph to which edges representing concept inclusions are added.
        :type g: nx.DiGraph
        :param A_t_C: Mapping of atomic concept names to their corresponding integer node identifiers in the graph.
        :type A_t_C: dict[str, int]
        :param use_tdr: Determines whether domain and range axioms are considered when adding links.
        :type use_tdr: bool

        :return: True if a cycle is detected via synonym relationships or domain/range axioms during the addition of inclusion links; False otherwise. Note that a False return does not guarantee the graph is acyclic.

        :rtype: bool
        """

        for a in self.t_inclusions:
            v1: int = A_t_C.get(a)
            for pcd in self.t_inclusions[a]:
                c: Concept = pcd.get_definition()
                for b in c.get_atomic_concepts():
                    b_name: str = str(b)
                    name_set: typing.Optional[set[str]] = self.t_synonyms.get(a)
                    if name_set is not None and b_name in name_set:
                        return True
                    v2: int = A_t_C.get(b_name)
                    g.add_edge(v1, v2)
                # Consider domain and range axioms
                if use_tdr and self.add_tdr_links(g, A_t_C, c.get_roles(), v1):
                    return True
        return False

    def add_tdr_links(
        self, g: nx.DiGraph, A_t_C: dict[str, int], used_roles: set[str], v: int
    ) -> bool:
        """
        Populates the provided directed graph `g` with edges representing dependencies derived from domain and range restrictions associated with the concept `v`. The method expands the set of `used_roles` to include all parent roles within the role hierarchy, then iterates through these roles to identify relevant restrictions. For every atomic concept found within these domain and range restrictions, a directed edge is added from `v` to the corresponding node in the graph. Additionally, the method checks for a specific cycle condition involving 't_synonyms'; if a restriction is identified as a synonym of an atomic concept it restricts, the method returns `True` immediately. If the process completes without detecting this condition, it returns `False`, although this result does not guarantee that the graph is cycle-free.

        :param g: The directed graph to which edges representing domain and range restrictions are added.
        :type g: nx.DiGraph
        :param A_t_C: Mapping of atomic concept names to their corresponding integer identifiers.
        :type A_t_C: dict[str, int]
        :param used_roles: The set of role identifiers to be processed for domain and range restrictions.
        :type used_roles: set[str]
        :param v: The integer identifier of the concept acting as the source node for the edges to be added.
        :type v: int

        :return: True if a cycle involving t_synonyms was detected during the link addition process; False otherwise. Note that a return value of False does not guarantee the graph is acyclic.

        :rtype: bool
        """

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
                    # Add link to graph
                    w: int = A_t_C.get(str(used_concept))
                    g.add_edge(v, w)
        return False

    def is_tbox_acyclic(self) -> bool:
        """
        Determines whether the TBox component of the knowledge base is acyclic by analyzing the dependencies formed by TBox inclusions and TBox definitions. The method constructs a directed graph representing the relationships between atomic concepts, checking for cycles both during the graph construction phase and upon completion. If a cycle is detected at any point, the method returns False; otherwise, it returns True. This validation ensures that concept definitions do not contain circular dependencies, which is often a prerequisite for specific reasoning tasks.

        :return: True if the union of terminological inclusions and definitions is acyclic, False if a cycle is detected.

        :rtype: bool
        """

        g: nx.DiGraph = nx.DiGraph()
        # Application mapping every atomic concept into an integer number
        A_t_C: dict[str, int] = self.get_A_t_C()
        # Add links to the graph because of t_inclusions and t_definitions
        if self.add_tinc_links(g, A_t_C, True):
            return False
        if self.add_tdef_links(g, A_t_C, True):
            return False
        # Check whether the graph has a cycle
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
        """
        Defines a fuzzy atomic concept by establishing a subsumption relationship between a source concept name and a target concept, governed by a specific implication operator and a degree of truth. The method verifies the concept's existence and automatically adjusts the implication operator to Lukasiewicz if the degree of truth is absolute (1.0) and the operator is not Kleene-Dienes. It includes a redundancy check to avoid duplicate definitions; if the definition is unique, it is stored in the knowledge base's internal axiom registry, categorized based on whether the target concept is atomic or complex.

        :param concept_name: The unique identifier for the atomic concept to be defined.
        :type concept_name: str
        :param conc: The Concept instance used as the definition for the atomic concept.
        :type conc: Concept
        :param implication: The fuzzy logic operator used to define the implication relationship between the atomic concept and its definition.
        :type implication: LogicOperatorType
        :param n: The degree of truth associated with the atomic concept definition.
        :type n: float
        """

        # Declares the atomic concept
        self.get_concept(concept_name)
        if n == 1.0 and implication != LogicOperatorType.KLEENE_DIENES:
            implication = LogicOperatorType.LUKASIEWICZ

        # Redundant elimination
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
        """
        Adds a fuzzy atomic concept definition to the knowledge base, specifically tailored for General Concept Inclusion (GCI) transformations. It first ensures the target concept is registered and skips the operation if the proposed definition is redundant relative to existing knowledge. The method creates a `PrimitiveConceptDefinition` encapsulating the concept, implication logic, and degree of truth, then routes it to the appropriate internal storage: definitions involving atomic concepts are stored directly in the main axiom registry, while those involving complex concepts are placed in a temporary queue for subsequent processing.

        :param concept_name: Identifier for the atomic concept being defined.
        :type concept_name: str
        :param conc: The concept expression or super-concept defining the atomic concept.
        :type conc: Concept
        :param implication: The fuzzy logic implication operator used to interpret the semantic relationship of the concept definition.
        :type implication: LogicOperatorType
        :param n: The degree of truth associated with the fuzzy implication defining the atomic concept.
        :type n: float
        """

        # Declares the atomic concept
        self.get_concept(concept_name)

        # Redundant elimination
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
        """
        Determines whether a specific implication rule, where an atomic concept implies a defined concept, is logically redundant within the knowledge base. The rule is considered redundant if the consequent concept is the universal 'Top' concept, or if the antecedent is identical to the consequent (except when using the Kleene-Dienes implication). Additionally, if the consequent is a disjunction (OR) that includes the antecedent as one of its operands, the implication is deemed redundant.

        :param concept_name: The name of the atomic concept acting as the antecedent (A) in the implication.
        :type concept_name: str
        :param conc: The concept definition representing the consequent $C$ in the implication $A \Rightarrow C$.
        :type conc: Concept
        :param implication: The fuzzy logic operator used to define the implication relationship between the atomic concept and the concept definition.
        :type implication: LogicOperatorType
        :param n: The degree of truth for the implication.
        :type n: float

        :return: True if the implication $A \Rightarrow C$ is redundant, False otherwise. Redundancy is determined by whether $C$ is the Top concept, $A$ is identical to $C$ (excluding Kleene-Dienes implication), or $A$ is a component of a disjunction $C$.

        :rtype: bool
        """

        # Checks if A => C redundant

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
        """Marks the Knowledge Base as unsatisfiable by introducing a logical contradiction into the associated MILP model. This operation updates the internal state to reflect that the current constraints cannot be satisfied, ensuring that subsequent solving attempts will fail to find a feasible solution. The method modifies both the boolean flag tracking satisfiability and the mathematical constraints within the solver."""

        self.KB_UNSAT = True
        self.milp.add_contradiction()

    def is_redundant_gci(
        self, C: Concept, D: Concept, implication: LogicOperatorType, n: float
    ) -> bool:
        """
        Determines whether a General Concept Inclusion (GCI) of the form $C \Rightarrow D$ is redundant within the knowledge base, taking into account the specific fuzzy implication operator and truth degree. The method identifies redundancy in cases of logical tautologies, such as when the subsumer $D$ is the universal concept or the subsumed concept $C$ is the bottom concept. For implication operators other than Kleene-Dienes, it also checks for structural redundancies, including when $C$ and $D$ are identical, or when $C$ is a direct component of a disjunction $D$ or $D$ is a direct component of a conjunction $C$. If the subsumed concept is the universal concept and the subsumer is the bottom concept, the method marks the knowledge base as unsatisfiable and raises an InconsistentOntologyException to signal a logical contradiction.

        :param C: The concept being subsumed (the antecedent of the implication).
        :type C: Concept
        :param D: The subsumer concept representing the superclass or parent in the general concept inclusion $C \Rightarrow D$.
        :type D: Concept
        :param implication: The fuzzy logic implication operator used to evaluate the subsumption relationship and determine redundancy.
        :type implication: LogicOperatorType
        :param n: The degree of truth associated with the fuzzy General Concept Inclusion.
        :type n: float

        :raises InconsistentOntologyException: Raised when the subsumed concept is Top and the subsumer concept is Bottom, implying an unsatisfiable knowledge base.

        :return: True if the General Concept Inclusion (GCI) $C \Rightarrow D$ is redundant (trivially true or structurally implied), False otherwise.

        :rtype: bool
        """

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
        """
        This method attempts to identify and resolve synonym relationships by checking for reciprocal definitions within the knowledge base. Given a primitive concept definition stating that concept A is a concept B, it searches for a corresponding definition stating that B is A. If both definitions exist, represent atomic concepts, and satisfy strict logical constraints—specifically, having a degree of 1.0 or operating under classical logic while excluding Kleene-Dienes implications—the method infers that A and B are synonyms. As a side effect, it formally defines the synonym relationship, removes the original "A is a B" definition, and removes the reciprocal "B is a A" definition from either the main axioms or temporary inclusions. The method returns true if the knowledge base was modified and false otherwise.

        :param pcd1: The primitive concept definition representing the "A is a B" relationship to be evaluated for potential synonym absorption.
        :type pcd1: PrimitiveConceptDefinition

        :return: True if a synonym relationship was identified and absorbed, resulting in modifications to the knowledge base; False otherwise.

        :rtype: bool
        """

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
            # Look for (b => a >= 1), remove it and create a synonym definition
            # We need to search in both sets below
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
                # Synonym definition
                self.define_synonyms(a, b)
                # Remove A isA B
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
                # Synonym definition
                self.define_synonyms(a, b)

                # Remove A isa C
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
        """
        Attempts to detect and absorb a bidirectional inclusion relationship into a synonym definition. Given a primitive concept definition representing an inclusion `A => B`, the method searches for a corresponding reverse inclusion `B => A` within the knowledge base's various axiom sets. If both directions exist, represent atomic concepts, and satisfy strict semantic conditions—specifically, operating under classical logic or possessing a degree of 1.0 with a non-Kleene-Dienes implication type—the method defines `A` and `B` as synonyms. This process involves removing the original inclusion axioms from the relevant internal collections and registering the synonym relationship, thereby modifying the state of the knowledge base. The method returns `True` if a synonym was successfully defined and axioms were removed, and `False` otherwise.

        :param pcd1: The primitive concept definition representing the "A is a B" relationship to be evaluated for potential synonym absorption.
        :type pcd1: PrimitiveConceptDefinition

        :return: True if a synonym relationship was successfully identified and absorbed, False otherwise.

        :rtype: bool
        """

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
            # Look for (b => a >= 1), remove it and create a synonym definition
            # We need to search in all sets below
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
                # Synonym definition
                self.define_synonyms(a, b)
                # Remove A isa B from t_inclusions
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
                # Synonym definition
                self.define_synonyms(a, b)
                # Remove A isa B
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
                # Synonym definition
                self.define_synonyms(a, b)
                # Remove A isa B
                self.remove_A_is_a_X(a, pcd1, self.axioms_to_do_A_is_a_B)
                self.remove_A_is_a_X(b, pcd4, self.axioms_to_do_A_is_a_B)
                Util.debug(f"Synonym absorption from axioms_to_do_A_is_a_B: {a} = {b}")
                return True
        return False

    def add_atomic_concepts_disjoint(self, disjoint_concepts: list[str]) -> None:
        """
        Declares that a specified collection of atomic concepts are pairwise disjoint within the knowledge base by adding the corresponding axioms. This method iterates through the provided list of concept names and establishes a disjointness relationship for every unique pair of concepts found in the collection, ensuring that no single instance can belong to more than one concept in the group. It implicitly validates the existence of each concept by attempting to retrieve it before adding the axioms, which may result in an error if a concept name is not currently defined in the ontology. The operation modifies the internal state of the knowledge base and logs the input list for debugging purposes.

        :param disjoint_concepts: A list of atomic concept names to be declared pairwise disjoint.
        :type disjoint_concepts: list[str]
        """

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
        """
        This method extends the knowledge base by asserting that specific concepts are mutually exclusive. It provides flexible argument handling to accommodate different data representations: a single sequence containing multiple Concept objects, or a pair of arguments consisting of either two string identifiers or two Concept instances. The function performs strict validation on argument count and types, raising errors for invalid inputs such as mismatched types or incorrect argument lengths.

        :param args: The concepts to be declared disjoint. Can be provided as a sequence of Concept objects, or as two arguments where each is either a string identifier or a Concept instance.
        :type args: typing.Any

        :raises ValueError: Raised if the arguments do not match the required format: either a single sequence of Concepts, or two arguments that are both strings or both Concepts.
        """

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
        """
        This method processes a list of concepts to establish that they are all mutually disjoint. It iterates through the input list to generate every unique pair of concepts and invokes the underlying `add_concepts_disjoint` method for each pair, effectively creating a clique of disjointness relationships. If the list contains fewer than two concepts, no axioms are added. As a side effect, this operation modifies the internal state of the knowledge base and logs debug information regarding the disjoint axioms being processed.

        :param disjoint_concepts: A list of concepts to be declared mutually disjoint.
        :type disjoint_concepts: list[Concept]
        """

        Util.debug(f"Disjoint axioms: {disjoint_concepts}")
        for i, c1 in enumerate(disjoint_concepts):
            for c2 in disjoint_concepts[i + 1 :]:
                self.add_concepts_disjoint(c1, c2)

    def __add_concepts_disjoint_2(self, c1: str, c2: str) -> None:
        """
        Updates the internal representation of the knowledge base to record that two concepts are disjoint. Specifically, it adds the second concept to the set of concepts known to be disjoint with the first concept. If the two concept names are identical, the method returns without making any changes. This operation directly modifies the instance's internal disjointness tracking structure.

        :param c1: The name of the first concept to be marked as disjoint from the second concept.
        :type c1: str
        :param c2: The name of the concept to be marked as disjoint from the first concept.
        :type c2: str
        """

        if c1 == c2:
            return
        self.t_disjoints[c1] = self.t_disjoints.get(c1, set()) | set([c2])

    def __add_concepts_disjoint_3(self, c: Concept, d: Concept) -> None:
        """
        Enforces a disjoint relationship between two concepts by adding appropriate axioms to the knowledge base. If the two concepts are identical, the method returns without making changes. When both concepts are atomic, they are directly marked as mutually disjoint; otherwise, for complex concepts, the method generates two new atomic concepts, establishes implications from the original concepts to these proxies, and declares the proxies mutually disjoint to ensure the original concepts cannot overlap.

        :param c: The first concept to be made disjoint from the second concept.
        :type c: Concept
        :param d: The concept to be made disjoint with `c`.
        :type d: Concept
        """

        if str(c) == str(d):
            return
        if c.is_atomic() and d.is_atomic():
            self.add_mutually_disjoint(str(c), str(d))
        else:
            # New concepts
            a: Concept = self.get_new_atomic_concept()
            b: Concept = self.get_new_atomic_concept()
            # C ==> A
            self.zadeh_implies(c, a)
            # D ==> B
            self.zadeh_implies(d, b)
            # disjoint(A,B)
            self.add_mutually_disjoint(str(a), str(b))

    def add_mutually_disjoint(self, c1: str, c2: str) -> None:
        """
        Establishes a mutual disjointness relationship between two concepts identified by their names within the knowledge base. This method ensures that the disjointness axiom is recorded symmetrically by invoking the underlying directional disjointness method twice—once for the pair (c1, c2) and once for (c2, c1)—thereby guaranteeing that the concepts are treated as non-overlapping in both directions. As a side effect, this operation modifies the internal state of the knowledge base by adding these axioms.

        :param c1: The name of the first concept to be declared mutually disjoint with the second.
        :type c1: str
        :param c2: The name of the second concept to be made mutually disjoint with the first.
        :type c2: str
        """

        self.add_concepts_disjoint(c1, c2)
        self.add_concepts_disjoint(c2, c1)

    def get_new_atomic_concept(self) -> Concept:
        """
        Creates and returns a new atomic concept instance with a unique name derived from an internal counter. The method ensures uniqueness by incrementing the knowledge base's counter of defined concepts and appending this value to a default prefix. This operation has the side effect of mutating the knowledge base's state by updating the counter, which affects the naming of any future concepts generated by this method.

        :return: A new atomic concept instance with a unique, auto-generated name.

        :rtype: Concept
        """

        self.num_defined_concepts += 1
        concept_name: str = f"{Concept.DEFAULT_NAME}{self.num_defined_concepts}"
        return AtomicConcept(concept_name)

    def add_equivalent_roles(self, equiv_roles: list[str]) -> None:
        """
        Establishes equivalence among a list of functional roles by adding mutual implication axioms to the knowledge base. It processes the input list by asserting that each role implies the next one in the sequence and vice versa, thereby linking them as equivalent. If the provided list contains fewer than two elements, the method performs no action. This operation modifies the internal state of the knowledge base through the addition of these implication relationships.

        :param equiv_roles: A collection of role names to be defined as mutually equivalent.
        :type equiv_roles: list[str]
        """

        if len(equiv_roles) < 2:
            return
        r1: str = equiv_roles[0]
        for r2 in equiv_roles[1:]:
            self.role_implies(r1, r2)
            self.role_implies(r2, r1)
            r1 = r2

    def add_equivalent_concepts(self, equiv_concepts: list[Concept]) -> None:
        """
        Registers a collection of concepts as equivalent within the knowledge base by establishing axioms between the first concept and every subsequent concept in the provided list. The method intelligently handles the definition process based on the nature of the concepts: if one concept in a pair is atomic, it defines that atomic concept in terms of the other, whereas if both are complex, it creates a direct equivalence axiom. This operation modifies the internal state of the knowledge base, but it will silently return without effect if the input list contains fewer than two concepts.

        :param equiv_concepts: A list of concepts to be treated as equivalent. The method establishes equivalence relationships between the first concept and each subsequent concept in the list.
        :type equiv_concepts: list[Concept]
        """

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
        """
        Establishes a strict semantic equivalence between two concepts by adding mutual implication axioms to the knowledge base. This method asserts that the first concept implies the second and that the second implies the first, both with a certainty degree of one, effectively treating them as interchangeable for logical inference. As a side effect, this operation modifies the internal state of the knowledge base, allowing subsequent reasoning processes to propagate properties and relationships between the two concepts.

        :param c1: The first concept to be asserted as equivalent to the second concept.
        :type c1: Concept
        :param c2: The concept to define as equivalent to the first concept.
        :type c2: Concept
        """

        self.lukasiewicz_implies(c1, c2, DegreeNumeric.get_one())
        self.lukasiewicz_implies(c2, c1, DegreeNumeric.get_one())

    def add_disjoint_union_concept(self, disjoint_union_concepts: list[str]) -> None:
        """
        Adds a disjoint union concept axiom to the knowledge base, defining the first concept in the provided list as the union of the subsequent concepts. If the list contains exactly two concepts, the first is defined as equivalent to the second. For lists longer than two elements, the first concept is defined as the logical disjunction of the remaining concepts, which are then declared to be pairwise disjoint. The method has no effect if the input list contains fewer than two elements. Note that this method modifies the input list in-place by removing the first element before processing the disjointness constraints.

        :param disjoint_union_concepts: Names of the concepts involved in the disjoint union. The first concept is defined as the union of the rest, which are also made mutually disjoint.
        :type disjoint_union_concepts: list[str]
        """

        if len(disjoint_union_concepts) < 2:
            return
        name1: str = disjoint_union_concepts[0]
        if len(disjoint_union_concepts) == 2:
            name2: str = disjoint_union_concepts[1]
            c2: Concept = self.get_concept(name2)
            self.define_concept(name1, c2)
        else:
            # Define C1 is a union of C2 ...
            big_or: Concept = None
            for name_i in disjoint_union_concepts[1:]:
                ci: Concept = self.get_concept(name_i)
                big_or = ci if big_or is None else OperatorConcept.or_(big_or, ci)

            self.define_concept(name1, big_or)
            del disjoint_union_concepts[0]

            # Make C2...Cn disjoint
            self.add_atomic_concepts_disjoint(disjoint_union_concepts)

    def role_is_functional(self, role: str) -> None:
        """
        Asserts that the specified role is functional by adding a corresponding axiom to the knowledge base. In semantic terms, this constrains the role such that an individual cannot be linked to more than one distinct entity via this role. The method updates the internal state by adding the role identifier to the set of functional roles, and the operation is idempotent, meaning re-adding the same role does not alter the state.

        :param role: The name of the role to be marked as functional.
        :type role: str
        """

        self.functional_roles.add(role)

    def role_is_inverse_functional(self, role: str) -> None:
        """
        Marks the specified role as inverse functional, indicating that an individual cannot be the target of this role for more than one distinct source individual. This method updates the internal registry of inverse functional roles and ensures the logical consistency of the role's inverse. Specifically, it marks the inverse role as functional; if an inverse role does not already exist in the knowledge base, a new abstract inverse role is automatically generated, added, and marked as functional.

        :param role: The name of the role to be declared as inverse functional.
        :type role: str
        """

        self.inverse_functional_roles.add(role)
        iv: typing.Optional[set[str]] = self.inverse_roles.get(role)
        if iv is not None:
            for inverse in iv:
                self.functional_roles.add(inverse)
        else:
            inverse: str = f"{role}{Concept.SPECIAL_STRING}inverse"
            self.add_inverse_roles(role, inverse)
            self.abstract_roles.add(inverse)
            self.functional_roles.add(inverse)

    def role_is_transitive(self, role: str) -> None:
        """
        Marks the specified role as transitive, indicating that the relationship propagates through intermediate nodes. This method updates the internal state by adding the role to both the set of transitive roles and the set of abstract roles. The operation is idempotent; if the role is already registered as transitive, the knowledge base remains unchanged.

        :param role: The name of the role to be declared transitive. This operation also implicitly marks the role as abstract.
        :type role: str
        """

        if role not in self.transitive_roles:
            self.abstract_roles.add(role)
            self.transitive_roles.add(role)

    def role_is_reflexive(self, role: str) -> None:
        """
        Marks the specified role as reflexive, asserting that every individual in the domain is related to itself via this role. As a side effect, the role is automatically added to the set of abstract roles within the knowledge base. This method is idempotent; it verifies that the role is not already marked as reflexive before performing the update, ensuring consistent state without duplication.

        :param role: The name of the role to be marked as reflexive.
        :type role: str
        """

        if role not in self.reflexive_roles:
            self.abstract_roles.add(role)
            self.reflexive_roles.add(role)

    def role_is_symmetric(self, role: str) -> None:
        """
        Declares the specified role as symmetric, enforcing the property that the relationship holds bidirectionally between any two entities. This method marks the role as abstract and symmetric, generates an explicit inverse role, and establishes axioms defining the inverse relationship and mutual implication between the original role and its inverse. As a side effect, it updates the internal sets of abstract and symmetric roles and adds new role axioms to the knowledge base.

        :param role: The role to be defined as symmetric.
        :type role: str
        """

        self.abstract_roles.add(role)
        self.symmetric_roles.add(role)
        inv_name: str = f"{role}{Concept.SPECIAL_STRING}inverse"
        self.add_inverse_roles(role, inv_name)
        self.role_implies(role, inv_name)
        self.role_implies(inv_name, role)

    def add_similarity_relation(self, role: str) -> None:
        """
        Registers the specified role as a fuzzy similarity relation within the knowledge base. The method ensures idempotency by checking if the role is already present in the similarity relations set before attempting to add it. As a prerequisite for addition, it enforces that the role satisfies the mathematical properties of reflexivity and symmetry, potentially triggering validation logic or raising errors if these conditions are not met.

        :param role: Name of the role to be added as a fuzzy similarity relation.
        :type role: str
        """

        if role not in self.similarity_relations:
            self.role_is_reflexive(role)
            self.role_is_symmetric(role)
            self.similarity_relations.add(role)

    def add_equivalence_relation(self, role: str) -> None:
        """
        Establishes the specified role as a fuzzy equivalence relation within the knowledge base by enforcing the necessary logical properties. This operation configures the role to be treated as a similarity relation and explicitly marks it as transitive, effectively combining these constraints to satisfy the definition of equivalence. As a side effect, this method modifies the internal state of the knowledge base to ensure that subsequent operations involving this role adhere to these rules.

        :param role: The name of the role to which the fuzzy equivalence relation is applied.
        :type role: str
        """

        self.add_similarity_relation(role)
        self.role_is_transitive(role)

    def get_inverses_of_inverse_role(self, role: str) -> typing.Optional[set[str]]:
        """
        Retrieves the set of roles that are inverses of the inverse of the specified role. The method performs a two-step lookup by first identifying the inverse of the provided role and then returning the set of roles associated with that inverse. If the input role is not found in the inverse roles mapping, has no defined inverses, or if its inverse has no defined inverses, the method returns None. This operation is read-only and does not modify the underlying knowledge base.

        :param role: The name of the role for which to retrieve the inverses of its inverse.
        :type role: str

        :return: The set of roles that are inverses of the inverse of the specified role, or None if the role or its inverse has no defined inverses.

        :rtype: typing.Optional[set[str]]
        """

        inv: typing.Optional[set[str]] = self.inverse_roles.get(role)
        if inv is None or len(inv) == 0:
            return None
        for r in inv:
            # There is only one iteration of the loop
            inv2: set[str] = self.inverse_roles.get(r)
            if inv2 is None or len(inv2) == 0:
                return None
            return inv2
        return None

    def add_inverse_roles(self, role: str, inv_role: str) -> None:
        """
        Establishes a symmetric inverse relationship between the specified role and its inverse role, ensuring both are registered as abstract roles within the knowledge base. This method performs transitive closure by examining existing inverse mappings; if the input roles are already associated with other inverses, those related roles are also linked as inverses to maintain consistency. Finally, the direct inverse pair is added to the internal mapping.

        :param role: The name of the role to be defined as the inverse of `inv_role`.
        :type role: str
        :param inv_role: The name of the role to be added as the inverse of the specified role.
        :type inv_role: str
        """

        self.abstract_roles.add(role)
        self.abstract_roles.add(inv_role)

        # Equivalent roles to "role" are inverse of "inv_role"
        a: set[str] = self.get_inverses_of_inverse_role(role) or set()
        for r in a:
            if role != r:
                self.add_simple_inverse_roles(inv_role, r)

        # Equivalent roles to "inv_role" are inverse of "role"
        b: set[str] = self.get_inverses_of_inverse_role(inv_role) or set()
        for r in b:
            if inv_role != r:
                self.add_simple_inverse_roles(inv_role, r)

        # Inverse roles of "inv_role" and inverse roles of "role" are inverse
        a: typing.Optional[set[str]] = self.inverse_roles.get(role)
        b: typing.Optional[set[str]] = self.inverse_roles.get(inv_role)
        if a is not None and b is not None:
            for r1 in a:
                for r2 in b:
                    if r1 != inv_role and role != r2:
                        self.add_simple_inverse_roles(r1, r2)

        # "role" and "inv_role" are inverse
        self.add_simple_inverse_roles(role, inv_role)

    def add_simple_inverse_roles(self, role: str, inv_role: str) -> None:
        """
        Establishes a symmetric inverse relationship between two roles by updating the internal mapping to reflect that each role is the inverse of the other. As a side effect, it infers functional characteristics: if either role is marked as inverse-functional, the corresponding inverse role is automatically added to the set of functional roles. This method directly mutates the knowledge base's state and supports multiple inverse associations per role through the use of sets.

        :param role: The name of the role to define an inverse relationship for.
        :type role: str
        :param inv_role: The name of the role to be designated as the inverse of the specified role.
        :type inv_role: str
        """

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
        """
        Adds a Role Inclusion Axiom to the knowledge base, defining a hierarchical relationship where the first role is subsumed by the second. This method accepts either two string arguments representing the subsumed and subsumer roles, or three arguments where the third is a numeric degree indicating the strength or certainty of the inclusion. The operation validates the input types and modifies the internal state of the knowledge base to incorporate the new axiom.

        :param args: Variable arguments representing the subsumed role, subsumer role, and an optional degree value for the inclusion axiom.
        :type args: typing.Any

        :raises ValueError: Raised if the number of arguments provided is not 2 or 3.
        """

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
        """
        This method adds a Role Inclusion Axiom to the knowledge base, asserting that the `subsumed` role is a sub-role of the `subsumer` role with a fixed confidence of 1.0. It acts as a specialized wrapper around the `role_subsumes` method, enforcing absolute certainty for the relationship. As a side effect, this operation modifies the internal state of the knowledge base to reflect the specified role hierarchy.

        :param subsumed: The name of the role that is subsumed by the subsumer role.
        :type subsumed: str
        :param subsumer: The name of the role that subsumes the `subsumed` role.
        :type subsumer: str
        """

        self.role_subsumes(subsumer, subsumed, 1.0)

    def __role_implies_2(self, subsumed: str, subsumer: str, n: float) -> None:
        """
        This internal method adds a Role Inclusion Axiom to the knowledge base, defining a hierarchical relationship where the `subsumer` role subsumes the `subsumed` role with a specific degree `n`. It acts as a wrapper that delegates the logic to the `role_subsumes` method, passing the arguments in the necessary order to establish the subsumption. Consequently, the operation modifies the internal state of the knowledge base to reflect this weighted or fuzzy role relationship.

        :param subsumed: The name of the role that is being included in the subsumer role.
        :type subsumed: str
        :param subsumer: The name of the role that subsumes the subsumed role.
        :type subsumer: str
        :param n: The degree of the role inclusion axiom.
        :type n: float
        """

        self.role_subsumes(subsumer, subsumed, n)

    def role_range(self, role: str, conc: Concept) -> None:
        """
        Asserts a range restriction axiom for a specified role, indicating that all fillers of the role must be instances of the provided concept. If the concept is the universal top concept, the method returns immediately without modifying the knowledge base, as this restriction is trivial. Otherwise, it updates the internal state by adding the concept to the set of range restrictions associated with the role, accumulating constraints if multiple restrictions are defined for the same role.

        :param role: The name of the role property to which the range restriction is applied.
        :type role: str
        :param conc: The concept defining the range of the role, restricting the types of objects the role can point to.
        :type conc: Concept
        """

        if conc == TruthConcept.get_top():
            return
        self.range_restrictions[role] = self.range_restrictions.get(role, set()) | set(
            [conc]
        )

    def role_domain(self, role: str, conc: Concept) -> None:
        """
        Adds a domain axiom to the knowledge base, constraining the source of a specific role to belong to the given concept. If the provided concept is the universal (Top) concept, the operation is skipped as it represents a trivial constraint. Otherwise, the concept is added to the set of existing domain restrictions for the role, ensuring that multiple domain constraints are accumulated.

        :param role: The name of the role to which the domain restriction is applied.
        :type role: str
        :param conc: The concept defining the domain restriction for the role.
        :type conc: Concept
        """

        if conc == TruthConcept.get_top():
            return
        self.domain_restrictions[role] = self.domain_restrictions.get(
            role, set()
        ) | set([conc])

    def solve_inverse_roles(self) -> None:
        """Orchestrates the resolution of inverse role axioms by systematically updating the internal state of the knowledge base. It delegates the generation of inclusion axioms, the handling of transitivity for inverse roles, and the establishment of role relations to specific helper methods. This process ensures that all logical constraints and structural relationships involving inverse roles are correctly applied and stored within the knowledge base."""

        self.form_inv_role_inc_axioms()
        self.form_inv_trans_roles()
        self.form_inv_role_relations()

    def form_inv_role_relations(self) -> None:
        """This method computes and enforces relationships for inverse roles within the knowledge base. It iterates through all existing role relations, identifying those where the role has a defined inverse. For each such relation, it adds an equality constraint to the MILP model linking the variable of the original relation to the variable of the inverse relation, thereby ensuring that the existence and degree of the relationship are symmetric. Finally, it instantiates the inverse relation objects and adds them to the respective individuals, effectively populating the graph with the reverse edges."""

        temp_role_relations: dict[str, list[Relation]] = dict()
        for ind_a in self.individuals.values():
            for role, relations in ind_a.role_relations.items():
                if role not in self.inverse_roles:
                    continue
                for rel in relations:
                    ind_b: Individual = rel.get_object_individual()
                    ind_b_name: str = str(ind_b)
                    temp_rels: list[Relation] = temp_role_relations.get(ind_b_name, [])
                    # For every inverse "inv_role"
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
        """Computes and adds role inclusion axioms for inverse roles based on the existing role hierarchy. For every known inclusion where a child role is a subrole of a parent role, this method checks if both roles have defined inverses. If they do, it infers that the inverse of the parent role is a subrole of the inverse of the child role, preserving the weight associated with the original relationship. The process runs iteratively until a fixed point is reached, ensuring that all transitive inferences are captured and the internal state of the knowledge base is updated with these new relationships."""

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
                    # For every inverse funcRole of C
                    for inv_role_r in self.inverse_roles[role_r]:
                        # For every inverse funcRole of D
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
        """Computes the closure of transitive roles with respect to inverse relationships, ensuring that if a role is transitive, its inverse is also marked as transitive. The method performs a fixpoint iteration, starting with the currently defined transitive roles and repeatedly checking for defined inverses. For each transitive role, any inverse roles that are not already in the transitive set are added, and the process repeats for these new roles until no further updates can be made. This operation modifies the `transitive_roles` attribute in place and gracefully handles cases where inverse mappings are missing or roles have already been processed."""

        to_do: set[str] = copy.deepcopy(self.transitive_roles)
        no_more_roles: bool = len(to_do) == 0
        while not no_more_roles:
            no_more_roles = True
            trans_roles_tmp: set[str] = set()
            for trans_role in to_do:
                if self.inverse_roles.get(trans_role) is None:
                    continue
                # For every inverse funcRole
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
        """
        Processes and resolves fuzzy role inclusion axioms to update the state of the knowledge base. The method supports two operational modes: a global resolution when called with no arguments, and a targeted resolution when provided with a specific `Individual` and `Relation`. It validates the input strictly, ensuring that exactly zero or two arguments are passed and that the specific types match the expected classes before delegating to the appropriate internal implementation.

        :param args: Optional arguments defining the scope of the operation. If omitted, solves general axioms; otherwise, expects an Individual and a Relation to solve specific axioms.
        :type args: typing.Any
        """

        assert len(args) in [0, 2]
        if len(args) == 0:
            self.__solve_role_inclusion_axioms_1()
        else:
            assert isinstance(args[0], Individual)
            assert isinstance(args[1], Relation)
            self.__solve_role_inclusion_axioms_2(*args)

    def __solve_role_inclusion_axioms_1(self) -> None:
        """This method enforces role inclusion axioms by inferring super-role relationships for all individuals within the knowledge base. It begins by precomputing the complete hierarchy of parent roles for each role and identifying transitive children. Subsequently, it iterates through every individual and their existing role relations; if a specific role possesses parent roles, the method infers that the individual also participates in those parent roles and adds these new relations to the individual's profile, modifying the internal state of the knowledge base accordingly."""

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
        """
        This method processes role inclusion axioms to infer new relations based on the hierarchical structure of roles within the knowledge base. Given a specific individual and a relation, it identifies all ancestor roles of the relation's type and generates corresponding relations between the subject and object individuals. The truth degree of these inferred relations is determined by the configured fuzzy logic semantics: under Lukasiewicz semantics, it computes the t-norm of the original relation's degree and the inclusion axiom's degree, handling both numeric values and symbolic variables by adding necessary constraints to the MILP solver; under Zadeh semantics, it propagates the relation directly. As a side effect, if the inferred parent role is marked as functional, the method triggers a filler merging process to ensure that the individual adheres to the functional property constraints.

        :param ind: The individual acting as the subject of the relation.
        :type ind: Individual
        :param r: The fuzzy relation instance being processed to infer new relations. It provides the role name to identify parent roles, the degree for calculating truth values, and the object individual for the inferred assertions.
        :type r: Relation
        """

        role_c: str = r.get_role_name()
        parents: dict[str, float] = self.roles_with_all_parents.get(role_c)
        if parents is not None:
            for role_p, n in parents.items():
                Util.debug(
                    f"Adding new relations, since {role_p} is an ancestor of {r.get_role_name()} with degree {n}"
                )
                # Lukasiewicz semantics
                if constants.KNOWLEDGE_BASE_SEMANTICS == FuzzyLogic.LUKASIEWICZ:
                    deg: Degree = r.get_degree()
                    if deg.is_numeric():
                        aux: float = typing.cast(
                            DegreeNumeric, deg
                        ).get_numerical_value()
                        luk_tnorm: float = LukasiewiczSolver.and_(n, aux)
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

                    # Add x l-and n
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
                # Zadeh semantics: assumes degree 1
                IndividualHandler.add_relation(
                    ind, role_p, r.get_object_individual(), r.get_degree(), self
                )
                if role_p not in self.functional_roles:
                    continue
                self.merge_fillers(ind, role_p)

    def add_relation_with_role_parent(
        self, ind: Individual, role_c: str, role_p: str, n: float
    ) -> None:
        """
        Infers new relations for a given individual based on a role hierarchy axiom, asserting that a child role is a sub-role of a parent role with a specific degree of inclusion. It retrieves all existing relations where the individual is the subject and the child role is the predicate, then generates corresponding relations using the parent role. The specific behavior depends on the active fuzzy logic semantics: under Zadeh semantics, it simply adds relations with the parent role while preserving the original object and degree, whereas under Lukasiewicz semantics, it applies a specific calculation to determine the degree of the inferred relations.

        :param ind: The individual acting as the subject of the relation.
        :type ind: Individual
        :param role_c: The name of the child role used to retrieve existing relations for the individual.
        :type role_c: str
        :param role_p: The name of the parent role to which the relation is being added.
        :type role_p: str
        :param n: The degree of truth or strength of the role inclusion axiom, indicating how strongly the child role implies the parent role.
        :type n: float
        """

        relations: list[Relation] = ind.role_relations.get(role_c, [])
        # Lukasiewicz semantics
        if constants.KNOWLEDGE_BASE_SEMANTICS == FuzzyLogic.LUKASIEWICZ:
            for r in relations:
                self.add_relation_with_role_parent_in_lukasiewicz(r, role_p, n)
        else:
            # Zadeh semantics: assumes degree 1
            for r in relations:
                self.add_relation(
                    ind, role_p, r.get_object_individual(), r.get_degree()
                )

    def add_relation_with_role_parent_in_lukasiewicz(
        self, r: Relation, role_p: str, n: float
    ) -> None:
        """
        This method incorporates a new relation into the knowledge base where the specified role acts as a parent, utilizing Lukasiewicz fuzzy logic semantics to determine the resulting truth degree. It computes the degree of the new relation by applying the Lukasiewicz t-norm to the original relation's degree and the provided threshold value. If the original relation possesses a numeric degree, the calculation is performed directly using floating-point arithmetic; otherwise, the method introduces auxiliary variables and linear constraints into the underlying Mixed-Integer Linear Programming (MILP) model to algebraically represent the t-norm operation. This process modifies the MILP model's state and updates internal variable counters before adding the derived relation to the knowledge base.

        :param r: The relation providing the subject, object, and initial degree for the new relation added to the parent role.
        :type r: Relation
        :param role_p: The name of the parent role used to identify the relation.
        :type role_p: str
        :param n: The truth degree of the role inclusion axiom, used to compute the resulting relation's degree under Lukasiewicz semantics.
        :type n: float
        """

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

            # Add x l-and n
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
        """
        Processes a General Concept Inclusion (GCI) relative to a specific individual within the knowledge base. The method supports two modes of operation: solving a specific GCI for an individual or solving a GCI based solely on the individual's context. It requires the first argument to be an `Individual` and optionally accepts a second `GeneralConceptInclusion` argument. Input validation is performed to ensure the correct types and argument count are provided, with the actual resolution logic delegated to internal helper methods.

        :param args: Variable arguments accepting either a single Individual or an Individual followed by a GeneralConceptInclusion to solve.
        :type args: typing.Any

        :raises ValueError: Raised if the number of arguments provided is not 1 or 2.
        """

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
        """
        Handles the resolution of a General Concept Inclusion (GCI) for a specific individual by delegating to logic-specific solver routines. The method acts as a dispatcher, first verifying that neither the subsumed nor the subsumer concept is a modified concrete concept; if such a concept is detected, the operation is aborted immediately. For valid GCIs, the method determines the associated fuzzy logic operator type—specifically Lukasiewicz, Goedel, Kleene-Dienes, or Zadeh—and triggers the appropriate internal solver to update the knowledge base state accordingly.

        :param ind: The individual subject to the General Concept Inclusion (GCI) constraint.
        :type ind: Individual
        :param gci: The General Concept Inclusion (GCI) constraint to be solved, containing the subsumed and subsumer concepts and the specific logic operator type to be applied.
        :type gci: GeneralConceptInclusion
        """

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
        """
        Iterates over the set of General Concept Inclusions (GCIs) stored in `self.t_G` and applies each one to the provided individual. By invoking `solve_gci` for every GCI in the collection, this method ensures that the individual adheres to all defined terminological constraints. This operation modifies the internal state of the knowledge base or the individual directly and produces no return value.

        :param ind: The individual to which all General Concept Inclusions are applied.
        :type ind: Individual
        """

        for gci in self.t_G:
            self.solve_gci(ind, gci)

    def solve_lukasiewicz_gci(
        self, ind: Individual, gci: GeneralConceptInclusion
    ) -> None:
        """
        Encodes a General Concept Inclusion (GCI) axiom into the internal Mixed Integer Linear Programming (MILP) model using Lukasiewicz fuzzy logic semantics for a specific individual. The method processes the GCI $C \sqsubseteq_l D$ by generating linear constraints that enforce the relationship between the membership degrees of the individual in concepts $C$ and $D$. It handles specific structural simplifications: if the subsumed concept is Top, it asserts the subsumer; if the subsumer is Bottom, it asserts the negation of the subsumed concept; and if both are Bottom, it introduces an inconsistency constraint. In the general case, it applies the Lukasiewicz implication constraint $1 - C(a) + D(a) \ge l$, utilizing a specialized crisp constraint when the degree is exactly 1.0. This operation modifies the MILP model by adding new constraints and assertions, and updates internal counters related to variable usage.

        :param ind: The individual entity to which the General Concept Inclusion is applied, serving as the subject for the generated assertions and constraints.
        :type ind: Individual
        :param gci: The general concept inclusion axiom containing the subsumed concept, subsumer concept, and degree to be enforced.
        :type gci: GeneralConceptInclusion
        """

        c: Concept = gci.get_subsumed()
        d: Concept = gci.get_subsumer()
        l: Degree = gci.get_degree()
        Util.debug(f"{constants.SEPARATOR}Applying GCI{constants.SEPARATOR}")
        Util.debug(f"{d} l-subsumes {c} >= {l}")

        if c.type == ConceptType.TOP:
            if d.type == ConceptType.BOTTOM:
                # Inconsistency
                self.milp.add_new_constraint(
                    Expression(1.0), InequalityType.EQUAL, DegreeNumeric.get_degree(0.0)
                )
            else:
                # a:D >= n
                new_ass: Assertion = Assertion(ind, d, l)
                self.add_assertion(new_ass)
        else:
            not_c: Concept = -c
            if d.type == ConceptType.BOTTOM:
                # a: \not C >= n
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
                    # xIndIsC <= xIndIsD
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
                    # 1 - x1 + x2 >= L
                    self.milp.add_new_constraint(
                        Expression(Term(1.0, x_ind_is_not_c), Term(1.0, x_ind_is_d)),
                        InequalityType.GREATER_THAN,
                        l,
                    )
        Util.debug(f"{constants.SEPARATOR}GCI completed{constants.SEPARATOR}")

    def solve_goedel_gci(self, ind: Individual, gci: GeneralConceptInclusion) -> None:
        """
        This method processes a General Concept Inclusion (GCI) for a specific individual by translating the logical constraint into mathematical assertions or linear inequalities based on Gödel fuzzy logic semantics. It handles edge cases such as when the subsumed concept is the universal concept (Top) or the subsumer is the empty concept (Bottom), adding specific assertions or inconsistency constraints to the underlying MILP model. For general concept pairs, it checks if the required degree is 1.0 (crisp logic); if so, it applies an optimization by adding a linear inequality constraint to the MILP model and incrementing the counter for 0-1 variables. Otherwise, it constructs a Gödel implication concept and adds a corresponding assertion to the knowledge base.

        :param ind: The individual instance to which the General Concept Inclusion is applied, serving as the subject for the generated assertions.
        :type ind: Individual
        :param gci: The General Concept Inclusion axiom containing the subsumed concept, subsumer concept, and degree of subsumption to be enforced.
        :type gci: GeneralConceptInclusion
        """

        c: Concept = gci.get_subsumed()
        d: Concept = gci.get_subsumer()
        Util.debug(f"{constants.SEPARATOR}Applying GCI{constants.SEPARATOR}")
        Util.debug(f"{d} g-subsumes {c} >= {gci.get_degree()}")
        l: Degree = gci.get_degree()

        if c.type == ConceptType.TOP:
            if d.type == ConceptType.BOTTOM:
                # Inconsistency
                self.milp.add_new_constraint(
                    Expression(1.0), InequalityType.EQUAL, DegreeNumeric.get_degree(0.0)
                )
            else:
                # a:D >= n
                new_ass: Assertion = Assertion(ind, d, l)
                self.add_assertion(new_ass)
        else:
            not_c: Concept = -c
            if d.type == ConceptType.BOTTOM:
                # a: \not C >= n
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
                    # xIndIsC <= xIndIsD
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
                    # a : C g-implies D >= L
                    self.add_assertion(Assertion(ind, c_impl_d, l))
        Util.debug(f"{constants.SEPARATOR}GCI completed{constants.SEPARATOR}")

    def solve_kleene_dienes_gci(
        self, ind: Individual, gci: GeneralConceptInclusion
    ) -> None:
        """
        Applies a General Concept Inclusion (GCI) constraint to a specific individual using Kleene-Dienes implication semantics. It retrieves the subsumed and subsumer concepts from the GCI and constructs an implication relationship, preserving the associated degree of truth. If the subsumed concept is the universal concept (Top), the method optimizes the operation by directly asserting the subsumer concept for the individual; otherwise, it asserts the derived implication concept. This action modifies the state of the knowledge base by adding a new assertion.

        :param ind: The individual instance to which the General Concept Inclusion rule is applied.
        :type ind: Individual
        :param gci: The subsumption rule to be applied, providing the subsumed concept, subsumer concept, and the degree of the implication.
        :type gci: GeneralConceptInclusion
        """

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
        """
        This method enforces a General Concept Inclusion (GCI) for a specific individual using Zadeh fuzzy logic semantics by translating the logical relationship into a constraint within a Mixed-Integer Linear Programming (MILP) model. It ensures that the membership degree of the individual in the subsumer concept is greater than or equal to its membership in the subsumed concept, effectively implementing the fuzzy implication $C(x) \le D(x)$. If the subsumed concept is the universal concept (TOP), the method handles this edge case by directly asserting that the individual belongs to the subsumer concept with a degree of 1.0. As side effects, the method increments the internal counter of binary variables, adds assertions to the knowledge base, and registers a new inequality constraint with the MILP solver.

        :param ind: The individual instance to which the General Concept Inclusion is applied.
        :type ind: Individual
        :param gci: The General Concept Inclusion axiom representing the subsumption relationship to be enforced on the individual using Zadeh semantics.
        :type gci: GeneralConceptInclusion
        """

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
            # xIndIsC <= xIndIsD
            self.milp.add_new_constraint(
                Expression(1.0, Term(-1.0, x_ind_is_not_c), Term(-1.0, x_ind_is_d)),
                InequalityType.LESS_THAN,
            )
        Util.debug(f"{constants.SEPARATOR}GCI completed{constants.SEPARATOR}")

    def solve_reflexive_role(self, role: str) -> None:
        """
        Materializes the reflexive property for a specific role by asserting that every individual currently in the knowledge base is related to itself via that role. This method iterates through all existing individuals and adds a self-relation with a degree of 1.0, effectively enforcing the axiom that the role holds for every entity. Note that this operation modifies the knowledge base state and only applies to individuals present at the time of execution; individuals added subsequently will not inherit this relation unless the method is invoked again.

        :param role: The role to be made reflexive, establishing a self-relation for every individual.
        :type role: str
        """

        for ind in self.individuals.values():
            self.add_relation(ind, role, ind, DegreeNumeric.get_degree(1.0))

    @typing.overload
    def solve_reflexive_roles(self, ind: Individual) -> None: ...

    @typing.overload
    def solve_reflexive_roles(self) -> None: ...

    def solve_reflexive_roles(self, *args) -> None:
        """
        Resolves reflexive role axioms by applying logic that infers relationships where an entity is related to itself. The method operates in two distinct modes depending on the arguments provided: it can apply the axiom globally to the entire knowledge base when called with no arguments, or it can target a specific individual when an `Individual` instance is passed. This process updates the internal state of the knowledge base to incorporate the new inferences derived from the reflexivity property.

        :param args: Variable arguments determining the scope of the operation. If empty, solves reflexive roles globally; if provided, must be a single Individual instance to solve for that specific entity.
        :type args: typing.Any
        """

        assert len(args) in [0, 1]
        if len(args) == 0:
            self.__solve_reflexive_roles_2()
        else:
            assert isinstance(args[0], Individual)
            self.__solve_reflexive_roles_1(*args)

    def __solve_reflexive_roles_1(self, ind: Individual) -> None:
        """
        Enforces the reflexivity axiom for a specific individual by iterating through all roles defined as reflexive within the knowledge base. For each such role, it establishes a self-relation where the individual acts as both the subject and the object, assigning a certainty degree of 1.0. This method modifies the internal state of the knowledge base by adding these necessary relations, ensuring that the individual satisfies all reflexive role constraints.

        :param ind: The individual instance to which reflexive role relations are applied, linking it to itself.
        :type ind: Individual
        """

        for role in self.reflexive_roles:
            self.add_relation(ind, role, ind, DegreeNumeric.get_degree(1.0))

    def __solve_reflexive_roles_2(self) -> None:
        """Iterates over the collection of reflexive roles defined in the knowledge base to process their associated axioms. For each role in the collection, the method delegates the specific resolution logic to `solve_reflexive_role`, thereby updating the internal state of the knowledge base to incorporate the implications of reflexivity. This method performs no explicit validation on the collection itself and returns no value."""

        for role in self.reflexive_roles:
            self.solve_reflexive_role(role)

    @typing.overload
    def get_correct_version_of_individual(self, ass: Assertion) -> None: ...

    @typing.overload
    def get_correct_version_of_individual(self, rel: Relation) -> None: ...

    def get_correct_version_of_individual(self, *args) -> None:
        """
        This method ensures that the `Individual` referenced by a specific object is updated to the correct version within the `KnowledgeBase`, which is essential for maintaining consistency after operations like cloning the knowledge base or merging individuals. It acts as a dispatcher that accepts a single argument, which must be an instance of either `Assertion` or `Relation`, and delegates the update logic to the appropriate internal handler. If the provided argument is not of the expected type, a `ValueError` is raised, and an `AssertionError` occurs if the number of arguments is not exactly one. The method modifies the passed object in place and returns `None`.

        :param args: A single argument, either an Assertion or a Relation, used to identify the correct version of the individual.
        :type args: typing.Any

        :raises ValueError: Raised if the provided argument is not an instance of Assertion or Relation.
        """

        assert len(args) == 1
        if isinstance(args[0], Assertion):
            self.__get_correct_version_of_individual_1(*args)
        elif isinstance(args[0], Relation):
            self.__get_correct_version_of_individual_2(*args)
        else:
            raise ValueError

    def __get_correct_version_of_individual_1(self, ass: Assertion) -> None:
        """
        Updates the provided assertion to reference the canonical instance of its associated individual within the knowledge base, ensuring consistency during operations like cloning or merging. It compares the individual currently held by the assertion against the knowledge base's internal registry; if the objects differ and the individual is not blockable, the assertion is modified to point to the knowledge base's version. This method effectively synchronizes the assertion's reference to match the state of the knowledge base, preventing issues related to object identity mismatches.

        :param ass: The assertion to be checked and updated to ensure it references the correct instance of its associated individual.
        :type ass: Assertion
        """

        ind: Individual = ass.get_individual()
        ind2: Individual = self.individuals.get(str(ind))
        if id(ind) == id(ind2):
            return
        if ind2 is None:
            ind2 = self.get_individual(str(ind))
        if not ind.is_blockable():
            ass.set_individual(ind2)

    def __get_correct_version_of_individual_2(self, rel: Relation) -> None:
        """
        Updates the relation's target individual to the version stored within the current knowledge base, provided the individual is not blockable. This is primarily used to resolve references after cloning or merging the knowledge base, ensuring that relations point to valid, local instances rather than stale external objects. The method compares the object identity of the relation's current target with the entry found in the internal registry; if they differ and the target is not blockable, the relation is modified to reference the local individual.

        :param rel: The relation to be updated to ensure its object individual points to the correct instance in the current knowledge base.
        :type rel: Relation
        """

        ind: Individual = rel.get_object_individual()
        ind2: Individual = self.individuals.get(str(ind))
        if id(ind) == id(ind2):
            return
        if ind2 is None:
            ind2 = self.get_individual(str(ind))
        if not ind.is_blockable():
            rel.set_object_individual(ind2)

    def solve_concrete_value_assertions(self) -> None:
        """Processes and resolves datatype restrictions, specifically concrete value assertions, for individuals within the knowledge base. The method begins by iterating through pending positive assertions, dispatching to the DatatypeReasoner to apply logic for "at most", "at least", and "exact" value constraints. Following this, it processes negative assertions by examining concrete role restrictions on individuals and applying rules for complemented value constraints. Execution may halt early if a blockable individual is currently blocked, and the method enforces a hard limit on the total number of defined individuals. Upon completion, the list of positive assertions is cleared, and internal counters tracking rule applications are updated."""

        # Positive restrictions
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
            # Check type of the assertion
            self.rules_applied[KnowledgeBaseRules.RULE_DATATYPE] += 1
            if ass.get_type() == ConceptType.AT_MOST_VALUE:
                DatatypeReasoner.apply_at_most_value_rule(ass, self)
            elif ass.get_type() == ConceptType.AT_LEAST_VALUE:
                DatatypeReasoner.apply_at_least_value_rule(ass, self)
            elif ass.get_type() == ConceptType.EXACT_VALUE:
                DatatypeReasoner.apply_exact_value_rule(ass, self)
            Util.debug(f"{constants.SEPARATOR}")

        self.positive_concrete_value_assertions.clear()

        # Negative restrictions
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

                    # Check type of the assertion
                    self.rules_applied[KnowledgeBaseRules.RULE_NOT_DATATYPE] += 1
                    if OperatorConcept.is_not_at_most_value(ass.get_concept()):
                        self.rule_complemented_at_most_datatype_restriction(b, ass)
                    elif OperatorConcept.is_not_at_least_value(ass.get_concept()):
                        self.rule_complemented_at_least_datatype_restriction(b, ass)
                    elif OperatorConcept.is_not_exact_value(ass.get_concept()):
                        self.rule_complemented_exact_datatype_restriction(b, ass)
                    Util.debug(f"{constants.SEPARATOR * 2}")

    def solve_functional_roles(self) -> None:
        """Iterates through all defined functional roles and individuals within the knowledge base to enforce functional role constraints. For each individual that has not already been merged, it invokes the merge logic to ensure that the individual has at most one filler for the given functional role. This process modifies the internal state of the knowledge base by merging individuals to satisfy the axioms, effectively reducing the number of distinct entities where functional role violations exist."""

        for role in self.functional_roles:
            for name, ind in self.individuals.items():
                # We skip the individual if has already been merged
                if str(ind) != name:
                    continue
                self.merge_fillers(ind, role)

    def merge_fillers(self, ind: Individual, func_role: str) -> None:
        """
        This method enforces the functional role constraint for a specific individual by consolidating multiple fillers into a single concept. If the individual possesses two or more fillers for the specified functional role, the method identifies the first filler as the primary target and iteratively merges all subsequent fillers into it. This process involves invoking the internal merge logic to combine the entities and updating the knowledge base's individual registry to map the names of the merged individuals to the target. If the individual has no relations for the specified role, the method returns without performing any action.

        :param ind: The subject individual whose multiple fillers for the specified functional role will be consolidated into a single concept.
        :type ind: Individual
        :param func_role: The name of the functional role relation used to identify the filler individuals to be merged.
        :type func_role: str
        """

        rels: list[Relation] = ind.role_relations.get(func_role)
        if rels is None:
            return
        a_name: str = str(rels[0].get_object_individual())
        a: Individual = self.individuals.get(a_name)
        for rel in rels[1:]:
            b_name: str = str(rel.get_object_individual())
            b: Individual = self.individuals.get(b_name)

            # If a and b have different names
            if a != b:
                self.merge(a, b)
                self.individuals[b_name] = a

    def merge(self, a: Individual, b: Individual) -> None:
        """
        Merges individual `b` into individual `a`, consolidating their identities within the knowledge base. If `a` is a `CreatedIndividual` and `b` is not, the roles are swapped to ensure the merge targets the root individual. The process redirects all incoming relations to `b` so that they point to `a`, and transfers outgoing relations from `b` to `a` provided the target individual is not blockable. All concept and existential assertions associated with `b` are reassigned to `a`, and the underlying MILP variables are updated accordingly. When both individuals are root individuals, a constraint is added to enforce the Unique Name Assumption, ensuring they cannot both exist simultaneously. After the merge, individual `b` is pruned.

        :param a: The target individual into which the other individual is merged. This object is modified in place to absorb the relations, assertions, and constraints of the second individual.
        :type a: Individual
        :param b: The individual to be merged into `a`. This individual acts as the source of the merge, having its relations and assertions absorbed into `a`.
        :type b: Individual
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
        """
        Adds a General Concept Inclusion (GCI) axiom to the knowledge base using Gödel logic semantics. This method asserts that the first concept is subsumed by the second concept, establishing a hierarchical relationship where the subsumed concept is considered a subset of the subsumer concept with a minimum truth value specified by the degree parameter. The operation modifies the internal state of the knowledge base by registering this fuzzy implication, delegating the storage logic to the underlying subsumption handler with the specific logic operator type set to Gödel.

        :param conc1: The concept that is subsumed by `conc2`.
        :type conc1: Concept
        :param conc2: The concept acting as the subsumer (super-concept) in the inclusion.
        :type conc2: Concept
        :param degree: The lower bound for the truth value of the implication.
        :type degree: Degree
        """

        self.add_subsumption(conc2, conc1, degree, LogicOperatorType.GOEDEL)

    def lukasiewicz_implies(
        self, conc1: Concept, conc2: Concept, degree: Degree
    ) -> None:
        """
        Adds a fuzzy General Concept Inclusion (GCI) constraint based on Lukasiewicz logic to the knowledge base. This method establishes that the first concept is subsumed by the second concept, effectively defining an implication relationship where the extent of the first concept is contained within the extent of the second. The provided degree parameter acts as a lower bound for the truth value of this implication, ensuring the relationship holds with at least the specified confidence. As a side effect, this constraint modifies the internal state of the knowledge base, potentially influencing the outcome of future reasoning tasks.

        :param conc1: The concept that is subsumed by the second concept.
        :type conc1: Concept
        :param conc2: The concept that subsumes the first argument (the super-concept).
        :type conc2: Concept
        :param degree: The lower bound for the degree of truth of the implication.
        :type degree: Degree
        """

        self.add_subsumption(conc2, conc1, degree, LogicOperatorType.LUKASIEWICZ)

    def kleene_dienes_implies(
        self, conc1: Concept, conc2: Concept, degree: Degree
    ) -> None:
        """
        Adds a General Concept Inclusion (GCI) axiom to the knowledge base utilizing the Kleene-Dienes implication operator. This method establishes a fuzzy subsumption relationship where the first concept is considered to be subsumed by the second concept, subject to a specified lower bound degree of truth. By invoking the internal subsumption handler, it permanently modifies the knowledge base's state to reflect this specific logical constraint.

        :param conc1: The concept that is subsumed (the antecedent).
        :type conc1: Concept
        :param conc2: The concept acting as the subsumer (consequent) in the implication.
        :type conc2: Concept
        :param degree: Minimum truth value for the implication.
        :type degree: Degree
        """

        self.add_subsumption(conc2, conc1, degree, LogicOperatorType.KLEENE_DIENES)

    def zadeh_implies(self, conc1: Concept, conc2: Concept) -> None:
        """
        Adds a Zadeh General Concept Inclusion to the knowledge base, asserting that the first concept is subsumed by the second concept. This method registers the implication with a fixed degree of 1.0 using Zadeh logic operators, thereby modifying the internal state of the knowledge base to include this specific constraint.

        :param conc1: The concept that is subsumed by the second concept.
        :type conc1: Concept
        :param conc2: The concept that acts as the subsumer (super-concept) in the implication.
        :type conc2: Concept
        """

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
        """
        Adds a General Concept Inclusion (GCI) to the knowledge base, defining a subsumption relationship where the first concept is the subsumer and the second concept is the subsumed, associated with a specific truth degree and logic operator type. If the provided degree is 1.0 and the logic type is not Kleene-Dienes, the method automatically defaults the logic type to Lukasiewicz. Before insertion, it performs a redundancy check; if the inclusion is already implied by the current knowledge base, the method returns without modifying the state. Depending on the structure of the subsumed concept, the method either delegates to a specific handler for atomic concepts or adds the GCI directly.

        :param conc2: The concept acting as the subsumer in the General Concept Inclusion.
        :type conc2: Concept
        :param conc1: The concept that is subsumed by `conc2` (the subclass or specific concept).
        :type conc1: Concept
        :param degree: The truth value or strength of the subsumption relationship, representing the degree to which the subsumer concept implies the subsumed concept.
        :type degree: Degree
        :param logic_type: Specifies the logic operator defining the semantics of the implication for the General Concept Inclusion.
        :type logic_type: LogicOperatorType
        """

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
        """
        Integrates a new concept axiom into the knowledge base by applying specific absorption rules. This method serves as a dispatcher that accepts either a PrimitiveConceptDefinition or a GeneralConceptInclusion along with a boolean flag indicating whether the operation should be atomic. Based on the type of the axiom provided, the execution is delegated to the appropriate internal absorption routine. The method returns a boolean indicating whether the knowledge base was modified as a result of the operation, and it raises a ValueError if the input type is unsupported.

        :param args: A tuple consisting of a concept definition (PrimitiveConceptDefinition or GeneralConceptInclusion) followed by a boolean flag indicating atomicity.
        :type args: typing.Any

        :raises ValueError: Raised when the first argument is not an instance of PrimitiveConceptDefinition or GeneralConceptInclusion.

        :return: True if the application of the concept absorption rules resulted in changes to the ontology, False otherwise.

        :rtype: bool
        """

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
        """
        This method performs the initial absorption of a primitive concept definition, specifically applying the CA0 and FA0 normalization rules. It checks whether the concept being defined is already present in the knowledge base's internal definitions; if the concept is new, the method adds the axiom to the internal incremental structure and removes the definition from the current processing context. This process modifies the state of the knowledge base by registering the new concept. The method returns `True` if the definition was successfully absorbed and changes were made, and `False` if the concept was already defined and no action was taken.

        :param pcd: The primitive concept definition containing the axiom to be absorbed.
        :type pcd: PrimitiveConceptDefinition
        :param atomic: True if the right-hand side of the subsumption is an atomic concept, False if it is a complex description.
        :type atomic: bool

        :return: True if the concept definition was absorbed and the internal state was modified, False if the concept was already defined.

        :rtype: bool
        """

        a: str = pcd.get_defined_concept()
        # CA0, FA0
        if a not in self.t_definitions:
            self.add_axiom_to_inc(a, pcd)
            self.remove_A_is_a_X(a, pcd, atomic)
            Util.debug(f"Absorbed axioms_A_is_a_C CA0, FA0: {pcd}")
            return True
        return False

    def __concept_absorption_2(
        self, tau: GeneralConceptInclusion, atomic: bool
    ) -> bool:
        """
        Applies specific concept absorption rules to a general concept inclusion in order to normalize the knowledge base. The method evaluates the structure of the subsumed and subsumer concepts against patterns defined by rules CA1, CA2, CA3, FA1, FA2.1, and FA2.2. If a pattern is identified—such as a complemented atomic concept in the subsumer or an atomic concept within a conjunction in the subsumed side—the method derives a new primitive concept definition, registers it within the knowledge base, and removes the original axiom. It returns true if a transformation was successfully applied, indicating a change in the state, and false otherwise.

        :param tau: The general concept inclusion axiom to be processed for absorption.
        :type tau: GeneralConceptInclusion
        :param atomic: Flag indicating if the inclusion has an atomic subsumer (C isA A) or a general subsumer (C isA D).
        :type atomic: bool

        :return: True if the concept absorption rules were successfully applied and the ontology was modified; False if no rules matched and no changes were made.

        :rtype: bool
        """

        # Computes is the degree of the axiom is one
        degree: Degree = tau.get_degree()
        n: float = typing.cast(DegreeNumeric, degree).get_numerical_value()
        degree_is_one: bool = n == 1.0

        conc1: Concept = tau.get_subsumed()
        conc2: Concept = tau.get_subsumer()
        key: str = str(conc1)
        implication_type: LogicOperatorType = tau.get_type()
        type_c1: ConceptType = conc1.type
        type_c2: ConceptType = conc2.type

        # CA1, FA1
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

        # CA2, FA2.1
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
                    if str(new_c1) in self.t_definitions:
                        continue
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

        # CA3, FA3
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
                if not (ci.is_atomic() and str(ci) not in self.t_definitions):
                    continue
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

        # FA2.2
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
        """
        Applies role absorption inference rules to the knowledge base, acting as a dispatcher that delegates to specific internal logic based on the argument types. It accepts either a single `PrimitiveConceptDefinition` or a `GeneralConceptInclusion` paired with a boolean flag indicating atomicity. The execution of this method modifies the internal state of the knowledge base to normalize the ontology, and it returns a boolean value indicating whether any changes were made during the absorption process.

        :param args: Variable-length arguments defining the absorption context: either a single PrimitiveConceptDefinition or a GeneralConceptInclusion paired with a boolean flag.
        :type args: typing.Any

        :return: True if the role absorption rules caused any modifications to the internal state, False otherwise.

        :rtype: bool
        """

        assert len(args) in [1, 2]
        if len(args) == 1:
            assert isinstance(args[0], PrimitiveConceptDefinition)
            return self.__role_absorption_1(*args)
        else:
            assert isinstance(args[0], GeneralConceptInclusion)
            assert isinstance(args[1], bool)
            return self.__role_absorption_2(*args)

    def __role_absorption_1(self, tau: PrimitiveConceptDefinition) -> bool:
        """
        This method attempts to absorb a primitive concept definition into a role domain constraint, specifically targeting universal restrictions with a crisp degree. It evaluates two distinct absorption rules, RE2 and RE3, which are conditionally applied based on the crispness of the role, the implication operator type, and the active fuzzy logic semantics. If the conditions for a rule are satisfied, the method derives a corresponding implication concept, assigns it as the domain for the associated role, and removes the original definition from the knowledge base. The function returns a boolean flag indicating whether the knowledge base state was modified during the process.

        :param tau: The primitive concept definition to be processed for role absorption, specifically checking if it contains a universal restriction that can be absorbed into a role domain.
        :type tau: PrimitiveConceptDefinition

        :return: True if the definition was modified by the role absorption rules, False otherwise.

        :rtype: bool
        """

        conc1: Concept = self.get_concept(tau.get_defined_concept())
        conc2: Concept = tau.get_definition()
        key: str = str(conc1)
        implication_type: LogicOperatorType = tau.get_type()
        type_c2: ConceptType = conc2.type
        n: float = tau.get_degree()
        degree_is_one: bool = n == 1.0

        if type_c2 == ConceptType.ALL and degree_is_one:
            role: str = conc2.role

            # RE2
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

            # RE3
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
        """
        Applies a set of role absorption rules to transform a General Concept Inclusion (GCI) into simpler role domain or range constraints. The method inspects the structure of the subsumed and subsumer concepts, checking for patterns such as existential restrictions, universal restrictions, or conjunctions containing existential restrictions. The applicability of specific rules depends on the degree of the axiom (often requiring a crisp value of 1.0) and the active fuzzy logic semantics (e.g., Gödel, Łukasiewicz, Zadeh). If a matching rule is found, the original GCI is removed from the knowledge base and replaced with a corresponding role domain or range axiom. The method returns true if the knowledge base was modified and false otherwise.

        :param tau: The general concept inclusion axiom to which the role absorption rules are applied.
        :type tau: GeneralConceptInclusion
        :param atomic: Indicates whether the subsumer is an atomic concept (C isA A) or a complex description (C isA D).
        :type atomic: bool

        :return: True if a role absorption rule was successfully applied to the general concept inclusion, resulting in changes to the ontology; False if no rules were applicable and no changes occurred.

        :rtype: bool
        """

        # Computes is the degree of the axiom is one
        degree: Degree = tau.get_degree()
        n: float = typing.cast(DegreeNumeric, degree).get_numerical_value()
        degree_is_one: bool = n == 1.0

        conc1: Concept = tau.get_subsumed()
        conc2: Concept = tau.get_subsumer()
        key: str = str(conc1)
        implication_type: LogicOperatorType = tau.get_type()
        type_c1: ConceptType = conc1.type
        type_c2: ConceptType = conc2.type

        # RB1
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

        # RB2
        if (
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

        # RE1
        if type_c1 in (ConceptType.SOME, ConceptType.HAS_VALUE) and degree_is_one:
            assert isinstance(conc1, HasRoleInterface)
            c: Concept = ImpliesConcept.goedel_implies(conc1, conc2)
            self.role_domain(conc1.role, c)
            self.remove_C_is_a_X(key, tau, atomic)
            Util.debug(f"Absorbed: domain {conc1.role}, {c}")
            return True

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

            # RE2
            if self.is_crisp_role(role) and (
                implication_type != LogicOperatorType.KLEENE_DIENES
                or constants.KNOWLEDGE_BASE_SEMANTICS == FuzzyLogic.CLASSICAL
            ):
                c: Concept = ImpliesConcept.goedel_implies(conc1, conc2)
                self.role_domain(role, c)
                self.remove_C_is_a_X(key, tau, atomic)
                Util.debug(f"Absorbed: domain {role}, {c}")
                return True

            # RE3
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
                else:  # if (typeC2 == Concept.NOT_HAS_VALUE)
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

        # RE4
        # test as for CA3, FA3
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
                # Now test if there is a 'some' concept, so apply RE4
                if ci.type in (ConceptType.SOME, ConceptType.HAS_VALUE):
                    del vc[j]
                    if ci.type == ConceptType.SOME:
                        ci: AllSomeConcept = typing.cast(AllSomeConcept, ci)
                    else:
                        ci: HasValueConcept = typing.cast(HasValueConcept, ci)

                    # Build the new implication
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

                    # Build the domain axiom according to RE4
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
        """
        Applies General Concept Inclusion (GCI) transformation rules to the knowledge base, serving as a dispatcher that routes specific inputs to the appropriate internal transformation logic. The method accepts either a single `PrimitiveConceptDefinition` or a `GeneralConceptInclusion` paired with a boolean flag to determine which transformation rules to apply. It validates the number and types of arguments, raising an `AssertionError` if the inputs do not match the expected signatures. The process modifies the internal state of the knowledge base and returns a boolean indicating whether any changes were made during the transformation.

        :param args: Input arguments for the transformation, accepting either a PrimitiveConceptDefinition or a GeneralConceptInclusion paired with an atomic boolean flag.
        :type args: typing.Any

        :return: True if the application of the transformation rules resulted in changes to the internal state, False otherwise.

        :rtype: bool
        """

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
        """
        This method applies the first set of General Concept Inclusion (GCI) transformation rules to decompose complex axioms into simpler components based on their logical structure. Specifically, it checks if the subsumer (the right-hand side of the inclusion) is a conjunction (AND) or if the subsumed concept (the left-hand side) is a disjunction (OR). If the subsumer is a conjunction, the method distributes the subsumption over the conjuncts, adding new axioms that assert the subsumed concept is included in each operand of the conjunction. Conversely, if the subsumed concept is a disjunction, it distributes the subsumption over the disjuncts, adding axioms that assert each operand of the disjunction is included in the subsumer. The method supports both standard logic operators and Goedel fuzzy logic operators, modifying the knowledge base by adding the resulting axioms and returning a boolean indicating whether any transformations were applied.

        :param tau: The general concept inclusion axiom to which the transformation rules are applied.
        :type tau: GeneralConceptInclusion
        :param atomic: Indicates whether the subsumer is an atomic concept (true) or a complex concept (false).
        :type atomic: bool

        :return: True if the transformation rules were applied and new axioms were added, False if the input structure did not match the required patterns.

        :rtype: bool
        """

        # Computes is the degree of the axiom is one
        degree: Degree = tau.get_degree()
        n: float = typing.cast(DegreeNumeric, degree).get_numerical_value()

        conc1: Concept = tau.get_subsumed()
        conc2: Concept = tau.get_subsumer()
        implication_type: LogicOperatorType = tau.get_type()
        type_c1: ConceptType = conc1.type
        type_c2: ConceptType = conc2.type

        # CT1, FT1
        if type_c2 in (ConceptType.AND, ConceptType.GOEDEL_AND):
            conc2: OperatorConcept = typing.cast(OperatorConcept, conc2)
            for ci in conc2.concepts:
                # conc1 => ci implicationType n
                self.gci_transformation_add_axiom_to_C_is_a_X(
                    ci, conc1, degree, implication_type
                )
                Util.debug(f"Absorbed CT1, FT1: {conc1} ==> {ci}")
            return True

        # CT2, FT2
        if type_c1 in (ConceptType.OR, ConceptType.GOEDEL_OR):
            conc1: OperatorConcept = typing.cast(OperatorConcept, conc1)
            for ci in conc1.concepts:
                # ci => conc2 implicationType n
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
        """
        Applies a specific General Concept Inclusion (GCI) transformation rule to a primitive concept definition, specifically handling conjunctions on the right-hand side of the definition. If the definition is a conjunction (either standard AND or Goedel AND), the method decomposes it by generating a new implication from the defined concept to each operand within the conjunction, effectively absorbing the definition into the knowledge base. The method returns a boolean indicating whether the transformation was applied; it returns true if the definition was a conjunction and false if the definition structure did not match the criteria for this rule.

        :param pcd: The primitive concept definition to be processed, specifically to check for conjunctions in its definition body and generate corresponding implications.
        :type pcd: PrimitiveConceptDefinition

        :return: True if the transformation was applied to the primitive concept definition, False if the definition type did not match the criteria for this transformation.

        :rtype: bool
        """

        a: str = pcd.get_defined_concept()
        conc2: Concept = pcd.get_definition()
        implication_type: LogicOperatorType = pcd.get_type()
        n: float = pcd.get_degree()
        type_c2: ConceptType = conc2.type

        # CT1, FT1
        if type_c2 in (ConceptType.AND, ConceptType.GOEDEL_AND):
            conc2: OperatorConcept = typing.cast(OperatorConcept, conc2)
            for ci in conc2.concepts:
                # a => ci implicationType n
                self.gci_transform_define_atomic_concept(a, ci, implication_type, n)
                Util.debug(f"Absorbed CT1, FT1: {a} ==> {ci}")
            return True
        return False

    def nominal_absorption(
        self, conc1: Concept, conc2: Concept, degree: Degree
    ) -> bool:
        """
        Applies the nominal absorption rule to transform a subsumption relationship where the subsumer is a 'hasValue' restriction into an assertion about an individual. If the second concept is a 'hasValue' restriction, the method infers that the individual filler belongs to a universal restriction defined by the inverse role and the first concept, adding this assertion to the knowledge base. As a side effect, the method ensures the existence of the inverse role, creating it if necessary. The method returns `True` if the transformation was applied and the knowledge base modified, or `False` if the subsumer concept was not a 'hasValue' restriction.

        :param conc1: The concept serving as the filler for the universal restriction applied to the individual.
        :type conc1: Concept
        :param conc2: Subsumer concept containing the nominal restriction to be absorbed.
        :type conc2: Concept
        :param degree: The lower bound for the degree of certainty or membership associated with the assertion added to the individual.
        :type degree: Degree

        :return: True if the nominal absorption rule was applied and the knowledge base was modified, False otherwise.

        :rtype: bool
        """

        # (R hasValue o) => D >= \alpha is replaced by o : (all R^- D) >= \alpha
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
        """
        Adds a General Concept Inclusion (GCI) axiom to the knowledge base, asserting that the subsumed concept `conc2` is included in the subsumer concept `conc1` with a specified degree and logic type. The method performs several preprocessing checks: it defaults the logic type to Lukasiewicz for crisp degrees (1.0), skips addition if the axiom is redundant, and handles nominal absorption if applicable. When an identical GCI (matching concepts and logic type) already exists, the method updates the stored degree only if the new degree is strictly greater; otherwise, the request is ignored. If no matching axiom is found, the new GCI is stored in the appropriate internal collection based on whether the subsumer is atomic or complex.

        :param conc1: The concept acting as the subsumer (super-concept) in the General Concept Inclusion.
        :type conc1: Concept
        :param conc2: The concept that is subsumed (the subclass or left-hand side of the inclusion).
        :type conc2: Concept
        :param degree: The truth value or confidence level representing the strength of the implication.
        :type degree: Degree
        :param logic_type: Specifies the logic operator or implication semantics (e.g., Lukasiewicz, Kleene-Dienes) used to interpret the subsumption relationship.
        :type logic_type: LogicOperatorType
        """

        new_degree: float = typing.cast(DegreeNumeric, degree).get_numerical_value()
        if new_degree == 1.0 and logic_type != LogicOperatorType.KLEENE_DIENES:
            logic_type = LogicOperatorType.LUKASIEWICZ
        if self.is_redundant_gci(conc2, conc1, logic_type, new_degree):
            return

        # CT3
        if self.nominal_absorption(conc1, conc2, degree):
            return

        # Check GCI does not exist
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

            # If there exists a similar GCI, replace the GCI or not add it
            if conc1 != old_c1 or conc2 != old_c2 or curr_gci.get_type() != logic_type:
                continue
            # If the existing GCI has a smaller degree, replace it
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
        """
        Adds a graded General Concept Inclusion (GCI) to the knowledge base, asserting that the subsumed concept is a subsumer concept with a specified degree and logical operator type. The method first checks for redundancy or applies nominal absorption; if either condition is met, the operation terminates without modification. Otherwise, it searches for an existing GCI with identical concepts and logic type, updating the degree to the higher value if a match is found. If no matching axiom exists, the new GCI is added to the internal collection, which is indexed by the subsumed concept.

        :param conc1: The concept acting as the subsumer (parent) in the General Concept Inclusion.
        :type conc1: Concept
        :param conc2: The concept that is being subsumed (the subclass) in the General Concept Inclusion.
        :type conc2: Concept
        :param degree: The numerical degree representing the strength or lower bound of the subsumption relationship. If an equivalent axiom already exists, a higher degree value will replace the existing one.
        :type degree: Degree
        :param logic_type: Specifies the logical operator or implication semantics for the General Concept Inclusion.
        :type logic_type: LogicOperatorType
        """

        n: float = typing.cast(DegreeNumeric, degree).get_numerical_value()
        if self.is_redundant_gci(conc2, conc1, logic_type, n):
            return
        # CT3
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
        """
        Constructs a General Concept Inclusion (GCI) axiom asserting that the subsumed concept is included in the subsumer concept, qualified by a specific degree and logic operator type. The method first validates the axiom by checking for redundancy; if the relationship is already present or implied, the method returns without making changes. If the axiom is new, it is stored in a temporary dictionary structure, with the specific target dictionary determined by the complexity of the subsumer concept: atomic subsumers are added to `axioms_to_do_tmp_C_is_a_A`, whereas complex subsumers are added to `axioms_to_do_tmp_C_is_a_D`. In both cases, the axiom is indexed using the string representation of the subsumed concept.

        :param conc1: The concept acting as the subsumer (right-hand side) of the General Concept Inclusion.
        :type conc1: Concept
        :param conc2: The concept that is subsumed by `conc1` in the General Concept Inclusion.
        :type conc2: Concept
        :param degree: The degree value associated with the General Concept Inclusion, representing a lower bound for the implication.
        :type degree: Degree
        :param logic_type: The logical operator type defining the semantics of the implication for the General Concept Inclusion.
        :type logic_type: LogicOperatorType
        """

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
        """
        This method adds a General Concept Inclusion (GCI) to the knowledge base, defining a subsumption relationship where the second concept is subsumed by the first. It accepts a degree representing a lower bound and a logic operator type to define the semantic implication of the relationship. Depending on the value of the `atomic` flag, the method delegates the storage of the axiom to either the collection of atomic axioms or the collection of non-atomic axioms, thereby updating the internal state of the knowledge base without returning a value.

        :param conc1: The concept acting as the subsumer (super-concept) in the General Concept Inclusion.
        :type conc1: Concept
        :param conc2: The concept that is being subsumed (the subclass) in the General Concept Inclusion.
        :type conc2: Concept
        :param degree: The lower bound of the truth value for the implication.
        :type degree: Degree
        :param logic_type: Defines the semantics of the implication for the General Concept Inclusion (GCI).
        :type logic_type: LogicOperatorType
        :param atomic: Flag indicating whether to add the axiom to the atomic (C is a A) or complex (C is a D) subsumption list.
        :type atomic: bool
        """

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
        """
        Adds a General Concept Inclusion (GCI) axiom to the knowledge base, asserting that the subsumed concept (`conc2`) is a specialization of the subsumer concept (`conc1`) with a specified degree and logic type. The method first checks for redundancy and applies nominal absorption logic; if the axiom is found to be redundant or absorbed, the operation terminates without modifying the state. Otherwise, the new GCI is stored in the `axioms_C_is_a_D` dictionary, keyed by the string representation of the subsumed concept, allowing multiple inclusions for the same subsumed concept to coexist.

        :param conc1: The concept acting as the superclass or parent category that subsumes the other concept in the General Concept Inclusion.
        :type conc1: Concept
        :param conc2: The concept that is subsumed by `conc1` (the subclass).
        :type conc2: Concept
        :param degree: The numeric lower bound for the truth degree of the subsumption relationship.
        :type degree: Degree
        :param logic_type: Specifies the semantics of the implication operator for the General Concept Inclusion.
        :type logic_type: LogicOperatorType
        """

        n: float = typing.cast(DegreeNumeric, degree).get_numerical_value()
        if self.is_redundant_gci(conc2, conc1, logic_type, n):
            return

        # CT3
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
        """
        Adds a General Concept Inclusion (GCI) to the knowledge base, defining a subsumption relationship where `conc1` is subsumed by `conc2`. The method's handling of the `degree` parameter is contingent upon the active fuzzy logic semantics; if the semantics are Lukasiewicz, the provided `degree` is used as the lower bound for the inclusion. Conversely, for Zadeh or Classical semantics, the input `degree` is ignored, and the relationship is enforced with a crisp degree of 1.0. This operation modifies the internal state of the knowledge base by registering the new subsumption rule.

        :param conc1: The concept that is subsumed by the second concept.
        :type conc1: Concept
        :param conc2: The concept that subsumes the first argument.
        :type conc2: Concept
        :param degree: The truth value or strength of the implication, representing the lower bound for the subsumption relationship.
        :type degree: Degree
        """

        if constants.KNOWLEDGE_BASE_SEMANTICS == FuzzyLogic.LUKASIEWICZ:
            self.add_subsumption(conc2, conc1, degree, LogicOperatorType.LUKASIEWICZ)
        else:  # ZADEH or CLASSICAL
            self.add_subsumption(
                conc2,
                conc1,
                DegreeNumeric.get_degree(1.0),
                LogicOperatorType.LUKASIEWICZ,
            )

    def get_inclusion_degree(self, subsumed: str, subsumer: str) -> float:
        """
        Retrieves the pre-computed inclusion degree indicating how much one role is subsumed by another within the knowledge base's hierarchy. The method checks the internal mapping of roles to their ancestors to locate the specific degree value associated with the subsumer. If the subsumer is not an ancestor of the subsumed role, or if the subsumed role is not present in the hierarchy, the function returns 0.0.

        :param subsumed: The identifier of the funcRole acting as the subset or child in the inclusion relationship.
        :type subsumed: str
        :param subsumer: The identifier of the role acting as the parent or superset in the inclusion relationship.
        :type subsumer: str

        :return: The degree of inclusion of the `subsumed` role within the `subsumer` role, or 0.0 if no relationship is found.

        :rtype: float
        """

        parents: dict[str, float] = self.roles_with_all_parents.get(subsumed)
        if parents is not None:
            d: float = parents.get(subsumer)
            if d is not None:
                return d
        return 0.0

    def create_roles_with_all_parents(self) -> None:
        """Computes the transitive closure of the role inclusion axioms to determine all direct and indirect ancestors for every role in the knowledge base. This method iterates through the direct parent relationships stored in `roles_with_parents`, recursively traversing the hierarchy to populate `roles_with_all_parents` with a complete mapping of roles to their ancestors and associated inclusion degrees. When multiple paths lead to the same ancestor, the method retains the maximum inclusion degree encountered. As a side effect, it also updates the set of functional roles by marking any role as functional if it subsumes another functional role with an inclusion degree of exactly 1.0."""

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

            # If func(R2) and R1 subsumes R2 with degree 1, then func(R1)
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
        """
        Recursively traverses the role hierarchy to compute the transitive closure of Role Inclusion Axioms, populating a dictionary with all ancestor roles reachable from a specified starting role. For each parent of the `current_role`, the method calculates a cumulative degree based on the input degree `n1` and the parent's associated degree. If a parent role is not yet recorded in the `all_parents` dictionary, it is added with the computed degree, and the recursion proceeds to explore its ancestors. If the parent already exists in the dictionary, the method updates the entry and continues recursion only if the newly computed degree is strictly greater than the existing value, effectively pruning paths that do not yield a higher degree. The method modifies the `all_parents` dictionary in place and explicitly skips processing the root role `role_c` to prevent immediate cycles.

        :param role_c: The role serving as the starting point of the traversal, representing the original child role for which ancestors are being collected.
        :type role_c: str
        :param all_parents: Accumulator dictionary mapping discovered parent role names to their computed degrees during the recursive traversal.
        :type all_parents: dict[str, float]
        :param current_role: The role currently being visited to retrieve its immediate parents and update the transitive closure.
        :type current_role: str
        :param n1: Accumulated degree of the current role relative to the starting role.
        :type n1: float
        """

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
        """Populates the dictionary mapping parent roles to their immediate children that are defined as transitive, which is a prerequisite for computing the transitive closure of role inclusion axioms. The method iterates over roles that have parents, filters for those marked as transitive, and registers the child role under each of its parents. This operation modifies the instance attribute storing transitive children in place, appending new children to existing lists for each parent role."""

        for role_c in self.roles_with_all_parents:
            if role_c not in self.transitive_roles:
                continue
            parents: dict[str, float] = self.roles_with_all_parents.get(role_c, dict())
            for role_p in parents:
                self.roles_with_trans_children[role_p] = (
                    self.roles_with_trans_children.get(role_p, []) + [role_c]
                )

    def role_subsumes(self, subsumer: str, subsumed: str, n: float) -> None:
        """
        This method adds a Role Inclusion Axiom to the knowledge base, defining a hierarchical relationship where the `subsumed` role is included in the `subsumer` role with a lower bound degree `n`. It modifies the internal `roles_with_parents` structure to reflect this relationship, handling edge cases such as identical roles by returning immediately. If the relationship between the two roles already exists, the method compares the new degree with the existing one and updates the record only if the new degree is higher, thereby preserving the maximum confidence level for the axiom.

        :param subsumer: The identifier of the super-role that includes the `subsumed` role. It represents the parent in the inclusion hierarchy.
        :type subsumer: str
        :param subsumed: The functional role that is included in or is a subset of the subsumer role.
        :type subsumed: str
        :param n: Degree of the subsumption relationship, representing the strength of the inclusion.
        :type n: float
        """

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
        """
        Evaluates whether a subsumer role subsumes a subsumed role within the knowledge base, considering a specified degree of inclusion. The method supports two argument formats: a standard three-argument version consisting of the role names and a numeric degree, and a four-argument version that includes a dictionary defining parent roles and their weights. It performs strict type validation on the inputs and delegates the computation to internal helper methods, returning a boolean result that indicates the validity of the subsumption relationship.

        :param args: Variable arguments specifying the subsumer role, subsumed role, and degree. An optional fourth argument provides a dictionary mapping roles to their parents.
        :type args: typing.Any

        :raises ValueError: Raised when the number of arguments provided is not 3 or 4.

        :return: True if the subsumer role subsumes the subsumed role according to the specified degree and optional parent list, False otherwise.

        :rtype: bool
        """

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
        """
        This method manages the inclusion hierarchy between functional roles by attempting to add or update a Role Inclusion Axiom with a specified degree. It prevents self-subsumption by immediately returning false if the subsumer and subsumed roles are identical. If the relationship does not already exist, it is recorded with the provided degree; if it does exist, the degree is updated only if the new value is strictly greater than the stored one. The method modifies the internal role hierarchy structure and returns a boolean indicating whether the knowledge base was actually changed, while also logging the operation for debugging purposes.

        :param subsumer: The identifier of the parent role that subsumes the target role.
        :type subsumer: str
        :param subsumed: The identifier of the role that is being subsumed (the child role) in the inclusion axiom.
        :type subsumed: str
        :param n: The degree of the subsumption relationship. The axiom is added or updated only if this value is greater than the existing degree.
        :type n: float

        :return: True if the role inclusion axiom was added or updated with a higher degree, False if the subsumer and subsumed are identical or if an existing axiom already has a greater or equal degree.

        :rtype: bool
        """

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
        """
        This method updates the provided role hierarchy dictionary with a new or refined inclusion axiom, defining that the 'subsumed' role is a child of the 'subsumer' role with a specific degree. If the relationship does not exist, it is added to the dictionary; if it exists, the degree is updated only if the new value is strictly greater than the current one. The function returns a boolean indicating success, returning False if the subsumer and subsumed roles are identical or if the existing degree is already greater than or equal to the proposed value. As a side effect, the input dictionary is mutated directly to reflect these changes.

        :param subsumer: The identifier of the parent role or super-role in the inclusion axiom.
        :type subsumer: str
        :param subsumed: The identifier of the role that is a sub-role of the subsumer, acting as the child in the inclusion axiom.
        :type subsumed: str
        :param n: The degree of the role inclusion axiom. The axiom is added or updated only if this value is strictly greater than the existing degree.
        :type n: float
        :param p_list: A dictionary mapping subsumed roles to dictionaries of their subsumer roles and inclusion degrees.
        :type p_list: dict[str, dict[str, float]]

        :return: True if the role inclusion axiom was added or updated with a higher degree; False if the axiom already exists with a greater or equal degree, or if the subsumer and subsumed are identical.

        :rtype: bool
        """

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
        """
        Removes the direct blocking constraint applied by a specific ancestor to its children. The method retrieves the list of children currently blocked by the ancestor, deletes the ancestor's entry from the internal tracking dictionary, and triggers the unblocking process for each child individually. If the ancestor does not exist in the blocked records, the method performs no operation.

        :param ancestor: Name of the ancestor individual whose children are to be unblocked.
        :type ancestor: str
        """

        # Directly blocked children
        db_children: list[str] = self.directly_blocked_children.get(ancestor)
        if db_children is None:
            return
        del self.directly_blocked_children[ancestor]
        for name in db_children:
            self.unblock_individual(name)

    def unblock_individual(self, node_name: str) -> None:
        """
        Unblocks the specified individual and all of its descendants within the knowledge base, reversing a previous blocking operation. This method retrieves the target individual by name and utilizes the `CreatedIndividualHandler` to process both directly and indirectly blocked nodes. As a side effect, it marks these nodes as unchecked, re-queuing them for further reasoning, and restores any existential ("some") assertions that were suspended while the nodes were blocked. This operation modifies the internal state of the knowledge base to allow continued expansion or validation of the affected individuals.

        :param node_name: The name of the ancestor individual to unblock.
        :type node_name: str
        """

        node: CreatedIndividual = typing.cast(
            CreatedIndividual, self.individuals.get(node_name)
        )
        # Mark the nodes that are directly blocked as uncheck and put back the "some" assertions
        CreatedIndividualHandler.unblock_directly_blocked(node, self)
        # Mark the nodes that are indirectly blocked as uncheck and put back the "some" assertions
        CreatedIndividualHandler.mark_indirectly_simple_unchecked(node, self)

        # node.unblock_directly_blocked(self)
        # node.mark_indirectly_simple_unchecked(self)

    def check_trans_role_applied(self, rel: Relation, restrict: Restriction) -> bool:
        """
        Determines whether a specific transitivity rule defined by the provided relation and restriction has already been processed. It constructs a unique identifier from the relation and the restriction's name (excluding degree) and checks for its presence in an internal registry. If the rule is found, the method returns True; otherwise, it registers the rule by adding it to the list and returns False. This method has the side effect of modifying the internal registry to ensure idempotency, preventing redundant application of the same transitivity logic.

        :param rel: The relation involved in the transitivity rule being checked.
        :type rel: Relation
        :param restrict: The universal restriction component of the transitivity rule to check.
        :type restrict: Restriction

        :return: True if the transitivity rule for the given relation and restriction has already been applied; False otherwise.

        :rtype: bool
        """

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
        """
        Constructs a Concept representing a datatype restriction on a specific concrete feature, defined by a restriction type (such as equality, at-most, or at-least) and a target value. The method validates that the specified feature exists within the knowledge base and ensures the provided value is type-compatible with the feature's definition (e.g., string, integer, real, or boolean). It handles complex value objects, such as feature functions, by resolving them to underlying fuzzy numbers or MILP variables. If the value type is incompatible with the feature type, the method returns the "bottom" concept, representing a logical contradiction. Additionally, boolean features are restricted to exact value comparisons only. As a side effect, string values and the resulting concepts are tracked in temporary lists for subsequent processing steps.

        :param restriction_type: Specifies the comparison logic for the restriction, determining if the feature value must be at most, at least, or exactly equal to the provided value.
        :type restriction_type: RestrictionType
        :param o: The value to compare against the concrete feature. It can be a literal, a variable, a triangular fuzzy number, or a feature function, and must be compatible with the feature's type.
        :type o: typing.Any
        :param f_name: Name of the concrete feature to which the restriction applies.
        :type f_name: str

        :return: A Concept representing the specified value restriction on the feature, or the bottom concept if the provided value is incompatible with the feature's type.

        :rtype: Concept
        """

        # Check that feature exists
        t: typing.Optional[ConcreteFeature] = self.concrete_features.get(f_name)
        if t is None:
            Util.error(f"Error: Concrete feature {f_name} is not defined")
        # In functions of the form (number), we replace with a double number for efficiency
        if isinstance(o, FeatureFunction):
            fun: FeatureFunction = typing.cast(FeatureFunction, o)
            f_type: FeatureFunctionType = fun.get_type()
            if f_type == FeatureFunctionType.ATOMIC:
                name: str = str(fun)
                tfn: typing.Optional[TriangularFuzzyNumber] = self.fuzzy_numbers.get(
                    name
                )
                if tfn is not None:
                    o = tfn
                else:
                    bv: bool = self.milp.has_variable(name)
                    if bv:
                        o = self.milp.get_variable(name)
            elif f_type == FeatureFunctionType.NUMBER:
                o = fun.get_number()

        # Check type is coherent with o
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

        # Create concept
        if restriction_type == RestrictionType.AT_MOST_VALUE:
            c: Concept = ValueConcept.at_most_value(f_name, o)
        elif restriction_type == RestrictionType.AT_LEAST_VALUE:
            c: Concept = ValueConcept.at_least_value(f_name, o)
        else:  # if (restriction_type == RestrictionType.EXACT_VALUE)
            c: Concept = ValueConcept.exact_value(f_name, o)

        # Mark concept containing a string restriction (for a later replacing)
        if t_type == ConcreteFeatureType.STRING:
            self.temp_string_concept_list.append(c)
        return c

    def get_language(self) -> str:
        """
        Retrieves the specific Description Logic language associated with the fuzzy knowledge base. The returned string indicates the expressivity of the ontology, typically falling within the range from ALC to SHIF(D). This method is a read-only accessor and has no side effects on the internal state of the object.

        :return: The description logic language of the fuzzy knowledge base, ranging from ALC to SHIF(D).

        :rtype: str
        """

        return self.language

    def compute_language(self) -> None:
        """Determines the Description Logic expressivity of the knowledge base by analyzing its structural components. It constructs a language string—ranging from ALC to SHIF(D)—by checking for the presence of transitive roles, role hierarchies, nominals, inverse roles, functional roles, and concrete fuzzy concepts. The resulting expressivity string is stored in the `language` attribute, and the method subsequently configures the MILP solver's nominal variables based on whether the language includes nominals or functional abstract roles."""

        if len(self.transitive_roles) != 0:
            self.language = "S"
        else:
            self.language = "ALC"
        if len(self.roles_with_parents) != 0 or len(self.symmetric_roles) != 0:
            self.language += "H"
        if self.has_nominals_in_tbox() or self.has_nominals_in_abox():
            self.language += "B"
        if (
            len(self.inverse_functional_roles) != 0
            or len(self.inverse_roles) != 0
            or len(self.symmetric_roles) != 0
        ):
            self.language += "I"
        if len(self.inverse_functional_roles) != 0 or len(self.functional_roles) != 0:
            self.language += "F"
        if self.concrete_fuzzy_concepts:
            self.language += "(D)"

        Util.debug(f"Expressivity = {self.language}")

        self.milp.set_nominal_variables(
            "B" in self.language or self.has_functional_abstract_roles()
        )

    def has_functional_abstract_roles(self) -> bool:
        """
        Determines whether the knowledge base defines any roles that are simultaneously functional and abstract. This method iterates through the collection of functional roles and checks for their presence within the set of abstract roles. It returns True immediately upon finding the first such intersection, ensuring efficient detection without modifying the state of the knowledge base.

        :return: True if the knowledge base contains at least one role that is both functional and abstract, otherwise False.

        :rtype: bool
        """

        for f in self.functional_roles:
            if f in self.abstract_roles:
                return True
        return False

    def has_nominals_in_abox(self) -> bool:
        """
        Inspects the assertions within the ABox to determine if any associated concepts contain nominals. This method iterates through the collection of assertions, checking each concept for the presence of nominal constructs. It returns True immediately upon finding the first instance of a nominal, or False if no such constructs are found after examining all assertions.

        :return: True if any assertion in the ABox contains a concept with nominals, False otherwise.

        :rtype: bool
        """

        for ass in self.assertions:
            if ass.get_concept().has_nominals():
                return True
        return False

    def has_nominals_in_tbox(self) -> bool:
        """
        Determines whether the TBox component of the knowledge base contains any nominals by inspecting all stored axioms. It iterates through concept equivalence axioms, concept inclusion axioms (GCIs), concept definitions, and attribute-related axioms, checking the associated class expressions for the presence of nominals. The search is short-circuited, returning `True` immediately upon finding the first nominal, and `False` only if no nominals are found in any TBox axiom.

        :return: True if the TBox contains any nominals, False otherwise.

        :rtype: bool
        """

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
        """Determines the appropriate blocking strategy for the reasoning process based on the structural characteristics of the ontology and specific configuration flags. This method updates the instance attributes `blocking_type` and `blocking_dynamic` to reflect the selected strategy, which can range from no blocking to various forms of subset, set, or double blocking. The logic evaluates the presence of inverse, functional, and transitive roles, as well as the acyclicity and dependencies of the TBox, to decide on the most efficient valid blocking type. If optimizations are disabled, it defaults to Double Blocking. Furthermore, it calculates whether the blocking must be dynamic, typically required when inverse roles or domain restrictions are present."""

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
        """This method transforms string-based data restrictions into integer-based ones to facilitate processing, typically for optimization solvers. It operates by sorting the unique strings found in the temporary string list and assigning them sequential integer identifiers. If strings are present, it updates any concrete features currently typed as `STRING` to `INTEGER`, adjusting their value ranges to accommodate the new encoding, and replaces the string values in the associated concept assertions with their corresponding integer identifiers. Additionally, it registers these mappings with the internal MILP solver and clears the temporary string storage lists upon completion. If the temporary string list is empty or uninitialized, the method performs no action."""

        if self.temp_string_list != None:
            # Sort strings
            self.temp_string_list = sorted(self.temp_string_list)
            # Get set of strings in assertions
            num_strings: int = 0
            if len(self.temp_string_list) > 0:
                num_strings += 1
                previous: str = self.temp_string_list[0]
                self.order[previous] = int(num_strings)
                for current in self.temp_string_list[1:]:
                    if previous != current:
                        num_strings += 1
                        self.order[current] = num_strings
                    previous = current
            # If there are strings
            if num_strings > 0:
                # Change the type of the concrete features from String to Integer
                for t in self.concrete_features.values():
                    if t.get_type() == ConcreteFeatureType.STRING:
                        t.set_type(ConcreteFeatureType.INTEGER)
                        t.set_range(0, num_strings + 1)
                # Replace string s_i with order(s_i)
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
        """
        Adds a constraint to the knowledge base that restricts the value of a specific variable to the interval [k1, k2]. This method can be called with either three or four arguments. With three arguments, the restriction is applied unconditionally to the target variable. With four arguments, the restriction is conditional, taking effect only if a second control variable is non-zero. The method updates the knowledge base's internal state to reflect these new bounds.

        :param args: Variable-length arguments defining the target variable, bounds, and an optional condition. Accepts either (x_b, k1, k2) or (x_b, x_f, k1, k2), where x_f determines if the restriction is active.
        :type args: typing.Any
        """

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
        """
        Enforces a bounded range for a specific variable by adding two linear inequality constraints to the underlying Mixed-Integer Linear Programming (MILP) model. The method restricts the variable `x_b` to be greater than the lower bound `k1` and less than the upper bound `k2`. This operation directly modifies the state of the MILP solver associated with the knowledge base.

        :param x_b: The variable to be constrained within the specified bounds.
        :type x_b: Variable
        :param k1: The lower bound defining the minimum value allowed for the variable.
        :type k1: float
        :param k2: The upper bound defining the maximum limit of the variable's range.
        :type k2: float
        """

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
        This method conditionally restricts the domain of the variable `x_b` to the interval `[k1, k2]` by adding linear constraints to the underlying MILP model. The restriction is enforced only when the flag variable `x_f` is non-zero; if `x_f` is zero, the constraints are relaxed, effectively removing the bounds on `x_b` using a large constant value. This implementation relies on a "Big-M" formulation to switch the constraints on or off based on the value of `x_f`.

        :param x_b: The variable to be restricted to the range [k1, k2].
        :type x_b: Variable
        :param x_f: A conditional switch variable; if non-zero, the bounds `[k1, k2]` are enforced on `x_b`.
        :type x_f: Variable
        :param k1: The lower bound of the allowed range for the variable.
        :type k1: float
        :param k2: The upper bound defining the maximum value of the range.
        :type k2: float
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
        """
        Creates a new individual entity within the knowledge base, supporting two distinct initialization modes depending on the arguments provided. When invoked without arguments, the method generates a standalone individual. Alternatively, if a parent individual and a role name string are supplied, it creates a new individual and establishes a relationship linking it to the parent via the specified role, effectively integrating it into the existing structure. The method validates that the parent is an instance of Individual and the role name is a string, though it permits `None` values for these parameters, and returns a `CreatedIndividual` object representing the newly generated entity.

        :param args: Variable length argument list specifying the creation context. Can be empty to create a standalone individual, or a parent Individual and a role name string to establish a relationship.
        :type args: typing.Any

        :return: A CreatedIndividual object representing the newly created individual, which may be standalone or associated with a parent individual and role name.

        :rtype: CreatedIndividual
        """

        assert len(args) in [0, 2]
        if len(args) == 0:
            return self.__get_new_individual_1()
        else:
            assert args[0] is None or isinstance(args[0], Individual)
            assert args[1] is None or isinstance(args[1], str)
            return self.__get_new_individual_2(*args)

    def __get_new_individual_1(self) -> CreatedIndividual:
        """
        Creates and returns a new individual instance that is not associated with a parent entity or a specific role name. This method acts as a specialized wrapper around the general `get_new_individual` function, passing `None` for both the parent and role name parameters to generate a standalone entity. It is useful for initializing root-level concepts or independent objects within the knowledge base without establishing immediate hierarchical relationships.

        :return: A new CreatedIndividual instance initialized without a parent or role name.

        :rtype: CreatedIndividual
        """

        return self.get_new_individual(None, None)

    def __get_new_individual_2(
        self, parent: Individual, f_name: str
    ) -> CreatedIndividual:
        """
        This method orchestrates the creation and immediate registration of a new individual entity within the knowledge base, utilizing a specified parent individual and role name. It delegates the core instantiation logic to a common code routine, ensuring the new entity is properly initialized relative to its parent. A significant side effect of this operation is the modification of the internal state, as the newly created individual is automatically added to the knowledge base's collection using its string representation as an identifier before being returned.

        :param parent: The existing individual that serves as the parent for the new entity.
        :type parent: Individual
        :param f_name: Name of the role defining the relationship from the parent to the new individual.
        :type f_name: str

        :return: The newly created and added individual, linked to the specified parent via the given role name.

        :rtype: CreatedIndividual
        """

        b: CreatedIndividual = self.get_new_individual_common_code(parent, f_name)
        self.add_individual(str(b), b)
        return b

    def get_new_individual_common_code(
        self, parent: Individual, f_name: str
    ) -> CreatedIndividual:
        """
        Creates a new `CreatedIndividual` instance linked to the specified parent via the provided role name, assigning it a unique identifier based on an internal counter. This method updates internal knowledge base state, including role successors and the maximum depth, but explicitly avoids adding the new individual to the main collection of individuals. It is designed to handle the common logic of individual instantiation and metadata updates without permanently registering the entity within the knowledge base.

        :param parent: The source instance for the new individual, linked via the specified role.
        :type parent: Individual
        :param f_name: The name of the role connecting the parent individual to the new individual.
        :type f_name: str

        :return: A CreatedIndividual instance representing a new entity with a unique generated name, linked to the specified parent through the provided role name.

        :rtype: CreatedIndividual
        """

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
        """
        Creates and returns a new concrete individual linked to the specified parent individual through the provided role name. The method performs the necessary initialization logic, marks the individual as concrete, and registers it within the knowledge base's internal registry of created individuals. This process ensures that the new entity is tracked by the system immediately upon creation, distinguishing it from temporary or unregistered objects.

        :param parent: The existing individual that serves as the parent for the new concrete individual.
        :type parent: Individual
        :param f_name: Name of the role from the parent to the new individual.
        :type f_name: str

        :return: A new concrete individual instance linked to the specified parent via the given role name, which has not yet been added to the main KB individuals list.

        :rtype: CreatedIndividual
        """

        b: CreatedIndividual = self.get_new_individual_common_code(parent, f_name)
        b.set_concrete_individual()
        self.add_created_individual(str(b), b)
        return b

    def solve_one_exist_assertion(self) -> None:
        """Processes a single existential assertion from the queue, applying blocking optimizations and handling resource constraints. The method iterates through pending assertions, skipping any that have already been processed. If the assertion involves a blockable individual that is currently blocked, the assertion is moved to a blocked list and deferred. Otherwise, provided the maximum number of individuals has not been reached, the method applies the existential rule to expand the knowledge base, marks the assertion as processed, and removes it from the queue. If the individual limit is exceeded, an error is logged."""

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
        """Prepares the fuzzy knowledge base for reasoning by performing a series of necessary preprocessing and compilation steps. If no specific logic semantics have been defined, it defaults to Lukasiewicz fuzzy logic. The method computes the language, converts symbolic strings into integer representations for efficiency, and resolves various role axioms including inverse, inclusion, reflexive, and functional properties. Additionally, it preprocesses the Terminological Box (TBox), prints its current state, and determines the appropriate blocking type for the reasoning algorithm. Upon completion, it sets an internal flag indicating that the knowledge base is fully loaded and ready for queries."""

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
        """Iterates through all individuals and their associated role relations within the knowledge base to enforce domain and range constraints. For each relation instance, the method applies the defined domain and range restrictions by invoking specific lazy unfolding rules, which updates the internal state of the knowledge base to reflect the consequences of these axioms. This process ensures that the types of individuals involved in relationships are consistent with the schema definitions, modifying the knowledge base in place without returning a value."""

        for ind in self.individuals.values():
            for rels in ind.role_relations.values():
                for rel in rels:
                    for domain_role in self.domain_restrictions:
                        self.rule_domain_lazy_unfolding(domain_role, rel)
                    for range_role in self.range_restrictions:
                        self.rule_range_lazy_unfolding(range_role, rel)

    def rule_domain_lazy_unfolding(self, domain_role: str, rel: Relation) -> None:
        """
        Applies the domain lazy unfolding rule to propagate domain restrictions from a specific role to the subject individual of a given relation. The method first determines the inclusion degree between the relation's role and the target domain role, defaulting to full inclusion if the roles are identical. If the inclusion degree is positive and the subject individual is not indirectly blocked, the method retrieves the concepts associated with the domain restriction and adds corresponding assertions to the knowledge base. Finally, it generates and adds fuzzy logic constraints to the internal MILP solver, enforcing that the subject's membership in these concepts is consistent with the relation's truth value according to the currently configured fuzzy logic semantics (Lukasiewicz or Zadeh).

        :param domain_role: The role identifier used to look up domain restrictions and determine the inclusion degree relative to the input relation.
        :type domain_role: str
        :param rel: The relation instance to be processed, providing the subject individual and role for deriving constraints.
        :type rel: Relation
        """

        role: str = rel.get_role_name()
        n: float = self.get_inclusion_degree(role, domain_role)
        if domain_role == role:
            n = 1.0
        if n > 0.0:
            a: Individual = rel.get_subject_individual()

            # If the individual is indirectly blocked, exit
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
                else:
                    ZadehSolver.and_geq_equation(a_is_c, x_rel, n, self.milp)

    def rule_range_lazy_unfolding(self, range_role: str, rel: Relation) -> None:
        """
        Applies the range lazy unfolding rule to a specific relation and range restriction role within the knowledge base. This process enforces that if a relation holds, the object of that relation must satisfy the concepts defined in the range restrictions of the specified role. The method first calculates the inclusion degree between the relation's role and the target range role, defaulting to 1.0 if they are identical. If the inclusion degree is non-positive, or if the object individual is indirectly blocked, the method exits without effect. Otherwise, it iterates over the concepts associated with the range restriction, adding assertions to the knowledge base and retrieving or creating corresponding variables in the Mixed-Integer Linear Programming (MILP) model. Finally, it adds fuzzy logic constraints (supporting either Lukasiewicz or Zadeh semantics) to the model, linking the truth degree of the relation, the inclusion degree, and the truth degree of the object belonging to the range concept.

        :param range_role: The identifier of the role defining the range restrictions to be applied.
        :type range_role: str
        :param rel: The relation instance to which the rule is applied, providing the role and object individual for constraint generation.
        :type rel: Relation
        """

        role: str = rel.get_role_name()
        n: float = self.get_inclusion_degree(role, range_role)
        if range_role == role:
            n = 1.0
        if n > 0.0:
            b: Individual = rel.get_object_individual()

            # If the individual is indirectly blocked, exit
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
                else:
                    ZadehSolver.and_geq_equation(b_is_c, x_rel, n, self.milp)

    def solve_abox(self) -> None:
        """Processes and resolves all fuzzy assertions associated with the ABox. This operation is idempotent; it checks the internal `ABOX_EXPANDED` flag and only proceeds with solving if the assertions have not yet been processed. If processing is required, it delegates to `solve_assertions` and subsequently sets the `ABOX_EXPANDED` flag to True to prevent redundant computation in future calls."""

        if not self.ABOX_EXPANDED:
            self.solve_assertions()
            self.ABOX_EXPANDED = True

    def solve_assertions(self) -> None:
        """
        Iteratively processes the queue of fuzzy assertions to determine satisfiability and membership degrees within the knowledge base. It begins by verifying that the knowledge base is not already marked as unsatisfiable, raising an exception if it is. For each assertion, the method checks for blocking conditions and zero-degree lower bounds to optimize processing, then dispatches to specific reasoning rules based on the concept type—ranging from standard logical constructs to complex fuzzy operators like Gödel or Łukasiewicz implications. This process updates the internal Mixed-Integer Linear Programming (MILP) model with new constraints and clears the assertion queue, repeating the cycle until no further assertions remain in the main or existential queues. Finally, it triggers the resolution of concrete value assertions to complete the reasoning process.

        :raises InconsistentOntologyException: Raised if the fuzzy knowledge base is unsatisfiable, indicating that no valid model exists for the current assertions.
        """

        if self.KB_UNSAT:
            raise InconsistentOntologyException("Unsatisfiable fuzzy KB")

        # We will exit only after solving all assertions
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
                    # Atomic but complemented
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
                elif c_type == ConceptType.SIGMA_CONCEPT:
                    self.rule_sigma_concept(ass)
                elif OperatorConcept.is_not_sigma_concept(ci):
                    self.rule_complemented_sigma_concept(ass)
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
        """
        Resolves a concept assertion for a specified individual by dispatching to a specialized solver based on the specific type of the concept provided. The method supports a wide range of fuzzy logic and aggregation constructs, including Choquet and Sugeno integrals, Ordered Weighted Averaging (OWA), weighted arithmetic operations, and concrete numerical concepts defined by crisp, linear, or membership functions such as triangular or trapezoidal shapes. It also handles concepts that have been modified by linguistic hedges. If the provided concept does not correspond to any recognized or supported type, a ValueError is raised. This method performs operations through delegation and modifies the internal state of the knowledge base or individual rather than returning a value.

        :param ind: The individual entity for which the concept assertion is being solved.
        :type ind: Individual
        :param concept: The concept assertion to be solved.
        :type concept: Concept

        :raises ValueError: Raised if the provided concept is not one of the supported concept types.
        """

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
        # elif isinstance(concept, SigmaConcept):
        #     self.solve_sigma_concept_assertion(ind, concept)
        else:
            raise ValueError

    def solve_concept_complemented_assertion(
        self, ind: Individual, lower_limit: Degree, concept: Concept
    ) -> None:
        """
        Processes a complemented concept assertion for a specified individual by delegating to specialized handlers based on the structure of the concept. The method inspects the concept to determine if it represents the negation of a Choquet integral, Sugeno integral, OWA, weighted aggregation operator, or a modified concept, and subsequently invokes the appropriate resolution routine. The `lower_limit` parameter is specifically passed to handlers for modifiers and fuzzy concrete concepts to constrain the solution. This operation updates the internal state of the knowledge base to reflect the solved assertion, and it raises a ValueError if the concept type is unsupported or unrecognized.

        :param ind: The individual entity for which the complemented concept assertion is being solved.
        :type ind: Individual
        :param lower_limit: The minimum degree threshold used when solving the complemented assertion.
        :type lower_limit: Degree
        :param concept: The concept representing the complemented assertion to be solved.
        :type concept: Concept

        :raises ValueError: Raised when the provided concept does not match any supported operator or atom type required for solving.
        """

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
        # elif isinstance(concept, OperatorConcept) and isinstance(
        #     concept.get_atom(), SigmaConcept
        # ):
        #     self.solve_sigma_concept_complement_assertion(
        #         ind, concept
        #     )
        else:
            raise ValueError

    def solve_modifier_assertion(
        self, ind: Individual, concept: Concept, modifier: Modifier
    ) -> None:
        """
        Resolves a modified concept assertion for a specified individual by delegating the task to specialized handlers based on the type of the provided modifier. This method acts as a dispatcher, routing the request to specific implementations for linear or triangular modifiers to ensure the correct logic is applied. If the modifier type is not recognized or supported, a ValueError is raised to indicate an invalid input.

        :param ind: The individual for which the modified concept assertion is being solved.
        :type ind: Individual
        :param concept: The concept assertion to be resolved for the individual.
        :type concept: Concept
        :param modifier: The modification rule (e.g., linear or triangular) used to solve the concept assertion.
        :type modifier: Modifier

        :raises ValueError: Raised if the provided modifier is not an instance of LinearModifier or TriangularModifier.
        """

        if isinstance(modifier, LinearModifier):
            self.solve_linear_modifier_assertion(ind, concept, modifier)
        elif isinstance(modifier, TriangularModifier):
            self.solve_triangular_modifier_assertion(ind, concept, modifier)
        else:
            raise ValueError

    def solve_choquet_integral_assertion(
        self, ind: Individual, c: ChoquetIntegral
    ) -> None:
        """
        Encodes the logic for a Choquet integral concept assertion into the underlying Mixed-Integer Linear Programming (MILP) model for a specific individual. It begins by retrieving the degree variables for the component concepts associated with the individual and ensures these sub-assertions are added to the model. To satisfy the sorting requirement of the Choquet integral, the method introduces auxiliary binary variables to generate an ordered permutation of the component degrees. It then constructs a linear expression based on the Choquet integral formula, applying the provided weights to the sorted variables. Finally, it adds a constraint to the MILP model that equates this calculated expression to the degree variable of the individual with respect to the Choquet integral concept itself.

        :param ind: The individual entity for which the Choquet integral assertion is being solved.
        :type ind: Individual
        :param c: The Choquet integral concept assertion to be evaluated, providing the component concepts and weights necessary to construct the integral constraint.
        :type c: ChoquetIntegral
        """

        # New n variables
        n: int = len(c.concepts)
        x: list[Variable] = [None] * n
        for i in range(n):
            ci = c.concepts[i]
            x[i] = self.milp.get_variable(ind, ci)
            self.add_assertion(ind, ci, DegreeVariable.get_degree(x[i]))

        # y1 > y2 > ... > yn
        z: list[list[Variable]] = [
            [self.milp.get_new_variable(VariableType.BINARY) for _ in range(n)]
            for _ in range(n)
        ]
        y: list[Variable] = self.milp.get_ordered_permutation(x, z)

        # y1 w1 + \sum^{n}_{i=2} yi (wi - wi-1) = x_{ind:CI}
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
        """
        Encodes the logic for a complemented Choquet integral concept assertion into the underlying Mixed-Integer Linear Programming (MILP) model for a specific individual. It retrieves the Choquet integral atom from the provided operator concept and generates MILP variables representing the degrees of the negated sub-concepts. The method establishes an ordering constraint on these variables to simulate the sorting required by the integral calculation, utilizing auxiliary binary variables. Using the integral's weights and the sorted variables, it constructs a linear expression representing the Choquet integral value and adds an equality constraint linking this expression to the degree variable of the original concept. Finally, it triggers the complemented rule logic for the individual and concept.

        :param ind: The individual entity for which the complemented Choquet integral concept assertion is being solved.
        :type ind: Individual
        :param c: The complemented Choquet integral concept assertion to be solved.
        :type c: OperatorConcept
        """

        assert isinstance(c.get_atom(), ChoquetIntegral)
        ci: ChoquetIntegral = c.get_atom()

        # New n variables
        n: int = len(ci.concepts)
        x: list[Variable] = [None] * n
        for i in range(n):
            not_ci = -ci.concepts[i]
            x[i] = self.milp.get_variable(ind, not_ci)
            self.add_assertion(ind, not_ci, DegreeVariable.get_degree(x[i]))

        # y1 > y2 > ... > yn
        z: list[list[Variable]] = [
            [self.milp.get_new_variable(VariableType.BINARY) for _ in range(n)]
            for _ in range(n)
        ]
        y: list[Variable] = self.milp.get_ordered_permutation(x, z)

        # 1 - y1 w1 - \sum^{n}_{i=2} yi (wi - wi-1) = x_{ind:not CI}
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
        """
        Translates a fuzzy logic Ordered Weighted Averaging (OWA) concept assertion into a set of constraints within the underlying Mixed-Integer Linear Programming (MILP) model. It retrieves the membership variables for the individual across the sub-concepts defined in the OWA operator and ensures that these sub-concepts are asserted. Depending on the system configuration, the method either constructs an explicit ordering of the variables to apply weights or utilizes an optimized algebraic reformulation involving pairwise minimum operations to avoid sorting. In both cases, it adds a new equality constraint to the solver that links the degree of the OWA concept to the aggregated degrees of its constituent concepts.

        :param ind: The specific individual entity for which the OWA concept assertion is being solved.
        :type ind: Individual
        :param c: The OWA or QOWA concept containing the constituent concepts and weights used to construct the aggregation constraint.
        :type c: typing.Union[fuzzy_dl_owl2.fuzzydl.concept.owa_concept.OwaConcept, fuzzy_dl_owl2.fuzzydl.concept.qowa_concept.QowaConcept]
        """

        if ConfigReader.OPTIMIZATIONS == 0:
            # New n variables x_i
            n: int = len(c.concepts)
            x: list[Variable] = []
            for i in range(n):
                ci: Concept = c.concepts[i]
                x.append(self.milp.get_variable(ind, ci))
                self.add_assertion(ind, ci, DegreeVariable.get_degree(x[i]))

            # y1 > y2 > ... > yn
            y: list[Variable] = self.milp.get_ordered_permutation(x)

            # \sum_{i} wi * yi = x_{ind:OWA}
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
            # (1/n - (w_n - w_1)/2) \sum^n_{i=1} x_i
            x: list[Variable] = []
            for i in range(n):
                ci: Concept = c.concepts[i]
                x.append(self.milp.get_variable(ind, ci))
                self.add_assertion(ind, ci, DegreeVariable.get_degree(x[i]))
                exp.add_term(Term(a, x[i]))

            # (w_n - w_1) / (n-1) \sum_{i,j} \min\{ x_i, x_j \}
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
        """
        This method translates a logical assertion involving a complemented Ordered Weighted Averaging (OWA) or Quantified OWA (QOWA) concept into a set of constraints within the underlying Mixed-Integer Linear Programming (MILP) model. It decomposes the OWA concept into its constituent sub-concepts and recursively ensures that the negations of these sub-concepts are asserted, thereby defining their membership degrees. To satisfy the sorting semantics of OWA aggregation, the method retrieves an ordered permutation of the variables representing the individual's membership in the sub-concepts. It then adds a linear equality constraint to the MILP model that defines the membership degree of the complemented concept as one minus the weighted sum of the ordered sub-concept degrees. This process modifies the MILP model state and may trigger further constraint generation for the nested negated concepts.

        :param ind: The individual entity for which the complemented OWA concept assertion is being solved.
        :type ind: Individual
        :param curr_concept: The complemented OWA or QOWA concept assertion, providing the weights and sub-concepts needed to construct the MILP constraints.
        :type curr_concept: OperatorConcept
        """

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

        # y1 > y2 > ... > yn
        y: list[Variable] = self.milp.get_ordered_permutation(x)

        # 1 - \sum_{i} wi * yi = xAinNotWS
        exp: Expression = Expression(1.0, Term(-1.0, x_A_in_not_WS))
        for j in range(n):
            exp.add_term(Term(-c.weights[j], y[j]))
        self.milp.add_new_constraint(exp, InequalityType.EQUAL)
        self.rule_complemented(ind, curr_concept)

    def solve_sugeno_integral_assertion(
        self, ind: Individual, concept: typing.Union[SugenoIntegral, QsugenoIntegral]
    ) -> None:
        """
        Encodes the mathematical definition of a Sugeno Integral or Quantified Sugeno Integral into the underlying Mixed-Integer Linear Programming (MILP) model to determine the degree of truth for a specific individual. It recursively processes the sub-concepts comprising the integral, establishing their degrees and corresponding MILP variables, and then constructs auxiliary variables and constraints to simulate the fuzzy logic operations required for the calculation. The method handles the sorting of sub-concept values, aligns them with the integral's weights, computes the minimum between each value and the cumulative weight, and finally determines the maximum of these minima to set the degree of the integral concept. Depending on the specific type of integral provided, it utilizes either Zadeh or Lukasiewicz logic for the intermediate aggregation steps, thereby modifying the MILP model state without returning a direct value.

        :param ind: The individual entity for which the Sugeno integral assertion is being evaluated and solved.
        :type ind: Individual
        :param concept: The Sugeno integral or Q-Sugeno integral concept assertion to be solved, containing the sub-concepts and weights necessary for the calculation.
        :type concept: typing.Union[SugenoIntegral, QsugenoIntegral]
        """

        # New n variables x_i
        n: int = len(concept.concepts)
        x: list[Variable] = []
        for i in range(n):
            ci: Concept = concept.concepts[i]
            x.append(self.milp.get_variable(ind, ci))
            self.add_assertion(ind, ci, DegreeVariable.get_degree(x[i]))

        # y1 > y2 > ... > yn
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
                # ow_j \geq (1 - z_{ij}) w_i
                self.milp.add_new_constraint(
                    Expression(
                        -concept.weights[k],
                        Term(concept.weights[k], z[k][i]),
                        Term(1.0, ow[i]),
                    ),
                    InequalityType.GREATER_THAN,
                )
                # ow_j \leq z_{ij} + w_i
                self.milp.add_new_constraint(
                    Expression(
                        -concept.weights[k], Term(-1.0, z[k][i]), Term(1.0, ow[i])
                    ),
                    InequalityType.LESS_THAN,
                )

        a: list[Variable] = [
            self.milp.get_new_variable(VariableType.SEMI_CONTINUOUS) for _ in range(n)
        ]
        # a_1 = ow_1
        self.milp.add_new_constraint(
            Expression(Term(1.0, a[0]), Term(-1.0, ow[0])), InequalityType.EQUAL
        )

        # a_i = ow_i \oplus a_{i-1}
        for m in range(1, n):
            vx: list[Variable] = [ow[m], a[m - 1]]
            LukasiewiczSolver.or_equation(vx, a[m], self.milp)

        # New n variables c_i
        c: list[Variable] = [
            self.milp.get_new_variable(VariableType.SEMI_CONTINUOUS) for _ in range(n)
        ]

        if isinstance(concept, QsugenoIntegral):
            for i in range(n):
                # c_i = y_i \otimes a_i
                LukasiewiczSolver.and_equation(c[i], y[i], a[i], self.milp)
        elif isinstance(concept, SugenoIntegral):
            for i in range(n):
                # c_i = y_i \otimes a_i
                ZadehSolver.and_equation(c[i], y[i], a[i], self.milp)

        # if bi = 0, then ci >= x_{ind:SI}
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

        # \sum bi = n-1
        exp: Expression = Expression()
        for i in range(n):
            exp.add_term(Term(1.0, b[i]))
        self.milp.add_new_constraint(exp, InequalityType.EQUAL, n - 1)

    def solve_sugeno_integral_complemented_assertion(
        self, ind: Individual, curr_concept: OperatorConcept
    ) -> None:
        """
        This method encodes the logic for a complemented Sugeno integral concept assertion into a Mixed-Integer Linear Programming (MILP) model for a specific individual. It first validates that the concept is a Sugeno or Quantified Sugeno integral and recursively adds assertions for the negated sub-concepts to the model. The method then constructs the MILP formulation for the integral by creating variables for the ordered permutation of the sub-concept degrees and calculating the ordered weights. It computes the intermediate terms of the integral—representing the conjunction of sorted inputs and accumulated weights—using either Zadeh or Lukasiewicz logic depending on the specific integral type. Finally, it introduces binary variables and constraints to link the degree of the complemented concept to the maximum term of the integral calculation, effectively modeling the negation of the Sugeno integral value, and invokes the general rule for complemented assertions.

        :param ind: The individual entity for which the complemented Sugeno integral assertion is being evaluated and solved.
        :type ind: Individual
        :param curr_concept: The complemented Sugeno integral concept assertion to be solved, containing a SugenoIntegral or QsugenoIntegral atom.
        :type curr_concept: OperatorConcept
        """

        assert isinstance(curr_concept.get_atom(), (SugenoIntegral, QsugenoIntegral))
        concept: typing.Union[SugenoIntegral, QsugenoIntegral] = curr_concept.get_atom()

        #  New n variables x_i
        n: int = len(concept.concepts)
        x: list[Variable] = []
        for i in range(n):
            ci: Concept = concept.concepts[i]
            not_ci: Concept = -ci
            x.append(self.milp.get_variable(ind, ci))
            x_not_i: Variable = self.milp.get_variable(ind, not_ci)
            self.add_assertion(ind, not_ci, DegreeVariable.get_degree(x_not_i))

        # y1 > y2 > ... > yn
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
                # ow_j \geq (1 - z_{ij}) w_i
                self.milp.add_new_constraint(
                    Expression(
                        -concept.weights[k],
                        Term(concept.weights[k], z[k][i]),
                        Term(1.0, ow[i]),
                    ),
                    InequalityType.GREATER_THAN,
                )
                # ow_j \leq z_{ij} + w_i
                self.milp.add_new_constraint(
                    Expression(
                        -concept.weights[k], Term(-1.0, z[k][i]), Term(1.0, ow[i])
                    ),
                    InequalityType.LESS_THAN,
                )

        a: list[Variable] = [
            self.milp.get_new_variable(VariableType.SEMI_CONTINUOUS) for _ in range(n)
        ]
        # a_1 = ow_1
        self.milp.add_new_constraint(
            Expression(Term(1.0, a[0]), Term(-1.0, ow[0])), InequalityType.EQUAL
        )
        # a_i = ow_i \oplus a_{i-1}
        for m in range(1, n):
            vx: list[Variable] = [ow[m], a[m - 1]]
            LukasiewiczSolver.or_equation(vx, a[m], self.milp)

        # New n variables c_i
        c: list[Variable] = [
            self.milp.get_new_variable(VariableType.SEMI_CONTINUOUS) for _ in range(n)
        ]

        if isinstance(concept, QsugenoIntegral):
            for i in range(n):
                # c_i = y_i \otimes a_i
                LukasiewiczSolver.and_equation(c[i], y[i], a[i], self.milp)
        elif isinstance(concept, SugenoIntegral):
            for i in range(n):
                # c_i = y_i \otimes a_i
                ZadehSolver.and_equation(c[i], y[i], a[i], self.milp)

        # if bi = 0, then ci >= x_{ind:SI}
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

        # \sum bi = n-1
        exp: Expression = Expression()
        for i in range(n):
            exp.add_term(Term(1.0, b[i]))
        self.milp.add_new_constraint(exp, InequalityType.EQUAL, n - 1)
        self.rule_complemented(ind, curr_concept)

    def solve_w_max_assertion(
        self, ind: Individual, concept: WeightedMaxConcept
    ) -> None:
        """
        Encodes the constraints necessary to evaluate a weighted maximum concept assertion for a specific individual within the underlying Mixed-Integer Linear Programming (MILP) model. The method computes the membership degree as the maximum of the minimum values between each sub-concept's membership degree and its associated weight, effectively implementing the logic $\max_i \min(\mu_{C_i}(ind), w_i)$. It recursively ensures that all constituent sub-concepts are asserted and resolved before introducing auxiliary variables and logical constraints to represent the aggregation.

        :param ind: The individual entity for which the weighted max concept assertion is being solved.
        :type ind: Individual
        :param concept: The weighted max concept assertion defining the sub-concepts and weights to be evaluated for the individual.
        :type concept: fuzzy_dl_owl2.fuzzydl.concept.weighted_max_concept.WeightedMaxConcept
        """

        x_A_in_WS: Variable = self.milp.get_variable(ind, concept)
        # min_i = \min \{ w_{i}, x_i \}
        min_vars: list[Variable] = []
        for ci, weight in zip(concept.concepts, concept.weights):
            xi: Variable = self.milp.get_variable(ind, ci)
            self.add_assertion(ind, ci, DegreeVariable.get_degree(xi))
            min_var: Variable = self.milp.get_new_variable(VariableType.SEMI_CONTINUOUS)
            ZadehSolver.and_equation(min_var, xi, weight, self.milp)
            min_vars.append(min_var)
        # max of the min_i = x:
        ZadehSolver.or_equation(min_vars, x_A_in_WS, self.milp)

    def solve_w_max_complemented_assertion(
        self, ind: Individual, curr_concept: OperatorConcept
    ) -> None:
        """
        Translates a complemented weighted max concept assertion into a series of constraints within the underlying Mixed-Integer Linear Programming (MILP) model for a specific individual. It iterates over the sub-concepts and weights associated with the input concept, calculating intermediate values that represent the maximum of the weight and the negated membership degree of each sub-concept. These intermediate values are then combined using a logical AND operation to determine the final truth value of the assertion. The method modifies the MILP model by adding new variables and constraints, recursively processes the negations of the sub-concepts, and triggers a specific rule for complemented assertions.

        :param ind: The individual for which the complemented weighted max concept assertion is being solved.
        :type ind: Individual
        :param curr_concept: The complemented weighted max concept assertion to be solved, containing the sub-concepts and weights needed to construct the MILP constraints.
        :type curr_concept: OperatorConcept
        """

        assert isinstance(curr_concept.get_atom(), WeightedMaxConcept)
        concept: WeightedMaxConcept = curr_concept.get_atom()

        x_A_in_WS: Variable = self.milp.get_variable(ind, curr_concept)
        # negmin_i = \max \{ w_{i}, 1 - x_i \}
        negmin: list[Variable] = []
        for ci, weight in zip(concept.concepts, concept.weights):
            not_ci: Concept = -ci
            xi: Variable = self.milp.get_variable(ind, ci)
            x_not_i: Variable = self.milp.get_variable(ind, not_ci)
            self.add_assertion(ind, not_ci, DegreeVariable.get_degree(x_not_i))
            max_var: Variable = self.milp.get_new_variable(VariableType.SEMI_CONTINUOUS)
            ZadehSolver.or_negated_equation(max_var, xi, 1.0 - weight, self.milp)
            negmin.append(max_var)
        # min of the negmax_i = x:
        ZadehSolver.and_equation(negmin, x_A_in_WS, self.milp)
        self.rule_complemented(ind, curr_concept)

    def solve_w_min_assertion(
        self, ind: Individual, concept: WeightedMinConcept
    ) -> None:
        """
        This method translates a weighted minimum concept assertion into a set of constraints within the underlying Mixed-Integer Linear Programming (MILP) model. It calculates the degree of membership for the given individual by determining the minimum value across a series of intermediate calculations, where each intermediate value represents the maximum of the sub-concept's degree and the complement of its associated weight. The process involves creating new auxiliary variables for the MILP solver and recursively ensuring that all nested sub-concepts are properly asserted before establishing the final logical constraints.

        :param ind: The individual entity for which the weighted min concept assertion is being evaluated and solved.
        :type ind: Individual
        :param concept: The weighted minimum concept structure containing the sub-concepts and weights required to formulate the assertion constraints.
        :type concept: fuzzy_dl_owl2.fuzzydl.concept.weighted_min_concept.WeightedMinConcept
        """

        x_A_in_WS: Variable = self.milp.get_variable(ind, concept)
        # max_i = \max \{ 1 - w_{i}, x_i \}
        max_vars: list[Variable] = []
        for ci, weight in zip(concept.concepts, concept.weights):
            xi: Variable = self.milp.get_variable(ind, ci)
            self.add_assertion(ind, ci, DegreeVariable.get_degree(xi))
            max_var: Variable = self.milp.get_new_variable(VariableType.SEMI_CONTINUOUS)
            ZadehSolver.or_equation(max_var, xi, 1.0 - weight, self.milp)
            max_vars.append(max_var)
        # min of the max_i = x:
        ZadehSolver.and_equation(max_vars, x_A_in_WS, self.milp)

    def solve_w_min_complemented_assertion(
        self, ind: Individual, curr_concept: OperatorConcept
    ) -> None:
        """
        Translates a complemented weighted minimum concept assertion into a series of constraints within the Mixed-Integer Linear Programming (MILP) model for a specified individual. It recursively processes the negation of each sub-concept involved in the weighted minimum, establishing auxiliary variables to represent the minimum value between each weight and the degree of the negated sub-concept. These intermediate values are then combined using a logical OR (maximum) operation to define the final variable representing the complemented assertion. This process modifies the MILP model by adding new variables and equations, and it triggers a rule application specific to complemented concepts.

        :param ind: The individual entity for which the assertion is being solved.
        :type ind: Individual
        :param curr_concept: The operator concept representing the complemented weighted min assertion to be solved.
        :type curr_concept: OperatorConcept
        """

        assert isinstance(curr_concept.get_atom(), WeightedMinConcept)
        concept: WeightedMinConcept = curr_concept.get_atom()

        x_A_in_WS: Variable = self.milp.get_variable(ind, curr_concept)
        # negmax_i = \min \{ w_{i}, 1 - x_i \}
        negmax: list[Variable] = []
        for ci, weight in zip(concept.concepts, concept.weights):
            not_ci: Concept = -ci
            xi: Variable = self.milp.get_variable(ind, ci)
            x_not_i: Variable = self.milp.get_variable(ind, not_ci)
            self.add_assertion(ind, not_ci, DegreeVariable.get_degree(x_not_i))
            max_var: Variable = self.milp.get_new_variable(VariableType.SEMI_CONTINUOUS)
            ZadehSolver.and_negated_equation(max_var, xi, weight, self.milp)
            negmax.append(max_var)
        # max of the negmax_i = x:
        ZadehSolver.or_equation(negmax, x_A_in_WS, self.milp)
        self.rule_complemented(ind, curr_concept)

    def solve_w_sum_assertion(
        self, ind: Individual, concept: WeightedSumConcept
    ) -> None:
        """
        This method enforces the logic of a weighted sum concept for a specific individual by integrating the necessary constraints into the MILP model. It processes the component concepts and their associated weights, ensuring that assertions for these sub-concepts are recursively added to the knowledge base. The core operation involves creating a linear equality constraint that equates the degree of the individual's membership in the weighted sum concept to the sum of the weighted degrees of membership in its constituent concepts.

        :param ind: The specific individual for which the weighted sum concept assertion is being solved.
        :type ind: Individual
        :param concept: The weighted sum concept assertion defining the component concepts and their corresponding weights to be enforced as a linear constraint.
        :type concept: fuzzy_dl_owl2.fuzzydl.concept.weighted_sum_concept.WeightedSumConcept
        """

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
        """
        Resolves the assertion for a complemented weighted sum concept associated with a specific individual by translating the logical relationship into a linear constraint within the MILP model. The method constructs an expression equating the degree of the complemented concept to one minus the weighted sum of the degrees of the constituent sub-concepts. Additionally, it recursively asserts the negations of the sub-concepts to ensure their values are defined before applying the specific complemented rule logic to finalize the state.

        :param ind: The individual entity for which the complemented weighted sum assertion is being solved.
        :type ind: Individual
        :param curr_concept: The complemented weighted sum concept assertion to be solved.
        :type curr_concept: OperatorConcept
        """

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
        """
        Encodes the logical constraints for a WeightedSumZeroConcept assertion applied to a specific Individual into the underlying Mixed-Integer Linear Programming (MILP) model. The method recursively processes the sub-concepts and their associated weights, ensuring that assertions for these sub-concepts are added to the model. It introduces auxiliary binary and semi-continuous variables to construct a set of linear constraints that approximate the fuzzy logic rule, specifically linking the truth value of the assertion to the weighted sum of its components while enforcing a dependency on the minimum truth value of those components. Finally, the method updates the solver state with these constraints and marks the rule as complemented.

        :param ind: The individual entity for which the weighted sum zero concept assertion is being solved.
        :type ind: Individual
        :param concept: The assertion defining the weighted sum zero condition, including the constituent concepts and their respective weights.
        :type concept: fuzzy_dl_owl2.fuzzydl.concept.weighted_sum_zero_concept.WeightedSumZeroConcept
        """

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
        # z = min { x_{v:C_i} }   for all i
        ZadehSolver.and_equation(vx, z, self.milp)
        # y = not_G z
        ZadehSolver.goedel_not_equation(y, z, self.milp)
        # xAinWS \leq  1-y
        self.milp.add_new_constraint(
            Expression(-1.0, Term(1.0, y), Term(1.0, x_A_in_ws)),
            InequalityType.LESS_THAN,
        )

        # xAinWS \geq  w_1 x_{v:C_1} + \dots + w_n x_{v:C_n} - y
        exp1: Expression = Expression(*terms)
        exp1.add_term(Term(-1.0, y))
        self.milp.add_new_constraint(exp1, InequalityType.LESS_THAN)

        # xAinWS \leq  w_1 x_{v:C_1} + \dots + w_n x_{v:C_n} + y
        exp2: Expression = Expression(*terms)
        exp2.add_term(Term(1.0, y))
        self.milp.add_new_constraint(exp2, InequalityType.GREATER_THAN)

        self.rule_complemented(ind, concept)

    def solve_w_sum_zero_complemented_assertion(
        self, ind: Individual, curr_concept: OperatorConcept
    ) -> None:
        """
        This method encodes the logical constraints for a complemented weighted sum zero concept assertion into the underlying MILP model for a specific individual. It recursively ensures that the negations of the component concepts are asserted and introduces auxiliary variables to model the logical relationships, specifically handling the minimum membership degree and its negation. The method adds linear constraints to the solver to define the truth value of the assertion based on the weighted sum of the component variables, effectively implementing the logic for the complemented operator. As a side effect, it modifies the MILP model by adding new variables and constraints and invokes the rule handling logic for complemented concepts.

        :param ind: The individual for which the complemented weighted sum zero assertion is being solved.
        :type ind: Individual
        :param curr_concept: The complemented weighted sum zero concept assertion to be resolved into MILP constraints.
        :type curr_concept: OperatorConcept
        """

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
        # z = min { x_{v:C_i} }   for all i
        ZadehSolver.and_equation(vx, z, self.milp)
        # y = not_G z
        ZadehSolver.goedel_not_equation(y, z, self.milp)
        # xAinNotWS \geq y
        self.milp.add_new_constraint(
            Expression(Term(-1.0, y), Term(1.0, x_A_in_not_ws)),
            InequalityType.GREATER_THAN,
        )
        # xAinNotWS \geq  1 - (w_1 x_{v:C_1} + \dots + w_n x_{v:C_n}) - y
        exp1: Expression = Expression(*terms)
        exp1.add_term(Term(-1.0, y))
        self.milp.add_new_constraint(exp1, InequalityType.LESS_THAN)

        # xAinNotWS \leq  1 - (w_1 x_{v:C_1} + \dots + w_n x_{v:C_n}) + y
        exp2: Expression = Expression(*terms)
        exp2.add_term(Term(1.0, y))
        self.milp.add_new_constraint(exp2, InequalityType.GREATER_THAN)

        self.rule_complemented(ind, curr_concept)

    def __add_fuzzy_concrete_concept_equation(
        self, concept: FuzzyConcreteConcept, x_c: Variable, x_ass: Variable
    ) -> None:
        """
        Dispatches the creation of mathematical equations for a fuzzy concrete concept by delegating to specialized handlers based on the concept's specific type. The method evaluates the provided `concept` against known subclasses—such as CrispConcreteConcept, LinearConcreteConcept, TriangularConcreteConcept, and TrapezoidalConcreteConcept—and invokes the corresponding private method to establish the relationship between the concept variable `x_c` and the assertion variable `x_ass`. This ensures that the specific shape and membership logic of the fuzzy concept are correctly integrated into the knowledge base. If the concept type does not match any of the expected implementations, a ValueError is raised.

        :param concept: The fuzzy concrete concept instance for which the equation is being added, determining the specific mathematical formulation based on its subclass type.
        :type concept: FuzzyConcreteConcept
        :param x_c: Symbolic variable representing the fuzzy concrete concept in the equation.
        :type x_c: Variable
        :param x_ass: The variable associated with the assertion.
        :type x_ass: Variable

        :raises ValueError: Raised if the provided concept is not one of the supported specific types (Crisp, Linear, Left, Right, Triangular, or Trapezoidal).
        """

        if isinstance(concept, CrispConcreteConcept):
            self.__add_crisp_concrete_concept_equations(concept, x_c, x_ass)
        if isinstance(concept, LinearConcreteConcept):
            self.__add_linear_concrete_concept_equations(concept, x_c, x_ass)
        if isinstance(concept, LeftConcreteConcept):
            self.__add_left_concrete_concept_equations(concept, x_c, x_ass)
        if isinstance(concept, RightConcreteConcept):
            self.__add_right_concrete_concept_equations(concept, x_c, x_ass)
        if isinstance(concept, TriangularConcreteConcept):
            self.__add_triangular_concrete_concept_equations(concept, x_c, x_ass)
        if isinstance(concept, TrapezoidalConcreteConcept):
            self.__add_trapezoidal_concrete_concept_equations(concept, x_c, x_ass)
        raise ValueError

    def solve_crisp_concrete_concept_assertion(
        self, ind: Individual, concept: CrispConcreteConcept
    ) -> None:
        """
        Generates and applies the linear constraints to the internal Mixed Integer Linear Programming (MILP) model necessary to represent the assertion that a specific individual belongs to a crisp concrete concept. The method retrieves the variable associated with the individual and the binary variable representing the concept membership, then invokes an internal helper to encode the specific mathematical relationships defining the crisp set boundaries. This process modifies the state of the MILP model by adding new equations, and it assumes that the required variables have already been initialized within the solver.

        :param ind: The individual entity for which the crisp concrete concept assertion constraints are being defined.
        :type ind: Individual
        :param concept: The crisp concrete concept defining the assertion constraints and parameters.
        :type concept: CrispConcreteConcept
        """

        x_c: Variable = self.milp.get_variable(ind)
        x_ass: Variable = self.milp.get_variable(ind, concept)
        self.__add_crisp_concrete_concept_equations(concept, x_c, x_ass)

    def __add_crisp_concrete_concept_equations(
        self, concept: CrispConcreteConcept, x_c: Variable, x_ass: Variable
    ) -> None:
        """
        Encodes the logical constraints for a crisp concrete concept into the underlying Mixed-Integer Linear Programming (MILP) model by establishing a relationship between the concept's value and its assertion status. This method introduces three auxiliary binary variables to partition the solution space into three mutually exclusive regions based on the concept variable `x_c`: a lower region where `x_c` is strictly less than the lower threshold `a`, a middle region where `x_c` lies between `a` and `b`, and an upper region where `x_c` is strictly greater than the upper threshold `b`. The assertion variable `x_ass` is constrained to be 1 only when `x_c` falls within the middle region `[a, b]`, and 0 otherwise. The formulation utilizes the concept's global bounds `k1` and `k2` to deactivate irrelevant constraints via a Big-M approach and employs a small epsilon value to strictly enforce inequalities at the boundaries. As a side effect, this method modifies the MILP model by adding the new binary variables and the necessary linear constraints.

        :param concept: The crisp concrete concept definition providing the threshold values (k1, a, b, k2) required to formulate the piecewise linear constraints.
        :type concept: CrispConcreteConcept
        :param x_c: The decision variable representing the value of the concept, used to enforce constraints based on the concept's thresholds.
        :type x_c: Variable
        :param x_ass: The variable representing the assertion of the concept, constrained to 1 if the concept variable falls within the assertion interval and 0 otherwise.
        :type x_ass: Variable
        """

        y1: Variable = self.milp.get_new_variable(VariableType.BINARY)
        y2: Variable = self.milp.get_new_variable(VariableType.BINARY)
        y3: Variable = self.milp.get_new_variable(VariableType.BINARY)

        # y1 + y2 + y3 = 1
        self.milp.add_new_constraint(
            Expression(Term(1.0, y1), Term(1.0, y2), Term(1.0, y3)),
            InequalityType.EQUAL,
            1.0,
        )
        # IF y1 = 1
        #   xC < a
        #   xC \geq k1
        #   xAss = 0
        #
        # IF y2 = 1
        #   xC \leq a
        #   xC \geq b
        #   xAss = 1
        #
        # IF y3 = 1
        #   xC > k2
        #   xC \geq b
        #   xAss = 0

        # x_c + (k_1 - a) y_2 \geq k_1
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_c), Term(concept.k1 - concept.a, y2)),
            InequalityType.GREATER_THAN,
            concept.k1,
        )
        # x_c + (k_1 - b - Epsilon) y_3 \geq k_1
        self.milp.add_new_constraint(
            Expression(
                Term(1.0, x_c), Term(concept.k1 - concept.b - ConfigReader.EPSILON, y3)
            ),
            InequalityType.GREATER_THAN,
            concept.k1,
        )
        # x_c + (k_2 - a + Epsilon) y_1 \leq k_2
        self.milp.add_new_constraint(
            Expression(
                Term(1.0, x_c), Term(concept.k2 - concept.a + ConfigReader.EPSILON, y1)
            ),
            InequalityType.LESS_THAN,
            concept.k2,
        )
        # x_c + (k_2 - b) y_2 \leq k_2
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_c), Term(concept.k2 - concept.b, y2)),
            InequalityType.LESS_THAN,
            concept.k2,
        )
        # xAss \leq 1 - y_1 - y_3
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_ass), Term(1.0, y1), Term(1.0, y3)),
            InequalityType.LESS_THAN,
            1.0,
        )
        # xAss \geq y_2
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_ass), Term(-1.0, y2)), InequalityType.GREATER_THAN
        )

    def solve_fuzzy_concrete_concept_complement_assertion(
        self,
        ind: CreatedIndividual,
        lower_limit: Degree,
        curr_concept: OperatorConcept,
    ) -> None:
        """
        Processes a complement assertion for a fuzzy concrete concept by validating the input and delegating to the rule engine. The method ensures that the atom of the provided operator concept is an instance of `FuzzyConcreteConcept` before constructing an `Assertion` object that links the individual, the concept, and the specified lower degree limit. Once the assertion is created, it invokes `rule_complemented_complex_assertion` to handle the logical implications, thereby potentially modifying the state of the knowledge base without returning a value.

        :param ind: The individual instance serving as the subject of the assertion.
        :type ind: CreatedIndividual
        :param lower_limit: The degree value representing the lower limit for the assertion.
        :type lower_limit: Degree
        :param curr_concept: The fuzzy concrete concept involved in the assertion, wrapped as an OperatorConcept.
        :type curr_concept: OperatorConcept
        """

        assert isinstance(curr_concept.get_atom(), FuzzyConcreteConcept)
        assertion: Assertion = Assertion(ind, curr_concept, lower_limit)
        self.rule_complemented_complex_assertion(assertion)

    def solve_left_concrete_concept_assertion(
        self, ind: CreatedIndividual, concept: LeftConcreteConcept
    ) -> None:
        """
        Encodes a left concrete concept assertion for a specific individual into the underlying Mixed-Integer Linear Programming (MILP) model. The method retrieves the decision variables associated with the individual and the assertion, then generates and adds the necessary linear equations to enforce the concept's semantics. This process modifies the internal MILP model in place and does not return a value.

        :param ind: The individual for which the assertion is being solved.
        :type ind: CreatedIndividual
        :param concept:
        :type concept: LeftConcreteConcept
        """

        x_c: Variable = self.milp.get_variable(ind)
        x_ass: Variable = self.milp.get_variable(ind, concept)
        self.__add_left_concrete_concept_equations(concept, x_c, x_ass)

    def __add_left_concrete_concept_equations(
        self, concept: LeftConcreteConcept, x_c: Variable, x_ass: Variable
    ) -> None:
        """
        Encodes the logical constraints for a left concrete concept assertion into the underlying Mixed-Integer Linear Programming (MILP) model by introducing auxiliary binary variables and linear inequalities. It establishes a piecewise relationship between the concrete concept variable and the assertion variable, defining three mutually exclusive regimes: one where the assertion is definitively true, one where it is definitively false, and a transitional region where the assertion value is interpolated. The method adds these constraints to the model to ensure that the assertion variable accurately reflects the state of the concrete concept based on the thresholds and bounds specified in the concept definition.

        :param concept: The left concrete concept assertion providing the parameters (a, b, k1, k2) required to formulate the MILP constraints.
        :type concept: LeftConcreteConcept
        :param x_c: The variable representing the value of the concrete concept.
        :type x_c: Variable
        :param x_ass: The variable representing the truth value of the assertion.
        :type x_ass: Variable
        """

        # y1 + y2 + y3 = 1
        y1: Variable = self.milp.get_new_variable(VariableType.BINARY)
        y2: Variable = self.milp.get_new_variable(VariableType.BINARY)
        y3: Variable = self.milp.get_new_variable(VariableType.BINARY)
        self.milp.add_new_constraint(
            Expression(Term(1.0, y1), Term(1.0, y2), Term(1.0, y3)),
            InequalityType.EQUAL,
            1.0,
        )
        # IF y1 = 1
        #   xC \leq a
        #   xC \geq k1
        #   xAss = 1
        #
        # IF y2 = 1
        #   xC \leq b
        #   xC \geq a
        #   xC = (a-b)xAss + b
        #
        # IF y3 = 1
        #   xC \leq k2
        #   xC \geq b
        #   xAss = 0

        # x_c + (k_1 - a) y_2 \geq k_1
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_c), Term(concept.k1 - concept.a, y2)),
            InequalityType.GREATER_THAN,
            concept.k1,
        )
        # x_c + (k_1 - b) y_3 \geq k_1
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_c), Term(concept.k1 - concept.b, y3)),
            InequalityType.GREATER_THAN,
            concept.k1,
        )
        # x_c + (k_2 - a) y_1 \leq k_2
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_c), Term(concept.k2 - concept.a, y1)),
            InequalityType.LESS_THAN,
            concept.k2,
        )
        # x_c + (k_2 - b) y_2 \leq k_2
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_c), Term(concept.k2 - concept.b, y2)),
            InequalityType.LESS_THAN,
            concept.k2,
        )
        # xAss \leq 1 - y_3
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_ass), Term(1.0, y3)), InequalityType.LESS_THAN, 1.0
        )
        # xAss \geq y_1
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_ass), Term(-1.0, y1)), InequalityType.GREATER_THAN
        )
        # xC + (b-a) xAss + (k2 - a) y2  \leq k2 + b - a
        self.milp.add_new_constraint(
            Expression(
                Term(1.0, x_c),
                Term(concept.b - concept.a, x_ass),
                Term(concept.k2 - concept.a, y2),
            ),
            InequalityType.LESS_THAN,
            concept.k2 + concept.b - concept.a,
        )
        # xC + (b-a) xAss + (k1 - b) y2 \geq k1
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
        """
        Encodes a linear concrete concept assertion for a specified individual into the internal Mixed-Integer Linear Programming (MILP) model. It retrieves the decision variables associated with the individual and the specific assertion, then invokes a helper method to generate and append the corresponding linear constraints. This process modifies the MILP model in place to reflect the logical relationship defined by the concept, ensuring that any subsequent solution satisfies the assertion.

        :param ind: The individual entity for which the linear concrete concept assertion is being solved.
        :type ind: CreatedIndividual
        :param concept: The linear concrete concept assertion to be evaluated and enforced for the individual.
        :type concept: LinearConcreteConcept
        """

        x_A_is_C: Variable = self.milp.get_variable(ind)
        x_ass: Variable = self.milp.get_variable(ind, concept)
        self.__add_linear_concrete_concept_equations(concept, x_A_is_C, x_ass)

    def __add_linear_concrete_concept_equations(
        self, concept: LinearConcreteConcept, x_A_is_C: Variable, x_ass: Variable
    ) -> None:
        """
        Encodes the logical constraints for a linear concrete concept assertion into the underlying Mixed-Integer Linear Programming (MILP) model. This method introduces an auxiliary binary variable to handle the disjunctive conditions defined by the concept's threshold `a` and boundaries `k1` and `k2`. It establishes a system of six linear inequalities that link the concrete domain variable `x_A_is_C` with the assertion variable `x_ass`, ensuring that the assertion's value is consistent with the linear relationship defined by the concept's slope `b` and intercepts. The constraints effectively model the piecewise logic where the concrete value falls either below or above the threshold, thereby determining the state of the assertion variable.

        :param concept: The linear concrete concept assertion providing the coefficients and thresholds necessary to formulate the MILP constraints.
        :type concept: LinearConcreteConcept
        :param x_A_is_C: The MILP variable representing the value of the concrete concept.
        :type x_A_is_C: Variable
        :param x_ass: The variable representing the assertion's truth value.
        :type x_ass: Variable
        """

        y: Variable = self.milp.get_variable(VariableType.BINARY)
        # if y=0:		xc <= a,		b xc  - (a - k1) xass  = b k1
        # if y=1:		xc >= a,		(1 - b) xc -  (k2 - a) xass =  a - b k2

        # xc + (a - k2) y <= a
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_A_is_C), Term(concept.a - concept.k2, y)),
            InequalityType.LESS_THAN,
            concept.a,
        )
        # xc + (k1-a)y  >= k1
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_A_is_C), Term(concept.k1 - concept.a, y)),
            InequalityType.GREATER_THAN,
            concept.k1,
        )
        # b xc  - (a - k1) xass + (a - k1) y >=  b k1
        self.milp.add_new_constraint(
            Expression(
                Term(concept.k1 - concept.a, x_ass),
                Term(concept.a - concept.k1, y),
                Term(concept.b, x_A_is_C),
            ),
            InequalityType.GREATER_THAN,
            concept.b * concept.k1,
        )
        # b xc  - (a - k1) xass - b (k2 - k1) y <=  b k1
        self.milp.add_new_constraint(
            Expression(
                Term(concept.k1 - concept.a, x_ass),
                Term(concept.b * (concept.k1 - concept.k2), y),
                Term(concept.b, x_A_is_C),
            ),
            InequalityType.LESS_THAN,
            concept.b * concept.k1,
        )
        # (1-b) xc - (k2 - a) xass - (1-b)(k2 - k1) y >=  a - k2 - k1 b + k1
        self.milp.add_new_constraint(
            Expression(
                Term(concept.a - concept.k2, x_ass),
                Term((1.0 - concept.b) * (concept.k1 - concept.k2), y),
                Term(1.0 - concept.b, x_A_is_C),
            ),
            InequalityType.GREATER_THAN,
            concept.a - concept.k2 - concept.k1 * concept.b + concept.k1,
        )
        # (1-b) xc - (k2 - a) xass  - (a - k2) y  <= k2 - b k2
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
        """
        This method integrates a right concrete concept assertion into the underlying Mixed-Integer Linear Programming (MILP) model for a specific individual. It retrieves the decision variables corresponding to the individual and the assertion from the MILP solver, then delegates the generation of the necessary mathematical constraints to a helper method. By adding these equations, the method ensures that the assertion is mathematically represented within the optimization problem, thereby modifying the solver's state without returning a value.

        :param ind: The individual instance subject to the right concrete concept assertion.
        :type ind: CreatedIndividual
        :param concept: The assertion to be solved for the individual.
        :type concept: RightConcreteConcept
        """

        x_c: Variable = self.milp.get_variable(ind)
        x_ass: Variable = self.milp.get_variable(ind, concept)
        self.__add_right_concrete_concept_equations(concept, x_c, x_ass)

    def __add_right_concrete_concept_equations(
        self, concept: RightConcreteConcept, x_c: Variable, x_ass: Variable
    ) -> None:
        """
        This method encodes the logical constraints for a right concrete concept assertion into the underlying Mixed-Integer Linear Programming (MILP) model. It establishes a relationship between a concrete concept variable and an assertion variable based on thresholds defined in the provided concept object. To model this piecewise logic, the method introduces three auxiliary binary variables that act as mutually exclusive switches, enforcing exactly one of three distinct operational regimes. These regimes define specific bounds on the concept variable and determine the value of the assertion variable, effectively creating a conditional mapping where the assertion is forced to zero in the lower region, one in the upper region, and follows a linear interpolation in the transition region. The primary side effect is the addition of these new variables and their associated linear constraints to the MILP solver.

        :param concept: The right concrete concept assertion defining the thresholds and logic used to construct the constraints linking the concept variable to the assertion variable.
        :type concept: RightConcreteConcept
        :param x_c: The decision variable representing the value of the concrete concept.
        :type x_c: Variable
        :param x_ass: The decision variable representing the assertion, used to model the truth value of the right concrete concept within the MILP constraints.
        :type x_ass: Variable
        """

        y1: Variable = self.milp.get_new_variable(VariableType.BINARY)
        y2: Variable = self.milp.get_new_variable(VariableType.BINARY)
        y3: Variable = self.milp.get_new_variable(VariableType.BINARY)

        # y1 + y2 + y3 = 1
        self.milp.add_new_constraint(
            Expression(Term(1.0, y1), Term(1.0, y2), Term(1.0, y3)),
            InequalityType.EQUAL,
            1.0,
        )

        #  IF y1 = 1
        #    xC \leq a
        #    xC \geq k1
        #    xAss = 0
        #
        #  IF y2 = 1
        #    xC \leq b
        #    xC \geq a
        #    xC = (b-a)xAss + a
        #
        #  IF y3 = 1
        #    xC \leq k2
        #    xC \geq b
        #    xAss = 1

        # x_c + (k_1 - a) y_2 \geq k_1
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_c), Term(concept.k1 - concept.a, y2)),
            InequalityType.GREATER_THAN,
            concept.k1,
        )
        # x_c + (k_1 - b) y_3 \geq k_1
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_c), Term(concept.k1 - concept.b, y3)),
            InequalityType.GREATER_THAN,
            concept.k1,
        )
        # x_c + (k_2 - a) y_1 \leq k_2
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_c), Term(concept.k2 - concept.a, y1)),
            InequalityType.LESS_THAN,
            concept.k2,
        )
        # x_c + (k_2 - b) y_2 \leq k_2
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_c), Term(concept.k2 - concept.b, y2)),
            InequalityType.LESS_THAN,
            concept.k2,
        )
        # xAss \leq 1 - y_1
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_ass), Term(1.0, y1)), InequalityType.LESS_THAN, 1.0
        )
        # xAss \geq y_3
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_ass), Term(-1.0, y3)), InequalityType.GREATER_THAN
        )
        # xC + (a-b) xAss + (k2 - a) y2 \leq k2
        self.milp.add_new_constraint(
            Expression(
                Term(1.0, x_c),
                Term(concept.a - concept.b, x_ass),
                Term(concept.k2 - concept.a, y2),
            ),
            InequalityType.LESS_THAN,
            concept.k2,
        )
        # xC + (a-b) xAss + (k1 - b) y2  \geq k1 + a - b
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
        """
        Formulates and adds the necessary constraints to the underlying Mixed-Integer Linear Programming (MILP) model to evaluate a trapezoidal concrete concept assertion for a specific individual. This method retrieves the variables associated with the individual and the assertion, then delegates to an internal helper to inject the trapezoidal membership equations. As a side effect, the MILP model is modified by the addition of these constraints, effectively encoding the fuzzy logic assertion into a solvable mathematical form.

        :param ind: The individual entity for which the trapezoidal concrete concept assertion is being solved.
        :type ind: CreatedIndividual
        :param concept: The trapezoidal concrete concept assertion defining the constraints to be added to the model.
        :type concept: TrapezoidalConcreteConcept
        """

        x_c: Variable = self.milp.get_variable(ind)
        x_ass: Variable = self.milp.get_variable(typing.cast(Individual, ind), concept)
        self.__add_trapezoidal_concrete_concept_equations(concept, x_c, x_ass)

    def __add_trapezoidal_concrete_concept_equations(
        self, concept: TrapezoidalConcreteConcept, x_c: Variable, x_ass: Variable
    ) -> None:
        """
        Encodes the relationship between a concrete variable and its assertion variable within the internal Mixed-Integer Linear Programming (MILP) model using a trapezoidal membership function. The method introduces five auxiliary binary variables to partition the domain into five distinct regions: the left tail, the rising slope, the core, the falling slope, and the right tail. By enforcing that exactly one binary variable is active, it applies specific linear constraints to set the assertion variable to 0 in the tails, 1 in the core, or a linear interpolation on the slopes, depending on the value of the concrete variable relative to the trapezoid's parameters. This process modifies the MILP model by adding the necessary variables and constraints.

        :param concept: The trapezoidal concrete concept assertion providing the parameters ($k_1, a, b, c, d, k_2$) used to construct the linear constraints.
        :type concept: TrapezoidalConcreteConcept
        :param x_c: The variable representing the value of the concrete concept within the mathematical model.
        :type x_c: Variable
        :param x_ass: The variable representing the truth value of the assertion, which corresponds to the degree of membership of the concrete concept.
        :type x_ass: Variable
        """

        y1: Variable = self.milp.get_new_variable(VariableType.BINARY)
        y2: Variable = self.milp.get_new_variable(VariableType.BINARY)
        y3: Variable = self.milp.get_new_variable(VariableType.BINARY)
        y4: Variable = self.milp.get_new_variable(VariableType.BINARY)
        y5: Variable = self.milp.get_new_variable(VariableType.BINARY)

        # y1 + y2 + y3 + y4 + y5 = 1
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

        # IF y1 = 1
        #   xC \leq a
        #   xC \geq k1
        #   xAss = 0
        #
        # IF y2 = 1
        #   xC \leq b
        #   xC \geq a
        #   xC = (b-a)xAss + a
        #
        # IF y3 = 1
        #   xC \leq c
        #   xC \geq b
        #   xAss = 1
        #
        # IF y4 = 1
        #   xC \leq d
        #   xC \geq c
        #   xC = (c-d)xAss + d
        #
        # IF y5 = 1
        #   xC \leq k2
        #   xC \geq d
        #   xAss = 0

        # x_c + (k_1 - a) y_2 \geq k_1
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_c), Term(concept.k1 - concept.a, y2)),
            InequalityType.GREATER_THAN,
            concept.k1,
        )
        # x_c + (k_1 - b) y_3 \geq k_1
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_c), Term(concept.k1 - concept.b, y3)),
            InequalityType.GREATER_THAN,
            concept.k1,
        )
        # x_c + (k_1 - c) y_4 \geq k_1
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_c), Term(concept.k1 - concept.c, y4)),
            InequalityType.GREATER_THAN,
            concept.k1,
        )
        # x_c + (k_1 - d) y_5 \geq k_1
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_c), Term(concept.k1 - concept.d, y5)),
            InequalityType.GREATER_THAN,
            concept.k1,
        )
        # x_c + (k_2 - a) y_1 \leq k_2
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_c), Term(concept.k2 - concept.a, y1)),
            InequalityType.LESS_THAN,
            concept.k2,
        )
        # x_c + (k_2 - b) y_2 \leq k_2
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_c), Term(concept.k2 - concept.b, y2)),
            InequalityType.LESS_THAN,
            concept.k2,
        )
        # x_c + (k_2 - c) y_3 \leq k_2
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_c), Term(concept.k2 - concept.c, y3)),
            InequalityType.LESS_THAN,
            concept.k2,
        )
        # x_c + (k_2 - d) y_4 \leq k_2
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_c), Term(concept.k2 - concept.d, y4)),
            InequalityType.LESS_THAN,
            concept.k2,
        )

        # xAss \leq 1 - y_1 - y_5
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_ass), Term(1.0, y1), Term(1.0, y5)),
            InequalityType.LESS_THAN,
            1.0,
        )
        # xAss \geq y_3
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_ass), Term(-1.0, y3)), InequalityType.GREATER_THAN
        )

        # xC + (a-b) xAss + (k2 - a) y2 \leq k2
        self.milp.add_new_constraint(
            Expression(
                Term(1.0, x_c),
                Term(concept.a - concept.b, x_ass),
                Term(concept.k2 - concept.a, y2),
            ),
            InequalityType.LESS_THAN,
            concept.k2,
        )
        # xC + (a-b) xAss + (k1 - b) y2  \geq k1 + a - b
        self.milp.add_new_constraint(
            Expression(
                Term(1.0, x_c),
                Term(concept.a - concept.b, x_ass),
                Term(concept.k1 - concept.b, y2),
            ),
            InequalityType.GREATER_THAN,
            concept.k1 + concept.a - concept.b,
        )
        # xC + (d-c) xAss + (k2 - c) y4  \leq k2 + d - c
        self.milp.add_new_constraint(
            Expression(
                Term(1.0, x_c),
                Term(concept.d - concept.c, x_ass),
                Term(concept.k2 - concept.c, y4),
            ),
            InequalityType.LESS_THAN,
            concept.k2 + concept.d - concept.c,
        )
        # xC + (d-c) xAss + (k1 - d) y4 \geq k1
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
        """
        This method encodes a triangular concrete concept assertion for a specified individual into the underlying Mixed-Integer Linear Programming (MILP) model. It retrieves the variables representing the individual and the specific assertion, then delegates to an internal helper to add the necessary linear equations defining the triangular constraints. As a side effect, this method mutates the MILP model by introducing these constraints, effectively enforcing the logical assertion within the optimization problem.

        :param individual: The subject of the triangular concrete concept assertion to be solved.
        :type individual: CreatedIndividual
        :param concept: The triangular concrete concept assertion defining the constraints to be applied to the individual.
        :type concept: TriangularConcreteConcept
        """

        x_c: Variable = self.milp.get_variable(individual)
        x_ass: Variable = self.milp.get_variable(
            typing.cast(Individual, individual), concept
        )
        self.__add_triangular_concrete_concept_equations(concept, x_c, x_ass)

    def __add_triangular_concrete_concept_equations(
        self, concept: TriangularConcreteConcept, x_c: Variable, x_ass: Variable
    ) -> None:
        """
        Encodes the logical constraints for a triangular concrete concept assertion into the underlying Mixed-Integer Linear Programming (MILP) model. This method creates four auxiliary binary variables to select the active segment of the triangular function, corresponding to the lower tail, rising edge, falling edge, and upper tail. It establishes a system of linear inequalities that relate the concrete variable `x_c` to the assertion variable `x_ass`, ensuring that `x_ass` accurately reflects the piecewise linear membership degree defined by the concept's parameters (k1, a, b, c, k2). The constraints enforce that the assertion is zero in the tail regions and scales linearly within the core region. As a side effect, this method modifies the MILP model by adding these new variables and constraints.

        :param concept: The triangular concrete concept assertion providing the parameters and boundaries used to construct the MILP constraints.
        :type concept: TriangularConcreteConcept
        :param x_c: The variable representing the value of the concrete concept.
        :type x_c: Variable
        :param x_ass: The variable representing the assertion value, which encodes the degree of membership or truth for the concrete concept.
        :type x_ass: Variable
        """

        y1: Variable = self.milp.get_new_variable(VariableType.BINARY)
        y2: Variable = self.milp.get_new_variable(VariableType.BINARY)
        y3: Variable = self.milp.get_new_variable(VariableType.BINARY)
        y4: Variable = self.milp.get_new_variable(VariableType.BINARY)

        # y1 + y2 + y3 + y4 = 1
        self.milp.add_new_constraint(
            Expression(Term(1.0, y1), Term(1.0, y2), Term(1.0, y3), Term(1.0, y4)),
            InequalityType.EQUAL,
            1.0,
        )
        # IF y1 = 1
        #     xC \leq a
        #     xC \geq k1
        #     xAss = 0
        #
        # IF y2 = 1
        #     xC \leq b
        #     xC \geq a
        #     xC = (b-a) xAss + a
        #
        # IF y3 = 1
        #     xC \leq c
        #     xC \geq b
        #     xC = (b-c) xAss + c
        #
        # IF y4 = 1
        #     xC \leq k2
        #     xC \geq c
        #     xAss = 0

        # x_c + (k_1 - a) y_2 \geq k_1
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_c), Term(concept.k1 - concept.a, y2)),
            InequalityType.GREATER_THAN,
            concept.k1,
        )
        # x_c + (k_1 - b) y_3 \geq k_1
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_c), Term(concept.k1 - concept.b, y3)),
            InequalityType.GREATER_THAN,
            concept.k1,
        )
        # x_c + (k_1 - c) y_4 \geq k_1
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_c), Term(concept.k1 - concept.c, y4)),
            InequalityType.GREATER_THAN,
            concept.k1,
        )
        # x_c + (k_2 - a) y_1 \leq k_2
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_c), Term(concept.k2 - concept.a, y1)),
            InequalityType.LESS_THAN,
            concept.k2,
        )
        # x_c + (k_2 - b) y_2 \leq k_2
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_c), Term(concept.k2 - concept.b, y2)),
            InequalityType.LESS_THAN,
            concept.k2,
        )
        # x_c + (k_2 - c) y_3 \leq k_2
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_c), Term(concept.k2 - concept.c, y3)),
            InequalityType.LESS_THAN,
            concept.k2,
        )
        # xAss \leq 1 - y_1 - y_4
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_ass), Term(1.0, y1), Term(1.0, y4)),
            InequalityType.LESS_THAN,
            1.0,
        )
        # xC + (a-b) xAss + (k2 - a) y2 \leq k2
        self.milp.add_new_constraint(
            Expression(
                Term(1.0, x_c),
                Term(concept.a - concept.b, x_ass),
                Term(concept.k2 - concept.a, y2),
            ),
            InequalityType.LESS_THAN,
            concept.k2,
        )
        # xC + (a-b) xAss + (k1 - b) y2  \geq k1 + a - b
        self.milp.add_new_constraint(
            Expression(
                Term(1.0, x_c),
                Term(concept.a - concept.b, x_ass),
                Term(concept.k1 - concept.b, y2),
            ),
            InequalityType.GREATER_THAN,
            concept.k1 + concept.a - concept.b,
        )
        # xC + (c-b) xAss + (k2 - b) y3  \leq k2 + c - b
        self.milp.add_new_constraint(
            Expression(
                Term(1.0, x_c),
                Term(concept.c - concept.b, x_ass),
                Term(concept.k2 - concept.b, y3),
            ),
            InequalityType.LESS_THAN,
            concept.k2 + concept.c - concept.b,
        )
        # xC + (c-b) xAss + (k1 - c) y3 \geq k1
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
        """
        Processes a complemented assertion involving a modified concept for a specific individual within the knowledge base. This method validates that the provided concept is an `OperatorConcept` wrapping a `ModifiedConcept` or `ModifiedConcreteConcept`, raising an error if the structure is invalid. It constructs an `Assertion` object from the individual, concept, and degree, and subsequently delegates the resolution logic to the `rule_complemented_complex_assertion` method to update the knowledge base state.

        :param ind: The individual entity serving as the subject of the complemented modifier assertion.
        :type ind: Individual
        :param concept: The complemented modifier assertion to be resolved.
        :type concept: OperatorConcept
        :param degree: The degree of truth associated with the assertion.
        :type degree: Degree
        """

        assert isinstance(concept, OperatorConcept) and isinstance(
            concept.get_atom(), (ModifiedConcept, ModifiedConcreteConcept)
        )
        ass: Assertion = Assertion(ind, concept, degree)
        self.rule_complemented_complex_assertion(ass)

    def solve_linear_modifier_assertion(
        self, ind: Individual, con: Concept, modifier: LinearModifier
    ) -> None:
        """
        Encodes the logical constraints of a linear modifier assertion into the underlying Mixed-Integer Linear Programming (MILP) model, establishing a mathematical relationship between the degree to which an individual belongs to a base concept and the degree to which it belongs to a modified version of that concept. The method handles both standard concepts and pre-modified concrete concepts, ensuring the base concept is asserted before applying the modifier logic. It introduces a binary variable to the MILP solver to model a piecewise linear constraint, ensuring that the truth values of the base and modified assertions adhere to the specific linear transformation defined by the modifier's parameters.

        :param ind: The individual entity acting as the subject of the assertion, for which membership variables are retrieved and constrained.
        :type ind: Individual
        :param con: The concept involved in the assertion, serving as the base concept to which the linear modifier is applied.
        :type con: Concept
        :param modifier: The linear modifier applied to the concept, providing parameters for the constraints linking the base concept to the modified concept.
        :type modifier: fuzzy_dl_owl2.fuzzydl.modifier.linear_modifier.LinearModifier
        """

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
        # If y = 0, xAisC <= a, xAisC = a/b xAisModC
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
        # If y = 1, xAisC >= a, (1-b) xAisC = (1-a) xAisModC + (a-b)
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
        """
        Encodes the logical constraints for a triangular modifier assertion within the Mixed-Integer Linear Programming (MILP) model associated with the knowledge base. This method establishes the relationship between an individual's membership degree in a base concept and its membership in a triangularly modified version of that concept, handling both standard concepts and modified concrete concepts by retrieving or creating the appropriate variables. The implementation introduces four binary auxiliary variables to model the piecewise linear structure of the triangular modifier, defined by parameters a, b, and c, thereby enforcing the specific fuzzy logic rules across the rising, peak, and falling segments of the membership function. As a side effect, this method adds new variables and constraints to the MILP solver and records the assertion within the knowledge base.

        :param individual: The entity or object instance serving as the subject of the assertion being solved.
        :type individual: Individual
        :param concept: The concept to which the triangular modifier is applied, serving as the subject of the assertion.
        :type concept: Concept
        :param modifier: Defines the parameters (a, b, c) of the triangular fuzzy logic modifier applied to the concept.
        :type modifier: fuzzy_dl_owl2.fuzzydl.modifier.triangular_modifier.TriangularModifier
        """

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

        # y1 + y2 + y3 + y4 = 1
        self.milp.add_new_constraint(
            Expression(Term(1.0, y1), Term(1.0, y2), Term(1.0, y3), Term(1.0, y4)),
            InequalityType.EQUAL,
            1.0,
        )

        # IF y1 = 1
        #   xAisC \leq a
        #   xAisC \geq 0
        #   xAisModC = 0
        #
        # IF y2 = 1
        #   xAisC \leq b
        #   xAisC \geq a
        #   xAisC = (b-a) xAisModC + a
        #
        # IF y3 = 1
        #   xAisC \leq c
        #   xAisC \geq b
        #   xAisC = (b-c) xAisModC + c
        #
        # IF y4 = 1
        #   xAisC \leq 1
        #   xAisC \geq c
        #   xAisModC = 0

        # xAisC - a y_2 \geq 0
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_A_is_C), Term(-modifier.a, y2)),
            InequalityType.GREATER_THAN,
        )
        # xAisC - b y_3 \geq 0
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_A_is_C), Term(-modifier.b, y3)),
            InequalityType.GREATER_THAN,
        )
        # xAisC - c y_4 \geq 0
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_A_is_C), Term(-modifier.c, y4)),
            InequalityType.GREATER_THAN,
        )
        # xAisC + (1 - a) y_1 \leq 1
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_A_is_C), Term(1.0 - modifier.a, y1)),
            InequalityType.LESS_THAN,
            1.0,
        )
        # xAisC + (1 - b) y_2 \leq 1
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_A_is_C), Term(1.0 - modifier.b, y2)),
            InequalityType.LESS_THAN,
            1.0,
        )
        # xAisC + (1 - c) y_3 \leq 1
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_A_is_C), Term(1.0 - modifier.c, y3)),
            InequalityType.LESS_THAN,
            1.0,
        )
        # xAisModC \leq 1 - y_1 - y_4
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_A_is_mod_C), Term(1.0, y1), Term(1.0, y4)),
            InequalityType.LESS_THAN,
            1.0,
        )
        # xAisC + (a-b) xAisModC + (1 - a) y2 \leq 1
        self.milp.add_new_constraint(
            Expression(
                Term(1.0, x_A_is_C),
                Term(modifier.a - modifier.b, x_A_is_mod_C),
                Term(1.0 - modifier.a, y2),
            ),
            InequalityType.LESS_THAN,
            1.0,
        )
        # xAisC + (a-b) xAisModC  - b y2  \geq a - b
        self.milp.add_new_constraint(
            Expression(
                Term(1.0, x_A_is_C),
                Term(modifier.a - modifier.b, x_A_is_mod_C),
                Term(-modifier.b, y2),
            ),
            InequalityType.GREATER_THAN,
            modifier.a - modifier.b,
        )
        # xAisC + (c-b) xAisModC + (1 - b) y3  \leq 1 + c - b
        self.milp.add_new_constraint(
            Expression(
                Term(1.0, x_A_is_C),
                Term(modifier.c - modifier.b, x_A_is_mod_C),
                Term(1.0 - modifier.b, y3),
            ),
            InequalityType.LESS_THAN,
            1.0 + modifier.c - modifier.b,
        )
        # xAisC + (c-b) xAisModC - c y3 \geq 0
        self.milp.add_new_constraint(
            Expression(
                Term(1.0, x_A_is_C),
                Term(modifier.c - modifier.b, x_A_is_mod_C),
                Term(-modifier.c, y3),
            ),
            InequalityType.GREATER_THAN,
        )

    def add_negated_datatype_restriction(self, ass: Assertion) -> None:
        """
        Processes an assertion representing a negated datatype restriction and applies it to the associated individual within the knowledge base. It validates that the assertion's concept is a complement operator wrapping a concept that defines a role, ensuring the structure matches a logical negation of a datatype property. Upon successful validation, the method extracts the underlying role name and invokes the individual's concrete restriction mechanism to enforce the negation.

        :param ass: The assertion representing the negated datatype restriction, containing the individual and the complement concept to be applied.
        :type ass: Assertion
        """

        a: Individual = ass.get_individual()
        op: Concept = ass.get_concept()
        assert isinstance(op, OperatorConcept) and op.type == ConceptType.COMPLEMENT
        c: Concept = op.get_atom()
        assert isinstance(c, HasRoleInterface)
        f_name: str = c.role
        a.add_concrete_restriction(f_name, ass)

    def rule_n2(self) -> None:
        """Enforces the N2 rule for all individuals by adding a constraint to the MILP model that ensures an individual cannot be asserted as more than one distinct nominal. For each individual, the method collects variables representing the individual's self-nominal status (if applicable) and its associations with other nominals. If there are two or more such variables, a constraint is added to the MILP solver requiring their sum to be less than or equal to one, thereby enforcing mutual exclusivity among nominal assertions."""

        for o in self.individuals.values():
            o_name: str = str(o)
            vars: set[Variable] = set()
            if not isinstance(o, CreatedIndividual) and len(o.get_nominal_list()) != 0:
                # Add xOisO to the list only O if is not a created individual
                x_O_is_O: Variable = self.milp.get_nominal_variable(o_name, o_name)
                vars.add(x_O_is_O)
            for b_name in o.get_nominal_list():
                x_O_is_B: Variable = self.milp.get_nominal_variable(o_name, b_name)
                vars.add(x_O_is_B)
            # The sum must be small or equal than 1
            if len(vars) >= 2:
                sum_vars: Expression = Expression(vars)
                self.milp.add_new_constraint(
                    Expression.add_constant(sum_vars, -1.0), InequalityType.LESS_THAN
                )
                Util.debug(f"Rule_n2: {sum_vars} <= 1")

    def rule_n3(self) -> None:
        """Iterates through the mapping of labels to their associated nodes to enforce a selection constraint within the MILP model. For any label that is linked to multiple nodes, this method retrieves the nominal variables corresponding to those nodes and adds an equality constraint requiring their sum to equal one. This ensures that exactly one node is selected for the given label, effectively implementing a one-hot encoding constraint for multi-node labels. The method modifies the internal MILP model by adding these constraints and does not return a value."""

        for o_name, nodes in self.labels_with_nodes.items():
            if nodes is not None and len(nodes) > 1:
                v: list[Variable] = [
                    self.milp.get_nominal_variable(node, o_name) for node in nodes
                ]
                # x_{v1:{o}} + ... + x_{vn:{o}} = 1
                exp: Expression = Expression(v)
                exp.set_constant(-1.0)
                self.milp.add_new_constraint(exp, InequalityType.EQUAL)
                Util.debug(f"Rule_n3: {exp}")

    def rule_ass_nom(self, a: Individual, c: Concept, v: str) -> None:
        """
        Applies the Assertion Nominal (AssNom) rule to enforce a relationship between a node, a nominal individual, and a concept. It ensures that if a node `v` is identified as the individual `a`, then the degree of membership of `v` in the concept `c` is at least the degree of membership of `a` in `c`. This is achieved by retrieving the relevant MILP variables, adding a formal assertion to the knowledge base, and appending a fuzzy implication constraint to the solver. The method modifies the internal state of the MILP model and assumes that the node `v` corresponds to a valid individual within the system.

        :param a: The individual representing the nominal in the assertion `<a : C>`.
        :type a: Individual
        :param c: The concept C from the assertion <a : C>.
        :type c: Concept
        :param v: Identifier of the node representing an individual.
        :type v: str
        """

        a_name = str(a)
        i: Individual = self.get_individual(v)
        a_is_c: Variable = self.milp.get_variable(a, c)
        v_is_a: Variable = self.milp.get_nominal_variable(v, a_name)
        v_is_c: Variable = self.milp.get_variable(i, c)
        # Add the assertion "v" is c
        self.add_assertion(i, c, DegreeVariable.get_degree(v_is_c))
        # vIs{a} => v:C >= a:C
        Util.debug(f"Adding equation {v_is_a} => {v_is_c} >= {a_is_c}")
        ZadehSolver.zadeh_implies_leq_equation(a_is_c, v_is_a, v_is_c, self.milp)

    def exists_primite_concept_definition(
        self, pcds: set[PrimitiveConceptDefinition], pcd: PrimitiveConceptDefinition
    ) -> bool:
        """
        Checks if a primitive concept definition exists within a provided set by comparing the underlying concept definitions. If a matching definition is found, the method compares the degrees of the input and existing definitions; if the input definition has a higher degree, it updates the degree of the existing definition in the set. Returns True if a match is found, otherwise returns False.

        :param pcds: The set of existing primitive concept definitions to search for a match; matching definitions may be updated.
        :type pcds: set[PrimitiveConceptDefinition]
        :param pcd: The primitive concept definition to check for existence within the set.
        :type pcd: PrimitiveConceptDefinition

        :return: True if a primitive concept definition with the same underlying concept is found in the provided set, False otherwise.

        :rtype: bool
        """

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
        """
        This method incorporates a subsumption axiom, asserting that an atomic concept is an instance of a defined concept, into the TBox. It validates the input by extracting the definition, type, and degree from the provided `PrimitiveConceptDefinition` and checking for redundancy against existing knowledge. Specifically, it prevents the addition of axioms that are logically redundant or already present in the set of inclusions for the given concept. If the axiom is valid and novel, it updates the internal `t_inclusions` dictionary, appending the new definition to the set associated with the concept name.

        :param a: The name of the atomic concept serving as the subject of the inclusion axiom.
        :type a: str
        :param pcd: The primitive concept definition object encapsulating the concept structure, logic operator type, and degree for the right-hand side of the inclusion axiom.
        :type pcd: PrimitiveConceptDefinition
        """

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
        """
        Adds a subsumption axiom of the form "A is a X" to the TBox, where A is an atomic concept and X is defined by the provided PrimitiveConceptDefinition. The method first checks for redundancy and ensures that an identical definition does not already exist for the given concept A. If the definition of X is atomic, the axiom is added to the registry for atomic subsumption; otherwise, it is added to the registry for complex subsumption, thereby modifying the internal state of the knowledge base.

        :param a: The name of the atomic concept A.
        :type a: str
        :param pcd: The primitive concept definition representing the concept X in the axiom 'A is a X', encompassing the concept structure, logic operator type, and degree.
        :type pcd: PrimitiveConceptDefinition
        """

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
        """
        Adds a primitive concept definition axiom of the form 'A is a C' to the specified dictionary within the TBox. The method first verifies that the axiom is not logically redundant based on the concept name, definition, type, and degree. It also checks to ensure that an identical definition object does not already exist in the set associated with the concept name in the target dictionary. If the axiom is valid and unique, it is added to the dictionary, modifying the collection in-place.

        :param a: The name of the atomic concept A, representing the subject of the axiom.
        :type a: str
        :param pcd: The object representing the axiom to be added, encapsulating the definition, logical operator type, and degree.
        :type pcd: PrimitiveConceptDefinition
        :param pcd_dict: Target dictionary mapping concept names to sets of primitive concept definitions where the axiom is stored.
        :type pcd_dict: dict[str, set[PrimitiveConceptDefinition]]
        """

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
        """
        This method adds an equivalence axiom of the form 'A equivalent to C' to the TBox of the knowledge base, where 'A' is an atomic concept identified by a string name and 'C' is a complex concept object. It ensures idempotency by checking whether the specific concept 'C' is already registered as equivalent to 'A'; if the axiom already exists, the method returns without modifying the state. If the axiom is new, it updates the internal dictionary of equivalence axioms to include the relationship between the atomic concept and the provided concept.

        :param a: The name of the atomic concept A.
        :type a: str
        :param conc: The concept expression that is equivalent to the atomic concept `a`.
        :type conc: Concept
        """

        hs: set[Concept] = self.axioms_A_equiv_C.get(a, set())
        # Return if the concept already exists
        for c in hs:
            if c == conc:
                return
        if conc not in hs:
            self.axioms_A_equiv_C[a] = hs | set([conc])

    def add_axioms_to_tg(self) -> None:
        """Processes the pending equivalence axioms stored in `axioms_A_equiv_C` and `axioms_C_equiv_D` and adds them to the TBox as equivalent concept definitions. The method iterates through the first collection to define equivalences between atomic concepts and their associated lists, and through the second collection to define equivalences between concept pairs. After registering these axioms, the method clears both internal collections, consuming the pending axioms and altering the instance state."""

        for cname in self.axioms_A_equiv_C:
            a: Concept = AtomicConcept(cname)
            for b in self.axioms_A_equiv_C.get(cname):
                self.define_equivalent_concepts(a, b)
        for ce in self.axioms_C_equiv_D:
            a: Concept = ce.get_c1()
            b: Concept = ce.get_c2()
            self.define_equivalent_concepts(a, b)
        # Axioms must not be cleared if we want to be able to save the KB correctly
        self.axioms_A_equiv_C.clear()
        self.axioms_C_equiv_D.clear()

    def disjoint_with_defined_concept(self, a: str) -> bool:
        """
        Determines whether the atomic concept `a` is disjoint with any defined concept in the knowledge base. The method iterates over the set of concepts known to be disjoint with `a` and checks if any of them are defined concepts (i.e., present in the definitions table). It returns `False` if a disjoint defined concept is found, and `True` if `a` is not disjoint with any defined concepts or if `a` has no disjointness assertions. This method performs a read-only operation and does not modify the state of the knowledge base.

        :param a: The name of the atomic concept to check for disjointness with defined concepts.
        :type a: str

        :return: True if the concept 'a' is not disjoint with any defined concept, False if it is disjoint with at least one defined concept.

        :rtype: bool
        """

        for b in self.t_disjoints.get(a, set()):
            if b in self.t_definitions:
                return False
        return True

    def definition_absorption(self, gci: GeneralConceptInclusion) -> bool:
        """
        Attempts to perform definition absorption by identifying a bi-directional implication between concepts within the knowledge base. Given an input General Concept Inclusion (GCI), the method searches for a complementary GCI in the existing axiom sets such that the pair forms an equivalence relationship (e.g., `A subsumedBy C` and `C subsumedBy A`). If a matching pair is found and specific semantic constraints are met—such as the logic being classical or the fuzzy degree being exactly 1.0—the method replaces the two inclusions with a single definition in the `t_definitions` collection. This operation modifies the internal state of the knowledge base by removing the absorbed axioms and returns `True` if the transformation was successful, or `False` if no absorption occurred.

        :param gci: A General Concept Inclusion (GCI) representing a subsumption axiom to be processed. It is evaluated to determine if it can be combined with existing axioms to form a concept definition.
        :type gci: GeneralConceptInclusion

        :return: True if the GCI was successfully absorbed into a definition, resulting in changes to the internal state; False otherwise.

        :rtype: bool
        """

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
                    or self.disjoint_with_defined_concept(
                        a
                    )  # there is no disjoint(a, b) in tDis with b being a head of an axiom in Tdef
                ):
                    continue
                # Add A = C
                self.t_definitions[a] = conc
                # Remove A => C
                self.remove_A_is_a_X(a, pcd, False)
                # Remove C => A
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
                # Add A = C
                self.t_definitions[a] = conc
                # Remove A => C
                self.remove_A_is_a_X(a, pcd, self.t_inclusions)
                # Remove C => A
                self.remove_C_is_a_A(aux, gci)
                Util.debug(f"Definition Absorbed: {a} = {conc}")
                return True
        return False

    def definition_absorption_to_do(self, pcd: PrimitiveConceptDefinition) -> bool:
        """
        Attempts to absorb a primitive concept definition into the TBox by identifying a corresponding reverse inclusion to form a full equivalence. The method checks if the provided definition (A subsumes C) can be paired with an existing axiom (C subsumes A) to establish a definition (A equals C). This operation is contingent upon the current knowledge base semantics; specifically, it will not proceed if the logic is fuzzy with a non-unitary degree or a Zadeh implication type. If a valid match is found, the method updates the internal definitions registry, removes the individual inclusions from the processing queue and the TBox, and returns True to indicate a structural change. If no matching reverse inclusion exists or the semantic conditions are not met, the method returns False without modifying the state.

        :param pcd: The primitive concept definition to be absorbed into the TBox.
        :type pcd: PrimitiveConceptDefinition

        :return: True if the primitive concept definition was successfully absorbed into the TBox; False otherwise.

        :rtype: bool
        """

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
                # Add A = C
                self.t_definitions[a] = conc
                # Remove A => C
                self.remove_A_is_a_X(a, pcd, self.axioms_to_do_A_is_a_C)
                self.remove_A_is_a_X(a, pcd, self.t_inclusions)
                # Remove C => A
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
        """
        Removes a primitive concept definition associated with a specific key from the knowledge base, with the removal strategy determined by the type of the third argument. When provided with a dictionary, the method removes the definition directly from that collection; alternatively, when provided with a boolean atomic flag, it delegates to logic specific to atomic or non-atomic concepts. This method mutates the knowledge base's internal state and enforces strict type checking, raising an error if the arguments do not match the required signature.

        :param args: A tuple containing a string key, a PrimitiveConceptDefinition, and either a boolean flag or a dictionary mapping strings to sets of definitions.
        :type args: typing.Any

        :raises ValueError: Raised if the third argument is neither a boolean flag nor a dictionary mapping strings to sets of PrimitiveConceptDefinition.
        """

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
        """
        This helper method removes a specific `PrimitiveConceptDefinition` from the set associated with the given key within the provided dictionary. It modifies the dictionary in place by extracting the set corresponding to the key and discarding the specified definition. As a cleanup step, if the removal results in an empty set for that key, the method deletes the key from the dictionary entirely to prevent cluttering the data structure with empty entries.

        :param key: The dictionary key identifying the set of definitions from which the primitive concept definition is removed.
        :type key: str
        :param pcd: The specific primitive concept definition instance to be removed from the collection.
        :type pcd: PrimitiveConceptDefinition
        :param pcd_dict: Dictionary mapping keys to sets of primitive concept definitions from which the specified definition is removed.
        :type pcd_dict: dict[str, set[PrimitiveConceptDefinition]]
        """

        pcd_dict.get(key).remove(pcd)
        if len(pcd_dict.get(key)) == 0:
            del pcd_dict[key]

    def __remove_A_is_a_X_2(
        self, key: str, pcd: PrimitiveConceptDefinition, atomic: bool
    ) -> None:
        """
        This method serves as a dispatcher for removing a primitive concept definition from the knowledge base, routing the operation based on the classification of the concept. If the `atomic` flag is True, the method delegates to `remove_A_is_a_B` to remove the definition from the collection of atomic axioms; otherwise, it delegates to `remove_A_is_a_C` to handle non-atomic definitions. As a side effect, this process permanently alters the internal state of the knowledge base by deleting the specified entry associated with the provided key and definition object.

        :param key: The unique identifier for the primitive concept definition.
        :type key: str
        :param pcd: The primitive concept definition to be removed.
        :type pcd: PrimitiveConceptDefinition
        :param atomic: If True, removes the definition from the A-is-a-B axioms; otherwise, removes it from the A-is-a-C axioms.
        :type atomic: bool
        """

        if atomic:
            self.remove_A_is_a_B(key, pcd)
        else:
            self.remove_A_is_a_C(key, pcd)

    def remove_A_is_a_B(self, key: str, pcd: PrimitiveConceptDefinition) -> None:
        """
        Deletes a specific primitive concept definition from the list of axioms associated with the provided key. This method modifies the internal state of the knowledge base by removing the specified definition object. As a cleanup step, if the removal leaves the list of definitions for the key empty, the key is removed entirely from the dictionary to maintain data integrity.

        :param key: The key identifying the specific entry in the axioms dictionary from which the definition is removed.
        :type key: str
        :param pcd: The specific instance to be removed from the collection identified by the key.
        :type pcd: PrimitiveConceptDefinition
        """

        self.axioms_A_is_a_B.get(key).remove(pcd)
        if len(self.axioms_A_is_a_B.get(key)) == 0:
            del self.axioms_A_is_a_B[key]

    def remove_A_is_a_C(self, key: str, pcd: PrimitiveConceptDefinition) -> None:
        """
        Removes a specific primitive concept definition from the collection stored under the given key in the `axioms_A_is_a_C` dictionary. This method mutates the internal state by deleting the specified definition from the list associated with the key. As a cleanup step, if the removal of the definition leaves the list empty, the key is deleted entirely from the dictionary to prevent empty entries.

        :param key: The dictionary key used to locate the collection of axioms containing the primitive concept definition.
        :type key: str
        :param pcd: The specific primitive concept definition instance to be removed.
        :type pcd: PrimitiveConceptDefinition
        """

        self.axioms_A_is_a_C.get(key).remove(pcd)
        if len(self.axioms_A_is_a_C.get(key)) == 0:
            del self.axioms_A_is_a_C[key]

    def remove_C_is_a_A(self, key: str, gci: GeneralConceptInclusion) -> None:
        """
        Removes a specific General Concept Inclusion (GCI) from the collection of axioms associated with the given key within the `axioms_C_is_a_A` dictionary. This method mutates the underlying data structure by deleting the specified GCI object from the list or set mapped to the key. Furthermore, it performs a cleanup operation where the key itself is removed from the dictionary if the associated collection becomes empty after the deletion. The method assumes that the provided key exists in the dictionary and that the GCI is present in the collection; failure to meet these conditions will result in an error.

        :param key: The dictionary key identifying the collection from which the general concept inclusion should be removed.
        :type key: str
        :param gci: The specific general concept inclusion to remove from the collection identified by the key.
        :type gci: GeneralConceptInclusion
        """

        self.axioms_C_is_a_A.get(key).remove(gci)
        if len(self.axioms_C_is_a_A.get(key)) == 0:
            del self.axioms_C_is_a_A[key]

    def remove_C_is_a_D(self, key: str, gci: GeneralConceptInclusion) -> None:
        """
        Deletes a specific General Concept Inclusion (GCI) from the internal dictionary mapping keys to collections of axioms. This method mutates the `axioms_C_is_a_D` attribute by removing the provided `gci` from the list associated with the given `key`. Furthermore, it performs a cleanup operation where the `key` is entirely removed from the dictionary if the associated collection becomes empty after the deletion.

        :param key: The identifier used to retrieve the specific collection of axioms from which the general concept inclusion will be removed.
        :type key: str
        :param gci: The specific general concept inclusion axiom to be removed from the collection.
        :type gci: GeneralConceptInclusion
        """

        self.axioms_C_is_a_D.get(key).remove(gci)
        if len(self.axioms_C_is_a_D.get(key)) == 0:
            del self.axioms_C_is_a_D[key]

    def remove_C_is_a_X(
        self, key: str, gci: GeneralConceptInclusion, atomic: bool
    ) -> None:
        """
        Removes a specified General Concept Inclusion (GCI) from the knowledge base, routing the removal request to the appropriate internal storage mechanism based on the nature of the concept. It accepts a key to identify the relevant context, the GCI object to be removed, and a boolean flag indicating whether the concept is atomic. If the `atomic` flag is true, the method delegates to `remove_C_is_a_A` to remove the inclusion from the set of atomic axioms; otherwise, it delegates to `remove_C_is_a_D` to remove it from the set of defined axioms. This operation directly modifies the internal state of the knowledge base by eliminating the specified relationship.

        :param key: Identifier used to locate the specific general concept inclusion to be removed.
        :type key: str
        :param gci: The general concept inclusion to be removed from the axioms.
        :type gci: GeneralConceptInclusion
        :param atomic: If True, removes the inclusion from the atomic axioms; otherwise, removes it from the derived axioms.
        :type atomic: bool
        """

        if atomic:
            self.remove_C_is_a_A(key, gci)
        else:
            self.remove_C_is_a_D(key, gci)

    def gci_transformations_A_is_a_C(self) -> None:
        """This method processes the queue of pending axioms representing subclass relationships where a concept A is a sub-concept of C. It iterates through these axioms, attempting to apply a General Concept Inclusion (GCI) transformation to each one. If the transformation is unsuccessful, the axiom is permanently added to the knowledge base's main collection of "A is a C" axioms. The method ensures that axioms which cannot be transformed further are retained, while potentially modifying the internal state of the knowledge base through the transformation process."""

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
        """Iterates through the collection of pending General Concept Inclusion (GCI) axioms representing subsumption relationships of the form 'C is a A'. For each axiom, it attempts to apply a specific transformation logic via the `gci_transformation` method; if the transformation is unsuccessful, the axiom is re-added to the knowledge base's storage for 'C is a A' relationships. This process modifies the internal state of the object by consuming the input list of axioms and potentially repopulating the axiom set based on the success or failure of the transformation."""

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
        """Processes the set of pending 'C is a D' axioms by attempting to apply General Concept Inclusion (GCI) transformations to each entry. For every axiom, it invokes a transformation helper; if the helper indicates that the transformation was not applied, the axiom is re-registered using its subsumer, subsumed, degree, and type attributes. The method iterates over a copy of the axiom lists to prevent iteration errors caused by modifications to the underlying collections and logs debug information to mark the start of the process."""

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
        """Iterates through the collection of axioms defining "is-a" relationships to perform concept absorption. To prevent issues arising from modifying the collection during iteration, the method processes a cloned copy of the axioms rather than the original data structure. For each axiom, it attempts to integrate the concept using synonym absorption specific to "is-a" relationships, and if that is unsuccessful, it falls back to general concept absorption. This process updates the internal state of the knowledge base by refining or merging concepts based on the defined taxonomic relationships."""

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
        """Iterates through the pending axioms of the form "A is a B" stored in the knowledge base to perform synonym absorption. To ensure data integrity during processing, the method creates a deep copy of the axioms before iterating over them. For each concept definition, it invokes the synonym absorption logic; if the process fails for a specific concept, it is skipped. Upon completion of the loop, the original collection of pending axioms is cleared, indicating that they have been processed."""

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
        """Executes the partitioning logic for axioms of the form "A is a C" by attempting to absorb concepts and roles into the knowledge base. The method operates on a cloned copy of the axioms to ensure the integrity of the iteration process, preventing issues that might arise from modifying the collection while traversing it. For each axiom, it invokes `concept_absorption` and `role_absorption`; if both operations fail to process the axiom, the iteration proceeds to the next candidate. This process modifies the internal state of the knowledge base but returns no value."""

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
        """Iterates through the pending axioms of the form "A is a C" to perform definition absorption. The method operates on cloned copies of the primitive concept definitions to prevent interference during iteration, invoking `definition_absorption_to_do` for each item. As a side effect, it clears the internal dictionary of pending axioms once the processing loop is finished, effectively resetting the queue for this specific axiom type."""

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
        """Iterates over a copy of the axioms representing subclass relationships (C is a A) to attempt their absorption into the knowledge base. For each axiom, the method sequentially tries concept absorption, definition absorption, and role absorption. If none of these strategies successfully process the axiom, the loop proceeds to the next one; otherwise, the side effects of the successful absorption modify the knowledge base's internal state."""

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
        """This method processes axioms asserting that a concept C is a subclass of concept D by iterating through a cloned snapshot of the stored axioms to ensure safe traversal. For each General Concept Inclusion (GCI) in the set, it attempts to absorb the axiom using either concept absorption or role absorption strategies. If neither absorption method successfully integrates the axiom, the loop proceeds to the next item without modifying the state for that specific axiom."""

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
        """Prepares the Terminological Box (TBox) for reasoning by normalizing axioms and applying structural optimizations based on the current configuration. If optimizations are disabled, the method converts all TBox axioms directly into General Concept Inclusions (GCIs). Otherwise, it evaluates whether the TBox is "lazy unfoldable"; if this condition is met, axioms are segregated into definitions and inclusions for efficient processing. For more complex structures, the method performs a multi-phase absorption process, iteratively applying GCI transformations to rewrite axioms until no further transformations are possible. This procedure modifies the internal state of the knowledge base by reorganizing axiom sets and ultimately solves the resulting constraints against all individuals, including domain and range axioms."""

        # expressivity
        # classes
        # A is C
        # A = C
        # A = B
        # domain
        # range
        # GCIs
        # disjoints
        # LU

        # 1. No optimizations: add every TBox axiom to tG
        # no_abs: bool = True
        no_abs: bool = False
        if ConfigReader.OPTIMIZATIONS == 0 or no_abs:
            Util.debug("No Absorption...")
            self.represent_tbox_with_gcis()
            return

        # Phase 0
        # Check if TBOX already lazy unfoldable
        if self.is_lazy_unfoldable():
            Util.debug("Already lazy unfoldable")
            self.lazy_unfoldable = True
            # Copy axioms_A_equiv_C into t_definitions
            for a, hs in self.axioms_A_equiv_C.items():
                for c in hs:
                    self.t_definitions[a] = c
            # copy axioms_A_is_a_C and axioms_A_is_a_B into t_inclusions
            for a, hs in self.axioms_A_is_a_C.items():
                for pcd in hs:
                    self.add_axiom_to_inc(a, pcd)
            for a, hs in self.axioms_A_is_a_B.items():
                for pcd in hs:
                    self.add_axiom_to_inc(a, pcd)
            # Solve TBox
            self.solve_domain_and_range_axioms()
            return

        # 2. Phase A
        # Add axioms to t_definitions, step 8b (Phase A)
        self.add_axioms_to_tg()

        # 3. Process GCI transformations until no GCI transformation can be applied
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
            # Select axiom tau in axioms_A_is_a_C that has not yet been processed
            self.gci_transformations_A_is_a_C()
            # Select axiom tau in axioms_C_is_a_A that has not yet been processed
            self.gci_transformations_C_is_a_A()
            # Select axiom tau in axioms_C_is_a_D that has not yet been processed
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

        # 4. Process the other absorptions
        # None of them can generate new axioms in the lists axioms_A_is_a_C, axioms_C_is_a_A, axioms_C_is_a_D
        # Hence, GCI transformation cannot be applied anymore.
        self.partition_loop_A_is_a_B()
        self.partition_loop_A_is_a_C()
        self.partition_loop_C_is_a_A()
        self.partition_loop_C_is_a_D()

        # another round
        self.partition_loop_to_do_A_is_a_B()
        self.partition_loop_to_do_A_is_a_C()

        # 5. Exit condition
        self.exit_condition()

        # Solve TBox
        for ind in self.individuals.values():
            for gci in self.t_G:
                self.solve_gci(ind, gci)
        self.solve_domain_and_range_axioms()

    def is_lazy_unfoldable(self) -> bool:
        """
        Determines whether the knowledge base satisfies the structural constraints required for lazy unfolding. The method returns `False` if the base contains axioms where a concept is a subclass of an atomic concept, a subclass of another concept, or equivalent to another concept. It also imposes strict conditions on equivalences between atomic concepts and concepts, requiring that such atomic concepts do not appear in other inclusion axioms and have at most one equivalent counterpart. Furthermore, the check fails if any pair of disjoint concepts are both involved in these equivalence axioms. This method performs a read-only validation and does not modify the knowledge base state.

        :return: True if the fuzzy knowledge base meets the structural requirements for lazy unfolding, False otherwise.

        :rtype: bool
        """

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
        # disj(a, b) with both a and b in t_disjoints
        for a in self.t_disjoints:
            for b in self.t_disjoints.get(a):
                if a not in self.axioms_A_equiv_C or b not in self.axioms_A_equiv_C:
                    continue
                return False
        return True

    def exit_condition(self) -> None:
        """Processes all stored General Concept Inclusions (GCIs) to finalize the knowledge base structure by converting them into a specific graph representation. It iterates through the internal collections of axioms categorized as 'A is a B', 'A is a C', 'C is a A', and 'C is a D', delegating the transformation of each item to the appropriate helper method. This operation results in the modification of the internal graph `tG`, adding the transformed axioms in the form `*top* isA (C -> D)`. If the internal axiom collections are empty, the method executes without effect."""

        Util.debug(f"{constants.SEPARATOR}Exit condition{constants.SEPARATOR}")

        # Convert all GCIs in axioms_A_is_a_B
        for pcds in self.axioms_A_is_a_B.values():
            for pcd in pcds:
                self.exit_condition_A_is_a_X(pcd)

        # Convert all GCIs in axioms_A_is_a_C
        for pcds in self.axioms_A_is_a_C.values():
            for pcd in pcds:
                self.exit_condition_A_is_a_X(pcd)

        # Convert all GCIs in axioms_C_is_a_A
        for gcis in self.axioms_C_is_a_A.values():
            for gci in gcis:
                self.exit_condition_C_is_a_X(gci)

        # Convert all GCIs in axioms_C_is_a_A
        for gcis in self.axioms_C_is_a_D.values():
            for gci in gcis:
                self.exit_condition_C_is_a_X(gci)

    def exit_condition_C_is_a_X(self, gci: GeneralConceptInclusion) -> None:
        """
        Processes the exit condition for general concept inclusions (GCIs) representing axioms of the form 'C is a X'. If the subsumed concept is the universal concept (Top), the original GCI is directly appended to the internal goal list `t_G`. Otherwise, the method transforms the GCI into an implication form where the subsumer is set to Top and the subsumed concept is replaced by a material implication between the original subsumed and subsumer concepts. The specific logic operator used for the implication—such as Gödel, Kleene-Dienes, Łukasiewicz, or Zadeh—is determined by the type of the input GCI. This transformation results in a new GCI being added to `t_G`, modifying the state of the knowledge base.

        :param gci: Represents the subsumption axiom "C is a X", providing the subsumed and subsumer concepts as well as the specific logic operator type and degree used to construct the implication.
        :type gci: GeneralConceptInclusion
        """

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
        """
        Processes a primitive concept definition representing the axiom "A is a X" and adds a corresponding General Concept Inclusion (GCI) to the knowledge base's internal list. The method extracts the defined concept, its definition, the implication type, and the degree of truth. If the defined concept is the universal concept (Top), the method directly appends a GCI representing the subsumption of the definition by the defined concept. For all other concepts, the method transforms the axiom into a GCI where the left-hand side is an implication concept (constructed using the specific logic operator such as Goedel, Kleene-Dienes, Lukasiewicz, or Zadeh) and the right-hand side is the Top concept, thereby asserting the validity of the implication within the system.

        :param pcd: Represents the primitive concept definition for the axiom "A is a X", containing the defined concept, the definition (atomic or complex), the implication type, and the degree.
        :type pcd: PrimitiveConceptDefinition
        """

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
        """
        Determines whether the fuzzy knowledge base is currently loaded and available for operations. It returns a boolean value representing the internal loading state, allowing users to verify readiness before attempting to access data. This method performs a read-only check and does not modify the object's state or trigger any side effects.

        :return: True if the fuzzy KB is loaded, False otherwise.

        :rtype: bool
        """

        return self.KB_LOADED

    def check_role(self, role_name: str, conc: Concept) -> None:
        """
        Verifies the consistency of a role's definition by ensuring it is not simultaneously classified as abstract and concrete. The method inspects the provided concept to determine the role's type: if the concept is concrete, the role is registered as concrete; otherwise, it is registered as abstract. Additionally, it checks for naming collisions between the role and existing concepts, issuing a warning if a conflict is detected. If the role has already been defined with a conflicting type (e.g., attempting to define a concrete role as abstract), an error is raised to maintain the integrity of the knowledge base.

        :param role_name: Name of the role to be validated and classified as abstract or concrete.
        :type role_name: str
        :param conc: The concept used to determine whether the role is concrete or abstract based on its own type.
        :type conc: Concept
        """

        if (
            self.atomic_concepts.get(role_name) is not None
            or self.concrete_concepts.get(role_name) is not None
        ):
            Util.warning(
                f"Warning: {role_name} is the name of both a concept and a role."
            )
        if conc.is_concrete():
            # role_name is concrete
            if role_name in self.abstract_roles:
                Util.error(f"Error: Role {role_name} cannot be concrete and abstract.")
            self.concrete_roles.add(role_name)
        else:
            # role_name is abstract
            if role_name in self.concrete_roles:
                Util.error(f"Error: Role {role_name} cannot be concrete and abstract.")
            self.abstract_roles.add(role_name)

    @typing.overload
    def degree_if_not_one(self, deg: Degree) -> str: ...

    @typing.overload
    def degree_if_not_one(self, d: float) -> str: ...

    def degree_if_not_one(self, *args) -> str:
        """
        This method provides a conditional string representation of a degree value, typically used to suppress the display of a default degree. It accepts a single argument, which may be either a `Degree` object or a numeric type. If the degree value is equal to 1.0, the method returns an empty string; otherwise, it returns the string representation of the degree. The method validates the input type and raises a `ValueError` if the provided argument is neither a `Degree` instance nor a number.

        :param args: A single argument representing the degree, accepted as either a `Degree` instance or a numeric type.
        :type args: typing.Any

        :raises ValueError: Raised if the provided argument is not a Degree instance or a numeric type.

        :return: The string representation of the degree if it is not equal to 1.0; otherwise, an empty string.

        :rtype: str
        """

        assert len(args) == 1
        if isinstance(args[0], Degree):
            return self.__degree_if_not_one_1(*args)
        elif isinstance(args[0], constants.NUMBER):
            return self.__degree_if_not_one_2(*args)
        else:
            raise ValueError

    def __degree_if_not_one_1(self, deg: Degree) -> str:
        """
        Generates a string representation of a degree, conditionally omitting the value if it is a numeric 1.0. If the input degree is numeric, the method delegates to `degree_if_not_one` to return an empty string when the value is 1.0 or the string representation otherwise. For non-numeric degrees, the method returns the direct string conversion of the degree object.

        :param deg: The degree of the term to be formatted, which can be numeric or symbolic.
        :type deg: Degree

        :return: The string representation of the degree, or an empty string if the degree is numeric and equal to 1.0.

        :rtype: str
        """

        if deg.is_numeric():
            return self.degree_if_not_one(
                typing.cast(DegreeNumeric, deg).get_numerical_value()
            )
        return str(deg)

    def __degree_if_not_one_2(self, d: float) -> str:
        """
        This helper method formats a degree value for string representation, typically used to simplify the display of mathematical expressions where a degree of one is implicit. It accepts a float representing the degree and returns an empty string if the value is strictly equal to 1.0. For any other value, including those close to 1.0 due to floating-point precision, it returns the standard string representation of the number.

        :param d:
        :type d: float

        :return: The string representation of the degree if it is not 1.0, otherwise an empty string.

        :rtype: str
        """

        return "" if d == 1.0 else str(d)

    def define_concreate_feature(self, role: str) -> None:
        """
        Registers the specified role as a concrete feature within the knowledge base, updating internal tracking sets and the underlying MILP model. This method adds the role to the collection of concrete and functional roles, sets a flag indicating the presence of concrete fuzzy concepts, and invokes the MILP solver to add the feature as a string attribute. The operation is idempotent, meaning that if the role is already defined as concrete, the method returns without making changes. However, it enforces mutual exclusivity by raising an error if the provided role is currently defined as an abstract role.

        :param role: The identifier for the concrete feature to be defined. It must not be an existing abstract role.
        :type role: str
        """

        if role in self.concrete_features:
            return
        if role in self.abstract_roles:
            Util.error(f"Error: Role {role} cannot be concrete and abstract.")

        self.concrete_roles.add(role)
        self.functional_roles.add(role)
        self.concrete_fuzzy_concepts = True

        self.milp.add_string_feature(role)

    def define_boolean_concrete_feature(self, fun_role: str) -> None:
        """
        Registers a concrete feature with a boolean range within the knowledge base using the specified identifier. This method performs internal setup by invoking `define_concreate_feature` and then instantiates a `ConcreteFeature` object configured for boolean values, storing it in the `concrete_features` dictionary. As a side effect, this operation mutates the `concrete_features` mapping, potentially overwriting any existing entry associated with the provided feature name.

        :param fun_role: The unique name or identifier for the concrete feature.
        :type fun_role: str
        """

        self.define_concreate_feature(fun_role)
        self.concrete_features[fun_role] = ConcreteFeature(fun_role, True)

    def define_string_concrete_feature(self, fun_role: str) -> None:
        """
        Defines a concrete feature with a string value range within the knowledge base. This method initializes the feature by calling the internal definition routine and then creates a `ConcreteFeature` instance associated with the provided role name. The instance is stored in the `concrete_features` dictionary, which will overwrite any existing entry mapped to the same name.

        :param fun_role: The name of the concrete feature to be defined.
        :type fun_role: str
        """

        self.define_concreate_feature(fun_role)
        self.concrete_features[fun_role] = ConcreteFeature(fun_role)

    def define_integer_concrete_feature(self, fun_role: str, d1: int, d2: int) -> None:
        """
        Defines a concrete feature constrained to integer values within a specific inclusive range, identified by the provided name. This method registers the feature within the knowledge base's internal collection, initializing a ConcreteFeature instance with the specified lower and upper bounds. The boundary values are explicitly cast to integers to handle potential type variations, and the operation will overwrite any existing definition associated with the same feature name.

        :param fun_role: The name or identifier for the concrete feature.
        :type fun_role: str
        :param d1: Inclusive lower bound of the integer range.
        :type d1: int
        :param d2: Upper bound of the integer range.
        :type d2: int
        """

        self.define_concreate_feature(fun_role)
        self.concrete_features[fun_role] = ConcreteFeature(fun_role, int(d1), int(d2))

    def define_real_concrete_feature(self, fun_role: str, d1: float, d2: float) -> None:
        """
        Defines and registers a concrete feature that accepts real number values within the closed interval [`d1`, `d2`]. This method performs internal initialization for the feature before creating a `ConcreteFeature` instance, which is then mapped to the specified `fun_role` in the `concrete_features` dictionary. The provided bounds are explicitly converted to floats, and any existing feature sharing the same name will be overwritten by this operation.

        :param fun_role: Name of the concrete feature being defined.
        :type fun_role: str
        :param d1: Lower bound of the real number range.
        :type d1: float
        :param d2: Upper bound of the inclusive range for the concrete feature.
        :type d2: float
        """

        self.define_concreate_feature(fun_role)
        self.concrete_features[fun_role] = ConcreteFeature(
            fun_role, float(d1), float(d2)
        )

    def set_logic(self, logic: FuzzyLogic) -> None:
        """
        Assigns the specified fuzzy logic system to the knowledge base, effectively updating the global semantics configuration used by the module. This method replaces the current logic definition stored in the module-level `KNOWLEDGE_BASE_SEMANTICS` constant with the provided `FuzzyLogic` instance. Consequently, this operation has a global side effect, altering the logical interpretation for all components that reference this constant. Additionally, it logs the updated logic value for debugging purposes.

        :param logic: The fuzzy logic instance defining the operational semantics for the knowledge base.
        :type logic: FuzzyLogic
        """

        constants.KNOWLEDGE_BASE_SEMANTICS = logic
        Util.debug(f"Fuzzy logic: {logic}")

    def get_logic(self) -> FuzzyLogic:
        """
        Retrieves the `FuzzyLogic` instance that defines the semantic rules and operations used by the knowledge base. The method returns a reference to a global constant representing the logic semantics, indicating that the logic configuration is shared across the application rather than being unique to specific instances. This is a read-only accessor with no side effects on the internal state of the knowledge base.

        :return: The fuzzy logic semantics used by the knowledge base.

        :rtype: FuzzyLogic
        """

        return constants.KNOWLEDGE_BASE_SEMANTICS

    def rule_atomic(self, ass: Assertion) -> None:
        """
        Processes the given assertion by applying the atomic rule, which triggers a lazy unfolding operation on the assertion. This method modifies the internal state of the knowledge base by incrementing the counters for both the atomic rule application and the old 01 variables. The actual logical manipulation is delegated to the `rule_lazy_unfolding` method, ensuring that the assertion is handled according to the system's lazy evaluation strategy while maintaining accurate usage statistics.

        :param ass: The assertion to which the atomic rule is applied.
        :type ass: Assertion
        """

        self.rules_applied[KnowledgeBaseRules.RULE_ATOMIC] += 1
        self.old_01_variables += 1
        self.rule_lazy_unfolding(ass)

    def rule_complemented_lazy_unfolding(self, ass: Assertion) -> None:
        """
        Applies the complemented lazy unfolding inference rule to a given assertion, specifically targeting assertions where an individual is associated with a negated concept. The method retrieves the positive form of the concept and consults the T-box to find synonyms or definitions for it. For each equivalent concept identified, it adds a new assertion to the knowledge base stating that the individual belongs to the negation of the equivalent concept and enforces an equality constraint within the underlying MILP model between the variables of the original and new assertions. This operation modifies the state of the knowledge base and the optimization model by introducing new variables and constraints, effectively propagating the assertion through equivalent class hierarchies.

        :param ass: The assertion containing the individual and the negated concept to be processed by the complemented lazy unfolding rule.
        :type ass: Assertion
        """

        ind: Individual = ass.get_individual()
        not_a: Concept = ass.get_concept()
        x_a_not_a: Variable = self.milp.get_variable(ass)
        a: Concept = -not_a
        a_name: str = str(a)

        # 1. A = B
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

        # 2. A = C
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
        """
        Performs lazy unfolding on a given assertion by expanding the concept based on the knowledge base's terminological axioms. It iterates through primitive concept inclusions, synonyms, concept definitions, and disjointness axioms associated with the concept in the assertion. For each inclusion, it generates a new assertion and adds a corresponding constraint to the MILP model, handling specific fuzzy logic operators such as Lukasiewicz, Gödel, and Zadeh. When synonyms or definitions are found, it enforces equality constraints between the variables representing the concepts. If disjointness axioms exist, it adds constraints ensuring the variables cannot be simultaneously true. This process modifies the internal MILP solver state by adding variables and constraints, updates internal counters for variable statistics, and manages a cache of processed disjoint relationships to prevent redundancy.

        :param ass: The assertion representing the individual and concept to be expanded via lazy unfolding.
        :type ass: Assertion
        """

        ind: Individual = ass.get_individual()
        a: Concept = ass.get_concept()
        a_name: str = str(a)
        var_a: Variable = self.milp.get_variable(ind, a)

        # 1. A isA C
        ind_a: Variable = self.milp.get_variable(ind, a)
        pcds: set[PrimitiveConceptDefinition] = self.t_inclusions.get(a_name, set())
        for pcd in pcds:
            if pcd.get_type() == LogicOperatorType.KLEENE_DIENES:
                kd: Concept = ImpliesConcept.kleene_dienes_implies(
                    a, pcd.get_definition()
                )
                self.add_assertion(ind, kd, DegreeNumeric.get_degree(pcd.get_degree()))
                continue
            # Rule: (A subclassof C >= n) and (a : A) imply (a : C) and x_{a:C} \geq x_{a:C} \otimes n)
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

        # 2. A = B (syn)
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

        # 3. A = C
        c: Concept = self.t_definitions.get(a_name)
        if c is not None:
            var_c: Variable = self.milp.get_variable(ind, c)
            self.add_assertion(ind, c, DegreeVariable.get_degree(var_c))
            self.milp.add_new_constraint(
                Expression(Term(1.0, var_c), Term(-1.0, var_a)), InequalityType.EQUAL
            )

        # 4. Disjoint axioms
        disj_concs: set[str] = self.t_disjoints.get(a_name)
        if disj_concs is not None:
            Util.debug(f"Lazy unfolding Disjoint axioms: {a_name}")
            hs2: set[str] = self.disjoint_variables.get(a_name, set())
            for name in disj_concs:
                Util.debug(f"Disjoint with: {name}")
                # Add v : name
                self.old_binary_variables += 1
                var_disj: Variable = self.milp.get_variable(ind, name)
                self.add_assertion(
                    ind, AtomicConcept(name), DegreeVariable.get_degree(var_disj)
                )
                # State that the variables are disjoint
                if str(var_disj) not in hs2:
                    ZadehSolver.and_equation(var_a, var_disj, self.milp)
                    hs2.add(str(var_disj))
            self.disjoint_variables[a_name] = hs2

    def rule_complemented_atomic(self, ass: Assertion) -> None:
        """
        Enforces the mathematical relationship between an individual's membership in a concept and its complement within the mixed-integer linear programming (MILP) model. Given an assertion asserting that an individual belongs to a negated concept, this method retrieves the corresponding MILP variables and adds an equality constraint defining the negated variable as one minus the positive variable (e.g., $x_{a:\neg A} = 1 - x_{a:A}$). As side effects, it increments the internal counter tracking the application of this rule and triggers a lazy unfolding process for the assertion to handle further logical implications.

        :param ass: The assertion involving an individual and a concept, used to enforce the logical constraint between the concept and its complement.
        :type ass: Assertion
        """

        self.rules_applied[KnowledgeBaseRules.RULE_COMPLEMENT] += 1
        ind: Individual = ass.get_individual()
        not_a: Concept = ass.get_concept()
        x_a_not_a: Variable = self.milp.get_variable(ass)
        a: Concept = -not_a
        x_a_is_a: Variable = self.milp.get_variable(ind, a)
        # x_{a:\not A} = 1 - x_{a: A}
        self.milp.add_new_constraint(
            Expression(1.0, Term(-1.0, x_a_is_a), Term(-1.0, x_a_not_a)),
            InequalityType.EQUAL,
        )
        self.rule_complemented_lazy_unfolding(ass)

    def rule_and(self, ass: Assertion) -> None:
        """
        Applies the logical AND rule to the provided assertion, delegating the specific implementation to a solver determined by the current knowledge base semantics. If the system is configured for Lukasiewicz logic, it invokes the Lukasiewicz solver; for Zadeh logic, it invokes the Zadeh solver; otherwise, it defaults to the Classical solver. Additionally, this method updates the internal statistics by incrementing the counter associated with the applied rule variant.

        :param ass: The assertion to be processed by the AND rule according to the active logic semantics.
        :type ass: Assertion
        """

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
        """
        Applies the logical OR rule to the provided assertion, delegating the resolution to a solver determined by the current knowledge base semantics. The method checks the global configuration to select between Lukasiewicz, Zadeh, or classical logic solvers, applying the corresponding logical operations to the assertion. As a side effect, it increments the internal counter tracking the usage of specific rules within the knowledge base and modifies the system state through the invoked solver.

        :param ass: The assertion to which the OR rule is applied.
        :type ass: Assertion
        """

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
        """
        Applies the HAS_VALUE rule to the given assertion by establishing a relation between the assertion's subject individual and the specific value individual defined by the concept. If the role involved is functional and a relation already exists for that role, the method merges the existing object individual with the target value individual to preserve functional uniqueness, determining the merge direction based on whether the existing individual is blockable. It subsequently adds constraints to the MILP solver to model the logical implications between the assertion, the nominal equality of the individuals, and the relation. For non-functional roles or when no prior relation exists, the method directly adds the new relation to the knowledge base.

        :param ass: The assertion representing a 'has value' constraint to be processed, defining a relationship between an individual and a specific value.
        :type ass: Assertion
        """

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
                # If b is a created individual, merge b into o
                self.merge(o, b)
            elif b_name != str(o):
                # Otherwise, merge o into b if they are different
                self.merge(b, o)
            rel2: Relation = Relation(r, a, o, d)
            x_rel: Variable = self.milp.get_variable(rel2)
            x_ass: Variable = self.milp.get_variable(a, c)
            # xImpl = x_{a : some R.{o}} => x_{a,b:R}
            x_impl: Variable = self.milp.get_new_variable(VariableType.SEMI_CONTINUOUS)
            ZadehSolver.zadeh_implies_equation(x_impl, x_ass, x_rel, self.milp)
            # x_{b:{o}} => x_{a : some R.{o}} => x_{a,b:R} = 1
            ZadehSolver.zadeh_implies_equation(1.0, x_b_is_o, x_impl, self.milp)
            # xAss <= x_{b:C} \otimes x_{(a:b):R}
            ZadehSolver.and_leq_equation(x_ass, x_b_is_o, x_rel, self.milp)
        else:
            self.add_relation(a, r, o, d)

    def add_labels_with_nodes(self, node: str, ind_name: str) -> None:
        """
        Associates a specific label with a target node within the knowledge base, performing an idempotent check to ensure the label is not added if it already exists. If the label is new, the method updates the internal registry of labels and retrieves the Individual object corresponding to the node. It then iterates through all concepts associated with that individual and applies the rule_ass_nom method to each, effectively triggering inference logic based on the new label for every concept the node participates in.

        :param node: The identifier of the target node (Individual) to which the label will be associated.
        :type node: str
        :param ind_name: The name of the individual to associate with the node as a label.
        :type ind_name: str
        """

        name_set: set[str] = self.labels_with_nodes.get(node, set())
        # We only apply ruleAssNom the first time that the label is added to the node
        if ind_name not in name_set:
            name_set.add(ind_name)
            self.labels_with_nodes[node] = name_set
            i: Individual = self.get_individual(node)
            for c in i.get_concepts():
                self.rule_ass_nom(i, c, ind_name)

    def rule_some(self, ass: Assertion) -> None:
        """
        Processes an assertion representing an existential restriction by applying the appropriate inference logic. If the assertion is specifically a 'hasValue' restriction, the method delegates to `rule_has_value`. For other existential restrictions, the behavior depends on the configured knowledge base semantics: it invokes the corresponding solver (Lukasiewicz, Zadeh, or Classical) to handle the inference. This operation modifies the state of the knowledge base by adding or updating assertions based on the derived consequences.

        :param ass: The assertion representing an existential restriction or HasValue constraint to be processed.
        :type ass: Assertion
        """

        # HasValue restriction
        if ass.get_type() == ConceptType.HAS_VALUE:
            self.rule_has_value(ass)
        else:
            # Other existential restriction
            if constants.KNOWLEDGE_BASE_SEMANTICS == FuzzyLogic.LUKASIEWICZ:
                LukasiewiczSolver.solve_some(ass, self)
            elif constants.KNOWLEDGE_BASE_SEMANTICS == FuzzyLogic.ZADEH:
                ZadehSolver.solve_some(ass, self)
            else:
                ClassicalSolver.solve_some(ass, self)

    def rule_all(self, ass: Assertion) -> None:
        """
        Applies the universal restriction (ALL) rule to a specific assertion within the knowledge base. If the concept involved in the restriction is the Top concept, the method simplifies the assertion by directly asserting that the individual belongs to the Top concept. Otherwise, it delegates to `IndividualHandler` to add a restriction to the individual, ensuring that all fillers of the associated role satisfy the specified concept. This process modifies the state of the knowledge base by introducing new assertions or restrictions.

        :param ass: The assertion representing the universal quantification constraint to be processed.
        :type ass: Assertion
        """

        concept: AllSomeConcept = typing.cast(AllSomeConcept, ass.get_concept())

        if concept.curr_concept.type == ConceptType.TOP:
            # Concept simplification
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
        """
        This method applies the COMPLEMENTED_HAS_VALUE reasoning rule to a given assertion by extracting and processing the underlying restriction. It expects the assertion's concept to be an operator wrapping a "HasValue" restriction, from which it retrieves the specific role and value. Once extracted, the method adds a restriction to the assertion's individual using these parameters, effectively updating the knowledge base state. The operation relies on the precondition that the concept structure matches the expected `OperatorConcept` and `HasValueInterface` types.

        :param ass: The assertion representing a complemented has-value constraint to be processed. It must contain an individual and a concept that resolves to a has-value restriction.
        :type ass: Assertion
        """

        a: Individual = ass.get_individual()

        c: Concept = ass.get_concept()
        assert isinstance(c, OperatorConcept)
        c: Concept = c.get_atom()
        assert isinstance(c, HasValueInterface)

        r: str = c.role
        b: str = str(c.value)
        IndividualHandler.add_restriction(a, r, b, ass.get_lower_limit(), self)

    def compute_variables_old_calculus(self, fcc: FuzzyConcreteConcept) -> None:
        """
        Updates the internal counters for the old calculus representation based on the specific subclass of the provided fuzzy concrete concept. The method increments the `old_binary_variables` attribute by a value corresponding to the complexity of the concept shape, adding 1 for crisp concepts, 3 for left or right concepts, 4 for triangular concepts, and 5 for trapezoidal concepts. For linear concepts, it increments both `old_binary_variables` and `old_01_variables` by one. This operation directly modifies the state of the `KnowledgeBase` instance, and no action is taken if the concept type does not match one of the expected subclasses.

        :param fcc: The fuzzy concrete concept whose specific subclass dictates the increment to the old calculus variable counters.
        :type fcc: FuzzyConcreteConcept
        """

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
        """
        Executes the CONCRETE inference rule on the provided assertion, processing it to update the knowledge base state. The method extracts the associated fuzzy concrete concept and created individual, performing variable computations using the old calculus logic before attempting to solve the concept assertion. As a side effect, it increments the internal counter tracking the application of this specific rule.

        :param ass: The assertion to be processed by the CONCRETE rule, expected to contain a fuzzy concrete concept and an individual.
        :type ass: Assertion
        """

        self.rules_applied[KnowledgeBaseRules.RULE_CONCRETE] += 1
        fcc: FuzzyConcreteConcept = typing.cast(FuzzyConcreteConcept, ass.get_concept())
        self.compute_variables_old_calculus(fcc)
        ind: CreatedIndividual = typing.cast(CreatedIndividual, ass.get_individual())

        self.solve_concept_assertion(ind, fcc)
        # fcc.solve_assertion(ind, ass.get_lower_limit(), self)

    def rule_complemented_concrete(self, ass: Assertion) -> None:
        """
        Applies the COMPLEMENTED_CONCRETE inference rule to process an assertion involving a negated concrete concept. The method extracts the underlying FuzzyConcreteConcept from the assertion's OperatorConcept structure and computes the associated variables using the old calculus logic. It then delegates the resolution of the assertion to a specialized solver, utilizing the assertion's individual and lower limit. This operation also updates the internal statistics by incrementing the counter for the RULE_NOT_CONCRETE rule.

        :param ass: The assertion to be processed by the COMPLEMENTED_CONCRETE rule.
        :type ass: Assertion
        """

        self.rules_applied[KnowledgeBaseRules.RULE_NOT_CONCRETE] += 1
        c: Concept = ass.get_concept()
        assert isinstance(c, OperatorConcept)
        fcc: FuzzyConcreteConcept = typing.cast(FuzzyConcreteConcept, c.get_atom())

        self.compute_variables_old_calculus(fcc)
        ind: CreatedIndividual = typing.cast(CreatedIndividual, ass.get_individual())

        self.solve_concept_complemented_assertion(ind, ass.get_lower_limit(), c)
        # fcc.solve_complement_assertion(ind, ass.get_lower_limit(), self)

    def rule_fuzzy_number(self, ass: Assertion) -> None:
        """
        Applies the FUZZY_NUMBER rule to the specified assertion, serving as a wrapper that tracks rule usage and delegates processing. This method increments the internal counter for the FUZZY_NUMBER rule to record its application and then invokes the `rule_concrete` method to handle the assertion logic. Consequently, the primary side effect is the update to the rule application statistics, while the actual transformation or validation behavior is determined by the `rule_concrete` implementation.

        :param ass: The assertion to apply the FUZZY_NUMBER rule to.
        :type ass: Assertion
        """

        self.rules_applied[KnowledgeBaseRules.RULE_FUZZY_NUMBER] += 1
        self.rule_concrete(ass)

    def rule_complemented_fuzzy_number(self, ass: Assertion) -> None:
        """
        Applies the COMPLEMENTED_FUZZY_NUMBER rule to the specified assertion, handling the logic for negated fuzzy number values. This method updates the internal statistics by incrementing the counter associated with the RULE_NOT_FUZZY_NUMBER rule. Subsequently, it delegates the core processing to the `rule_complemented_concrete` method, passing the assertion along for further handling.

        :param ass: The assertion to apply the complemented fuzzy number rule to.
        :type ass: Assertion
        """

        self.rules_applied[KnowledgeBaseRules.RULE_NOT_FUZZY_NUMBER] += 1
        self.rule_complemented_concrete(ass)

    def rule_modified(self, ass: Assertion) -> None:
        """
        Processes an assertion involving a modified concept by applying the specific MODIFIED logic rule. It updates internal counters for variable types based on the nature of the modification: triangular modifications increment the count of 01 variables by two, while linear modifications increment both 01 and binary variable counts by one. Additionally, the method logs the application of this rule and delegates the actual resolution of the modifier relationship to the `solve_modifier_assertion` method.

        :param ass: The assertion involving a ModifiedConcept to which the MODIFIED rule is applied.
        :type ass: Assertion
        """

        mod: ModifiedConcept = typing.cast(ModifiedConcept, ass.get_concept())
        if isinstance(mod, TriangularlyModifiedConcept):
            self.old_01_variables += 2
        else:  # LinearlyModifiedConcept
            self.old_01_variables += 1
            self.old_binary_variables += 1
        self.rules_applied[KnowledgeBaseRules.RULE_MODIFIED] += 1

        self.solve_modifier_assertion(
            ass.get_individual(), mod.curr_concept, mod.modifier
        )
        # mod.solve_assertion(ass.get_individual(), ass.get_lower_limit(), self)

    def rule_complemented_modified(self, ass: Assertion) -> None:
        """
        Applies the COMPLEMENTED_MODIFIED inference rule to the provided assertion, handling the logic for concepts that are both modified and negated. It inspects the assertion's underlying concept to determine if the modification is triangular or linear, adjusting internal counters for binary and 0-1 variables accordingly to reflect the computational cost. The method then delegates the actual resolution of the constraint to the solver, updating the knowledge base state without returning a value.

        :param ass: The assertion representing a modified concept to which the COMPLEMENTED_MODIFIED rule is applied.
        :type ass: Assertion
        """

        c: Concept = ass.get_concept()
        assert isinstance(c, OperatorConcept)
        mod: ModifiedConcept = typing.cast(ModifiedConcept, c.get_atom())

        if isinstance(mod, TriangularlyModifiedConcept):
            self.old_01_variables += 1
            self.old_binary_variables += 1
        else:  # LinearlyModifiedConcept
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
        """
        Applies the BOTTOM logical rule to the provided assertion by translating it into a constraint within the underlying Mixed-Integer Linear Programming (MILP) model. Specifically, this method retrieves the variable associated with the assertion and enforces an equality constraint that sets its value to zero, effectively asserting the falsity of the statement. As a side effect, it increments the internal counter tracking the number of times this specific rule has been applied and permanently modifies the MILP model by adding the new constraint. This operation assumes that the assertion has already been registered within the MILP solver; otherwise, variable retrieval may fail.

        :param ass: The assertion to which the BOTTOM rule is applied.
        :type ass: Assertion
        """

        self.rules_applied[KnowledgeBaseRules.RULE_BOTTOM] += 1
        x_ass: Variable = self.milp.get_variable(ass)
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_ass)), InequalityType.EQUAL, 0.0
        )

    def rule_top(self, ass: Assertion) -> None:
        """
        Applies the TOP rule to the provided assertion by translating it into a constraint within the internal Mixed-Integer Linear Programming (MILP) model. This method updates the internal statistics by incrementing the application count for the TOP rule and modifies the MILP solver's state by adding a new constraint derived from the assertion with a coefficient of 1.0. The operation relies on the underlying MILP solver to handle the specifics of the constraint and does not return a value.

        :param ass: The assertion to which the TOP rule is applied.
        :type ass: Assertion
        """

        self.rules_applied[KnowledgeBaseRules.RULE_TOP] += 1
        self.milp.add_new_constraint(ass, 1.0)

    def rule_self(self, ass: Assertion) -> None:
        """
        Applies the SELF rule to the provided assertion, inferring that the individual involved is related to itself via the role specified in the assertion's concept. The method extracts the individual and the concept—asserting that the concept represents a role restriction—and explicitly adds a self-relation to the knowledge base. As a side effect, it increments the counter for the SELF rule and triggers the resolution of role inclusion axioms to handle any logical implications resulting from the new relation.

        :param ass: The assertion providing the individual and the concept defining the role for the self-relation.
        :type ass: Assertion
        """

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
        """
        This method implements the COMPLEMENTED_SELF inference rule by processing a given assertion to enforce a restriction on an individual. It extracts the individual and concept from the assertion, verifying that the concept is an `OperatorConcept` containing a role definition. If the structure is valid, it delegates to `IndividualHandler` to add a constraint ensuring the individual is not related to itself via the identified role. As a side effect, the method increments the internal counter for the `RULE_NOT_SELF` rule to track usage statistics.

        :param ass: The assertion to which the COMPLEMENTED_SELF rule is applied, containing the individual and role information necessary for the transformation.
        :type ass: Assertion
        """

        self.rules_applied[KnowledgeBaseRules.RULE_NOT_SELF] += 1
        a: Individual = ass.get_individual()
        c: Concept = ass.get_concept()
        assert isinstance(c, OperatorConcept)
        assert isinstance(c.concepts[0], HasRoleInterface)
        c: Concept = c.concepts[0]
        IndividualHandler.add_not_self_restriction(a, c.role, self)

    def rule_upper_approximation(self, ass: Assertion) -> None:
        """
        Applies the UPPER_APPROXIMATION inference rule to the provided assertion, deriving new knowledge based on the properties of an approximation concept. The method extracts the individual and the approximation concept from the input assertion, then constructs and adds a new assertion to the knowledge base. This new assertion asserts that the individual satisfies an existential restriction involving the role and current concept defined in the original approximation. Note that this method modifies the knowledge base state by adding the derived assertion and expects the input assertion's concept to be an instance of ApproximationConcept.

        :param ass: The assertion to which the upper approximation rule is applied. It must contain an `ApproximationConcept` to define the transformation logic.
        :type ass: Assertion
        """

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
        """
        Applies the LOWER_APPROXIMATION inference rule to the provided assertion, deriving a new assertion based on the properties of an ApproximationConcept. The method extracts the individual and concept from the input assertion, requiring that the concept is an instance of ApproximationConcept. It then constructs and adds a new assertion to the knowledge base where the concept is transformed into an AllSomeConcept using the role and current concept from the original approximation, while preserving the original lower limit.

        :param ass: An assertion involving an ApproximationConcept to which the lower approximation transformation is applied.
        :type ass: Assertion
        """

        a: Individual = ass.get_individual()
        con: Concept = ass.get_concept()
        assert isinstance(con, ApproximationConcept)

        self.add_assertion(
            Assertion(
                a, AllSomeConcept.all(con.role, con.curr_concept), ass.get_lower_limit()
            )
        )

    def rule_tight_upper_approximation(self, ass: Assertion) -> None:
        """
        Applies the TIGHT_UPPER_APPROXIMATION inference rule to the provided assertion, deriving a new logical consequence based on the input's structure. The method requires the assertion's concept to be an instance of ApproximationConcept; if this condition is not met, an assertion error is raised. Upon successful application, it constructs a new assertion for the same individual using a transformed concept structure—specifically, a universal restriction over an existential restriction involving the original role and current concept—and adds this new assertion to the knowledge base while preserving the original lower limit.

        :param ass: The assertion involving an ApproximationConcept to which the rule is applied.
        :type ass: Assertion
        """

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
        """
        Applies the TIGHT_LOWER_APPROXIMATION inference rule to the provided assertion, deriving a new constraint based on the properties of an approximation concept. The method extracts the individual and the concept from the input assertion, verifying that the concept is an instance of `ApproximationConcept`. It then constructs a new assertion for the same individual, where the concept is transformed into a double universal restriction involving the role and the current concept of the original approximation. This new assertion is added to the knowledge base, modifying its state. An `AssertionError` will be raised if the concept associated with the assertion is not an `ApproximationConcept`.

        :param ass: The assertion containing the individual and approximation concept to be processed by the rule.
        :type ass: Assertion
        """

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
        """
        Applies the loose upper approximation inference rule to the provided assertion, deriving a new assertion based on the properties of the approximation concept involved. The method extracts the individual and the approximation concept from the input assertion, verifying that the concept is indeed an instance of `ApproximationConcept`. It then constructs a new concept representing a double existential restriction on the role associated with the approximation concept, applied to the concept's current definition. This new assertion, which preserves the lower limit of the original assertion, is subsequently added to the knowledge base.

        :param ass: The assertion to which the rule is applied. It must contain an ApproximationConcept, which is used to derive the new assertion.
        :type ass: Assertion
        """

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
        """
        This method applies the loose lower approximation inference rule to a specific assertion, deriving new knowledge based on an approximation concept. It requires the input assertion's concept to be an instance of `ApproximationConcept`, from which it extracts the role and the underlying current concept. The method then generates a new assertion for the same individual, replacing the original concept with a nested structure defined by an existential restriction of the role followed by a universal restriction of that same role over the current concept. Finally, this derived assertion is added to the knowledge base, preserving the lower limit associated with the original assertion.

        :param ass: The assertion containing an ApproximationConcept to which the loose lower approximation rule is applied.
        :type ass: Assertion
        """

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
        """
        Applies the Gödel AND rule to the provided assertion, performing a logical conjunction based on Gödel's t-norm. This method increments the internal usage counter for the GOEDEL_AND rule as a side effect. The core logic is delegated to the ZadehSolver, which resolves the assertion and updates the state of the knowledge base.

        :param ass: The assertion to be processed using the Gödel AND rule.
        :type ass: Assertion
        """

        self.rules_applied[KnowledgeBaseRules.RULE_GOEDEL_AND] += 1
        ZadehSolver.solve_and(ass, self)

    def rule_goedel_or(self, ass: Assertion) -> None:
        """
        Applies the Gödel disjunction rule to the provided assertion, modifying the state of the knowledge base based on the logic defined in the ZadehSolver. This method serves as a wrapper that delegates the core processing to the solver while simultaneously tracking the application of rules by incrementing an internal counter for the Gödel OR operation.

        :param ass: The assertion to which the Gödel OR rule is applied.
        :type ass: Assertion
        """

        self.rules_applied[KnowledgeBaseRules.RULE_GOEDEL_OR] += 1
        ZadehSolver.solve_or(ass, self)

    def rule_lukasiewicz_and(self, ass: Assertion) -> None:
        """
        Applies the Łukasiewicz conjunction (AND) inference rule to the specified assertion, updating the internal state of the knowledge base accordingly. This method increments the usage counter for the `RULE_LUKASIEWICZ_AND` rule as a side effect to track rule application statistics. The actual logical resolution is delegated to the `LukasiewiczSolver.solve_and` method, which processes the assertion within the current context of the knowledge base.

        :param ass: The assertion to which the LUKASIEWICZ_AND logical rule is applied.
        :type ass: Assertion
        """

        self.rules_applied[KnowledgeBaseRules.RULE_LUKASIEWICZ_AND] += 1
        LukasiewiczSolver.solve_and(ass, self)

    def rule_lukasiewicz_or(self, ass: Assertion) -> None:
        """
        Applies the Łukasiewicz OR inference rule to the provided assertion, facilitating logical deduction within the knowledge base. As a side effect, this method increments the internal counter tracking the usage of this specific rule. The core logic is delegated to the LukasiewiczSolver, which processes the assertion and updates the knowledge base accordingly.

        :param ass: The assertion to which the Lukasiewicz OR rule is applied.
        :type ass: Assertion
        """

        self.rules_applied[KnowledgeBaseRules.RULE_LUKASIEWICZ_OR] += 1
        LukasiewiczSolver.solve_or(ass, self)

    def rule_goedel_implication(self, ass: Assertion) -> None:
        """
        Applies the Gödel implication inference rule to a given assertion, integrating the corresponding fuzzy logic constraints into the underlying MILP solver. The method processes an assertion containing an implication concept, decomposing it into its antecedent and consequent components, and retrieves the associated decision variables for the individual involved. It updates internal statistics tracking variable usage and rule applications, and as a side effect, recursively adds new assertions for the negation of the antecedent and the consequent to the knowledge base, applying the complement rule to the negated concept. The core operation involves adding a linear equation to the solver that mathematically represents the Gödel implication relationship between the variables representing the implication, the antecedent, and the consequent.

        :param ass: The assertion representing the implication statement to be processed. It must contain an `ImpliesConcept` defining the antecedent and consequent, which are used to generate the corresponding MILP constraints and auxiliary assertions.
        :type ass: Assertion
        """

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
        """
        Applies the Zadeh implication rule to an assertion representing a logical implication between two concepts for a specific individual. This method updates internal counters tracking variable usage and rule application statistics. It decomposes the implication into its constituent parts—specifically the antecedent, the consequent, and the negation of the antecedent—and ensures these components are added to the knowledge base as assertions. Additionally, it invokes the complement rule for the negated antecedent and imposes the necessary mathematical constraints on the MILP variables to formally define the Zadeh implication relationship within the solver.

        :param ass: The assertion representing the implication relationship to which the Zadeh implication rule is applied.
        :type ass: Assertion
        """

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
        """
        Applies the NOT_GOEDEL_IMPLIES rule to the provided assertion, handling the logical decomposition of a negated Goedel implication within the knowledge base. The method extracts the individual and the implication concept from the assertion, then adds new assertions for the antecedent and the negation of the consequent. It simultaneously updates the underlying Mixed-Integer Linear Programming (MILP) model with the necessary equations to represent the implication structure. This process modifies the internal state by incrementing counters for variable usage and rule applications, and it concludes by invoking the complemented rule handler for the individual and concept.

        :param ass: The assertion containing the Gödel implication concept to be processed.
        :type ass: Assertion
        """

        self.old_01_variables += 2
        self.old_binary_variables += 1
        self.rules_applied[KnowledgeBaseRules.RULE_NOT_GOEDEL_IMPLIES] += 1
        ind: Individual = ass.get_individual()
        # not g-implies
        c: Concept = ass.get_concept()
        assert isinstance(c, OperatorConcept)
        goedel_impl: ImpliesConcept = typing.cast(ImpliesConcept, c.get_atom())
        x_is_c: Variable = self.milp.get_variable(ind, goedel_impl)
        c1: Concept = goedel_impl.concepts[0]
        x_is_c1: Variable = self.milp.get_variable(ind, c1)
        c2: Concept = goedel_impl.concepts[1]
        x_is_c2: Variable = self.milp.get_variable(ind, c2)
        not_c2: Concept = -c2
        x_is_not_c2: Variable = self.milp.get_variable(ind, not_c2)
        self.add_assertion(ind, c1, DegreeVariable.get_degree(x_is_c1))
        self.add_assertion(ind, not_c2, DegreeVariable.get_degree(x_is_not_c2))
        ZadehSolver.goedel_implies_equation(x_is_c, x_is_c1, x_is_c2, self.milp)

        self.rule_complemented(ind, c)

    def rule_complemented_zadeh_implication(self, ass: Assertion) -> None:
        """
        Applies the NOT_ZADEH_IMPLIES rule to the provided assertion, decomposing a Zadeh implication into its logical components and enforcing the necessary constraints within the MILP solver. It extracts the individual and the implication concept, retrieves the corresponding variables for the antecedent and consequent, and adds new assertions for the antecedent and the negation of the consequent. The method also updates internal statistics regarding variable usage and rule applications, and recursively invokes the complemented rule processing for the individual and concept.

        :param ass: The assertion representing the complemented Zadeh implication to be decomposed into linear constraints.
        :type ass: Assertion
        """

        self.old_01_variables += 2
        self.old_binary_variables += 1
        self.rules_applied[KnowledgeBaseRules.RULE_NOT_ZADEH_IMPLIES] += 1
        ind: Individual = ass.get_individual()
        # not z-implies
        c: Concept = ass.get_concept()
        assert isinstance(c, OperatorConcept)
        z_impl: ImpliesConcept = typing.cast(ImpliesConcept, c.get_atom())
        x_is_c: Variable = self.milp.get_variable(ind, z_impl)
        c1: Concept = z_impl.concepts[0]
        x_is_c1: Variable = self.milp.get_variable(ind, c1)
        c2: Concept = z_impl.concepts[1]
        x_is_c2: Variable = self.milp.get_variable(ind, c2)
        not_c2: Concept = -c2
        x_is_not_c2: Variable = self.milp.get_variable(ind, not_c2)
        self.add_assertion(ind, c1, DegreeVariable.get_degree(x_is_c1))
        self.add_assertion(ind, not_c2, DegreeVariable.get_degree(x_is_not_c2))
        ZadehSolver.zadeh_implies_equation(x_is_c, x_is_c1, x_is_c2, self.milp)

        self.rule_complemented(ind, c)

    def rule_positive_threshold(self, ass: Assertion) -> None:
        """
        This method enforces the POSITIVE THRESHOLD rule for a given assertion by translating logical requirements into Mixed Integer Linear Programming (MILP) constraints. It retrieves the individual and the threshold concept from the assertion, then introduces a new binary variable to the MILP model to act as a switch for the threshold condition. The method adds a new assertion linking the individual to the underlying concept and invokes a helper function to establish common constraints. Finally, it appends two specific linear inequalities to the MILP model to mathematically enforce the relationship between the individual's membership degree, the threshold weight, and the binary variable. As a side effect, this method increments internal counters for binary variables and applied rules, and modifies the state of the MILP solver by adding variables and constraints.

        :param ass: The assertion representing the threshold relationship to be encoded as constraints in the model.
        :type ass: Assertion
        """

        self.old_binary_variables += 1
        self.rules_applied[KnowledgeBaseRules.RULE_THRESHOLD] += 1
        i: Individual = ass.get_individual()
        tc: ThresholdConcept = typing.cast(ThresholdConcept, ass.get_concept())
        x_a_in_tc: Variable = self.milp.get_variable(i, tc)
        c: Concept = tc.curr_concept
        x_a_in_c: Variable = self.milp.get_variable(i, c)
        x: float = tc.weight
        # a : C >= x_{C}
        self.add_assertion(i, c, DegreeVariable.get_degree(x_a_in_c))
        y: Variable = self.milp.get_new_variable(VariableType.BINARY)
        # Rules independent of the x
        self.rule_threshold_common(x_a_in_c, x_a_in_tc, y)
        # x_{v:C} < y + x
        self.milp.add_new_constraint(
            Expression(-x + ConfigReader.EPSILON, Term(-1.0, y), Term(1.0, x_a_in_c)),
            InequalityType.LESS_THAN,
        )
        # x_{v:[\geq x] \; C} + (1-y) \geq x
        self.milp.add_new_constraint(
            Expression(1.0 - x, Term(1.0, x_a_in_tc), Term(-1.0, y)),
            InequalityType.GREATER_THAN,
        )

    def rule_threshold_common(
        self, x_a_in_c: Variable, x_a_in_tc: Variable, y: Variable
    ) -> None:
        """
        This method adds three linear constraints to the internal Mixed-Integer Linear Programming (MILP) model to enforce the logical relationship between a concept membership variable, a threshold concept variable, and a binary selector variable. The constraints are formulated such that if the binary variable is active (1), the threshold concept variable is forced to equal the concept variable; if the binary variable is inactive (0), the threshold concept variable is forced to zero. This mechanism is used to model the conditional activation of a threshold concept within the knowledge base, modifying the optimization problem's feasible region.

        :param x_a_in_c: The variable representing the degree to which the individual belongs to the concept.
        :type x_a_in_c: Variable
        :param x_a_in_tc: The variable representing the degree to which the individual belongs to the threshold concept.
        :type x_a_in_tc: Variable
        :param y: A binary variable acting as a switch that controls the activation of the threshold relationship between the concept and the threshold concept.
        :type y: Variable
        """

        # x_{v:[\geq x] \; C} \leq x_{v:C} + (1-y)
        self.milp.add_new_constraint(
            Expression(-1.0, Term(1.0, x_a_in_tc), Term(-1.0, x_a_in_c), Term(1.0, y)),
            InequalityType.LESS_THAN,
        )
        # x_{v:[\leq x] \; C} + (1-y) \geq x_{v:C}
        self.milp.add_new_constraint(
            Expression(1.0, Term(1.0, x_a_in_tc), Term(-1.0, x_a_in_c), Term(-1.0, y)),
            InequalityType.GREATER_THAN,
        )
        # x_{v:[\geq x] \; C} \leq y
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_a_in_tc), Term(-1.0, y)), InequalityType.LESS_THAN
        )

    def rule_complemented_positive_threshold(self, ass: Assertion) -> None:
        """
        Applies the COMPLEMENTED POSITIVE THRESHOLD rule to the provided assertion, updating internal statistics to reflect the transformation. Specifically, this method increments the counters for old 01 variables by two, old binary variables by one, and the specific rule application count for RULE_NOT_THRESHOLD. The actual logic for handling the assertion is delegated to the `rule_complemented_complex_assertion` method.

        :param ass: The assertion to which the complemented positive threshold rule is applied.
        :type ass: Assertion
        """

        self.old_01_variables += 2
        self.old_binary_variables += 1
        self.rules_applied[KnowledgeBaseRules.RULE_NOT_THRESHOLD] += 1
        self.rule_complemented_complex_assertion(ass)

    def rule_negative_threshold(self, ass: Assertion) -> None:
        """
        Enforces the logic of a negative threshold constraint on the provided assertion, translating semantic requirements regarding an individual's membership degree into linear constraints within the underlying Mixed Integer Linear Programming (MILP) model. It extracts the individual and the threshold concept from the assertion, creates a new binary auxiliary variable, and establishes inequalities that link the individual's degree in the concept to the threshold weight. This process involves adding a new assertion to the knowledge base and registering specific constraints with the MILP solver to ensure the threshold condition is met. As a side effect, the method updates internal counters tracking the total number of binary variables used and the frequency of rule applications.

        :param ass: The assertion to which the negative threshold rule is applied, providing the individual and threshold concept necessary for constraint generation.
        :type ass: Assertion
        """

        self.old_01_variables += 1
        self.rules_applied[KnowledgeBaseRules.RULE_THRESHOLD] += 1
        i: Individual = ass.get_individual()
        tc: ThresholdConcept = typing.cast(ThresholdConcept, ass.get_concept())
        x_a_in_tc: Variable = self.milp.get_variable(i, tc)
        c: Concept = tc.curr_concept
        x_a_in_c: Variable = self.milp.get_variable(i, c)
        x: float = tc.weight
        # a : C >= x_{C}
        self.add_assertion(Assertion(i, c, DegreeVariable.get_degree(x_a_in_c)))
        y: Variable = self.milp.get_new_variable(VariableType.BINARY)
        # Rules independent of the x
        self.rule_threshold_common(x_a_in_c, x_a_in_tc, y)
        # x_{v:C} + 2y > x
        self.milp.add_new_constraint(
            Expression(-x - ConfigReader.EPSILON, Term(2.0, y), Term(1.0, x_a_in_c)),
            InequalityType.GREATER_THAN,
        )
        # x_{v:[\leq x] \; C} \leq x + (1-y)
        self.milp.add_new_constraint(
            Expression(-1.0 - x, Term(1.0, x_a_in_tc), Term(1.0, y)),
            InequalityType.LESS_THAN,
        )

    def rule_complemented_negative_threshold(self, ass: Assertion) -> None:
        """
        Applies the COMPLEMENTED NEGATIVE THRESHOLD rule to the provided assertion, updating internal statistics to track the transformation's impact on variable counts. Specifically, this method increments the counters for old 01 variables and old binary variables, and records that this specific rule has been applied. The actual logic for handling the assertion is delegated to the `rule_complemented_complex_assertion` method.

        :param ass: The assertion to which the COMPLEMENTED NEGATIVE THRESHOLD rule is applied.
        :type ass: Assertion
        """

        self.old_01_variables += 2
        self.old_binary_variables += 1
        self.rules_applied[KnowledgeBaseRules.RULE_NOT_THRESHOLD] += 1
        self.rule_complemented_complex_assertion(ass)

    def rule_extended_positive_threshold(self, ass: Assertion) -> None:
        """
        Applies the EXTENDED POSITIVE THRESHOLD rule to the provided assertion, which involves an `ExtThresholdConcept`. This method retrieves the MILP variables associated with the individual, the threshold concept, and its underlying base concept, then recursively adds an assertion for the base concept to ensure its constraints are enforced. To model the threshold logic, it introduces a new binary auxiliary variable and adds specific linear constraints to the MILP model that link the individual's membership degrees in the base and extended concepts with the threshold weight. As side effects, the method increments internal counters tracking the total number of binary variables generated and the frequency with which this rule has been applied.

        :param ass: The assertion representing the individual and extended threshold concept to be processed by this rule.
        :type ass: Assertion
        """

        self.old_01_variables += 1
        self.rules_applied[KnowledgeBaseRules.RULE_THRESHOLD] += 1
        i: Individual = ass.get_individual()
        tc: ExtThresholdConcept = typing.cast(ExtThresholdConcept, ass.get_concept())
        x_a_in_tc: Variable = self.milp.get_variable(i, tc)
        c: Concept = tc.curr_concept
        x_a_in_c: Variable = self.milp.get_variable(i, c)
        x: Variable = tc.weight_variable
        # a : C >= x_{C}
        self.add_assertion(Assertion(i, c, DegreeVariable.get_degree(x_a_in_c)))
        y: Variable = self.milp.get_new_variable(VariableType.BINARY)
        # Rules independent of the x
        self.rule_threshold_common(x_a_in_c, x_a_in_tc, y)
        # x_{v:C} < y + x
        self.milp.add_new_constraint(
            Expression(
                ConfigReader.EPSILON,
                Term(-1.0, x),
                Term(-1.0, y),
                Term(1.0, x_a_in_c),
            ),
            InequalityType.LESS_THAN,
        )
        # x_{v:[\geq x] \; C} + (1-y) \geq x
        self.milp.add_new_constraint(
            Expression(1.0, Term(-1.0, x), Term(1.0, x_a_in_tc), Term(-1.0, y)),
            InequalityType.GREATER_THAN,
        )

    def rule_complemented_extended_positive_threshold(self, ass: Assertion) -> None:
        """
        Applies the COMPLEMENTED EXTENDED POSITIVE THRESHOLD rule to the provided assertion, delegating the actual transformation logic to the `rule_complemented_complex_assertion` method. As part of this operation, the method updates internal tracking metrics to reflect the computational cost of the rule: it increments the count of old 01 variables by two, increments the count of old binary variables by one, and logs the application of the RULE_NOT_THRESHOLD rule. This method modifies the state of the knowledge base in place and does not return a value.

        :param ass: The assertion to which the rule is applied.
        :type ass: Assertion
        """

        self.old_01_variables += 2
        self.old_binary_variables += 1
        self.rules_applied[KnowledgeBaseRules.RULE_NOT_THRESHOLD] += 1
        self.rule_complemented_complex_assertion(ass)

    def rule_extended_negative_threshold(self, ass: Assertion) -> None:
        """
        Applies the EXTENDED NEGATIVE THRESHOLD rule to the provided assertion, translating the logical relationship into Mixed-Integer Linear Programming (MILP) constraints. The method extracts the individual and the extended threshold concept from the assertion, retrieves the corresponding MILP variables for the individual's membership in the extended and base concepts, and the threshold value itself. It introduces a new binary variable to model the logical condition, adds a derived assertion for the base concept, and invokes common threshold logic before adding specific linear constraints that link the membership degrees, the threshold, and the binary variable. This process modifies the MILP model by adding new variables and constraints and updates internal counters for binary variables and applied rules.

        :param ass: The assertion representing the individual and extended threshold concept to be processed by the rule.
        :type ass: Assertion
        """

        self.old_binary_variables += 1
        self.rules_applied[KnowledgeBaseRules.RULE_THRESHOLD] += 1
        i: Individual = ass.get_individual()
        tc: ExtThresholdConcept = typing.cast(ExtThresholdConcept, ass.get_concept())
        x_a_in_tc: Variable = self.milp.get_variable(i, tc)
        c: Concept = tc.curr_concept
        x_a_in_c: Variable = self.milp.get_variable(i, c)
        x: Variable = tc.weight_variable
        # a : C >= x_{C}
        self.add_assertion(Assertion(i, c, DegreeVariable.get_degree(x_a_in_c)))
        y: Variable = self.milp.get_new_variable(VariableType.BINARY)
        # Rules independent of the x
        self.rule_threshold_common(x_a_in_c, x_a_in_tc, y)
        # x_{v:C} + 2y > x
        self.milp.add_new_constraint(
            Expression(
                -ConfigReader.EPSILON,
                Term(-1.0, x),
                Term(2.0, y),
                Term(1.0, x_a_in_c),
            ),
            InequalityType.GREATER_THAN,
        )
        # x_{v:[\leq x] \; C} \leq x + (1-y)
        self.milp.add_new_constraint(
            Expression(-1.0, Term(-1.0, x), Term(1.0, x_a_in_tc), Term(1.0, y)),
            InequalityType.LESS_THAN,
        )

    def rule_complemented_extended_negative_threshold(self, ass: Assertion) -> None:
        """
        Applies the COMPLEMENTED EXTENDED NEGATIVE THRESHOLD rule to the provided assertion, updating internal counters to reflect the cost of this transformation. Specifically, it increments the count of old 01 variables by two and old binary variables by one, and logs the application of the RULE_NOT_THRESHOLD rule. The actual processing of the assertion is delegated to the `rule_complemented_complex_assertion` method.

        :param ass: The assertion instance to which the complemented extended negative threshold rule is applied.
        :type ass: Assertion
        """

        self.old_01_variables += 2
        self.old_binary_variables += 1
        self.rules_applied[KnowledgeBaseRules.RULE_NOT_THRESHOLD] += 1
        self.rule_complemented_complex_assertion(ass)

    def rule_weighted_concept(self, ass: Assertion) -> None:
        """
        Processes an assertion involving a weighted concept by establishing the mathematical relationship between the weighted concept and its underlying base concept within the mixed-integer linear programming (MILP) model. It extracts the individual and the weighted concept from the provided assertion, then adds a linear constraint equating the individual's membership in the weighted concept to the product of the weight and the individual's membership in the base concept. Additionally, the method adds a new assertion to the knowledge base regarding the individual's membership in the base concept and increments the internal counter for the number of times this rule has been applied.

        :param ass: The assertion containing the individual and weighted concept to be processed by the rule.
        :type ass: Assertion
        """

        self.rules_applied[KnowledgeBaseRules.RULE_WEIGHTED] += 1
        i: Individual = ass.get_individual()
        wc: WeightedConcept = typing.cast(WeightedConcept, ass.get_concept())
        x_a_in_wc: Variable = self.milp.get_variable(i, wc)
        c: Concept = wc.curr_concept
        x_a_in_c: Variable = self.milp.get_variable(i, c)
        w: float = wc.weight
        # a : C >= x_{C}
        self.add_assertion(Assertion(i, c, DegreeVariable.get_degree(x_a_in_c)))
        # x_{WC} = w x_{C}
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_a_in_wc), Term(-w, x_a_in_c)), InequalityType.EQUAL
        )

    def rule_complemented_weighted_concept(self, ass: Assertion) -> None:
        """
        Applies the COMPLEMENTED WEIGHTED CONCEPT rule to the provided assertion, integrating the logic into the knowledge base's MILP model. This method expects the assertion's concept to be an operator concept wrapping a weighted concept, and it proceeds to extract the individual, the weight, and the underlying base concept. It adds a new assertion to the knowledge base linking the individual to the complement of the base concept and enforces a linear constraint that equates the weighted concept's variable to the weight multiplied by the base concept's variable. As a side effect, the method updates the internal counter for this rule and recursively invokes the complemented rule processing to ensure logical consistency.

        :param ass: The assertion containing the individual and weighted concept to be processed by the rule.
        :type ass: Assertion
        """

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
        # a : not C >= x_{not C}
        self.add_assertion(Assertion(i, not_c, DegreeVariable.get_degree(x_a_in_not_c)))
        # x_{WC} = w x_{C}
        self.milp.add_new_constraint(
            Expression(Term(1.0, x_a_in_wc), Term(-w, x_a_in_c)), InequalityType.EQUAL
        )
        self.rule_complemented(i, c)

    def rule_complemented_complex_assertion(self, ass: Assertion) -> None:
        """
        Applies the COMPLEMENTED COMPLEX ASSERTION inference rule to the provided assertion to derive a new constraint involving the logical complement of the assertion's concept. It extracts the individual and the negated concept, retrieves the corresponding variable from the internal MILP model, and invokes the `rule_complemented` logic for the pair. As a side effect, the method adds a new assertion to the knowledge base that links the individual and the complemented concept to the degree of the retrieved variable, effectively formalizing the relationship where the assertion's degree is bounded by the variable's value.

        :param ass: The assertion to be processed, providing the individual and concept used to generate a new assertion with a complemented concept.
        :type ass: Assertion
        """

        i: Individual = ass.get_individual()
        c: Concept = -ass.get_concept()
        x: Variable = self.milp.get_variable(i, c)
        self.rule_complemented(i, c)
        # a : C >= x_{C}
        self.add_assertion(Assertion(i, c, DegreeVariable.get_degree(x)))

    def rule_complemented(self, i: Individual, c: Concept) -> None:
        """
        Enforces the logical constraint that a specific individual must belong to exactly one of a given concept or its complement. It retrieves the decision variables corresponding to the individual for both the concept and its negation from the underlying MILP model. The method then adds an equality constraint to the model ensuring that the sum of these two variables equals one, thereby preventing the individual from being simultaneously classified as both the concept and its negation, or neither.

        :param i: The individual entity for which the complementarity constraint is enforced.
        :type i: Individual
        :param c: The concept for which the complementarity constraint is enforced, ensuring the individual belongs to either this concept or its complement.
        :type c: Concept
        """

        x: Variable = self.milp.get_variable(i, c)
        c2: Concept = -c
        x2: Variable = self.milp.get_variable(i, c2)
        self.milp.add_new_constraint(
            Expression(1.0, Term(-1.0, x), Term(-1.0, x2)), InequalityType.EQUAL
        )

    def rule_weighted_sum(self, ass: Assertion) -> None:
        """
        Applies the WEIGHTED SUM rule to the provided assertion to resolve weighted sum constraints within the knowledge base. The method updates internal statistics by incrementing the counter for this specific rule and adjusting the tally of legacy binary variables based on the number of constituent concepts involved. It assumes the assertion's concept is a `WeightedSumConcept` and delegates the actual resolution logic to the `solve_concept_assertion` method.

        :param ass: The assertion containing the weighted sum concept to be processed.
        :type ass: Assertion
        """

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
        """
        Applies the COMPLEMENTED WEIGHTED SUM inference rule to the provided assertion, facilitating the resolution of constraints involving weighted sums. The method validates that the assertion's concept is an OperatorConcept wrapping a WeightedSumConcept before proceeding. It updates internal statistics regarding the number of variables processed and the usage count of this specific rule. The core logic is delegated to `solve_concept_complemented_assertion`, which modifies the knowledge base state to satisfy the assertion.

        :param ass: The assertion containing the WeightedSumConcept to which the rule is applied.
        :type ass: Assertion
        """

        c: Concept = ass.get_concept()
        assert isinstance(c, OperatorConcept)
        ws: WeightedSumConcept = typing.cast(WeightedSumConcept, c.get_atom())

        n: int = len(ws.concepts)
        self.old_01_variables += n
        self.rules_applied[KnowledgeBaseRules.RULE_NOT_W_SUM] += 1

        # ws.solve_complemented_assertion(ass.get_individual(), self)
        self.solve_concept_complemented_assertion(ass.get_individual(), None, c)

    def rule_weighted_sum_zero(self, ass: Assertion) -> None:
        """
        Applies the WEIGHTED SUM ZERO rule to the provided assertion, updating internal tracking metrics and delegating the resolution logic. Specifically, it increments the usage counter for this rule type and updates the count of old 01 variables based on the number of concepts involved in the weighted sum. The method then invokes `solve_concept_assertion` to process the assertion using the associated individual and the specific weighted sum concept.

        :param ass: The assertion representing the weighted sum zero concept to be processed.
        :type ass: Assertion
        """

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
        """
        Applies the COMPLEMENTED WEIGHTED SUM ZERO inference rule to the provided assertion, specifically targeting assertions involving a weighted sum zero concept wrapped in an operator. The method verifies that the assertion's concept is an `OperatorConcept` containing a `WeightedSumZeroConcept` as its atom, raising an error if these structural conditions are not met. As a side effect, it increments the internal statistics counter for this rule and delegates the actual resolution of the assertion to the `solve_concept_complemented_assertion` method.

        :param ass: The assertion to which the COMPLEMENTED WEIGHTED SUM ZERO rule is applied.
        :type ass: Assertion
        """

        c: Concept = ass.get_concept()
        assert isinstance(c, OperatorConcept)
        assert isinstance(c.get_atom(), WeightedSumZeroConcept)

        self.rules_applied[KnowledgeBaseRules.RULE_NOT_W_SUM_ZERO] += 1
        # wsz.solve_complemented_assertion(ass.get_individual(), self)
        self.solve_concept_complemented_assertion(ass.get_individual(), None, c)

    def rule_weighted_min(self, ass: Assertion) -> None:
        """
        Applies the WEIGHTED MIN inference rule to the provided assertion to resolve or evaluate its associated individual. This method retrieves the concept encapsulated by the assertion, treating it as a WeightedMinConcept, and delegates the actual solving logic to the `solve_concept_assertion` method. As a side effect, it increments the internal usage counter for the WEIGHTED MIN rule, tracking how often this specific rule has been invoked within the knowledge base.

        :param ass: The assertion to be processed by the WEIGHTED MIN rule.
        :type ass: Assertion
        """

        self.rules_applied[KnowledgeBaseRules.RULE_W_MIN] += 1
        # typing.cast(WeightedMinConcept, ass.get_concept()).solve_assertion(
        #     ass.get_individual(), self
        # )
        self.solve_concept_assertion(
            ass.get_individual(), typing.cast(WeightedMinConcept, ass.get_concept())
        )

    def rule_complemented_weighted_min(self, ass: Assertion) -> None:
        """
        Applies the COMPLEMENTED WEIGHTED MIN inference rule to the provided assertion, facilitating the resolution of logical constraints involving weighted minimum operations under negation. The method strictly validates the input structure, requiring the assertion's concept to be an `OperatorConcept` that encapsulates a `WeightedMinConcept`; failure to meet these criteria results in an assertion error. Upon execution, it updates the internal statistics by incrementing the counter for this specific rule and triggers the underlying solving logic by invoking `solve_concept_complemented_assertion` with the assertion's individual and concept.

        :param ass: The assertion to be processed by the complemented weighted min rule.
        :type ass: Assertion
        """

        c: Concept = ass.get_concept()
        assert isinstance(c, OperatorConcept)
        assert isinstance(c.get_atom(), WeightedMinConcept)

        self.rules_applied[KnowledgeBaseRules.RULE_NOT_W_MIN] += 1
        # wm.solve_complemented_assertion(ass.get_individual(), self)
        self.solve_concept_complemented_assertion(ass.get_individual(), None, c)

    def rule_weighted_max(self, ass: Assertion) -> None:
        """
        Applies the WEIGHTED MAX inference rule to the specified assertion within the knowledge base. This method increments the internal counter tracking the usage of this specific rule. It subsequently delegates the resolution logic by extracting the individual from the assertion and invoking the general concept solver with the assertion's concept cast to a `WeightedMaxConcept`.

        :param ass: The assertion to be processed by the weighted max rule.
        :type ass: Assertion
        """

        self.rules_applied[KnowledgeBaseRules.RULE_W_MAX] += 1
        # typing.cast(WeightedMaxConcept, ass.get_concept()).solve_assertion(
        #     ass.get_individual(), self
        # )
        self.solve_concept_assertion(
            ass.get_individual(), typing.cast(WeightedMaxConcept, ass.get_concept())
        )

    def rule_complemented_weighted_max(self, ass: Assertion) -> None:
        """
        Applies the COMPLEMENTED WEIGHTED MAX inference rule to the specified assertion, handling cases where a weighted maximum concept is negated. The method validates that the assertion's concept is an `OperatorConcept` containing a `WeightedMaxConcept` as its atom. As a side effect, it increments the usage counter for this rule within the knowledge base and delegates the actual resolution of the complemented assertion to the `solve_concept_complemented_assertion` method.

        :param ass: The assertion containing a WeightedMaxConcept to be processed by the complemented weighted max rule.
        :type ass: Assertion
        """

        c: Concept = ass.get_concept()
        assert isinstance(c, OperatorConcept)
        assert isinstance(c.get_atom(), WeightedMaxConcept)

        self.rules_applied[KnowledgeBaseRules.RULE_NOT_W_MAX] += 1
        # wm.solve_complemented_assertion(ass.get_individual(), self)
        self.solve_concept_complemented_assertion(ass.get_individual(), None, c)

    def rule_owa(self, ass: Assertion) -> None:
        """
        Applies the Ordered Weighted Averaging (OWA) rule to the provided assertion, updating internal solver statistics and delegating the resolution logic. It calculates the number of constituent concepts within the OWA concept to increment the counters for 0-1 and binary variables, which track the resources required for the underlying solver. The method also records the application of this rule and triggers the resolution of the concept assertion for the associated individual.

        :param ass: The assertion containing an OWA concept to which the rule is applied.
        :type ass: Assertion
        """

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
        """
        Applies the COMPLEMENTED Ordered Weighted Averaging (OWA) rule to the provided assertion, specifically handling cases where the assertion's concept is an OperatorConcept containing an OwaConcept atom. This method updates internal counters for 0-1 and binary variables based on the number of concepts involved in the OWA operator and increments the statistics for the `RULE_NOT_OWA` rule application. It subsequently delegates the actual resolution of the assertion to the `solve_concept_complemented_assertion` method.

        :param ass: The assertion containing the OWA concept and individual to which the Complemented OWA rule is applied.
        :type ass: Assertion
        """

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
        """
        Executes the Quantified Ordered Weighted Averaging (OWA) inference rule on the specified assertion to update the knowledge base. This method processes the assertion by extracting the associated individual and concept—specifically cast to a `QowaConcept`—and delegating the resolution to the `solve_concept_complemented_assertion` method. As a side effect, it increments the internal counter tracking the number of times this specific rule has been applied. The operation modifies the state of the knowledge base and assumes that the input assertion contains a concept compatible with the Quantified OWA logic.

        :param ass: The assertion containing the individual and concept to be processed by the Quantified OWA rule.
        :type ass: Assertion
        """

        self.rules_applied[KnowledgeBaseRules.RULE_OWA] += 1
        # typing.cast(QowaConcept, ass.get_concept()).solve_complemented_assertion(
        #     ass.get_individual(), self
        # )

        self.solve_concept_complemented_assertion(
            ass.get_individual(), None, typing.cast(QowaConcept, ass.get_concept())
        )

    def rule_complemented_quantified_owa(self, ass: Assertion) -> None:
        """
        Applies the Complemented Quantified Ordered Weighted Averaging (OWA) rule to the provided assertion. This method updates the internal tracking statistics to record that the rule has been executed and subsequently delegates the actual processing logic to the `rule_complemented_complex_assertion` method. The operation is primarily a side-effecting procedure that modifies the state of the knowledge base's rule counters and potentially the assertion structure through the delegated call.

        :param ass: The assertion to which the complemented quantified OWA rule is applied.
        :type ass: Assertion
        """

        self.rules_applied[KnowledgeBaseRules.RULE_NOT_OWA] += 1
        self.rule_complemented_complex_assertion(ass)

    def rule_choquet(self, ass: Assertion) -> None:
        """
        Applies the Choquet Integral inference rule to the provided assertion, facilitating the evaluation or resolution of concepts involving Choquet integrals within the knowledge base. Upon invocation, this method increments the internal statistics counter tracking the usage of the Choquet Integral rule. It extracts the individual and the specific concept from the assertion—casting the concept to `ChoquetIntegral`—and delegates the actual solving logic to the `solve_concept_assertion` method. This operation assumes that the assertion's concept is compatible with the Choquet Integral structure; otherwise, the type casting may result in runtime errors.

        :param ass: The assertion to which the Choquet Integral rule is applied.
        :type ass: Assertion
        """

        self.rules_applied[KnowledgeBaseRules.RULE_CHOQUET_INTEGRAL] += 1
        # typing.cast(ChoquetIntegral, ass.get_concept()).solve_assertion(
        #     ass.get_individual(), self
        # )
        self.solve_concept_assertion(
            ass.get_individual(), typing.cast(ChoquetIntegral, ass.get_concept())
        )

    def rule_complemented_choquet(self, ass: Assertion) -> None:
        """
        Applies the COMPLEMENTED CHOQUET INTEGRAL rule to the provided assertion, handling the logic for negated Choquet integral expressions. The method validates that the assertion's concept is an `OperatorConcept` containing a `ChoquetIntegral` atom, ensuring the structure matches the rule's requirements. As a side effect, it increments the internal counter tracking the application of this rule and delegates the actual resolution of the complemented assertion to the `solve_concept_complemented_assertion` method.

        :param ass: The assertion object to be processed by the Complemented Choquet Integral rule.
        :type ass: Assertion
        """

        c: Concept = ass.get_concept()
        assert isinstance(c, OperatorConcept)
        assert isinstance(c.get_atom(), ChoquetIntegral)

        self.rules_applied[KnowledgeBaseRules.RULE_NOT_CHOQUET_INTEGRAL] += 1
        # ci.solve_complemented_assertion(ass.get_individual(), self)

        self.solve_concept_complemented_assertion(ass.get_individual(), None, c)

    def rule_sugeno(self, ass: Assertion) -> None:
        """
        Applies the Sugeno Integral inference rule to the provided assertion, facilitating the evaluation of fuzzy measures or integrals associated with a specific individual. The method extracts the individual and the concept from the assertion, explicitly treating the concept as a SugenoIntegral, and delegates the computational logic to the `solve_concept_assertion` method. As a side effect, this operation increments the internal counter tracking the application of the Sugeno Integral rule within the knowledge base's statistics. It assumes that the assertion's concept is compatible with the SugenoIntegral type; passing an assertion with an incompatible concept type may lead to errors during the resolution phase.

        :param ass: The assertion to be processed, containing the SugenoIntegral concept and individual required for evaluation.
        :type ass: Assertion
        """

        self.rules_applied[KnowledgeBaseRules.RULE_SUGENO_INTEGRAL] += 1
        # typing.cast(SugenoIntegral, ass.get_concept()).solve_assertion(
        #     ass.get_individual(), self
        # )
        self.solve_concept_assertion(
            ass.get_individual(), typing.cast(SugenoIntegral, ass.get_concept())
        )

    def rule_complemented_sugeno(self, ass: Assertion) -> None:
        """
        Applies the COMPLEMENTED SUGENO INTEGRAL inference rule to the provided assertion, facilitating the resolution of assertions involving Sugeno integrals under negation. The method first validates that the assertion's concept is an `OperatorConcept` containing a `SugenoIntegral` atom, raising an error if these structural requirements are not met. As a side effect, it increments the internal counter tracking the application of this specific rule and delegates the actual resolution logic to the `solve_concept_complemented_assertion` method, passing the relevant individual and concept data.

        :param ass: The assertion containing a Sugeno Integral concept to which the complemented rule is applied.
        :type ass: Assertion
        """

        c: Concept = ass.get_concept()
        assert isinstance(c, OperatorConcept)
        assert isinstance(c.get_atom(), SugenoIntegral)

        self.rules_applied[KnowledgeBaseRules.RULE_NOT_SUGENO_INTEGRAL] += 1
        # si.solve_complemented_assertion(ass.get_individual(), self)
        self.solve_concept_complemented_assertion(ass.get_individual(), None, c)

    def rule_quasi_sugeno(self, ass: Assertion) -> None:
        """
        Applies the Quasi-Sugeno Integral inference rule to the provided assertion to evaluate the associated fuzzy logic concept. It extracts the individual and the concept from the assertion, casting the concept to the specific Quasi-Sugeno Integral type, and delegates the actual resolution to the knowledge base's `solve_concept_assertion` method. This process updates the internal state of the knowledge base and increments the usage counter for the Quasi-Sugeno Integral rule.

        :param ass: The assertion containing the individual and the Quasi-Sugeno Integral concept to be evaluated.
        :type ass: Assertion
        """

        self.rules_applied[KnowledgeBaseRules.RULE_QUASI_SUGENO_INTEGRAL] += 1
        # typing.cast(QsugenoIntegral, ass.get_concept()).solve_assertion(
        #     ass.get_individual(), self
        # )
        self.solve_concept_assertion(
            ass.get_individual(), typing.cast(QsugenoIntegral, ass.get_concept())
        )

    def rule_complemented_quasi_sugeno(self, ass: Assertion) -> None:
        """
        Applies the Complemented Quasi-Sugeno Integral inference rule to the provided assertion, specifically handling cases where the assertion involves a negated Quasi-Sugeno Integral concept. The method verifies that the assertion's concept is an `OperatorConcept` wrapping a `QsugenoIntegral` atom before proceeding. It updates the internal statistics tracking rule application and delegates the actual resolution logic to `solve_concept_complemented_assertion`, which modifies the state of the knowledge base regarding the individual associated with the assertion.

        :param ass: The assertion to which the complemented Quasi-Sugeno integral rule is applied.
        :type ass: Assertion
        """

        c: Concept = ass.get_concept()
        assert isinstance(c, OperatorConcept)
        assert isinstance(c.get_atom(), QsugenoIntegral)

        self.rules_applied[KnowledgeBaseRules.RULE_NOT_QUASI_SUGENO_INTEGRAL] += 1
        # qsi.solve_complemented_assertion(ass.get_individual(), self)
        self.solve_concept_complemented_assertion(ass.get_individual(), None, c)

    def rule_complemented_at_most_datatype_restriction(
        self, b: CreatedIndividual, ass: Assertion
    ) -> None:
        """
        Applies the inference rule for complemented 'at most' datatype restrictions to the provided assertion and individual, handling the logical consequences of negated data property cardinality constraints. The core reasoning logic is delegated to the `DatatypeReasoner.apply_not_at_most_value_rule` method, which modifies the knowledge base state accordingly. Additionally, this method increments the internal counter for `RULE_NOT_DATATYPE`, serving as a side effect to track the frequency of rule application during the reasoning process.

        :param b: The individual instance serving as the subject of the assertion.
        :type b: CreatedIndividual
        :param ass: The assertion to which the complemented at most datatype restriction rule is applied.
        :type ass: Assertion
        """

        self.rules_applied[KnowledgeBaseRules.RULE_NOT_DATATYPE] += 1
        DatatypeReasoner.apply_not_at_most_value_rule(b, ass, self)

    def rule_complemented_at_least_datatype_restriction(
        self, b: CreatedIndividual, ass: Assertion
    ) -> None:
        """
        Applies the reasoning rule for complemented "at least" datatype restrictions to the specified individual and assertion. This method updates the internal statistics by incrementing the counter for the `RULE_NOT_DATATYPE` rule and delegates the actual logical processing to the `DatatypeReasoner`. The delegation ensures that the knowledge base state is modified according to the semantics of negated minimum cardinality constraints on data properties.

        :param b: The individual subject to the complemented at least datatype restriction rule.
        :type b: CreatedIndividual
        :param ass: The assertion representing the complemented at least datatype restriction to be processed.
        :type ass: Assertion
        """

        self.rules_applied[KnowledgeBaseRules.RULE_NOT_DATATYPE] += 1
        DatatypeReasoner.apply_not_at_least_value_rule(b, ass, self)

    def rule_complemented_exact_datatype_restriction(
        self, b: CreatedIndividual, ass: Assertion
    ) -> None:
        """
        Applies the COMPLEMENTED EXACT DATATYPE RESTRICTION inference rule to the specified individual and assertion. This method processes constraints where a data property value is explicitly negated or restricted to be different from a specific literal. As a side effect, it increments the internal statistics counter for the `RULE_NOT_DATATYPE` rule to track reasoning progress. The actual logic is delegated to the `DatatypeReasoner`, which updates the knowledge base state based on the provided inputs.

        :param b: The individual to which the complemented exact datatype restriction assertion applies.
        :type b: CreatedIndividual
        :param ass: The assertion to which the complemented exact datatype restriction rule is applied.
        :type ass: Assertion
        """

        self.rules_applied[KnowledgeBaseRules.RULE_NOT_DATATYPE] += 1
        DatatypeReasoner.apply_not_exact_value_rule(b, ass, self)

    def rule_sigma_concept(self, ass: Assertion) -> None:
        """
        Applies the SIGMA CONCEPT rule to the provided assertion by translating it into constraints within the underlying Mixed-Integer Linear Programming (MILP) model. The method creates a new continuous variable to represent the count of individuals related to the assertion's subject via a specific role that satisfy a target concept. If the sigma concept does not explicitly define a set of individuals to evaluate, the method defaults to using all named individuals available in the knowledge base. It then establishes a cardinality constraint to calculate this count and applies a fuzzy modifier to link the result to the truth value of the assertion. As a side effect, this method increments the internal counter tracking the application of this specific rule.

        :param ass: The assertion representing the SigmaConcept to be processed by the rule.
        :type ass: Assertion
        """

        self.rules_applied[KnowledgeBaseRules.RULE_SIGMA_COUNT] += 1
        x_sigma: Variable = self.milp.get_new_variable(VariableType.CONTINUOUS)
        sigma: SigmaConcept = typing.cast(SigmaConcept, ass.get_concept())
        i1: Individual = ass.get_individual()
        inds: typing.Optional[list[Individual]] = sigma.get_individuals()
        if inds is None or len(inds) == 0:
            inds = self.get_named_individuals()
        c: Concept = sigma.get_concept()
        r: str = sigma.get_role()
        self.milp.add_cardinality_list(SigmaCount(x_sigma, i1, inds, r, c))

        x_ass: Variable = self.milp.get_variable(ass)
        d: FuzzyConcreteConcept = sigma.get_fuzzy_concept()

        # xAss = d (x_sigma)
        self.__add_fuzzy_concrete_concept_equation(d, x_sigma, x_ass)

    def rule_complemented_sigma_concept(self, ass: Assertion) -> None:
        """
        Applies the COMPLEMENTED SIGMA CONCEPT inference rule to the provided assertion object. This method serves as a specific handler for the rule, incrementing the internal statistics counter for `RULE_NOT_SIGMA_COUNT` to track how often this rule has been utilized. The actual logical processing and transformation of the assertion are delegated to the `rule_complemented_complex_assertion` method, which handles the underlying mechanics of the operation. The function modifies the knowledge base's internal state regarding rule application metrics but does not return a value.

        :param ass: The assertion to be processed by the COMPLEMENTED SIGMA CONCEPT rule.
        :type ass: Assertion
        """

        self.rules_applied[KnowledgeBaseRules.RULE_NOT_SIGMA_COUNT] += 1
        self.rule_complemented_complex_assertion(ass)

    def set_crisp_concept(self, c: Concept) -> None:
        """
        Registers a specific concept as a crisp (binary) entity within the underlying Mixed-Integer Linear Programming (MILP) model. This method converts the provided Concept object to a string representation and delegates the registration to the internal MILP solver, effectively modifying the model's constraints or variable definitions to treat the concept discretely rather than fuzzily. As a side effect, the internal state of the solver is updated immediately. The method does not return a value and relies on the internal solver to handle the validity of the string identifier.

        :param c: The concept to be defined as crisp.
        :type c: Concept
        """

        self.milp.add_crisp_concept(str(c))

    def set_crisp_role(self, role_name: str) -> None:
        """
        Designates a specific role within the knowledge base as "crisp," indicating that the role should be treated as a binary or definitive entity rather than a fuzzy one. This method updates the internal state of the underlying Mixed-Integer Linear Programming (MILP) model by registering the role, which affects how constraints or variables associated with this role are processed during optimization. The function does not return a value, and its primary side effect is the modification of the solver's configuration to enforce crisp logic for the specified role.

        :param role_name: The name of the role to be defined as crisp.
        :type role_name: str
        """

        self.milp.add_crisp_role(role_name)

    def set_dynamic_blocking(self) -> None:
        """Enables dynamic blocking for the knowledge base instance by setting the `blocking_dynamic` attribute to True. This method directly modifies the internal state to activate the dynamic blocking strategy. It does not return a value and unconditionally applies the setting regardless of the current blocking configuration."""

        self.blocking_dynamic = True

    def is_crisp_role(self, role_name: str) -> bool:
        """
        Determines whether the specified role is crisp, meaning it adheres to binary truth values rather than fuzzy degrees. If the knowledge base is currently operating under classical logic semantics, the method returns True for any role name, as classical logic does not support fuzziness. In fuzzy logic contexts, the method delegates the check to the internal MILP solver to determine if the specific role is explicitly defined as crisp. This method performs a read-only operation and does not modify the state of the knowledge base.

        :param role_name: The name of the role to check for crispness.
        :type role_name: str

        :return: True if the role is crisp, which is the case if the global semantics are classical or the role is explicitly defined as crisp.

        :rtype: bool
        """

        return (
            constants.KNOWLEDGE_BASE_SEMANTICS == FuzzyLogic.CLASSICAL
            or self.milp.is_crisp_role(role_name)
        )

    def is_crisp_concept(self, concept_name: str) -> bool:
        """
        Determines whether a specific concept is defined as crisp (binary) or fuzzy within the knowledge base. The method returns True if the global knowledge base semantics are set to classical logic, which implies that all concepts are crisp regardless of their individual definitions. If the system operates under fuzzy logic semantics, the method delegates the check to the underlying MILP model to determine if the specific concept is crisp. This function performs a read-only check and does not alter the state of the knowledge base.

        :param concept_name: The name of the concept to check for crispness.
        :type concept_name: str

        :return: True if the knowledge base uses classical logic semantics or if the specific concept is crisp; otherwise, false.

        :rtype: bool
        """

        return (
            constants.KNOWLEDGE_BASE_SEMANTICS == FuzzyLogic.CLASSICAL
            or self.milp.is_crisp_concept(concept_name)
        )

    def is_atomic_crisp_concept(self, c: Concept) -> bool:
        """
        Determines whether a given concept is both atomic and crisp within the context of the knowledge base. A concept is considered atomic if it is a fundamental, non-composed entity, and crisp if it possesses a binary truth value rather than a fuzzy or graded membership. This method performs a conjunction of checks, verifying the concept's internal atomicity alongside a lookup in the knowledge base based on the concept's string representation. The operation is read-only and does not modify the state of the concept or the knowledge base.

        :param c: The concept to evaluate for atomicity and crispness.
        :type c: Concept

        :return: True if the concept is both atomic and crisp, False otherwise.

        :rtype: bool
        """

        return c.is_atomic() and self.is_crisp_concept(str(c))

    def optimize(self, e: Expression) -> Solution:
        """
        Orchestrates the optimization of a given expression by configuring and invoking the internal Mixed-Integer Linear Programming (MILP) solver. Depending on the active knowledge base semantics, specifically when using Classical logic, the method enforces binary variable constraints before applying internal transformation rules and resolving cardinality constraints for pending tasks. Upon completion, it triggers a side effect of displaying optimization statistics and returns the computed optimal solution.

        :param e: The expression representing the objective function or target formula to be optimized.
        :type e: Expression

        :return: The optimal solution for the given expression, computed by the underlying MILP solver.

        :rtype: Solution
        """

        if constants.KNOWLEDGE_BASE_SEMANTICS == FuzzyLogic.CLASSICAL:
            self.milp.set_binary_variables()
        self.rule_n2()
        self.rule_n3()

        # Sigma-count pending tasks
        self.solve_cardinality_list()

        sol: Solution = self.milp.optimize(e)
        self.show_statistics()
        return sol

    def solve_cardinality_list(self) -> None:
        """Iterates through the list of cardinality constraints defined in the associated MILP model to resolve pending sigma-count tasks. For each constraint in the collection, the method extracts the relevant variables, individuals, roles, and concepts, and delegates the actual resolution logic to the internal `__solve_cardinality` helper. This process modifies the internal state of the model or knowledge base to satisfy the cardinality constraints, and performs no operation if the list of cardinalities is empty."""

        for sc in self.milp.cardinalities:
            self.__solve_cardinality(
                sc.get_variable(),
                sc.get_individual(),
                sc.get_individuals(),
                sc.get_role(),
                sc.get_concept(),
            )

    def __solve_cardinality(
        self, x_sigma: Variable, i1: Individual, O: list[Individual], r: str, C: Concept
    ) -> None:
        """
        This method constructs the constraints required to compute the sigma count (cardinality) of a set defined by a specific role and concept. It iterates through the list of candidate individuals `O`, processing only those for which a relation variable exists between the subject `i1` and the candidate via the role `r`. For each valid candidate, it creates a new variable representing the logical conjunction of the relation's truth value and the candidate's membership in the concept `C`, adding the appropriate fuzzy logic constraints (Lukasiewicz or Zadeh) to the solver. The method has the side effect of populating the MILP solver with these new variables and equations, ultimately linking the target variable `x_sigma` to the sum of the calculated conjunctions.

        :param x_sigma: Free variable representing the sigma count of the conjunctions between the relation and concept membership for the candidate individuals.
        :type x_sigma: Variable
        :param i1: The individual acting as the subject of the relation `r`.
        :type i1: Individual
        :param O: The set of candidate individuals to be considered as the object of the relation.
        :type O: list[Individual]
        :param r: Name of the role or relation connecting the subject individual to the candidates.
        :type r: str
        :param C: Concept representing the restriction applied to the objects of the relation, used to evaluate the membership degree of candidate individuals.
        :type C: Concept
        """

        # kb is needed to get the semantics and to use the method addSigmaCountEquation
        xw_in_Ci: list[Variable] = list()
        for i2 in O:
            # Only for known r-fillers, the relation must already exist!
            if self.milp.exists_variable(i1, i2, r):
                x_ass: Variable = self.milp.get_variable(i1, i2, r)
                xw_in_C: Variable = self.milp.get_variable(i2, C)
                x_and: Variable = self.milp.get_new_variable(
                    VariableType.SEMI_CONTINUOUS
                )

                xw_in_Ci.append(x_and)

                # xAnd = xwInC \otimes xAss
                if constants.KNOWLEDGE_BASE_SEMANTICS == FuzzyLogic.LUKASIEWICZ:
                    LukasiewiczSolver.and_equation(x_and, xw_in_C, x_ass)
                else:
                    ZadehSolver.and_equation(x_and, xw_in_C, x_ass)

        # xSigma = cardinality(xwInCi)
        self.__add_sigma_count_equation(x_sigma, xw_in_Ci)

    def __add_sigma_count_equation(
        self, x_sigma: Variable, xw_in_Ci: list[Variable]
    ) -> None:
        """
        This method constructs and adds a linear equality constraint to the internal MILP model to enforce a sigma count relationship. It creates an expression representing the sum of the variables in `xw_in_Ci` and constrains this sum to be equal to the degree of the `x_sigma` variable. If the provided list of variables is empty, the method exits without adding any constraints.

        :param x_sigma: The variable representing the sum or count of the concept variables, used as the target value for the constraint.
        :type x_sigma: Variable
        :param xw_in_Ci: A list of variables representing the elements within the concept that are summed to determine the sigma count.
        :type xw_in_Ci: list[Variable]
        """

        n: int = len(xw_in_Ci)
        if n <= 0:
            return
        terms: list[Term] = [None] * n
        for i in range(n):
            terms[i] = Term(1.0, xw_in_Ci[i])
        self.milp.add_new_constraint(
            Expression(*terms),
            InequalityType.EQUAL,
            DegreeVariable.get_degree(x_sigma),
        )

    def show_statistics(self) -> None:
        """Prints a comprehensive summary of the knowledge base's internal state and processing metrics to the debug output. The report categorizes information into sections detailing the processed TBox (such as synonyms, definitions, inclusions, and domain/range restrictions), the Tableau (including the number of individuals, assertions, and maximal forest depth), and the specific reasoning rules applied during the session. Additionally, it displays statistics regarding variables used in the old calculus. This method is read-only and serves as a diagnostic tool to inspect the composition and reasoning history of the knowledge base."""

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
        """
        Calculates the total number of domain restrictions currently stored in the knowledge base. This is achieved by iterating over the internal `domain_restrictions` mapping and summing the lengths of the collections associated with each key. The method performs a read-only operation and returns zero if no restrictions are defined.

        :return: The total number of domain restrictions.

        :rtype: int
        """

        return sum(len(s) for s in self.domain_restrictions.values())

    def get_number_of_range_restrictions(self) -> int:
        """
        Calculates the total number of range restrictions currently defined in the knowledge base by summing the lengths of the restriction collections associated with each entity. This method provides a global count of all individual range constraints stored in the internal `range_restrictions` mapping. It performs a read-only operation and returns zero if the knowledge base contains no range restrictions.

        :return:

        :rtype: int
        """

        return sum(len(s) for s in self.range_restrictions.values())

    def add_negated_equations(self, i: Individual, c: Concept) -> None:
        """
        Adds constraints to the knowledge base that define the mathematical relationship between a concept and its negation for a specific individual. Specifically, it enforces the equation $x_{v:C} = 1 - x_{v:\neg C}$, ensuring that the membership variables for the concept and its complement sum to one. This logic is applied selectively based on the concept type, targeting existential restrictions, universal restrictions, top and bottom concepts, and value restrictions (including their negations). The actual constraint generation is delegated to the `rule_complemented` method, which modifies the internal state of the knowledge base.

        :param i: The individual entity for which the negation equation is being added.
        :type i: Individual
        :param c: The concept for which to add the constraint linking the concept to its negation.
        :type c: Concept
        """

        if c.type in (
            ConceptType.SOME,
            ConceptType.ALL,
            ConceptType.TOP,
            ConceptType.BOTTOM,
            ConceptType.HAS_VALUE,
        ) or OperatorConcept.is_not_has_value(c):
            self.rule_complemented(i, c)

    def is_concrete_type(self, c: Concept) -> bool:
        """
        Determines whether the provided concept belongs to the category of concrete types, including specific numeric variations and their logical negations. The method returns true if the concept's type is explicitly defined as CONCRETE or FUZZY_NUMBER. It also returns true if the concept represents a logical complement of these types, identified through checks for negation operators on concrete or fuzzy number types.

        :param c: The concept to evaluate for concrete type, fuzzy number, or their complements.
        :type c: Concept

        :return: True if the concept is a concrete type, a fuzzy number, or a complement of either; otherwise False.

        :rtype: bool
        """

        return (
            c.type in (ConceptType.CONCRETE, ConceptType.FUZZY_NUMBER)
            or OperatorConcept.is_not_concrete(c)
            or OperatorConcept.is_not_fuzzy_number(c)
        )

    def has_only_crisp_sub_concepts(self, c: Concept) -> bool:
        """
        Determines whether the provided concept is composed exclusively of atomic crisp concepts as defined by the knowledge base. This method iterates through the immediate sub-concepts of the input concept and verifies that each one satisfies the criteria for being an atomic crisp concept. If any sub-concept fails this verification, the method returns False; otherwise, it returns True. The method requires the input concept to implement the HasConceptsInterface to access its constituent concepts.

        :param c: The concept to verify is composed only of crisp concepts.
        :type c: Concept

        :return: True if the provided concept is composed exclusively of crisp sub-concepts, False otherwise.

        :rtype: bool
        """

        assert isinstance(c, HasConceptsInterface)

        for ci in c.concepts:
            if not self.is_atomic_crisp_concept(ci):
                return False
        return True

    def is_classified(self) -> bool:
        """
        Determines whether the knowledge base has been subjected to a classification process, verifying if its entries have been categorized or labeled. It returns a boolean flag indicating the current state, which can be used to ensure that operations requiring a classified structure are only performed after the necessary processing has occurred.

        :return: True if the knowledge base has already been classified, False otherwise.

        :rtype: bool
        """

        return False

    def classify(self) -> None:
        """Analyzes the items within the knowledge base to assign them to specific categories or classes based on their inherent properties. This operation is intended to modify the internal state of the knowledge base by updating metadata or tags associated with the stored entities, which can improve organization and retrieval efficiency. Note that this method is currently a stub and does not perform any actual processing or state changes."""

        pass

    def get_classification_node(name: str) -> typing.Optional[ClassificationNode]:
        """
        Retrieves a specific classification node from the knowledge base by matching the provided name against existing node identifiers. It performs a lookup operation to locate the node associated with the given string, returning the corresponding ClassificationNode object if a match is found. If no node with the specified name exists within the knowledge base, the method returns None. This operation is read-only and does not modify the underlying data structure.

        :param name: The name of the classification node to retrieve.
        :type name: str

        :return: The ClassificationNode corresponding to the provided name, or None if no match is found.

        :rtype: typing.Optional[ClassificationNode]
        """

        return None

    def get_subsumption_flags(a: ClassificationNode, b: ClassificationNode) -> float:
        """
        Retrieves the numerical value representing the subsumption flags associated with the relationship between two classification nodes. This method evaluates the structural or logical connection between the first node and the second node, returning a float that encodes specific properties or a confidence score regarding the subsumption hierarchy. The result is typically used to inform classification decisions or to query the state of the relationship within the knowledge base.

        :param a: The first classification node involved in the subsumption flags calculation.
        :type a: ClassificationNode
        :param b: The classification node to compare against the first node to determine subsumption properties.
        :type b: ClassificationNode

        :return: The subsumption flags value representing the relationship between the two classification nodes.

        :rtype: float
        """

        return 0.0

    def get_number_from_concept(self, concept_name: str) -> int:
        """
        Retrieves the unique integer identifier associated with a given concept name by checking the internal mapping. If the concept name is not already present, the method generates a new identifier equal to the current size of the mapping, stores this new association, and returns the identifier. This process has the side effect of mutating the internal state of the knowledge base by adding new entries for previously unseen concepts.

        :param concept_name: The string label representing the concept to be encoded into a unique integer.
        :type concept_name: str

        :return: The unique integer identifier assigned to the concept name. If the concept is new, a new identifier is generated; otherwise, the existing identifier is returned.

        :rtype: int
        """

        number: int = self.number_of_concepts.get(concept_name)
        if number is None:
            value: int = len(self.number_of_concepts)
            self.number_of_concepts[concept_name] = value
            return value
        return number

    def get_concept_from_number(self, n: int) -> typing.Optional[str]:
        """
        Performs a reverse lookup to find the concept name corresponding to a given numerical value. The method searches the internal mapping of concept names to their counts for a value that matches the input integer. If a match is found, the associated concept name is returned; otherwise, the method returns None to indicate that no such concept exists.

        :param n: The numeric count used to identify the concept name.
        :type n: int

        :return: The concept name associated with the given number, or None if no such concept exists.

        :rtype: typing.Optional[str]
        """

        for name, count in self.number_of_concepts.items():
            if count == n:
                return name
        return None

    def mark_process_assertion(self, ass: Assertion) -> None:
        """
        Marks the provided assertion as processed by registering its unique identifier in the knowledge base's internal tracking set. The method retrieves the integer representation of the assertion from the associated MILP solver and adds it to the collection of processed assertions. This operation modifies the internal state of the knowledge base and is idempotent, meaning marking an already processed assertion again will not change the state.

        :param ass: The assertion object to be marked as processed.
        :type ass: Assertion
        """

        n: int = self.milp.get_number_for_assertion(ass)
        Util.debug(f"Add assertion to processed_assertions: {n}")
        self.processed_assertions.add(n)

    def is_assertion_processed(self, ass: Assertion) -> bool:
        """
        Verifies whether a specific assertion has already been handled by the system. It retrieves the unique identifier associated with the assertion from the MILP interface and checks for its presence in the collection of processed assertion identifiers. This method performs a read-only check and does not modify the state of the knowledge base or the underlying solver.

        :param ass: The assertion to verify for prior processing.
        :type ass: Assertion

        :return: True if the assertion has already been processed, False otherwise.

        :rtype: bool
        """

        return self.milp.get_number_for_assertion(ass) in self.processed_assertions

    def represent_tbox_with_gcis(self) -> None:
        """Consolidates various terminological axioms, such as synonyms, concept subsumptions, equivalences, and disjointness constraints, into a unified set of General Concept Inclusions (GCIs) stored within the knowledge base. The method iterates through internal axiom collections to construct specific inclusion rules, appropriately handling fuzzy logic degrees and logic operators; for instance, equivalences are decomposed into bidirectional inclusions, and disjointness is modeled using the bottom concept. Once the GCI list is populated, the method applies these inferences to all known individuals and resolves domain and range constraints, resulting in a comprehensive update to the knowledge base's internal state."""

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
        # tG contains disjointConcepts
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
        """Outputs a detailed, formatted representation of the TBox (Terminological Box) component of the knowledge base to the debug stream. This method iterates over internal data structures to display concept inclusions, definitions, synonyms, domain and range restrictions, disjointness axioms, and general concept inclusions. The output is organized into labeled sections with specific formatting, such as indentation and separators, to enhance readability. While the method does not modify the state of the knowledge base, it generates side effects by logging information via the `Util.debug` utility. Additionally, the logic for displaying synonyms includes a filter to prevent duplicate entries based on string comparison."""

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
    """The DatatypeReasoner class encapsulates the logic for translating logical assertions involving concrete data types—such as integers, floats, booleans, and triangular fuzzy numbers—into constraints for a Mixed-Integer Linear Programming (MILP) solver. It acts as a bridge between the knowledge base's semantic layer and the mathematical optimization layer, managing the creation of auxiliary individuals and variables required to represent data properties. The class provides specific reasoning rules for handling simple numeric comparisons, arithmetic feature functions, and fuzzy number memberships, as well as their negations. By generating the appropriate linear inequalities and variable bounds, it enables the system to reason about concrete feature values and their relationships within a fuzzy logic framework."""

    @staticmethod
    def get_feature(f_name: str, kb: KnowledgeBase) -> ConcreteFeature:
        """
        Looks up and returns a specific concrete feature definition from the provided knowledge base based on the supplied name. This method acts as an accessor to the knowledge base's internal registry of concrete features. If the requested feature name does not exist within the knowledge base, the function invokes an error handling routine to report the undefined feature, effectively terminating the lookup process.

        :param f_name: The unique name identifying the concrete feature to be retrieved.
        :type f_name: str
        :param kb: The knowledge base instance containing the concrete features to be queried.
        :type kb: KnowledgeBase

        :return: The ConcreteFeature object corresponding to the specified name.

        :rtype: ConcreteFeature
        """

        t = kb.concrete_features.get(f_name)
        if t is None:
            Util.error(f"Error: Concrete feature {f_name} is not defined")
        return t

    @staticmethod
    def get_bounds(t: ConcreteFeature) -> typing.Optional[list[float]]:
        """
        Retrieves the lower and upper bounds associated with a concrete feature, returning them as a list of floating-point numbers. For integer features, the bounds are explicitly converted to floats to maintain type consistency. If the input feature is boolean, the method returns None, as boolean types do not define numerical bounds.

        :param t: The concrete feature object whose lower and upper bounds are to be retrieved.
        :type t: ConcreteFeature

        :return: The lower and upper bounds of the feature as a list of two floats, or None if the feature is boolean.

        :rtype: typing.Optional[list[float]]
        """

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
        """
        This method ensures the existence of an individual representing a concrete feature connected to a source individual via a specific role, retrieving the associated MILP variables in the process. If the role relation is already present, the existing target individual is utilized; otherwise, a new concrete individual is instantiated and the relation is established within the knowledge base. It retrieves a binary variable associated with the feature selection and a variable representing the feature's value. When a new individual is created and specific bounds are provided, the method applies range constraints to the value variable relative to the binary variable. The function returns a list containing the target individual, the value variable, and the binary variable.

        :param ind: The source individual used to retrieve an existing related individual or create a new one, along with the associated variables.
        :type ind: Individual
        :param role: The role defining the relationship between the source individual and the created or retrieved individual.
        :type role: str
        :param t: The concrete feature instance for which the associated individual and variables are retrieved or created, used to derive the feature name and generate the corresponding variable.
        :type t: ConcreteFeature
        :param k: A list of two floats representing the lower and upper bounds used to restrict the range of the concrete feature's variable.
        :type k: list[float]
        :param kb: The knowledge base used to access and manage individuals, variables, and constraints.
        :type kb: KnowledgeBase

        :return: A list where the first element is the retrieved or created individual, the second is the variable representing the feature's value, and the third is the binary variable representing the feature's existence.

        :rtype: list[typing.Any]
        """

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
        """
        This static method enforces the reasoning rule for negations or inequalities involving a triangular fuzzy number by adding constraints to the knowledge base's MILP solver. It first determines a representative individual that serves as a boundary reference point for the fuzzy number, specifically using a 'greater than or equal to' logic. The method then asserts that this representative individual satisfies the fuzzy number concept. Subsequently, it constructs and writes a linear equation to the solver that connects the variables of the original individual, the representative individual, and the fuzzy number, effectively encoding the logical relationship defined by the provided inequality type and bounds. This process modifies the internal state of the MILP model by introducing new constraints and variables.

        :param b: The created individual instance to which the rule is applied.
        :type b: CreatedIndividual
        :param kb: The knowledge base managing the MILP model, variables, and concept assertions required for the rule application.
        :type kb: KnowledgeBase
        :param f_name: The name of the concrete feature.
        :type f_name: str
        :param x_b: The variable representing the created individual within the mathematical model.
        :type x_b: Variable
        :param x_f: The variable representing the concrete feature's value.
        :type x_f: Variable
        :param x_is_c: Binary variable indicating whether the concrete feature is of a specific type.
        :type x_is_c: Variable
        :param n: The triangular fuzzy number instance used to derive the representative individual and variables for the rule.
        :type n: TriangularFuzzyNumber
        :param k: The lower and upper bounds defining the interval of the concrete feature.
        :type k: list[float]
        :param type: Specifies the inequality relation (e.g., less than or greater than) to apply when formulating the constraint for the non-triangular fuzzy number.
        :type type: InequalityType
        """

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
        """
        Encodes the logical constraints for a triangular fuzzy number inequality into the Mixed-Integer Linear Programming (MILP) model maintained by the knowledge base. The method retrieves a representative individual that serves as a boundary for the specified inequality type and asserts that this representative satisfies the fuzzy number concept. It then establishes a constraint linking the original individual's type certainty variable to the membership degree of the representative. Finally, the method generates the specific linear equation relating the individual's value, the feature variable, and the representative's value, thereby integrating the fuzzy number logic into the solver's constraints.

        :param b: The created individual entity serving as the subject for the triangular fuzzy number rule application.
        :type b: CreatedIndividual
        :param kb: The knowledge base containing the individuals, fuzzy numbers, and MILP model context used to retrieve variables, solve assertions, and add constraints.
        :type kb: KnowledgeBase
        :param f_name: The name of the concrete feature associated with the individual.
        :type f_name: str
        :param x_b: The variable representing the created individual within the mathematical model.
        :type x_b: Variable
        :param x_f: The variable representing the concrete feature.
        :type x_f: Variable
        :param x_is_c: The variable representing the degree of membership or truth value that the concrete feature is of the specific type associated with the fuzzy number.
        :type x_is_c: Variable
        :param n: The triangular fuzzy number representing the concept or value to be asserted and used to derive the representative individual.
        :type n: TriangularFuzzyNumber
        :param type: Specifies the inequality relation to apply when constructing the fuzzy number equation.
        :type type: InequalityType
        """

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
        """
        This method implements the reasoning logic for a feature function by decomposing it into its constituent sub-features and integrating them into the Mixed-Integer Linear Programming (MILP) model. It iterates through the features associated with the function, verifying or creating the necessary individuals and variables within the knowledge base. If a specific feature relation does not exist for the individual, the method generates a new concrete individual, establishes the relation, and applies range constraints based on the feature's defined bounds. It enforces logical dependencies by adding constraints that link the main feature's type indicator to the binary variables of the sub-features. Finally, it delegates the construction of the mathematical equation representing the feature function to a separate handler.

        :param ind: The individual entity serving as the subject for the rule, whose features and relations are processed to generate constraints and variables.
        :type ind: Individual
        :param t: The concrete feature associated with the feature function, defining the datatype (integer or continuous) for the resulting variables.
        :type t: ConcreteFeature
        :param fun: The feature function defining the rule to be applied, providing the set of features involved in the relationship.
        :type fun: FeatureFunction
        :param kb: The knowledge base serving as the central context for the rule application, providing access to the MILP solver, variable management, and the ontology definitions.
        :type kb: KnowledgeBase
        :param x_b: The variable representing the value of the individual in the MILP model.
        :type x_b: Variable
        :param x_is_c: The decision variable representing the activation of the concrete feature for the individual.
        :type x_is_c: Variable
        :param x_f: The decision variable representing the feature function in the MILP model.
        :type x_f: Variable
        :param k: The lower and upper bounds defining the valid range for the concrete feature.
        :type k: list[float]
        :param type: Specifies the inequality operator (e.g., less than or equal) to apply when constructing the feature equation constraint.
        :type type: InequalityType
        """

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
    ) -> None:
        """
        Adds linear constraints to the Mixed-Integer Linear Programming (MILP) solver within the provided KnowledgeBase to encode a fuzzy number relationship between the specified variables. The method employs a Big-M formulation to conditionally enforce the specified inequality type between the concrete feature `x_b` and the modified concrete feature `x_b_prime`, using the feature variable `x_f` as a control switch. If the inequality type is `EQUAL`, the method recursively adds constraints for both `GREATER_THAN` and `LESS_THAN` to enforce equality. Furthermore, it ensures that the variable `x_b_prime` is bounded within the limits defined by `MAXVAL` to maintain the integrity of the optimization model.

        :param x_f: The variable representing the feature function, acting as a control to activate the inequality constraint between the concrete features.
        :type x_f: Variable
        :param x_b: The variable representing the original concrete feature value.
        :type x_b: Variable
        :param x_b_prime: The variable representing the modified concrete feature used to define the fuzzy number constraints.
        :type x_b_prime: Variable
        :param type: Specifies the inequality relation to enforce, determining the specific constraints added to the model.
        :type type: InequalityType
        :param kb: The knowledge base instance to which the generated fuzzy number constraints are added.
        :type kb: KnowledgeBase
        """

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
    ) -> None:
        """
        Adds linear constraints to the Mixed-Integer Linear Programming (MILP) model within the knowledge base to enforce a specific inequality relationship between an individual and a feature function. The method constructs a degree expression from the feature function and applies a Big-M formulation to link the individual variable and the feature function variable based on the specified inequality type. When the inequality type is equality, the method recursively enforces both greater-than and less-than constraints. Additionally, it applies fixed upper and lower bounds to the degree expression to ensure it remains within a valid numerical range.

        :param ind: The individual for which the feature equation is being generated.
        :type ind: Individual
        :param fun: The feature function for which to write the equation.
        :type fun: FeatureFunction
        :param x_b: The variable representing the individual in the constraint system.
        :type x_b: Variable
        :param x_is_c: Variable indicating whether the concrete feature is of a specific type.
        :type x_is_c: Variable
        :param x_f: The variable representing the feature function, used to construct the constraints linking the individual variable to the feature's degree expression.
        :type x_f: Variable
        :param k: The lower and upper bounds defining the range of the concrete feature.
        :type k: list[float]
        :param type: Specifies the direction of the inequality constraint to apply, determining the mathematical relationship enforced on the feature equation.
        :type type: InequalityType
        :param kb: The knowledge base providing the MILP model and context for adding the feature equation constraints.
        :type kb: KnowledgeBase
        """

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
        """
        Applies a simple restriction rule by adding linear constraints to the knowledge base's MILP solver to enforce a relationship between a binary variable `x_b` and a feature variable `x_f` relative to a threshold `n`. The method handles different inequality types by decomposing an EQUAL constraint into GREATER_THAN and LESS_THAN components. It utilizes a big-M formulation to construct these constraints, ensuring the logical consistency of the restriction within the optimization model. If the threshold `n` is a Variable, the method also adds bounding constraints to `n`. Note that the arguments `x_is_c` and `k` are currently unused in the implementation.

        :param n: The numeric constant or variable acting as the threshold or bound for the simple restriction.
        :type n: typing.Any
        :param kb: The knowledge base containing the MILP solver to which the restriction constraints are added.
        :type kb: KnowledgeBase
        :param x_b: The variable representing the individual involved in the restriction.
        :type x_b: Variable
        :param x_is_c: Variable representing the condition that the concrete feature is of a specific type.
        :type x_is_c: Variable
        :param x_f: The variable representing the value of the concrete feature being restricted.
        :type x_f: Variable
        :param k: The bounds of the concrete feature.
        :type k: list[float]
        :param type: Specifies the inequality relation (e.g., less than, greater than, or equal) to enforce for the restriction.
        :type type: InequalityType
        """

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
        """
        This static method applies a reasoning rule to an assertion representing a "HasValue" restriction, translating it into constraints within the knowledge base's Mixed-Integer Linear Programming (MILP) model. It validates that the assertion's concept implements the `HasValueInterface`, retrieves the corresponding concrete feature, and generates or retrieves variables for the assertion, the role filler, and the individual. The method establishes a fundamental constraint linking the assertion variable to the role filler variable and updates the knowledge base's binary variable counter. Subsequently, it dispatches to specialized sub-routines based on the type of the value associated with the restriction—handling triangular fuzzy numbers, feature functions, boolean values, or simple numeric restrictions—to apply the specific inequality logic defined by the `type` parameter.

        :param ass: The assertion representing the individual and concept pair to which the rule is applied.
        :type ass: Assertion
        :param kb: The knowledge base containing the assertion and the MILP model to which the rule's constraints are added.
        :type kb: KnowledgeBase
        :param type: Specifies the inequality relation (e.g., less than, greater than) to enforce on the assertion's value during constraint generation.
        :type type: InequalityType
        """

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
        """
        Applies the "at least" value rule to a specific assertion within the provided knowledge base, enforcing a constraint that the assertion's value must satisfy a lower bound. This method delegates the core logic to the generic rule application handler, specifying that the relationship type to be processed is a strict greater-than inequality. As a side effect, the knowledge base is modified to include any new inferences or constraints derived from applying this rule to the assertion.

        :param ass: The assertion within the knowledge base to which the "at least" value constraint rule is applied.
        :type ass: Assertion
        :param kb: The knowledge base containing the assertion and serving as the context for the rule application.
        :type kb: KnowledgeBase
        """

        DatatypeReasoner.apply_rule(ass, kb, InequalityType.GREATER_THAN)

    @staticmethod
    def apply_at_most_value_rule(ass: Assertion, kb: KnowledgeBase) -> None:
        """
        This static method applies the "at most" value constraint rule to a specific assertion within the provided knowledge base. It delegates the core logic to a generic rule application function, explicitly passing the "less than" inequality type to define the constraint relationship. The operation updates the knowledge base by propagating the logical consequences of the assertion, ensuring that the system's state reflects the restrictions imposed by the upper bound rule.

        :param ass: The assertion to which the "at most" value constraint is applied.
        :type ass: Assertion
        :param kb: The knowledge base containing the assertion to which the rule is applied.
        :type kb: KnowledgeBase
        """

        DatatypeReasoner.apply_rule(ass, kb, InequalityType.LESS_THAN)

    @staticmethod
    def apply_exact_value_rule(ass: Assertion, kb: KnowledgeBase) -> None:
        """
        Applies the specific reasoning rule associated with exact value constraints to the provided assertion within the context of the given knowledge base. This method delegates to the general rule application logic, specifically invoking it with the equality inequality type to enforce that the assertion's value must strictly match a specific target. The operation modifies the state of the knowledge base in-place, potentially updating the assertion's status or adding new derived information based on the exact value constraint.

        :param ass: The assertion to which the exact value rule is applied.
        :type ass: Assertion
        :param kb: The knowledge base containing the assertion and serving as the context for the rule application.
        :type kb: KnowledgeBase
        """

        DatatypeReasoner.apply_rule(ass, kb, InequalityType.EQUAL)

    @staticmethod
    def get_xb(b: CreatedIndividual, t: ConcreteFeature, kb: KnowledgeBase) -> Variable:
        """
        This static method retrieves the optimization variable associated with a specific individual and concrete feature within the provided knowledge base. It determines the variable type by inspecting the concrete feature's type: if the feature is an integer, it returns an integer variable from the underlying MILP solver; otherwise, it returns a continuous variable. This function effectively bridges the logical representation of individuals and features with their mathematical counterparts in the optimization model.

        :param b: The individual entity for which the associated variable is to be retrieved.
        :type b: CreatedIndividual
        :param t: The concrete feature used to determine the variable type (integer or continuous) for the individual.
        :type t: ConcreteFeature
        :param kb: The knowledge base instance containing the MILP model from which the variable is retrieved.
        :type kb: KnowledgeBase

        :return: The optimization variable representing the value of the concrete feature for the specified individual within the knowledge base's MILP model.

        :rtype: Variable
        """

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
        """
        Encodes the "not simple restriction" logical rule into linear constraints within the provided knowledge base's MILP solver, handling relationships between an individual, a feature, and a condition. The method supports three inequality types—greater than, less than, and equal—and adapts the constraint formulation based on whether the input value `n` is a numeric constant or a decision variable. When `n` is a variable, the method explicitly bounds it within the solver's maximum value range to maintain numerical stability. For equality constraints, an auxiliary binary variable is introduced to decompose the equality into a pair of inequalities using a Big-M formulation. This process modifies the knowledge base by adding the generated constraints and, in the case of equality, creating new binary variables.

        :param n: The numeric constant or variable acting as the bound in the inequality restriction.
        :type n: typing.Any
        :param kb: The knowledge base containing the MILP model to which the new constraints are added.
        :type kb: KnowledgeBase
        :param x_b: The variable representing the individual being restricted.
        :type x_b: Variable
        :param x_f: The variable representing the feature involved in the restriction.
        :type x_f: Variable
        :param x_is_c: A binary variable representing the condition; when active, it relaxes the restriction constraint.
        :type x_is_c: Variable
        :param k: The list of constants used to define the restriction constraints.
        :type k: list[float]
        :param type: Specifies the type of inequality constraint to apply, determining whether the restriction is greater than, less than, or equal.
        :type type: InequalityType
        """

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
        """
        Encodes the "not feature" logical relationship into the Mixed-Integer Linear Programming (MILP) model contained within the provided knowledge base. The method first establishes upper and lower bounds for the specified degree expression to ensure it remains within a valid range. It then constructs and adds specific linear constraints that relate the individual, feature, and condition variables according to the specified inequality type; for equality constraints, an auxiliary binary variable is introduced to the model to enforce the logic. This method modifies the state of the knowledge base by adding constraints and variables to its solver, although the list of constants `k` is currently unused in the implementation.

        :param deg: The degree expression representing the target value to be constrained by the "not feature" logic.
        :type deg: DegreeExpression
        :param x_b: The individual entity to which the constraint applies.
        :type x_b: Variable
        :param x_f: The variable representing the feature involved in the constraint.
        :type x_f: Variable
        :param x_is_c: The variable representing the condition that governs the constraint logic.
        :type x_is_c: Variable
        :param k: A list of floating-point constants used as coefficients or offsets within the equation.
        :type k: list[float]
        :param type: Specifies the inequality relationship (greater than, less than, or equal) to enforce, which dictates the specific linear constraints added to the model.
        :type type: InequalityType
        :param kb: The knowledge base instance managing the MILP model to which the equation constraints are added.
        :type kb: KnowledgeBase
        """

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
        """
        Encodes the logical constraints for the "not fuzzy number" rule into the MILP solver of the provided Knowledge Base. By introducing auxiliary binary variables to represent the satisfaction of specific inequalities between the input variables, this method constructs linear constraints that enforce the condition that the feature variable $x_f$ must be zero when the specified inequality type (greater than, less than, or equal) is met. The method directly modifies the Knowledge Base by adding these new variables and constraints to its internal optimization model.

        :param x_b: The variable representing the individual used in the inequality comparison.
        :type x_b: Variable
        :param x_b_prime: The variable representing the modified individual, used in comparisons with the original individual to enforce the inequality constraints.
        :type x_b_prime: Variable
        :param x_b_prime_is_f: The variable representing the modified individual's feature value.
        :type x_b_prime_is_f: Variable
        :param x_f: The variable representing the feature value or membership degree to be constrained by the equation.
        :type x_f: Variable
        :param x_is_c: The variable representing the condition value used in the equation.
        :type x_is_c: Variable
        :param x_is_f: The variable representing the condition associated with the feature.
        :type x_is_f: Variable
        :param k: List of constants used in the equation.
        :type k: list[float]
        :param type: Specifies the inequality relation (greater than, less than, or equal) to be enforced by the equation.
        :type type: InequalityType
        :param kb: The knowledge base containing the MILP solver where the equation constraints and auxiliary variables are added.
        :type kb: KnowledgeBase
        """

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
        """
        This static method adds linear constraints to the MILP helper to model the relationship where the binary variable `y` represents the result of comparing `x1` and `x2`. It introduces an auxiliary continuous variable `z` to represent the difference `x1 - x2` and bounds `z` within the solver's maximum value limits. The constraints enforce that `y` is set to 1 if `x1` is greater than `x2` by at least a small epsilon margin, and 0 if `x1` is less than or equal to `x2`, effectively creating a "big-M" formulation for the comparison. As a side effect, this method modifies the MILP helper by registering the new variable `z` and adding the necessary inequality constraints to the model.

        :param y: The binary variable representing the result of the comparison.
        :type y: Variable
        :param x1: The variable representing the first operand in the comparison against x2.
        :type x1: Variable
        :param x2: The variable representing the right-hand side operand of the greater-than-or-equal comparison.
        :type x2: Variable
        :param milp: The MILP helper instance to which the auxiliary variable and constraints are added to enforce the comparison logic.
        :type milp: MILPHelper
        """

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
        """
        This static method applies the "not" rule to a specific assertion within a knowledge base, translating logical negation into Mixed-Integer Linear Programming (MILP) constraints. It processes an assertion where a concept is negated, extracting the underlying concept and role to retrieve or create the necessary MILP variables for the individuals and feature values involved. The method enforces the logical relationship between a concept and its negation by adding a constraint that ensures they are mutually exclusive. Depending on the nature of the value associated with the concept—whether it is a triangular fuzzy number, a feature function, a boolean, or a simple value—it delegates to specialized helper functions to generate the specific inequalities required. If the value is a feature function and the individual lacks the necessary fillers, the method exits early. As a side effect, it updates the knowledge base's MILP model with new constraints and variables and increments the counter for binary variables.

        :param b: The individual representing the filler value for the datatype feature involved in the negation constraint.
        :type b: CreatedIndividual
        :param ass: The assertion linking an individual to the negated concept to which the rule is applied.
        :type ass: Assertion
        :param kb: The knowledge base managing the current state, including the MILP model, feature definitions, and variable mappings.
        :type kb: KnowledgeBase
        :param type: Specifies the inequality relation (e.g., equality or inequality) to use when constructing the constraints for the negation rule.
        :type type: InequalityType
        """

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
        """
        Applies the reasoning rule for the negation of an "at least" value restriction to a specific individual within the provided knowledge base. This method acts as a specialized wrapper that delegates the logic to the generic `apply_not_rule` function, specifying `InequalityType.GREATER_THAN` to handle the specific inequality constraints involved. The execution of this rule modifies the knowledge base or the individual's state to enforce the logical implications of the assertion.

        :param b: The individual entity on which the "not at least" value rule is applied.
        :type b: CreatedIndividual
        :param ass: The assertion containing the concept and individual involved in the rule application.
        :type ass: Assertion
        :param kb: The knowledge base containing the individuals and concepts.
        :type kb: KnowledgeBase
        """

        DatatypeReasoner.apply_not_rule(b, ass, kb, InequalityType.GREATER_THAN)

    @staticmethod
    def apply_not_at_most_value_rule(
        b: CreatedIndividual, ass: Assertion, kb: KnowledgeBase
    ) -> None:
        """
        This static method enforces the "not at most" value restriction rule for a given individual within a knowledge base. It processes the assertion to infer the necessary constraints resulting from the negation of an upper bound, delegating the specific logic to a generic rule handler with the inequality type set to "less than". The execution of this method directly modifies the state of the knowledge base by adding inferred information to the specified individual.

        :param b: The individual instance to which the rule is applied.
        :type b: CreatedIndividual
        :param ass: The assertion representing the constraint or fact involving the concept and individual.
        :type ass: Assertion
        :param kb: The knowledge base containing the individuals and concepts.
        :type kb: KnowledgeBase
        """

        DatatypeReasoner.apply_not_rule(b, ass, kb, InequalityType.LESS_THAN)

    @staticmethod
    def apply_not_exact_value_rule(
        b: CreatedIndividual, ass: Assertion, kb: KnowledgeBase
    ) -> None:
        """
        This static method enforces the "not exact value" reasoning rule by processing a specific assertion against a target individual within the provided knowledge base. It delegates the core logic to the general inequality handler, specifically targeting equality constraints to ensure the individual is restricted from holding the exact value defined in the assertion. As a side effect, this operation updates the knowledge base by adding or refining inferred restrictions based on the negation of the exact value.

        :param b: The individual entity to which the rule is applied.
        :type b: CreatedIndividual
        :param ass: The assertion containing the concept and individual to which the rule is applied.
        :type ass: Assertion
        :param kb: The knowledge base containing the individuals and concepts involved in the reasoning.
        :type kb: KnowledgeBase
        """

        DatatypeReasoner.apply_not_rule(b, ass, kb, InequalityType.EQUAL)


@class_debugging()
class LukasiewiczSolver:
    """
    This class provides a static interface for solving fuzzy logic assertions by applying the Lukasiewicz t-norm and t-conorm within a Mixed-Integer Linear Programming (MILP) framework. It translates high-level fuzzy description logic constructs—such as conjunctions, disjunctions, and existential or universal restrictions—into a set of linear constraints and variables that are added to a provided knowledge base. Users typically invoke methods like `solve_and`, `solve_or`, `solve_some`, or `solve_all` by passing a specific assertion and the target knowledge base; the class then handles the internal logic of creating necessary variables, managing role relations, and generating the specific equations required to model the fuzzy logic operations accurately. The implementation accounts for complex scenarios such as transitive roles, role hierarchies, and functional roles, ensuring that the generated constraints correctly reflect the semantics of the Lukasiewicz logic.

    :raises ValueError: Raised when the arguments provided to the equation methods do not match the expected types, specifically when a required argument is neither a Variable nor a numeric constant.
    """

    @staticmethod
    def and_(n1: float, n2: float) -> float:
        """
        Computes the Łukasiewicz t-norm, which serves as a fuzzy logic conjunction for the two provided numerical values. The operation is defined mathematically as the maximum of the sum of the inputs minus one and zero. This effectively clamps the result to ensure it remains non-negative, returning zero if the sum of the inputs is less than or equal to one. The method is a pure function with no side effects.

        :param n1: The first operand or truth value for the Lukasiewicz t-norm calculation.
        :type n1: float
        :param n2: The second operand for the Lukasiewicz t-norm.
        :type n2: float

        :return: The result of the Lukasiewicz t-norm applied to n1 and n2, calculated as the maximum of the sum of the inputs minus one and zero.

        :rtype: float
        """

        return max(n1 + n2 - 1, 0)

    @staticmethod
    def solve_and(ass: Assertion, kb: KnowledgeBase) -> None:
        """
        This static method translates a fuzzy logic conjunction assertion into a set of constraints within the associated Mixed-Integer Linear Programming (MILP) model. It extracts the composite concept and the individual from the input assertion, verifying that the concept supports a conjunction structure. The method iterates through the sub-concepts, retrieving their corresponding MILP variables and registering them within the knowledge base. As a side effect, it updates the knowledge base's counters for 01 and binary variables based on the number of sub-concepts processed. Finally, it establishes the mathematical relationship between the main assertion variable and the sub-concept variables using the Lukasiewicz t-norm formulation.

        :param ass: The fuzzy assertion representing a conjunction (AND) operation, linking an individual to a composite concept containing multiple sub-concepts to be evaluated.
        :type ass: Assertion
        :param kb: The reference fuzzy knowledge base containing the individuals, concepts, and MILP solver context used to resolve the assertion.
        :type kb: KnowledgeBase
        """

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
        """
        Translates a fuzzy disjunction assertion into a set of linear constraints within the provided knowledge base's MILP solver. It retrieves the individual and the composite concept from the assertion, verifying that the concept represents a collection of sub-concepts. For each sub-concept, it resolves the corresponding variable for the individual and updates the knowledge base with the degree information. Finally, it enforces the logical relationship between the main assertion variable and the variables of its constituent parts by applying the Lukasiewicz OR equation to the solver model.

        :param ass: The fuzzy assertion to be solved, representing a disjunction of concepts for a specific individual.
        :type ass: Assertion
        :param kb: The reference fuzzy knowledge base containing the individuals, concepts, and MILP solver context used to resolve the disjunction.
        :type kb: KnowledgeBase
        """

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
        """
        Encodes the semantics of an existential restriction fuzzy assertion ($a: \exists R.C$) into the Mixed-Integer Linear Programming (MILP) model associated with the knowledge base. The method identifies or creates a filler individual $b$ such that $a$ is related to $b$ via role $R$ and $b$ is an instance of concept $C$. It enforces the fuzzy logic constraint that the truth degree of the original assertion is less than or equal to the Lukasiewicz t-norm of the truth degrees of the relation $(a, b): R$ and the assertion $b: C$. Special handling is provided for functional roles, which reuse existing related individuals, and for inverse roles, which are processed by creating corresponding relations with equal degrees. This operation modifies the knowledge base by adding new individuals, assertions, relations, and MILP constraints.

        :param ass: The fuzzy assertion to be solved, containing the subject individual and the existential restriction concept.
        :type ass: Assertion
        :param kb: The reference fuzzy knowledge base providing the context, MILP model, and role definitions needed to resolve the assertion and update the solver state.
        :type kb: KnowledgeBase
        """

        a: Individual = ass.get_individual()
        concept: AllSomeConcept = typing.cast(AllSomeConcept, ass.get_concept())
        role: str = concept.role
        c: Concept = concept.curr_concept
        kb.rules_applied[KnowledgeBaseRules.RULE_LUKASIEWICZ_SOME] += 1

        # Concept simplification
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

        # b:C >= x_{b:C}
        kb.add_assertion(b, c, DegreeVariable.get_degree(c_var))

        # (a,b):R >= x_{(a:b):R}
        r: Relation = IndividualHandler.add_relation(
            a, role, b, DegreeVariable.get_degree(r_var), kb
        )

        # xAss <= x_{b:C} \otimes x_{(a:b):R}
        x_ass: Variable = kb.milp.get_variable(ass)
        LukasiewiczSolver.and_leq_equation(x_ass, c_var, r_var, kb.milp)

        kb.solve_role_inclusion_axioms(a, r)

        # For every inverse role
        list_inverse_roles: list[str] = kb.inverse_roles.get(ass.get_concept().role, [])
        for inv_role in list_inverse_roles:
            var: Variable = kb.milp.get_variable(b, ass.get_individual(), inv_role)
            # (b,a):inv(R) >= l
            IndividualHandler.add_relation(
                b, inv_role, ass.get_individual(), DegreeVariable.get_degree(var), kb
            )
            kb.milp.add_new_constraint(
                Expression(Term(1.0, r_var), Term(-1.0, var)), InequalityType.EQUAL
            )
            kb.solve_role_inclusion_axioms(b, r)

    @staticmethod
    def solve_all(rel: Relation, restrict: Restriction, kb: KnowledgeBase) -> None:
        """
        Encodes a universal restriction fuzzy assertion into the Mixed-Integer Linear Programming (MILP) model associated with the given knowledge base, adhering to Lukasiewicz logic semantics. This method processes a relation between two individuals and a restriction to enforce that if the subject is related to the object, the object must satisfy the restriction's concept. It handles both standard universal restrictions and HasValue restrictions, creating the necessary variables and constraints within the solver. Additionally, the method accounts for transitive roles and their hierarchical relationships by propagating constraints and adjusting for inclusion degrees. As a side effect, it updates the knowledge base by adding new assertions, tracking rule usage statistics, and incrementing counters for non-numeric variables.

        :param rel: The fuzzy relation instance connecting the subject and object individuals, used to derive the specific variables and constraints for the universal restriction.
        :type rel: Relation
        :param restrict: The restriction defining the role and the concept (or individual) involved in the universal restriction assertion.
        :type restrict: Restriction
        :param kb: The reference fuzzy knowledge base containing individuals, concepts, and role hierarchies. It manages the MILP solver state, tracks applied reasoning rules, and is updated with new assertions and constraints during the solving process.
        :type kb: KnowledgeBase
        """

        if not rel.get_degree().is_numeric() or not restrict.get_degree().is_numeric():
            kb.old_01_variables += 1

        a: Individual = rel.get_subject_individual()
        b: Individual = rel.get_object_individual()

        # Has value restriction
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
            # xForAllB >= xForAll \otimes xRel
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
        # xBinC >= xForAll \otimes xRel
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
        """
        This static method acts as a dispatcher to enforce the Lukasiewicz logical AND operation within a Mixed-Integer Linear Programming (MILP) context by adding specific constraints to the model. It supports multiple argument patterns: a sequence of input variables with a designated result variable, or a pair of input variables combined with a third operand that is either a numeric constant or another variable. In all cases, a `MILPHelper` object must be provided to handle the constraint generation. The method performs strict validation on the number and types of arguments, raising errors if the input does not match the expected signatures for the underlying constraint logic.

        :param args: A variable-length argument list specifying the operands and solver context for the AND constraint. Valid signatures include a sequence of input variables and a result variable, or two input variables combined with a numeric constant or a third variable, followed by a MILP helper.
        :type args: typing.Any

        :raises ValueError: Raised if the provided arguments do not match any of the supported signatures, specifically when the third argument is neither a numeric constant nor a Variable.
        """

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
        """
        Encodes the logical conjunction of a list of binary variables into linear constraints within the provided MILP model. This method ensures that the target variable `z` is 1 if and only if all variables in the input list `x` are 1, and 0 otherwise. To linearize this logical operation, it introduces a new auxiliary binary variable and adds three specific linear inequalities to the model, modifying the MILP instance in place.

        :param x: The list of variables representing the operands of the logical AND operation.
        :type x: list[Variable]
        :param z: The variable to be constrained to the result of the logical AND operation.
        :type z: Variable
        :param milp: Helper instance used to create variables and add constraints to the MILP model.
        :type milp: MILPHelper
        """

        y: Variable = milp.get_new_variable(VariableType.BINARY)
        N: int = len(x)
        exp: Expression = Expression(x)
        exp.add_term(Term(-1.0, z))
        exp.set_constant(1.0 - N)
        # \sum_{i=1}^{n} x_i - (n-1) \leq z
        milp.add_new_constraint(exp, InequalityType.LESS_THAN)
        # y \leq 1-z
        milp.add_new_constraint(
            Expression(1.0, Term(-1.0, z), Term(-1.0, y)),
            InequalityType.GREATER_THAN,
        )
        # \sum_{i=1}^{n} x_i - (n-1)  \geq z - (n-1) y
        exp2: Expression = Expression(exp)
        exp2.add_term(Term(N - 1.0, y))
        milp.add_new_constraint(exp2, InequalityType.GREATER_THAN)

    @staticmethod
    def __and_equation_2(
        z: Variable, x1: Variable, x2: float, milp: MILPHelper
    ) -> None:
        """
        This method encodes the logical AND operation $z = x_1 \land x_2$ within the Mixed-Integer Linear Programming (MILP) framework, specifically for the case where the second operand $x_2$ is a constant float. It implements the Łukasiewicz t-norm formulation, which mathematically corresponds to $z = \max(0, x_1 + x_2 - 1)$, by introducing an auxiliary binary variable to linearize the relationship. The method modifies the MILP helper instance by adding this new variable and appending the necessary inequality constraints to enforce the logical equivalence.

        :param z: The variable to be constrained to the result of the logical AND operation between x1 and x2.
        :type z: Variable
        :param x1: The first operand variable for the logical AND operation.
        :type x1: Variable
        :param x2: The constant float value representing the second operand in the logical AND operation.
        :type x2: float
        :param milp: The MILP helper used to create auxiliary variables and add constraints.
        :type milp: MILPHelper
        """

        y: Variable = milp.get_new_variable(VariableType.BINARY)
        # x1 + x2 - 1 \leq z
        milp.add_new_constraint(
            Expression(1.0 - x2, Term(-1.0, x1), Term(1.0, z)),
            InequalityType.GREATER_THAN,
        )
        # x1 + x2 - 1 \geq z - y
        milp.add_new_constraint(
            Expression(1.0 - x2, Term(-1.0, x1), Term(1.0, z), Term(-1.0, y)),
            InequalityType.LESS_THAN,
        )
        # z \leq 1 - y
        milp.add_new_constraint(
            Expression(-1.0, Term(1.0, z), Term(1.0, y)),
            InequalityType.LESS_THAN,
        )

    @staticmethod
    def __and_equation_3(
        z: Variable, x1: Variable, x2: Variable, milp: MILPHelper
    ) -> None:
        """
        Encodes the logical AND operation $z = x_1 \land x_2$ into the MILP model by introducing a new auxiliary binary variable and adding three linear constraints to the helper instance. This method modifies the model in place to enforce the relationship, ensuring that $z$ is 1 if and only if both $x_1$ and $x_2$ are 1. The formulation relies on the auxiliary variable to define the feasible region of the logical operation.

        :param z: The variable to be constrained to the result of the logical AND operation between x1 and x2.
        :type z: Variable
        :param x1: The first variable in the logical AND operation.
        :type x1: Variable
        :param x2: The second operand of the logical AND operation.
        :type x2: Variable
        :param milp: Helper instance used to generate auxiliary variables and add the linear constraints required to model the AND operation.
        :type milp: MILPHelper
        """

        y: Variable = milp.get_new_variable(VariableType.BINARY)
        # x1 + x2 - 1 \leq z
        milp.add_new_constraint(
            Expression(1.0, Term(-1.0, x1), Term(-1.0, x2), Term(1.0, z)),
            InequalityType.GREATER_THAN,
        )
        # x1 + x2 - 1 \geq z - y
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
        # z \leq 1 - y
        milp.add_new_constraint(
            Expression(-1.0, Term(1.0, z), Term(1.0, y)),
            InequalityType.LESS_THAN,
        )

    @staticmethod
    def and_leq_equation(
        z: Variable, x1: Variable, x2: Variable, milp: MILPHelper
    ) -> None:
        """
        Adds linear constraints to the provided MILP model to enforce the logical relationship that the variable `z` is less than or equal to the conjunction of `x1` and `x2`. This formulation introduces an auxiliary binary variable to linearize the logical AND operation, ensuring that `z` can only be 1 if both `x1` and `x2` are 1, while forcing `z` to 0 if either input is 0. The method modifies the `MILPHelper` instance by registering the new variable and adding the necessary inequality constraints to the solver.

        :param z: The variable representing the result of the logical AND operation, constrained to be less than or equal to the conjunction of x1 and x2.
        :type z: Variable
        :param x1: The first operand of the logical AND operation.
        :type x1: Variable
        :param x2: The second operand of the logical AND operation.
        :type x2: Variable
        :param milp: The MILP helper instance used to introduce auxiliary variables and add constraints to the model.
        :type milp: MILPHelper
        """

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
        """
        Adds a constraint to the MILP model representing the inequality $z \ge x_1 \land x_2$, where $z$ is the result variable and $x_1, x_2$ are the operands. The method accepts a result variable, a first operand variable, a second operand (which can be either a variable or a numeric constant), and a MILP helper instance. It dispatches to specific internal implementations to generate the appropriate linear constraints based on whether the second operand is a variable or a constant. The method raises a ValueError if the second operand is of an unsupported type and asserts that the first and last arguments are of the correct types.

        :param args: A sequence of four elements defining the logical constraint: the result variable, the first operand variable, the second operand (either a variable or a numeric constant), and the MILP helper instance.
        :type args: typing.Any

        :raises ValueError: Raised if the third argument is not a Variable or a numeric constant.
        """

        assert len(args) == 4
        assert isinstance(args[0], Variable)
        assert isinstance(args[1], Variable)
        assert isinstance(args[3], MILPHelper)
        if isinstance(args[2], Variable):
            LukasiewiczSolver.__and_geq_equation_1(*args)
        elif isinstance(args[2], constants.NUMBER):
            LukasiewiczSolver.__and_geq_equation_2(*args)
        else:
            raise ValueError("Invalid argument type for AND operation")

    @staticmethod
    def __and_geq_equation_1(
        z: Variable, x1: Variable, x2: Variable, milp: MILPHelper
    ) -> None:
        """
        This static method enforces the first linear inequality required to model the logical conjunction $z = x_1 \land x_2$ within a Mixed-Integer Linear Programming (MILP) framework. It adds a constraint to the provided `MILPHelper` instance ensuring that the result variable $z$ is not less than the sum of the input variables $x_1$ and $x_2$ minus one ($z \ge x_1 + x_2 - 1$). This constraint specifically prevents $z$ from being false (0) when both inputs are true (1), effectively establishing the lower bound for the AND operation, while the upper bounds are typically handled by separate constraints.

        :param z: The output variable representing the result of the logical AND operation.
        :type z: Variable
        :param x1: The first operand of the logical AND operation.
        :type x1: Variable
        :param x2: The second variable in the logical AND operation.
        :type x2: Variable
        :param milp: The MILP helper object used to add the generated constraint to the optimization model.
        :type milp: MILPHelper
        """

        milp.add_new_constraint(
            Expression(-1.0, Term(-1.0, z), Term(1.0, x1), Term(1.0, x2)),
            InequalityType.LESS_THAN,
        )

    @staticmethod
    def __and_geq_equation_2(
        z: Variable, x1: Variable, x2: float, milp: MILPHelper
    ) -> None:
        """
        Adds a linear constraint to the MILP model to enforce the lower bound relationship for a logical AND operation between a variable and a constant. Specifically, it implements the inequality $x_1 + x_2 - 1 < z$, ensuring that the result variable `z` is strictly greater than the Lukasiewicz t-norm calculation of `x1` and `x2`. This method modifies the `milp` object by appending the new constraint, which is essential for accurately modeling fuzzy or probabilistic logic within the linear programming framework. The behavior assumes that the variables operate within a domain where this linearization is valid, typically the interval [0, 1].

        :param z: The variable representing the result of the logical AND operation.
        :type z: Variable
        :param x1: The variable operand of the logical AND operation.
        :type x1: Variable
        :param x2: The constant value representing the second operand in the logical AND operation.
        :type x2: float
        :param milp: Helper object used to add the constraint to the model.
        :type milp: MILPHelper
        """

        milp.add_new_constraint(
            Expression(-1.0 + x2, Term(-1.0, z), Term(1.0, x1)),
            InequalityType.LESS_THAN,
        )

    @staticmethod
    def or_equation(x: list[Variable], z: Variable, milp: MILPHelper) -> None:
        """
        Adds linear constraints to the MILP model to enforce the logical condition that the variable `z` represents the OR operation of the variables in list `x`. This ensures that `z` is 1 if and only if at least one variable in `x` is 1, and `z` is 0 if all variables in `x` are 0. The method introduces an auxiliary binary variable to linearize the relationship and modifies the `milp` helper by adding the new variable and the necessary inequality constraints.

        :param x: A list of variables representing the operands of the logical OR operation.
        :type x: list[Variable]
        :param z: The variable representing the result of the logical OR operation.
        :type z: Variable
        :param milp: The MILP helper used to add the linear constraints and auxiliary variables defining the OR operation.
        :type milp: MILPHelper
        """

        y: Variable = milp.get_new_variable(VariableType.BINARY)
        N: int = len(x)

        # \sum_{i=1}^{n} x_i \geq z
        exp: Expression = Expression(x)
        exp.add_term(Term(-1.0, z))
        milp.add_new_constraint(exp, InequalityType.GREATER_THAN)

        # y \leq z
        milp.add_new_constraint(
            Expression(Term(1.0, y), Term(-1.0, z)), InequalityType.LESS_THAN
        )

        # \sum_{i=1}^{n} x_i \leq z + (n-1) y
        exp2: Expression = Expression(exp)
        exp2.add_term(Term(1.0 - N, y))
        milp.add_new_constraint(exp2, InequalityType.LESS_THAN)


@class_debugging()
class ZadehSolver:
    """
    This class serves as a static solver for translating fuzzy logic assertions into Mixed-Integer Linear Programming (MILP) constraints, primarily operating under Zadeh fuzzy logic semantics. It provides a suite of methods to model fundamental logical operations—such as conjunction, disjunction, negation, and various forms of implication (including Zadeh, Goedel, and Kleene-Dienes)—by mapping them to linear inequalities and introducing auxiliary binary variables where necessary. The solver interacts directly with a `KnowledgeBase` and an `MILPHelper` to populate the optimization model, handling both simple logical connectives and complex quantifiers like existential and universal restrictions. Users typically invoke the high-level `solve_and`, `solve_or`, `solve_some`, and `solve_all` methods to process assertions against a knowledge base, while the lower-level equation methods are utilized to construct the specific mathematical relationships required by the underlying solver.

    :raises ValueError: Raised when the arguments provided to the overloaded equation methods (such as `and_equation`, `and_geq_equation`, or `zadeh_implies_equation`) do not match the expected type signatures for any supported operation.
    """

    @staticmethod
    def solve_and(ass: Assertion, kb: KnowledgeBase) -> None:
        """
        Processes a fuzzy assertion representing a logical conjunction by integrating it into the Mixed-Integer Linear Programming (MILP) model of the provided knowledge base. It extracts the individual and the composite concept, ensuring the concept implements the `HasConceptsInterface` to access its constituent parts. For each sub-concept, the method retrieves the corresponding variable, adds an assertion linking the individual to that sub-concept's degree, and finally applies a constraint equation to the MILP solver that defines the relationship between the conjunction variable and its components.

        :param ass: The fuzzy assertion representing a conjunction to be solved and translated into solver constraints.
        :type ass: Assertion
        :param kb: The fuzzy knowledge base providing the solver and existing assertions used as the context for resolving the conjunction.
        :type kb: KnowledgeBase
        """

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
        """
        Computes and enforces the logical AND operation within a Mixed-Integer Linear Programming (MILP) context by adding constraints to the provided solver helper. This static method serves as a dispatcher that validates the input arguments—accepting either 3 or 4 arguments where the final argument must be a `MILPHelper` instance—and delegates the constraint generation to specific private helper methods based on the types of the preceding inputs. Supported input patterns include lists of variables, pairs of variables, variables combined with terms, or variables combined with numeric constants. The method modifies the state of the `MILPHelper` object to reflect the new constraints and raises a `ValueError` if the argument types do not conform to the expected patterns.

        :param args: Operands for the AND operation and the MILP solver helper, provided as a variable-length list. Valid configurations include three arguments (a list of variables, a variable or term, and a helper) or four arguments (two variables, a variable or number, and a helper).
        :type args: typing.Any

        :raises ValueError: Raised when the arguments do not match the required type combinations. For three arguments, the first two must be a list of variables and a variable, a list of variables and a term, or two variables. For four arguments, the first two must be variables and the third must be a variable or a numeric constant.
        """

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
        """
        Encodes the logical constraint $z = x_1 \land x_2 \land \dots \land x_n$ into the Mixed-Integer Linear Programming (MILP) model provided. This method acts as a wrapper around the general `and_equation` function, passing the list of input variables and the output variable `z` formatted as a Term with a coefficient of 1.0. It modifies the `milp` object by adding the necessary linear inequalities to enforce that the result variable `z` is true only when all variables in the input list `x` are true.

        :param x: A list of variables representing the operands of the logical AND operation.
        :type x: list[Variable]
        :param z: Variable representing the result of the logical AND operation.
        :type z: Variable
        :param milp: The MILP helper instance to which the constraints defining the AND operation are added.
        :type milp: MILPHelper
        """

        ZadehSolver.and_equation(x, Term(1.0, z), milp)

    @staticmethod
    def __and_equation_2(x: list[Variable], t: Term, milp: MILPHelper) -> None:
        """
        Encodes the logical conjunction (AND) of a list of variables into the provided MILP model, assigning the result to the specified term. The method first adds constraints ensuring the result term is less than or equal to each input variable, which enforces that the result is true only if all inputs are true. To efficiently handle the reverse implication—that the result is false if at least one input is false—it introduces a set of auxiliary binary variables, the number of which scales logarithmically with the number of inputs. These auxiliary variables are used in conjunction with constraints derived from the binary representation of the input indices to ensure that if the result is zero, the auxiliary variables can be configured to force at least one input variable to zero. As a side effect, this method modifies the MILP helper by adding new constraints and creating the necessary auxiliary binary variables.

        :param x: A list of variables representing the operands of the logical AND operation.
        :type x: list[Variable]
        :param t: The term representing the output variable of the logical AND operation.
        :type t: Term
        :param milp: The MILP helper instance used to add constraints and auxiliary variables to the model.
        :type milp: MILPHelper
        """

        N: int = len(x)
        M: float = Util.log2(N)
        # z \leq x_i
        for xi in x:
            milp.add_new_constraint(
                Expression(t, Term(-1.0, xi)), InequalityType.LESS_THAN
            )
        # y \in {0,1}
        y: list[Variable] = [
            milp.get_new_variable(VariableType.BINARY) for _ in range(M)
        ]
        # x_{i} \leq z + \sum_{j=1}^{m} e_{ij}
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

        # \sum_{j=1}^{m} 2^{j-1} y_{j} \leq n-1
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
        """
        Encodes the logical AND operation $z = x_1 \land x_2$ into the Mixed-Integer Linear Programming (MILP) model, specifically for the scenario where the second operand $x_2$ is a constant float value. This method linearizes the non-linear logical relationship by introducing an auxiliary binary variable and adding four linear inequality constraints to the MILP helper. The constraints ensure that the result variable $z$ is bounded above by both inputs and that the inputs are bounded below by $z$ combined with the auxiliary variable, thereby enforcing the AND condition. As a side effect, this method modifies the state of the provided `MILPHelper` instance by registering the new auxiliary variable and appending the necessary constraints to the model.

        :param z: The variable representing the result of the logical AND operation between x1 and x2.
        :type z: Variable
        :param x1: The first variable operand in the logical AND operation.
        :type x1: Variable
        :param x2: The constant value representing the second operand of the logical AND operation.
        :type x2: float
        :param milp: The MILP helper used to introduce auxiliary variables and add constraints to the model.
        :type milp: MILPHelper
        """

        y: Variable = milp.get_new_variable(VariableType.BINARY)
        # x_1 \leq x_2
        milp.add_new_constraint(
            Expression(Term(1.0, z), Term(-1.0, x1)), InequalityType.LESS_THAN
        )
        # x_1 \leq x_3
        milp.add_new_constraint(Expression(Term(1.0, z)), InequalityType.LESS_THAN, x2)
        # x_2 \leq x_1 + y
        milp.add_new_constraint(
            Expression(Term(1.0, x1), Term(-1.0, z), Term(-1.0, y)),
            InequalityType.LESS_THAN,
        )
        # x_3 \leq x_1 + (1-y)
        milp.add_new_constraint(
            Expression(-1.0 + x2, Term(-1.0, z), Term(1.0, y)),
            InequalityType.LESS_THAN,
        )

    @staticmethod
    def __and_equation_4(
        z: Variable, x1: Variable, x2: Variable, milp: MILPHelper
    ) -> None:
        """
        Encodes the logical AND operation $z = x_1 \land x_2$ into the MILP model using a specific linearization formulation that relies on an auxiliary binary variable. This method introduces a new binary variable $y$ and adds four linear inequality constraints to the MILP helper to enforce the relationship: $z \le x_1$, $z \le x_2$, $x_1 \le z + y$, and $x_2 \le z + 1 - y$. These constraints ensure that $z$ takes the value 1 only when both $x_1$ and $x_2$ are 1, provided the input variables are binary. The operation modifies the `milp` object by registering the new variable and appending the constraints, and it returns None.

        :param z: The variable representing the result of the logical AND operation between x1 and x2.
        :type z: Variable
        :param x1: The first operand of the logical AND operation.
        :type x1: Variable
        :param x2: The second operand of the logical AND operation.
        :type x2: Variable
        :param milp: The MILP helper instance used to introduce auxiliary variables and add the linear constraints defining the logical AND operation.
        :type milp: MILPHelper
        """

        y: Variable = milp.get_new_variable(VariableType.BINARY)
        # x_1 \leq x_2
        milp.add_new_constraint(
            Expression(Term(1.0, z), Term(-1.0, x1)), InequalityType.LESS_THAN
        )
        # x_1 \leq x_3
        milp.add_new_constraint(
            Expression(Term(1.0, z), Term(-1.0, x2)), InequalityType.LESS_THAN
        )
        # x_2 \leq x_1 + y
        milp.add_new_constraint(
            Expression(Term(1.0, x1), Term(-1.0, z), Term(-1.0, y)),
            InequalityType.LESS_THAN,
        )
        # x_3 \leq x_1 + (1-y)
        milp.add_new_constraint(
            Expression(-1.0, Term(1.0, x2), Term(-1.0, z), Term(1.0, y)),
            InequalityType.LESS_THAN,
        )

    @staticmethod
    def __and_equation_5(x1: Variable, x2: Variable, milp: MILPHelper) -> None:
        """
        This static method enforces the logical constraint that the conjunction of `x1` and `x2` is less than or equal to zero, which is used to model disjoint concepts within the optimization problem. It operates by introducing a new auxiliary binary variable into the MILP model and adding two linear constraints: the first ensures `x1` is less than or equal to the auxiliary variable, and the second ensures the sum of the auxiliary variable and `x2` is strictly less than one. Collectively, these constraints imply that the sum of `x1` and `x2` must be strictly less than one, effectively preventing both variables from being active or true simultaneously. The method modifies the provided `MILPHelper` instance by registering the new variable and the associated constraints.

        :param x1: The first variable in the pair, constrained to be mutually exclusive with x2.
        :type x1: Variable
        :param x2: The second variable in the logical constraint ensuring mutual exclusivity with x1.
        :type x2: Variable
        :param milp: Helper object used to generate auxiliary binary variables and add the resulting linear constraints.
        :type milp: MILPHelper
        """

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
        """
        Encodes the logical relationship z = (1 - x1) AND x2 into the Mixed-Integer Linear Programming (MILP) model by adding linear constraints and an auxiliary binary variable. This method ensures that the binary variable z is 1 if and only if x1 is 0 and the float parameter x2 is 1, effectively linearizing the logical AND operation for the solver. It modifies the MILPHelper instance in place by creating a new binary variable and appending four inequality constraints that enforce the equivalence between the logical expression and the variable z.

        :param z: The variable representing the result of the logical expression $(1 - x_1) \land x_2$.
        :type z: Variable
        :param x1: The variable representing the first operand, which is negated before being ANDed with x2.
        :type x1: Variable
        :param x2: The constant value representing the second operand of the AND operation.
        :type x2: float
        :param milp: Helper object used to introduce auxiliary variables and enforce the linear constraints defining the logical relationship.
        :type milp: MILPHelper
        """

        y: Variable = milp.get_new_variable(VariableType.BINARY)
        # x_1 \leq (1 - x_2)
        milp.add_new_constraint(
            Expression(-1.0, Term(1.0, z), Term(1.0, x1)),
            InequalityType.LESS_THAN,
        )
        # x_1 \leq x_3
        milp.add_new_constraint(Expression(Term(1.0, z)), InequalityType.LESS_THAN, x2)
        # (1 - x_2) \leq x_1 + y
        milp.add_new_constraint(
            Expression(1.0, Term(-1.0, x1), Term(-1.0, z), Term(-1.0, y)),
            InequalityType.LESS_THAN,
        )
        # x_3 \leq x_1 + (1-y)
        milp.add_new_constraint(
            Expression(-1.0 + x2, Term(-1.0, z), Term(1.0, y)),
            InequalityType.LESS_THAN,
        )

    @staticmethod
    def and_leq_equation(
        z: Variable, x1: Variable, x2: Variable, milp: MILPHelper
    ) -> None:
        """
        Adds constraints to the provided MILP model to enforce that the variable `z` is less than or equal to the logical AND of `x1` and `x2`, interpreted as the minimum of the two inputs. This is achieved by appending two linear inequalities, $z \le x_1$ and $z \le x_2$, to the model, effectively bounding `z` from above by the smaller of the two operands. The method modifies the `MILPHelper` instance in place by registering these constraints and returns nothing.

        :param z: The variable representing the result of the logical AND operation, constrained to be less than or equal to both x1 and x2.
        :type z: Variable
        :param x1: The first operand of the logical AND operation.
        :type x1: Variable
        :param x2: The second operand of the logical AND operation.
        :type x2: Variable
        :param milp: The MILP helper instance to which the generated constraints are added.
        :type milp: MILPHelper
        """

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
        """
        Adds constraints to a Mixed-Integer Linear Programming (MILP) model to enforce the inequality $z \ge x_1 \land x_2$, where $z$ is the result variable and $x_1, x_2$ are the operands. This static method validates the input arguments and delegates the constraint generation to specialized internal methods based on the type of the second operand; it handles cases where the operand is a `Variable` or a numeric constant differently. The method modifies the MILP model via the provided `MILPHelper` instance and raises an `AssertionError` for incorrect argument counts or types, or a `ValueError` if the second operand is neither a variable nor a number.

        :param args: A tuple containing the result variable, the first operand variable, the second operand (either a variable or a numeric constant), and the MILP helper instance.
        :type args: typing.Any

        :raises ValueError: Raised if the third argument is not a Variable or a numeric constant.
        """

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
        """
        This static method enforces the constraint that the variable `z` must be greater than or equal to the logical AND of `x1` and `x2`, which is equivalent to the minimum of the two values. It introduces a new binary auxiliary variable `y` to linearize this relationship, adding two inequality constraints to the provided MILP helper. The constraints are structured such that `z` is bounded below by `x1` when `y` is 0, and by `x2` when `y` is 1, ensuring `z` meets the lower bound of the minimum value regardless of which input is smaller. As a side effect, the method modifies the MILP model by creating the new binary variable and registering the associated linear constraints.

        :param z: The variable representing the result of the logical AND operation, constrained to be greater than or equal to the conjunction of x1 and x2.
        :type z: Variable
        :param x1: The first operand of the logical AND operation.
        :type x1: Variable
        :param x2: The second operand of the logical AND operation.
        :type x2: Variable
        :param milp: The MILP helper object used to introduce auxiliary variables and add constraints to the model.
        :type milp: MILPHelper
        """

        y: Variable = milp.get_new_variable(VariableType.BINARY)
        # If y = 0, z >= x1
        milp.add_new_constraint(
            Expression(Term(1.0, y), Term(1.0, z), Term(-1.0, x1)),
            InequalityType.GREATER_THAN,
        )
        # If y = 1, z >= x2
        milp.add_new_constraint(
            Expression(1.0, Term(-1.0, y), Term(1.0, z), Term(-1.0, x2)),
            InequalityType.GREATER_THAN,
        )

    @staticmethod
    def __and_geq_equation_2(
        z: Variable, x1: Variable, x2: float, milp: MILPHelper
    ) -> None:
        """
        Adds linear constraints to the MILP model to enforce the inequality $z \ge x_1 \land x_2$, interpreting the AND operation as the minimum of the operands. To linearize this logical condition, the method introduces a new binary auxiliary variable which allows the solver to select the active constraint, effectively ensuring that $z$ is greater than or equal to the smaller of $x_1$ and $x_2$. This process modifies the MILP helper by adding the new variable and the associated inequality constraints to the model.

        :param z: The variable representing the result of the AND operation.
        :type z: Variable
        :param x1: The first variable operand of the logical AND operation.
        :type x1: Variable
        :param x2: The constant value representing the second operand in the logical AND operation.
        :type x2: float
        :param milp: The MILP helper instance used to create variables and add constraints to the model.
        :type milp: MILPHelper
        """

        y: Variable = milp.get_new_variable(VariableType.BINARY)
        # If y = 0, z >= x1
        milp.add_new_constraint(
            Expression(Term(1.0, y), Term(1.0, z), Term(-1.0, x1)),
            InequalityType.GREATER_THAN,
        )
        # If y = 1, z >= x2
        milp.add_new_constraint(
            Expression(1.0, Term(-1.0, y), Term(1.0, z)),
            InequalityType.GREATER_THAN,
            x2,
        )

    @staticmethod
    def solve_or(ass: Assertion, kb: KnowledgeBase) -> None:
        """
        This static method encodes a fuzzy disjunction assertion into the Mixed-Integer Linear Programming (MILP) model associated with the given Knowledge Base. It processes the assertion by extracting the individual and the composite concept, verifying that the concept contains a list of constituent sub-concepts. The method retrieves the MILP variable representing the assertion itself, as well as the variables representing the individual's membership degrees for each sub-concept. It then applies Zadeh's OR operator constraints to link these variables within the MILP solver. As a side effect, the method updates the Knowledge Base's internal counters for binary and 0-1 variables to reflect the complexity added by the disjunction logic and registers the constituent sub-concepts as assertions within the base.

        :param ass: The fuzzy assertion representing a disjunction (OR) relationship to be resolved. It provides the individual and composite concept structure necessary to formulate the corresponding logical constraints and variables.
        :type ass: Assertion
        :param kb: The reference fuzzy knowledge base containing the MILP model, which is updated to incorporate the disjunction logic, update variable counters, and store new assertions.
        :type kb: KnowledgeBase
        """

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
        """
        Resolves an existential restriction fuzzy assertion by identifying or instantiating a filler individual that satisfies the specified role and concept constraints. If the role is functional and the subject individual already participates in such a role, the existing target individual is reused; otherwise, a new individual is generated, with special handling for concrete data types. The method updates the knowledge base by adding the new relation and concept assertion, and it enforces a fuzzy logic constraint ensuring the degree of the original assertion does not exceed the t-norm of the relation degree and the concept degree. Furthermore, it propagates these changes to inverse roles by adding corresponding relations and resolving role inclusion axioms.

        :param ass: The existential restriction fuzzy assertion to be solved, representing a constraint requiring the existence of a related individual with a specific concept.
        :type ass: Assertion
        :param kb: The fuzzy knowledge base serving as the context and state container for the solving process, providing access to rules, individuals, and the MILP solver.
        :type kb: KnowledgeBase
        """

        a: Individual = ass.get_individual()
        concept: AllSomeConcept = typing.cast(AllSomeConcept, ass.get_concept())
        role: str = concept.role
        c: Concept = concept.curr_concept
        kb.rules_applied[KnowledgeBaseRules.RULE_GOEDEL_SOME] += 1

        # Concept simplification
        if role in kb.functional_roles and role in a.role_relations:
            rel_set: list[Relation] = a.role_relations[role]
            b: Individual = rel_set[0].get_object_individual()
        elif kb.is_concrete_type(c):
            b: Individual = kb.get_new_concrete_individual(a, role)
        else:
            b: Individual = kb.get_new_individual(a, role)

        r_var: Variable = kb.milp.get_variable(a, b, role)
        c_var: Variable = kb.milp.get_variable(b, c)
        # b:C >= x_{b:C}
        kb.add_assertion(b, c, DegreeVariable.get_degree(c_var))
        # (a,b):R >= x_{(a:b):R}
        r: Relation = IndividualHandler.add_relation(
            a, role, b, DegreeVariable.get_degree(r_var), kb
        )
        # xAss <= x_{b:C} \otimes x_{(a:b):R}
        x_ass: Variable = kb.milp.get_variable(ass)
        ZadehSolver.and_leq_equation(x_ass, c_var, r_var, kb.milp)
        kb.solve_role_inclusion_axioms(a, r)
        # For every inverse role
        list_inverse_roles: list[str] = kb.inverse_roles.get(concept.role, [])
        for inv_role in list_inverse_roles:
            # (b,a):inv(R) >= l
            IndividualHandler.add_relation(
                b, inv_role, ass.get_individual(), DegreeVariable.get_degree(r_var), kb
            )
            kb.solve_role_inclusion_axioms(b, r)

    @staticmethod
    def solve_all(rel: Relation, restrict: Restriction, kb: KnowledgeBase) -> None:
        """
        Resolves a universal restriction fuzzy assertion by encoding logical constraints into the reference fuzzy knowledge base's MILP solver. It distinguishes between `HasValueRestriction` and standard concept restrictions, creating the necessary variables and adding corresponding assertions to the knowledge base. The method explicitly handles transitive roles and their hierarchical children, applying specific implication rules to ensure logical consistency across the role hierarchy. Finally, it establishes the core constraint linking the subject's universal restriction, the relation degree, and the object's membership in the target concept using Kleene-Dienes implication, while also tracking rule application and adjusting variable counts for non-numeric degrees.

        :param rel: The specific relation instance connecting the subject and object individuals, providing the truth degree and context for the universal restriction.
        :type rel: Relation
        :param restrict: The universal restriction assertion to be solved, defining the condition (concept or individual value) that must hold for all fillers of the associated role.
        :type restrict: Restriction
        :param kb: The reference fuzzy knowledge base providing the MILP solver, role definitions, and storage for assertions and variables.
        :type kb: KnowledgeBase
        """

        if not rel.get_degree().is_numeric() or not restrict.get_degree().is_numeric():
            kb.old_01_variables += 1

        b: Individual = rel.get_object_individual()
        # Has value restriction
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
            # xForAll  \leq  xRel \Rightarrow xForAllB
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
                # xForAll  \leq  xRel \Rightarrow xForAllB
                a: Individual = rel.get_subject_individual()
                x_for_all: Variable = kb.milp.get_variable(a, restrict)
                x_rel: Variable = kb.milp.get_variable(rel)
                ZadehSolver.kleene_dienes_implies_equation(
                    x_for_all, x_rel, x_for_all_b, kb.milp
                )

        # xForAll  \leq xRel  \Rightarrow  xBinC
        x_rel: Variable = kb.milp.get_variable(rel)
        x_for_all: Variable = kb.milp.get_variable(
            rel.get_subject_individual(), restrict
        )
        ZadehSolver.kleene_dienes_implies_equation(x_for_all, x_rel, x_B_in_C, kb.milp)

    @staticmethod
    def kleene_dienes_implies_equation(
        z: Variable, x1: Variable, x2: Variable, milp: MILPHelper
    ) -> None:
        """
        Enforces the constraint that the variable `z` is less than or equal to the Kleene-Dienes implication of `x1` and `x2`, which is defined as $\max(1 - x_1, x_2)$. This method linearizes the non-linear maximum operation by introducing a new binary auxiliary variable into the MILP model, which acts as a switch to select the active term of the implication. Consequently, it adds two linear inequality constraints to the provided MILP helper instance to define the relationship between `z`, `x1`, `x2`, and the auxiliary variable. Note that this implementation only restricts `z` from above, meaning `z` may be strictly less than the implication value depending on the broader optimization context.

        :param z: The variable representing the result of the Kleene-Dienes implication operation.
        :type z: Variable
        :param x1: The variable representing the antecedent of the Kleene-Dienes implication.
        :type x1: Variable
        :param x2: The variable representing the consequent (right-hand side) of the Kleene-Dienes implication operation.
        :type x2: Variable
        :param milp: The MILP helper object used to introduce auxiliary variables and add constraints to the model.
        :type milp: MILPHelper
        """

        y: Variable = milp.get_new_variable(VariableType.BINARY)
        # If y=0: x2  \geq  z
        milp.add_new_constraint(
            Expression(Term(1.0, x2), Term(1.0, y), Term(-1.0, z)),
            InequalityType.GREATER_THAN,
        )
        # If y=1: 1 - x1 \geq  z
        milp.add_new_constraint(
            Expression(2.0, Term(-1.0, y), Term(-1.0, z), Term(-1.0, x1)),
            InequalityType.GREATER_THAN,
        )

    @staticmethod
    def goedel_implies_equation(
        z: Variable, x1: Variable, x2: Variable, milp: MILPHelper
    ) -> None:
        """
        Encodes the Gödel implication operation $z = x1 \rightarrow x2$ into the Mixed-Integer Linear Programming (MILP) model represented by the helper object. This logical operation is defined such that the result $z$ is 1 if $x1$ is less than or equal to $x2$, and $z$ is equal to $x2$ otherwise. To linearize this conditional relationship, the method introduces an auxiliary binary variable and adds five linear constraints to the MILP solver, effectively enforcing the correct value for $z$ based on the relationship between $x1$ and $x2$. The function modifies the state of the MILP helper by registering the new variable and constraints but does not return a value.

        :param z: Variable to hold the result of the Gödel implication operation between x1 and x2.
        :type z: Variable
        :param x1: The variable representing the antecedent (left-hand side) of the Gödel implication.
        :type x1: Variable
        :param x2: The consequent variable in the Gödel implication $x1 \to x2$.
        :type x2: Variable
        :param milp: Helper object for the MILP model used to create auxiliary variables and add constraints.
        :type milp: MILPHelper
        """

        y: Variable = milp.get_new_variable(VariableType.BINARY)
        # 2y + x1 \geq x2 + \epsilon
        milp.add_new_constraint(
            Expression(Term(2.0, y), Term(1.0, x1), Term(-1.0, x2)),
            InequalityType.GREATER_THAN,
            ConfigReader.EPSILON,
        )
        # y + x2 \geq z
        milp.add_new_constraint(
            Expression(Term(1.0, y), Term(1.0, x2), Term(-1.0, z)),
            InequalityType.GREATER_THAN,
        )
        # x2 \leq z + y
        milp.add_new_constraint(
            Expression(Term(1.0, x2), Term(-1.0, z), Term(-1.0, y)),
            InequalityType.LESS_THAN,
        )
        # z \geq y
        milp.add_new_constraint(
            Expression(Term(1.0, z), Term(-1.0, y)), InequalityType.GREATER_THAN
        )
        # x1 \leq x2 + (1 - y)
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
        """
        Formulates the linear constraints necessary to represent the Zadeh implication operation $z = x_1 \to x_2$ within a Mixed-Integer Linear Programming (MILP) model. The method dispatches to specific internal implementations based on whether the result $z$ is provided as a decision variable or a constant float. It requires two input variables and a MILP helper object to construct and add the relevant constraints to the solver. The method performs strict type checking on the arguments and will raise a ValueError if the result type is unsupported or assertion errors if the input types are invalid.

        :param args: A tuple containing the result (Variable or numeric constant), two operand Variables, and a MILPHelper instance.
        :type args: typing.Any

        :raises ValueError: Raised if the first argument is not a number or a Variable.
        """

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
        """
        Encodes the Zadeh implication operation ($x_1 \to x_2$) into the Mixed-Integer Linear Programming (MILP) model by enforcing the relationship $z = x_1 \text{ Z-implies } x_2$. This implementation introduces an auxiliary binary variable to linearize the logical relationship and adds three specific linear constraints to the model via the provided `MILPHelper` instance. The method modifies the MILP model in place by adding the new variable and constraints, and it relies on a small epsilon value to handle strict inequality requirements.

        :param z: The variable to be constrained to the result of the Zadeh implication between x1 and x2.
        :type z: Variable
        :param x1: The antecedent variable in the Z-implication operation.
        :type x1: Variable
        :param x2: The consequent variable in the Z-implies operation.
        :type x2: Variable
        :param milp: Helper object for the MILP model used to introduce auxiliary variables and add constraints.
        :type milp: MILPHelper
        """

        y: Variable = milp.get_new_variable(VariableType.BINARY)
        # 2y + x1 \geq x2 + \epsilon
        milp.add_new_constraint(
            Expression(Term(2.0, y), Term(1.0, x1), Term(-1.0, x2)),
            InequalityType.GREATER_THAN,
            ConfigReader.EPSILON,
        )
        # z = y
        milp.add_new_constraint(
            Expression(Term(1.0, z), Term(-1.0, y)), InequalityType.EQUAL
        )
        # x1 \leq x2 + (1 - y)
        milp.add_new_constraint(
            Expression(-1.0, Term(1.0, x1), Term(-1.0, x2), Term(1.0, y)),
            InequalityType.LESS_THAN,
        )

    @staticmethod
    def __zadeh_implies_equation_2(
        z: float, x1: Variable, x2: Variable, milp: MILPHelper
    ) -> None:
        """
        This method adds constraints to the provided MILP helper to model the Zadeh implication operation between two variables, `x1` and `x2`, storing the result in `z`. It introduces a new binary auxiliary variable to linearize the logic, enforcing that `z` equals 1 if `x1` is less than or equal to `x2`, and 0 otherwise. The implementation relies on a small epsilon constant to handle the strict inequality boundary for the "false" case. As a side effect, this method modifies the `MILPHelper` object by adding the new variable and the necessary linear constraints to the model.

        :param z: Variable representing the result of the Z-implication operation between x1 and x2.
        :type z: float
        :param x1: The antecedent variable in the Z-implication operation.
        :type x1: Variable
        :param x2: The second operand of the Z-implication operation.
        :type x2: Variable
        :param milp: Helper object used to interface with the MILP model, responsible for creating auxiliary variables and adding the linear constraints that define the Z-implies relationship.
        :type milp: MILPHelper
        """

        y: Variable = milp.get_new_variable(VariableType.BINARY)
        # 2y + x1 \geq x2 + \epsilon
        milp.add_new_constraint(
            Expression(Term(2.0, y), Term(1.0, x1), Term(-1.0, x2)),
            InequalityType.GREATER_THAN,
            ConfigReader.EPSILON,
        )
        # z = y
        milp.add_new_constraint(Expression(z, Term(-1.0, y)), InequalityType.EQUAL)
        # x1 \leq x2 + (1 - y)
        milp.add_new_constraint(
            Expression(-1.0, Term(1.0, x1), Term(-1.0, x2), Term(1.0, y)),
            InequalityType.LESS_THAN,
        )

    @staticmethod
    def zadeh_implies_leq_equation(
        z: Variable, x1: Variable, x2: Variable, milp: MILPHelper
    ) -> None:
        """
        Adds a linear constraint to the MILP model to enforce that the variable `z` is less than or equal to the result of the Zadeh implication operation between `x1` and `x2`. The method implements the inequality $z \le 1 - x_1 + x_2$, which accurately models the upper bound of the implication under the assumption that `x1` is a binary variable. This operation modifies the `milp` helper instance by registering the new constraint, thereby restricting the solution space of the optimization problem.

        :param z: The variable representing the result of the Z-implication operation.
        :type z: Variable
        :param x1: The first operand of the Z-implies operation, which is a binary variable.
        :type x1: Variable
        :param x2: The second operand of the Zadeh implication, representing the consequent in the logical relationship $x1 \to x2$.
        :type x2: Variable
        :param milp: Helper object used to add the generated constraint to the model.
        :type milp: MILPHelper
        """

        milp.add_new_constraint(
            Expression(1.0, Term(-1.0, x1), Term(1.0, x2), Term(-1.0, z)),
            InequalityType.GREATER_THAN,
        )

    @staticmethod
    def goedel_not_equation(y: Variable, z: Variable, milp: MILPHelper) -> None:
        """
        This method enforces the logical relationship $y = \neg z$ by adding linear constraints to the provided MILP helper object. It ensures that the result variable `y` is configured as a binary variable, modifying its type if necessary. The implementation adds two inequalities: one ensuring that `y` is less than or equal to the complement of `z`, and another ensuring that the sum of `y` and `z` is at least a small epsilon value, thereby forcing `y` to be 1 whenever `z` is 0.

        :param y: The variable representing the result of the logical NOT operation.
        :type y: Variable
        :param z: The variable representing the operand of the logical NOT operation.
        :type z: Variable
        :param milp: Helper object used to add the linear constraints enforcing the logical relationship.
        :type milp: MILPHelper
        """

        if y.get_type() != VariableType.BINARY:
            y.set_type(VariableType.BINARY)

        # y \leq 1 - z
        milp.add_new_constraint(
            Expression(-1.0, Term(1.0, z), Term(1.0, y)),
            InequalityType.LESS_THAN,
        )
        # z + y \geq \epsilon
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
        """
        Encodes the logical OR operation as a set of linear constraints within a Mixed-Integer Linear Programming (MILP) model, allowing the solver to represent the relationship $z = x_1 \lor x_2 \lor \dots$. This static method acts as a dispatcher that validates the input arguments and delegates to the appropriate internal implementation based on the number of arguments provided. It supports two distinct signatures: a three-argument form accepting a list of input variables, a result variable, and a MILP helper, and a four-argument form accepting two input variables, a numeric constant, and a MILP helper. The method modifies the MILP model by adding constraints through the helper object and returns None. It raises an AssertionError if the arguments do not conform to the expected types or counts.

        :param args: Arguments for the OR operation, provided as either a list of input variables, the result variable, and a MILP helper, or as two input variables, a numeric constant, and a MILP helper.
        :type args: typing.Any
        """

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
        """
        Encodes the logical OR operation `z = x1 OR x2` into the Mixed-Integer Linear Programming (MILP) model by adding linear constraints to the provided helper object. This method specifically handles the case where the second operand `x2` is a constant float value, while `x1` and `z` are decision variables. To linearize the logical relationship, it introduces a new binary auxiliary variable and adds four inequalities that enforce the condition that `z` is 1 if either `x1` or `x2` is 1, and 0 otherwise. As a side effect, this method modifies the `MILPHelper` instance by registering the new variable and the associated constraints.

        :param z: The output variable representing the result of the logical OR operation.
        :type z: Variable
        :param x1: The first variable operand in the logical OR operation.
        :type x1: Variable
        :param x2: The constant float value representing the second operand of the logical OR operation.
        :type x2: float
        :param milp: The MILP helper instance used to create auxiliary variables and add the linear constraints required to model the OR operation.
        :type milp: MILPHelper
        """

        y: Variable = milp.get_new_variable(VariableType.BINARY)
        # z  \geq x1
        milp.add_new_constraint(
            Expression(Term(1.0, z), Term(-1.0, x1)), InequalityType.GREATER_THAN
        )
        # z \geq x2
        milp.add_new_constraint(
            Expression(Term(1.0, z)), InequalityType.GREATER_THAN, x2
        )
        # x1 + y \geq z
        milp.add_new_constraint(
            Expression(Term(1.0, x1), Term(1.0, y), Term(-1.0, z)),
            InequalityType.GREATER_THAN,
        )
        # x_2 + (1-y) \geq z
        milp.add_new_constraint(
            Expression(1.0 + x2, Term(-1.0, y), Term(-1.0, z)),
            InequalityType.GREATER_THAN,
        )

    @staticmethod
    def __or_equation_2(x: list[Variable], z: Variable, milp: MILPHelper) -> None:
        """
        This static method implements a logarithmic formulation to model the logical OR operation $z = x_1 \lor x_2 \lor \dots \lor x_N$ within a Mixed-Integer Linear Programming (MILP) context. It adds constraints to the provided `MILPHelper` instance to ensure the result variable `z` is true if and only if at least one variable in the input list `x` is true. The method introduces a set of new binary auxiliary variables to the model, which allows the number of constraints to scale logarithmically with the size of the input list, offering efficiency gains over standard linear formulations for large $N$. As a side effect, this method modifies the `milp` object by creating these auxiliary variables and appending the new constraints to the solver. Note that the implementation assumes the input list is non-empty, as it calculates the logarithm of the list length.

        :param x: A list of decision variables representing the operands of the logical OR operation.
        :type x: list[Variable]
        :param z: The output variable constrained to equal the logical OR of the input variables.
        :type z: Variable
        :param milp: Helper object used to add constraints and create auxiliary binary variables.
        :type milp: MILPHelper
        """

        N: int = len(x)
        M: float = Util.log2(N)
        # z \geq x_i
        for xi in x:
            milp.add_new_constraint(
                Expression(Term(1.0, z), Term(-1.0, xi)), InequalityType.GREATER_THAN
            )
        # y \in {0,1}
        y: list[Variable] = [
            milp.get_new_variable(VariableType.BINARY) for _ in range(int(M))
        ]
        # x_{i} + \sum_{j=1}^{m} e_{ij} \geq z
        for i, xi in enumerate(x):
            remainder: int = i
            exp: Expression = Expression(Term(-1.0, z), Term(1.0, xi))
            for n in range(int(M)):
                if remainder % 2 == 0:
                    exp.add_term(Term(1.0, y[n]))
                else:
                    exp.add_term(Term(-1.0, y[n]))
                    exp.increment_constant()
                remainder //= 2
            i += 1
            milp.add_new_constraint(exp, InequalityType.GREATER_THAN)

        # \sum_{j=1}^{m} 2^{j-1} y_{j} \leq n-1
        exp2: Expression = Expression(1.0 - N)
        k: float = 1.0
        for m in range(int(M)):
            exp2.add_term(Term(k, y[m]))
            k *= 2.0
        milp.add_new_constraint(exp2, InequalityType.LESS_THAN)

    @staticmethod
    def or_negated_equation(
        z: Variable, x1: Variable, x2: float, milp: MILPHelper
    ) -> None:
        """
        Encodes the logical relationship $z = (1 - x_1) \lor x_2$ into the provided MILP model by adding linear constraints. This ensures that the variable $z$ is equivalent to the maximum of $(1 - x_1)$ and the constant $x_2$. The implementation introduces a new auxiliary binary variable to the model to handle the disjunction logic and adds four specific inequality constraints to enforce the correct upper and lower bounds on $z$. The method modifies the MILP helper in place by registering these new variables and constraints.

        :param z: The variable representing the result of the logical operation (1 - x1) OR x2.
        :type z: Variable
        :param x1: The first operand variable, which is negated in the logical expression.
        :type x1: Variable
        :param x2: The constant value serving as the second operand in the OR operation.
        :type x2: float
        :param milp: Helper instance used to create auxiliary variables and add the necessary linear constraints to the model.
        :type milp: MILPHelper
        """

        y: Variable = milp.get_new_variable(VariableType.BINARY)

        # z  \geq (1 - x1)
        milp.add_new_constraint(
            Expression(1.0, Term(1.0, z), Term(1.0, x1)), InequalityType.GREATER_THAN
        )
        # z  \geq x2
        milp.add_new_constraint(
            Expression(Term(1.0, z)), InequalityType.GREATER_THAN, x2
        )
        # (1 - x1) + y \geq z
        milp.add_new_constraint(
            Expression(1.0, Term(-1.0, x1), Term(1.0, y), Term(-1.0, z)),
            InequalityType.GREATER_THAN,
        )
        # x_2 + (1-y) \geq z
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
        """
        Calculates the logical conjunction of two values using the Gödel t-norm, which serves as the standard fuzzy logic interpretation for the AND operation. This method returns the minimum of the two input floating-point numbers, effectively determining the degree of truth shared by both operands. While typically used with values between 0 and 1, the function does not enforce this range and will compute the minimum for any comparable numeric inputs. It is a pure function with no side effects on the input arguments or the surrounding state.

        :param n1: The first operand for the Gödel t-norm operation.
        :type n1: float
        :param n2: The second operand for the Gödel t-norm operation.
        :type n2: float

        :return: The minimum of the two input values, representing the Gödel t-norm.

        :rtype: float
        """

        return min(n1, n2)


@class_debugging()
class ClassicalSolver:
    """This class serves as a solver for classical logic semantics, providing static methods to evaluate and resolve fuzzy assertions against a knowledge base. It handles logical operations such as conjunctions, disjunctions, and existential or universal restrictions by modifying the knowledge base in place. The implementation combines specific fuzzy logic strategies, delegating conjunction and restriction operations to the Zadeh solver while utilizing the Lukasiewicz solver for disjunctions."""

    @staticmethod
    def solve_and(ass: Assertion, kb: KnowledgeBase) -> None:
        """
        Evaluates a conjunction fuzzy assertion by leveraging a reference fuzzy knowledge base to determine its validity or truth degree. This static method acts as a wrapper that delegates the specific solving logic to the ZadehSolver implementation. The operation modifies the provided assertion object in place rather than returning a new value, ensuring the assertion reflects the result of the evaluation against the knowledge base.

        :param ass: The fuzzy assertion representing a conjunction to be solved.
        :type ass: Assertion
        :param kb: The fuzzy knowledge base serving as the reference context for solving the assertion.
        :type kb: KnowledgeBase
        """

        ZadehSolver.solve_and(ass, kb)

    @staticmethod
    def solve_or(ass: Assertion, kb: KnowledgeBase) -> None:
        """
        Resolves a disjunction assertion by applying logical constraints derived from the provided knowledge base. This static method delegates the core resolution logic to the Łukasiewicz solver, updating the state of the assertion in place to reflect the solution. It specifically handles assertions representing a logical OR operation, ensuring consistency with the fuzzy logic rules defined in the reference knowledge base.

        :param ass: The disjunction fuzzy assertion to be solved.
        :type ass: Assertion
        :param kb: The reference fuzzy knowledge base against which the assertion is solved.
        :type kb: KnowledgeBase
        """

        LukasiewiczSolver.solve_or(ass, kb)

    @staticmethod
    def solve_some(ass: Assertion, kb: KnowledgeBase) -> None:
        """
        Resolves an existential restriction fuzzy assertion by evaluating it against the provided fuzzy knowledge base. This static method delegates the core computational logic to the `ZadehSolver`, effectively applying Zadeh's logic operators to determine the assertion's validity. As the function returns `None`, the operation results in a side effect that modifies the input `Assertion` object in place with the calculated solution.

        :param ass: The existential restriction fuzzy assertion to be solved.
        :type ass: Assertion
        :param kb: The fuzzy knowledge base serving as the reference context for solving the assertion.
        :type kb: KnowledgeBase
        """

        ZadehSolver.solve_some(ass, kb)

    @staticmethod
    def solve_all(rel: Relation, restrict: Restriction, kb: KnowledgeBase) -> None:
        """
        Resolves a universal restriction fuzzy assertion by integrating it into a reference fuzzy Knowledge Base. This static method accepts a specific relation and restriction, then delegates the core solving logic to the ZadehSolver implementation. The operation modifies the Knowledge Base in place, applying the constraints defined by the universal restriction to the existing data without returning a value.

        :param rel: The relation over which the universal restriction is applied.
        :type rel: Relation
        :param restrict: The restriction condition to be applied.
        :type restrict: Restriction
        :param kb: The reference fuzzy knowledge base against which the universal restriction is solved.
        :type kb: KnowledgeBase
        """

        ZadehSolver.solve_all(rel, restrict, kb)


@class_debugging()
class IndividualHandler:
    """
    This class serves as a static utility for managing the lifecycle and constraints of individuals within a fuzzy knowledge base, specifically focusing on the creation of relations and the application of semantic restrictions. It provides methods to add relations between individuals, automatically updating the underlying Mixed-Integer Linear Programming (MILP) model with necessary constraints, handling inverse roles, and resolving conflicts by updating relation degrees when appropriate. Furthermore, it facilitates the addition of various restriction types—such as universal, hasValue, and not-self rules—applying them to existing relations and delegating the solving logic to specific solvers based on the configured fuzzy logic type (e.g., Lukasiewicz, Zadeh, or Classical). The class also interacts with blocking mechanisms to optimize reasoning performance by unblocking individuals when new restrictions are applied.

    :raises ValueError: Raised when the arguments provided to `add_restriction` do not match the expected types for either a concept-based or an individual-based restriction.
    """

    @staticmethod
    def add_relation(
        ind: Individual,
        role_name: str,
        b: Individual,
        degree: Degree,
        kb: KnowledgeBase,
    ) -> typing.Optional[Relation]:
        """
        Adds a relation between a source individual and a target individual with a specified role name and degree to the knowledge base. The method first checks for existing relations with the same role and target; if the degree is numeric, it only updates the relation if the new degree is greater than the existing one, otherwise the operation is skipped. Upon successfully adding a new relation, the method increments the global relation counter, updates the source individual's internal relation mapping, and adds corresponding constraints to the MILP solver to enforce logical consistency. Additionally, if the knowledge base is in a loaded state, it triggers the application of domain, range, and inverse restrictions, as well as specific role restrictions and "not-self" rules defined for the source individual.

        :param ind: The individual acting as the source or subject of the relation.
        :type ind: Individual
        :param role_name: The identifier for the specific type or predicate of the relationship to be established between the source and target individuals.
        :type role_name: str
        :param b: The individual acting as the object or target of the relation.
        :type b: Individual
        :param degree: The intensity or value of the relation, used to determine precedence over existing relations and to define constraints in the knowledge base.
        :type degree: Degree
        :param kb: The knowledge base instance that stores the relation and enforces associated MILP constraints and rule restrictions.
        :type kb: KnowledgeBase

        :return: The Relation object representing the link between the source and target individuals with the specified role and degree.

        :rtype: typing.Optional[Relation]
        """

        #  We check if the relation already exists when both degrees are double
        add_new_rel: bool = True
        rels: list[Relation] = ind.role_relations.get(role_name, [])
        rel: Relation = Relation(role_name, ind, b, degree)

        if degree.is_numeric():
            new_degree: float = typing.cast(DegreeNumeric, degree).get_numerical_value()
            # Check relation does not exist
            for i in range(len(rels)):
                old_rel: Relation = rels[i]
                old_role: str = old_rel.get_role_name()
                old_ind: Individual = old_rel.get_object_individual()
                # If there exists b similar relation, stop the loop. Do not add b new relation
                if (
                    b == old_ind
                    and old_role == role_name
                    and old_rel.get_degree().is_numeric()
                ):
                    add_new_rel = False
                    old_degree: float = typing.cast(
                        DegreeNumeric, old_rel.get_degree()
                    ).get_numerical_value()
                    # If the existing relation has a smaller degree, replace it
                    if new_degree > old_degree:
                        add_new_rel = False
                        rels[i] = rel
                        ind.role_relations[role_name] = rels
                    Util.debug(
                        f"Relation {ind.name}, {b} through role {role_name} has already been processed hence ignored"
                    )
                    break
        # If not, add new relation to the list
        if add_new_rel:
            Util.debug(f"Adding ({ind}, {b}): {role_name}")
            kb.num_relations += 1
            rels.append(rel)
            ind.role_relations[role_name] = rels
            # Add MILP restriction
            ass_var: Variable = kb.milp.get_variable(rel)
            # If the degree is not x_{(a,b):R}
            if str(degree) != str(ass_var):
                kb.milp.add_new_constraint(
                    Expression(Term(1.0, ass_var)), InequalityType.GREATER_THAN, degree
                )
            # x_{b : {b} } >= x_{(a,b):R}
            b_is_B: Variable = kb.milp.get_nominal_variable(str(b))
            kb.milp.add_new_constraint(
                Expression(Term(1.0, b_is_B), Term(-1.0, ass_var)),
                InequalityType.GREATER_THAN,
            )
            # Show abstract fillers
            if kb.milp.show_vars.show_abstract_role_fillers(role_name, str(ind)):
                kb.milp.show_vars.add_individual_to_show(str(b))
            if kb.is_loaded():
                # Apply domain restrictions
                for r in kb.domain_restrictions:
                    kb.rule_domain_lazy_unfolding(r, rel)
                # Apply range restrictions
                for r in kb.range_restrictions:
                    kb.rule_range_lazy_unfolding(r, rel)
                # Add inverse restriction
                if role_name in kb.inverse_roles:
                    var1: Variable = kb.milp.get_variable(ind, b, role_name)
                    for inv_role in kb.inverse_roles.get(role_name):
                        var2: Variable = kb.milp.get_variable(b, ind, inv_role)
                        kb.milp.add_new_constraint(
                            Expression(Term(1.0, var1), Term(-1.0, var2)),
                            InequalityType.EQUAL,
                        )
            # Apply restrictions with same role name as the created relation
            restricts: list[Restriction] = ind.role_restrictions.get(role_name, [])
            for r in restricts:
                IndividualHandler.solve_relation_restriction(rel, r, kb)
            # Apply not-self rule
            if b == ind and role_name in ind.not_self_roles:
                IndividualHandler.solve_not_self_rule(ind, role_name, kb)
        return rel

    @staticmethod
    def solve_not_self_rule(ind: Individual, role_name: str, kb: KnowledgeBase) -> None:
        """
        Enforces a consistency constraint within the knowledge base's MILP solver linking an individual's self-relation to its membership in the negation of the self-restriction concept. It retrieves the binary variable representing the degree of the relation where the individual is related to itself via the specified role, as well as the binary variable representing the degree to which the individual satisfies the negation of the self-restriction concept. The method adds an equality constraint requiring the sum of these two variables to be one, which effectively forces the variables to be logical negations of one another given their binary nature. This operation modifies the internal state of the MILP model by adding a new constraint.

        :param ind: The entity subject to the "not self" constraint.
        :type ind: Individual
        :param role_name: The name of the role used to define the self-restriction constraint.
        :type role_name: str
        :param kb: The knowledge base instance used to retrieve variables and add the new constraint.
        :type kb: KnowledgeBase
        """

        # (v,v):R
        var1: Variable = kb.milp.get_variable(ind, ind, role_name)
        # v:\neg \some R.Self
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
        """
        Applies a universal restriction to a specific relation associated with an individual within the provided knowledge base. The method determines the appropriate reasoning strategy by inspecting the logic type defined in the knowledge base—specifically Lukasiewicz, Zadeh, or Classical logic—and delegates the resolution to the corresponding solver. As a side effect, if dynamic blocking is enabled in the knowledge base configuration, the object individual associated with the relation is unblocked following the application of the restriction.

        :param rel: The relation instance to which the universal restriction is applied.
        :type rel: Relation
        :param restrict: The universal restriction constraint to be applied to the relation.
        :type restrict: Restriction
        :param kb: The knowledge base instance providing the logic type and configuration for the solving process.
        :type kb: KnowledgeBase
        """

        if kb.get_logic() == FuzzyLogic.LUKASIEWICZ:
            LukasiewiczSolver.solve_all(rel, restrict, kb)
        elif kb.get_logic() == FuzzyLogic.ZADEH:
            ZadehSolver.solve_all(rel, restrict, kb)
        elif kb.get_logic() == FuzzyLogic.CLASSICAL:
            ClassicalSolver.solve_all(rel, restrict, kb)
        # Dynamic blocking
        if kb.blocking_dynamic:
            CreatedIndividualHandler.unblock(rel.get_object_individual(), kb)

    @staticmethod
    def unblock_simple(ind: Individual, kb: KnowledgeBase) -> None:
        """
        Removes the blocking status for an individual by checking if the individual is listed as having directly blocked children within the knowledge base. If the individual is found in the knowledge base's registry of blocked parents, the method triggers the unblocking process for those children, effectively modifying the knowledge base's state. If the individual is not currently blocking any children, the method performs no action.

        :param ind: The individual whose children are to be unblocked.
        :type ind: Individual
        :param kb: The knowledge base instance containing the individual and managing its blocking status.
        :type kb: KnowledgeBase
        """

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
        """
        This method adds a fuzzy restriction to a specific individual within a knowledge base, acting as a dispatcher that delegates to internal logic based on the argument types. It requires exactly five arguments: the target `Individual`, a role name as a string, a restriction object (either a `Concept` or a string representing another individual's name), a `Degree` representing the truth value, and the `KnowledgeBase` to modify. Depending on whether the third argument is a `Concept` or a string, the method handles concept-based or individual-based restrictions, respectively. If the argument count is incorrect or the types do not match the expected signatures, the method raises an error, specifically a `ValueError` for type mismatches in the restriction object.

        :param args: A variable-length argument list containing exactly five elements that define the restriction. The arguments must correspond to either a concept-based restriction (Individual, role name, Concept, Degree, KnowledgeBase) or an individual-based restriction (Individual, role name, individual name, Degree, KnowledgeBase), distinguished by the type of the third argument.
        :type args: typing.Any

        :raises ValueError: Raised if the provided arguments do not match the expected types for either a concept-based or individual-based restriction.
        """

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
        """
        Creates a universal restriction defined by the specific role, concept, and degree, and associates it with the target individual within the knowledge base. The method delegates the implementation to a shared handler, which attaches the restriction to the individual and propagates the constraint to all existing relations linked by the specified role name. This operation modifies the internal state of the individual and its connected relations to enforce the new restriction.

        :param ind: The individual entity to which the universal restriction is applied.
        :type ind: Individual
        :param role_name: The name of the role to which the restriction applies.
        :type role_name: str
        :param c: The concept defining the range of the restriction.
        :type c: Concept
        :param degree: The quantifier or type of the restriction to be applied.
        :type degree: Degree
        :param kb: The knowledge base instance to which the restriction is applied.
        :type kb: KnowledgeBase
        """

        restrict: Restriction = Restriction(role_name, c, degree)
        IndividualHandler.common_part_add_restriction(ind, role_name, restrict, kb)

    def __add_restriction_2(
        ind: Individual,
        role_name: str,
        ind_name: str,
        degree: Degree,
        kb: KnowledgeBase,
    ) -> None:
        """
        This method constructs a `HasValueRestriction` object that binds a specific role to a target individual value, qualified by a given degree. It delegates the integration of this restriction to a shared helper routine, which updates the individual's internal list of constraints and registers the change within the provided Knowledge Base. As a result of this operation, the individual's state is modified to enforce the new restriction, and the knowledge base is updated to reflect this constraint, potentially influencing the validation of existing relationships.

        :param ind: The individual instance to which the hasValue restriction is applied.
        :type ind: Individual
        :param role_name: The name of the role (property) to which the restriction applies.
        :type role_name: str
        :param ind_name: The name of the individual that serves as the specific value for the hasValue restriction.
        :type ind_name: str
        :param degree: The degree value associated with the `hasValue` restriction.
        :type degree: Degree
        :param kb: The knowledge base to which the restriction is being added.
        :type kb: KnowledgeBase
        """

        restrict: HasValueRestriction = HasValueRestriction(role_name, ind_name, degree)
        IndividualHandler.common_part_add_restriction(ind, role_name, restrict, kb)

    @staticmethod
    def common_part_add_restriction(
        ind: Individual, role_name: str, restrict: Restriction, kb: KnowledgeBase
    ) -> None:
        """
        Appends a specific restriction to the list of constraints associated with a given role name on the target individual. Beyond simply storing the constraint, this method immediately enforces it against the current state of the knowledge base by iterating through all existing relations defined for that role and attempting to resolve the restriction for each one. This ensures that the new constraint is applied retroactively to pre-existing relationships.

        :param ind: The target individual to receive the restriction. The restriction is added to the individual's internal list and applied to all existing relations associated with the specified role.
        :type ind: Individual
        :param role_name: The identifier for the role or relationship type to which the restriction applies, used to categorize the restriction and target existing relations for enforcement.
        :type role_name: str
        :param restrict: The restriction to be appended to the individual's list of restrictions for the specified role and applied to all existing relations associated with that role.
        :type restrict: Restriction
        :param kb: The knowledge base context used to apply the restriction to existing relations.
        :type kb: KnowledgeBase
        """

        ind.role_restrictions[role_name] = ind.role_restrictions.get(role_name, []) + [
            restrict
        ]
        # Apply new restriction to all the existing relations via roleName
        rels: list[Relation] = ind.role_relations.get(role_name, [])
        for r in rels:
            Util.debug(f"Adding universal restriction {restrict} to relation {r}")
            IndividualHandler.solve_relation_restriction(r, restrict, kb)

    @staticmethod
    def add_not_self_restriction(ind: Individual, role: str, kb: KnowledgeBase) -> None:
        """
        Registers a "not self" restriction for a specific role on the provided individual, effectively preventing the individual from forming a reflexive relationship via that role. The method updates the individual's internal set of restricted roles, performing a no-op if the restriction is already present to ensure idempotency. Following the update, it inspects existing relations for the specified role to check for immediate violations; if the individual is currently related to itself via this role, a resolution routine is triggered to address the conflict within the knowledge base.

        :param ind: The individual entity to which the restriction is applied. This individual's list of restricted roles is updated, and its existing relations are checked for immediate violations.
        :type ind: Individual
        :param role: The name of the role (relationship) to which the "not self" restriction is applied.
        :type role: str
        :param kb: The knowledge base context used to resolve the restriction rule.
        :type kb: KnowledgeBase
        """

        if role in ind.not_self_roles:
            return
        # Add new self restriction to the list
        ind.not_self_roles.add(role)
        # Apply new restriction to all the existing relations via role_name
        rels: list[Relation] = ind.role_relations.get(role, [])
        for r in rels:
            if r.get_object_individual() == ind:
                IndividualHandler.solve_not_self_rule(role, kb)
                return


@class_debugging()
class CreatedIndividualHandler:
    """This class serves as a utility handler for individuals dynamically generated during the reasoning process within a fuzzy knowledge base, primarily focusing on the implementation of blocking strategies to ensure algorithm termination. It provides static methods to determine if an individual is directly or indirectly blocked based on various configurations such as subset, set, or pairwise blocking, comparing concept labels against ancestors or other nodes in the completion forest. Furthermore, it manages the unblocking procedure, which involves resetting the status of blocked nodes and re-queuing their associated assertions for processing. Beyond blocking logic, the class is responsible for updating role successor lists and retrieving or creating representative individuals for concrete features involving fuzzy numbers."""

    @staticmethod
    def update_role_successors(name: str, role_name: str, kb: KnowledgeBase) -> None:
        """
        Appends the specified individual name to the list of successors associated with the given role name within the provided knowledge base. If the role name is not None, the method ensures the role exists in the `r_successors` mapping—initializing a new list if necessary—and adds the individual to it. This operation modifies the knowledge base in place and triggers debug logging to reflect the updated state of the successor list.

        :param name: The name of the individual to be added as a successor for the specified role.
        :type name: str
        :param role_name: The specific role for which the successor list is being updated.
        :type role_name: str
        :param kb: The knowledge base instance containing the role-successor mappings to be updated.
        :type kb: KnowledgeBase
        """

        # update list of R-successors
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
        """
        Retrieves or creates a representative individual that corresponds to a set of entities satisfying a specific fuzzy inequality condition relative to the current individual. The method first checks if a representative for the given inequality type, feature name, and fuzzy number already exists; if found, it returns the cached instance to ensure consistency. If no such representative exists, it generates a new concrete individual within the provided KnowledgeBase, establishes a relationship between the current individual and the new one via a `RepresentativeIndividual` object, and appends this relationship to the current individual's list of representatives. The returned individual effectively represents the subset of individuals that are greater than or equal to (or less than or equal to) the specified fuzzy number for the given feature.

        :param current_individual: The individual for which the representative is being retrieved or created.
        :type current_individual: CreatedIndividual
        :param type: Specifies the inequality direction (e.g., GREATER_EQUAL, LESS_EQUAL) used to define the representative individual relative to the fuzzy number.
        :type type: InequalityType
        :param f_name: Name of the feature for which the representative individual serves as a filler.
        :type f_name: str
        :param f: The fuzzy number value used as the threshold to define the representative individual based on the specified inequality type.
        :type f: TriangularFuzzyNumber
        :param kb: The knowledge base instance used to create new concrete individuals.
        :type kb: KnowledgeBase

        :return: The representative individual corresponding to the specified fuzzy number and inequality type. Returns an existing individual if available, otherwise creates and returns a new one.

        :rtype: CreatedIndividual
        """

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
        Handles the unblocking of individuals within a pairwise blocking framework by examining the specific role of the provided individual in the blocking hierarchy. If the individual acts as a blocking node (Y), the method removes it from the parent's tracking list and unblocks all descendant nodes (X) that were directly blocked by it. Conversely, if the individual is a parent of blocking nodes (Y') or a parent of blocked nodes (X'), the method recursively triggers the unblocking of relevant child nodes. This process involves updating the knowledge base's internal tracking structures, specifically removing entries from the lists of directly blocked children, Y-prime individuals, and X-prime individuals, and invoking the unblock operation on affected nodes.

        :param current_individual: The individual node to be processed for unblocking, potentially acting as a blocking node, a Y-prime node, or an X-prime node.
        :type current_individual: CreatedIndividual
        :param kb: The knowledge base managing the individuals and the current blocking state.
        :type kb: KnowledgeBase
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
        """
        Reverses the blocked status of the provided individual, enabling further expansion or processing of the node within the tableau. The operation is contingent upon the knowledge base using dynamic blocking; if blocking is static or the input is not a CreatedIndividual, the method returns immediately without effect. Based on the specific blocking strategy configured in the knowledge base, the procedure varies: for subset or set blocking, it unblocks all children of the individual, whereas for pairwise blocking, it resolves mutual blocking relationships by unblocking both the individuals blocked by the current node and those that block it.

        :param current_individual: The target individual to be unblocked.
        :type current_individual: CreatedIndividual
        :param kb: The knowledge base containing the individual and the blocking configuration required to determine the unblocking strategy.
        :type kb: KnowledgeBase
        """

        b_type: BlockingDynamicType = kb.blocking_type
        dynamic: bool = kb.blocking_dynamic

        if not isinstance(current_individual, CreatedIndividual):
            return  # unblock only children of created individuals
        if not dynamic:
            return  # no unblock if not dynamic blocking

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
        Determines if a specific individual is indirectly blocked with respect to the given knowledge base, meaning that at least one of its ancestors is blocked. The behavior varies based on the blocking strategy configured in the knowledge base; for instance, if the blocking type is set to none, the method immediately returns false. For subset or set blocking strategies, indirect blocking is only evaluated if the knowledge base is configured for dynamic blocking, otherwise it returns false. The actual verification is delegated to specialized helper methods tailored to specific blocking types like double blocking or anywhere subset blocking. As a side effect, this method logs debug information regarding the individual being tested and its depth.

        :param current_individual:
        :type current_individual: CreatedIndividual
        :param kb: The knowledge base providing the context and blocking configuration (such as blocking type and dynamic settings) used to determine if the individual is indirectly blocked.
        :type kb: KnowledgeBase

        :return: True if the individual is indirectly blocked with respect to the knowledge base, meaning that at least one of its ancestors is blocked; otherwise, False.

        :rtype: bool
        """

        Util.debug(
            f'Testing indirect blocking "{current_individual}" at depth {current_individual.depth}'
        )
        type: BlockingDynamicType = kb.blocking_type
        dynamic: bool = kb.blocking_dynamic

        # Indirect blocking applies only if we have dynamic blocking
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
        Determines whether the specified individual is indirectly blocked with respect to the provided fuzzy knowledge base, specifically under subset or set blocking conditions. This is achieved by traversing the individual's ancestor chain to determine if any blockable ancestor is directly blocked. The method includes a depth optimization where individuals with a depth less than 4 are immediately considered not blocked. Additionally, it updates the individual's internal state to cache the result and records the specific ancestor responsible for the block, preventing redundant checks in future invocations.

        :param current_individual: The individual node to evaluate for indirect blocking by checking if any of its ancestors are blocked.
        :type current_individual: CreatedIndividual
        :param kb: The knowledge base against which the indirect blocking status is evaluated.
        :type kb: KnowledgeBase

        :return: True if the individual is indirectly blocked, which occurs if any of its blockable ancestors are directly blocked with respect to the knowledge base.

        :rtype: bool
        """

        # Don't test if not deep enough in completion forest
        if current_individual.depth < 4:
            Util.debug("Depth < 4, node is not indirectly blocked")
            current_individual.indirectly_blocked = (
                CreatedIndividualBlockingType.NOT_BLOCKED
            )
            return False
        # Check if already blocked
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
        # Proceed, assuming indirectlyBlocked == UNCHECKED holds
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
        """
        Determines whether the provided individual is indirectly blocked within the completion forest by traversing its ancestor chain to find a directly blocked ancestor, specifically handling SUBSET or SET blocking scenarios. The method enforces a depth threshold, immediately returning false for individuals at a depth less than three to avoid unnecessary computation. It utilizes memoization to prevent redundant checks, updating the individual's blocking status and recording the specific ancestor responsible for the block if one is found.

        :param current_individual: The individual to evaluate for indirect blocking based on the blocking status of its ancestors.
        :type current_individual: CreatedIndividual
        :param kb: The knowledge base against which the blocking status of the individual and its ancestors is evaluated.
        :type kb: KnowledgeBase

        :return: True if the individual is indirectly blocked because at least one of its blockable ancestors is directly blocked with respect to the knowledge base; False otherwise.

        :rtype: bool
        """

        # Don't test if not deep enough in completion forest
        if current_individual.depth < 3:
            Util.debug("Depth < 3, node is not indirectly anywhere blocked")
            current_individual.indirectly_blocked = (
                CreatedIndividualBlockingType.NOT_BLOCKED
            )
            return False
        # Check if already blocked
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
        # Proceed, assuming indirectlyBlocked == UNCHECKED holds
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
        """
        Evaluates whether the specified individual is indirectly blocked within the context of the provided knowledge base by examining its lineage. This condition is met if any blockable ancestor of the individual is determined to be directly blocked. The method implements a depth-based optimization, automatically returning False for individuals at a depth less than 5. Additionally, it manages side effects by updating the individual's blocking status attribute to cache the result and storing a reference to the ancestor responsible for the block, ensuring efficient subsequent checks.

        :param current_individual: The individual node to be evaluated for indirect blocking status.
        :type current_individual: CreatedIndividual
        :param kb: The knowledge base against which the blocking status of the individual's ancestors is evaluated.
        :type kb: KnowledgeBase

        :return: True if the individual is deep enough in the completion forest and has a blockable ancestor that is directly blocked with respect to the knowledge base, False otherwise.

        :rtype: bool
        """

        # Don't test if not deep enough in completion forest
        if current_individual.depth < 5:
            Util.debug("Depth < 5, node is not indirectly blocked")
            current_individual.indirectly_blocked = (
                CreatedIndividualBlockingType.NOT_BLOCKED
            )
            return False
        # Check if already blocked
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
        # Proceed, assuming indirectlyBlocked == UNCHECKED holds
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
        """
        Checks if the provided individual is indirectly anywhere pairwise blocked with respect to the knowledge base by traversing its ancestors to find one that is directly blocked. The method includes a depth optimization, immediately returning False for individuals at a depth less than 4. It also utilizes memoization to avoid redundant calculations, and as a side effect, it updates the individual's internal blocking status and records the blocking ancestor if one is found.

        :param current_individual: The individual node to evaluate for indirect anywhere pairwise blocking status.
        :type current_individual: CreatedIndividual
        :param kb: The knowledge base used to evaluate the blocking condition for the individual and its ancestors.
        :type kb: KnowledgeBase

        :return: True if the individual has a blockable ancestor that is directly blocked, False otherwise.

        :rtype: bool
        """

        # Don't test if not deep enough in completion forest
        if current_individual.depth < 4:
            Util.debug("Depth < 4, node is not indirectly anywhere pairwise blocked")
            current_individual.indirectly_blocked = (
                CreatedIndividualBlockingType.NOT_BLOCKED
            )
            return False
        # Check if already blocked
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
        # Proceed, assuming indirectlyBlocked == UNCHECKED holds
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
        Determines if the provided individual is directly blocked with respect to the given knowledge base by applying the blocking strategy currently configured in the knowledge base. This method functions as a dispatcher, selecting the appropriate blocking algorithm—such as simple, pairwise, or anywhere blocking—based on the `blocking_type` attribute. If the knowledge base specifies that no blocking should be applied, the method returns False immediately. Otherwise, it delegates the specific blocking check to corresponding helper methods within the handler.

        :param current_individual: The individual to check for direct blocking.
        :type current_individual: CreatedIndividual
        :param kb: The knowledge base providing the context and blocking configuration used to evaluate the individual.
        :type kb: KnowledgeBase

        :return: True if the individual is directly blocked according to the knowledge base's blocking strategy, False otherwise.

        :rtype: bool
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
        """
        Determines if the specified individual is directly blocked by an ancestor in the knowledge base, applicable to subset or set blocking mechanisms. The method first verifies that the individual has a depth of at least three, as shallower nodes are exempt from blocking checks. It then traverses the ancestor chain, comparing concept labels against blockable ancestors to identify a potential blocker. If a match is found, the individual is marked as blocked, the blocking ancestor is recorded, and the knowledge base is updated to reflect this relationship. Additionally, this operation triggers a side effect where all descendants of the blocked individual are marked as indirectly blocked. The method utilizes memoization to return cached results if the blocking status has already been determined.

        :param current_individual: The individual node to evaluate for direct blocking against its ancestors.
        :type current_individual: CreatedIndividual
        :param kb: The knowledge base used to compare concept labels and maintain the registry of directly blocked children.
        :type kb: KnowledgeBase

        :return: True if the individual is directly blocked by a blockable ancestor with matching concept labels, False otherwise.

        :rtype: bool
        """

        Util.debug(
            f"Directly Simple blocking status {current_individual.directly_blocked}"
        )
        # Don't test if not deep enough in completion forest
        if current_individual.depth < 3:
            Util.debug("Depth < 3, node is not blocked")
            current_individual.directly_blocked = (
                CreatedIndividualBlockingType.NOT_BLOCKED
            )
            return False
        # If already blocked don't test again
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
        # Proceed, assuming directlyBlocked == UNCHECKED holds
        # Direct blocking
        current_individual.directly_blocked = CreatedIndividualBlockingType.NOT_BLOCKED
        Util.debug(f"Testing direct blocking: {current_individual}")
        # Loops until the node is blocked or we reach the first root ancestor.
        anc: typing.Optional[Individual] = current_individual.get_parent()
        while anc and anc.is_blockable():
            ancestor: CreatedIndividual = typing.cast(CreatedIndividual, anc)
            Util.debug(
                f"Compare with created individual {ancestor.name} of depth {ancestor.depth}"
            )
            # Test if the concept labels matches
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
                # Mark all descendants as indirectly blocked
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
        """
        Determines whether the provided individual is directly blocked by another individual anywhere in the completion forest with respect to the given fuzzy knowledge base, applying subset or set blocking criteria. The method first validates that the individual is not a root node or too shallow in the tree (depth less than 2), as these conditions preclude blocking. If a matching blocking ancestor is found, the method updates the individual's internal state to blocked, records the blocking ancestor in the knowledge base's registry of blocked children, and recursively marks all descendants of the current individual as indirectly blocked.

        :param current_individual: The individual to be evaluated for direct anywhere simple blocking.
        :type current_individual: CreatedIndividual
        :param kb: The knowledge base used to determine if the individual is blocked and to update the blocking state.
        :type kb: KnowledgeBase

        :return: True if the individual is directly anywhere simple blocked with respect to the knowledge base, considering SUBSET or SET blocking cases; False otherwise.

        :rtype: bool
        """

        Util.debug(
            f"Directly Anywhere Simple blocking status {current_individual.directly_blocked}"
        )
        node_id: int = current_individual.get_integer_id()
        # Don't test if not deep enough in completion forest
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
        # If already blocked don't test again
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
        # Proceed, assuming directlyBlocked == UNCHECKED holds
        # Direct blocking
        current_individual.directly_blocked = CreatedIndividualBlockingType.NOT_BLOCKED
        Util.debug(f"Testing direct anywhere blocking: {current_individual}")
        # Find anywhere blocking node
        candidate_ind: SortedSet[CreatedIndividual] = (
            CreatedIndividualHandler.matching_individual(current_individual, kb)
        )
        Util.debug(f"Anywhere blocking: Found individuals: {candidate_ind}")
        # Check if we found one
        if len(candidate_ind) > 0:
            # pick the the first blocking node
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
            # Mark all descendants as indirectly blocked
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
        """
        Traverses the subtree rooted at the specified individual to mark blockable descendants as indirectly unblocked. The method utilizes a breadth-first search strategy, processing role relations to identify child nodes while explicitly excluding the parent node to prevent cycles. For each valid descendant encountered, it invokes the unblocking logic and continues the traversal, provided the relation is not a self-loop. This operation modifies the blocking status of individuals within the knowledge base without returning a value.

        :param current_individual: The individual serving as the root of the subtree to be marked as indirectly unblocked.
        :type current_individual: CreatedIndividual
        :param kb: The knowledge base containing the individuals, used to update their blocking status.
        :type kb: KnowledgeBase
        """

        Util.debug(
            f"{constants.SEPARATOR}MARK UNCHECKED subtree of: {current_individual.name}"
        )
        queue: deque[CreatedIndividual] = deque()
        queue.append(current_individual)
        while len(queue) > 0:
            ind: CreatedIndividual = queue.popleft()
            # If there are no descendants, skip
            if len(ind.role_relations) == 0:
                break
            for role in ind.role_relations:
                rels: list[Relation] = copy.deepcopy(ind.role_relations[role])
                for rel in rels:
                    Util.debug(
                        f"{rel.get_subject_individual()} has role {rel.get_role_name()} with filler {rel.get_object_individual()}"
                    )
                    son: Individual = rel.get_object_individual()
                    if son != ind.parent:  # not parent via inverse role
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
        """
        Determines whether the provided individual is directly pairwise blocked within the context of the given fuzzy knowledge base. The algorithm traverses the completion forest to identify a candidate ancestor node that satisfies the pairwise blocking criteria, which requires that the current node and the candidate share the same incoming role and that their concept labels match pairwise with their respective parents. This check is bypassed if the individual's depth is less than 4 or if the blocking status has already been cached. If a valid blocking ancestor is found, the method updates the individual's status to blocked, records the relationship in the knowledge base, and recursively marks all descendants of the current individual as indirectly blocked.

        :param current_individual: The individual node to be tested for direct pairwise blocking against other nodes in the completion forest.
        :type current_individual: CreatedIndividual
        :param kb: The knowledge base against which the blocking check is performed, providing concept definitions and storing blocking state.
        :type kb: KnowledgeBase

        :return: True if the individual is directly pairwise blocked by another individual in the completion forest based on matching concept and role labels; False otherwise.

        :rtype: bool
        """

        Util.debug(
            f"Directly pairwise blocking status {current_individual.directly_blocked}"
        )
        # Don't test if not deep enough in completion forest
        if current_individual.depth < 4:
            Util.debug("Depth < 4, node is not directly blocked")
            current_individual.directly_blocked = (
                CreatedIndividualBlockingType.NOT_BLOCKED
            )
            return False
        # If already blocked don't test again
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
        # Proceed, assuming directlyBlocked == UNCHECKED holds
        # Direct blocking
        current_individual.directly_blocked = CreatedIndividualBlockingType.NOT_BLOCKED
        Util.debug(f"Testing direct pair-wise blocking: {current_individual}")
        node_x_prime: CreatedIndividual = typing.cast(
            CreatedIndividual, current_individual.get_parent()
        )
        node_y: CreatedIndividual = typing.cast(
            CreatedIndividual, current_individual.get_parent()
        )
        # Test for direct blocking
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
                # We got a pair-wise direct blocking
                current_individual.directly_blocked = (
                    CreatedIndividualBlockingType.BLOCKED
                )
                current_individual.blocking_ancestor = str(node_y)
                blocked_children: list[str] = kb.directly_blocked_children.get(
                    current_individual.blocking_ancestor, []
                )
                # Add nodeX to blocked nodes of blocking node nodeY
                if current_individual.name not in blocked_children:
                    blocked_children.append(current_individual.name)
                kb.directly_blocked_children[current_individual.blocking_ancestor] = (
                    blocked_children
                )

                y_prime: str = str(node_y_prime)
                # Create a link from y' to y
                y_individuals: list[str] = []
                if y_prime in kb.y_prime_individuals:
                    y_individuals = kb.y_prime_individuals.get(y_prime)
                if current_individual.blocking_ancestor not in y_individuals:
                    y_individuals.append(current_individual.blocking_ancestor)
                # Given yprime, update the list of y nodes
                kb.y_prime_individuals[y_prime] = y_individuals
                x_prime: str = str(node_x_prime)
                # Create a link from x' to x
                x_individuals: list[str] = []
                if x_prime in kb.x_prime_individuals:
                    x_individuals = kb.x_prime_individuals.get(x_prime)
                if current_individual.name not in x_individuals:
                    x_individuals.append(current_individual.name)
                # Given xprime, update the list of x nodes
                kb.x_prime_individuals[x_prime] = x_individuals
                Util.debug(
                    f"BLOCKING: x ={current_individual.name} is directly blocked with y = {node_y}, x' = {node_x_prime}, y' = {node_y_prime}"
                )
                # Mark all descendants as indirectly blocked
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
        """
        Determines whether the provided individual is subject to direct anywhere pairwise blocking within the given fuzzy knowledge base by searching for a predecessor in the role successor list that shares matching concept labels with both the current individual and its parent. If a matching candidate is found, the method marks the individual as blocked, updates the knowledge base to record the blocking relationship and associated parent-child links, and recursively marks all descendants of the individual as indirectly blocked. The check is bypassed for nodes with a depth less than 3, and the method utilizes cached status information to avoid redundant evaluations if the blocking state has already been determined.

        :param current_individual: The individual node to be evaluated for direct anywhere pairwise blocking.
        :type current_individual: CreatedIndividual
        :param kb: The fuzzy knowledge base containing the role successors, individuals, and concept labels required to evaluate blocking conditions and update the blocking state.
        :type kb: KnowledgeBase

        :return: True if the individual is blocked by a predecessor node in the knowledge base where the individual and its parent match the concept labels of the predecessor and its parent, respectively; False otherwise.

        :rtype: bool
        """

        Util.debug(
            f"Directly anywhere pairwise blocking status {current_individual.directly_blocked}"
        )
        # Don't test if not deep enough in completion forest
        if current_individual.depth < 3:
            Util.debug("Depth < 3, node is not directly  anywhere pairwise blocked")
            current_individual.directly_blocked = (
                CreatedIndividualBlockingType.NOT_BLOCKED
            )
            return False

        # If already blocked don't test again
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

        # Proceed, assuming directlyBlocked == UNCHECKED holds
        # Direct blocking
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
        # Test for direct blocking
        while i < index_node_x:
            ynode: str = rsuccs[i]
            node_y: CreatedIndividual = typing.cast(
                CreatedIndividual, kb.get_individual(ynode)
            )
            Util.debug(f"Node y {ynode} depth = {node_y.depth}")
            # skip if nodeY not deep enough in tree
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
                # We got a pair-wise direct blocking
                current_individual.directly_blocked = (
                    CreatedIndividualBlockingType.BLOCKED
                )
                current_individual.blocking_ancestor = str(node_y)
                blocked_children: list[str] = kb.directly_blocked_children.get(
                    current_individual.blocking_ancestor, []
                )
                # Add nodeX to blocked nodes of blocking node nodeY
                if current_individual.name not in blocked_children:
                    blocked_children.append(current_individual.name)
                kb.directly_blocked_children[current_individual.blocking_ancestor] = (
                    blocked_children
                )
                y_prime: str = str(node_y_prime)
                # reate a link from y' to y
                y_individuals: list[str] = kb.y_prime_individuals.get(y_prime, [])
                if current_individual.blocking_ancestor not in y_individuals:
                    y_individuals.append(current_individual.blocking_ancestor)
                # Given yprime, update the list of y nodes
                kb.y_prime_individuals[y_prime] = y_individuals
                # Create a link from x' to x
                x_individuals: list[str] = kb.x_prime_individuals.get(x_prime, [])
                if current_individual.name not in x_individuals:
                    x_individuals.append(current_individual.name)
                # Given xprime, update the list of x nodes
                kb.x_prime_individuals[x_prime] = x_individuals
                Util.debug(
                    f"BLOCKING: x = {current_individual.name} is directly blocked with y = {node_y}, x' = {node_x_prime}, y' = {node_y_prime}"
                )
                current_individual.blocking_ancestor = str(node_x_prime)
                current_individual.blocking_ancestor_y = str(node_y)
                current_individual.blocking_ancestor_y_prime = str(node_y_prime)
                # Mark all descendants as indirectly blocked
                current_individual.mark_indirectly_blocked()
                break
            i += 1
        return (
            current_individual.directly_blocked == CreatedIndividualBlockingType.BLOCKED
        )

    @staticmethod
    def is_blocked(current_individual: CreatedIndividual, kb: KnowledgeBase) -> bool:
        """
        Determines whether a specific individual is considered blocked within the context of a fuzzy knowledge base. This evaluation combines two distinct blocking conditions: direct blocking and indirect blocking. The method returns true if either of these conditions is met, indicating that the individual should not be processed further in the current reasoning state.

        :param current_individual: The individual to check for blocking status.
        :type current_individual: CreatedIndividual
        :param kb: The knowledge base against which the individual's blocking status is evaluated.
        :type kb: KnowledgeBase

        :return: True if the individual is blocked (either directly or indirectly) with respect to the knowledge base, False otherwise.

        :rtype: bool
        """

        return CreatedIndividualHandler.is_indirectly_blocked(
            current_individual, kb
        ) or CreatedIndividualHandler.is_directly_blocked(current_individual, kb)

    @staticmethod
    def matching_individual(
        current_individual: CreatedIndividual, kb: KnowledgeBase
    ) -> set[CreatedIndividual]:
        """
        This static method searches the knowledge base for existing individuals that match the provided current individual, primarily to determine if blocking conditions are met. It begins by identifying candidates associated with the first concept of the current individual, filtering them to ensure they were created earlier, are not blocked, and meet size requirements based on the configured blocking dynamic type (subset or set equality). If this initial candidate set is empty, the method returns an empty set immediately. For each subsequent concept, the method checks for an intersection between the candidate set and individuals possessing that concept; if a non-empty intersection is found, it is returned right away. If the loop completes without finding such an intersection, the initial candidate set is returned. The operation is read-only with respect to the knowledge base and the individual, though it generates debug logs.

        :param current_individual: The individual for which matching candidates are sought within the knowledge base.
        :type current_individual: CreatedIndividual
        :param kb: The knowledge base providing the existing individuals and blocking configuration for the match check.
        :type kb: KnowledgeBase

        :return: A set of individuals from the knowledge base that share all concepts with the current individual, were created earlier, are not blocked, and satisfy the specific blocking type constraints. Returns an empty set if no matches are found.

        :rtype: set[CreatedIndividual]
        """

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
                # If empty, exit immediately
                if len(tmp_current_ind) == 0:
                    continue
                return tmp_current_ind

            # Drop no good individuals:
            # 1. created later
            # 2. node label size is not ok
            # 3. is not blocked
            #
            # Do it only for the fist concept
            candidate_set: SortedSet[CreatedIndividual] = SortedSet()
            for ind in current_ind:
                assert isinstance(ind, CreatedIndividual)

                if ind.get_integer_id() >= current_individual.get_integer_id():
                    break
                Util.debug(
                    f"Individual {ind.name} ID : {ind.get_integer_id()} size : {len(ind.concept_list)}"
                )
                Util.debug(f"Concept list -> {ind.concept_list}")
                # Node should be created earlier and node is not blocked
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
                ) >= len(
                    current_individual.concept_list
                ):  # subset blocking
                    candidate_set.add(ind)
                elif type == BlockingDynamicType.ANYWHERE_SET_BLOCKING and len(
                    ind.concept_list
                ) == len(
                    current_individual.concept_list
                ):  # set blocking
                    candidate_set.add(ind)
            Util.debug(f"Candidate set -> {candidate_set}")
            # For concept c, there is no candidate, so return immediately false
            if len(candidate_set) == 0:
                return candidate_set
            first_concept = False
        return candidate_set

    @staticmethod
    def match_concept_labels(
        current_individual: CreatedIndividual, b: CreatedIndividual, kb: KnowledgeBase
    ) -> bool:
        """
        Determines whether two individuals share matching concept labels according to the blocking strategy defined in the provided knowledge base. The specific matching logic depends on the `blocking_type` attribute of the knowledge base; if blocking is disabled, the method immediately returns False, whereas subset-based strategies trigger a subset check and other strategies trigger a set equality check. As a side effect, this method triggers debug logging to record the concept lists of the individuals being compared.

        :param current_individual: The individual whose concept labels are being compared to those of another individual.
        :type current_individual: CreatedIndividual
        :param b: The individual to compare against the current individual to determine if concept labels match.
        :type b: CreatedIndividual
        :param kb: The knowledge base providing the blocking configuration and concept definitions used to determine the matching strategy.
        :type kb: KnowledgeBase

        :return: True if the concept labels of the two individuals match according to the blocking strategy defined in the knowledge base, otherwise False.

        :rtype: bool
        """

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
        # indirect blocking applies only if we have dynamic blocking
        if (
            type == BlockingDynamicType.NO_BLOCKING
        ):  # no blocking. matching does not apply
            return False
        elif type in (
            BlockingDynamicType.SUBSET_BLOCKING,
            BlockingDynamicType.ANYWHERE_SUBSET_BLOCKING,
        ):  # subset blocking
            # match subset
            return CreatedIndividualHandler.match_subset_concept_labels(
                current_individual, b
            )
        # match set
        return CreatedIndividualHandler.match_set_concept_labels(current_individual, b)

    @staticmethod
    def match_subset_concept_labels(
        current_individual: CreatedIndividual, b: CreatedIndividual
    ) -> bool:
        """
        Determines whether the set of concept labels associated with the first individual is entirely contained within the set of concept labels associated with the second individual. This method performs a subset check on the `concept_list` attributes of the provided `CreatedIndividual` instances. It returns `True` only if the second individual is not `None` and all concepts from the first individual are present in the second; otherwise, it returns `False`.

        :param current_individual: The individual whose concept list is checked to verify if it is a subset of the other individual's concept list.
        :type current_individual: CreatedIndividual
        :param b: The individual to compare against, expected to contain all concept labels present in the current individual.
        :type b: CreatedIndividual

        :return: True if all concepts in `current_individual` are present in `b`, otherwise False.

        :rtype: bool
        """

        if b is None:
            return False
        return current_individual.concept_list.issubset(b.concept_list)

    @staticmethod
    def match_set_concept_labels(
        current_individual: CreatedIndividual, b: CreatedIndividual
    ) -> bool:
        """
        Compares the concept lists of two `CreatedIndividual` instances to determine if they are identical. The method evaluates the equality of the `concept_list` attribute belonging to the `current_individual` against that of the second individual, `b`. If the second individual is `None`, the method returns `False` rather than raising an error, ensuring safe comparison against missing or uninitialized data.

        :param current_individual: The individual whose concept list is compared against the other individual.
        :type current_individual: CreatedIndividual
        :param b: The individual whose concept labels are compared against the current individual.
        :type b: CreatedIndividual

        :return: True if the concept lists of the two individuals are equal, False otherwise.

        :rtype: bool
        """

        if b is None:
            return False
        return current_individual.concept_list == b.concept_list

    @staticmethod
    def unblock_directly_blocked(
        current_individual: CreatedIndividual, kb: KnowledgeBase
    ) -> None:
        """
        Resets the blocking status of a specific individual from directly blocked to unchecked, effectively clearing any reference to a blocking ancestor. This process restores any existence assertions that were previously suspended in the knowledge base due to this individual's blocked status by moving them back into the main list of active existence assertions. The method also updates the knowledge base by removing the record of these blocked assertions, ensuring the individual is treated as unchecked in subsequent processing.

        :param current_individual: The individual currently marked as directly blocked that is to be unblocked and have its associated assertions restored.
        :type current_individual: CreatedIndividual
        :param kb: The knowledge base containing the individual and its associated assertions.
        :type kb: KnowledgeBase
        """

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
        """
        Resets the blocking status of a specific individual that was previously marked as indirectly blocked, changing its state to 'UNCHECKED' and clearing the reference to the ancestor that caused the block. This process involves modifying the individual's attributes directly and updating the provided knowledge base. Specifically, the method retrieves any assertions that were suspended due to the individual's blocked status—both general assertions and existence assertions—and re-integrates them into the knowledge base's active processing queues, effectively removing them from the blocked storage.

        :param current_individual: The individual to be unblocked, resetting its blocking status and restoring associated assertions.
        :type current_individual: CreatedIndividual
        :param kb: The knowledge base used to restore assertions that were previously blocked for the individual.
        :type kb: KnowledgeBase
        """

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
