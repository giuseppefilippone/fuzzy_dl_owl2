# Summary

A query mechanism that determines the minimum membership degree of a role relationship between two individuals within a fuzzy ontology using mixed-integer linear programming.

## Description

The software implements a specific type of fuzzy description logic query designed to compute the minimum truth value associated with a role assertion between two distinct individuals. By leveraging mixed-integer linear programming, the logic constructs a mathematical model where the objective is to minimize the degree to which the first individual participates in a specific role with the second individual. To ensure the integrity of the original data, the process operates on a cloned version of the provided knowledge base, thereby preventing unintended side effects during the optimization phase. The implementation dynamically generates necessary constraints and assertions, such as those involving negation and existential restrictions, before invoking the solver to derive the final result. Error handling mechanisms are integrated to gracefully manage scenarios where the underlying ontology is found to be inconsistent, returning a specific status rather than failing abruptly.
