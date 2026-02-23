# Summary

Centralizes the definition of fuzzy concept types and parsing keywords required for processing the FuzzyOWL2 ontology language.

## Description

The `ConceptType` enumeration categorizes various fuzzy logic constructs, such as aggregation operators and weighted operations, serving as a type discriminator to ensure correct semantic application during ontology manipulation. Complementing this, the `FuzzyOWL2Keyword` enumeration maps the specific vocabulary of the FuzzyOWL2 syntax—including logic operators, comparison symbols, and structural tags—to their corresponding `pyparsing` objects. By encapsulating parser definitions within an enumeration, the codebase avoids scattered string literals and provides a robust mechanism for token identification. Custom equality overrides further enhance usability by allowing comparisons against raw strings or parser objects directly, ensuring that the parsing logic remains both readable and maintainable.
