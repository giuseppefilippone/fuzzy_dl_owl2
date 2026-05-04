# Summary

Encapsulates mathematical inequalities of the form expression compared to zero for use in fuzzy description logic ontologies.

## Description

The software models linear constraints by pairing a mathematical expression with a relational operator, ensuring the right-hand side is always normalized to zero. It supports the creation of greater-than, less-than, and equality constraints through static factory methods, which simplify the instantiation process by automatically assigning the appropriate operator type. Internally, the logic delegates term and constant retrieval to the encapsulated expression object while providing mechanisms to clone the inequality and check if the expression evaluates to zero. Standard object behaviors such as hashing, equality comparison, and string representation are implemented to facilitate the use of these constraints within sets, dictionaries, and debugging workflows.
