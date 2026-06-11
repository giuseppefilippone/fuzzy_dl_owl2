# Summary

An abstract base class that defines the structure for evaluating the satisfiability of fuzzy concepts within a fuzzy description logic system.

## Description

Extending the base `Query` interface, the software provides a foundational mechanism for determining the degree to which a fuzzy concept is satisfied. It supports two distinct operational modes: evaluating the general satisfiability of a concept or assessing how well a specific individual fulfills that concept. To maintain logical integrity, the implementation enforces a strict constraint that the input concept must be non-concrete, preventing the application of satisfiability checks on specific instances. By utilizing overloaded initialization methods, the design flexibly handles the presence or absence of an individual argument while storing the necessary components—such as the concept, individual, and objective expression—required for subsequent mixed-integer linear programming evaluations.
