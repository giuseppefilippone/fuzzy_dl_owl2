import enum
import re
import typing

import pyparsing as pp


class ConceptType(enum.StrEnum):
    CHOQUET = enum.auto()
    FUZZY_NOMINAL = enum.auto()
    MODIFIED_CONCEPT = enum.auto()
    OWA = enum.auto()
    QUANTIFIED_OWA = enum.auto()
    QUASI_SUGENO = enum.auto()
    SUGENO = enum.auto()
    WEIGHTED_CONCEPT = enum.auto()
    WEIGHTED_MAX = enum.auto()
    WEIGHTED_MIN = enum.auto()
    WEIGHTED_SUM = enum.auto()
    WEIGHTED_SUM_ZERO = enum.auto()

    def __repr__(self) -> str:
        return self.name

    def __str__(self) -> str:
        return self.name


# class FuzzyOWL2Keyword(enum.Enum):
#     OPEN_TAG = pp.Word("<")
#     CLOSE_TAG = pp.Word(">")
#     SINGLE_CLOSE_TAG = pp.Word("/>")
#     SLASH = pp.Word("/")
#     ONTOLOGY = pp.CaselessKeyword("ontology")
#     FUZZY_OWL_2 = pp.CaselessKeyword("fuzzyOwl2")
#     FUZZY_LABEL = pp.CaselessKeyword("fuzzyLabel")
#     FUZZY_TYPE = pp.CaselessKeyword("fuzzytype")
#     FUZZY_LOGIC = pp.CaselessKeyword("FuzzyLogic")
#     TYPE = pp.CaselessKeyword("type")
#     LOGIC = pp.CaselessKeyword("logic")
#     DATATYPE = pp.CaselessKeyword("datatype")
#     CONCEPT = pp.CaselessKeyword("concept")
#     ROLE = pp.CaselessKeyword("role")
#     AXIOM = pp.CaselessKeyword("axiom")
#     DEGREE_DEF = pp.CaselessKeyword("degree")
#     DEGREE_VALUE = pp.CaselessKeyword("value")
#     MODIFIED = pp.CaselessKeyword("modified")
#     WEIGHTED = pp.CaselessKeyword("weighted")
#     NOMINAL = pp.CaselessKeyword("nominal")
#     INDIVIDUAL = pp.CaselessKeyword("individual")
#     WEIGHTED_MAXIMUM = pp.CaselessKeyword("weightedMaximum")
#     WEIGHTED_MINIMUM = pp.CaselessKeyword("weightedMinimum")
#     WEIGHTED_SUM = pp.CaselessKeyword("weightedSum")
#     WEIGHTED_SUMZERO = pp.CaselessKeyword("weightedSumZero")
#     OWA = pp.CaselessKeyword("owa")
#     Q_OWA = pp.CaselessKeyword("qowa")
#     CHOQUET = pp.CaselessKeyword("choquet")
#     SUGENO = pp.CaselessKeyword("sugeno")
#     QUASI_SUGENO = pp.CaselessKeyword("quasisugeno")
#     MODIFIER = pp.CaselessKeyword("modifier")
#     BASE = pp.CaselessKeyword("base")
#     CONCEPT_NAMES = pp.CaselessKeyword("names")
#     NAME = pp.CaselessKeyword("name")
#     WEIGHT = pp.CaselessKeyword("weight")
#     WEIGHTS = pp.CaselessKeyword("weights")
#     QUANTIFIER = pp.CaselessKeyword("quantifier")
#     CRISP = pp.CaselessKeyword("crisp")
#     LEFT_SHOULDER = pp.CaselessKeyword("leftshoulder")
#     RIGHT_SHOULDER = pp.CaselessKeyword("rightshoulder")
#     TRIANGULAR = pp.CaselessKeyword("triangular")
#     TRAPEZOIDAL = pp.CaselessKeyword("trapezoidal")
#     LINEAR = pp.CaselessKeyword("linear")
#     A = pp.CaselessKeyword("a")
#     B = pp.CaselessKeyword("b")
#     C = pp.CaselessKeyword("c")
#     D = pp.CaselessKeyword("d")
#     LUKASIEWICZ = pp.CaselessKeyword("lukasiewicz")
#     GOEDEL = pp.CaselessKeyword("goedel")
#     ZADEH = pp.CaselessKeyword("zadeh")
#     PRODUCT = pp.CaselessKeyword("product")
#     EQUAL = pp.Word("=")
#     LES = pp.CaselessKeyword("les")
#     LEQ = pp.CaselessKeyword("leq")
#     GEQ = pp.CaselessKeyword("geq")
#     GRE = pp.CaselessKeyword("gre")

#     def get_name(self) -> str:
#         return re.sub(r"[\"\']+", "", self.value.name.lower())

