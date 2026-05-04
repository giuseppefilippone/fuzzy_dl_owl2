# Summary

Implements a fuzzy logic concept characterized by a triangular membership function to model linguistic variables within a specific domain.

## Description

The software models a specific type of fuzzy set where membership degrees follow a triangular shape, defined by a rising edge, a peak, and a falling edge. It enforces strict validation during initialization to ensure that the geometric parameters form a valid triangle and that the overall domain encompasses the active support interval. Membership evaluation relies on linear interpolation, calculating a value between zero and one based on where a specific input falls relative to the triangle's vertices. To support complex logical reasoning, the implementation delegates operations like negation, conjunction, and disjunction to a central operator handler, allowing these concepts to be combined within a broader fuzzy ontology framework.
