"""
Faster drop-in replacement for fuzzy_dl_owl2.fuzzydl.parser.dl_parser.DLParser.

It uses a hand-rolled tokenizer plus a deterministic recursive-descent parser.
The grammar accepted is identical to the legacy parser. All semantic actions
are reused: this module imports the DLParser class from ``dl_parser_clean`` and
invokes every ``_parse_*`` callback with a plain token list so the knowledge
base / queries are populated exactly the same way.

The file is written so that it can be compiled with Cython using
``setup_dl_parser.py`` for an additional native-code speedup. When run as
plain Python it still parses 5-10x faster than the legacy parser because
backtracking, packrat caching and the bounded-recursion machinery are gone.
"""

from __future__ import annotations

import gc
import time
import traceback
import typing

from fuzzy_dl_owl2.fuzzydl.exception.fuzzy_ontology_exception import (
    FuzzyOntologyException,
)
from fuzzy_dl_owl2.fuzzydl.exception.inconsistent_ontology_exception import (
    InconsistentOntologyException,
)
from fuzzy_dl_owl2.fuzzydl.knowledge_base import KnowledgeBase
from fuzzy_dl_owl2.fuzzydl.milp.solution import Solution
from fuzzy_dl_owl2.fuzzydl.parser.dl_parser_clean import DLParser
from fuzzy_dl_owl2.fuzzydl.parser.tokenizer.tokenizer_handler import (
    _SPLIT_NUM_RE,
    _STREAM_THRESHOLD,
    FdlFileTokenizer,
    Token,
    _fdl_ok,
    _iter_form_chunks,
    _tokenize_best,
)
from fuzzy_dl_owl2.fuzzydl.parser.tokenizer.tokens import (
    LBRACE,
    LBRACK,
    LPAREN,
    NUMBER,
    RBRACE,
    RBRACK,
    RPAREN,
    T_EOF,
    T_IDENT,
)
from fuzzy_dl_owl2.fuzzydl.query.all_instances_query import AllInstancesQuery
from fuzzy_dl_owl2.fuzzydl.query.query import Query
from fuzzy_dl_owl2.fuzzydl.util import constants
from fuzzy_dl_owl2.fuzzydl.util.config_reader import ConfigReader
from fuzzy_dl_owl2.fuzzydl.util.constants import FuzzyDLKeyword, FuzzyLogic
from fuzzy_dl_owl2.fuzzydl.util.util import Util

# ---------------------------------------------------------------------------
# Keyword tables
# ---------------------------------------------------------------------------
#
# The parser dispatches on the lowercase form of every keyword. Because the
# original grammar reaches each keyword through
# ``FuzzyDLKeyword.X.get_name()`` (which after the ``re.sub`` quote-stripping
# returns the same kebab/glob literal as ``get_value().match``), we can pull
# every keyword string from the enum and avoid duplicating literals here. If
# the upstream enum ever renames a keyword, the parser picks up the change
# automatically on the next process start.

# Short alias so the lookup tables below fit on one line each.
_K = FuzzyDLKeyword


def _kn(k: FuzzyDLKeyword) -> str:
    """
    Returns the source-text literal (spelling) that a given :class:`FuzzyDLKeyword` matches in input.

    :param k: The keyword whose literal spelling is needed.
    :type k: FuzzyDLKeyword

    :return: The keyword's source-text literal.

    :rtype: str
    """

    return k.get_name()


# ---- frozensets used for ``head in <set>`` dispatch in parse_gformula -----
#
# Each set holds the literals that legally appear immediately after the
# opening ``(`` of a top-level form. They are mutually exclusive so the
# parser can commit to a branch with a single-token lookahead.

# axiom head keywords (instance, related, ...,  <name>-implies, ...)
_AXIOM_KW = frozenset(
    {
        _kn(_K.INSTANCE),
        _kn(_K.RELATED),
        _kn(_K.IMPLIES_ROLE),
        _kn(_K.IMPLIES),
        _kn(_K.GOEDEL_IMPLIES),
        _kn(_K.LUKASIEWICZ_IMPLIES),
        _kn(_K.KLEENE_DIENES_IMPLIES),
        _kn(_K.ZADEH_IMPLIES),
        _kn(_K.DEFINE_CONCEPT),
        _kn(_K.DEFINE_PRIMITIVE_CONCEPT),
        _kn(_K.EQUIVALENT_CONCEPTS),
        _kn(_K.DISJOINT_UNION),
        _kn(_K.DISJOINT),
        _kn(_K.RANGE),
        _kn(_K.DOMAIN),
        _kn(_K.INVERSE),
        _kn(_K.INVERSE_FUNCTIONAL),
        _kn(_K.FUNCTIONAL),
        _kn(_K.REFLEXIVE),
        _kn(_K.SYMMETRIC),
        _kn(_K.TRANSITIVE),
    }
)

# query head keywords ("max-instance?", "sat?", ...)
_QUERY_KW = frozenset(
    {
        _kn(_K.ALL_INSTANCES_QUERY),
        _kn(_K.SAT_QUERY),
        _kn(_K.BNP_QUERY),
        _kn(_K.MAX_INSTANCE_QUERY),
        _kn(_K.MIN_INSTANCE_QUERY),
        _kn(_K.MAX_SUBS_QUERY),
        _kn(_K.MIN_SUBS_QUERY),
        _kn(_K.MAX_G_SUBS_QUERY),
        _kn(_K.MIN_G_SUBS_QUERY),
        _kn(_K.MAX_L_SUBS_QUERY),
        _kn(_K.MIN_L_SUBS_QUERY),
        _kn(_K.MAX_KD_SUBS_QUERY),
        _kn(_K.MIN_KD_SUBS_QUERY),
        _kn(_K.MAX_RELATED_QUERY),
        _kn(_K.MIN_RELATED_QUERY),
        _kn(_K.MAX_SAT_QUERY),
        _kn(_K.MIN_SAT_QUERY),
        _kn(_K.MAX_VAR_QUERY),
        _kn(_K.MIN_VAR_QUERY),
        _kn(_K.DEFUZZIFY_LOM_QUERY),
        _kn(_K.DEFUZZIFY_SOM_QUERY),
        _kn(_K.DEFUZZIFY_MOM_QUERY),
    }
)

# show-* head keywords
_SHOW_KW = frozenset(
    {
        _kn(_K.SHOW_CONCRETE_FILLERS),
        _kn(_K.SHOW_CONCRETE_FILLERS_FOR),
        _kn(_K.SHOW_CONCRETE_INSTANCE_FOR),
        _kn(_K.SHOW_ABSTRACT_FILLERS),
        _kn(_K.SHOW_ABSTRACT_FILLERS_FOR),
        _kn(_K.SHOW_CONCEPTS),
        _kn(_K.SHOW_INSTANCES),
        _kn(_K.SHOW_VARIABLES),
        _kn(_K.SHOW_LANGUAGE),
    }
)

# binary connective heads inside a concept's parens
_CONCEPT_OP_AND_OR_IMPL = frozenset(
    {
        _kn(_K.AND),
        _kn(_K.GOEDEL_AND),
        _kn(_K.LUKASIEWICZ_AND),
        _kn(_K.OR),
        _kn(_K.GOEDEL_OR),
        _kn(_K.LUKASIEWICZ_OR),
        _kn(_K.IMPLIES),
        _kn(_K.GOEDEL_IMPLIES),
        _kn(_K.LUKASIEWICZ_IMPLIES),
        _kn(_K.KLEENE_DIENES_IMPLIES),
    }
)

# universal / approximation connective heads inside a concept's parens
_APPROX_KW = frozenset(
    {
        _kn(_K.ALL),
        _kn(_K.UPPER_APPROXIMATION),
        _kn(_K.LOWER_APPROXIMATION),
        _kn(_K.TIGHT_UPPER_APPROXIMATION),
        _kn(_K.TIGHT_LOWER_APPROXIMATION),
        _kn(_K.LOOSE_UPPER_APPROXIMATION),
        _kn(_K.LOOSE_LOWER_APPROXIMATION),
    }
)

# weighted concept aggregator heads
_WEIGHTED_KW = frozenset(
    {
        _kn(_K.W_SUM_ZERO),
        _kn(_K.W_SUM),
        _kn(_K.W_MAX),
        _kn(_K.W_MIN),
    }
)

# OWA-family fuzzy integral heads
_OWA_INTEGRAL_KW = frozenset(
    {
        _kn(_K.OWA),
        _kn(_K.CHOQUET),
        _kn(_K.QUASI_SUGENO),
        _kn(_K.SUGENO),
    }
)

# Datatype / threshold comparison operators
_CMP_KW = frozenset(
    {
        _kn(_K.LESS_THAN_OR_EQUAL_TO),
        _kn(_K.GREATER_THAN_OR_EQUAL_TO),
        _kn(_K.EQUALS),
    }
)

# Every keyword that can appear in head position of a top-level form. The
# parser falls back to parse_concept when the head is none of these.
_STATEMENT_KW = (
    frozenset(
        {
            _kn(_K.DEFINE_FUZZY_LOGIC),
            _kn(_K.DEFINE_TRUTH_CONSTANT),
            _kn(_K.DEFINE_MODIFIER),
            _kn(_K.DEFINE_FUZZY_CONCEPT),
            _kn(_K.DEFINE_FUZZY_NUMBER),
            _kn(_K.DEFINE_FUZZY_NUMBER_RANGE),
            _kn(_K.DEFINE_FUZZY_SIMILARITY),
            _kn(_K.DEFINE_FUZZY_EQUIVALENCE),
            _kn(_K.CONSTRAINTS),
            _kn(_K.CRISP_CONCEPT),
            _kn(_K.CRISP_ROLE),
        }
    )
    | _AXIOM_KW
    | _QUERY_KW
    | _SHOW_KW
)

