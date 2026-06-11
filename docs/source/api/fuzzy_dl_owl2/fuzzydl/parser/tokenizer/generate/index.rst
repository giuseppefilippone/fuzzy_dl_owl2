fuzzy_dl_owl2.fuzzydl.parser.tokenizer.generate
===============================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.parser.tokenizer.generate

.. autoapi-nested-parse::

   Single source of truth for all token / keyword tables in the parser.

   Regenerates tokens.h, tokens.py, lexer_re2c.re and lexer_flex.l from one
   master list so keywords are never out of sync again.

   Usage:
       python generate.py




.. ── LLM-GENERATED DESCRIPTION START ──

A code generation utility that synchronizes token definitions and lexer source files for the FuzzyDL parser from a central list of keywords.


Description
-----------


Acting as the single source of truth for the parser infrastructure, this utility ensures that token definitions remain synchronized across C and Python environments. It dynamically loads the ``FuzzyDLKeyword`` enumeration from a separate constants module to derive the canonical list of language keywords and their string representations. By centralizing this data, the system prevents inconsistencies that often arise when maintaining separate token tables for different compiler components.

The generator constructs a comprehensive mapping of token names to integer codes, distinguishing between structural punctuation, meta tokens, and language-specific keywords. It produces a C header file containing an enum definition, a Python module exposing token constants, and a lexer specification compatible with either re2c or flex depending on the runtime arguments. During the generation of the Python module, the process preserves any hand-written logic by splitting the existing file content and appending it to the newly generated header.

To ensure correct lexical analysis, the generated lexer rules sort keywords by descending literal length so that longer identifiers are not shadowed by shorter prefixes. Additionally, the output sanitizes C identifiers by prefixing keyword names to avoid conflicts with system macros defined in standard headers. The resulting artifacts are written directly to the filesystem, providing a build-time step that automates the maintenance of the parser's low-level scanning and tokenization logic.

.. ── LLM-GENERATED DESCRIPTION END ──

Attributes
----------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.parser.tokenizer.generate.FuzzyDLKeyword
   fuzzy_dl_owl2.fuzzydl.parser.tokenizer.generate.HERE
   fuzzy_dl_owl2.fuzzydl.parser.tokenizer.generate.KEYWORDS
   fuzzy_dl_owl2.fuzzydl.parser.tokenizer.generate.META
   fuzzy_dl_owl2.fuzzydl.parser.tokenizer.generate.PARSER_TOKENS
   fuzzy_dl_owl2.fuzzydl.parser.tokenizer.generate.STRUCTURAL
   fuzzy_dl_owl2.fuzzydl.parser.tokenizer.generate._NON_KEYWORD_LITERALS


Functions
---------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.parser.tokenizer.generate._c_name
   fuzzy_dl_owl2.fuzzydl.parser.tokenizer.generate._lexer_keywords
   fuzzy_dl_owl2.fuzzydl.parser.tokenizer.generate._load_fuzzy_dl_keyword
   fuzzy_dl_owl2.fuzzydl.parser.tokenizer.generate._max_lit_width
   fuzzy_dl_owl2.fuzzydl.parser.tokenizer.generate._pad
   fuzzy_dl_owl2.fuzzydl.parser.tokenizer.generate._structural_names
   fuzzy_dl_owl2.fuzzydl.parser.tokenizer.generate.gen_lexer_flex
   fuzzy_dl_owl2.fuzzydl.parser.tokenizer.generate.gen_lexer_re2c
   fuzzy_dl_owl2.fuzzydl.parser.tokenizer.generate.gen_tokens_h
   fuzzy_dl_owl2.fuzzydl.parser.tokenizer.generate.gen_tokens_py
   fuzzy_dl_owl2.fuzzydl.parser.tokenizer.generate.main
   fuzzy_dl_owl2.fuzzydl.parser.tokenizer.generate.token_literal


Module Contents
---------------

.. py:function:: _c_name(name: str) -> str

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


.. py:function:: _lexer_keywords()

   Returns the keyword names sorted by literal longest-first so a prefix never
   shadows a longer keyword (e.g. 'w-sum-zero' before 'w-sum', 'g-and' before
   'and').

   :return: The keyword names ordered by descending literal length, then name.

   :rtype: list[str]


.. py:function:: _load_fuzzy_dl_keyword()

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


.. py:function:: _max_lit_width(names) -> int

   Returns the width of the widest quoted literal across a sequence of token
   names, used to align columns in generated scanner source code.

   :param names: Sequence of token names to measure.
   :type names: typing.Iterable[str]

   :return: The maximum quoted-literal width.

   :rtype: int


