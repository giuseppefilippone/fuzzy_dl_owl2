# Summary

An abstract base class that anchors the hierarchy of fuzzy concept definitions in the FuzzyOWL2 framework by tagging each definition with a `ConceptType` and exposing that tag through a common interface.

## Description

`ConceptDefinition` is the root abstraction for all fuzzy concept definitions, and it is declared abstract so that it can never be instantiated on its own — every usable definition must come from a concrete subclass modelling a particular kind of fuzzy concept. Its design rests on a simple type-tag pattern: at construction time each definition receives a `ConceptType` value recording its category, that value is stored privately and never changed afterwards, and a single accessor exposes it to the rest of the system. This lets other components, such as the ontology serialiser or the fuzzy reasoner, handle arbitrary concept definitions uniformly, querying what kind of concept they are looking at without needing to know its concrete class and dispatching accordingly. The only additional behaviour is a deliberate convenience in which the formal, debugging-oriented string representation simply delegates to the informal one, guaranteeing that both forms of output always agree. The minimalism is intentional — the abstraction exists to impose a shared contract on the hierarchy while leaving every aspect of concept-specific semantics to the subclasses.
