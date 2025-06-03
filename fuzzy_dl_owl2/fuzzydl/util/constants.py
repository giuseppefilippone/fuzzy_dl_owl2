import enum
import os
import re
import typing

import pyparsing as pp

SEPARATOR: str = "-" * 25
STAR_SEPARATOR: str = "*" * 25
NUMBER = typing.Union[int, float]
RESULTS_PATH: str = os.path.join(".", "results")

if not os.path.exists(RESULTS_PATH):
    os.makedirs(RESULTS_PATH)


class ConcreteFeatureType(enum.Enum):
    STRING = 0
    INTEGER = 1
    REAL = 2
    BOOLEAN = 3

    def __repr__(self) -> str:
        return self.name

    def __str__(self) -> str:
        return self.name


class FeatureFunctionType(enum.Enum):
    ATOMIC = 0
    NUMBER = 1
    SUM = 2
    SUBTRACTION = 3
    PRODUCT = 5

    def __repr__(self) -> str:
        return self.name

    def __str__(self) -> str:
        return self.name


class BlockingDynamicType(enum.Enum):
    NO_BLOCKING = 0
    SUBSET_BLOCKING = 1
    SET_BLOCKING = 2
    DOUBLE_BLOCKING = 3
    ANYWHERE_SUBSET_BLOCKING = 4
    ANYWHERE_SET_BLOCKING = 5
    ANYWHERE_DOUBLE_BLOCKING = 6

    def __repr__(self) -> str:
        return self.name

    def __str__(self) -> str:
        return self.name


class KnowledgeBaseRules(enum.Enum):
    RULE_ATOMIC = 0
    RULE_COMPLEMENT = 1
    RULE_GOEDEL_AND = 2
    RULE_LUKASIEWICZ_AND = 3
    RULE_GOEDEL_OR = 4
    RULE_LUKASIEWICZ_OR = 5
    RULE_GOEDEL_SOME = 6
    RULE_LUKASIEWICZ_SOME = 7
    RULE_GOEDEL_ALL = 8
    RULE_LUKASIEWICZ_ALL = 9
    RULE_TOP = 10
    RULE_BOTTOM = 11
    RULE_GOEDEL_IMPLIES = 12
    RULE_NOT_GOEDEL_IMPLIES = 13
    RULE_CONCRETE = 14
    RULE_NOT_CONCRETE = 15
    RULE_MODIFIED = 16
    RULE_NOT_MODIFIED = 17
    RULE_DATATYPE = 18
    RULE_NOT_DATATYPE = 19
    RULE_FUZZY_NUMBER = 20
    RULE_NOT_FUZZY_NUMBER = 21
    RULE_WEIGHTED = 22
    RULE_NOT_WEIGHTED = 23
    RULE_THRESHOLD = 24
    RULE_NOT_THRESHOLD = 25
    RULE_OWA = 26
    RULE_NOT_OWA = 27
    RULE_W_SUM = 28
    RULE_NOT_W_SUM = 29
    RULE_CHOQUET_INTEGRAL = 30
    RULE_NOT_CHOQUET_INTEGRAL = 31
    RULE_SUGENO_INTEGRAL = 32
    RULE_NOT_SUGENO_INTEGRAL = 33
    RULE_QUASI_SUGENO_INTEGRAL = 34
    RULE_NOT_QUASI_SUGENO_INTEGRAL = 35
    RULE_SELF = 36
    RULE_NOT_SELF = 37
    RULE_W_MIN = 38
    RULE_NOT_W_MIN = 39
    RULE_W_MAX = 40
    RULE_NOT_W_MAX = 41
    RULE_W_SUM_ZERO = 42
    RULE_NOT_W_SUM_ZERO = 43
    RULE_HAS_VALUE = 44
    RULE_NOT_HAS_VALUE = 45
    RULE_ZADEH_IMPLIES = 46
    RULE_NOT_ZADEH_IMPLIES = 47

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return self.name.replace("RULE_", "")


class LogicOperatorType(enum.Enum):
    LUKASIEWICZ = 0
    GOEDEL = 1
    KLEENE_DIENES = 2
    ZADEH = 3

    def __repr__(self) -> str:
        return self.name

    def __str__(self) -> str:
        return self.name


