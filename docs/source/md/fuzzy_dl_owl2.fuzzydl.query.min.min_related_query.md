# Summary

A specialized query mechanism that computes the minimum degree to which two individuals are related through a specific role within a fuzzy description logic knowledge base.

## Description

The software implements a logic for determining the minimum membership degree associated with a specific role assertion between two entities in a fuzzy ontology. By leveraging mixed-integer linear programming, the system constructs a concept representing the target relationship and integrates it into a cloned version of the provided knowledge base to prevent unintended side effects on the original data. During the optimization process, the logic adds specific assertions linking the primary individual to the constructed concept and its negation, thereby establishing constraints that drive the solver to find the lowest possible truth value for the relationship. The execution flow handles potential inconsistencies within the ontology gracefully, returning a specific status indicator rather than failing, while also managing dynamic blocking for concepts involving existential restrictions.
