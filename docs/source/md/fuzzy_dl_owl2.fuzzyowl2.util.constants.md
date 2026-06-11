# Summary

Centralizes the definition of fuzzy concept types and parsing keywords for the FuzzyOWL2 framework.

## Description

The `ConceptType` enumeration categorizes various fuzzy logic constructs, such as aggregation operators like Sugeno and Choquet integrals or weighted operations, providing string-based identifiers that act as type discriminators during ontology processing. Complementing this, the `FuzzyOWL2Keyword` enumeration maps the specific vocabulary of the FuzzyOWL2 language—including XML-like tags, logic operators, and comparison symbols—to their corresponding `pyparsing` definitions to support grammar construction and syntax validation. This class includes utility methods for normalizing token names and retrieving underlying parser objects, while also overriding equality comparisons to allow flexible matching against raw strings or other parser elements. Together, these enumerations establish a standardized vocabulary and type system that ensures consistent interpretation of fuzzy semantics across the broader application.
