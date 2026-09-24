# Summary

A small value class that models a named attribute of an individual in a fuzzy description-logic knowledge base, inferring its data type — string, boolean, integer, or real — and its optional numeric range from the constructor arguments.

## Description

ConcreteFeature is the single abstraction involved: it pairs a feature name with a `ConcreteFeatureType` and, when the feature is numeric, lower and upper bounds. The type is never declared explicitly; instead it is derived at construction time from the shape of the arguments, so a lone name produces a string feature, a name plus a boolean flag produces a boolean feature, and a name plus two numbers produces an integer or real feature depending on whether the bounds are integers or floats. To make these calling conventions statically checkable, the constructor is declared with `typing.overload` stubs while the actual implementation inspects the variadic arguments at runtime and delegates to one of four private initialisation helpers, raising `TypeError` or `ValueError` when no accepted signature matches. The result is a single public constructor that still enforces argument correctness, though it deliberately does not verify that the lower bound precedes the upper bound, leaving such ordering concerns to callers.

Instances are mutable by design: simple accessors and mutators expose the name, the type, and the numeric range, allowing a feature's classification or bounds to be refined after creation, and a clone method produces an independent copy by replaying the constructor signature that corresponds to the current type. Both the repr and str forms collapse to the feature's name, so features render as plain identifiers in debugging output and in any generated knowledge-base text.
