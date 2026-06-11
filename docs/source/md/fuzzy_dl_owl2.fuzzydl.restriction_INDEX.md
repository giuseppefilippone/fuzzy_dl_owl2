# Summary

A framework for modeling fuzzy description logic restrictions that enforce constraints on roles, concepts, and specific individuals with varying degrees of certainty.

## Description

Universal constraints are handled by encapsulating a role, a target concept, and a degree threshold to ensure connected entities meet specific certainty levels. Value restrictions link roles to concrete individuals through a transformation into negated existential quantifications, effectively integrating crisp values into the fuzzy reasoning system. The architecture utilizes inheritance to share core functionality across different restriction types while supporting state preservation via object copying. String representations are generated to visualize logical syntax, enabling both full constraint display and simplified relationship views for downstream processing.

## Modules

- [`fuzzy_dl_owl2.fuzzydl.restriction.has_value_restriction`] — A fuzzy description logic restriction that enforces a specific individual value for a given role, represented internally as a negated existential quantification.
- [`fuzzy_dl_owl2.fuzzydl.restriction.restriction`] — Defines a data structure for modeling universal restrictions within a fuzzy description logic framework by combining a role, a target concept, and a specific degree threshold.
