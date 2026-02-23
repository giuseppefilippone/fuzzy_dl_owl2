# Summary

Implements a data structure for representing atomic assertions within a fuzzy description logic system by associating a concept with a minimum membership degree.

## Description

Software components within a fuzzy description logic system rely on this structure to model fundamental constraints where a specific concept must satisfy a minimum membership threshold. By associating a *Concept* instance with a *Degree* object, the implementation encapsulates the logical relationship between an entity and its required truth value. Accessor methods are provided to retrieve the concept's identifier and the specific degree value, enabling the evaluation of logical rules or constraints. Additionally, a string representation is generated to visualize the assertion in a human-readable format, displaying the concept and the associated degree enclosed in angle brackets.
