import enum


class ParserConstants(enum.Enum):
    DEFAULT = 0
    EOF = 0
    SINGLE_LINE_COMMENT = 3
    EOL = 4
    INSTANCE = 5
    MAX_INSTANCE_QUERY = 6
    MIN_INSTANCE_QUERY = 7
    ALL_INSTANCE_QUERY = 8
    MAX_RELATED_QUERY = 9
    MIN_RELATED_QUERY = 10
    MAX_SUBSUMES_QUERY = 11
    MAX_G_SUBSUMES_QUERY = 12
    MAX_L_SUBSUMES_QUERY = 13
    MAX_KD_SUBSUMES_QUERY = 14
    MIN_SUBSUMES_QUERY = 15
    MIN_G_SUBSUMES_QUERY = 16
    MIN_L_SUBSUMES_QUERY = 17
    MIN_KD_SUBSUMES_QUERY = 18
    MAX_SATISFIABLE_QUERY = 19
    MIN_SATISFIABLE_QUERY = 20
    MAX_QUERY = 21
    MIN_QUERY = 22
    SATISFIABLE_QUERY = 23
    LOM_DEFUZZIFY_QUERY = 24
    SOM_DEFUZZIFY_QUERY = 25
    MOM_DEFUZZIFY_QUERY = 26
    BNP_QUERY = 27
    DEFINE_TRUTH_CONSTANT = 28
    DEFINE_CONCEPT = 29
    DEFINE_PRIMITIVE_CONCEPT = 30
    EQUIVALENT_CONCEPTS = 31
    DEFINE_FUZZY_CONCEPT = 32
    DEFINE_FUZZY_NUMBER = 33
    DEFINE_FUZZY_NUMBER_RANGE = 34
    DEFINE_FUZZY_SIMILARITY = 35
    DEFINE_FUZZY_EQUIVALENCE = 36
    RELATED = 37
    DEFINE_MODIFIER = 38
    FUNCTIONAL = 39
    TRANSITIVE = 40
    REFLEXIVE = 41
    SYMMETRIC = 42
    IMPLIES_ROLE = 43
    INVERSE = 44
    INVERSE_FUNCTIONAL = 45
    DISJOINT = 46
    DISJOINT_UNION = 47
    RANGE = 48
    DOMAIN = 49
    CONSTRAINTS = 50
    FUZZY_LOGIC = 51
    CRISP_CONCEPT = 52
    CRISP_ROLE = 53
    COM = 54
    AND = 55
    G_AND = 56
    L_AND = 57
    IMPLIES = 58
    G_IMPLIES = 59
    KD_IMPLIES = 60
    L_IMPLIES = 61
    Z_IMPLIES = 62
    OR = 63
    G_OR = 64
    L_OR = 65
    NOT = 66
    SOME = 67
    HAS_VALUE = 68
    ALL = 69
    TOP = 70
    BOTTOM = 71
    W_SUM = 72
    W_SUM_ZERO = 73
    W_MAX = 74
    W_MIN = 75
    SELF = 76
    UPPER_APPROX = 77
    LOWER_APPROX = 78
    OWA = 79
    QOWA = 80
    CHOQUET = 81
    SUGENO = 82
    QSUGENO = 83
    TIGHT_UPPER_APPROX = 84
    TIGHT_LOWER_APPROX = 85
    LOOSE_UPPER_APPROX = 86
    LOOSE_LOWER_APPROX = 87
    FUZZY_NUMBER_ADD = 88
    FUZZY_NUMBER_MINUS = 89
    FUZZY_NUMBER_MULT = 90
    FUZZY_NUMBER_DIV = 91
    CRISP = 92
    LS = 93
    RS = 94
    TRI = 95
    TRAP = 96
    LINEAR = 97
    MODIFIED = 98
    LM = 99
    TRIAM = 100
    SHOW_VARIABLES = 101
    SHOW_ABSTRACT_FILLER = 102
    SHOW_ABSTRACT_FILLER_FOR = 103
    SHOW_CONCRETE_FILLER = 104
    SHOW_CONCRETE_FILLER_FOR = 105
    SHOW_CONCRETE_FILLER_AND_LABELS = 106
    SHOW_INSTANCES = 107
    SHOW_CONCEPTS = 108
    SHOW_LANGUAGE = 109
    FR = 110
    BV = 111
    LUKASIEWICZ = 112
    ZADEH = 113
    CLASSICAL = 114
    PLUS = 115
    MINUS = 116
    STAR = 117
    LESS = 118
    GRE = 119
    EQL = 120
    IDENTIFIER = 121
    OP = 122
    CP = 123
    OSB = 124
    CSB = 125
    OCB = 126
    CCB = 127
    COMMENT_MARK = 128
    COMMA = 129
    NUMBER = 130
    STRING_TYPE = 131
    BOOLEAN_TYPE = 132
    NUMBER_TYPE = 133


