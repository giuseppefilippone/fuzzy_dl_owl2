# Summary

Defines a fuzzy description-logic restriction that ties a role to one specific named individual, requiring the association to hold with at least a given degree of truth.

## Description

HasValueRestriction specialises the generic Restriction abstraction for the case where a role's filler is a concrete individual rather than a concept expression, so the constructor forwards `None` as the concept filler to the parent and keeps the individual's name in its own attribute, which is exposed through a simple getter for use by parsers, simplifiers, and other reasoning components. The accompanying `Degree` object encodes the lower bound on the truth degree, which is what distinguishes the fuzzy variant from a classical "has value" (nominal filler) restriction. When a textual rendering without the degree is requested, the restriction is deliberately formatted as a negated existential — `(not (b-some role individual))` — in the Lisp-like syntax consumed by the underlying reasoning engine. That encoding lets the reasoner normalise and reason about the value restriction uniformly alongside other quantified expressions, avoiding a dedicated code path for nominal fillers. The overall design is intentionally minimal: the object acts as a plain carrier of role name, individual name, and degree, with all heavier behaviour inherited from the shared Restriction machinery.