#     def get_value(self) -> typing.Union[pp.CaselessKeyword, pp.Word]:
#         return self.value

#     def get_str_value(self) -> str:
#         return str(self.value).replace('"', "").replace("'", "")

#     def get_tag_name(self) -> str:
#         return self.get_str_value().capitalize()

#     def __eq__(self, value: object) -> bool:
#         if isinstance(value, str):
#             return self.get_name() == value.lower()
#         elif isinstance(value, pp.CaselessKeyword):
#             return self.get_name() == value.name.lower()
#         elif isinstance(value, FuzzyOWL2Keyword):
#             return self.get_name() == value.get_name()
#         raise NotImplementedError

#     def __repr__(self) -> str:
#         return self.name

#     def __str__(self) -> str:
#         return self.name


class FuzzyOWL2Keyword(enum.Enum):
    OPEN_TAG = pp.Word("<")
    CLOSE_TAG = pp.Word(">")
    SINGLE_CLOSE_TAG = pp.Word("/>")
    SLASH = pp.Word("/")
    ONTOLOGY = pp.Keyword("ontology")
    FUZZY_OWL_2 = pp.Keyword("fuzzyOwl2")
    FUZZY_LABEL = pp.Keyword("fuzzyLabel")
    FUZZY_TYPE = pp.Keyword("fuzzyType")
    FUZZY_LOGIC = pp.Keyword("FuzzyLogic")
    TYPE = pp.Keyword("type")
    LOGIC = pp.Keyword("logic")
    DATATYPE = pp.Keyword("datatype")
    CONCEPT = pp.Keyword("concept")
    ROLE = pp.Keyword("role")
    AXIOM = pp.Keyword("axiom")
    DEGREE_DEF = pp.Keyword("degree")
    DEGREE_VALUE = pp.Keyword("value")
    MODIFIED = pp.Keyword("modified")
    WEIGHTED = pp.Keyword("weighted")
    NOMINAL = pp.Keyword("nominal")
    INDIVIDUAL = pp.Keyword("individual")
    WEIGHTED_MAXIMUM = pp.Keyword("weightedMaximum")
    WEIGHTED_MINIMUM = pp.Keyword("weightedMinimum")
    WEIGHTED_SUM = pp.Keyword("weightedSum")
    WEIGHTED_SUMZERO = pp.Keyword("weightedSumZero")
    OWA = pp.Keyword("owa")
    Q_OWA = pp.Keyword("qowa")
    CHOQUET = pp.Keyword("choquet")
    SUGENO = pp.Keyword("sugeno")
    QUASI_SUGENO = pp.Keyword("quasisugeno")
    MODIFIER = pp.Keyword("modifier")
    BASE = pp.Keyword("base")
    CONCEPT_NAMES = pp.Keyword("names")
    NAME = pp.Keyword("name")
    WEIGHT = pp.Keyword("weight")
    WEIGHTS = pp.Keyword("weights")
    QUANTIFIER = pp.Keyword("quantifier")
    CRISP = pp.Keyword("crisp")
    LEFT_SHOULDER = pp.Keyword("leftshoulder")
    RIGHT_SHOULDER = pp.Keyword("rightshoulder")
    TRIANGULAR = pp.Keyword("triangular")
    TRAPEZOIDAL = pp.Keyword("trapezoidal")
    LINEAR = pp.Keyword("linear")
    A = pp.Keyword("a")
    B = pp.Keyword("b")
    C = pp.Keyword("c")
    D = pp.Keyword("d")
    LUKASIEWICZ = pp.Keyword("lukasiewicz")
    GOEDEL = pp.Keyword("goedel")
    ZADEH = pp.Keyword("zadeh")
    PRODUCT = pp.Keyword("product")
    EQUAL = pp.Word("=")
    LES = pp.Keyword("les")
    LEQ = pp.Keyword("leq")
    GEQ = pp.Keyword("geq")
    GRE = pp.Keyword("gre")

    def get_name(self) -> str:
        return re.sub(r"[\"\']+", "", self.value.name.lower())

    def get_value(self) -> typing.Union[pp.CaselessKeyword, pp.Word]:
        return self.value

    def get_str_value(self) -> str:
        return str(self.value).replace('"', "").replace("'", "")

    def get_tag_name(self) -> str:
        return self.get_str_value().capitalize()

    def __eq__(self, value: object) -> bool:
        if isinstance(value, str):
            return self.get_name() == value.lower()
        elif isinstance(value, pp.Keyword):
            return self.get_name() == value.name.lower()
        elif isinstance(value, FuzzyOWL2Keyword):
            return self.get_name() == value.get_name()
        raise NotImplementedError

    def __repr__(self) -> str:
        return self.name

    def __str__(self) -> str:
        return self.name
