# Summary

Models a weighted hierarchical relationship between a role and its parent by associating a specific inclusion degree with the parent identifier.

## Description

Designed to support fuzzy logic reasoning, the software captures the extent to which a parent role is included within a specific hierarchy, moving beyond simple binary relationships. It encapsulates a string identifier for the parent entity alongside a floating-point value that quantifies the strength or probability of the inheritance link, typically constrained between zero and one. By providing direct access to these stored values, the logic allows external systems to evaluate complex role inheritance rules where relationships are graded rather than absolute. The absence of strict validation logic ensures flexibility for various input scenarios, relying on the calling context to enforce specific constraints on the degree or naming conventions.