class ConceptType(enum.Enum):
    AND = 0
    GOEDEL_AND = 1
    LUKASIEWICZ_AND = 2
    OR = 3
    GOEDEL_OR = 4
    LUKASIEWICZ_OR = 5
    SOME = 6
    ALL = 7
    UPPER_APPROX = 8
    LOWER_APPROX = 9
    FUZZY_NUMBER_COMPLEMENT = 10
    TIGHT_UPPER_APPROX = 11
    TIGHT_LOWER_APPROX = 12
    LOOSE_UPPER_APPROX = 13
    LOOSE_LOWER_APPROX = 14
    GOEDEL_IMPLIES = 15
    NOT_GOEDEL_IMPLIES = 16
    ATOMIC = 17
    COMPLEMENT = 18
    TOP = 19
    BOTTOM = 20
    AT_MOST_VALUE = 21
    AT_LEAST_VALUE = 22
    EXACT_VALUE = 23
    NOT_AT_MOST_VALUE = 24
    NOT_AT_LEAST_VALUE = 25
    NOT_EXACT_VALUE = 26
    WEIGHTED = 27
    NOT_WEIGHTED = 28
    W_SUM = 29
    NOT_W_SUM = 30
    POS_THRESHOLD = 31
    NOT_POS_THRESHOLD = 32
    NEG_THRESHOLD = 33
    NOT_NEG_THRESHOLD = 34
    EXT_POS_THRESHOLD = 35
    NOT_EXT_POS_THRESHOLD = 36
    EXT_NEG_THRESHOLD = 37
    NOT_EXT_NEG_THRESHOLD = 38
    CONCRETE = 39
    CONCRETE_COMPLEMENT = 40
    MODIFIED = 41
    MODIFIED_COMPLEMENT = 42
    SELF = 43
    FUZZY_NUMBER = 44
    OWA = 45
    QUANTIFIED_OWA = 46
    NOT_OWA = 47
    NOT_QUANTIFIED_OWA = 48
    CHOQUET_INTEGRAL = 49
    SUGENO_INTEGRAL = 50
    QUASI_SUGENO_INTEGRAL = 51
    NOT_CHOQUET_INTEGRAL = 52
    NOT_SUGENO_INTEGRAL = 53
    NOT_QUASI_SUGENO_INTEGRAL = 54
    W_MAX = 55
    NOT_W_MAX = 56
    W_MIN = 57
    NOT_W_MIN = 58
    W_SUM_ZERO = 59
    NOT_W_SUM_ZERO = 60
    NOT_SELF = 61
    HAS_VALUE = 62
    NOT_HAS_VALUE = 63
    ZADEH_IMPLIES = 64
    NOT_ZADEH_IMPLIES = 65

    def __repr__(self) -> str:
        return self.name

    def __str__(self) -> str:
        return self.name


class CreatedIndividualBlockingType(enum.Enum):
    BLOCKED = 0
    NOT_BLOCKED = 1
    UNCHECKED = 2

    def __repr__(self) -> str:
        return self.name

    def __str__(self) -> str:
        return self.name


class RepresentativeIndividualType(enum.Enum):
    GREATER_EQUAL = 0
    LESS_EQUAL = 1

    def __repr__(self) -> str:
        return self.name

    def __str__(self) -> str:
        return self.name


class InequalityType(enum.StrEnum):
    GREATER_THAN = ">"
    LESS_THAN = "<"
    EQUAL = "="

    def __repr__(self) -> str:
        return self.name

    def __str__(self) -> str:
        return self.value


class VariableType(enum.StrEnum):
    BINARY = enum.auto()
    CONTINUOUS = enum.auto()
    INTEGER = enum.auto()
    SEMI_CONTINUOUS = enum.auto()

    def __repr__(self) -> str:
        return self.name

    def __str__(self) -> str:
        return self.name