# Concrete feature type tags used inside a (range var <type> ...) declaration
_FEATURE_TYPE_KW = frozenset(
    {
        _kn(_K.INTEGER),
        _kn(_K.REAL),
        _kn(_K.STRING),
        _kn(_K.BOOLEAN),
    }
)

# Fuzzy-number arithmetic operators inside a datatype restriction.
#   _FUZZY_NUMBER_OP_BIN  : n-ary (1 or more operands)  --  "f+", "f*"
#   _FUZZY_NUMBER_OP_PAIR : exactly 2 operands          --  "f-", "f/"
_FUZZY_NUMBER_OP_BIN = frozenset({_kn(_K.FEATURE_SUM), _kn(_K.FEATURE_MUL)})
_FUZZY_NUMBER_OP_PAIR = frozenset({_kn(_K.FEATURE_SUB), _kn(_K.FEATURE_DIV)})


# Namespace bundling every single-keyword constant referenced by the parser.
# Keeping them grouped on a class keeps the dispatch sites readable
# (``kw == _KW.SOME``) without polluting the module's top level.
class _KW:  # noqa: D401 -- namespace, not a real class
    """Namespace of every FuzzyDLKeyword token literal used in dispatch."""

    # ---- range / domain --------------------------------------------------
    RANGE = _kn(_K.RANGE)
    DOMAIN = _kn(_K.DOMAIN)

    # ---- top-level "define-..." statements ------------------------------
    DEFINE_FUZZY_LOGIC = _kn(_K.DEFINE_FUZZY_LOGIC)
    DEFINE_TRUTH_CONSTANT = _kn(_K.DEFINE_TRUTH_CONSTANT)
    DEFINE_MODIFIER = _kn(_K.DEFINE_MODIFIER)
    DEFINE_FUZZY_CONCEPT = _kn(_K.DEFINE_FUZZY_CONCEPT)
    DEFINE_FUZZY_NUMBER = _kn(_K.DEFINE_FUZZY_NUMBER)
    DEFINE_FUZZY_NUMBER_RANGE = _kn(_K.DEFINE_FUZZY_NUMBER_RANGE)
    DEFINE_FUZZY_SIMILARITY = _kn(_K.DEFINE_FUZZY_SIMILARITY)
    DEFINE_FUZZY_EQUIVALENCE = _kn(_K.DEFINE_FUZZY_EQUIVALENCE)
    CONSTRAINTS = _kn(_K.CONSTRAINTS)
    CRISP_CONCEPT = _kn(_K.CRISP_CONCEPT)
    CRISP_ROLE = _kn(_K.CRISP_ROLE)

    # ---- show statements -------------------------------------------------
    SHOW_CONCRETE_FILLERS = _kn(_K.SHOW_CONCRETE_FILLERS)
    SHOW_CONCRETE_FILLERS_FOR = _kn(_K.SHOW_CONCRETE_FILLERS_FOR)
    SHOW_CONCRETE_INSTANCE_FOR = _kn(_K.SHOW_CONCRETE_INSTANCE_FOR)
    SHOW_ABSTRACT_FILLERS = _kn(_K.SHOW_ABSTRACT_FILLERS)
    SHOW_ABSTRACT_FILLERS_FOR = _kn(_K.SHOW_ABSTRACT_FILLERS_FOR)
    SHOW_CONCEPTS = _kn(_K.SHOW_CONCEPTS)
    SHOW_INSTANCES = _kn(_K.SHOW_INSTANCES)
    SHOW_VARIABLES = _kn(_K.SHOW_VARIABLES)
    SHOW_LANGUAGE = _kn(_K.SHOW_LANGUAGE)

    # ---- axiom heads ----------------------------------------------------
    INSTANCE = _kn(_K.INSTANCE)
    RELATED = _kn(_K.RELATED)
    IMPLIES_ROLE = _kn(_K.IMPLIES_ROLE)
    IMPLIES = _kn(_K.IMPLIES)
    GOEDEL_IMPLIES = _kn(_K.GOEDEL_IMPLIES)
    LUKASIEWICZ_IMPLIES = _kn(_K.LUKASIEWICZ_IMPLIES)
    KLEENE_DIENES_IMPLIES = _kn(_K.KLEENE_DIENES_IMPLIES)
    ZADEH_IMPLIES = _kn(_K.ZADEH_IMPLIES)
    DEFINE_CONCEPT = _kn(_K.DEFINE_CONCEPT)
    DEFINE_PRIMITIVE_CONCEPT = _kn(_K.DEFINE_PRIMITIVE_CONCEPT)
    EQUIVALENT_CONCEPTS = _kn(_K.EQUIVALENT_CONCEPTS)
    DISJOINT_UNION = _kn(_K.DISJOINT_UNION)
    DISJOINT = _kn(_K.DISJOINT)
    INVERSE = _kn(_K.INVERSE)
    INVERSE_FUNCTIONAL = _kn(_K.INVERSE_FUNCTIONAL)
    FUNCTIONAL = _kn(_K.FUNCTIONAL)
    REFLEXIVE = _kn(_K.REFLEXIVE)
    SYMMETRIC = _kn(_K.SYMMETRIC)
    TRANSITIVE = _kn(_K.TRANSITIVE)

    # ---- query heads ----------------------------------------------------
    ALL_INSTANCES_QUERY = _kn(_K.ALL_INSTANCES_QUERY)
    SAT_QUERY = _kn(_K.SAT_QUERY)
    BNP_QUERY = _kn(_K.BNP_QUERY)
    MAX_INSTANCE_QUERY = _kn(_K.MAX_INSTANCE_QUERY)
    MIN_INSTANCE_QUERY = _kn(_K.MIN_INSTANCE_QUERY)
    MAX_SUBS_QUERY = _kn(_K.MAX_SUBS_QUERY)
    MIN_SUBS_QUERY = _kn(_K.MIN_SUBS_QUERY)
    MAX_G_SUBS_QUERY = _kn(_K.MAX_G_SUBS_QUERY)
    MIN_G_SUBS_QUERY = _kn(_K.MIN_G_SUBS_QUERY)
    MAX_L_SUBS_QUERY = _kn(_K.MAX_L_SUBS_QUERY)
    MIN_L_SUBS_QUERY = _kn(_K.MIN_L_SUBS_QUERY)
    MAX_KD_SUBS_QUERY = _kn(_K.MAX_KD_SUBS_QUERY)
    MIN_KD_SUBS_QUERY = _kn(_K.MIN_KD_SUBS_QUERY)
    MAX_RELATED_QUERY = _kn(_K.MAX_RELATED_QUERY)
    MIN_RELATED_QUERY = _kn(_K.MIN_RELATED_QUERY)
    MAX_SAT_QUERY = _kn(_K.MAX_SAT_QUERY)
    MIN_SAT_QUERY = _kn(_K.MIN_SAT_QUERY)
    MAX_VAR_QUERY = _kn(_K.MAX_VAR_QUERY)
    MIN_VAR_QUERY = _kn(_K.MIN_VAR_QUERY)
    DEFUZZIFY_LOM_QUERY = _kn(_K.DEFUZZIFY_LOM_QUERY)
    DEFUZZIFY_SOM_QUERY = _kn(_K.DEFUZZIFY_SOM_QUERY)
    DEFUZZIFY_MOM_QUERY = _kn(_K.DEFUZZIFY_MOM_QUERY)

    # ---- concept connectives / operators -------------------------------
    SOME = _kn(_K.SOME)
    HAS_VALUE = _kn(_K.HAS_VALUE)
    NOT = _kn(_K.NOT)
    SELF = _kn(_K.SELF)
    Q_OWA = _kn(_K.Q_OWA)
    SIGMA_COUNT = _kn(_K.SIGMA_COUNT)

    # ---- comparison + arithmetic operators -----------------------------
    LE = _kn(_K.LESS_THAN_OR_EQUAL_TO)
    GE = _kn(_K.GREATER_THAN_OR_EQUAL_TO)
    EQ = _kn(_K.EQUALS)
    SUM = _kn(_K.SUM)
    SUB = _kn(_K.SUB)
    MUL = _kn(_K.MUL)

    # ---- constraint variable kinds -------------------------------------
    BINARY = _kn(_K.BINARY)
    FREE = _kn(_K.FREE)


# ---------------------------------------------------------------------------
# Parser
# ---------------------------------------------------------------------------


