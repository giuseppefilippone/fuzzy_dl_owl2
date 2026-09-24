# Summary

A lightweight value object that models a universal role restriction in a fuzzy description logic, storing a role name, a target concept, and the minimum membership degree that the restriction imposes.

## Description

The `Restriction` class encodes the fuzzy analogue of the classical ∀R.C construct: every individual connected through the given role must belong to the specified concept with a degree of at least the stored threshold. Its three components — the role name, the `Concept` being restricted to, and the lower-bound `Degree` — are held as plain attributes and exposed through trivial getters, so the type serves purely as a carrier of data rather than as an active participant in reasoning. A cloning operation yields a fresh instance that shares the same concept and degree references, a deliberate shallow-copy choice that keeps duplication cheap while relying on those collaborators being treated as immutable. Human-readable rendering comes in two flavours: a degree-free form, `(all role concept)`, matching the concrete syntax used by the fuzzydl reasoner when the threshold is irrelevant, and a full form that appends `>= degree` to make the minimum-membership condition explicit; the official representation simply delegates to the informal string form so that debug output and user-facing output remain consistent.
