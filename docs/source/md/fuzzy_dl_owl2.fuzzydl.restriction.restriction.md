# Summary

A universal restriction in a fuzzy description logic system that enforces a minimum membership degree for a specific role and concept combination.

## Description

The software models a universal restriction within a logical framework by combining a specific role, a target concept, and a lower bound degree to define a constraint. It represents the condition that for all entities connected via the given role, they must belong to the specified concept with a certainty or membership level that meets or exceeds the provided degree. The implementation stores these three core components—role name, concept, and degree—and provides mechanisms to create independent copies of the restriction object to ensure data integrity during processing. String representations are generated to reflect the logical syntax, offering formats that either explicitly include the degree threshold or focus solely on the universal scope of the role and concept relationship.
