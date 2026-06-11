# Summary

A specialized parser for Fuzzy Description Logic that interprets textual definitions to construct a knowledge base and associated queries using the pyparsing library.

## Description

The software utilizes the `pyparsing` library to define a comprehensive grammar capable of interpreting a wide array of fuzzy logic constructs, including concepts, roles, modifiers, and axioms. Through a series of static callback methods, raw string tokens are transformed into domain-specific objects such as `Concept`, `Individual`, and `Degree` instances, effectively bridging the gap between textual syntax and an executable object model. The parsing logic enforces semantic validation and logic-specific constraints, ensuring that constructs like weighted sums or integral operators adhere to the mathematical rules of the selected fuzzy logic, whether it be Zadeh, Lukasiewicz, or classical. Ultimately, the process populates a central `KnowledgeBase` with the parsed domain model while simultaneously extracting and instantiating query objects that can be executed against the constructed model.
