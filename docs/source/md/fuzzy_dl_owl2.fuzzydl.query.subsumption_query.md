# Summary

An abstract base class for fuzzy subsumption queries, capturing the pair of concepts whose containment relationship is to be evaluated along with the fuzzy implication operator used to grade it.

## Description

Subsumption in fuzzy description logics is a matter of degree rather than a simple yes-or-no question, so a query must record not only the subsumed and subsumer concepts but also the specific fuzzy implication chosen to interpret the containment. **SubsumptionQuery** acts as the shared foundation for all such queries: it inherits from the generic `Query` abstraction and remains abstract itself, deliberately leaving the construction of the actual optimization problem to concrete subclasses. During construction it enforces a key semantic restriction — neither concept may be concrete, since subsumption is only well-defined between abstract concepts — and reports any violation through the central error-handling utility. Once validation passes, the two concepts, the implication operator type, and a placeholder for the objective expression are stored as instance state; that objective expression, initially unset, is expected to be populated by subclasses with a linear expression encoding the computed degree of subsumption within the mixed-integer linear programming framework that drives the reasoning engine.
