# Summary

A minimal value object representing an atomic fuzzy assertion, namely that an atomic concept must hold with a membership degree greater than or equal to a given threshold.

## Description

The **AtomicAssertion** class is one of the elementary building blocks of a fuzzy description logic knowledge base: it pairs a `Concept` with a `Degree` and expresses the constraint that the concept's membership is at least that degree. The design is deliberately kept as a plain, declarative container — the constructor simply stores the two components, and the only behaviour offered is read-only access to the concept's name and the stored degree, with no validation, mutation, or evaluation logic of any kind. All actual reasoning about whether such a constraint is satisfied is delegated to other parts of the fuzzy DL engine, which keeps the assertion cheap to create, inspect, and print. A human-readable string rendering that wraps the concept and its degree in angle brackets makes individual assertions easy to trace when debugging or logging the contents of a knowledge base.
