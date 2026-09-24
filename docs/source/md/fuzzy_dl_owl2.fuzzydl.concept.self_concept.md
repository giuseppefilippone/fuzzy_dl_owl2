# Summary

A fuzzy description-logic concept expressing local reflexivity, where an individual belongs to the concept exactly when it stands in a given role relationship with itself.

## Description

`SelfConcept` captures the OWL 2-style self-construct within a fuzzy description-logic framework, making it possible to state properties such as "someone who knows themself" by tying concept membership to a role that an individual must fulfil with itself. The class inherits from both the abstract `Concept` hierarchy and `HasRoleInterface`, so it combines standard concept behaviour — a `ConceptType.SELF` type tag, a canonical name of the form "(self role)", and role-reporting support — with a deliberately simple construction path, since a bare role string is enough whether one uses the constructor or the static factory method. Cloning yields a fresh, independent instance carrying the same role, and because every operation returns new objects rather than mutating existing ones, instances effectively behave as immutable building blocks for larger expressions.

The concept is intentionally treated as an atomic leaf node: decomposing it into atomic concepts yields only itself, and any substitution attempt returns it unchanged, since it has no internal structure to rewrite. Overloaded operators for negation, conjunction, and disjunction delegate to `OperatorConcept`, allowing self-concepts to be woven into arbitrarily complex fuzzy expressions using natural Python syntax (`-`, `&`, and `|`). Hashing follows object identity rather than the string representation — the structural-hash alternative survives only as a comment — so two structurally identical self-concepts over the same role remain distinct entries in sets and dictionaries.
