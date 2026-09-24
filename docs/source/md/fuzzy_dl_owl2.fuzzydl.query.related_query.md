# Summary

An abstract query type that captures the shared structure needed to evaluate how strongly a role assertion holds between two individuals in a fuzzy description-logic knowledge base.

## Description

Sitting beneath the generic `Query` abstraction, `RelatedQuery` provides the common foundation for concrete query implementations that compute the minimum or maximum degree of membership of a relation between individuals. Rather than performing any evaluation itself, it declares and stores the four ingredients such queries require: the abstract role (the relation type being examined), the subject individual, the object individual, and an objective expression representing the degree of membership to be optimised. The constructor deliberately initialises every one of these attributes to `None`, keeping the class purely structural and signalling that subclasses must populate the state before the query can be meaningfully processed. By standardising these parameters up front, the design guarantees that all role-entailment queries share a uniform shape, allowing the reasoning engine to route them through a single code path once the underlying mixed-integer linear programming machinery resolves the objective expression.
