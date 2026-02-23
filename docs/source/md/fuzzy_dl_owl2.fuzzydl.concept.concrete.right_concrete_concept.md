# Summary

Implements a right-shoulder fuzzy membership function where truth values increase linearly from zero to one over a specified interval.

## Description

The implementation models concepts that become increasingly true as a variable grows, such as "high temperature," by defining a geometric shape where membership is zero up to a certain point, ramps up linearly, and then stays at one. It enforces strict ordering constraints during initialization to ensure the domain boundaries correctly encapsulate the transition interval, preventing invalid logical states. By overriding standard Python operators, the class seamlessly integrates with a larger fuzzy logic framework to support negation, conjunction, and disjunction operations. Additional utility features include the ability to generate string representations, clone instances to preserve state, and compute hash values for use in collections.
