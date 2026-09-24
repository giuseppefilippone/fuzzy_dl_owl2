# Summary

Defines a fuzzy nominal concept that binds a named ontology individual to a graded degree of membership, extending the FuzzyOWL2 concept-definition hierarchy.

## Description

In fuzzy ontologies, membership in a concept is not an all-or-nothing affair: an individual may belong to a concept only to some graded extent. **FuzzyNominalConcept** captures exactly such an assertion by storing a floating-point degree alongside the identifier of the individual involved, making it possible to express statements like "John is Tall to degree 0.7" within the FuzzyOWL2 framework. It derives from the shared ConceptDefinition base and registers itself under the FUZZY_NOMINAL concept type, which lets the surrounding ontology machinery distinguish these graded individual assertions from other kinds of fuzzy concepts during processing and serialisation. The design is deliberately minimal and value-like: the degree and the individual's name are held as private attributes exposed through simple, side-effect-free accessors, with no validation or computation performed beyond the type registration required by the superclass. A human-readable rendering of the pair as a parenthesised "(degree individual)" string is provided for display and logging, rounding out a small, effectively immutable data carrier rather than a behaviour-rich component.
