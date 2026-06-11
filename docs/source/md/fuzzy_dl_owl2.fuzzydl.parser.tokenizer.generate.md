# Summary

A code generation utility that synchronizes token definitions and lexer source files for the FuzzyDL parser from a central list of keywords.

## Description

Acting as the single source of truth for the parser infrastructure, this utility ensures that token definitions remain synchronized across C and Python environments. It dynamically loads the `FuzzyDLKeyword` enumeration from a separate constants module to derive the canonical list of language keywords and their string representations. By centralizing this data, the system prevents inconsistencies that often arise when maintaining separate token tables for different compiler components.

The generator constructs a comprehensive mapping of token names to integer codes, distinguishing between structural punctuation, meta tokens, and language-specific keywords. It produces a C header file containing an enum definition, a Python module exposing token constants, and a lexer specification compatible with either re2c or flex depending on the runtime arguments. During the generation of the Python module, the process preserves any hand-written logic by splitting the existing file content and appending it to the newly generated header.

To ensure correct lexical analysis, the generated lexer rules sort keywords by descending literal length so that longer identifiers are not shadowed by shorter prefixes. Additionally, the output sanitizes C identifiers by prefixing keyword names to avoid conflicts with system macros defined in standard headers. The resulting artifacts are written directly to the filesystem, providing a build-time step that automates the maintenance of the parser's low-level scanning and tokenization logic.
