# Summary

A Python class representing logical conjunctions, disjunctions, and negations within a fuzzy description logic framework, supporting various semantics and normalization techniques.

## Description

It serves as the core mechanism for constructing and manipulating complex logical expressions by extending the base `Concept` class to handle binary operations like AND and OR, as well as unary negation, across different fuzzy logic systems such as classical, Łukasiewicz, and Gödel. The implementation utilizes static factory methods to instantiate operator nodes, automatically selecting the appropriate semantic variant based on global configuration while flattening nested structures to maintain a canonical form. Beyond simple construction, the logic includes sophisticated algorithms for expression simplification, applying De Morgan's laws, eliminating double negations, distributing operators, and reducing quantifiers to transform expressions into Conjunctive or Disjunctive Normal Forms. To facilitate natural usage, the class overloads standard bitwise operators for conjunction, disjunction, and negation, allowing developers to write intuitive logical expressions while the underlying system handles the complexities of fuzzy logic algebraic rules.
