# Summary

Defines a data structure for representing fuzzy General Concept Inclusion axioms, which assert that one concept is subsumed by another to a specific degree of truth using a designated logic operator.

## Description

The implementation models a graded subsumption relationship where a specific concept is included within a broader category according to a defined truth value and fuzzy implication operator. By storing references to the subsumer, subsumed concept, degree, and operator type, the structure allows for the dynamic modification of these components through setter methods, making the underlying axiom mutable during runtime. Equality comparisons are determined by verifying that all constituent attributes match exactly between instances, while ordering comparisons rely on hash values to provide a consistent but arbitrary sorting mechanism. A string representation is generated to display the logical structure in a human-readable format, combining the concepts, operator type, and degree into a standard notation.
