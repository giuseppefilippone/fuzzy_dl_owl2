# Summary

A right-shoulder fuzzy concrete concept whose membership degree ramps linearly from zero to one across a transition interval, modelling linguistic terms that become fully true once a quantity grows sufficiently large.

## Description

RightConcreteConcept specialises the generic FuzzyConcreteConcept to express ideas such as "high temperature" or "large size", where the degree of truth increases as the underlying value grows. Construction is defensive: the domain interval [k1, k2] must completely contain the transition interval [a, b], and any violation of the ordering constraints is rejected through the shared error utility, guaranteeing that an ill-formed membership function can never silently exist. Evaluation is stateless and deliberately simple — values at or below the left breakpoint score zero, values at or beyond the right breakpoint score one, and intermediate values are interpolated proportionally — producing the characteristic rising ramp. The breakpoints are exposed as float-coercing properties, and a clone operation yields independent copies, which matters because fuzzy concepts are routinely shared and recombined during reasoning.

Integration with the wider fuzzy description-logic machinery is achieved through operator overloading: negation, conjunction, and disjunction all delegate to OperatorConcept, so concepts compose naturally with Python's `-`, `&`, and `|` syntax while the operands themselves remain unmodified. Hashing is derived from the numeric parameters rather than object identity, allowing structurally identical concepts to be deduplicated in sets and dictionaries, and a canonical "right-shoulder(k1, k2, a, b)" string is generated for naming and display purposes.
