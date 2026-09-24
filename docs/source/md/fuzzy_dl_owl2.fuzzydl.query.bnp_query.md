# Summary

A specialised query that defuzzifies a triangular fuzzy number by computing its **best non-fuzzy performance (BNP)**, i.e. the crisp value holding the highest degree of membership in the fuzzy set.

## Description

The `BnpQuery` class plugs into the query framework of a fuzzy description-logic reasoner, but unlike typical queries it performs no reasoning over the knowledge base whatsoever. Instead, it acts as a thin adapter around a `TriangularFuzzyNumber`, delegating the actual defuzzification to that number, which itself knows how to derive its representative crisp value. The knowledge base parameter is accepted purely to satisfy the uniform preprocessing and solving interface shared by all query types, and the preprocessing step is deliberately a no-op since no schema resolution or execution planning is required. The resulting value is wrapped in a `Solution` object so that it flows through the same result channel as the outputs of every other query, allowing callers to handle it without special-casing. A human-readable string representation is also provided for reporting purposes, producing a label of the form "Best non-fuzzy performance of *name* = " that callers can append the numeric result to. This design keeps defuzzification consistent with the broader query pipeline while leaving the calculation logic entirely encapsulated within the fuzzy number itself.