.. py:function:: _pad(lit: str, width: int) -> str

   Right-pads a quoted literal with spaces so columns line up in generated
   scanner source code.

   :param lit: The literal string to pad.
   :type lit: str
   :param width: The target column width.
   :type width: int

   :return: The quoted and padded literal.

   :rtype: str


.. py:function:: _structural_names()

   Returns the token names of the STRUCTURAL entries, dropping the Python display name.

   :return: The token names of every STRUCTURAL entry.

   :rtype: list[str]


.. py:function:: gen_lexer_flex() -> str

   Renders the flex scanner source ``lexer_flex.l`` from the master tables, the flex counterpart of :func:`gen_lexer_re2c`. Keyword and structural literals are emitted as flex rules sorted longest-literal-first, followed by the number and identifier rules and the public ``fdl_count_tokens`` / ``fdl_tokenize`` entry points that drive ``yylex`` over the whole input. The result is returned as a string rather than written to disk.

   :return: The full text of the generated ``lexer_flex.l`` scanner source.

   :rtype: str


.. py:function:: gen_lexer_re2c() -> str

   Renders the re2c scanner source ``lexer_re2c.re`` from the master tables. Keyword and structural literals are emitted as re2c rules sorted longest-literal-first (so a short prefix never shadows a longer keyword), followed by the number and identifier rules and the public ``fdl_count_tokens`` / ``fdl_tokenize`` entry points. Literal columns are padded for readability via :func:`_pad`. The result is returned as a string rather than written to disk.

   :return: The full text of the generated ``lexer_re2c.re`` scanner source.

   :rtype: str


.. py:function:: gen_tokens_h() -> str

   Renders the C header ``tokens.h`` from the master :data:`PARSER_TOKENS` table. Every token code is emitted as an ``enum`` member in lock-step with the Python table (specials first, then ``FuzzyDLKeyword`` order, then the ``T_EOF`` sentinel), with keyword identifiers ``KW_``-prefixed via :func:`_c_name` to dodge system-macro collisions. The result is returned as a string rather than written to disk.

   :return: The full text of the generated ``tokens.h`` header.

   :rtype: str


.. py:function:: gen_tokens_py() -> str

   Renders the Python module ``tokens.py`` from the master tables. The generated header defines the ``TOK_NAMES`` code-to-display-name mapping plus the exported token-code constants (``NUMBER``, ``IDENT``, ``ERROR``, ``FIRST_KEYWORD``, the structural names, ``T_IDENT``, ``T_EOF``). The remainder of the module — the ``_Buffer`` / ``_BytesBuffer`` / ``Tokens`` classes and the tokenize helpers — is copied verbatim from the existing ``tokens.py`` (everything after the ``_PAGE = mmap.PAGESIZE`` marker), so hand-written edits to those classes are preserved across regeneration. The result is returned as a string rather than written to disk.

   :return: The full text of the generated ``tokens.py`` module.

   :rtype: str


.. py:function:: main(lexer_type: str) -> None

   Regenerates the token/lexer source files from the master tables and writes them to disk. ``tokens.h`` and ``tokens.py`` are always written; the scanner source is written for exactly one backend depending on ``lexer_type`` (``"re2c"`` emits ``lexer_re2c.re``, ``"flex"`` emits ``lexer_flex.l``). Progress and a final token-count summary are printed to stdout.

   :param lexer_type: Which lexer backend to emit, either ``"re2c"`` or ``"flex"``.
   :type lexer_type: str


.. py:function:: token_literal(name: str) -> str

   Returns the literal string that a token name matches in source.

   For a token whose name is a :class:`FuzzyDLKeyword` member this returns
   ``FuzzyDLKeyword[name].get_name()`` (single source of truth in
   ``constants.py``); for the bracket / comma tokens it returns the
   hard-coded literal from :data:`_NON_KEYWORD_LITERALS`.

   :param name: The token name to look up.
   :type name: str

   :return: The source-text literal matched by this token.

   :rtype: str


.. py:data:: FuzzyDLKeyword

.. py:data:: HERE

.. py:data:: KEYWORDS

.. py:data:: META
   :value: [('T_NUMBER', 'NUMBER'), ('T_IDENT', 'IDENT'), ('T_ERROR', 'ERROR')]


.. py:data:: PARSER_TOKENS
   :type:  dict[str, int]

.. py:data:: STRUCTURAL

.. py:data:: _NON_KEYWORD_LITERALS
   :type:  dict[str, str]
