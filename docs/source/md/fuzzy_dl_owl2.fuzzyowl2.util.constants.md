# Summary

Establishes a centralized vocabulary of fuzzy logic concept types and parsing tokens for the FuzzyOWL2 framework.

## Description

The `ConceptType` enumeration categorizes various fuzzy constructs, such as aggregation operators like Sugeno and Choquet integrals, alongside weighted operations and structural modifications, acting as a type discriminator to ensure correct semantic application during ontology processing. Simultaneously, the `FuzzyOWL2Keyword` class maps specific language tokens—including logic operators, modifiers, and XML-like tags—to their corresponding `pyparsing` definitions, effectively bridging the gap between the abstract syntax of the fuzzy ontology language and the concrete parsing logic required to process it. By encapsulating parser objects within an enumeration, the design provides a single source of truth for grammar definitions while offering utility methods to normalize string representations and handle flexible equality comparisons. These constants serve as foundational building blocks for the broader system, allowing other components to reference fuzzy logic operators and structural elements reliably without hardcoding string literals or parser definitions throughout the codebase.
