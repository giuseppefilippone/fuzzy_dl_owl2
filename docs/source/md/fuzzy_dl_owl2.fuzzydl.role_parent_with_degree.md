# Summary

A lightweight value class that pairs a parent role's name with a numeric inclusion degree, representing weighted relationships in a fuzzy description-logic role hierarchy.

## Description

Role hierarchies in fuzzy description logics are rarely all-or-nothing: a role may subsume its parent only to some extent, so the knowledge base needs a way to record both the identity of the parent and the strength of that relationship. The `RoleParentWithDegree` class provides exactly that pairing, holding a string identifier for the parent role alongside a floating-point degree that typically lies between 0 and 1 and expresses the probability or weight of the inclusion. The design is deliberately minimal: the constructor stores its two arguments directly as instance attributes without any validation, and a pair of simple getter methods exposes them afterwards, leaving the object as a passive data carrier with no behaviour of its own. Because it imposes no constraints on its inputs, callers are trusted to supply well-formed names and degrees, which keeps the class cheap to construct and suitable for use deep inside the engine's role-inheritance machinery, where many such weighted links may be created and inspected during reasoning.
