# Summary

A minimal value object that binds a property name to its associated fuzzy modifier so the pair can travel together when expressing fuzzy axioms in the FuzzyOWL2 ontology framework.

## Description

PropertyDefinition acts as a fundamental building block for fuzzy logic constraints by capturing the two pieces of information needed to attach a linguistic hedge to an object or data property: the modifier itself and the name of the property it applies to. Bundling these values into a single unit simplifies downstream code, since any component that constructs fuzzy axioms can retrieve both elements through dedicated getter methods rather than juggling loose strings. The design is deliberately minimal and defensive: the constructor performs no validation and simply stores the two strings in private attributes, while the absence of setter methods means instances effectively behave as immutable records once created. This immutability makes objects safe to pass around and reuse, and the getter-only interface preserves encapsulation by keeping the underlying attribute names hidden from callers. In practice, consumers instantiate the class with a modifier such as a linguistic hedge and a property name, then read both values back when translating fuzzy restrictions into concrete ontology axioms.