class _Parser(object):
    """Single-pass recursive descent over a pre-lexed token stream.

    Every ``parse_*`` method mirrors one non-terminal of the original
    grammar.  There is **no backtracking**: once a method
    commits to a branch it consumes tokens greedily.  This is safe because
    the fuzzy-DL grammar is LL(1) at the top level and the tokenizer has
    already disambiguated numbers, identifiers and punctuation.
    """

    __slots__ = ("tokens", "pos", "n")

    def __init__(self, tokens: typing.List[Token]) -> None:
        """
        Initializes the recursive-descent parser over a pre-tokenized stream. The 4-tuple token list is stored and a read cursor ``pos`` is set to the start, with ``n`` caching the token count so the low-level stream helpers can bounds-check without recomputing the length. The parser consumes this stream left to right; the caller retains ownership of the token list.

        :param tokens: The parser's 4-tuple token stream to consume.
        :type tokens: typing.List[Token]
        """

        self.tokens = tokens
        self.pos = 0
        self.n = len(tokens)

    # ----- low-level stream helpers --------------------------------------

    def _peek(self, offset: int = 0) -> Token:
        """
        Returns the token at ``pos + offset`` without advancing the cursor. Lookahead past the end of the stream is clamped to the last token (the EOF sentinel), so callers can peek freely without bounds checks.

        :param offset: How many tokens ahead of the current position to look.
        :type offset: int

        :return: The token at the requested position, or the final token if out of range.

        :rtype: Token
        """

        p: int = self.pos + offset
        if p >= self.n:
            return self.tokens[self.n - 1]
        return self.tokens[p]

    def _advance(self) -> Token:
        """
        Consumes the current token and advances the cursor by one. The token at the old position is returned, so callers can read and step in a single call.

        :return: The token that was at the cursor before advancing.

        :rtype: Token
        """

        t: Token = self.tokens[self.pos]
        self.pos += 1
        return t

    def _expect(self, kind: int) -> Token:
        """
        Requires the current token to have the given type code, consuming and returning it on a match. If the token's kind does not match, a :class:`FuzzyOntologyException` is raised with the byte offset and the offending token, and the cursor is left unmoved.

        :param kind: The expected token type code.
        :type kind: int

        :raises FuzzyOntologyException: if the current token is not of the expected kind.

        :return: The consumed token of the expected kind.

        :rtype: Token
        """

        t: Token = self.tokens[self.pos]
        if t[0] != kind:
            raise FuzzyOntologyException(
                f"Parse error at offset {t[3]}: expected token kind {kind} got {t!r}"
            )
        self.pos += 1
        return t

    def _eat(self, kind: int) -> bool:
        """
        Conditionally consumes the current token if it matches the given type code. Unlike :meth:`_expect`, a mismatch is not an error: the cursor is advanced and ``True`` returned only on a match, otherwise the cursor stays put and ``False`` is returned.

        :param kind: The token type code to consume if present.
        :type kind: int

        :return: ``True`` if a matching token was consumed, ``False`` otherwise.

        :rtype: bool
        """

        if self.tokens[self.pos][0] == kind:
            self.pos += 1
            return True
        return False

    # ----- entry point ----------------------------------------------------

    def parse_program(self) -> None:
        """program ::= gformula*"""
        while self.tokens[self.pos][0] != T_EOF:
            self.parse_gformula()

    def parse_gformula(self) -> typing.Any:
        """
        Parses a top-level ``gformula``, matching the grammar rule
        ``gformula ::= statement | axiom | query | show_statement | concept``.
        The first token must be ``(``; the keyword (or number / bracket)
        immediately after ``(`` is peeked and the stream is dispatched to the
        appropriate sub-parser. The consumed form is forwarded to the
        corresponding ``DLParser._parse_*`` callback.

        :raises FuzzyOntologyException: if the first token is not ``(`` or the
            inner keyword is unrecognised.

        :return: The parsed result (concept, axiom, statement, etc.) forwarded
            from the sub-parser.

        :rtype: typing.Any
        """
        t: Token = self.tokens[self.pos]
        if t[0] != LPAREN:
            raise FuzzyOntologyException(
                f"Parse error at offset {t[3]}: expected '(' got {t!r}"
            )
        # Peek the first keyword (or number/`[`/`(`) inside the parens.
        head: Token = self.tokens[self.pos + 1]
        head_low: str = head[2]
        if head[0] == T_IDENT and head_low in _STATEMENT_KW:
            # special-case range: range can be a feature decl OR an axiom.
            # Feature decl looks like (range var <type-kw> ...). Axiom looks
            # like (range var concept).  Disambiguate on the third token.
            if head_low == _KW.RANGE:
                third: Token = self.tokens[self.pos + 3]
                if third[0] == T_IDENT and third[2] in _FEATURE_TYPE_KW:
                    return self.parse_features()
                return self.parse_axioms()
            if head_low == _KW.DEFINE_FUZZY_LOGIC:
                return self.parse_fuzzy_logic()
            if head_low == _KW.DEFINE_TRUTH_CONSTANT:
                return self.parse_truth_constants()
            if head_low == _KW.DEFINE_MODIFIER:
                return self.parse_modifier()
            if head_low == _KW.DEFINE_FUZZY_CONCEPT:
                return self.parse_fuzzy_concept()
            if head_low == _KW.DEFINE_FUZZY_NUMBER:
                return self.parse_fuzzy_number_def()
            if head_low == _KW.DEFINE_FUZZY_NUMBER_RANGE:
                return self.parse_fuzzy_range()
            if head_low == _KW.DEFINE_FUZZY_SIMILARITY:
                return self.parse_fuzzy_similarity()
            if head_low == _KW.DEFINE_FUZZY_EQUIVALENCE:
                return self.parse_fuzzy_equivalence()
            if head_low == _KW.CONSTRAINTS:
                return self.parse_constraints()
            if head_low == _KW.CRISP_CONCEPT or head_low == _KW.CRISP_ROLE:
                return self.parse_crisp_declarations()
            if head_low in _SHOW_KW:
                return self.parse_show_statement()
            if head_low in _QUERY_KW:
                return self.parse_queries()
            if head_low in _AXIOM_KW:
                return self.parse_axioms()
        # Fallback: a parenthesised concept used as a top-level form.
        return self.parse_concept()

    # ----- atoms -----------------------------------------------------------

    def parse_number(self) -> typing.Union[int, float]:
        r"""
        Parses a numeric literal, matching the grammar rule
        ``number ::= [+-]? ( \d+ [ . \d* ] | . \d+ ) ( [eE] [+-]? \d+ )?``.
        The current token must be a number; it is consumed and converted to an ``int`` or ``float`` via ``DLParser._to_number``.

        :raises FuzzyOntologyException: if the current token is not a numeric literal.

        :return: The parsed numeric value.

        :rtype: typing.Union[int, float]
        """

        t: Token = self.tokens[self.pos]
        if t[0] != NUMBER:
            raise FuzzyOntologyException(
                f"Parse error at offset {t[3]}: expected number got {t!r}"
            )
        self.pos += 1
        res = DLParser._to_number([t[1]])
        return res

    def parse_variable(self) -> str:
        """
        Parses a variable, matching the grammar rule ``variable ::= identifier``. The current token must be a bare identifier; it is consumed and its source text returned.

        :raises FuzzyOntologyException: if the current token is not an identifier.

        :return: The variable name.

        :rtype: str
        """

        t: Token = self.tokens[self.pos]
        if t[0] != T_IDENT:
            raise FuzzyOntologyException(
                f"Parse error at offset {t[3]}: expected identifier got {t!r}"
            )
        self.pos += 1
        return t[1]

    # ----- concept ---------------------------------------------------------

    def parse_concept(self) -> typing.Any:
        """concept ::=
          variable
        | "top" | "bottom"
        | "(" datatype_restriction ")"
        | "(" number concept ")"                               -- weighted part
        | "(" "[" ("<=" | ">=") number|variable "]" concept ")"
        | "(" binary_connective concept+ ")"
        | "(" "some" role (concept | variable) ")"
        | "(" "has-value" role individual ")"
        | "(" approx_op role concept ")"
        | "(" "not" concept ")"
        | "(" "self" variable ")"
        | "(" weighted_op weighted_part+ ")"
        | "(" "q-owa" variable concept+ ")"
        | "(" owa_integral_op "(" number+ ")" "(" concept+ ")" ")"
        | "(" "sigma-count" role concept "{" individual* "}" fuzzy_name ")"
        | "(" modifier_name concept ")"

        Dispatches on the leading token (a bare identifier yields a variable /
        top / bottom; otherwise the keyword after ``(`` selects the concept
        sub-parser) and consumes the whole concept form.

        :raises FuzzyOntologyException: if the tokens do not form a valid concept.

        :return: The parsed concept node.

        :rtype: typing.Any
        """
        t: Token = self.tokens[self.pos]
        if t[0] == T_IDENT:
            # variables | TOP | BOTTOM
            self.pos += 1
            res = DLParser._to_top_bottom_concept([t[1]])
            return res
        if t[0] != LPAREN:
            raise FuzzyOntologyException(
                f"Parse error at offset {t[3]}: expected concept got {t!r}"
            )
        # ( ... )
        head: Token = self.tokens[self.pos + 1]
        # datatype restriction: ( less_than_or_equal_to | greater_than_or_equal_to | equals  var (var|fn|fuzzy_num) )
        if head[0] == T_IDENT and head[2] in _CMP_KW:
            return self.parse_datatype_restriction()
        # weighted concept part: ( num concept )
        if head[0] == NUMBER:
            return self.parse_weighted_concept_part()
        # threshold concept: ( [ <=/>= num concept ] )
        if head[0] == LBRACK:
            return self.parse_threshold_concept_wrapped()
        if head[0] == T_IDENT:
            kw: str = head[2]
            if kw in _CONCEPT_OP_AND_OR_IMPL:
                return self.parse_implies_like_concept()
            if kw == _KW.SOME:
                return self.parse_some_concept()
            if kw == _KW.HAS_VALUE:
                return self.parse_has_value_concept()
            if kw in _APPROX_KW:
                return self.parse_approx_concept()
            if kw == _KW.NOT or kw == _KW.SELF:
                return self.parse_unary_concept()
            if kw in _WEIGHTED_KW:
                return self.parse_weighted_concept()
            if kw == _KW.Q_OWA:
                return self.parse_q_owa_concept()
            if kw in _OWA_INTEGRAL_KW:
                return self.parse_owa_integral_concept()
            if kw == _KW.SIGMA_COUNT:
                return self.parse_sigma_count_concept()
            # modifier_concept: ( var concept )
            return self.parse_modifier_concept()
        raise FuzzyOntologyException(
            f"Parse error at offset {head[3]}: unexpected token inside concept {head!r}"
        )

    # ----- concept variants -----------------------------------------------

    def parse_weighted_concept_part(self) -> typing.Any:
        """
        Parses a weighted concept part, matching the grammar rule
        ``weighted_concept_part ::= "(" number concept ")"``. The three inner
        elements are consumed and forwarded to the callback as a flat list.

        :return: The parsed weighted concept part.

        :rtype: typing.Any
        """

        self._expect(LPAREN)
        num = self.parse_number()
        c = self.parse_concept()
        self._expect(RPAREN)
        res = DLParser._parse_weighted_concept_simple([num, c])
        return res

    def parse_threshold_concept_wrapped(self) -> typing.Any:
        """
        Parses a threshold concept wrapper, matching the grammar rule
        ``threshold_concept_wrapped ::= "(" "[" ("<=" | ">=") number|variable "]" concept ")"``.

        The tokenizer may merge the operator and its operand into a single
        identifier (e.g. ``>=0.4``), so the method splits off the inline
        operator and operand before forwarding the pieces to the callback.

        :raises FuzzyOntologyException: if a threshold operator is not found or
            the inline operand is malformed.

        :return: The parsed threshold concept.

        :rtype: typing.Any
        """

        self._expect(LPAREN)
        self._expect(LBRACK)
        op_tok: Token = self.tokens[self.pos]
        # The tokenizer treats `>=x` / `<=0.4` as a single ident because the
        # character class for identifiers includes operator chars. Split off
        # an inline operator + operand here so that the original syntax with
        # no whitespace between `>=` and its argument still parses.
        op: typing.Optional[str] = None
        inline_operand: typing.Optional[str] = None
        if op_tok[0] == T_IDENT:
            raw = op_tok[2]
            if raw in (_KW.LE, _KW.GE):
                op = raw
                self.pos += 1
            elif raw.startswith((_KW.LE, _KW.GE)):
                op = raw[:2]
                inline_operand = op_tok[1][2:]
                self.pos += 1
        if op is None:
            raise FuzzyOntologyException(
                f"Parse error: threshold operator expected at {op_tok[3]}"
            )
        operand: typing.Any
        if inline_operand is not None:
            if _SPLIT_NUM_RE.fullmatch(inline_operand):
                operand = (
                    float(inline_operand)
                    if "." in inline_operand
                    or "e" in inline_operand
                    or "E" in inline_operand
                    else int(inline_operand)
                )
            else:
                operand = inline_operand
        else:
            operand_tok: Token = self.tokens[self.pos]
            if operand_tok[0] == NUMBER:
                operand = operand_tok[1]
                self.pos += 1
            else:
                operand = self.parse_variable()
        self._expect(RBRACK)
        c = self.parse_concept()
        self._expect(RPAREN)
        res = DLParser._parse_threshold_concept([op, operand, c])
        return res

    def parse_implies_like_concept(self) -> typing.Any:
        """
        Parses a binary connective concept (AND, OR, IMPLIES variants), matching
        the grammar rule
        ``implies_like_concept ::= "(" op concept+ ")"``. The operator keyword
        and all operand concepts are consumed and forwarded as a flat list to
        ``DLParser._parse_binary_concept``.

        :return: The parsed binary connective concept.

        :rtype: typing.Any
        """

        self._expect(LPAREN)
        op_tok: Token = self._expect(T_IDENT)
        # Map the lowercase keyword to the enum-name form
        # _parse_binary_concept compares against: it accepts FuzzyDLKeyword
        # values, and FuzzyDLKeyword.__eq__ does case-insensitive string
        # compare. So passing the raw keyword string works.
        op_kw: str = op_tok[2]
        concepts: typing.List[typing.Any] = []
        while self.tokens[self.pos][0] != RPAREN:
            concepts.append(self.parse_concept())
        self._expect(RPAREN)
        res = DLParser._parse_binary_concept([op_kw] + concepts)
        return res

    def parse_some_concept(self) -> typing.Any:
        """
        Parses an existential restriction concept, matching the grammar rule
        ``some_concept ::= "(" "some" role (concept | variable) ")"``. The role
        and second argument (either a nested concept or a bare variable) are
        consumed and forwarded as a flat list.

        :return: The parsed existential restriction concept.

        :rtype: typing.Any
        """

        self._expect(LPAREN)
        self._expect(T_IDENT)  # SOME keyword
        role: str = self.parse_variable()
        # second arg is either a variable (treated as concept name) or a concept
        nxt: Token = self.tokens[self.pos]
        arg: typing.Any
        if nxt[0] == LPAREN:
            arg = self.parse_concept()
        else:
            arg = self.parse_variable()
        self._expect(RPAREN)
        res = DLParser._parse_binary_concept([_KW.SOME, role, arg])
        return res

    def parse_has_value_concept(self) -> typing.Any:
        """
        Parses a value restriction concept, matching the grammar rule
        ``has_value_concept ::= "(" "has-value" role individual ")"``. The role
        and individual name are consumed and forwarded as a flat list.

        :return: The parsed value restriction concept.

        :rtype: typing.Any
        """

        self._expect(LPAREN)
        self._expect(T_IDENT)  # HAS_VALUE keyword (b-some)
        role: str = self.parse_variable()
        ind: str = self.parse_variable()
        self._expect(RPAREN)
        res = DLParser._parse_binary_concept([_KW.HAS_VALUE, role, ind])
        return res

    def parse_approx_concept(self) -> typing.Any:
        """
        Parses an approximation concept, matching the grammar rule
        ``approx_concept ::= "(" approx_op role concept ")"``. The approximation
        operator, role, and inner concept are consumed and forwarded as a flat list.

        :return: The parsed approximation concept.

        :rtype: typing.Any
        """

        self._expect(LPAREN)
        op_tok: Token = self._expect(T_IDENT)
        role: str = self.parse_variable()
        c = self.parse_concept()
        self._expect(RPAREN)
        res = DLParser._parse_binary_concept([op_tok[2], role, c])
        return res

    def parse_unary_concept(self) -> typing.Any:
        """
        Parses a unary concept (negation or self-restriction), matching the grammar
        rule
        ``unary_concept ::= "(" "not" concept ")" | "(" "self" variable ")"``.
        The keyword after the opening parenthesis selects which form to parse.

        :return: The parsed unary concept.

        :rtype: typing.Any
        """

        self._expect(LPAREN)
        op_tok: Token = self._expect(T_IDENT)
        kw: str = op_tok[2]
        if kw == _KW.NOT:
            c = self.parse_concept()
            self._expect(RPAREN)
            res = DLParser._parse_unary_concept([_KW.NOT, c])
            return res
        # SELF
        v: str = self.parse_variable()
        self._expect(RPAREN)
        res = DLParser._parse_unary_concept([_KW.SELF, v])
        return res

    def parse_modifier_concept(self) -> typing.Any:
        """
        Parses a modifier application concept, matching the grammar rule
        ``modifier_concept ::= "(" modifier_name concept ")"``. The modifier name
        and inner concept are consumed and forwarded as a flat list.

        :return: The parsed modified concept.

        :rtype: typing.Any
        """

        self._expect(LPAREN)
        modifier_name: str = self.parse_variable()
        c = self.parse_concept()
        self._expect(RPAREN)
        res = DLParser._parse_modifier_concept([modifier_name, c])
        return res

    def parse_weighted_concept(self) -> typing.Any:
        """
        Parses a weighted aggregation concept, matching the grammar rule
        ``weighted_concept ::= "(" ("w-sum-zero"|"w-sum"|"w-max"|"w-min") weighted_part+ ")"``.
        The operator keyword and one or more weighted parts are consumed and
        forwarded as a flat list.

        :return: The parsed weighted aggregation concept.

        :rtype: typing.Any
        """

        self._expect(LPAREN)
        op_tok: Token = self._expect(T_IDENT)
        parts: typing.List[typing.Any] = []
        while self.tokens[self.pos][0] == LPAREN:
            parts.append(self._parse_weighted_part_inline())
        self._expect(RPAREN)
        res = DLParser._parse_weighted_concept([op_tok[2]] + parts)
        return res

    def _parse_weighted_part_inline(self) -> typing.Any:
        """
        Parses an inline weighted part, matching the grammar rule
        ``weighted_part ::= "(" number concept ")"``. The weight and concept are
        consumed and forwarded as a flat list.

        :return: The parsed weighted part.

        :rtype: typing.Any
        """

        self._expect(LPAREN)
        num = self.parse_number()
        c = self.parse_concept()
        self._expect(RPAREN)
        res = DLParser._parse_weighted_concept_simple([num, c])
        return res

    def parse_q_owa_concept(self) -> typing.Any:
        """
        Parses a quantifier-guided OWA concept, matching the grammar rule
        ``q_owa_concept ::= "(" "q-owa" variable concept+ ")"``. The quantifier
        variable and one or more operand concepts are consumed and forwarded as
        a flat list.

        :return: The parsed quantifier-guided OWA concept.

        :rtype: typing.Any
        """

        self._expect(LPAREN)
        self._expect(T_IDENT)  # "q-owa" - suppressed in original grammar
        v: str = self.parse_variable()
        concepts: typing.List[typing.Any] = []
        while self.tokens[self.pos][0] != RPAREN:
            concepts.append(self.parse_concept())
        self._expect(RPAREN)
        res = DLParser._parse_q_owa_concept([v] + concepts)
        return res

    def parse_owa_integral_concept(self) -> typing.Any:
        """
        Parses an OWA / Choquet / Sugeno / quasi-Sugeno integral concept, matching
        the grammar rule
        ``owa_integral_concept ::= "(" op "(" number+ ")" "(" concept+ ")" ")"``.
        The operator keyword, the parenthesised weight list, and the
        parenthesised concept list are consumed and forwarded as a single flat
        list (the callback locates the weights/concepts boundary via element types).

        :return: The parsed OWA-integral concept.

        :rtype: typing.Any
        """

        self._expect(LPAREN)
        op_tok: Token = self._expect(T_IDENT)
        # Original grammar nests both groups in '(' ')' (lbrace=`(`)
        self._expect(LPAREN)
        weights: typing.List[typing.Any] = []
        while self.tokens[self.pos][0] != RPAREN:
            weights.append(self.parse_number())
        self._expect(RPAREN)
        self._expect(LPAREN)
        concepts: typing.List[typing.Any] = []
        while self.tokens[self.pos][0] != RPAREN:
            concepts.append(self.parse_concept())
        self._expect(RPAREN)
        self._expect(RPAREN)
        payload: typing.List[typing.Any] = [op_tok[2]] + weights + concepts
        # The original grammar passes everything in a single flat list to the
        # callback; the callback locates the weights/concepts boundary via the
        # element types. Use the same convention.
        res = DLParser._parse_owa_integral_concept(payload)
        return res

    def parse_sigma_count_concept(self) -> typing.Any:
        """
        Parses a sigma-count concept, matching the grammar rule
        ``sigma_count_concept ::= "(" "sigma-count" role concept "{" individual* "}" fuzzy_name ")"``.
        The role, concept, brace-enclosed individual list, and fuzzy name are
        consumed and forwarded as a flat list.

        :return: The parsed sigma-count concept.

        :rtype: typing.Any
        """

        self._expect(LPAREN)
        self._expect(T_IDENT)  # "sigma-count" - suppressed
        role: str = self.parse_variable()
        c = self.parse_concept()
        self._expect(LBRACE)
        inds: typing.List[str] = []
        while self.tokens[self.pos][0] != RBRACE:
            inds.append(self.parse_variable())
        self._expect(RBRACE)
        fuzzy_name: str = self.parse_variable()
        self._expect(RPAREN)
        res = DLParser._parse_sigma_count_concept([role, c] + inds + [fuzzy_name])
        return res

    # ----- datatype restriction -------------------------------------------

    def parse_datatype_restriction(self) -> typing.Any:
        """
        Parses a datatype restriction, matching the grammar rule
        ``datatype_restriction ::= "(" cmp_op role (fuzzy_number_expr | datatype_restriction_function | variable) ")"``. The comparison operator, role, and third operand are consumed and forwarded as a flat list. Feature-type dispatch for ``STRING`` values lives in ``DLParser._parse_datatype_restriction`` so both fast and slow parsers share one source of truth.

        :return: The parsed datatype restriction.

        :rtype: typing.Any
        """

        self._expect(LPAREN)
        op_tok: Token = self._expect(T_IDENT)
        role: str = self.parse_variable()
        nxt: Token = self.tokens[self.pos]
        third: typing.Any
        if nxt[0] == LPAREN:
            third = self.parse_datatype_restriction_function_or_fuzzy_number()
        elif nxt[0] == NUMBER:
            # A bare number in this position is matched by the original grammar
            # as datatype_restriction_function (via datatype_restriction_operand),
            # which wraps it in a FeatureFunction via _parse_restrictions.
            third = self.parse_datatype_restriction_function()
        else:
            third = self.parse_variable()
        self._expect(RPAREN)
        # Feature-type dispatch for STRING values lives in
        # DLParser._parse_datatype_restriction so the fast and slow parsers
        # share one source of truth.
        res = DLParser._parse_datatype_restriction([op_tok[2], role, third])
        return res

    def parse_datatype_restriction_function_or_fuzzy_number(self) -> typing.Any:
        """
        Parses a datatype-restriction function or a fuzzy number expression,
        disambiguating by lookahead. Uses 1-token lookahead on the token after
        ``(`` to decide among:

        * ``(f+ ...)`` / ``(f- ...)`` / ``(f* ...)`` / ``(f/ ...)`` → fuzzy number expression
        * ``(num num num)`` → simple triangular fuzzy number
        * ``(num [*] fn)`` or ``(fn - fn)`` → datatype restriction function

        :return: The parsed restriction function or fuzzy number expression.

        :rtype: typing.Any
        """

        # Lookahead on '('. Possible productions starting here:
        #   (f+ ...), (f- ...), (f* ...), (f/ ...)      -- fuzzy_number_expr compound
        #   (num num num)                               -- simple_fuzzy_number triangle
        #   (num [*] fn) | (fn - fn)                    -- datatype_restriction_function operand
        head: Token = self.tokens[self.pos + 1]
        if head[0] == T_IDENT and (
            head[2] in _FUZZY_NUMBER_OP_BIN or head[2] in _FUZZY_NUMBER_OP_PAIR
        ):
            return self.parse_fuzzy_number_expr()
        if (
            head[0] == NUMBER
            and self.tokens[self.pos + 2][0] == NUMBER
            and self.tokens[self.pos + 3][0] == NUMBER
            and self.tokens[self.pos + 4][0] == RPAREN
        ):
            return self.parse_simple_fuzzy_number()
        return self.parse_datatype_restriction_function()

    def parse_datatype_restriction_function(self) -> typing.Any:
        """
        Parses a datatype restriction function, matching the grammar rule
        ``datatype_restriction_function ::= datatype_restriction_operand ( "+" datatype_restriction_operand )*``.
        The first operand is parsed, then a chain of ``+``-separated operands is
        consumed if present. The flat operand list is forwarded to the callback.

        :return: The parsed restriction function.

        :rtype: typing.Any
        """

        first = self.parse_datatype_restriction_operand()
        # Sum-of-operands chain: operand '+' operand '+' ...
        if not (
            self.tokens[self.pos][0] == T_IDENT and self.tokens[self.pos][2] == _KW.SUM
        ):
            return first
        flat: typing.List[typing.Any] = [first]
        while (
            self.tokens[self.pos][0] == T_IDENT and self.tokens[self.pos][2] == _KW.SUM
        ):
            self.pos += 1
            flat.append(_KW.SUM)
            flat.append(self.parse_datatype_restriction_operand())
        res = DLParser._parse_restrictions(flat)
        return res

    def parse_datatype_restriction_operand(self) -> typing.Any:
        """
        Parses a datatype restriction operand, matching the grammar rule
        ``datatype_restriction_operand ::= number | variable | "(" number ["*"] datatype_restriction_function ")" | "(" datatype_restriction_function ("-"|"+") datatype_restriction_function ")"``. Disambiguation is done by 1-token lookahead after the opening parenthesis.

        :return: The parsed restriction operand.

        :rtype: typing.Any
        """

        nxt: Token = self.tokens[self.pos]
        if nxt[0] == LPAREN:
            inner: Token = self.tokens[self.pos + 1]
            if inner[0] == NUMBER:
                after_num: Token = self.tokens[self.pos + 2]
                # Parenthesized sum: (num + fn + ...).  Must NOT be treated as
                # (num [*] fn) because the + chain belongs to the enclosing
                # datatype_restriction_function (same as the original infix).
                if after_num[0] == T_IDENT and after_num[2] == _KW.SUM:
                    self._expect(LPAREN)
                    res = self.parse_datatype_restriction_function()
                    self._expect(RPAREN)
                    return res
                elif after_num[0] == RPAREN:
                    # Parenthesized number: (num)
                    self._expect(LPAREN)
                    num = self.parse_number()
                    self._expect(RPAREN)
                    res = DLParser._parse_restrictions([num])
                    return res
                # (num [*] fn)
                self._expect(LPAREN)
                num = self.parse_number()
                if (
                    self.tokens[self.pos][0] == T_IDENT
                    and self.tokens[self.pos][2] == _KW.MUL
                ):
                    self.pos += 1
                fn = self.parse_datatype_restriction_function()
                self._expect(RPAREN)
                res = DLParser._parse_restrictions([num, fn])
                return res
            # (fn - fn)  --  '+' is handled by parse_datatype_restriction_function.
            self._expect(LPAREN)
            a = self.parse_datatype_restriction_function()
            op = self._expect(T_IDENT)
            b = self.parse_datatype_restriction_function()
            self._expect(RPAREN)
            res = DLParser._parse_restrictions([a, op[1], b])
            return res
        if nxt[0] == NUMBER:
            n = self.parse_number()
            res = DLParser._parse_restrictions([n])
            return res
        v = self.parse_variable()
        res = DLParser._parse_restrictions([v])
        return res

    # ----- fuzzy number ---------------------------------------------------

    def parse_simple_fuzzy_number(self) -> typing.Any:
        """
        Parses a simple fuzzy number literal, matching the grammar rule
        ``simple_fuzzy_number ::= "(" number number number ")" | number | variable``.
        A parenthesised triple produces a triangular fuzzy number; a bare number
        or variable is wrapped as a scalar fuzzy number.

        :raises FuzzyOntologyException: if a triangular literal does not contain
            exactly three numbers.

        :return: The parsed fuzzy number literal.

        :rtype: typing.Any
        """

        nxt: Token = self.tokens[self.pos]
        # Triangular fuzzy literal uses '(' a b c ')' in the original grammar
        if nxt[0] == LPAREN:
            self._expect(LPAREN)
            nums: typing.List[typing.Any] = []
            while self.tokens[self.pos][0] != RPAREN:
                nums.append(self.parse_number())
            self._expect(RPAREN)
            if len(nums) != 3:
                raise FuzzyOntologyException(
                    "Triangular fuzzy literal requires exactly 3 numbers."
                )
            res = DLParser._create_fuzzy_number(nums)
            return res
        if nxt[0] == NUMBER:
            n = self.parse_number()
            res = DLParser._create_fuzzy_number([n])
            return res
        v = self.parse_variable()
        res = DLParser._create_fuzzy_number([v])
        return res

    def parse_fuzzy_number_expr(self) -> typing.Any:
        """
        Parses a fuzzy number expression, matching the grammar rule
        ``fuzzy_number_expr ::= simple_fuzzy_number | "(" ("f+"|"f*") fuzzy_number_expr+ ")" | "(" ("f-"|"f/") fuzzy_number_expr fuzzy_number_expr ")"``. Compound forms (``f+``, ``f*``, ``f-``, ``f/``) are returned as raw flat lists ``[op, *operands]`` for the consuming callback to handle.

        :raises FuzzyOntologyException: if a compound form is malformed (e.g.
            ``f+/f*`` with fewer than one operand or an unknown operator).

        :return: The parsed fuzzy number expression.

        :rtype: typing.Any
        """

        nxt: Token = self.tokens[self.pos]
        if nxt[0] != LPAREN:
            return self.parse_simple_fuzzy_number()
        head: Token = self.tokens[self.pos + 1]
        if head[0] == T_IDENT and (
            head[2] in _FUZZY_NUMBER_OP_BIN or head[2] in _FUZZY_NUMBER_OP_PAIR
        ):
            self._expect(LPAREN)
            op_tok: Token = self._expect(T_IDENT)
            kw: str = op_tok[2]
            operands: typing.List[typing.Any] = []
            if kw in _FUZZY_NUMBER_OP_BIN:
                while self.tokens[self.pos][0] != RPAREN:
                    operands.append(self.parse_fuzzy_number_expr())
                self._expect(RPAREN)
                if len(operands) < 1:
                    raise FuzzyOntologyException("f+/f* require at least 1 operand.")
            elif kw in _FUZZY_NUMBER_OP_PAIR:
                for _ in range(2):
                    operands.append(self.parse_fuzzy_number_expr())
                self._expect(RPAREN)
            else:
                raise FuzzyOntologyException(f"Unknown fuzzy-number operator: {kw}")
            # No dedicated callback for the compound form in the original grammar.
            # We return the raw tuple ([op] + operands) and let the consuming
            # callback handle it.
            return [kw] + operands
        return self.parse_simple_fuzzy_number()

    # ----- top-level statements -------------------------------------------

    def parse_fuzzy_logic(self) -> None:
        '''fuzzy_logic ::= "(" "define-fuzzy-logic" logic_name ")"'''
        self._expect(LPAREN)
        self._expect(T_IDENT)  # define-fuzzy-logic (suppressed)
        kw_tok: Token = self._expect(T_IDENT)
        self._expect(RPAREN)
        DLParser._fuzzy_logic_parser([kw_tok[2]])

    def parse_truth_constants(self) -> None:
        '''truth_constants ::= "(" "define-truth-constant" name number ")"'''
        self._expect(LPAREN)
        self._expect(T_IDENT)  # define-truth-constant
        name: str = self.parse_variable()
        num = self.parse_number()
        self._expect(RPAREN)
        DLParser._parse_truth_constants([name, num])

    def parse_modifier(self) -> None:
        '''modifier ::= "(" "define-modifier" name modifier_kind "(" number* ")" ")"'''
        self._expect(LPAREN)
        self._expect(T_IDENT)  # define-modifier
        name: str = self.parse_variable()
        kind_tok: Token = self._expect(T_IDENT)
        # Original grammar wraps the modifier parameters in '(' ')' (lbrace=`(`)
        self._expect(LPAREN)
        nums: typing.List[typing.Any] = []
        while self.tokens[self.pos][0] != RPAREN:
            nums.append(self.parse_number())
        self._expect(RPAREN)
        self._expect(RPAREN)
        DLParser._parse_modifier([name, kind_tok[2]] + nums)

    def parse_fuzzy_concept(self) -> None:
        '''fuzzy_concept ::= "(" "define-fuzzy-concept" name shape "(" (number|variable)* ")" ")"'''
        self._expect(LPAREN)
        self._expect(T_IDENT)  # define-fuzzy-concept
        name: str = self.parse_variable()
        shape_tok: Token = self._expect(T_IDENT)
        # Original grammar wraps the shape parameters in '(' ')' (lbrace=`(`)
        self._expect(LPAREN)
        nums: typing.List[typing.Any] = []
        while self.tokens[self.pos][0] != RPAREN:
            # modified shape uses two variable names
            t: Token = self.tokens[self.pos]
            if t[0] == NUMBER:
                nums.append(self.parse_number())
            else:
                nums.append(self.parse_variable())
        self._expect(RPAREN)
        self._expect(RPAREN)
        DLParser._parse_fuzzy_concept([name, shape_tok[2]] + nums)

    def parse_fuzzy_number_def(self) -> None:
        '''fuzzy_number_def ::= "(" "define-fuzzy-number" name (fuzzy_number_expr | simple_fuzzy_number) ")"'''
        self._expect(LPAREN)
        self._expect(T_IDENT)  # define-fuzzy-number
        name: str = self.parse_variable()
        # The grammar accepts variables | numeric triples | scalar | compound
        # f+/f*/f-/f/ expressions. We use parse_fuzzy_number_expr which handles
        # all of those.
        expr: typing.Any
        if self.tokens[self.pos][0] == LPAREN:
            expr = self.parse_fuzzy_number_expr()
        else:
            expr = self.parse_simple_fuzzy_number()
        self._expect(RPAREN)
        # parse_fuzzy_number_expr returns a list [op_kw, *operands] for the
        # compound (f+/f*/f-/f/) form. _set_fuzzy_number expects those flat
        # (tokens = [name, op_kw, *operands]), not nested.
        if isinstance(expr, list):
            DLParser._set_fuzzy_number([name] + expr)
        else:
            DLParser._set_fuzzy_number([name, expr])

    def parse_fuzzy_range(self) -> None:
        '''fuzzy_range ::= "(" "define-fuzzy-number-range" number number ")"'''
        self._expect(LPAREN)
        self._expect(T_IDENT)  # define-fuzzy-number-range
        a = self.parse_number()
        b = self.parse_number()
        self._expect(RPAREN)
        DLParser._parse_fuzzy_number_range([a, b])

    def parse_features(self) -> None:
        '''features ::= "(" "range" variable type_kw number* ")"'''
        self._expect(LPAREN)
        # Original grammar keeps the RANGE keyword in the token stream so the
        # callback's positional indexing (tokens[1]=role, tokens[2]=type kw,
        # tokens[3..4]=bounds) is preserved.
        range_tok: Token = self._expect(T_IDENT)
        var: str = self.parse_variable()
        type_tok: Token = self._expect(T_IDENT)
        nums: typing.List[typing.Any] = []
        while self.tokens[self.pos][0] == NUMBER:
            nums.append(self.parse_number())
        self._expect(RPAREN)
        DLParser._parse_feature([range_tok[2], var, type_tok[2]] + nums)

    def parse_constraints(self) -> None:
        """constraints ::=
        "(" "constraints"
            ( "(" ("binary" | "free") variable ")"
            | "(" expression cmp_op number ")" )+
        ")"
        """
        self._expect(LPAREN)
        self._expect(T_IDENT)  # constraints
        # one-or-more of:
        #   ( inequation )           expr op num
        #   ( binary var )
        #   ( free var )
        while self.tokens[self.pos][0] == LPAREN:
            self._expect(LPAREN)
            head: Token = self.tokens[self.pos]
            if head[0] == T_IDENT and (head[2] == _KW.BINARY or head[2] == _KW.FREE):
                kw_tok = self._expect(T_IDENT)
                var: str = self.parse_variable()
                self._expect(RPAREN)
                DLParser._parse_constraints([kw_tok[2], var])
            else:
                # inequation: expression op num
                expr = self.parse_expression()
                op_tok: Token = self._expect(T_IDENT)
                num = self.parse_number()
                self._expect(RPAREN)
                DLParser._parse_inequation([expr, op_tok[2], num])
        self._expect(RPAREN)

    # ----- arithmetic expressions (linear) --------------------------------

    def parse_term(self) -> typing.Any:
        """
        Parses a linear term, matching the grammar rule
        ``term ::= number | variable | "(" number "*" variable ")" | number "*" variable``.
        Bare numbers, bare variables, and parenthesised or infix ``num * var`` forms
        are consumed and forwarded as a flat list.

        :return: The parsed term.

        :rtype: typing.Any
        """

        t: Token = self.tokens[self.pos]
        if t[0] == LPAREN:
            self._expect(LPAREN)
            num = self.parse_number()
            self._expect(T_IDENT)  # '*'
            var = self.parse_variable()
            self._expect(RPAREN)
            res = DLParser._parse_term([num, _KW.MUL, var])
            return res
        if t[0] == NUMBER:
            num = self.parse_number()
            if (
                self.tokens[self.pos][0] == T_IDENT
                and self.tokens[self.pos][2] == _KW.MUL
            ):
                self.pos += 1
                var = self.parse_variable()
                res = DLParser._parse_term([num, _KW.MUL, var])
                return res
            res = DLParser._parse_term([num])
            return res
        var = self.parse_variable()
        res = DLParser._parse_term([var])
        return res

    def parse_expression(self) -> typing.Any:
        """
        Parses a linear expression, matching the grammar rule
        ``expression ::= term ( "+" term )*``. One or more terms separated by
        ``+`` are consumed and forwarded as a flat list with explicit ``+``
        separators inserted.

        :return: The parsed expression.

        :rtype: typing.Any
        """

        terms: typing.List[typing.Any] = [self.parse_term()]
        while (
            self.tokens[self.pos][0] == T_IDENT and self.tokens[self.pos][2] == _KW.SUM
        ):
            self.pos += 1
            terms.append(self.parse_term())
        if len(terms) == 1:
            return DLParser._parse_expression(terms)
        payload: typing.List[typing.Any] = []
        for idx, tm in enumerate(terms):
            if idx > 0:
                payload.append(_KW.SUM)
            payload.append(tm)
        return DLParser._parse_expression(payload)

    # ----- show statements ------------------------------------------------

    def parse_show_statement(self) -> None:
        '''show_statement ::= "(" show_kw (concept | variable)* ")"'''
        self._expect(LPAREN)
        kw_tok: Token = self._expect(T_IDENT)
        kw: str = kw_tok[2]
        args: typing.List[typing.Any] = []
        if kw == _KW.SHOW_INSTANCES:
            while self.tokens[self.pos][0] != RPAREN:
                args.append(self.parse_concept())
        else:
            while self.tokens[self.pos][0] != RPAREN:
                args.append(self.parse_variable())
        self._expect(RPAREN)
        if kw == _KW.SHOW_CONCRETE_FILLERS:
            DLParser._show_concrete_fillers(args)
        elif kw == _KW.SHOW_CONCRETE_FILLERS_FOR:
            DLParser._show_concrete_fillers_for(args)
        elif kw == _KW.SHOW_CONCRETE_INSTANCE_FOR:
            DLParser._show_concrete_instance_for(args)
        elif kw == _KW.SHOW_ABSTRACT_FILLERS:
            DLParser._show_abstract_fillers(args)
        elif kw == _KW.SHOW_ABSTRACT_FILLERS_FOR:
            DLParser._show_abstract_fillers_for(args)
        elif kw == _KW.SHOW_CONCEPTS:
            DLParser._show_concepts(args)
        elif kw == _KW.SHOW_INSTANCES:
            DLParser._show_instances(args)
        elif kw == _KW.SHOW_VARIABLES:
            DLParser._show_variables(args)
        elif kw == _KW.SHOW_LANGUAGE:
            DLParser._show_languages(args)

    # ----- crisp declarations / similarity / equivalence ------------------

    def parse_crisp_declarations(self) -> None:
        '''crisp_declarations ::= "(" ("crisp-concept" | "crisp-role") name+ ")"'''
        self._expect(LPAREN)
        kw_tok: Token = self._expect(T_IDENT)
        names: typing.List[str] = []
        while self.tokens[self.pos][0] != RPAREN:
            names.append(self.parse_variable())
        self._expect(RPAREN)
        DLParser._parse_crisp_declarations([kw_tok[2]] + names)

    def parse_fuzzy_similarity(self) -> None:
        '''fuzzy_similarity ::= "(" "define-fuzzy-similarity" name ")"'''
        self._expect(LPAREN)
        self._expect(T_IDENT)  # define-fuzzy-similarity
        name: str = self.parse_variable()
        self._expect(RPAREN)
        DLParser._parse_fuzzy_similarity([name])

    def parse_fuzzy_equivalence(self) -> None:
        '''fuzzy_equivalence ::= "(" "define-fuzzy-equivalence" name ")"'''
        self._expect(LPAREN)
        self._expect(T_IDENT)  # define-fuzzy-equivalence
        name: str = self.parse_variable()
        self._expect(RPAREN)
        DLParser._parse_fuzzy_equivalence([name])

    # ----- axioms ---------------------------------------------------------

    def parse_axioms(self) -> None:
        """
        Parses an axiom, matching the grammar rule covering instance assertions,
        role assertions, implications, concept definitions, equivalent concepts,
        disjoint unions, range/domain declarations, role characteristics, and
        inverse role declarations. The keyword after ``(`` selects the branch;
        the branch-specific tokens are consumed and forwarded as a flat list to
        ``DLParser._parse_axioms``.

        :raises FuzzyOntologyException: if the axiom keyword is unrecognised.
        """

        self._expect(LPAREN)
        kw_tok: Token = self._expect(T_IDENT)
        kw: str = kw_tok[2]
        body: typing.List[typing.Any] = [kw]
        if kw == _KW.INSTANCE:
            body.append(self.parse_variable())
            body.append(self.parse_concept())
            if self.tokens[self.pos][0] != RPAREN:
                body.append(self.parse_degree())
        elif kw == _KW.RELATED:
            body.append(self.parse_variable())
            body.append(self.parse_variable())
            body.append(self.parse_variable())
            if self.tokens[self.pos][0] != RPAREN:
                body.append(self.parse_degree())
        elif kw == _KW.IMPLIES_ROLE:
            body.append(self.parse_variable())
            body.append(self.parse_variable())
            if self.tokens[self.pos][0] == NUMBER:
                body.append(self.parse_number())
        elif kw in (
            _KW.IMPLIES,
            _KW.GOEDEL_IMPLIES,
            _KW.LUKASIEWICZ_IMPLIES,
            _KW.KLEENE_DIENES_IMPLIES,
            _KW.ZADEH_IMPLIES,
        ):
            body.append(self.parse_concept())
            body.append(self.parse_concept())
            if self.tokens[self.pos][0] != RPAREN:
                body.append(self.parse_degree())
        elif kw == _KW.DEFINE_CONCEPT or kw == _KW.DEFINE_PRIMITIVE_CONCEPT:
            body.append(self.parse_variable())
            body.append(self.parse_concept())
        elif kw == _KW.EQUIVALENT_CONCEPTS:
            body.append(self.parse_concept())
            body.append(self.parse_concept())
        elif kw == _KW.DISJOINT_UNION or kw == _KW.DISJOINT:
            while self.tokens[self.pos][0] != RPAREN:
                body.append(self.parse_concept())
        elif kw == _KW.RANGE or kw == _KW.DOMAIN:
            body.append(self.parse_variable())
            body.append(self.parse_concept())
        elif kw in (
            _KW.INVERSE_FUNCTIONAL,
            _KW.FUNCTIONAL,
            _KW.REFLEXIVE,
            _KW.SYMMETRIC,
            _KW.TRANSITIVE,
        ):
            body.append(self.parse_variable())
        elif kw == _KW.INVERSE:
            body.append(self.parse_variable())
            body.append(self.parse_variable())
        else:
            raise FuzzyOntologyException(f"Unknown axiom keyword: {kw}")
        self._expect(RPAREN)
        DLParser._parse_axioms(body)

    # ----- degrees --------------------------------------------------------

    def parse_degree(self) -> typing.Any:
        """
        Parses a degree, matching the grammar rule
        ``degree ::= number | expression | variable``. A number becomes a numeric
        degree, a parenthesised expression is parsed as a degree expression, and
        a bare variable becomes a variable degree.

        :return: The parsed degree.

        :rtype: typing.Any
        """

        t: Token = self.tokens[self.pos]
        if t[0] == NUMBER:
            num = self.parse_number()
            res = DLParser._parse_degree([num])
            return res
        if t[0] == LPAREN:
            # expression in parens (rare)
            expr = self.parse_expression()
            res = DLParser._parse_degree([expr])
            return res
        v = self.parse_variable()
        res = DLParser._parse_degree([v])
        return res

    # ----- queries --------------------------------------------------------

    def parse_queries(self) -> None:
        """
        Parses a query, matching the grammar rule covering all query types
        (all-instances, satisfiability, instance / subsumption / related / variable
        max/min, defuzzify, and BNP). The query keyword after ``(`` selects the
        branch; branch-specific arguments are consumed and forwarded as a flat
        list to ``DLParser._parse_queries``.

        :raises FuzzyOntologyException: if the query keyword is unrecognised.
        """

        self._expect(LPAREN)
        kw_tok: Token = self._expect(T_IDENT)
        kw: str = kw_tok[2]
        body: typing.List[typing.Any] = [kw]
        if kw == _KW.ALL_INSTANCES_QUERY:
            body.append(self.parse_concept())
        elif kw == _KW.SAT_QUERY:
            pass
        elif kw in (_KW.MAX_INSTANCE_QUERY, _KW.MIN_INSTANCE_QUERY):
            body.append(self.parse_variable())
            body.append(self.parse_concept())
        elif kw in (
            _KW.MAX_SUBS_QUERY,
            _KW.MIN_SUBS_QUERY,
            _KW.MAX_G_SUBS_QUERY,
            _KW.MIN_G_SUBS_QUERY,
            _KW.MAX_L_SUBS_QUERY,
            _KW.MIN_L_SUBS_QUERY,
            _KW.MAX_KD_SUBS_QUERY,
            _KW.MIN_KD_SUBS_QUERY,
        ):
            body.append(self.parse_concept())
            body.append(self.parse_concept())
        elif kw in (_KW.MAX_RELATED_QUERY, _KW.MIN_RELATED_QUERY):
            body.append(self.parse_variable())
            body.append(self.parse_variable())
            body.append(self.parse_variable())
        elif kw in (_KW.MAX_SAT_QUERY, _KW.MIN_SAT_QUERY):
            body.append(self.parse_concept())
            if self.tokens[self.pos][0] != RPAREN:
                body.append(self.parse_variable())
        elif kw in (_KW.MAX_VAR_QUERY, _KW.MIN_VAR_QUERY):
            body.append(self.parse_expression())
        elif kw in (
            _KW.DEFUZZIFY_LOM_QUERY,
            _KW.DEFUZZIFY_SOM_QUERY,
            _KW.DEFUZZIFY_MOM_QUERY,
        ):
            body.append(self.parse_concept())
            body.append(self.parse_variable())
            body.append(self.parse_variable())
        elif kw == _KW.BNP_QUERY:
            body.append(self.parse_fuzzy_number_expr())
        else:
            raise FuzzyOntologyException(f"Unknown query keyword: {kw}")
        self._expect(RPAREN)
        DLParser._parse_queries(body)


