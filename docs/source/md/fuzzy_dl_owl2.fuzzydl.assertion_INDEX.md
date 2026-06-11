# Summary

A framework for modeling fuzzy logic constraints that enforce minimum membership thresholds for individuals and concepts.

## Description

The implementation provides structures to encapsulate logical expressions where specific entities or categories must satisfy defined degrees of membership. By distinguishing between constraints applied to individual subjects and those applied to atomic concepts, the architecture supports a comprehensive representation of fuzzy logic rules. Components within the system allow for the dynamic modification and cloning of these constraints, facilitating complex reasoning processes. Furthermore, the design incorporates specialized comparison logic that evaluates equivalence based on the strength of the membership degree, enabling the ordering and management of fuzzy assertions.

## Modules

- [`fuzzy_dl_owl2.fuzzydl.assertion.assertion`] — Models a fuzzy logic constraint stating that an individual belongs to a concept with a minimum degree of membership.
- [`fuzzy_dl_owl2.fuzzydl.assertion.atomic_assertion`] — A class representing a fundamental fuzzy logic constraint that links a specific concept to a minimum membership degree threshold.
