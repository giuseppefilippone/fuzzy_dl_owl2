#!/usr/bin/env python3
"""Single source of truth for all token / keyword tables in the parser.

Regenerates tokens.h, tokens.py, lexer_re2c.re and lexer_flex.l from one
master list so keywords are never out of sync again.

Usage:
    python generate.py
"""

from __future__ import annotations

import importlib.util
import pathlib

HERE = pathlib.Path(__file__).resolve().parent


def _load_fuzzy_dl_keyword():
    """
    Loads ``FuzzyDLKeyword`` straight from constants.py by file path.

    This generator runs as a standalone script during the build (build.py),
    before the compiled ``_fdl_lexer`` extension exists.  A normal package
    import would drag in ``fuzzy_dl_owl2.fuzzydl.parser.__init__`` →
    ``tokenizer.tokens`` → ``import _fdl_lexer`` and crash.  constants.py only
    depends on the stdlib + pyparsing, so loading it in isolation avoids the
    package __init__ chain entirely while keeping the keyword table as the
    single source of truth.

    :return: The ``FuzzyDLKeyword`` enum class loaded in isolation from constants.py.

    :rtype: type
    """
    # HERE is parser/tokenizer/; constants.py lives in fuzzydl/util/.
    constants_path = HERE.parent.parent / "util" / "constants.py"
    spec = importlib.util.spec_from_file_location("_gentok_constants", constants_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.FuzzyDLKeyword


FuzzyDLKeyword = _load_fuzzy_dl_keyword()


# Token codes as a {name: code} mapping.
#
# Keys are the `FuzzyDLKeyword` enum member names (so a token name always
# matches its source of truth in constants.py).  Special tokens that have no
# `FuzzyDLKeyword` counterpart (parentheses, brackets, comma and the meta
# NUMBER / IDENT / ERROR tokens) keep their historical `T_` names and come
# first, numbered 1..k.
#
# The `FuzzyDLKeyword`-derived codes that follow are numbered in
# `FuzzyDLKeyword` declaration order — this renumbers everything and therefore
# desyncs the generated C lexer until it is regenerated from this table.
PARSER_TOKENS: dict[str, int] = {
    # special tokens without a FuzzyDLKeyword counterpart
    "T_LPAREN": 1,
    "T_RPAREN": 2,
    "T_LBRACK": 3,
    "T_RBRACK": 4,
    "T_LBRACE": 5,
    "T_RBRACE": 6,
    "T_COMMA": 7,
    "T_NUMBER": 8,
    "T_IDENT": 9,
    "T_ERROR": 10,
    # codes derived from FuzzyDLKeyword, in FuzzyDLKeyword declaration order
    **{kw.name: 11 + i for i, kw in enumerate(FuzzyDLKeyword)},
    "T_EOF": len(FuzzyDLKeyword) + 11,  # safe sentinel
}


# ---------------------------------------------------------------------------
# Master data
# ---------------------------------------------------------------------------

# Literals for the few structural tokens that have NO FuzzyDLKeyword
# counterpart (brackets, comma, the bare slash).  Every other token's literal
# is fetched from FuzzyDLKeyword.<name>.get_name() via `token_literal()`.
_NON_KEYWORD_LITERALS: dict[str, str] = {
    "T_LPAREN": "(",
    "T_RPAREN": ")",
    "T_LBRACK": "[",
    "T_RBRACK": "]",
    "T_LBRACE": "{",
    "T_RBRACE": "}",
    "T_COMMA": ",",
}


def token_literal(name: str) -> str:
    """
    Returns the literal string that a token name matches in source.

    For a token whose name is a :class:`FuzzyDLKeyword` member this returns
    ``FuzzyDLKeyword[name].get_name()`` (single source of truth in
    ``constants.py``); for the bracket / comma tokens it returns the
    hard-coded literal from :data:`_NON_KEYWORD_LITERALS`.

    :param name: The token name to look up.
    :type name: str

    :return: The source-text literal matched by this token.

    :rtype: str
    """

    if name in _NON_KEYWORD_LITERALS:
        return _NON_KEYWORD_LITERALS[name]
    return FuzzyDLKeyword[name].get_name()


# Structural punctuation / operators that have an explicit literal rule.
# (token name, Python display name).  The token name is a FuzzyDLKeyword member
# name wherever one exists (so the literal comes from constants.py via
# token_literal()); the brackets, comma and bare slash keep their `T_` names.
STRUCTURAL = [
    ("T_LPAREN", "LPAREN"),
    ("T_RPAREN", "RPAREN"),
    ("T_LBRACK", "LBRACK"),
    ("T_RBRACK", "RBRACK"),
    ("T_LBRACE", "LBRACE"),
    ("T_RBRACE", "RBRACE"),
    ("T_COMMA", "COMMA"),
    (FuzzyDLKeyword.GREATER_THAN_OR_EQUAL_TO.name, "GE"),
    (FuzzyDLKeyword.LESS_THAN_OR_EQUAL_TO.name, "LE"),
    (FuzzyDLKeyword.EQUALS.name, "EQ"),
    (FuzzyDLKeyword.FEATURE_SUM.name, "FADD"),
    (FuzzyDLKeyword.FEATURE_SUB.name, "FSUB"),
    (FuzzyDLKeyword.FEATURE_MUL.name, "FMUL"),
    (FuzzyDLKeyword.FEATURE_DIV.name, "FDIV"),
    (FuzzyDLKeyword.SUM.name, "PLUS"),
    (FuzzyDLKeyword.SUB.name, "MINUS"),
    (FuzzyDLKeyword.MUL.name, "STAR"),
]

# Meta tokens without explicit literal rules (just enum entries).
META = [
    ("T_NUMBER", "NUMBER"),
    ("T_IDENT", "IDENT"),
    ("T_ERROR", "ERROR"),
]

# Keywords as FuzzyDLKeyword member names.  Literals are fetched from
# FuzzyDLKeyword via token_literal() (e.g. "define-fuzzy-logic" lives only in
# constants.py).  Order here fixes the relative lexer ordering only; the token
# CODE numbers come from PARSER_TOKENS (FuzzyDLKeyword order).  Do NOT reorder.
KEYWORDS = [
    FuzzyDLKeyword.DEFINE_FUZZY_LOGIC.name,
    FuzzyDLKeyword.LUKASIEWICZ.name,
    FuzzyDLKeyword.ZADEH.name,
    FuzzyDLKeyword.CLASSICAL.name,
    FuzzyDLKeyword.DEFINE_TRUTH_CONSTANT.name,
    FuzzyDLKeyword.DEFINE_MODIFIER.name,
    FuzzyDLKeyword.LINEAR_MODIFIER.name,
    FuzzyDLKeyword.TRIANGULAR_MODIFIER.name,
    FuzzyDLKeyword.DEFINE_FUZZY_CONCEPT.name,
    FuzzyDLKeyword.CRISP.name,
    FuzzyDLKeyword.LEFT_SHOULDER.name,
    FuzzyDLKeyword.RIGHT_SHOULDER.name,
    FuzzyDLKeyword.TRIANGULAR.name,
    FuzzyDLKeyword.TRAPEZOIDAL.name,
    FuzzyDLKeyword.LINEAR.name,
    FuzzyDLKeyword.MODIFIED.name,
    FuzzyDLKeyword.DEFINE_FUZZY_NUMBER_RANGE.name,
    FuzzyDLKeyword.DEFINE_FUZZY_NUMBER.name,
    FuzzyDLKeyword.RANGE.name,
    FuzzyDLKeyword.INTEGER.name,
    FuzzyDLKeyword.REAL.name,
    FuzzyDLKeyword.STRING.name,
    FuzzyDLKeyword.BOOLEAN.name,
    FuzzyDLKeyword.CONSTRAINTS.name,
    FuzzyDLKeyword.BINARY.name,
    FuzzyDLKeyword.FREE.name,
    FuzzyDLKeyword.SHOW_CONCRETE_FILLERS_FOR.name,
    FuzzyDLKeyword.SHOW_CONCRETE_FILLERS.name,
    FuzzyDLKeyword.SHOW_CONCRETE_INSTANCE_FOR.name,
    FuzzyDLKeyword.SHOW_ABSTRACT_FILLERS_FOR.name,
    FuzzyDLKeyword.SHOW_ABSTRACT_FILLERS.name,
    FuzzyDLKeyword.SHOW_CONCEPTS.name,
    FuzzyDLKeyword.SHOW_INSTANCES.name,
    FuzzyDLKeyword.SHOW_VARIABLES.name,
    FuzzyDLKeyword.SHOW_LANGUAGE.name,
    FuzzyDLKeyword.CRISP_CONCEPT.name,
    FuzzyDLKeyword.CRISP_ROLE.name,
    FuzzyDLKeyword.DEFINE_FUZZY_SIMILARITY.name,
    FuzzyDLKeyword.DEFINE_FUZZY_EQUIVALENCE.name,
    FuzzyDLKeyword.TOP.name,
    FuzzyDLKeyword.BOTTOM.name,
    FuzzyDLKeyword.GOEDEL_AND.name,
    FuzzyDLKeyword.LUKASIEWICZ_AND.name,
    FuzzyDLKeyword.AND.name,
    FuzzyDLKeyword.GOEDEL_OR.name,
    FuzzyDLKeyword.LUKASIEWICZ_OR.name,
    FuzzyDLKeyword.OR.name,
    FuzzyDLKeyword.NOT.name,
    FuzzyDLKeyword.GOEDEL_IMPLIES.name,
    FuzzyDLKeyword.LUKASIEWICZ_IMPLIES.name,
    FuzzyDLKeyword.KLEENE_DIENES_IMPLIES.name,
    FuzzyDLKeyword.ZADEH_IMPLIES.name,
    FuzzyDLKeyword.IMPLIES_ROLE.name,
    FuzzyDLKeyword.IMPLIES.name,
    FuzzyDLKeyword.ALL.name,
    FuzzyDLKeyword.HAS_VALUE.name,
    FuzzyDLKeyword.SOME.name,
    FuzzyDLKeyword.LOOSE_UPPER_APPROXIMATION.name,
    FuzzyDLKeyword.TIGHT_UPPER_APPROXIMATION.name,
    FuzzyDLKeyword.UPPER_APPROXIMATION.name,
    FuzzyDLKeyword.LOOSE_LOWER_APPROXIMATION.name,
    FuzzyDLKeyword.TIGHT_LOWER_APPROXIMATION.name,
    FuzzyDLKeyword.LOWER_APPROXIMATION.name,
    FuzzyDLKeyword.SELF.name,
    FuzzyDLKeyword.W_SUM_ZERO.name,
    FuzzyDLKeyword.W_SUM.name,
    FuzzyDLKeyword.W_MAX.name,
    FuzzyDLKeyword.W_MIN.name,
    FuzzyDLKeyword.Q_OWA.name,
    FuzzyDLKeyword.OWA.name,
    FuzzyDLKeyword.CHOQUET.name,
    FuzzyDLKeyword.QUASI_SUGENO.name,
    FuzzyDLKeyword.SUGENO.name,
    FuzzyDLKeyword.SIGMA_COUNT.name,
    FuzzyDLKeyword.DEFINE_CONCEPT.name,
    FuzzyDLKeyword.DEFINE_PRIMITIVE_CONCEPT.name,
    FuzzyDLKeyword.EQUIVALENT_CONCEPTS.name,
    FuzzyDLKeyword.DISJOINT_UNION.name,
    FuzzyDLKeyword.DISJOINT.name,
    FuzzyDLKeyword.DOMAIN.name,
    FuzzyDLKeyword.INVERSE_FUNCTIONAL.name,
    FuzzyDLKeyword.FUNCTIONAL.name,
    FuzzyDLKeyword.REFLEXIVE.name,
    FuzzyDLKeyword.SYMMETRIC.name,
    FuzzyDLKeyword.TRANSITIVE.name,
    FuzzyDLKeyword.INVERSE.name,
    FuzzyDLKeyword.MAX_INSTANCE_QUERY.name,
    FuzzyDLKeyword.MIN_INSTANCE_QUERY.name,
    FuzzyDLKeyword.ALL_INSTANCES_QUERY.name,
    FuzzyDLKeyword.MAX_RELATED_QUERY.name,
    FuzzyDLKeyword.MIN_RELATED_QUERY.name,
    FuzzyDLKeyword.INSTANCE.name,
    FuzzyDLKeyword.RELATED.name,
    FuzzyDLKeyword.MAX_SUBS_QUERY.name,
    FuzzyDLKeyword.MIN_SUBS_QUERY.name,
    FuzzyDLKeyword.MAX_G_SUBS_QUERY.name,
    FuzzyDLKeyword.MIN_G_SUBS_QUERY.name,
    FuzzyDLKeyword.MAX_L_SUBS_QUERY.name,
    FuzzyDLKeyword.MIN_L_SUBS_QUERY.name,
    FuzzyDLKeyword.MAX_KD_SUBS_QUERY.name,
    FuzzyDLKeyword.MIN_KD_SUBS_QUERY.name,
    FuzzyDLKeyword.MAX_SAT_QUERY.name,
    FuzzyDLKeyword.MIN_SAT_QUERY.name,
    FuzzyDLKeyword.MAX_VAR_QUERY.name,
    FuzzyDLKeyword.MIN_VAR_QUERY.name,
    FuzzyDLKeyword.DEFUZZIFY_LOM_QUERY.name,
    FuzzyDLKeyword.DEFUZZIFY_MOM_QUERY.name,
    FuzzyDLKeyword.DEFUZZIFY_SOM_QUERY.name,
    FuzzyDLKeyword.BNP_QUERY.name,
    FuzzyDLKeyword.SAT_QUERY.name,
]

# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------


def _pad(lit: str, width: int) -> str:
    """
    Right-pads a quoted literal with spaces so columns line up in generated
    scanner source code.

    :param lit: The literal string to pad.
    :type lit: str
    :param width: The target column width.
    :type width: int

    :return: The quoted and padded literal.

    :rtype: str
    """

    q = f'"{lit}"'
    return q + " " * max(0, width - len(q))


def _max_lit_width(names) -> int:
    """
    Returns the width of the widest quoted literal across a sequence of token
    names, used to align columns in generated scanner source code.

    :param names: Sequence of token names to measure.
    :type names: typing.Iterable[str]

    :return: The maximum quoted-literal width.

    :rtype: int
    """

    return max(len(f'"{token_literal(name)}"') for name in names)


def _structural_names():
    """
    Returns the token names of the STRUCTURAL entries, dropping the Python display name.

    :return: The token names of every STRUCTURAL entry.

    :rtype: list[str]
    """
    return [name for name, _ in STRUCTURAL]


def _c_name(name: str) -> str:
    """
    Returns the C enum identifier for a token name.

    The bare :class:`FuzzyDLKeyword` names collide with system macros in C
    (e.g. ``DOMAIN`` is defined by ``<math.h>``), so every keyword / operator
    identifier is prefixed with ``KW_`` in the generated C.  The ``T_*``
    special tokens already have a safe prefix and are emitted unchanged —
    ``_fdl_tuples.pyx`` refers to them by those exact names.

    :param name: The token name to translate.
    :type name: str

    :return: The safe C enum identifier.

    :rtype: str
    """

    return name if name.startswith("T_") else f"KW_{name}"


def _lexer_keywords():
    """
    Returns the keyword names sorted by literal longest-first so a prefix never
    shadows a longer keyword (e.g. 'w-sum-zero' before 'w-sum', 'g-and' before
    'and').

    :return: The keyword names ordered by descending literal length, then name.

    :rtype: list[str]
    """
    return sorted(KEYWORDS, key=lambda name: (-len(token_literal(name)), name))


# ---------------------------------------------------------------------------
# generators
# ---------------------------------------------------------------------------


def gen_tokens_h() -> str:
    """
    Renders the C header ``tokens.h`` from the master :data:`PARSER_TOKENS` table. Every token code is emitted as an ``enum`` member in lock-step with the Python table (specials first, then ``FuzzyDLKeyword`` order, then the ``T_EOF`` sentinel), with keyword identifiers ``KW_``-prefixed via :func:`_c_name` to dodge system-macro collisions. The result is returned as a string rather than written to disk.

    :return: The full text of the generated ``tokens.h`` header.

    :rtype: str
    """

    lines = [
        "/* fuzzyDL token codes. Auto-generated by generate.py.",
        " * Do NOT edit by hand — change the master list in generate.py",
        " * and re-run it instead. */",
        "#ifndef FDL_TOKENS_H",
        "#define FDL_TOKENS_H",
        "",
        "enum {",
    ]
    # Emit the whole PARSER_TOKENS table (specials first, then FuzzyDLKeyword
    # order, then the T_EOF sentinel) so the C enum stays in lock-step with the
    # Python table.  Keyword identifiers are KW_-prefixed via _c_name() to dodge
    # system macro collisions (e.g. DOMAIN in <math.h>).
    for name, code in PARSER_TOKENS.items():
        lines.append(f"    {_c_name(name)} = {code},")
    lines.append("};")
    lines.append("")
    lines.append("#endif /* FDL_TOKENS_H */")
    lines.append("")
    return "\n".join(lines)


def gen_tokens_py() -> str:
    """
    Renders the Python module ``tokens.py`` from the master tables. The generated header defines the ``TOK_NAMES`` code-to-display-name mapping plus the exported token-code constants (``NUMBER``, ``IDENT``, ``ERROR``, ``FIRST_KEYWORD``, the structural names, ``T_IDENT``, ``T_EOF``). The remainder of the module — the ``_Buffer`` / ``_BytesBuffer`` / ``Tokens`` classes and the tokenize helpers — is copied verbatim from the existing ``tokens.py`` (everything after the ``_PAGE = mmap.PAGESIZE`` marker), so hand-written edits to those classes are preserved across regeneration. The result is returned as a string rather than written to disk.

    :return: The full text of the generated ``tokens.py`` module.

    :rtype: str
    """

    lines = [
        "# Auto-generated by generate.py. Do NOT edit by hand.",
        "",
        "import mmap",
        "import os",
        "",
        "import numpy as np",
        "",
        "try:",
        "    from fuzzy_dl_owl2.fuzzydl.parser.tokenizer._fdl_lexer import ffi, lib",
        "except ImportError:  # pragma: no cover",
        "    try:",
        "        from _fdl_lexer import ffi, lib",
        "    except ImportError:",
        "        ffi = lib = None",
        "",
        "TOK_NAMES = {",
    ]
    # code -> display name: structural / meta use their short Python display
    # name; keywords use the matched literal (e.g. "define-fuzzy-logic").
    for name, pyname in STRUCTURAL:
        lines.append(f'    {PARSER_TOKENS[name]}: "{pyname}",')
    for name, pyname in META:
        lines.append(f'    {PARSER_TOKENS[name]}: "{pyname}",')
    for name in KEYWORDS:
        lines.append(f'    {PARSER_TOKENS[name]}: "{token_literal(name)}",')
    lines.append("}")
    lines.append("")
    lines.append(f"NUMBER = {PARSER_TOKENS['T_NUMBER']}")
    lines.append(f"IDENT = {PARSER_TOKENS['T_IDENT']}")
    lines.append(f"ERROR = {PARSER_TOKENS['T_ERROR']}")
    lines.append(f"FIRST_KEYWORD = {PARSER_TOKENS[KEYWORDS[0]]}")
    lines.append("")
    # Export scanner structural names so parser can use them directly
    for name, pyname in STRUCTURAL:
        lines.append(f"{pyname} = {PARSER_TOKENS[name]}")
    lines.append(
        f"T_IDENT = {PARSER_TOKENS['T_IDENT']}"
    )  # parser uses scanner value directly
    lines.append(f"T_EOF = {PARSER_TOKENS['T_EOF']}")  # safe sentinel
    lines.append("")
    # copy the rest of tokens.py (Buffer classes, Tokens, get_tokens) unchanged
    rest = (
        (HERE / "tokens.py")
        .read_text(encoding="utf-8")
        .split("_PAGE = mmap.PAGESIZE")[1]
    )
    lines.append("_PAGE = mmap.PAGESIZE\n")
    lines.append(rest.strip())
    return "\n".join(lines)


def gen_lexer_re2c() -> str:
    """
    Renders the re2c scanner source ``lexer_re2c.re`` from the master tables. Keyword and structural literals are emitted as re2c rules sorted longest-literal-first (so a short prefix never shadows a longer keyword), followed by the number and identifier rules and the public ``fdl_count_tokens`` / ``fdl_tokenize`` entry points. Literal columns are padded for readability via :func:`_pad`. The result is returned as a string rather than written to disk.

    :return: The full text of the generated ``lexer_re2c.re`` scanner source.

    :rtype: str
    """

    kw = _lexer_keywords()
    kw_width = _max_lit_width(kw)
    struct_width = _max_lit_width(_structural_names())
    max_width = max(kw_width, struct_width)

    lines = [
        "/* Auto-generated by generate.py. Do NOT edit by hand.",
        " * Change the master list in generate.py and re-run it. */",
        "#include <stddef.h>",
        "#include <stdint.h>",
        "",
        '#include "tokens.h"',
        "",
        "/* When `types` is NULL, count only (pass 1); otherwise fill spans (pass 2).",
        " * Scans the buffer in place; buf[len] must be a NUL sentinel. */",
        "static size_t scan(const char *buf, size_t len,",
        "                   int32_t *types, int32_t *starts, int32_t *lens)",
        "{",
        "    const unsigned char *base = (const unsigned char *)buf;",
        "    const unsigned char *cur  = base;",
        "    const unsigned char *lim  = base + len;",
        "    const unsigned char *mar;",
        "    const unsigned char *tok;",
        "    size_t n = 0;",
        "",
        "    #define EMIT(t) do { if (types) { types[n]=(t); starts[n]=(int32_t)(tok-base); \\",
        "                                      lens[n]=(int32_t)(cur-tok); } n++; } while (0)",
        "",
        "    for (;;) {",
        "        tok = cur;",
        "        /*!re2c",
        '            re2c:define:YYCTYPE  = "unsigned char";',
        "            re2c:define:YYCURSOR = cur;",
        "            re2c:define:YYLIMIT  = lim;",
        "            re2c:define:YYMARKER = mar;",
        "            re2c:yyfill:enable   = 0;",
        "            re2c:eof             = 0;",
        "",
        '            [ \\t\\r\\n\\f\\v"]+                                             { continue; }',
        '            ("#" | "%") [^\\n]*                                              { continue; }',
    ]
    for name in kw:
        lines.append(
            f"            {_pad(token_literal(name), max_width)} {{ EMIT({_c_name(name)}); continue; }}"
        )
    for name, _ in STRUCTURAL:
        lines.append(
            f"            {_pad(token_literal(name), max_width)} {{ EMIT({_c_name(name)}); continue; }}"
        )
    lines += [
        '            [+-]?[0-9]+("." [0-9]*)?([eE][+-]?[0-9]+)?                             { EMIT(T_NUMBER); continue; }',
        "            [a-zA-Z0-9_><][a-zA-Z0-9_'/.:><@$!?-]*                                 { EMIT(T_IDENT); continue; }",
        "            $                                                                      { break; }",
        "            *                                                                      { EMIT(T_ERROR); continue; }",
        "        */",
        "    }",
        "    #undef EMIT",
        "    return n;",
        "}",
        "",
    ]
    lines.append("""
size_t fdl_count_tokens(const char *buf, size_t len) { return scan(buf, len, NULL, NULL, NULL); }
size_t fdl_tokenize(const char *buf, size_t len,
                    int32_t *types, int32_t *starts, int32_t *lens) {
    return scan(buf, len, types, starts, lens);
}
    """.strip())
    return "\n".join(lines)


def gen_lexer_flex() -> str:
    """
    Renders the flex scanner source ``lexer_flex.l`` from the master tables, the flex counterpart of :func:`gen_lexer_re2c`. Keyword and structural literals are emitted as flex rules sorted longest-literal-first, followed by the number and identifier rules and the public ``fdl_count_tokens`` / ``fdl_tokenize`` entry points that drive ``yylex`` over the whole input. The result is returned as a string rather than written to disk.

    :return: The full text of the generated ``lexer_flex.l`` scanner source.

    :rtype: str
    """

    kw = _lexer_keywords()
    kw_width = _max_lit_width(kw)
    struct_width = _max_lit_width(_structural_names())
    max_width = max(kw_width, struct_width)

    lines = [
        "/* Auto-generated by generate.py. Do NOT edit by hand.",
        " * Change the master list in generate.py and re-run it. */",
        "%{",
        "#include <stddef.h>",
        "#include <stdint.h>",
        '#include "tokens.h"',
        "/* Output arrays for the current run; NULL during the counting pass. */",
        "static int32_t *g_types, *g_starts, *g_lens;",
        "static size_t g_n;   /* tokens emitted so far */",
        "static size_t g_off; /* byte offset of yytext within the input */",
        "/* Every rule must advance g_off by yyleng (EMIT or SKIP), otherwise",
        " * the recorded token spans drift from the real input offsets. */",
        "#define EMIT(t) do { \\",
        "    if (g_types) { g_types[g_n] = (t); g_starts[g_n] = (int32_t)g_off; \\",
        "                   g_lens[g_n] = (int32_t)yyleng; } \\",
        "    g_n++; g_off += (size_t)yyleng; } while (0)",
        "#define SKIP() (g_off += (size_t)yyleng)",
        "%}",
        "",
        "%option noyywrap",
        "",
        "%%",
        "",
        '[ \\t\\r\\n\\f\\v"]+                 { SKIP(); /* skip whitespace and quotes */ }',
        "(#|%).*                              { SKIP(); /* skip comments */ }",
    ]
    for name in kw:
        lines.append(
            f"{_pad(token_literal(name), max_width)} {{ EMIT({_c_name(name)}); }}"
        )
    for name, _ in STRUCTURAL:
        lines.append(
            f"{_pad(token_literal(name), max_width)} {{ EMIT({_c_name(name)}); }}"
        )
    lines += [
        '[+-]?[0-9]+("."[0-9]*)?([eE][+-]?[0-9]+)?      {{ EMIT(T_NUMBER); }}',
        "[a-zA-Z0-9_><][a-zA-Z0-9_'/.:><@$!?-]*         {{ EMIT(T_IDENT); }}",
        ".                                              {{ EMIT(T_ERROR); }}",
        "%%",
        "",
    ]
    lines.append("""
/* One yylex() call scans the whole input (no action returns until EOF). */
static size_t run(const char *buf, size_t len,
                int32_t *ty, int32_t *st, int32_t *ln) {
    g_types = ty; g_starts = st; g_lens = ln;
    g_n = 0; g_off = 0;
    YY_BUFFER_STATE b = yy_scan_bytes(buf, (int)len);  /* copies the input */
    yylex();
    yy_delete_buffer(b);
    return g_n;
}
size_t fdl_count_tokens(const char *buf, size_t len) { return run(buf, len, NULL, NULL, NULL); }
size_t fdl_tokenize(const char *buf, size_t len,
                    int32_t *types, int32_t *starts, int32_t *lens) {
    return run(buf, len, types, starts, lens);
}""".strip())
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------


def main(lexer_type: str) -> None:
    """
    Regenerates the token/lexer source files from the master tables and writes them to disk. ``tokens.h`` and ``tokens.py`` are always written; the scanner source is written for exactly one backend depending on ``lexer_type`` (``"re2c"`` emits ``lexer_re2c.re``, ``"flex"`` emits ``lexer_flex.l``). Progress and a final token-count summary are printed to stdout.

    :param lexer_type: Which lexer backend to emit, either ``"re2c"`` or ``"flex"``.
    :type lexer_type: str
    """

    print("Regenerating token files from generate.py ...")

    (HERE / "tokens.h").write_text(gen_tokens_h())
    print("  tokens.h")

    (HERE / "tokens.py").write_text(gen_tokens_py())
    print("  tokens.py")

    if lexer_type == "re2c":
        (HERE / "lexer_re2c.re").write_text(gen_lexer_re2c())
        print("  lexer_re2c.re")

    if lexer_type == "flex":
        (HERE / "lexer_flex.l").write_text(gen_lexer_flex())
        print("  lexer_flex.l")

    total = len(STRUCTURAL) + len(META) + len(KEYWORDS)
    print(
        f"\nDone. {len(KEYWORDS)} keywords + {len(STRUCTURAL)} structural + {len(META)} meta = {total} token codes."
    )


if __name__ == "__main__":
    import sys

    main(sys.argv[1] if len(sys.argv) > 1 else "re2c")
