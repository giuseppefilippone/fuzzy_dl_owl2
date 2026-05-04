# Summary

Defines a data structure for representing primitive concept definitions within a fuzzy description logic system.

## Description

The software models a specific type of axiom where a named concept is defined by a complex description using a fuzzy implication. It encapsulates the logical relationship by storing the identifier of the concept being defined, the complex concept expression acting as the definition, the specific fuzzy logic operator (such as Łukasiewicz or Gödel) used to interpret the implication, and a floating-point degree representing the lower bound of truth. To manage these logical constraints, the implementation provides standard accessor and mutator methods for retrieving and modifying the definition and its associated truth degree, alongside a cloning utility to generate independent copies of the instance. The design also supports structural comparison and ordering by implementing equality and relational operators based on the hash of the object's string representation, allowing the definitions to be sorted or used as keys in collections for efficient knowledge base management.
