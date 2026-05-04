# Summary

A class representing a concept modified by a numerical weight within a fuzzy description logic framework.

## Description

The implementation models a logical construct where a specific concept is qualified by a numerical value, typically representing importance or relevance in a fuzzy logic context. By inheriting from a base concept class and utilizing an interface for holding nested concepts, the design allows the object to act as a wrapper that preserves the structure of the underlying logic while adding a quantitative modifier. Structural queries, such as retrieving atomic concepts or roles, are delegated directly to the encapsulated concept, ensuring that the wrapper does not obscure the internal details of the logic it modifies. Furthermore, the class supports standard logical operations like negation, conjunction, and disjunction through operator overloading, enabling these weighted constructs to participate seamlessly in complex logical expressions.
