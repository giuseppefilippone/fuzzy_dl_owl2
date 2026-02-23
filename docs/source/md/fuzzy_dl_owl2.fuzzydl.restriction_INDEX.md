# Summary

Implements fuzzy description logic restrictions that enforce constraints on roles and concepts using specific membership degrees.

## Description

Logic constraints within a fuzzy framework are modeled by combining roles, concepts, and degree thresholds to define specific relationships. A universal restriction ensures that for all entities connected via a given role, they belong to a specified concept with a certainty meeting a lower bound degree. Another type of constraint enforces that a specific role must be associated with a particular individual, using a fuzzy degree to represent the strength of this association. These components utilize a common base structure to manage attributes like role names and degrees while translating logical assertions into formatted string expressions suitable for integration into broader reasoning tasks.

## Modules

- [`fuzzy_dl_owl2.fuzzydl.restriction.has_value_restriction`](./fuzzydl_restriction_has_value_restriction.md) — A fuzzy description logic restriction that enforces a specific value for a given role, constrained by a degree of membership.
- [`fuzzy_dl_owl2.fuzzydl.restriction.restriction`](./fuzzydl_restriction_restriction.md) — A class representing a universal restriction that combines a role, a concept, and a degree threshold within a fuzzy logic framework.
