# Summary

A central configuration repository for a fuzzy description logic reasoning system that defines enumerations for logic operators, concept types, solver backends, and parsing keywords.

## Description

Standardizing the vocabulary and configuration options used throughout the application, the code defines a comprehensive set of enumerations to manage the complexity of fuzzy reasoning. It categorizes distinct logic constructs, such as t-norms, t-conorms, implication rules, and aggregation operators like OWA and Sugeno integrals, into specific types to ensure type safety and consistency during inference. To support the interpretation of domain-specific syntax, the definitions map reserved language keywords directly to `pyparsing` objects, facilitating the automated parsing of FuzzyDL commands. Furthermore, the configuration specifies computational backend settings, including supported Mixed-Integer Linear Programming solvers and variable domains, while also managing global constants for file paths and numerical limits.
