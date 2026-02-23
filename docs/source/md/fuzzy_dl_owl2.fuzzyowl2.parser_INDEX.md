# Summary

Parsing utilities interpret Fuzzy OWL 2 logic definitions provided in either a custom annotation syntax or standard XML format, transforming them into a structured object model suitable for reasoning.

## Description

One implementation leverages the pyparsing library to construct a grammar capable of handling complex fuzzy operators, left-recursive concept definitions, and specific datatype functions, ultimately converting token streams into KnowledgeBase and Query instances. A parallel implementation utilizes the ElementTree standard library to map XML tags and attributes to corresponding Python classes, dispatching logic based on element types to build hierarchical representations of fuzzy concepts and modifiers. Both approaches integrate configuration loading and robust error handling to ensure the parsing environment is correctly initialized and resilient against malformed input or file access issues.

## Modules

- [`fuzzyowl2.parser.owl2_parser`](./fuzzyowl2_parser_owl2_parser.md) — A parser implementation that interprets Fuzzy OWL 2 annotation strings and transforms them into structured KnowledgeBase and Query objects using the pyparsing library.
- [`fuzzyowl2.parser.owl2_xml_parser`](./fuzzyowl2_parser_owl2_xml_parser.md) — Converts FuzzyOWL2 XML annotations into Python objects representing fuzzy logic concepts, datatypes, and modifiers.
