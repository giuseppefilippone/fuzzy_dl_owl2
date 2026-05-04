# Summary

Specialized parsing logic transforms Fuzzy OWL 2 XML annotations and grammar-based strings into internal knowledge bases and fuzzy logic objects.

## Description

Two distinct parsing strategies are employed to interpret fuzzy logic constructs, utilizing both the pyparsing library for grammar definition and standard XML parsing for structural analysis. These components process complex fuzzy elements, such as weighted aggregations, integral-based concepts, and specific datatypes like triangular functions, converting raw text or XML tokens into strongly typed domain objects. A central dispatch mechanism and internal callback functions orchestrate the translation flow, ensuring that nested attributes and annotation types are correctly mapped to the appropriate object attributes within the knowledge base. Integration with external configuration systems allows for parameter loading prior to parsing, while robust error handling manages file access and malformed input to ensure reliable data transformation.

## Modules

- [`fuzzy_dl_owl2.fuzzyowl2.parser.owl2_parser`] — A specialized parser that interprets Fuzzy OWL 2 XML annotations and transforms them into a knowledge base and query objects using the pyparsing library.
- [`fuzzy_dl_owl2.fuzzyowl2.parser.owl2_xml_parser`] — A specialized parser converts FuzzyOWL2 XML annotations into corresponding Python data structures representing fuzzy logic elements.
