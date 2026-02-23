# Summary

A specialized parser for Fuzzy Description Logic that interprets textual input to construct a knowledge base and a set of executable queries using the pyparsing library.

## Description

The software defines a comprehensive grammar for a Fuzzy Description Logic language, enabling the interpretation of complex constructs such as fuzzy concepts, modifiers, roles, and axioms. It utilizes the pyparsing library to define syntax rules and parse actions that transform raw string tokens into domain-specific objects, including concepts, individuals, and various query types. During the parsing process, the system validates semantic constraints, such as ensuring abstract concepts are not used where concrete ones are required and enforcing logic-specific rules for operators like conjunction and implication. The parser populates a central `KnowledgeBase` instance with the interpreted data and accumulates a list of queries, which can subsequently be solved to perform reasoning tasks like subsumption checking, instance retrieval, and satisfiability analysis. By supporting multiple fuzzy logic semantics, including Zadeh and Lukasiewicz, the implementation provides a flexible framework for defining and reasoning about fuzzy ontologies.
