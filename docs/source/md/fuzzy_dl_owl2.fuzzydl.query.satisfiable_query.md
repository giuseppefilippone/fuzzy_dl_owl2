# Summary

An abstract base class, **SatisfiableQuery**, that prepares fuzzy satisfiability queries by validating and storing a fuzzy concept, an optional individual, and a placeholder objective expression for later minimum/maximum satisfiability evaluation.

## Description

SatisfiableQuery extends the generic Query abstraction to provide the shared foundation for minimum and maximum satisfiability checks in a fuzzy description-logic setting. Its role is to capture the common inputs of such queries — a fuzzy concept and an optional individual — while deferring the actual solving logic to concrete subclasses, which determine the bounds or the extent to which the concept is fulfilled. Because satisfiability is only meaningful for abstract concepts, initialization rejects concrete concepts with an error message, guaranteeing that only valid fuzzy concepts proceed to the reasoning stage.

The constructor emulates Java-style constructor overloading: `typing.overload` declarations advertise two accepted signatures (a concept alone, or a concept paired with an individual), while the variadic implementation checks the argument count and types through assertions before delegating to a private initializer. The single-argument path deliberately invokes that private two-argument initializer with `None` rather than re-entering `__init__`, mirroring Java's `this(c, null)` idiom and preventing virtual dispatch into subclass constructors whose two-argument branch might reject `None`. Once initialized, the query holds the concept, the optional individual, and a `None`-valued objective expression drawn from the MILP layer, which concrete subclasses are expected to populate when the query is compiled into an optimization problem.