class FuzzyDLKeyword(enum.Enum):
    MAX_INSTANCE_QUERY = pp.CaselessKeyword("max-instance?")
    MIN_INSTANCE_QUERY = pp.CaselessKeyword("min-instance?")
    ALL_INSTANCES_QUERY = pp.CaselessKeyword("all-instances?")
    MAX_RELATED_QUERY = pp.CaselessKeyword("max-related?")
    MIN_RELATED_QUERY = pp.CaselessKeyword("min-related?")
    MAX_SUBS_QUERY = pp.CaselessKeyword("max-subs?")
    MAX_G_SUBS_QUERY = pp.CaselessKeyword("max-g-subs?")
    MAX_L_SUBS_QUERY = pp.CaselessKeyword("max-l-subs?")
    MAX_KD_SUBS_QUERY = pp.CaselessKeyword("max-kd-subs?")
    MIN_SUBS_QUERY = pp.CaselessKeyword("min-subs?")
    MIN_G_SUBS_QUERY = pp.CaselessKeyword("min-g-subs?")
    MIN_L_SUBS_QUERY = pp.CaselessKeyword("min-l-subs?")
    MIN_KD_SUBS_QUERY = pp.CaselessKeyword("min-kd-subs?")
    MAX_SAT_QUERY = pp.CaselessKeyword("max-sat?")
    MIN_SAT_QUERY = pp.CaselessKeyword("min-sat?")
    MAX_VAR_QUERY = pp.CaselessKeyword("max-var?")
    MIN_VAR_QUERY = pp.CaselessKeyword("min-var?")
    SAT_QUERY = pp.CaselessKeyword("sat?")
    DEFUZZIFY_LOM_QUERY = pp.CaselessKeyword("defuzzify-lom?")
    DEFUZZIFY_SOM_QUERY = pp.CaselessKeyword("defuzzify-som?")
    DEFUZZIFY_MOM_QUERY = pp.CaselessKeyword("defuzzify-mom?")
    BNP_QUERY = pp.CaselessKeyword("bnp?")
    INSTANCE = pp.CaselessKeyword("instance")
    DEFINE_TRUTH_CONSTANT = pp.CaselessKeyword("define-truth-constant")
    DEFINE_CONCEPT = pp.CaselessKeyword("define-concept")
    DEFINE_PRIMITIVE_CONCEPT = pp.CaselessKeyword("define-primitive-concept")
    EQUIVALENT_CONCEPTS = pp.CaselessKeyword("equivalent-concepts")
    DEFINE_FUZZY_CONCEPT = pp.CaselessKeyword("define-fuzzy-concept")
    DEFINE_FUZZY_NUMBER = pp.CaselessKeyword("define-fuzzy-number")
    DEFINE_FUZZY_NUMBER_RANGE = pp.CaselessKeyword("define-fuzzy-number-range")
    DEFINE_FUZZY_SIMILARITY = pp.CaselessKeyword("define-fuzzy-similarity")
    DEFINE_FUZZY_EQUIVALENCE = pp.CaselessKeyword("define-fuzzy-equivalence")
    RELATED = pp.CaselessKeyword("related")
    DEFINE_MODIFIER = pp.CaselessKeyword("define-modifier")
    FUNCTIONAL = pp.CaselessKeyword("functional")
    TRANSITIVE = pp.CaselessKeyword("transitive")
    REFLEXIVE = pp.CaselessKeyword("reflexive")
    SYMMETRIC = pp.CaselessKeyword("symmetric")
    IMPLIES_ROLE = pp.CaselessKeyword("implies-role")
    INVERSE = pp.CaselessKeyword("inverse")
    INVERSE_FUNCTIONAL = pp.CaselessKeyword("inverse-functional")
    DISJOINT = pp.CaselessKeyword("disjoint")
    DISJOINT_UNION = pp.CaselessKeyword("disjoint-union")
    RANGE = pp.CaselessKeyword("range")
    DOMAIN = pp.CaselessKeyword("domain")
    CONSTRAINTS = pp.CaselessKeyword("constraints")
    DEFINE_FUZZY_LOGIC = pp.CaselessKeyword("define-fuzzy-logic")
    CRISP_CONCEPT = pp.CaselessKeyword("crisp-concept")
    CRISP_ROLE = pp.CaselessKeyword("crisp-role")
    AND = pp.CaselessKeyword("and")
    GOEDEL_AND = pp.CaselessKeyword("g-and")
    LUKASIEWICZ_AND = pp.CaselessKeyword("l-and")
    IMPLIES = pp.CaselessKeyword("implies")
    GOEDEL_IMPLIES = pp.CaselessKeyword("g-implies")
    KLEENE_DIENES_IMPLIES = pp.CaselessKeyword("kd-implies")
    LUKASIEWICZ_IMPLIES = pp.CaselessKeyword("l-implies")
    ZADEH_IMPLIES = pp.CaselessKeyword("z-implies")
    OR = pp.CaselessKeyword("or")
    GOEDEL_OR = pp.CaselessKeyword("g-or")
    LUKASIEWICZ_OR = pp.CaselessKeyword("l-or")
    NOT = pp.CaselessKeyword("not")
    SOME = pp.CaselessKeyword("some")
    HAS_VALUE = pp.CaselessKeyword("b-some")
    ALL = pp.CaselessKeyword("all")
    TOP = pp.CaselessKeyword("*top*")
    BOTTOM = pp.CaselessKeyword("*bottom*")
    W_SUM = pp.CaselessKeyword("w-sum")
    W_SUM_ZERO = pp.CaselessKeyword("w-sum-zero")
    W_MAX = pp.CaselessKeyword("w-max")
    W_MIN = pp.CaselessKeyword("w-min")
    SELF = pp.CaselessKeyword("self")
    UPPER_APPROXIMATION = pp.CaselessKeyword("ua")
    LOWER_APPROXIMATION = pp.CaselessKeyword("la")
    OWA = pp.CaselessKeyword("owa")
    Q_OWA = pp.CaselessKeyword("q-owa")
    CHOQUET = pp.CaselessKeyword("choquet")
    SUGENO = pp.CaselessKeyword("sugeno")
    QUASI_SUGENO = pp.CaselessKeyword("q-sugeno")
    TIGHT_UPPER_APPROXIMATION = pp.CaselessKeyword("tua")
    TIGHT_LOWER_APPROXIMATION = pp.CaselessKeyword("tla")
    LOOSE_UPPER_APPROXIMATION = pp.CaselessKeyword("lua")
    LOOSE_LOWER_APPROXIMATION = pp.CaselessKeyword("lla")
    FEATURE_SUM = pp.CaselessKeyword("f+")
    FEATURE_SUB = pp.CaselessKeyword("f-")
    FEATURE_MUL = pp.CaselessKeyword("f*")
    FEATURE_DIV = pp.CaselessKeyword("f/")
    CRISP = pp.CaselessKeyword("crisp")
    LEFT_SHOULDER = pp.CaselessKeyword("left-shoulder")
    RIGHT_SHOULDER = pp.CaselessKeyword("right-shoulder")
    TRIANGULAR = pp.CaselessKeyword("triangular")
    TRAPEZOIDAL = pp.CaselessKeyword("trapezoidal")
    LINEAR = pp.CaselessKeyword("linear")
    MODIFIED = pp.CaselessKeyword("modified")
    LINEAR_MODIFIER = pp.CaselessKeyword("linear-modifier")
    TRIANGULAR_MODIFIER = pp.CaselessKeyword("triangular-modifier")
    SHOW_VARIABLES = pp.CaselessKeyword("show-variables")
    SHOW_ABSTRACT_FILLERS = pp.CaselessKeyword("show-abstract-fillers")
    SHOW_ABSTRACT_FILLERS_FOR = pp.CaselessKeyword("show-abstract-fillers-for")
    SHOW_CONCRETE_FILLERS = pp.CaselessKeyword("show-concrete-fillers")
    SHOW_CONCRETE_FILLERS_FOR = pp.CaselessKeyword("show-concrete-fillers-for")
    SHOW_CONCRETE_INSTANCE_FOR = pp.CaselessKeyword("show-concrete-instance-for")
    SHOW_INSTANCES = pp.CaselessKeyword("show-instances")
    SHOW_CONCEPTS = pp.CaselessKeyword("show-concepts")
    SHOW_LANGUAGE = pp.CaselessKeyword("show-language")
    FREE = pp.CaselessKeyword("free")
    BINARY = pp.CaselessKeyword("binary")
    LUKASIEWICZ = pp.CaselessKeyword("lukasiewicz")
    ZADEH = pp.CaselessKeyword("zadeh")
    CLASSICAL = pp.CaselessKeyword("classical")
    SUM = pp.Literal("+")
    SUB = pp.Literal("-")
    MUL = pp.Literal("*")
    LESS_THAN_OR_EQUAL_TO = pp.Literal("<=")
    GREATER_THAN_OR_EQUAL_TO = pp.Literal(">=")
    EQUALS = pp.Literal("=")
    STRING = pp.CaselessKeyword("*string*")
    BOOLEAN = pp.CaselessKeyword("*boolean*")
    INTEGER = pp.CaselessKeyword("*integer*")
    REAL = pp.CaselessKeyword("*real*")

    def get_name(self) -> str:
        return re.sub(r"[\"\']+", "", self.value.name.lower())

    def get_value(self) -> typing.Union[pp.CaselessKeyword, pp.Literal]:
        return self.value

    def __eq__(self, value: object) -> bool:
        if isinstance(value, str):
            return self.get_name() == value.lower()
        elif isinstance(value, pp.CaselessKeyword):
            return self.get_name() == value.name.lower()
        elif isinstance(value, pp.Literal):
            return self.get_name() == value.name.lower()
        elif isinstance(value, FuzzyDLKeyword):
            return self.get_name() == value.get_name()
        raise NotImplementedError

    def __repr__(self) -> str:
        return self.name

    def __str__(self) -> str:
        return self.name


class RestrictionType(enum.Enum):
    AT_MOST_VALUE = 0
    AT_LEAST_VALUE = 1
    EXACT_VALUE = 2

    def __repr__(self) -> str:
        return self.name

    def __str__(self) -> str:
        return self.name


class FuzzyLogic(enum.StrEnum):
    CLASSICAL = "classical"
    ZADEH = "zadeh"
    LUKASIEWICZ = "lukasiewicz"

    def __repr__(self) -> str:
        return self.name

    def __str__(self) -> str:
        return self.value


KNOWLEDGE_BASE_SEMANTICS: FuzzyLogic = FuzzyLogic.CLASSICAL
MAXVAL: float = ((1 << 31) - 1) * 1000  # 2.147483647e12
MAXVAL2: float = MAXVAL * 2
