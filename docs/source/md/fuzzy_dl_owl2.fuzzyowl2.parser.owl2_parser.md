# Summary

A parser implementation that interprets Fuzzy OWL 2 annotation strings and transforms them into structured KnowledgeBase and Query objects using the pyparsing library.

## Description

The software constructs a comprehensive grammar using the pyparsing library to recognize and interpret the syntax of Fuzzy OWL 2 annotations, which include complex fuzzy logic operators, modifiers, and data types. It defines a set of parsing actions that transform raw token streams into specific domain objects, such as modified concepts, weighted aggregations, and various fuzzy datatype functions like triangular or trapezoidal shapes. The central class orchestrates the parsing process by enabling left recursion to handle nested concept definitions and managing the conversion of these definitions into a KnowledgeBase and a list of Query instances. Error handling and configuration loading are integrated into the main execution flow to ensure robust processing of input strings and proper initialization of the underlying reasoning system.
