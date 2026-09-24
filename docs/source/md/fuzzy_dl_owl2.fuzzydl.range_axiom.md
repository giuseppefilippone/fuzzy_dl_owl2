# Summary

Defines a role range axiom for a fuzzy description-logic knowledge base, pairing a role name with the concept that restricts which individuals may appear as its values.

## Description

In description logics, a range axiom constrains the fillers of a role: whenever two individuals are connected through the given role, the target individual must be an instance of the specified concept. **RangeAxiom** captures exactly this constraint as a pair of values — the role's identifier, given as a plain string, and the Concept object describing the admissible set of individuals. The design is deliberately minimal: the constructor simply stores both inputs as instance attributes, performing no validation or reasoning of its own, because enforcement of the restriction is delegated to the reasoning engine that later consumes the knowledge base. As a result, the object serves as a lightweight, declarative building block that knowledge-base authors instantiate to state a typing constraint, leaving interpretation to the broader fuzzy DL machinery during consistency checking, classification, or query answering. Keeping the role as a bare string rather than a dedicated role object reinforces its nature as a simple data carrier within the larger fuzzydl package, where concepts carry the expressive structure and axioms merely record the relationships between them.