TOKEN_IMAGE: list[str] = [
    "<EOF>",
    '" "',
    '"\\t"',
    "<SINGLE_LINE_COMMENT>",
    "<EOL>",
    '"instance"',
    '"max-instance?"',
    '"min-instance?"',
    '"all-instances?"',
    '"max-related?"',
    '"min-related?"',
    '"max-subs?"',
    '"max-g-subs?"',
    '"max-l-subs?"',
    '"max-kd-subs?"',
    '"min-subs?"',
    '"min-g-subs?"',
    '"min-l-subs?"',
    '"min-kd-subs?"',
    '"max-sat?"',
    '"min-sat?"',
    '"max-var?"',
    '"min-var?"',
    '"sat?"',
    '"defuzzify-lom?"',
    '"defuzzify-som?"',
    '"defuzzify-mom?"',
    '"bnp?"',
    '"define-truth-constant"',
    '"define-concept"',
    '"define-primitive-concept"',
    '"equivalent-concepts"',
    '"define-fuzzy-concept"',
    '"define-fuzzy-number"',
    '"define-fuzzy-number-range"',
    '"define-fuzzy-similarity"',
    '"define-fuzzy-equivalence"',
    '"related"',
    '"define-modifier"',
    '"functional"',
    '"transitive"',
    '"reflexive"',
    '"symmetric"',
    '"implies-role"',
    '"inverse"',
    '"inverse-functional"',
    '"disjoint"',
    '"disjoint-union"',
    '"range"',
    '"domain"',
    '"constraints"',
    '"define-fuzzy-logic"',
    '"crisp-concept"',
    '"crisp-role"',
    '"\\""',
    '"and"',
    '"g-and"',
    '"l-and"',
    '"implies"',
    '"g-implies"',
    '"kd-implies"',
    '"l-implies"',
    '"z-implies"',
    '"or"',
    '"g-or"',
    '"l-or"',
    '"not"',
    '"some"',
    '"b-some"',
    '"all"',
    '"*top*"',
    '"*bottom*"',
    '"w-sum"',
    '"w-sum-zero"',
    '"w-max"',
    '"w-min"',
    '"self"',
    '"ua"',
    '"la"',
    '"owa"',
    '"q-owa"',
    '"choquet"',
    '"sugeno"',
    '"q-sugeno"',
    '"tua"',
    '"tla"',
    '"lua"',
    '"lla"',
    '"f+"',
    '"f-"',
    '"f*"',
    '"f/"',
    '"crisp"',
    '"left-shoulder"',
    '"right-shoulder"',
    '"triangular"',
    '"trapezoidal"',
    '"linear"',
    '"modified"',
    '"linear-modifier"',
    '"triangular-modifier"',
    '"show-variables"',
    '"show-abstract-fillers"',
    '"show-abstract-fillers-for"',
    '"show-concrete-fillers"',
    '"show-concrete-fillers-for"',
    '"show-concrete-instance-for"',
    '"show-instances"',
    '"show-concepts"',
    '"show-language"',
    '"free"',
    '"binary"',
    '"lukasiewicz"',
    '"zadeh"',
    '"classical"',
    '"+"',
    '"-"',
    '"*"',
    '"<="',
    '">="',
    '"="',
    "<IDENTIFIER>",
    '"("',
    '")"',
    '"["',
    '"]"',
    '"{"',
    '"}"',
    '"#"',
    '","',
    "<NUMBER>",
    '"*string*"',
    '"*boolean*"',
    "<NUMBER_TYPE>",
]

LITERAL_IMAGES: list[str] = [
    "max-instance?",
    "min-instance?",
    "all-instances?",
    "max-related?",
    "min-related?",
    "max-subs?",
    "max-g-subs?",
    "max-l-subs?",
    "max-kd-subs?",
    "min-subs?",
    "min-g-subs?",
    "min-l-subs?",
    "min-kd-subs?",
    "max-sat?",
    "min-sat?",
    "max-var?",
    "min-var?",
    "sat?",
    "defuzzify-lom?",
    "defuzzify-som?",
    "defuzzify-mom?",
    "bnp?",
    "instance",
    "define-truth-constant",
    "define-concept",
    "define-primitive-concept",
    "equivalent-concepts",
    "define-fuzzy-concept",
    "define-fuzzy-number",
    "define-fuzzy-number-range",
    "define-fuzzy-similarity",
    "define-fuzzy-equivalence",
    "related",
    "define-modifier",
    "functional",
    "transitive",
    "reflexive",
    "symmetric",
    "implies-role",
    "inverse",
    "inverse-functional",
    "disjoint",
    "disjoint-union",
    "range",
    "domain",
    "constraints",
    "define-fuzzy-logic",
    "crisp-concept",
    "crisp-role",
    '"',
    "and",
    "g-and",
    "l-and",
    "implies",
    "g-implies",
    "kd-implies",
    "l-implies",
    "z-implies",
    "or",
    "g-or",
    "l-or",
    "not",
    "some",
    "b-some",
    "all",
    "*top*",
    "*bottom*",
    "w-sum",
    "w-sum-zero",
    "w-max",
    "w-min",
    "self",
    "ua",
    "la",
    "owa",
    "q-owa",
    "choquet",
    "sugeno",
    "q-sugeno",
    "tua",
    "tla",
    "lua",
    "lla",
    "f+",
    "f-",
    "f*",
    "f/",
    "crisp",
    "left-shoulder",
    "right-shoulder",
    "triangular",
    "trapezoidal",
    "linear",
    "modified",
    "linear-modifier",
    "triangular-modifier",
    "show-variables",
    "show-abstract-fillers",
    "show-abstract-fillers-for",
    "show-concrete-fillers",
    "show-concrete-fillers-for",
    "show-concrete-instance-for",
    "show-instances",
    "show-concepts",
    "show-language",
    "free",
    "binary",
    "lukasiewicz",
    "zadeh",
    "classical",
    "+",
    "-",
    "*",
    "<=",
    ">=",
    "=",
    "(",
    ")",
    "[",
    "]",
    "{",
    "}",
    "#",
    ",",
    "*string*",
    "*boolean*",
]

STATE_NAMES: list[str] = ["DEFAULT"]