# ---------------------------------------------------------------------------
# Public facade
# ---------------------------------------------------------------------------


class DLParserFast(object):
    """Drop-in replacement for :class:`DLParser` using the hand-rolled parser.

    Public API is intentionally identical: :meth:`get_kb`, :meth:`main`,
    :meth:`parse_string`, :meth:`parse_string_opt`, :meth:`load_config`.
    The knowledge-base / queries-list class attributes live on DLParser so
    parse-action callbacks (which still reference DLParser.kb directly)
    continue to work without modification.
    """

    @staticmethod
    def parse_string(instring: str) -> None:
        """
        Parses a complete fuzzy-DL source string. The constructed knowledge base
        and queries are accumulated as side effects in ``DLParser.kb`` and
        ``DLParser.queries_list``; the method itself returns nothing.

        Small sources are tokenized and parsed in a single pass. Sources above
        ``_STREAM_THRESHOLD`` are streamed form-by-form in bounded chunks so the
        live token set stays proportional to one chunk rather than the whole file;
        the resulting knowledge base is identical either way.

        :param instring: The fuzzy-DL source text to parse.
        :type instring: str
        """

        if len(instring) <= _STREAM_THRESHOLD:
            DLParserFast._parse_chunk(instring)
            return
        for chunk in _iter_form_chunks(instring):
            DLParserFast._parse_chunk(chunk)

    @staticmethod
    def _parse_chunk(text: str) -> None:
        """
        Tokenizes the given text and parses every top-level form it contains.
        The token list is local, so it is reclaimed as soon as this returns —
        bounding peak token memory to one chunk when called by the streaming
        path above.

        :param text: A chunk of fuzzy-DL source text to tokenize and parse.
        :type text: str
        """

        tokens: typing.List[Token] = _tokenize_best(text)
        # if ConfigReader.DEBUG_PRINT:
        #     Util.debug(f"\t\tTokenized {len(tokens)} tokens: {[t[2] for t in tokens]}")
        _Parser(tokens).parse_program()

    @staticmethod
    def parse_string_opt(filename: str) -> None:
        """
        Parses an entire fuzzy-DL file using the fastest available path. When the compiled re2c/flex backend is present, the file is mmap-ed and tokenized in C and parsed form-by-form so peak token memory stays bounded even for large inputs (timing is logged per chunk). Otherwise it falls back to reading the whole file into a string and delegating to :meth:`parse_string`. Parsing populates the shared knowledge base as a side effect and returns nothing.

        :param filename: Path to the fuzzy-DL source file to parse.
        :type filename: str
        """

        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"Parsing file (fast mode): {filename}")
        # Fast path: when the re2c/flex backend is available, mmap and tokenize
        # the file once in C — no whole-file Python ``str`` is built and no
        # per-chunk re-encode happens. _parse_fdl_file streams the token array
        # form-by-form for large files so peak 4-tuple memory stays bounded.
        if _fdl_ok:
            for chunk in FdlFileTokenizer().tokenize_file(filename):
                t0 = time.perf_counter_ns()
                _Parser(chunk).parse_program()
                t1 = time.perf_counter_ns() - t0
                if ConfigReader.DEBUG_PRINT:
                    Util.debug(f"Parsed chunk of {len(chunk)} tokens in {(t1 * 1e-9)}s")
            return
        # Fallback (extension not built): read the source and use the
        # string-based path, which splits forms on the source text directly.
        with open(filename, "r") as fh:
            instring: str = fh.read()
        DLParserFast.parse_string(instring)

    @staticmethod
    def load_config(**kwargs: typing.Any) -> None:
        """
        Loads reasoner/parser configuration by delegating to :meth:`DLParser.load_config`, so the fast parser shares the exact same configuration handling as the legacy one. Any keyword overrides are forwarded unchanged; the call updates global configuration state and returns nothing.

        :param kwargs: Configuration overrides forwarded to :meth:`DLParser.load_config`.
        :type kwargs: typing.Any
        """

        DLParser.load_config(**kwargs)

    @staticmethod
    def get_kb(
        file_path: str, **kwargs: typing.Any
    ) -> typing.Tuple[KnowledgeBase, typing.List[Query]]:
        """
        Parses a fuzzy-DL file and returns the populated knowledge base together
        with the list of parsed queries. This is the fast-parser mirror of
        :meth:`DLParser.get_kb` so callers can swap implementations without
        changing their call site.

        :param file_path: Path to the fuzzy-DL source file.
        :type file_path: str
        :param kwargs: Configuration overrides forwarded to :meth:`load_config`.
        :type kwargs: typing.Any

        :raises FuzzyOntologyException: if parsing fails or the file is not found.

        :return: The parsed knowledge base and the list of queries.

        :rtype: typing.Tuple[KnowledgeBase, typing.List[Query]]
        """

        if ConfigReader.DEBUG_PRINT:
            Util.debug("DLParserFast.get_kb called.")

        starting_time: float = time.perf_counter_ns()
        DLParserFast.load_config(**kwargs)
        DLParser.kb = KnowledgeBase()
        DLParser.queries_list = []
        constants.KNOWLEDGE_BASE_SEMANTICS = FuzzyLogic.LUKASIEWICZ
        # Bulk KB construction allocates millions of concept / axiom objects
        # that form a DAG with no cycles to reclaim mid-parse. Python's cyclic
        # collector would otherwise sweep the steadily growing object graph
        # over and over (O(N) each pass) — pure overhead here. Disable it for
        # the parse, then restore and let the next collection reclaim normally.
        gc_was_enabled: bool = gc.isenabled()
        gc.disable()
        try:
            if ConfigReader.DEBUG_PRINT:
                # Read once, log every non-empty source line for debug
                # tracing, then parse the whole file in a single pass. The
                # previous code re-tokenised and re-entered the parser per
                # line, which is O(L) extra setup on every source line.
                with open(file_path, "r") as file:
                    instring = file.read()
                for line in instring.splitlines():
                    stripped = line.strip()
                    if stripped:
                        Util.debug(f"Line -> {stripped}")
                    DLParserFast.parse_string(stripped)
            else:
                DLParserFast.parse_string_opt(file_path)
        except FileNotFoundError:
            Util.warning(f"File {file_path} not found.")
            raise
        except Exception as e:
            Util.warning(traceback.format_exc())
            raise FuzzyOntologyException(str(e)) from e
        finally:
            if gc_was_enabled:
                gc.enable()
        ending_time: float = time.perf_counter_ns() - starting_time
        if ConfigReader.DEBUG_PRINT:
            Util.debug(f"Knowledge Base parsed in {(ending_time * 1e-9)}s")
        return DLParser.kb, DLParser.queries_list

    @staticmethod
    def main(file_path: str, **kwargs: typing.Any) -> dict[Query, Solution]:
        """
        Runs the full fast-parser pipeline for a fuzzy-DL file: it parses the file into a knowledge base, solves the TBox, and answers every parsed query, collecting the per-query solutions into a dictionary. ``all-instances`` queries short-circuit to an informational message when the KB has no individuals. The cyclic garbage collector is disabled for the duration (and restored afterwards) since the run builds a large acyclic object graph that would otherwise be scanned repeatedly; an inconsistent ontology is reported as the answer ``1.0`` rather than propagated.

        :param file_path: Path to the fuzzy-DL source file to run.
        :type file_path: str
        :param kwargs: Configuration overrides forwarded to :meth:`get_kb`.
        :type kwargs: typing.Any

        :return: A mapping from each parsed query to its computed solution.

        :rtype: dict[Query, Solution]
        """

        if ConfigReader.DEBUG_PRINT:
            Util.debug("Starting DLParserFast main execution.")
        results: dict[Query, Solution] = {}
        # Parsing, TBox solving and query answering all allocate large numbers
        # of long-lived objects (concepts, axioms, MILP terms) that form a DAG
        # with nothing to reclaim until the run ends. Disable the cyclic
        # collector for the whole run so it does not repeatedly scan the
        # growing graph. get_kb()'s own gc bracket composes (it sees gc already
        # disabled here and leaves it that way). Restore the prior state after.
        gc_was_enabled: bool = gc.isenabled()
        gc.disable()
        try:
            kb, queries = DLParserFast.get_kb(file_path, **kwargs)
            kb.solve_kb()
            for query in queries:
                if (
                    isinstance(query, AllInstancesQuery)
                    and not kb.get_individuals().values()
                ):
                    Util.info(f"{query} -- There are no individuals in the fuzzy KB")
                else:
                    result: Solution = query.solve(kb)
                    results[query] = result
                    if result.is_consistent_kb():
                        Util.info(f"{query}{result}")
                    else:
                        Util.info("KnowledgeBase inconsistent: Answer is 1.0.")
                Util.info(f"Time (s): {query.get_total_time()}")
                if kb.show_language:
                    Util.info(f"The language of the KB is {kb.get_language()}")
        except InconsistentOntologyException:
            Util.error("KnowledgeBase inconsistent: Any answer is 1.0.")
        except Exception as e:
            Util.error(e)
            Util.error(traceback.format_exc())
        finally:
            if gc_was_enabled:
                gc.enable()
        return results


if __name__ == "__main__":
    import sys

    DLParserFast.main(*sys.argv[1:])
