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

A high-performance tokenization subsystem for the FuzzyDL language that bridges Python and C environments through automated code generation and flexible backend selection.


Description
-----------


The architecture employs a strategy pattern to prioritize compiled C extensions for speed while falling back to pure Python implementations, ensuring efficient lexical analysis across different runtime environments. By utilizing **C Foreign Function Interface (CFFI)** and memory mapping, the system delegates heavy scanning tasks to low-level C functions while managing data structures within Python to handle large inputs without excessive memory consumption. Build-time utilities synchronize token definitions across C headers and Python modules, maintaining consistency between the parser infrastructure and the specific syntax requirements of fuzzy-DL. A two-pass tokenization strategy further optimizes performance by pre-allocating exact-sized arrays, while specialized logic handles compound identifiers and numeric literals to support the language's unique grammar.


Modules
-------


* [``fuzzy_dl_owl2.fuzzydl.parser.tokenizer.generate``] — A code generation utility that synchronizes token definitions and lexer source files for the FuzzyDL parser from a central list of keywords.
* [``fuzzy_dl_owl2.fuzzydl.parser.tokenizer.tokenizer_handler``] — Manages a registry of tokenizer backends for the fuzzy-DL parser, providing a unified interface that abstracts over pure-Python and compiled C implementations.
* [``fuzzy_dl_owl2.fuzzydl.parser.tokenizer.tokens``] — A high-performance tokenizer for the FuzzyDL language that bridges Python and a C-based lexer using CFFI and memory mapping.

.. ── LLM-GENERATED DESCRIPTION END ──

Submodules
----------

.. toctree::
   :maxdepth: 1

   /api/fuzzy_dl_owl2/fuzzydl/parser/tokenizer/generate/index
   /api/fuzzy_dl_owl2/fuzzydl/parser/tokenizer/tokenizer_handler/index
   /api/fuzzy_dl_owl2/fuzzydl/parser/tokenizer/tokens/index

