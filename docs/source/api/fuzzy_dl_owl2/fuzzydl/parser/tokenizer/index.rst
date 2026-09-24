fuzzy_dl_owl2.fuzzydl.parser.tokenizer
======================================

.. only:: html

    .. figure:: /_uml/module_fuzzy_dl_owl2_fuzzydl_parser_tokenizer.png
       :alt: UML Class Diagram for fuzzy_dl_owl2.fuzzydl.parser.tokenizer
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **fuzzy_dl_owl2.fuzzydl.parser.tokenizer**

.. only:: latex

    .. raw:: latex

       \begin{landscape}

       \vspace*{\fill}

    .. figure:: /_uml/module_fuzzy_dl_owl2_fuzzydl_parser_tokenizer.pdf
       :alt: UML Class Diagram for fuzzy_dl_owl2.fuzzydl.parser.tokenizer
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **fuzzy_dl_owl2.fuzzydl.parser.tokenizer**

    .. raw:: latex

       \vspace*{\fill}

       \end{landscape}

.. py:module:: fuzzy_dl_owl2.fuzzydl.parser.tokenizer

.. autoapi-nested-parse::

   Tokenizer subpackage: token tables, the re2c/flex lexer and tokenizer backends.

   Holds the generated token codes (``tokens``), the C-lexer CFFI/Cython
   extensions (``_fdl_lexer`` / ``_fdl_tuples``), the tokenizer registry
   (``tokenizer_handler``) and the generator that produces them all
   (``generate_tokens``).

   Kept import-light on purpose: importing this package must not pull in the
   compiled lexer, so ``generate_tokens`` can run at build time before the
   extensions exist.








.. ── LLM-GENERATED DESCRIPTION START ──

The tokenization stage of the fuzzy description-logic (FDL) parser, turning source files and in-memory text into flat token streams through interchangeable pure-Python and compiled C scanning backends whose shared vocabulary is kept in sync by a build-time code generator.


Description
-----------


Tokenizing the fuzzy description-logic input language is organised around a single source of truth: a master keyword enum from which a build-time generator derives every artifact — the C token-code header, the Python token-name table, and the re2c or flex scanner source — so the Python, C, and scanner definitions of the vocabulary can never drift apart. The generator assigns deterministic numeric token codes (fixed low codes for punctuation and meta tokens, keywords numbered in declaration order, and a trailing end-of-file sentinel), emits keyword rules longest-literal-first so a short keyword can never shadow a longer one sharing its prefix, and prefixes C identifiers with ``KW_`` to avoid colliding with system macros. At runtime, a registry-based handler instantiates candidate scanning backends in preference order and adopts the first one that reports itself available: compiled re2c/flex scanners loaded through CFFI or Cython are used when the extensions have been built, while a pure-Python regex tokenizer — which can never fail to import — silently takes over otherwise, giving graceful degradation with no import-time risk. Every backend, native or pure-Python, honours the same normalised output contract of ``(kind, value, lower/raw, offset)`` tuples terminated by an end-of-file sentinel, which frees the recursive-descent parser from knowing or caring which scanner actually ran.

Performance and memory behaviour are central to the design. The compiled path scans a NUL-terminated buffer in two passes — a first C call merely counts tokens so three parallel int32 arrays (type codes, byte start offsets, and byte lengths) can be allocated to the exact size, and a second call fills them — keeping the hot path free of per-token Python objects; the resulting stream retains ownership of the source buffer, decodes token text lazily and only on request, and answers keyword or identifier queries with pure integer comparisons. Files are opened read-only and memory-mapped, exploiting the fact that mmap zero-fills the final partial page to obtain the NUL sentinel the re2c backend requires essentially for free, while an in-memory counterpart wraps already-resident bytes with an appended NUL so whole-file and chunk-oriented entry points share all of their logic. For large inputs the file-oriented backend streams rather than materialising everything at once: sources beyond a roughly one-megabyte threshold are partitioned into batches that end on whole top-level parenthesised forms — with depth counting that correctly ignores strings and comments — so peak memory stays bounded and the parser never receives a partially scanned form.

Lexically, whitespace, commas, and ``#``/``%`` line comments are skipped; parentheses, braces, and brackets are classified; quoted strings are treated as identifier-like tokens; and numeric literals are converted into ``int`` or ``float`` values. Identifiers that embed the ``*`` and ``+`` characters are split into separate operator and operand tokens unless they match a protected fuzzy-DL keyword, and keyword codes are folded into identifier tokens carrying their lowercase spelling so downstream matching stays case-insensitive. The vocabulary itself spans punctuation, arithmetic and comparison operators, numbers, bare identifiers, and an extensive keyword set covering fuzzy logic families such as *lukasiewicz* and *zadeh*, concept and role declarations, quantifiers, weighted aggregation operators like OWA, Choquet and Sugeno, and the various satisfiability and instance queries.


Modules
-------


* [``fuzzy_dl_owl2.fuzzydl.parser.tokenizer.generate``] — A build-time code generator that regenerates the parser's token tables and lexer sources — ``tokens.h``, ``tokens.py``, and either the re2c or flex scanner — from one master keyword list so the Python, C, and scanner definitions can never drift out of sync.
* [``fuzzy_dl_owl2.fuzzydl.parser.tokenizer.tokenizer_handler``] — A pluggable tokenization layer for the fuzzy-DL parser that wraps interchangeable scanning backends — an always-available pure-Python regex tokenizer plus optional compiled re2c/flex string and file scanners — behind a registry that automatically selects the fastest usable one.
* [``fuzzy_dl_owl2.fuzzydl.parser.tokenizer.tokens``] — A tokenizer for the fuzzy description-logic (FDL) input language that drives a compiled C scanner through CFFI and returns flat, NumPy-backed token streams built from either memory-mapped files or in-memory byte strings.

.. ── LLM-GENERATED DESCRIPTION END ──

Submodules
----------

.. toctree::
   :maxdepth: 1

   /api/fuzzy_dl_owl2/fuzzydl/parser/tokenizer/generate/index
   /api/fuzzy_dl_owl2/fuzzydl/parser/tokenizer/tokenizer_handler/index
   /api/fuzzy_dl_owl2/fuzzydl/parser/tokenizer/tokens/index