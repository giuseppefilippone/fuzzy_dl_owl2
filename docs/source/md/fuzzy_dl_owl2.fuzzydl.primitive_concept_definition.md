# Summary

A Python class representing a primitive concept definition within a fuzzy description logic system, encapsulating a named concept, its defining description, a truth degree, and a specific implication operator.

## Description

The software models a specific type of fuzzy logic axiom that defines a primitive concept through a complex description, governed by a fuzzy implication operator such as Łukasiewicz or Gödel. It captures the relationship between a named concept and its definition alongside a numerical degree representing the lower bound of truth, which is essential for reasoning under uncertainty. Design choices include providing full mutability for the definition and degree attributes while offering a cloning mechanism to create independent copies of the axiom. To facilitate storage and comparison within data structures like sets or dictionaries, the implementation overrides standard magic methods to determine equality and ordering based on the string representation of the logical rule.
