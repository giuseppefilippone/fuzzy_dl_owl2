# Summary

A comprehensive parsing framework for Fuzzy Description Logic that transforms textual definitions into executable knowledge bases and queries through a multi-layered architecture supporting both standard and high-performance execution modes.

## Description

The software interprets textual definitions of Fuzzy Description Logic to construct a knowledge base and associated queries, bridging the gap between raw syntax and an executable object model. By employing a modular architecture, the system separates lexical analysis from semantic actions, allowing specialized components to handle tokenization, grammar definition, and the instantiation of domain-specific objects like concepts and individuals. To accommodate varying performance needs, the implementation supports multiple parsing strategies, ranging from a standard grammar-based approach using `pyparsing` to a high-performance recursive-descent parser that eliminates backtracking overhead. Furthermore, the infrastructure leverages a strategy pattern for tokenization that prioritizes compiled C extensions via CFFI for speed while maintaining a pure Python fallback, ensuring efficient processing of complex fuzzy logic ontologies.

## Modules

- [`fuzzy_dl_owl2.fuzzydl.parser.dl_parser`] — A specialized parser for Fuzzy Description Logic that interprets textual definitions to construct a knowledge base and associated queries using the pyparsing library.
- [`fuzzy_dl_owl2.fuzzydl.parser.dl_parser_clean`] — A semantic action handler that transforms parsed tokens into a Fuzzy Description Logic knowledge base and associated query objects.
- [`fuzzy_dl_owl2.fuzzydl.parser.dl_parser_fast`] — A high-performance recursive-descent parser that acts as a drop-in replacement for the legacy FuzzyDL parser by reusing semantic actions while eliminating backtracking and caching overhead.

## Sub-packages

- [`fuzzy_dl_owl2.fuzzydl.parser.tokenizer`] — A high-performance tokenization subsystem for the FuzzyDL language that bridges Python and C environments through automated code generation and flexible backend selection.
