fuzzy_dl_owl2.fuzzydl.parser
============================

.. only:: html

    .. figure:: /_uml/module_fuzzy_dl_owl2_fuzzydl_parser.png
       :alt: UML Class Diagram for fuzzy_dl_owl2.fuzzydl.parser
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **fuzzy_dl_owl2.fuzzydl.parser**

.. only:: latex

    .. figure:: /_uml/module_fuzzy_dl_owl2_fuzzydl_parser.pdf
       :alt: UML Class Diagram for fuzzy_dl_owl2.fuzzydl.parser
       :align: center
       :width: 14.1cm
       :class: uml-diagram

       UML Class Diagram for **fuzzy_dl_owl2.fuzzydl.parser**

.. py:module:: fuzzy_dl_owl2.fuzzydl.parser





.. ── LLM-GENERATED DESCRIPTION START ──

A parsing front end for the fuzzy description-logic (FDL) language that reads textual knowledge base files and produces a fully populated knowledge base together with the list of queries to be answered against it, using interchangeable parser and tokenizer implementations that range from a pure-Python pyparsing grammar to compiled C scanners.


Description
-----------


Parsing is organised as a layered pipeline in which tokenization, grammar recognition, and semantic interpretation are cleanly separated. At the front, a pluggable tokenization layer turns source text into flat token streams, automatically adopting the fastest available scanning backend — a compiled re2c/flex scanner driven through CFFI or Cython when the extensions have been built, or an always-importable pure-Python regex tokenizer otherwise — while a build-time code generator derives the Python, C, and scanner definitions of the keyword vocabulary from one master list so they can never drift apart. Grammar recognition comes in two interchangeable flavours: a legacy pyparsing-based grammar and a faster hand-written recursive-descent parser that exploits the LL(1) nature of the language to commit to a grammar branch with a single token of lookahead and no backtracking. Both are drop-in replacements for one another and deliberately share the same semantic-action layer, so knowledge base construction, validation, and query registration remain a single source of truth regardless of which parser actually runs.

Semantic interpretation is side-effect driven: as statements are recognised, parse-action callbacks immediately transform the matched tokens into domain objects — fuzzy concepts of many flavours, degrees, and MILP expressions and constraints — and register them on a shared knowledge base, while query statements accumulate in a companion list for later evaluation rather than being executed at parse time. Validation is woven into the parse actions instead of being deferred to a later pass: weights in weighted aggregations and fuzzy integrals are checked for non-negativity and correct normalisation, concepts are verified to be abstract where required, and any referenced modifier, individual, feature, or fuzzy concept must be defined before use. Multiple fuzzy semantics — Łukasiewicz, Zadeh/Gödel, and classical — are supported, with the configured logic selecting the concrete operator implementation for each connective and fuzzy-specific operators rejected outright under the classical reasoner.

Performance and diagnosability are treated as first-class concerns. Large ontologies are streamed form-by-form in bounded chunks so peak memory stays proportional to a single chunk, input files are memory-mapped, and the cyclic garbage collector is deliberately disabled during bulk parsing because the constructed object graph is large and acyclic with nothing to reclaim until the end. The fast parser is written to be Cython-compilable for a native-code speedup, and even in plain Python it runs several times faster than the legacy grammar because backtracking and packrat caching are gone. Errors are surfaced through a central reporting utility, unexpected failures are wrapped in an ontology exception with the original cause chained, and debug mode traces every parse action into a timestamped diagnostic log — mirroring the behaviour of the original Java fuzzyDL reasoner whose syntax is reproduced here.


Modules
-------


* [``fuzzy_dl_owl2.fuzzydl.parser.dl_parser``] — A pyparsing-based parser for the fuzzy Description Logic language that reads textual knowledge base files and constructs a fully populated **KnowledgeBase** together with the list of queries to be answered against it.
* [``fuzzy_dl_owl2.fuzzydl.parser.dl_parser_clean``] — A pyparsing-free semantic-action layer for a fuzzy Description Logic parser that converts raw token lists into typed domain objects — fuzzy concepts, degrees, MILP expressions, and queries — while incrementally building and validating a shared fuzzy knowledge base.
* [``fuzzy_dl_owl2.fuzzydl.parser.dl_parser_fast``] — A faster drop-in replacement for the legacy fuzzy-DL parser that pairs a hand-rolled tokenizer with a deterministic recursive-descent parser to load fuzzy description-logic knowledge bases and answer queries, reusing the original parser's semantic actions so the resulting knowledge base and queries are populated exactly the same way.


Sub-packages
------------


* [``fuzzy_dl_owl2.fuzzydl.parser.tokenizer``] — The tokenization stage of the fuzzy description-logic (FDL) parser, turning source files and in-memory text into flat token streams through interchangeable pure-Python and compiled C scanning backends whose shared vocabulary is kept in sync by a build-time code generator.

.. ── LLM-GENERATED DESCRIPTION END ──

Submodules
----------

.. toctree::
   :maxdepth: 1

   /api/fuzzy_dl_owl2/fuzzydl/parser/dl_parser/index
   /api/fuzzy_dl_owl2/fuzzydl/parser/dl_parser_clean/index
   /api/fuzzy_dl_owl2/fuzzydl/parser/dl_parser_fast/index
   /api/fuzzy_dl_owl2/fuzzydl/parser/tokenizer/index
